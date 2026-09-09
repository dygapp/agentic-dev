#!/usr/bin/env python3
"""规则检索与激活 A/B 评估基线运行器。

默认只做 C2 静态校验；只有显式 --run 才执行 C3 Codex 新上下文。
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

from query_rule_index import check_sources, load_json, query_index, unique_sources, validate_index
from run_codex_evals import RESULTS, check_codex, run_codex

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
DESIGN = EVALS / "rule-retrieval" / "targeted-evaluation-design.json"
INDEX = EVALS / "rule-retrieval" / "rule-index.json"
FIXTURES = EVALS / "rule-retrieval" / "fixtures"
RESULT_SCHEMA = EVALS / "rule-retrieval" / "result-schema.json"
RESULT_GROUP = "rule-retrieval"
VARIANTS = ("A", "B")
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
REQUIRED_SHARED_FLAGS = {
    "fresh_context",
    "isolated_workdir",
    "same_model",
    "same_reasoning_effort",
    "same_task_prompt",
    "process_exit_is_not_semantic_pass",
    "human_assertion_scoring_required",
}


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"不安全的相对路径：{value}")
    return path


def case_fixture_root(case: dict[str, Any]) -> Path | None:
    name = case.get("fixture")
    if not name or name == "semantic-noop-source-drift":
        return None
    if not isinstance(name, str):
        raise ValueError(f"{case.get('id', '<unknown>')}: fixture 必须是字符串")
    root = FIXTURES / name
    if not root.is_dir():
        raise ValueError(f"{case['id']}: fixture 不存在：{name}")
    return root


def resolve_context_source(
    case: dict[str, Any], relative: str, preferred_root: Path = ROOT
) -> Path:
    rel = safe_relative(relative)
    if rel.parts and rel.parts[0] == "fixture":
        fixture = case_fixture_root(case)
        if fixture is None:
            raise ValueError(f"{case['id']}: fixture/ 路径没有对应 fixture")
        source = fixture.joinpath(*rel.parts[1:])
    else:
        # 该参数只服务制造 / 读取临时来源视图；真正 fallback 装配会显式
        # 传 ROOT，确保陈旧索引源不会继续作为 Agent 的规则上下文。
        preferred = preferred_root / rel
        source = preferred if preferred.is_file() else ROOT / rel
    source = source.resolve()
    if not source.is_file():
        raise ValueError(f"{case['id']}: 上下文文件不存在：{relative}")
    return source


def copy_context(
    case: dict[str, Any], relative: str, workspace: Path, preferred_root: Path = ROOT
) -> str:
    source = resolve_context_source(case, relative, preferred_root)
    target = workspace / safe_relative(relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return relative


def section_numbers(spec: str) -> list[str]:
    numbers: list[str] = []
    spans: list[tuple[int, int]] = []
    range_pattern = re.compile(r"§(\d+)\.(\d+)\s*[～~-]\s*§?(\d+)\.(\d+)")
    for match in range_pattern.finditer(spec):
        major_a, minor_a, major_b, minor_b = match.groups()
        if major_a != major_b or int(minor_b) < int(minor_a):
            raise ValueError(f"不支持的章节范围：{match.group(0)}")
        for minor in range(int(minor_a), int(minor_b) + 1):
            value = f"{major_a}.{minor}"
            if value not in numbers:
                numbers.append(value)
        spans.append((match.start(), match.end()))
    for match in re.finditer(r"§(\d+(?:\.\d+)?)", spec):
        if any(start <= match.start() < end for start, end in spans):
            continue
        value = match.group(1)
        if value not in numbers:
            numbers.append(value)
    return numbers


def extract_numbered_section(text: str, number: str) -> str:
    lines = text.splitlines(keepends=True)
    pattern = re.compile(rf"^(#{{1,6}})\s+{re.escape(number)}(?:\.|\s|$)")
    start = level = None
    for index, line in enumerate(lines):
        match = pattern.match(line)
        if match:
            start, level = index, len(match.group(1))
            break
    if start is None or level is None:
        raise ValueError(f"无法解析源章节 §{number}")
    end = len(lines)
    heading = re.compile(r"^(#{1,6})\s+")
    for index in range(start + 1, len(lines)):
        match = heading.match(lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return "".join(lines[start:end]).rstrip() + "\n"


def materialize_result(result: dict[str, Any], workspace: Path, source_root: Path) -> str:
    pointer = result["source_pointer"]
    source = (source_root / safe_relative(pointer["path"])).resolve()
    if not source.is_file():
        source = (ROOT / safe_relative(pointer["path"])).resolve()
    if not source.is_file():
        raise ValueError(f"规范性源不存在：{pointer['path']}")
    text = source.read_text(encoding="utf-8")
    numbers = section_numbers(pointer["section"])
    body = (
        "\n\n".join(extract_numbered_section(text, number).rstrip() for number in numbers)
        + "\n"
        if numbers
        else text
    )
    relative = Path("retrieved") / f"{result['entry_key']}.md"
    target = workspace / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        "<!-- 派生评估上下文；"
        f"source={pointer['path']}；section={pointer['section']}；identity={pointer['identity']} -->\n"
        + body,
        encoding="utf-8",
    )
    return relative.as_posix()


def copy_index_sources(index: dict[str, Any], root: Path) -> None:
    for source in unique_sources(index):
        rel = safe_relative(source["path"])
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, target)


def build_stale_root(index: dict[str, Any], temp_root: Path) -> Path:
    root = temp_root / "stale-source-root"
    copy_index_sources(index, root)
    target = root / "docs" / "guides" / "using-agentic-dev.md"
    with target.open("a", encoding="utf-8") as handle:
        handle.write("\n")
    return root


def run_b_query(
    index: dict[str, Any], case: dict[str, Any], temp_root: Path
) -> tuple[dict[str, Any], int, Path]:
    source_root = (
        build_stale_root(index, temp_root)
        if case.get("fixture") == "semantic-noop-source-drift"
        else ROOT
    )
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


def prepare_workspace(
    design: dict[str, Any],
    index: dict[str, Any],
    case: dict[str, Any],
    variant: str,
    workspace: Path,
    temp_root: Path,
) -> tuple[list[str], dict[str, Any] | None]:
    contexts: list[str] = []
    query_payload: dict[str, Any] | None = None
    if variant == "A":
        for relative in case["a_context_paths"]:
            contexts.append(copy_context(case, relative, workspace))
    elif variant == "B":
        query_payload, _, source_root = run_b_query(index, case, temp_root)
        (workspace / "retrieval-result.json").write_text(
            json.dumps(query_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        contexts.append("retrieval-result.json")

        # Consumer-local 项目事实不属于上游规则索引，B 组也必须保留。
        for relative in case["a_context_paths"]:
            if safe_relative(relative).parts[:1] == ("fixture",):
                contexts.append(copy_context(case, relative, workspace, source_root))

        if query_payload["fallback_required"]:
            # fallback 的意义是停止信任派生索引及其临时来源视图，重新从
            # 当前仓库 Authority 装配规则上下文。即使 stale-root 中存在同名
            # 文件，也不得继续把该陈旧副本交给 Agent。
            for relative in case["a_context_paths"]:
                if relative not in contexts:
                    contexts.append(copy_context(case, relative, workspace, ROOT))
        else:
            for result in query_payload["results"]:
                contexts.append(materialize_result(result, workspace, source_root))
    else:
        raise ValueError(f"未知变体：{variant}")

    # Agent 不应知道自己属于 A 还是 B，也不暴露 metric_focus。运行时文件
    # 只保存场景身份与允许读取的上下文列表，分组信息留在外部结果记录。
    visible = {"scenario_id": case["id"], "context_paths": contexts}
    (workspace / "runtime-input.json").write_text(
        json.dumps(visible, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    contexts.append("runtime-input.json")
    return contexts, query_payload


def validate_design(design: dict[str, Any], index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    hidden = set(design.get("runtime_answer_fields_hidden", []))
    required_hidden = {
        "expected_behavior",
        "assertions",
        "b_expected_rule_keys",
        "b_expected_fallback",
        "b_expected_fallback_reason",
    }
    if not required_hidden.issubset(hidden):
        errors.append("隐藏答案字段集合不完整")

    shared = design.get("shared_run_contract", {})
    for flag in REQUIRED_SHARED_FLAGS:
        if shared.get(flag) is not True:
            errors.append(f"shared_run_contract.{flag} 必须为 true")

    if not RESULT_SCHEMA.is_file():
        errors.append("缺少 result-schema.json")
    else:
        try:
            schema = load_json(RESULT_SCHEMA)
            required = set(schema.get("required", []))
            expected_required = set(design.get("required_result_fields", []))
            if not expected_required.issubset(required):
                errors.append("result-schema 未覆盖 C1 required_result_fields")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"result-schema 无效：{exc}")

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
        if scenario_id in seen:
            errors.append(f"重复 scenario id：{scenario_id}")
        seen.add(scenario_id)
        for relative in case["a_context_paths"]:
            try:
                resolve_context_source(case, relative)
            except ValueError as exc:
                errors.append(str(exc))

    index_errors = validate_index(index)
    errors.extend(f"rule-index: {error}" for error in index_errors)
    if not index_errors:
        for stale in check_sources(index, ROOT):
            errors.append(f"rule-index 当前来源陈旧：{stale['path']} ({stale['reason']})")
    return errors


def validate_static(design: dict[str, Any], index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    hidden = set(design["runtime_answer_fields_hidden"])
    forbidden_runtime_names = hidden | {"variant", "metric_focus", "expected_behavior"}
    for case in design["scenarios"]:
        with tempfile.TemporaryDirectory(prefix=f"agentic-dev-c2-{case['id']}-") as temp:
            temp_root = Path(temp)
            payload, exit_code, _ = run_b_query(index, case, temp_root)
            actual_keys = [item["entry_key"] for item in payload.get("results", [])]
            if actual_keys != case["b_expected_rule_keys"]:
                errors.append(
                    f"{case['id']}: B keys actual={actual_keys}, expected={case['b_expected_rule_keys']}"
                )
            if payload.get("fallback_required") is not case["b_expected_fallback"]:
                errors.append(f"{case['id']}: fallback 与 C1 冻结预期不一致")
            expected_reason = case.get("b_expected_fallback_reason")
            if expected_reason is not None and payload.get("fallback_reason") != expected_reason:
                errors.append(f"{case['id']}: fallback_reason 与 C1 冻结预期不一致")
            if exit_code != (2 if case["b_expected_fallback"] else 0):
                errors.append(f"{case['id']}: 查询退出码与回退语义不一致")

            for variant in VARIANTS:
                workspace = temp_root / f"workspace-{variant}"
                workspace.mkdir(parents=True, exist_ok=True)
                contexts, query_payload = prepare_workspace(
                    design, index, case, variant, workspace, temp_root
                )
                runtime_text = (workspace / "runtime-input.json").read_text(encoding="utf-8")
                for field in forbidden_runtime_names:
                    if f'"{field}"' in runtime_text:
                        errors.append(f"{case['id']}/{variant}: runtime-input 泄漏 {field}")
                for relative in contexts:
                    if not (workspace / relative).is_file():
                        errors.append(f"{case['id']}/{variant}: 缺少上下文 {relative}")

                # B 发生 fallback 时，所有声明上下文必须与当前仓库 / 当前
                # fixture 一致；这直接防止 stale-root 中的同名陈旧规则被继续消费。
                if variant == "B" and query_payload and query_payload["fallback_required"]:
                    for relative in case["a_context_paths"]:
                        target = workspace / safe_relative(relative)
                        current = resolve_context_source(case, relative, ROOT)
                        if not target.is_file() or target.read_bytes() != current.read_bytes():
                            errors.append(
                                f"{case['id']}/B: fallback 未从当前 Authority 装配 {relative}"
                            )
    return errors


def build_prompt(case: dict[str, Any], contexts: list[str]) -> str:
    listing = "\n".join(f"- {path}" for path in contexts)
    return (
        "这是规则检索与激活隔离评估。\n"
        "先读取以下当前工作区上下文；这些文件与本提示构成本场景全部可用上下文，"
        "不要读取当前工作目录之外的路径：\n"
        f"{listing}\n\n{case['prompt']}"
    )


def write_result_stub(
    case: dict[str, Any], variant: str, returncode: int, query_payload: dict[str, Any] | None
) -> None:
    result_dir = RESULTS / RESULT_GROUP
    result_dir.mkdir(parents=True, exist_ok=True)
    result = {
        "scenario_id": case["id"],
        "variant": variant,
        "process_exit_code": returncode,
        "semantic_assertions_passed": None,
        "semantic_assertions_total": len(case["assertions"]),
        "semantic_pass": None,
        "authority_confusion": None,
        "wrong_stop_or_escalation": None,
        "wrong_execution": None,
        "files_read": None,
        "tool_calls": None,
        "retrieved_rule_keys": (
            [item["entry_key"] for item in query_payload.get("results", [])]
            if query_payload is not None
            else None
        ),
        "fallback_required": (
            query_payload.get("fallback_required") if query_payload is not None else None
        ),
        "fallback_reason": (
            query_payload.get("fallback_reason") if query_payload is not None else None
        ),
        "failure_classification": None,
        "input_tokens": None,
        "output_tokens": None,
        "wall_clock_ms": None,
        "file_read_count": None,
        "rule_bytes_or_lines_read": None,
        "query_invocations": 1 if query_payload is not None else 0,
        # 实际模型 / 推理强度必须由 C3 运行证据填写；不能把环境变量
        # 或请求配置冒充成实际执行事实。
        "model": None,
        "reasoning_effort": None,
        "grading_status": "pending",
    }
    path = result_dir / f"{case['id']}-{variant}.result.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="规则检索与激活 A/B 基线运行器")
    parser.add_argument("--validate-only", action="store_true", help="只做 C2 静态校验")
    parser.add_argument("--run", action="store_true", help="显式执行 C3 Codex A/B")
    parser.add_argument("--scenario", action="append", default=[])
    parser.add_argument("--variant", choices=VARIANTS, action="append", default=[])
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
        print(f"无法读取设计或索引：{exc}", file=sys.stderr)
        return 64

    errors = validate_design(design, index)
    if not errors:
        errors.extend(validate_static(design, index))
    if errors:
        print("C2 静态校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"C2 静态校验通过：{len(design['scenarios'])} 个场景的 A/B 工作区均可装配。")
    print("隐藏答案和 A/B 分组未进入 runtime-input；B 查询与 C1 冻结命中 / 回退一致。")
    if not args.run:
        print("未执行 Agent A/B；真正的新上下文运行与人工语义评分属于 C3。")
        return 0

    selected = set(args.scenario)
    known = {case["id"] for case in design["scenarios"]}
    unknown = selected - known
    if unknown:
        print(f"未知场景：{', '.join(sorted(unknown))}", file=sys.stderr)
        return 64
    cases = [case for case in design["scenarios"] if not selected or case["id"] in selected]
    variants = args.variant or list(VARIANTS)
    check_codex(args.codex_bin)

    failures = 0
    for case in cases:
        for variant in variants:
            # 临时目录可能被 Agent 作为当前工作目录观察到，因此路径中不能
            # 暴露 A/B 分组。变体身份只保留在运行器外部控制与结果记录中。
            with tempfile.TemporaryDirectory(
                prefix=f"agentic-dev-rule-retrieval-{case['id']}-"
            ) as temp:
                temp_root = Path(temp)
                workspace = temp_root / "workspace"
                workspace.mkdir(parents=True, exist_ok=True)
                contexts, query_payload = prepare_workspace(
                    design, index, case, variant, workspace, temp_root
                )
                returncode = run_codex(
                    codex_bin=args.codex_bin,
                    scenario_id=f"{case['id']}-{variant}",
                    prompt=build_prompt(case, contexts),
                    result_group=RESULT_GROUP,
                    cwd=workspace,
                    skip_git_repo_check=True,
                )
                write_result_stub(case, variant, returncode, query_payload)
                failures += returncode != 0

    if failures:
        print(f"Codex 进程失败数：{failures}", file=sys.stderr)
        return 1
    print("所有选中 A/B Codex 进程均正常结束；仍需人工按隐藏断言评分。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
