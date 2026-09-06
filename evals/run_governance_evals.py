#!/usr/bin/env python3
"""在隔离 Codex CLI 会话中运行 agentic-dev 项目治理定向评估。"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Iterable

from run_codex_evals import (
    EVALS,
    check_codex,
    copy_capability_context,
    run_codex,
)


GOVERNANCE_FILES = [
    EVALS / "governance" / "chinese-human-facing-output.json",
    EVALS / "governance" / "formal-concept-semantic-safety.json",
    EVALS / "governance" / "method-object-semantic-safety.json",
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def governance_cases() -> Iterable[tuple[str, list[str], dict]]:
    for path in GOVERNANCE_FILES:
        document = load_json(path)
        governance_name = document["governance_name"]
        context_paths = document["context_paths"]
        for case in document["evals"]:
            yield governance_name, context_paths, case


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="在隔离 Codex 会话中运行 agentic-dev 项目治理定向评估。"
    )
    parser.add_argument(
        "--scenario",
        action="append",
        default=[],
        help="只运行指定场景；需要多个场景时重复传入该参数",
    )
    parser.add_argument(
        "--codex-bin",
        default=os.environ.get("CODEX_BIN", "codex"),
        help="Codex CLI 可执行文件，默认读取 CODEX_BIN 或使用 codex",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.scenario) or None

    cases = list(governance_cases())
    known = {case["id"] for _, _, case in cases}
    if selected:
        unknown = selected - known
        if unknown:
            print(f"未知场景：{', '.join(sorted(unknown))}", file=sys.stderr)
            return 2

    check_codex(args.codex_bin)

    process_failures = 0
    for governance_name, context_paths, case in cases:
        scenario_id = case["id"]
        if selected and scenario_id not in selected:
            continue

        with tempfile.TemporaryDirectory(
            prefix=f"agentic-dev-governance-{scenario_id}-"
        ) as temp_dir:
            cwd = Path(temp_dir)
            copy_capability_context(cwd, context_paths)

            context_list = "\n".join(f"- {path}" for path in context_paths)
            prompt = (
                f"当前评估对象：{governance_name}。\n"
                "先读取以下当前项目治理上下文；这些文件与本提示构成本场景"
                "全部可用上下文，不要读取当前工作目录之外的路径：\n"
                f"{context_list}\n\n"
                f"{case['prompt']}"
            )

            failed = run_codex(
                codex_bin=args.codex_bin,
                scenario_id=scenario_id,
                prompt=prompt,
                result_group="governance",
                cwd=cwd,
                skip_git_repo_check=True,
            ) != 0
            process_failures += failed

    if process_failures:
        print(f"Codex 进程失败数：{process_failures}", file=sys.stderr)
        return 1

    print("所有选中场景的 Codex 进程均已正常结束。")
    print("仍需人工逐项进行语义评分；进程退出码 0 不等于评估通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())