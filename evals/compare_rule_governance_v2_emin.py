#!/usr/bin/env python3
"""比较规则治理 v2 `01-technical-design` 的 v1 A 组与 E-min B 组。

比较器只汇总运行事实和预注册效率指标，不自动替代人工语义评分。
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "evals" / "results" / "rule-governance-v2"
REPORT_MD = RESULTS / "emin-comparison.md"
REPORT_JSON = RESULTS / "emin-comparison.json"
PRIMARY_REDUCTION_TARGET = 40.0

LARGE_SOURCE_PATTERNS = [
    "docs/guides/using-agentic-dev.md",
    "docs/method/ai-development-method.md",
    "docs/architecture/skill-contracts.md",
    "docs/architecture/skill-architecture.md",
    "docs/architecture/engineering-capability-architecture.md",
    "docs/architecture/engineering-disciplines.md",
    "docs/decisions/method-decisions.md",
    "docs/project/project-roadmap.md",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_command_metrics(jsonl_path: Path) -> dict[str, Any]:
    command_count = 0
    output_bytes = 0
    commands: list[str] = []

    for line in jsonl_path.read_text(encoding="utf-8").splitlines():
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

    large_sources = sorted(
        source for source in LARGE_SOURCE_PATTERNS if any(source in command for command in commands)
    )
    return {
        "command_execution_count": command_count,
        "repository_command_output_bytes": output_bytes,
        "commands": commands,
        "large_sources_referenced_in_commands": large_sources,
    }


def reduction_percent(a: int | float | None, b: int | float | None) -> float | None:
    if a is None or b is None or a == 0:
        return None
    return (float(a) - float(b)) / float(a) * 100.0


def usage_metrics(payload: dict[str, Any]) -> dict[str, int | None]:
    usage = payload.get("usage")
    if not isinstance(usage, dict):
        return {
            "input_tokens": None,
            "cached_input_tokens": None,
            "non_cached_input_tokens": None,
            "output_tokens": None,
            "reasoning_output_tokens": None,
        }
    input_tokens = usage.get("input_tokens")
    cached = usage.get("cached_input_tokens")
    non_cached = (
        input_tokens - cached
        if isinstance(input_tokens, int) and isinstance(cached, int)
        else None
    )
    return {
        "input_tokens": input_tokens if isinstance(input_tokens, int) else None,
        "cached_input_tokens": cached if isinstance(cached, int) else None,
        "non_cached_input_tokens": non_cached,
        "output_tokens": usage.get("output_tokens") if isinstance(usage.get("output_tokens"), int) else None,
        "reasoning_output_tokens": (
            usage.get("reasoning_output_tokens")
            if isinstance(usage.get("reasoning_output_tokens"), int)
            else None
        ),
    }


def changed_files(base: str | None, head: str | None) -> tuple[str, list[str]]:
    if not base or not head:
        return "unknown", []
    completed = subprocess.run(
        ["git", "diff", "--name-only", f"{base}..{head}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        return "unknown", []
    files = [line.strip() for line in completed.stdout.splitlines() if line.strip()]
    non_eval = [path for path in files if not path.startswith("evals/")]
    return ("eval-only" if not non_eval else "authority-drift"), files


def compare_model(model: str) -> dict[str, Any]:
    model_dir = RESULTS / model
    a_dir = model_dir / "01-technical-design"
    b_dir = model_dir / "01-technical-design-emin"

    required = [
        a_dir / "metadata.json",
        a_dir / "run.jsonl",
        a_dir / "final.md",
        b_dir / "metadata.json",
        b_dir / "run.jsonl",
        b_dir / "final.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        return {"model": model, "status": "missing-results", "missing": missing}

    a_meta = load_json(a_dir / "metadata.json")
    b_meta = load_json(b_dir / "metadata.json")
    a_cmd = extract_command_metrics(a_dir / "run.jsonl")
    b_cmd = extract_command_metrics(b_dir / "run.jsonl")
    a_usage = usage_metrics(a_meta)
    b_usage = usage_metrics(b_meta)

    a_head = (a_meta.get("source_repository") or {}).get("head")
    b_head = (b_meta.get("source_repository") or {}).get("head")
    repo_delta_status, repo_delta_files = changed_files(a_head, b_head)

    a_prompt_hash = a_meta.get("prompt_sha256")
    b_scenario_hash = b_meta.get("scenario_sha256")
    scenario_equal = bool(a_prompt_hash and b_scenario_hash and a_prompt_hash == b_scenario_hash)

    provider_equal = (
        a_meta.get("provider_model") is not None
        and a_meta.get("provider_model") == b_meta.get("provider_model")
    )
    effort_equal = (
        a_meta.get("observed_reasoning_effort") is not None
        and a_meta.get("observed_reasoning_effort") == b_meta.get("observed_reasoning_effort")
    )
    runtime_observed = (
        a_meta.get("runtime_facts_status") == "observed"
        and b_meta.get("runtime_facts_status") == "observed"
    )

    runtime_comparable = (
        scenario_equal
        and provider_equal
        and effort_equal
        and runtime_observed
        and repo_delta_status == "eval-only"
    )

    output_reduction = reduction_percent(
        a_cmd["repository_command_output_bytes"],
        b_cmd["repository_command_output_bytes"],
    )
    efficiency_target_met = (
        output_reduction is not None and output_reduction >= PRIMARY_REDUCTION_TARGET
    )

    return {
        "model": model,
        "status": "ready-for-human-semantic-review",
        "runtime_comparable": runtime_comparable,
        "comparability": {
            "scenario_equal": scenario_equal,
            "provider_equal": provider_equal,
            "reasoning_effort_equal": effort_equal,
            "runtime_facts_observed": runtime_observed,
            "repository_delta_status": repo_delta_status,
            "repository_delta_files": repo_delta_files,
            "a_head": a_head,
            "b_head": b_head,
            "a_provider_model": a_meta.get("provider_model"),
            "b_provider_model": b_meta.get("provider_model"),
            "a_effort": a_meta.get("observed_reasoning_effort"),
            "b_effort": b_meta.get("observed_reasoning_effort"),
        },
        "primary_metric": {
            "name": "repository_command_output_bytes",
            "target_reduction_percent": PRIMARY_REDUCTION_TARGET,
            "a": a_cmd["repository_command_output_bytes"],
            "b": b_cmd["repository_command_output_bytes"],
            "reduction_percent": output_reduction,
            "target_met": efficiency_target_met,
        },
        "secondary_metrics": {
            "command_execution_count": {
                "a": a_cmd["command_execution_count"],
                "b": b_cmd["command_execution_count"],
                "reduction_percent": reduction_percent(
                    a_cmd["command_execution_count"], b_cmd["command_execution_count"]
                ),
            },
            "input_tokens": {
                "a": a_usage["input_tokens"],
                "b": b_usage["input_tokens"],
                "reduction_percent": reduction_percent(a_usage["input_tokens"], b_usage["input_tokens"]),
            },
            "non_cached_input_tokens": {
                "a": a_usage["non_cached_input_tokens"],
                "b": b_usage["non_cached_input_tokens"],
                "reduction_percent": reduction_percent(
                    a_usage["non_cached_input_tokens"], b_usage["non_cached_input_tokens"]
                ),
            },
            "output_tokens": {
                "a": a_usage["output_tokens"],
                "b": b_usage["output_tokens"],
                "reduction_percent": reduction_percent(a_usage["output_tokens"], b_usage["output_tokens"]),
            },
            "wall_clock_ms": {
                "a": a_meta.get("wall_clock_ms"),
                "b": b_meta.get("wall_clock_ms"),
                "reduction_percent": reduction_percent(a_meta.get("wall_clock_ms"), b_meta.get("wall_clock_ms")),
            },
        },
        "context_expansion": {
            "a_large_sources": a_cmd["large_sources_referenced_in_commands"],
            "b_large_sources": b_cmd["large_sources_referenced_in_commands"],
            "a_commands": a_cmd["commands"],
            "b_commands": b_cmd["commands"],
        },
        "human_semantic_status": "PENDING",
        "a_final": str((a_dir / "final.md").relative_to(ROOT)),
        "b_final": str((b_dir / "final.md").relative_to(ROOT)),
    }


def fmt_percent(value: float | None) -> str:
    return "N/A" if value is None else f"{value:.1f}%"


def write_report(comparisons: list[dict[str, Any]]) -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(
        json.dumps({"primary_reduction_target_percent": PRIMARY_REDUCTION_TARGET, "models": comparisons}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# 规则治理 v2 E-min A/B 对比",
        "",
        "本报告只比较运行事实和预注册效率指标。语义结论必须继续按 `evals/rule-governance-v2/emin-design.md` 人工复核。",
        "",
        f"Primary efficiency target：`repository_command_output_bytes` 至少下降 {PRIMARY_REDUCTION_TARGET:.0f}% 且无重大语义回归。",
        "",
    ]

    for result in comparisons:
        model = result["model"]
        lines.extend([f"## {model}", ""])
        if result.get("status") == "missing-results":
            lines.append("结果不完整：")
            lines.extend(f"- `{path}`" for path in result["missing"])
            lines.append("")
            continue

        comp = result["comparability"]
        primary = result["primary_metric"]
        lines.extend(
            [
                f"- Runtime comparable：`{result['runtime_comparable']}`",
                f"- Scenario identical：`{comp['scenario_equal']}`",
                f"- Provider model identical：`{comp['provider_equal']}` (`{comp['a_provider_model']}` → `{comp['b_provider_model']}`)",
                f"- Reasoning effort identical：`{comp['reasoning_effort_equal']}` (`{comp['a_effort']}` → `{comp['b_effort']}`)",
                f"- A→B repository delta：`{comp['repository_delta_status']}`",
                f"- Primary metric：`{primary['a']}` → `{primary['b']}` bytes，下降 `{fmt_percent(primary['reduction_percent'])}`，目标达成：`{primary['target_met']}`",
                f"- Human semantic status：`{result['human_semantic_status']}`",
                "",
                "### Secondary metrics",
                "",
                "| Metric | A | B | Reduction |",
                "|---|---:|---:|---:|",
            ]
        )
        for name, metric in result["secondary_metrics"].items():
            lines.append(
                f"| `{name}` | {metric['a']} | {metric['b']} | {fmt_percent(metric['reduction_percent'])} |"
            )

        lines.extend(["", "### 大型来源命令引用", ""])
        lines.append("A：" + (", ".join(f"`{x}`" for x in result["context_expansion"]["a_large_sources"]) or "无"))
        lines.append("")
        lines.append("B：" + (", ".join(f"`{x}`" for x in result["context_expansion"]["b_large_sources"]) or "无"))
        lines.extend(
            [
                "",
                "### 人工语义复核入口",
                "",
                f"- A：`{result['a_final']}`",
                f"- B：`{result['b_final']}`",
                "- 逐项按 `emin-design.md` 第 5 节 10 条语义检查评分；任何重大语义回归都优先于效率收益。",
                "",
            ]
        )

    REPORT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(REPORT_MD.relative_to(ROOT))
    print(REPORT_JSON.relative_to(ROOT))


def main() -> int:
    parser = argparse.ArgumentParser(description="规则治理 v2 E-min A/B 对比")
    parser.add_argument("--model", action="append", help="只比较指定模型目录名，可重复")
    args = parser.parse_args()

    models = args.model
    if not models:
        models = sorted(path.name for path in RESULTS.iterdir() if path.is_dir()) if RESULTS.is_dir() else []
    if not models:
        print("ERROR: 没有可比较的模型结果", file=sys.stderr)
        return 2

    comparisons = [compare_model(model) for model in models]
    write_report(comparisons)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
