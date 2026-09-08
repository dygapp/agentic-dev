#!/usr/bin/env python3
"""规则检索与激活 A/B 评估基线运行器。

C2 只要求实现并静态校验 A/B 基线；真正的 Codex 新上下文运行属于 C3。
默认不调用 Agent，只有显式传入 --run 才执行 Codex。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

from query_rule_index import (
    check_sources,
    load_json,
    query_index,
    unique_sources,
    validate_index,
)
from run_codex_evals import check_codex, run_codex


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
DESIGN = EVALS / "rule-retrieval" / "targeted-evaluation-design.json"
INDEX = EVALS / "rule-retrieval" / "rule-index.json"
FIXTURES = EVALS / "rule-retrieval" / "fixtures"
RESULT_GROUP = "rule-retrieval"
VARIANTS = {"A", "B"}
REQUIRED_SCENARIO_FIELDS = {
    "id",
    "prompt",
    "a_context_paths",
    "b_query",
    "b_expected_rule_keys",
    "b_expected_fallback",
    "expected_behavior",
    "assertions",
}


def ensure_safe_relative(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError(f"不安全的相对路径：{path}")
    return candidate


def fixture_root(case: dict[str, Any]) -> Path | None:
    fixture = case.get("fixture")
    if not fixture:
        return None
    if not isinstance(fixture, str) or not fixture:
        raise ValueError(f"{case.get('id', '<unknown>')}: fixture 必须是非空字符串")
    root = FIXTURES / fixture
    if not root.is_dir():
        raise ValueError(f"{case['id']}: fixture 不存在：{fixture}")
    return root


def resolve_declared_path(case: dict[str, Any], relative: str, source_root: Path = ROOT) -> Path:
    rel = ensure_safe_relative(relative)
    if rel.parts and rel.parts[0] == "fixture":
        root = fixture_root(case)
        if root is None:
            raise ValueError(f"{case['id']}: 声明了 fixture/ 路径但没有 fixture")
        source = root.joinpath(*rel.parts[1:])
    else:
        source = source_root / rel
    source = source.resolve()
    if not source.is_file():
        raise ValueError(f"{case['id']}: 上下文文件不存在：{relative}")
    return source


def copy_declared_path(
    case: dict[str, Any],
    relative: str,
    workspace: Path,
    source_root: Path = ROOT,
) -> str:
    source = resolve_declared_path(case, relative, source_root)
    rel = ensure_safe_relative(relative)
    target = workspace / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return relative


def heading_section(text: str, section_number: str) -> str:
    """按 Markdown 数字标题提取一个规范性源章节。"""
    lines = text.splitlines(keepends=True)
    pattern = re.compile(
        rf"^(#{{1,6}})\s+{re.escape(section_number)}(?:\.|\s|$)"
    )
    start = None
    level = None
    for index, line in enumerate(lines):
        match = pattern.match(line)
        if match:
            start = index
            level = len(match.group(1))
            break
    if start is None or level is None:
        raise ValueError(f"无法解析源章节 §{section_number}")

    end = len(lines)
    next_heading = re.compile(r"^(#{1,6})\s+")
    for index in range(start + 1, len(lines)):
        match = next_heading.match(lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return "".join(lines[start:end]).rstrip() + "\n"


def section_numbers(section_spec: str) -> list[str]:
    numbers: list[str] = []

    range_pattern = re.compile(r"§(\d+)\.(\d+)\s*[～~-]\s*§?(\d+)\.(\d+)")
    ranges: list[tuple[str, str]] = []
    for match in range_pattern.finditer(section_spec):
        major_a, minor_a, major_b, minor_b = match.groups()
        if major_a != major_b:
            raise ValueError(f"不支持跨主章节范围：{match.group(0)}")
        start = int(minor_a)
        end = int(minor_b)
        if end < start:
            raise ValueError(f"反向章节范围：{match.group(0)}")
        for minor in range(start, end + 1):
            number = f"{major_a}.{minor}"
            if number not in numbers:
                numbers.append(number)
        ranges.append((match.start(), match.end()))

    for match in re.finditer(r"§(\d+(?:\.\d+)?)", section_spec):
        if any(start <= match.start() < end for start, end in ranges):
            continue
        number = match.group(1)
        if number not in numbers:
            numbers.append(number)
    return numbers


def materialize_result_excerpt(
    result: dict[str, Any], workspace: Path, source_root: Path = ROOT
) -> str:
    pointer = result["source_pointer"]
    source_path = ensure_safe_relative(pointer["path"])
    source = (source_root / source_path).resolve()
    if not source.is_file():
        raise ValueError(f"规范性源不存在：{pointer['path']}")
    text = source.read_text(encoding="utf-8")
    numbers = section_numbers(pointer["section"])

    if numbers:
        body = "\n\n".join(heading_section(text, number).rstrip() for number in numbers) + "\n"
    else:
        # Skill 职责契约、AGENTS 薄指针等无法由数字章节进一步缩小；
        # 它们本身就是已命中的独立职责载体，允许复制当前完整文件。
        body = text

    relative = Path("retrieved") / f"{result['entry_key']}.md"
    target = workspace / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    provenance = (
        f"<!-- 派生评估上下文；规范性源：{pointer['path']}；"
        f"section={pointer['section']}；identity={pointer['identity']} -->\n"
    )
    target.write_text(provenance + body, encoding="utf-8")
    return relative.as_posix()


def copy_all_index_sources(index: dict[str, Any], target_root: Path) -> None:
    for source in unique_sources(index):
        rel = ensure_safe_relative(source["path"])
        source_path = ROOT / rel
        target = target_root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target)


def stale_fixture_root(index: dict[str, Any], case: dict[str, Any], temp_root: Path) -> Path:
    root = temp_root / "stale-source-root"
    copy_all_index_sources(index, root)
    # 只制造内容身份变化，不改变规则语义。选择当前评估会使用的使用指南。
    target = root / "docs" / "guides" / "using-agentic-dev.md"
    if not target.is_file():
        raise ValueError(f"{case['id']}: stale fixture 缺少目标规范性源")
    with target.open("a", encoding="utf-8") as handle:
        handle.write("\n")
    return root


def b_query_result(
    index: dict[str, Any], case: dict[str, Any], temp_root: Path
) -> tuple[dict[str, Any], int, Path]:
    source_root = ROOT
    if case.get("fixture") == "semantic-noop-source-drift":
        source_root = stale_fixture_root(index, case, temp_root)

    stale = check_sources(index, source_root)
    if stale:
        return (
            {
                "fallback_required": True,
                "fallback_reason": "indexed_source_stale_or_missing",
                "stale_sources": stale,
                "query": case["b_query"],
                "results": [],
                "metrics": {"indexed_entries": len(index["entries"]), "result_count": 0},
            },
            2,
            source_root,
        )

    payload, exit_code = query_index(index, case["b_query"])
    return payload, exit_code, source_root


def visible_runtime_case(case: dict[str, Any], hidden_fields: set[str]) -> dict[str, Any]:
    visible = {
        "scenario_id": case["id"],
        "prompt": case["prompt"],
        "metric_focus": case.get("metric_focus", []),
    }
    leaked = hidden_fields & set(visible)
    if leaked:
        raise ValueError(f"{case['id']}: 运行时字段泄漏：{', '.join(sorted(leaked))}")
    return visible


def prepare_workspace(
    design: dict[str, Any],
    index: dict[str, Any],
    case: dict[str, Any],
    variant: str,
    workspace: Path,
    temp_root: Path,
) -> tuple[list[str], dict[str, Any] | None]:
    if variant not in VARIANTS:
        raise ValueError(f"未知变体：{variant}")

    hidden_fields = set(design["runtime_answer_fields_hidden"])
    runtime_case = visible_runtime_case(case, hidden_fields)
    context_paths: list[str] = []
    query_payload: dict[str, Any] | None = None

    if variant == "A":
        for relative in case["a_context_paths"]:
            context_paths.append(copy_declared_path(case, relative, workspace))
    else:
        query_payload, _, source_root = b_query_result(index, case, temp_root)
        query_file = workspace / "retrieval-result.json"
        query_file.write_text(
            json.dumps(query_payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        context_paths.append("retrieval-result.json")

        # Consumer-local 项目事实始终由使用方本地 Authority 提供；它不是
        # agentic-dev 派生索引的一部分，也不能被上游检索结果替代。
        for relative in case["a_context_paths"]:
            if Path(relative).parts and Path(relative).parts[0] == "fixture":
                context_paths.append(copy_declared_path(case, relative, workspace, source_root))

        if query_payload["fallback_required"]:
            # 回退意味着直接读取当前仓库权威。为保持 A/B 题面公平，使用
            # C1 已声明的强 A 组文件集，而不是临时猜测新的回退文件。
            for relative in case["a_context_paths"]:
                if relative in context_paths:
                    continue
                context_paths.append(copy_declared_path(case, relative, workspace, source_root))
        else:
            for result in query_payload["results"]:
                context_paths.append(materialize_result_excerpt(result, workspace, source_root))

    runtime_case["variant"] = variant
    runtime_case["context_paths"] = context_paths
    runtime_file = workspace / "runtime-input.json"
    runtime_file.write_text(
        json.dumps(runtime_case, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    context_paths.append("runtime-input.json")
    return context_paths, query_payload


def validate_design(design: dict[str, Any], index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    hidden = design.get("runtime_answer_fields_hidden")
    if not isinstance(hidden, list) or not all(isinstance(item, str) for item in hidden):
        return ["runtime_answer_fields_hidden 必须是字符串列表"]
    hidden_fields = set(hidden)
    required_hidden = {
        "expected_behavior",
        "assertions",
        "b_expected_rule_keys",
        "b_expected_fallback",
        "b_expected_fallback_reason",
    }
    if not required_hidden.issubset(hidden_fields):
        errors.append("隐藏答案字段集合不完整")

    cases = design.get("scenarios")
    if not isinstance(cases, list) or not cases:
        return errors + ["scenarios 必须是非空列表"]

    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            errors.append("scenario 必须是对象")
            continue
        missing = REQUIRED_SCENARIO_FIELDS - set(case)
        if missing:
            errors.append(f"scenario 缺少字段：{', '.join(sorted(missing))}")
            continue
        scenario_id = case["id"]
        if not isinstance(scenario_id, str) or not scenario_id:
            errors.append("scenario.id 必须是非空字符串")
            continue
        if scenario_id in seen:
            errors.append(f"重复 scenario id：{scenario_id}")
        seen.add(scenario_id)
        if not isinstance(case["a_context_paths"], list) or not case["a_context_paths"]:
            errors.append(f"{scenario_id}: a_context_paths 必须非空")
        for relative in case["a_context_paths"]:
            try:
                resolve_declared_path(case, relative)
            except ValueError as exc:
                errors.append(str(exc))

    index_errors = validate_index(index)
    errors.extend(f"rule-index: {error}" for error in index_errors)
    if not index_errors:
        stale = check_sources(index, ROOT)
        errors.extend(
            f"rule-index 当前来源陈旧：{item['path']} ({item['reason']})" for item in stale
        )
    return errors


def validate_static_behavior(design: dict[str, Any], index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    hidden_fields = set(design["runtime_answer_fields_hidden"])

    for case in design["scenarios"]:
        scenario_id = case["id"]
        with tempfile.TemporaryDirectory(prefix=f"agentic-dev-c2-{scenario_id}-") as temp_dir:
            temp_root = Path(temp_dir)
            payload, exit_code, _ = b_query_result(index, case, temp_root)
            actual_keys = [item["entry_key"] for item in payload.get("results", [])]
            expected_keys = case["b_expected_rule_keys"]
            if actual_keys != expected_keys:
                errors.append(
                    f"{scenario_id}: B 命中键不一致：actual={actual_keys}, expected={expected_keys}"
                )
            expected_fallback = case["b_expected_fallback"]
            if payload.get("fallback_required") is not expected_fallback:
                errors.append(
                    f"{scenario_id}: fallback 不一致：actual={payload.get('fallback_required')}, "
                    f"expected={expected_fallback}"
                )
            expected_reason = case.get("b_expected_fallback_reason")
            if expected_reason is not None and payload.get("fallback_reason") != expected_reason:
                errors.append(
                    f"{scenario_id}: fallback_reason 不一致：actual={payload.get('fallback_reason')}, "
                    f"expected={expected_reason}"
                )
            if expected_fallback and exit_code != 2:
                errors.append(f"{scenario_id}: 预期回退时查询退出码必须为 2")
            if not expected_fallback and exit_code != 0:
                errors.append(f"{scenario_id}: 不回退场景查询退出码必须为 0")

            for variant in sorted(VARIANTS):
                workspace = temp_root / f"workspace-{variant}"
                workspace.mkdir(parents=True, exist_ok=True)
                context_paths, _ = prepare_workspace(
                    design, index, case, variant, workspace, temp_root
                )
                runtime_text = (workspace / "runtime-input.json").read_text(encoding="utf-8")
                for field in hidden_fields:
                    if f'"{field}"' in runtime_text:
                        errors.append(f"{scenario_id}/{variant}: runtime-input 泄漏隐藏字段 {field}")
                for relative in context_paths:
                    if not (workspace / relative).is_file():
                        errors.append(f"{scenario_id}/{variant}: 缺少运行时上下文 {relative}")

    return errors


def build_prompt(case: dict[str, Any], variant: str, context_paths: list[str]) -> str:
    context_list = "\n".join(f"- {path}" for path in context_paths)
    return (
        "这是规则检索与激活隔离 A/B 评估。\n"
        f"当前变体：{variant}。\n"
        "先读取以下当前工作区上下文；这些文件与本提示构成本场景全部可用上下文，"
        "不要读取当前工作目录之外的路径：\n"
        f"{context_list}\n\n"
        f"{case['prompt']}"
    )


def selected_cases(design: dict[str, Any], selected: set[str] | None) -> list[dict[str, Any]]:
    cases = design["scenarios"]
    known = {case["id"] for case in cases}
    if selected:
        unknown = selected - known
        if unknown:
            raise ValueError(f"未知场景：{', '.join(sorted(unknown))}")
        return [case for case in cases if case["id"] in selected]
    return cases


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="规则检索与激活 A/B 评估基线运行器")
    parser.add_argument("--validate-only", action="store_true", help="只执行 C2 静态校验，不运行 Agent")
    parser.add_argument("--run", action="store_true", help="显式执行 C3 Codex A/B；C2 不使用")
    parser.add_argument("--scenario", action="append", default=[], help="只处理指定场景，可重复")
    parser.add_argument("--variant", choices=["A", "B"], action="append", default=[], help="只处理指定变体")
    parser.add_argument("--codex-bin", default=os.environ.get("CODEX_BIN", "codex"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.validate_only and args.run:
        print("--validate-only 与 --run 不能同时使用", file=sys.stderr)
        return 64

    try:
        design = load_json(DESIGN)
        index = load_json(INDEX)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"无法读取评估设计或索引：{exc}", file=sys.stderr)
        return 64

    errors = validate_design(design, index)
    if not errors:
        errors.extend(validate_static_behavior(design, index))
    if errors:
        print("C2 静态校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"C2 静态校验通过：{len(design['scenarios'])} 个场景，A/B 工作区均可装配。")
    print("隐藏断言未进入 runtime-input；B 查询结果与 C1 冻结预期一致。")

    if not args.run:
        print("未执行 Agent A/B。真正的新上下文运行与人工语义评分属于 C3。")
        return 0

    selected = set(args.scenario) or None
    try:
        cases = selected_cases(design, selected)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 64
    variants = args.variant or ["A", "B"]
    check_codex(args.codex_bin)

    failures = 0
    for case in cases:
        for variant in variants:
            with tempfile.TemporaryDirectory(
                prefix=f"agentic-dev-rule-retrieval-{case['id']}-{variant}-"
            ) as temp_dir:
                temp_root = Path(temp_dir)
                workspace = temp_root / "workspace"
                workspace.mkdir(parents=True, exist_ok=True)
                context_paths, _ = prepare_workspace(
                    design, index, case, variant, workspace, temp_root
                )
                prompt = build_prompt(case, variant, context_paths)
                run_id = f"{case['id']}-{variant}"
                failures += run_codex(
                    codex_bin=args.codex_bin,
                    scenario_id=run_id,
                    prompt=prompt,
                    result_group=RESULT_GROUP,
                    cwd=workspace,
                    skip_git_repo_check=True,
                ) != 0

    if failures:
        print(f"Codex 进程失败数：{failures}", file=sys.stderr)
        return 1
    print("所有选中 A/B Codex 进程均正常结束。")
    print("仍需人工逐项按隐藏断言评分；进程退出码 0 不等于语义通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
