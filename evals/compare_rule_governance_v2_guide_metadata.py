#!/usr/bin/env python3
"""汇总规则治理 v2 A / E-min / G-min 三组效率证据。

只汇总运行事实，不自动完成语义评分。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from run_rule_governance_v2_emin import extract_command_metrics
from run_rule_governance_v2_research import safe_name

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "evals" / "results" / "rule-governance-v2"

VARIANTS = {
    "A-v1": "01-technical-design",
    "B-emin": "01-technical-design-emin",
    "C-guide-metadata": "01-technical-design-guide-metadata",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def number(value: Any) -> int | None:
    return value if isinstance(value, int) else None


def load_case(model: str, directory: str) -> dict[str, Any] | None:
    case_dir = RESULTS / safe_name(model) / directory
    metadata_path = case_dir / "metadata.json"
    jsonl_path = case_dir / "run.jsonl"
    if not metadata_path.is_file() or not jsonl_path.is_file():
        return None

    metadata = load_json(metadata_path)
    usage = metadata.get("usage") if isinstance(metadata.get("usage"), dict) else {}
    command_metrics = metadata.get("command_metrics")
    if not isinstance(command_metrics, dict):
        command_metrics = extract_command_metrics(jsonl_path.read_text(encoding="utf-8"))

    input_tokens = number(usage.get("input_tokens"))
    cached_tokens = number(usage.get("cached_input_tokens"))
    noncached = None
    if input_tokens is not None and cached_tokens is not None:
        noncached = input_tokens - cached_tokens

    return {
        "directory": directory,
        "provider_model": metadata.get("provider_model"),
        "reasoning_effort": metadata.get("observed_reasoning_effort"),
        "runtime_facts_status": metadata.get("runtime_facts_status"),
        "exit_code": metadata.get("process_exit_code"),
        "wall_clock_ms": metadata.get("wall_clock_ms"),
        "input_tokens": input_tokens,
        "cached_input_tokens": cached_tokens,
        "noncached_input_tokens": noncached,
        "output_tokens": number(usage.get("output_tokens")),
        "command_count": command_metrics.get("command_execution_count"),
        "repo_output_bytes": command_metrics.get("repository_command_output_bytes"),
        "commands": command_metrics.get("commands", []),
        "source_head": (metadata.get("source_repository") or {}).get("head"),
        "final_path": case_dir / "final.md",
    }


def pct_reduction(base: int | None, current: int | None) -> float | None:
    if not isinstance(base, int) or not isinstance(current, int) or base <= 0:
        return None
    return (base - current) * 100.0 / base


def fmt_int(value: Any) -> str:
    return f"{value:,}" if isinstance(value, int) else "n/a"


def fmt_pct(value: float | None) -> str:
    return f"{value:.1f}%" if value is not None else "n/a"


def main() -> int:
    parser = argparse.ArgumentParser(description="规则治理 v2 A/E-min/G-min 三组对比")
    parser.add_argument("--model", action="append", required=True)
    args = parser.parse_args()

    lines = [
        "# 规则治理 v2 A / E-min / G-min 对比",
        "",
        "本报告只汇总运行事实与效率，不自动完成 10 条语义人工评分。",
        "",
    ]

    for model in args.model:
        rows = {name: load_case(model, directory) for name, directory in VARIANTS.items()}
        lines.extend([f"## {model}", ""])
        missing = [name for name, payload in rows.items() if payload is None]
        if missing:
            lines.append(f"缺少结果：{', '.join(missing)}")
            lines.append("")
            continue

        a = rows["A-v1"]
        b = rows["B-emin"]
        c = rows["C-guide-metadata"]
        assert a and b and c

        comparable = (
            a["runtime_facts_status"] == b["runtime_facts_status"] == c["runtime_facts_status"] == "observed"
            and a["provider_model"] == b["provider_model"] == c["provider_model"]
            and a["reasoning_effort"] == b["reasoning_effort"] == c["reasoning_effort"] == "high"
            and a["exit_code"] == b["exit_code"] == c["exit_code"] == 0
        )
        lines.extend([
            f"- 运行时可比：`{'YES' if comparable else 'NO'}`",
            f"- Provider model：`{c['provider_model']}`",
            f"- Reasoning effort：`{c['reasoning_effort']}`",
            "",
            "| 指标 | A-v1 | B-E-min | C-Guide+Metadata | B vs A | C vs A |",
            "|---|---:|---:|---:|---:|---:|",
        ])

        metrics = [
            ("Repository output bytes", "repo_output_bytes"),
            ("Command executions", "command_count"),
            ("Input tokens", "input_tokens"),
            ("Non-cached input", "noncached_input_tokens"),
            ("Output tokens", "output_tokens"),
            ("Wall clock ms", "wall_clock_ms"),
        ]
        for label, key in metrics:
            av = a[key]
            bv = b[key]
            cv = c[key]
            lines.append(
                f"| {label} | {fmt_int(av)} | {fmt_int(bv)} | {fmt_int(cv)} | "
                f"{fmt_pct(pct_reduction(av, bv))} | {fmt_pct(pct_reduction(av, cv))} |"
            )

        b_primary = pct_reduction(a["repo_output_bytes"], b["repo_output_bytes"])
        c_primary = pct_reduction(a["repo_output_bytes"], c["repo_output_bytes"])
        gap = None
        if b_primary is not None and c_primary is not None:
            gap = abs(b_primary - c_primary)

        lines.extend([
            "",
            f"- E-min 主指标下降：**{fmt_pct(b_primary)}**",
            f"- G-min 主指标下降：**{fmt_pct(c_primary)}**",
            f"- 两者主指标收益差：**{fmt_pct(gap)}**",
            f"- G-min 达到 ≥40% 预注册效率门槛：`{'YES' if c_primary is not None and c_primary >= 40.0 else 'NO'}`",
            f"- G-min 与 E-min 收益差 ≤20 个百分点：`{'YES' if gap is not None and gap <= 20.0 else 'NO'}`",
            "",
            "### G-min 命令轨迹",
            "",
            "```text",
            *[str(command) for command in c.get("commands", [])],
            "```",
            "",
            "### 人工语义评分",
            "",
            "请读取 C 组 `final.md`，按 `guide-metadata-design.md` 的同一 10 条语义标准评分。",
            "只有无重大语义回归，效率门槛才有意义。",
            "",
        ])

    target = RESULTS / "guide-metadata-comparison.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
