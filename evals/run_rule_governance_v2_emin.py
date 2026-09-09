#!/usr/bin/env python3
"""规则治理 v2 E-min Skill-first 运行时激活实验。

本 runner 只运行 `01-technical-design` 的 B 组：
- 保留完整 Repository 可访问性；
- 将当前职责预解析为 `technical-plan`；
- 显式激活当前仓库的 `technical-plan` Skill；
- 只有 Skill 不足 / 冲突 / 高影响边界不明时才允许 fail-closed 扩展读取；
- 不修改正式 Method / Guide / Skill；
- 不自动把进程成功或 token 下降判定为语义 PASS。

A 组复用此前已完成的本地 Pilot 结果，不由本脚本重跑。
"""

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
from typing import Any

from run_codex_evals import check_codex
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
SCENARIO = EVAL_DIR / "scenarios" / "01-technical-design.md"
DESIGN = EVAL_DIR / "emin-design.md"
RESULTS = ROOT / "evals" / "results" / "rule-governance-v2"
SKILL_SOURCE = ROOT / "skills" / "technical-plan"
VARIANT_ID = "emin-skill-first"
RUNTIME_FACTS_SOURCE = "codex-exec-sse-provider-model+turn-span-reasoning-effort"

ACTIVATION_ENVELOPE = """$technical-plan

[规则治理 v2 E-min 评估运行时激活结果]

这是评估专用的派生激活结果，不是 Repository Authority，也不改变后续任务事实。

- 当前责任已解析为：`technical-planning`
- 主要运行时激活单元：`technical-plan`
- 先使用已激活 Skill 与任务中提供的 Consumer 事实完成当前职责。
- 遵守渐进式披露：不要为了“完整”默认读取全部 Method / Guide / Contract / Architecture 文档。
- 完整 Repository 仍然可访问；如果已激活 Skill 无法回答当前职责、来源冲突、规范性缺口暴露，或高影响 / 不可逆 / 重大架构 / 安全隐私 / 授权边界不清，按现有规则 fail-closed 扩展读取当前 Repository Authority。
- 如果发生扩展读取，最终答案必须明确说明触发扩展的具体原因。

[/规则治理 v2 E-min 评估运行时激活结果]
"""


def validate_assets() -> list[str]:
    errors: list[str] = []
    for path in (SCENARIO, DESIGN, SKILL_SOURCE / "SKILL.md"):
        if not path.is_file():
            errors.append(f"缺少 E-min 资产：{path.relative_to(ROOT)}")
    if SCENARIO.is_file() and "场景 01：复杂技术设计" not in SCENARIO.read_text(encoding="utf-8"):
        errors.append("01-technical-design 场景身份异常")
    return errors


def install_only_technical_plan_skill(workspace: Path) -> None:
    """只把当前 technical-plan Skill 暴露为 Codex 可显式激活 Skill。

    这不会隐藏仓库里的其他文件；完整 Repository 仍保留在 workspace 中。
    """
    target = workspace / ".agents" / "skills" / "technical-plan"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKILL_SOURCE, target)


def build_prompt() -> tuple[str, str]:
    scenario = SCENARIO.read_text(encoding="utf-8")
    return ACTIVATION_ENVELOPE.rstrip() + "\n\n" + scenario, scenario


def extract_command_metrics(jsonl_text: str) -> dict[str, Any]:
    command_count = 0
    output_bytes = 0
    commands: list[str] = []

    for line in jsonl_text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict) or item.get("type") != "command_execution":
            continue

        command_count += 1
        command = item.get("command")
        if isinstance(command, str):
            commands.append(command)
        output = item.get("aggregated_output")
        if isinstance(output, str):
            output_bytes += len(output.encode("utf-8"))

    return {
        "command_execution_count": command_count,
        "repository_command_output_bytes": output_bytes,
        "commands": commands,
    }


def run_one(
    *,
    codex_bin: str,
    model: str,
    reasoning_effort: str,
    force: bool,
) -> int:
    model_dir = RESULTS / safe_name(model)
    case_dir = model_dir / "01-technical-design-emin"
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

    with tempfile.TemporaryDirectory(prefix="agentic-dev-rgv2-emin-") as temp_dir:
        temp = Path(temp_dir)
        workspace = prepare_isolated_repository(temp)
        install_only_technical_plan_skill(workspace)

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

        print(f"[01-technical-design-emin] model={model} effort={reasoning_effort}")
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
        (case_dir / "tool-metrics.json").write_text(
            json.dumps(command_metrics, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        metadata = {
            "case_id": "01-technical-design",
            "variant": VARIANT_ID,
            "scenario_source": str(SCENARIO.relative_to(ROOT)),
            "scenario_sha256": sha256_text(scenario),
            "activation_envelope_sha256": sha256_text(ACTIVATION_ENVELOPE),
            "composed_prompt_sha256": sha256_text(prompt),
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
            "command_metrics": {
                "command_execution_count": command_metrics["command_execution_count"],
                "repository_command_output_bytes": command_metrics["repository_command_output_bytes"],
            },
            "full_repository_available": True,
            "installed_runtime_skill": "technical-plan",
            "final_text_extracted": final_text is not None,
            "source_repository": source_before,
            "grading": "pending-human-review",
        }
        (case_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    status = "OK" if completed.returncode == 0 else f"EXIT {completed.returncode}"
    print(
        f"[01-technical-design-emin] {status}; provider={runtime_facts['model']} "
        f"effort={runtime_facts['reasoning_effort']} facts={runtime_facts['status']} "
        f"commands={command_metrics['command_execution_count']} "
        f"repo_output={command_metrics['repository_command_output_bytes']} bytes"
    )
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="规则治理 v2 E-min Skill-first 实验")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-only", action="store_true")
    mode.add_argument("--run", action="store_true")
    parser.add_argument("--model")
    parser.add_argument("--reasoning-effort", default="high")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--force", action="store_true", help="允许覆盖已有 E-min 结果；默认拒绝以保护额度")
    args = parser.parse_args()

    errors = validate_assets()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2

    if args.validate_only:
        facts = source_repository_facts()
        print("rule-governance-v2 E-min assets: OK")
        print(f"branch={facts['branch']} head={facts['head']}")
        print(f"scenario_sha256={sha256_text(SCENARIO.read_text(encoding='utf-8'))}")
        print(f"activation_envelope_sha256={sha256_text(ACTIVATION_ENVELOPE)}")
        if facts["status_porcelain"]:
            print("WARNING: source working tree is not clean")
            print(facts["status_porcelain"])
        return 0

    if not args.model:
        parser.error("--run requires --model")

    check_codex(args.codex_bin)
    try:
        return run_one(
            codex_bin=args.codex_bin,
            model=args.model,
            reasoning_effort=args.reasoning_effort,
            force=args.force,
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
