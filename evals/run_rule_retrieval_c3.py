#!/usr/bin/env python3
"""规则检索与激活 C3 隔离运行时执行器。

C2 runner 负责静态装配；本文件只服务 C3 真正 A/B：
- 每个场景 / 变体使用独立新 Codex exec；
- A/B 任务正文相同，Agent 可见路径不包含变体身份；
- 每个 run 设置独立 log_dir，从同一次真实 turn 的运行日志提取 model / reasoning effort；
- 只有 A/B 两侧实际运行时事实均可观察且完全一致，才标记为可比较；
- 进程退出与公平性证据都不自动等于语义 PASS，人工隐藏断言评分仍是必需步骤。

本执行器保持 eval 原型性质，不创建新的 Repository Authority。
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

from query_rule_index import load_json
from run_codex_evals import RESULTS, check_codex
from run_rule_retrieval_ab import (
    DESIGN,
    INDEX,
    RESULT_GROUP,
    RESULT_SCHEMA,
    VARIANTS,
    build_prompt,
    prepare_workspace,
    validate_design,
    validate_static,
)

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_FACTS_SOURCE = "isolated-codex-log-turn-span"
MODEL_RE = re.compile(r'\bmodel=(?:"([^"]+)"|([^\s}:]+))')
EFFORT_RE = re.compile(r'\bcodex\.turn\.reasoning_effort=(?:"([^"]+)"|([^\s}:]+))')


def first_group(match: re.Match[str] | None) -> str | None:
    if match is None:
        return None
    return next((value for value in match.groups() if value is not None), None)


def extract_thread_id(jsonl_text: str) -> str | None:
    """从 exec --json 的 thread.started 事件取得主线程 ID。"""
    for line in jsonl_text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "thread.started" and isinstance(event.get("thread_id"), str):
            return event["thread_id"]
    return None


def parse_runtime_facts(log_text: str, thread_id: str | None) -> dict[str, Any]:
    """从同一次隔离 Codex 日志中的 turn span 读取实际 model / effort。

    若主线程 ID 可取得，只接受包含该 ID 的 turn 行；否则只在整份隔离日志恰好
    出现一个唯一事实对时接受。任何多值都标记 ambiguous，禁止推断。
    """
    pairs: set[tuple[str, str]] = set()
    for line in log_text.splitlines():
        if "codex.turn.reasoning_effort=" not in line or "model=" not in line:
            continue
        if thread_id is not None and thread_id not in line:
            continue
        model = first_group(MODEL_RE.search(line))
        effort = first_group(EFFORT_RE.search(line))
        if model and effort:
            pairs.add((model, effort))

    if len(pairs) == 1:
        model, effort = next(iter(pairs))
        return {
            "status": "observed",
            "model": model,
            "reasoning_effort": effort,
        }
    if len(pairs) > 1:
        return {
            "status": "ambiguous",
            "model": None,
            "reasoning_effort": None,
        }
    return {
        "status": "unavailable",
        "model": None,
        "reasoning_effort": None,
    }


def runtime_log_path(log_dir: Path) -> Path:
    return log_dir / "codex-tui.log"


def run_codex_c3(
    *,
    codex_bin: str,
    prompt: str,
    cwd: Path,
    log_dir: Path,
    requested_model: str,
    requested_reasoning_effort: str,
) -> tuple[int, str, str, int]:
    """执行一次真实 C3 turn；返回退出码、stdout JSONL、stderr 与耗时。"""
    log_dir.mkdir(parents=True, exist_ok=True)
    command = [
        codex_bin,
        "exec",
        "--ephemeral",
        "--json",
        "--skip-git-repo-check",
        "--model",
        requested_model,
        "--config",
        f'model_reasoning_effort="{requested_reasoning_effort}"',
        "--config",
        f'log_dir="{log_dir}"',
        "--config",
        'web_search="disabled"',
        "-C",
        str(cwd),
        prompt,
    ]

    runtime_env = os.environ.copy()
    runtime_env["PWD"] = str(cwd)
    runtime_env.pop("OLDPWD", None)
    for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"):
        runtime_env.pop(key, None)

    started = time.monotonic_ns()
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=runtime_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    elapsed_ms = (time.monotonic_ns() - started) // 1_000_000
    return completed.returncode, completed.stdout, completed.stderr, elapsed_ms


def result_path(scenario_id: str, variant: str) -> Path:
    return RESULTS / RESULT_GROUP / f"{scenario_id}-{variant}.result.json"


def write_run_artifacts(
    *,
    case: dict[str, Any],
    variant: str,
    returncode: int,
    stdout: str,
    stderr: str,
    elapsed_ms: int,
    query_payload: dict[str, Any] | None,
    requested_model: str,
    requested_reasoning_effort: str,
    runtime_log: Path,
) -> dict[str, Any]:
    result_dir = RESULTS / RESULT_GROUP
    result_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{case['id']}-{variant}"

    jsonl_path = result_dir / f"{stem}.jsonl"
    stderr_path = result_dir / f"{stem}.stderr.txt"
    runtime_copy = result_dir / f"{stem}.runtime.log"
    jsonl_path.write_text(stdout, encoding="utf-8")
    stderr_path.write_text(stderr, encoding="utf-8")

    if runtime_log.is_file():
        shutil.copy2(runtime_log, runtime_copy)
        log_text = runtime_log.read_text(encoding="utf-8", errors="replace")
    else:
        runtime_copy.write_text("", encoding="utf-8")
        log_text = ""

    thread_id = extract_thread_id(stdout)
    facts = parse_runtime_facts(log_text, thread_id)

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
        "wall_clock_ms": elapsed_ms,
        "file_read_count": None,
        "rule_bytes_or_lines_read": None,
        "query_invocations": 1 if query_payload is not None else 0,
        "model": facts["model"],
        "reasoning_effort": facts["reasoning_effort"],
        "requested_model": requested_model,
        "requested_reasoning_effort": requested_reasoning_effort,
        "runtime_facts_status": facts["status"],
        "runtime_facts_source": RUNTIME_FACTS_SOURCE,
        "pair_fairness_status": "pending",
        "grading_status": "pending",
    }
    result_path(case["id"], variant).write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return result


def update_pair_fairness(case_id: str, results: dict[str, dict[str, Any]]) -> str:
    a = results["A"]
    b = results["B"]
    if a["runtime_facts_status"] != "observed" or b["runtime_facts_status"] != "observed":
        status = "insufficient"
    elif (a["model"], a["reasoning_effort"]) != (b["model"], b["reasoning_effort"]):
        status = "mismatch"
    else:
        status = "comparable"

    for variant in VARIANTS:
        path = result_path(case_id, variant)
        payload = load_json(path)
        payload["pair_fairness_status"] = status
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return status


def validate_runtime_parser() -> list[str]:
    errors: list[str] = []
    thread_id = "019f0000-0000-7000-8000-000000000001"
    observed = parse_runtime_facts(
        (
            '2026-09-09T00:00:00Z INFO turn{otel.name="session_task.turn" '
            f'thread.id={thread_id} model=gpt-5.6-sol '
            'codex.turn.reasoning_effort=high}: ok\n'
        ),
        thread_id,
    )
    if observed != {"status": "observed", "model": "gpt-5.6-sol", "reasoning_effort": "high"}:
        errors.append(f"runtime facts observed 解析失败：{observed}")

    ambiguous = parse_runtime_facts(
        (
            f'turn{{thread.id={thread_id} model=gpt-5.6-sol codex.turn.reasoning_effort=high}}\n'
            f'turn{{thread.id={thread_id} model=gpt-5.6-terra codex.turn.reasoning_effort=high}}\n'
        ),
        thread_id,
    )
    if ambiguous["status"] != "ambiguous":
        errors.append(f"runtime facts ambiguous 解析失败：{ambiguous}")

    unavailable = parse_runtime_facts("no turn facts\n", thread_id)
    if unavailable["status"] != "unavailable":
        errors.append(f"runtime facts unavailable 解析失败：{unavailable}")

    try:
        schema = load_json(RESULT_SCHEMA)
    except (OSError, json.JSONDecodeError) as exc:
        return errors + [f"result schema 无法读取：{exc}"]
    properties = schema.get("properties", {})
    for field in (
        "requested_model",
        "requested_reasoning_effort",
        "runtime_facts_status",
        "runtime_facts_source",
        "pair_fairness_status",
    ):
        if field not in properties:
            errors.append(f"result schema 缺少 C3 字段：{field}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="规则检索与激活 C3 隔离运行时执行器")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--validate-only", action="store_true", help="只做 C3 Readiness 静态校验")
    mode.add_argument("--run", action="store_true", help="执行真实 C3 A/B；仍需后续人工评分")
    parser.add_argument("--scenario", action="append", default=[], help="定向场景；可重复")
    parser.add_argument("--model", help="C3 A/B 两侧共同请求的 Codex 模型")
    parser.add_argument("--reasoning-effort", help="C3 A/B 两侧共同请求的推理强度")
    parser.add_argument("--codex-bin", default=os.environ.get("CODEX_BIN", "codex"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        design = load_json(DESIGN)
        index = load_json(INDEX)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"无法读取 C1 设计或规则索引：{exc}", file=sys.stderr)
        return 64

    errors = validate_design(design, index)
    if not errors:
        errors.extend(validate_static(design, index))
    errors.extend(validate_runtime_parser())
    if errors:
        print("C3 Readiness 静态校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("C3 Readiness 静态校验通过：C2 装配、runtime-facts 解析与结果契约一致。")
    if not args.run:
        print("未执行真实 Agent A/B。")
        return 0

    if not args.model or not args.reasoning_effort:
        print("--run 必须同时提供 --model 与 --reasoning-effort；请求值不能替代实际运行证据。", file=sys.stderr)
        return 64

    selected = set(args.scenario)
    known = {case["id"] for case in design["scenarios"]}
    unknown = selected - known
    if unknown:
        print(f"未知场景：{', '.join(sorted(unknown))}", file=sys.stderr)
        return 64
    cases = [case for case in design["scenarios"] if not selected or case["id"] in selected]

    check_codex(args.codex_bin)
    RESULTS.mkdir(parents=True, exist_ok=True)

    process_failures = 0
    fairness_failures = 0
    for case in cases:
        pair_results: dict[str, dict[str, Any]] = {}
        for variant in VARIANTS:
            # 临时路径只暴露场景 ID，不包含 A/B；随机后缀提供独立工作区。
            with tempfile.TemporaryDirectory(
                prefix=f"agentic-dev-rule-retrieval-{case['id']}-"
            ) as temp:
                temp_root = Path(temp)
                workspace = temp_root / "workspace"
                log_dir = temp_root / "runtime-log"
                workspace.mkdir(parents=True, exist_ok=True)
                contexts, query_payload = prepare_workspace(
                    design, index, case, variant, workspace, temp_root
                )
                prompt = build_prompt(case, contexts)
                returncode, stdout, stderr, elapsed_ms = run_codex_c3(
                    codex_bin=args.codex_bin,
                    prompt=prompt,
                    cwd=workspace,
                    log_dir=log_dir,
                    requested_model=args.model,
                    requested_reasoning_effort=args.reasoning_effort,
                )
                result = write_run_artifacts(
                    case=case,
                    variant=variant,
                    returncode=returncode,
                    stdout=stdout,
                    stderr=stderr,
                    elapsed_ms=elapsed_ms,
                    query_payload=query_payload,
                    requested_model=args.model,
                    requested_reasoning_effort=args.reasoning_effort,
                    runtime_log=runtime_log_path(log_dir),
                )
                pair_results[variant] = result
                process_failures += returncode != 0
                print(
                    f"[{case['id']}] turn 完成；runtime facts="
                    f"{result['runtime_facts_status']}"
                )

        fairness = update_pair_fairness(case["id"], pair_results)
        print(f"[{case['id']}] A/B fairness={fairness}")
        fairness_failures += fairness != "comparable"

    if process_failures:
        print(f"C3 Codex 进程失败数：{process_failures}", file=sys.stderr)
        return 1
    if fairness_failures:
        print(
            f"C3 公平性证据不足或不一致的场景数：{fairness_failures}；这些配对不得进入效果比较。",
            file=sys.stderr,
        )
        return 2

    print("全部选中 A/B 配对已取得一致的实际模型 / 推理强度证据。")
    print("语义评分仍为 pending；进程成功与公平性成立都不等于 Eval PASS。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
