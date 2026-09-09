#!/usr/bin/env python3
"""规则治理 v2 G-min：Guide decomposition + metadata 运行时发现实验。

本 runner 只运行 01-technical-design 的 C 组：
- 不预解析当前 responsibility；
- 不直接调用 technical-plan；
- 从当前 using-agentic-dev.md 按章节原文动态生成小模块；
- 只给 Agent 一个不含规则正文的 metadata Catalog 作为初始发现入口；
- 不把任何 Skill 额外安装为运行时自动发现项，避免绕过 Catalog；
- 完整 Repository 仍可访问，模块可按 pointer 指向现有 Skill / Authority；
- 允许必要时 fail-closed；
- 不修改正式 Method / Guide / Skill。
"""

from __future__ import annotations

import argparse
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
from run_rule_governance_v2_emin import extract_command_metrics
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
DESIGN = EVAL_DIR / "guide-metadata-design.md"
MANIFEST = EVAL_DIR / "guide-metadata-manifest.json"
RESULTS = ROOT / "evals" / "results" / "rule-governance-v2"
VARIANT_ID = "guide-metadata"
RUNTIME_FACTS_SOURCE = "codex-exec-sse-provider-model+turn-span-reasoning-effort"
CATALOG_DIR = Path(".eval-rule-catalog")

DISCOVERY_ENVELOPE = """[规则治理 v2 G-min 评估发现入口]

这是评估专用的派生发现机制，不是 Repository Authority，也没有预先判断当前任务属于哪个责任。

开始时只执行以下发现过程：

1. 先读取 `.eval-rule-catalog/catalog.json`；
2. 只根据任务本身与 Catalog metadata，自行选择最小必要模块；
3. 再读取被选中模块正文；模块正文是当前正式 Guide 的原文章节投影，不是新规则；
4. 若模块提供 `recommended_sources`，只有当前职责确实需要时才继续读取相应当前 Authority / Skill；
5. 不要为了“完整”默认读取完整大型 Guide、完整 Method 或完整 Contract；
6. 完整 Repository 仍然可访问。只有模块 / Skill 无法回答当前职责、来源冲突、规范性缺口，或高影响 / 不可逆 / 重大架构 / 安全隐私 / 授权边界不清时，才 fail-closed 扩展读取当前 Repository Authority。

最终答案除原场景要求外，再单独列出：

- 你选择的 metadata module id；
- 你实际读取的 Repository 文件；
- 如果发生 fail-closed 扩展读取，具体触发原因。

不要讨论规则治理 v2 候选架构本身。

[/规则治理 v2 G-min 评估发现入口]
"""


def load_manifest() -> dict[str, Any]:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def heading_level(line: str) -> int | None:
    match = re.match(r"^(#{1,6})\s+", line)
    return len(match.group(1)) if match else None


def extract_markdown_section(text: str, heading_prefix: str) -> str:
    lines = text.splitlines()
    start: int | None = None
    level: int | None = None
    for index, line in enumerate(lines):
        if line.startswith(heading_prefix):
            start = index
            level = heading_level(line)
            break
    if start is None or level is None:
        raise RuntimeError(f"无法定位章节：{heading_prefix}")

    end = len(lines)
    for index in range(start + 1, len(lines)):
        current = heading_level(lines[index])
        if current is not None and current <= level:
            end = index
            break
    return "\n".join(lines[start:end]).rstrip() + "\n"


def yaml_list(values: list[str]) -> str:
    if not values:
        return "[]"
    return "\n".join(f"  - {value}" for value in values)


