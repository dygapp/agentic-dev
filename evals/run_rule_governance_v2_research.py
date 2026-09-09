#!/usr/bin/env python3
"""规则治理 v2 研究评估 runner。

目标：
- 用完全相同的架构评估命题分别运行不同模型；
- 用独立 Fresh Codex exec 运行当前 v1 生成阶段基线场景；
- 每次运行使用隔离仓库副本，避免后一模型读取前一模型的结果；
- 保存 provider model / reasoning effort 可观察事实；
- 不自动把模型输出判定为架构事实或 Eval PASS。

本文件只属于 evals/ 研究资产，不修改正式 Method / Guide / Skill。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

from run_codex_evals import check_codex
from run_rule_retrieval_c3 import (
    extract_thread_id,
    parse_runtime_facts,
    sanitize_persisted_stderr,
)

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals" / "rule-governance-v2"
PROMPT_FILE = EVAL_DIR / "evaluation-prompt.md"
SCENARIO_DIR = EVAL_DIR / "scenarios"
RESULTS = ROOT / "evals" / "results" / "rule-governance-v2"
RUNTIME_FACTS_SOURCE = "codex-exec-sse-provider-model+turn-span-reasoning-effort"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value)


def git_text(*args: str) -> str | None:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        return None
    return completed.stdout.strip()


def source_repository_facts() -> dict[str, Any]:
    return {
        "head": git_text("rev-parse", "HEAD"),
        "branch": git_text("branch", "--show-current"),
        "status_porcelain": git_text("status", "--porcelain"),
    }


def validate_assets() -> list[str]:
    errors: list[str] = []
    required = [PROMPT_FILE, EVAL_DIR / "README.md", EVAL_DIR / "rubric.md"]
    for path in required:
        if not path.is_file():
            errors.append(f"缺少评估资产：{path.relative_to(ROOT)}")

    scenarios = sorted(SCENARIO_DIR.glob("*.md")) if SCENARIO_DIR.is_dir() else []
    expected = {
        "01-technical-design",
        "02-specification-analysis",
        "03-code-generation",
        "04-debug-verification",
        "05-consumer-fresh-context",
    }
    actual = {path.stem for path in scenarios}
    if actual != expected:
        errors.append(
            "场景集合不完整："
            f"expected={sorted(expected)} actual={sorted(actual)}"
        )

    if PROMPT_FILE.is_file():
        prompt = PROMPT_FILE.read_text(encoding="utf-8")
        for marker in (
            "A — Runtime Rule Index",
            "B — Guide Decomposition + Metadata",
            "C — Guide Rule Reduction + Existing Skill Ownership",
            "D — 新增专项 Skill",
            "E — 混合方案",
            "F — KEEP V1",
            "Consumer-local",
            "GO — 可以进入有限 v2 Milestone",
        ):
            if marker not in prompt:
                errors.append(f"evaluation-prompt 缺少关键命题：{marker}")

    return errors


def ignore_runtime_artifacts(path: str, names: list[str]) -> set[str]:
    """复制工作区时只排除会泄漏前序运行结果或无意义缓存的本地资产。"""
    current = Path(path).resolve()
    ignored: set[str] = set()
    try:
        relative = current.relative_to(ROOT)
    except ValueError:
        return ignored

    if relative == Path("evals"):
        ignored.update(name for name in names if name in {"results", "workspace"})
    ignored.update(name for name in names if name == "__pycache__")
    ignored.update(name for name in names if name.endswith(".pyc"))
    return ignored


def prepare_isolated_repository(parent: Path) -> Path:
    workspace = parent / "repository"
    shutil.copytree(ROOT, workspace, ignore=ignore_runtime_artifacts)
    return workspace


def extract_final_agent_text(jsonl_text: str) -> str | None:
    messages: list[str] = []
    for line in jsonl_text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        if event.get("type") != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict):
            continue
        if item.get("type") not in {"agent_message", "message"}:
            continue
        text = item.get("text")
        if isinstance(text, str) and text.strip():
            messages.append(text.strip())
            continue
        content = item.get("content")
        if isinstance(content, list):
            parts: list[str] = []
            for part in content:
                if isinstance(part, dict) and isinstance(part.get("text"), str):
                    parts.append(part["text"])
            if parts:
                messages.append("\n".join(parts).strip())

    return messages[-1] if messages else None


def extract_usage(jsonl_text: str) -> dict[str, Any] | None:
    latest: dict[str, Any] | None = None
    for line in jsonl_text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") != "turn.completed":
            continue
        usage = event.get("usage")
        if isinstance(usage, dict):
            latest = usage
    return latest


def case_prompt(case_id: str) -> tuple[str, str]:
    if case_id == "architecture":
        path = PROMPT_FILE
    else:
        path = SCENARIO_DIR / f"{case_id}.md"
    if not path.is_file():
        raise RuntimeError(f"未知评估 case：{case_id}")
    return path.read_text(encoding="utf-8"), str(path.relative_to(ROOT))


def selected_cases(case_group: str, scenarios: list[str] | None) -> list[str]:
    available = [path.stem for path in sorted(SCENARIO_DIR.glob("*.md"))]
    if scenarios:
        unknown = sorted(set(scenarios) - set(available))
        if unknown:
            raise RuntimeError(f"未知场景：{', '.join(unknown)}")
        return scenarios
    if case_group == "architecture":
        return ["architecture"]
    if case_group == "scenarios":
        return available
    return ["architecture", *available]


def run_one(
    *,
    codex_bin: str,
    case_id: str,
    model: str,
    reasoning_effort: str,
) -> int:
    prompt, prompt_source = case_prompt(case_id)
    model_dir = RESULTS / safe_name(model)
    case_dir = model_dir / case_id
    case_dir.mkdir(parents=True, exist_ok=True)

    facts_before = source_repository_facts()

    with tempfile.TemporaryDirectory(prefix=f"agentic-dev-rgv2-{case_id}-") as temp_dir:
        temp = Path(temp_dir)
        workspace = prepare_isolated_repository(temp)
        log_dir = temp / "codex-log"
        log_dir.mkdir(parents=True, exist_ok=True)

        command = [
            codex_bin,
            "exec",
            "--ephemeral",
            "--json",
            "--sandbox",
            "read-only",
            "--model",
            model,
            "--config",
            f'model_reasoning_effort="{reasoning_effort}"',
            "--config",
            f'log_dir="{log_dir}"',
            "--config",
            'approval_policy="never"',
            "--config",
            'web_search="disabled"',
            "-C",
            str(workspace),
            prompt,
        ]

        runtime_env = os.environ.copy()
        runtime_env["PWD"] = str(workspace)
        runtime_env["RUST_LOG"] = "error,codex_core=info,codex_api::sse::responses=trace"
        runtime_env.pop("OLDPWD", None)
        for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"):
            runtime_env.pop(key, None)

        print(f"[{case_id}] model={model} effort={reasoning_effort}")
        started = time.monotonic_ns()
        completed = subprocess.run(
            command,
            cwd=workspace,
            env=runtime_env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        elapsed_ms = (time.monotonic_ns() - started) // 1_000_000

        runtime_log = log_dir / "codex-tui.log"
        trace_parts = [completed.stderr]
        trace_sources = ["stderr"]
        if runtime_log.is_file():
            trace_parts.append(runtime_log.read_text(encoding="utf-8", errors="replace"))
            trace_sources.append("isolated-log-dir")
        trace_text = "\n".join(trace_parts)

        thread_id = extract_thread_id(completed.stdout)
        runtime_facts = parse_runtime_facts(trace_text, thread_id)
        final_text = extract_final_agent_text(completed.stdout)
        usage = extract_usage(completed.stdout)

        (case_dir / "run.jsonl").write_text(completed.stdout, encoding="utf-8")
        (case_dir / "stderr.txt").write_text(
            sanitize_persisted_stderr(completed.stderr),
            encoding="utf-8",
        )
        if final_text is not None:
            (case_dir / "final.md").write_text(final_text + "\n", encoding="utf-8")

        runtime_record = {
            "thread_id": thread_id,
            "sources": trace_sources,
            "status": runtime_facts["status"],
            "provider_models": runtime_facts["provider_models"],
            "client_turn_models": runtime_facts["turn_models"],
            "turn_reasoning_efforts": runtime_facts["turn_reasoning_efforts"],
        }
        (case_dir / "runtime-facts.json").write_text(
            json.dumps(runtime_record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        metadata = {
            "case_id": case_id,
            "prompt_source": prompt_source,
            "prompt_sha256": sha256_text(prompt),
            "requested_model": model,
            "requested_reasoning_effort": reasoning_effort,
            "provider_model": runtime_facts["model"],
            "client_turn_model": runtime_facts["client_turn_model"],
            "observed_reasoning_effort": runtime_facts["reasoning_effort"],
            "runtime_facts_status": runtime_facts["status"],
            "runtime_facts_source": RUNTIME_FACTS_SOURCE,
            "process_exit_code": completed.returncode,
            "wall_clock_ms": elapsed_ms,
            "usage": usage,
            "final_text_extracted": final_text is not None,
            "source_repository": facts_before,
            "grading": "pending-human-review",
        }
        (case_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    status = "OK" if completed.returncode == 0 else f"EXIT {completed.returncode}"
    print(
        f"[{case_id}] {status}; provider={runtime_facts['model']} "
        f"effort={runtime_facts['reasoning_effort']} facts={runtime_facts['status']}"
    )
    return completed.returncode


def report() -> Path:
    RESULTS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 规则治理 v2 研究评估汇总",
        "",
        "本文件由 eval runner 从本地结果自动汇总，不构成 Repository Authority，也不自动完成语义评分。",
        "",
    ]

    metadata_files = sorted(RESULTS.glob("*/*/metadata.json"))
    if not metadata_files:
        lines.append("当前没有可汇总的运行结果。")
    else:
        for metadata_path in metadata_files:
            payload = json.loads(metadata_path.read_text(encoding="utf-8"))
            model = metadata_path.parent.parent.name
            case_id = payload["case_id"]
            lines.extend(
                [
                    f"## {model} / {case_id}",
                    "",
                    f"- 请求模型：`{payload['requested_model']}`",
                    f"- Provider model：`{payload['provider_model']}`",
                    f"- 请求 reasoning effort：`{payload['requested_reasoning_effort']}`",
                    f"- 观察 reasoning effort：`{payload['observed_reasoning_effort']}`",
                    f"- Runtime facts：`{payload['runtime_facts_status']}`",
                    f"- 退出码：`{payload['process_exit_code']}`",
                    f"- Wall clock：`{payload['wall_clock_ms']} ms`",
                    f"- Prompt SHA-256：`{payload['prompt_sha256']}`",
                    "",
                ]
            )
            usage = payload.get("usage")
            if isinstance(usage, dict):
                lines.extend(["### Usage", "", "```json", json.dumps(usage, ensure_ascii=False, indent=2), "```", ""])

            final_path = metadata_path.parent / "final.md"
            if final_path.is_file():
                lines.extend(["### 模型最终输出", "", final_path.read_text(encoding="utf-8").rstrip(), ""])
            else:
                lines.extend(["### 模型最终输出", "", "未能从 JSONL 可靠提取，请人工读取同目录 `run.jsonl`。", ""])

    target = RESULTS / "summary.md"
    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(target.relative_to(ROOT))
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="规则治理 v2 研究评估")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-only", action="store_true")
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--report", action="store_true")
    parser.add_argument("--case", choices=["architecture", "scenarios", "all"], default="architecture")
    parser.add_argument("--scenario", action="append", help="定向运行一个场景，可重复")
    parser.add_argument("--model")
    parser.add_argument("--reasoning-effort", default="high")
    parser.add_argument("--codex-bin", default="codex")
    args = parser.parse_args()

    errors = validate_assets()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2

    if args.validate_only:
        facts = source_repository_facts()
        print("rule-governance-v2 assets: OK")
        print(f"branch={facts['branch']} head={facts['head']}")
        if facts["status_porcelain"]:
            print("WARNING: source working tree is not clean")
            print(facts["status_porcelain"])
        return 0

    if args.report:
        report()
        return 0

    if not args.model:
        parser.error("--run requires --model")

    check_codex(args.codex_bin)
    cases = selected_cases(args.case, args.scenario)
    failures = 0
    for case_id in cases:
        failures += run_one(
            codex_bin=args.codex_bin,
            case_id=case_id,
            model=args.model,
            reasoning_effort=args.reasoning_effort,
        ) != 0

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
