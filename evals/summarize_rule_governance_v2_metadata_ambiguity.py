#!/usr/bin/env python3
"""汇总 metadata 歧义实验运行事实；不自动做语义判分。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "evals" / "results" / "rule-governance-v2"


def safe_name(value: str) -> str:
    return value.replace("/", "-").replace(":", "-")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def fmt_int(value) -> str:
    return "n/a" if value is None else f"{value:,}"


def row_for(model: str) -> tuple[dict, str]:
    case_dir = RESULTS / safe_name(model) / "06-metadata-ambiguity"
    metadata_path = case_dir / "metadata.json"
    if not metadata_path.is_file():
        return {"model": model, "missing": True}, ""
    metadata = load_json(metadata_path)
    final_path = case_dir / "final.md"
    final = final_path.read_text(encoding="utf-8") if final_path.is_file() else ""
    usage = metadata.get("usage") or {}
    metrics = metadata.get("command_metrics") or {}
    input_tokens = usage.get("input_tokens")
    cached = usage.get("cached_input_tokens")
    non_cached = None
    if isinstance(input_tokens, int) and isinstance(cached, int):
        non_cached = input_tokens - cached
    return {
        "model": model,
        "missing": False,
        "provider_model": metadata.get("provider_model"),
        "effort": metadata.get("observed_reasoning_effort"),
        "runtime_status": metadata.get("runtime_facts_status"),
        "exit_code": metadata.get("process_exit_code"),
        "repo_output": metrics.get("repository_command_output_bytes"),
        "commands": metrics.get("command_execution_count"),
        "input_tokens": input_tokens,
        "cached_tokens": cached,
        "non_cached_tokens": non_cached,
        "output_tokens": usage.get("output_tokens"),
        "wall_ms": metadata.get("wall_clock_ms"),
        "source_repository": metadata.get("source_repository"),
        "scenario_sha256": metadata.get("scenario_sha256"),
        "manifest_sha256": metadata.get("manifest_sha256"),
    }, final


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", action="append", required=True)
    args = parser.parse_args()

    rows: list[dict] = []
    finals: dict[str, str] = {}
    for model in args.model:
        row, final = row_for(model)
        rows.append(row)
        finals[model] = final

    lines = [
        "# Rule Governance v2 — Metadata Ambiguity Summary",
        "",
        "> 仅汇总运行事实与最终输出，不自动判定语义 PASS。不同场景之间的 token / wall-clock 只能作为参考，不能作为正式 A/B。",
        "",
        "| Requested model | Provider model | Effort | Runtime | Exit | Repo output bytes | Commands | Input | Non-cached input | Output | Wall ms |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        if row.get("missing"):
            lines.append(f"| {row['model']} | MISSING | | | | | | | | | |")
            continue
        lines.append(
            "| {model} | {provider} | {effort} | {runtime} | {exit_code} | {repo_output} | {commands} | {input_tokens} | {non_cached_tokens} | {output_tokens} | {wall_ms} |".format(
                model=row["model"],
                provider=row.get("provider_model") or "n/a",
                effort=row.get("effort") or "n/a",
                runtime=row.get("runtime_status") or "n/a",
                exit_code=fmt_int(row.get("exit_code")),
                repo_output=fmt_int(row.get("repo_output")),
                commands=fmt_int(row.get("commands")),
                input_tokens=fmt_int(row.get("input_tokens")),
                non_cached_tokens=fmt_int(row.get("non_cached_tokens")),
                output_tokens=fmt_int(row.get("output_tokens")),
                wall_ms=fmt_int(row.get("wall_ms")),
            )
        )

    comparable = [row for row in rows if not row.get("missing")]
    lines.extend(["", "## Reproducibility facts", ""])
    for row in comparable:
        source = row.get("source_repository") or {}
        lines.extend(
            [
                f"### {row['model']}",
                "",
                f"- source branch: `{source.get('branch')}`",
                f"- source head: `{source.get('head')}`",
                f"- source status: `{source.get('status')}`",
                f"- scenario sha256: `{row.get('scenario_sha256')}`",
                f"- manifest sha256: `{row.get('manifest_sha256')}`",
                "",
            ]
        )

    lines.extend(["## Human semantic review", ""])
    lines.extend(
        [
            "按 `evals/rule-governance-v2/metadata-ambiguity-design.md` 的预注册标准人工检查：",
            "",
            "1. primary responsibility 是否为 `technical-plan`；",
            "2. supporting context 是否被正确降级；",
            "3. 是否停止当前 Execute；",
            "4. 是否错误进入 `systematic-debug`；",
            "5. 是否错误重新打开已 Ready 的 WHAT / WHY；",
            "6. 是否在事实不足时发明 shared contract 方案；",
            "7. stale Readiness 是否被错误复用；",
            "8. 是否正确要求重新 `slice-work → readiness-check`；",
            "9. Unit identity / stable identifier 边界是否正确；",
            "10. 是否出现无依据 Human escalation；",
            "11. metadata module 是否明显过激活；",
            "12. 是否无理由回退完整规则栈。",
            "",
        ]
    )

    for model in args.model:
        lines.extend([f"## Final output — {model}", "", finals.get(model, "") or "MISSING", ""])

    output = RESULTS / "metadata-ambiguity-summary.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(output.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