def build_catalog_projection(workspace: Path) -> dict[str, Any]:
    manifest = load_manifest()
    source_relative = Path(manifest["source"])
    source_path = workspace / source_relative
    source_text = source_path.read_text(encoding="utf-8")
    source_sha256 = sha256_text(source_text)

    catalog_root = workspace / CATALOG_DIR
    modules_root = catalog_root / "modules"
    modules_root.mkdir(parents=True, exist_ok=True)

    catalog_modules: list[dict[str, Any]] = []
    for entry in manifest["modules"]:
        section = extract_markdown_section(source_text, entry["heading_prefix"])
        module_path = modules_root / f"{entry['id']}.md"
        recommended = list(entry.get("recommended_sources", []))
        front_matter = [
            "---",
            f"id: {entry['id']}",
            f"source: {manifest['source']}",
            f"source_pointer: \"{entry['heading_prefix']}\"",
            f"source_sha256: {source_sha256}",
            "scope:",
            yaml_list(entry.get("scope", [])),
            "responsibility:",
            yaml_list(entry.get("responsibility", [])),
            "conditions:",
            yaml_list(entry.get("conditions", [])),
            "risk:",
            yaml_list(entry.get("risk", [])),
            "consumers:",
            yaml_list(entry.get("consumers", [])),
        ]
        if recommended:
            front_matter.extend(["recommended_sources:", yaml_list(recommended)])
        front_matter.extend(["---", ""])
        note = (
            "> 评估派生模块：metadata 只用于发现；下方正文逐字来自当前 source section，"
            "正式语义仍归原 Repository Authority。\n\n"
        )
        module_path.write_text("\n".join(front_matter) + note + section, encoding="utf-8")

        catalog_modules.append(
            {
                "id": entry["id"],
                "module_path": str(module_path.relative_to(workspace)),
                "source": manifest["source"],
                "source_pointer": entry["heading_prefix"],
                "scope": entry.get("scope", []),
                "responsibility": entry.get("responsibility", []),
                "conditions": entry.get("conditions", []),
                "risk": entry.get("risk", []),
                "consumers": entry.get("consumers", []),
                "recommended_sources": recommended,
            }
        )

    catalog = {
        "schema_version": 1,
        "authority": False,
        "derived": True,
        "selection_rule": "Choose the minimum applicable modules from task scope/responsibility/conditions/risk; do not load every module.",
        "source": manifest["source"],
        "source_sha256": source_sha256,
        "modules": catalog_modules,
    }
    catalog_text = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    (catalog_root / "catalog.json").write_text(catalog_text, encoding="utf-8")
    return {
        "catalog_sha256": sha256_text(catalog_text),
        "source_sha256": source_sha256,
        "module_count": len(catalog_modules),
    }


def validate_assets() -> list[str]:
    errors: list[str] = []
    for path in (SCENARIO, DESIGN, MANIFEST):
        if not path.is_file():
            errors.append(f"缺少 G-min 资产：{path.relative_to(ROOT)}")
    if errors:
        return errors

    try:
        manifest = load_manifest()
    except Exception as exc:  # noqa: BLE001
        return [f"manifest 无法解析：{exc}"]

    ids: set[str] = set()
    source = ROOT / manifest.get("source", "")
    if not source.is_file():
        errors.append(f"manifest source 不存在：{manifest.get('source')}")
        return errors
    source_text = source.read_text(encoding="utf-8")

    for entry in manifest.get("modules", []):
        module_id = entry.get("id")
        if not isinstance(module_id, str) or not module_id:
            errors.append("存在无效 module id")
            continue
        if module_id in ids:
            errors.append(f"重复 module id：{module_id}")
        ids.add(module_id)
        try:
            extract_markdown_section(source_text, entry["heading_prefix"])
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{module_id} 章节提取失败：{exc}")
        for pointer in entry.get("recommended_sources", []):
            if not (ROOT / pointer).is_file():
                errors.append(f"{module_id} recommended source 不存在：{pointer}")

    if "technical-planning" not in ids:
        errors.append("缺少 technical-planning 模块")
    return errors


def build_prompt() -> tuple[str, str]:
    scenario = SCENARIO.read_text(encoding="utf-8")
    return DISCOVERY_ENVELOPE.rstrip() + "\n\n" + scenario, scenario


def run_one(*, codex_bin: str, model: str, reasoning_effort: str, force: bool) -> int:
    model_dir = RESULTS / safe_name(model)
    case_dir = model_dir / "01-technical-design-guide-metadata"
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

    with tempfile.TemporaryDirectory(prefix="agentic-dev-rgv2-guide-metadata-") as temp_dir:
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

        print(f"[guide-metadata] model={model} effort={reasoning_effort}")
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
            "case_id": "01-technical-design",
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

    status = "OK" if completed.returncode == 0 else f"EXIT {completed.returncode}"
    print(
        f"[guide-metadata] {status}; provider={runtime_facts['model']} "
        f"effort={runtime_facts['reasoning_effort']} facts={runtime_facts['status']} "
        f"repo_output={command_metrics['repository_command_output_bytes']}B"
    )
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="规则治理 v2 Guide + Metadata G-min 实验")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-only", action="store_true")
    mode.add_argument("--run", action="store_true")
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
        print("rule-governance-v2 Guide + Metadata assets: OK")
        print(f"branch={facts['branch']} head={facts['head']}")
        print(f"modules={len(load_manifest()['modules'])}")
        return 0

    if not args.model:
        parser.error("--run requires --model")
    check_codex(args.codex_bin)
    return run_one(
        codex_bin=args.codex_bin,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        force=args.force,
    )


if __name__ == "__main__":
    raise SystemExit(main())
