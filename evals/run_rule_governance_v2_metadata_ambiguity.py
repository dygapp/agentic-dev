#!/usr/bin/env python3
"""规则治理 v2：metadata 歧义与误激活压力实验。"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from run_codex_evals import check_codex
from run_rule_governance_v2_emin import extract_command_metrics
from run_rule_governance_v2_guide_metadata import build_catalog_projection
from run_rule_governance_v2_research import (
    extract_final_agent_text,
    extract_usage,
    prepare_isolated_repository,
    safe_name,
    sha256_text,
    source_repository_facts,
)
from run_rule_retrieval_c3 import (
    extract_thread_id,
    parse_runtime_facts,
    sanitize_persisted_stderr,
)

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "evals" / "rule-governance-v2"
SCENARIO = EVAL_DIR / "scenarios" / "06-metadata-ambiguity.md"
DESIGN = EVAL_DIR / "metadata-ambiguity-design.md"
MANIFEST = EVAL_DIR / "guide-metadata-manifest.json"
RESULTS = ROOT / "evals" / "results" / "rule-governance-v2"
VARIANT_ID = "metadata-ambiguity"
RUNTIME_FACTS_SOURCE = "codex-exec-sse-provider-model+turn-span-reasoning-effort"

DISCOVERY_ENVELOPE = """[规则治理 v2 metadata 歧义实验发现入口]

这是 eval-only 派生发现机制，不是 Repository Authority，也没有预先判断当前任务的责任归属。

开始时：

1. 读取 `.eval-rule-catalog/catalog.json`；
2. 根据任务事实自行选择最小必要 metadata modules；
3. 区分一个 primary responsibility 与必要 supporting context，不把所有可能相关模块并列激活；
4. 读取被选中模块正文；模块正文来自当前正式 Guide 原文章节投影；
5. 只有职责判断确实需要时，才读取模块指向的现行 Skill / Authority；
6. 不要为了完整性默认读取完整 Guide、Method、Skill Contracts 或全部模块；
7. 完整 Repository 仍可访问。只有模块 / Skill 无法回答当前职责、来源冲突、规范性缺口，或高影响 / 不可逆 / 安全隐私 / 授权边界不清时，才 fail-closed 扩展读取当前 Repository Authority。

本入口不提供正确责任、正确 Skill 或正确 Stage Return。请只根据场景与当前 Repository Authority 判断。

最终答案除场景要求外，必须明确：

- primary responsibility；
- supporting context；
- 选择的 metadata module id；
- 实际读取的 Repository 文件；
- 是否发生 fail-closed 扩展读取及原因。

[/规则治理 v2 metadata 歧义实验发现入口]
"""


def validate_assets() -> list[str]:
    errors: list[str] = []
    required = [
        SCENARIO,
        DESIGN,
        MANIFEST,
        ROOT / "skills" / "technical-plan" / "SKILL.md",
        ROOT / "skills" / "execute-unit" / "SKILL.md",
        ROOT / "skills" / "readiness-check" / "SKILL.md",
        ROOT / "skills" / "systematic-debug" / "SKILL.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"缺少实验资产：{path.relative_to(ROOT)}")

    if errors:
        return errors

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"manifest 无法解析：{exc}"]

    ids = {entry.get("id") for entry in manifest.get("modules", [])}
    for required_id in ("technical-planning", "execution-context", "slice-readiness"):
        if required_id not in ids:
            errors.append(f"manifest 缺少竞争模块：{required_id}")

    scenario_text = SCENARIO.read_text(encoding="utf-8")
    if "Observed Defect" not in scenario_text or "readiness-check" not in scenario_text:
        errors.append("歧义场景关键竞争信号缺失")

    return errors


def build_prompt() -> tuple[str, str]:
    scenario = SCENARIO.read_text(encoding="utf-8")
    return DISCOVERY_ENVELOPE.rstrip() + "\n\n" + scenario, scenario


def run_one(*, codex_bin: str, model: str, reasoning_effort: str, force: bool) -> int:
    model_dir = RESULTS / safe_name(model)
    case_dir = model_dir / "06-metadata-ambiguity"
    if case_dir.exists() and any(case_dir.iterdir()) and not force:
        raise RuntimeError(
            f"结果目录已存在：{case_dir.relative_to(ROOT)}；为避免重复消耗额度，默认拒绝重跑。"
            "如确需覆盖，请显式增加 --force。"
        )
    if case_dir.exists() and force:
        shutil.rmtree(case_dir)
    case_dir.mkdir(parents=True, exist_ok=True)

    prompt, scenario = build_prompt()
    source_before = source_repository_facts()

    with tempfile.TemporaryDirectory(prefix="agentic-dev-rgv2-metadata-ambiguity-") as temp_dir:
        temp = Path(temp_dir)
        workspace = prepare_isolated_repository(temp)
        projection = build_catalog_projection(workspace)

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

        print(f"[metadata-ambiguity] model={model} effort={reasoning_effort}")
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
        command_metrics = extract_command_metrics(completed.stdout)

        (case_dir / "run.jsonl").write_text(completed.stdout, encoding="utf-8")
        (case_dir / "stderr.txt").write_text(
            sanitize_persisted_stderr(completed.stderr), encoding="utf-8"
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
            json.dumps(runtime_record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

        metadata = {
            "case_id": "06-metadata-ambiguity",
            "variant": VARIANT_ID,
            "scenario_sha256": sha256_text(scenario),
            "prompt_sha256": sha256_text(prompt),
            "manifest_sha256": sha256_text(MANIFEST.read_text(encoding="utf-8")),
            "catalog_sha256": projection["catalog_sha256"],
            "catalog_source_sha256": projection["source_sha256"],
            "catalog_module_count": projection["module_count"],
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
            "command_metrics": command_metrics,
            "source_repository": source_before,
            "grading": "pending-human-review",
        }
        (case_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    print(f"results={case_dir.relative_to(ROOT)}")
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--model")
    parser.add_argument("--reasoning-effort", default="high")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    errors = validate_assets()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2

    if args.validate_only:
        facts = source_repository_facts()
        print("rule-governance-v2 metadata ambiguity assets: OK")
        print(f"branch={facts.get('branch')}")
        print(f"head={facts.get('head')}")
        print(f"status={facts.get('status')}")
        return 0

    if not args.run:
        parser.error("请使用 --validate-only 或 --run")
    if not args.model:
        parser.error("--run 需要 --model")

    check_codex(args.codex_bin)
    return run_one(
        codex_bin=args.codex_bin,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        force=args.force,
    )


if __name__ == "__main__":
    raise SystemExit(main())
