#!/usr/bin/env python3
# agentic-dev-distribution: source-only
"""Automatically grade selected Codex behavior eval outputs after isolated runtime execution."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
BEHAVIOR_FILES = sorted((EVALS / "behavior").glob("*.json"))
RESULTS = EVALS / "results" / "behavior"


class GradeError(RuntimeError):
    pass


def load_behavior_cases() -> dict[str, dict[str, Any]]:
    cases: dict[str, dict[str, Any]] = {}
    for path in BEHAVIOR_FILES:
        document = json.loads(path.read_text(encoding="utf-8"))
        skill_name = document["skill_name"]
        for case in document["evals"]:
            scenario_id = case["id"]
            if scenario_id in cases:
                raise GradeError(f"duplicate behavior scenario id: {scenario_id}")
            cases[scenario_id] = {"skill_name": skill_name, **case}
    return cases


def extract_last_agent_message(jsonl: str) -> str:
    last: str | None = None
    completed = False
    for line in jsonl.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        if event.get("type") == "turn.completed":
            completed = True
        item = event.get("item")
        if (
            event.get("type") == "item.completed"
            and isinstance(item, dict)
            and item.get("type") == "agent_message"
            and isinstance(item.get("text"), str)
        ):
            last = item["text"]
    if not completed:
        raise GradeError("runtime JSONL has no turn.completed event")
    if not last:
        raise GradeError("runtime JSONL has no agent_message")
    return last


def parse_json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    try:
        payload = json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise GradeError(f"grader final message is not JSON: {stripped}") from exc
    if not isinstance(payload, dict):
        raise GradeError("grader final JSON is not an object")
    return payload


def run_grader(
    codex_bin: str,
    scenario: dict[str, Any],
    runtime_output: str,
    *,
    timeout_seconds: int,
) -> tuple[dict[str, Any], str, str]:
    assertions = scenario.get("assertions")
    if not isinstance(assertions, list) or not assertions:
        raise GradeError(f"{scenario['id']} has no grading assertions")

    prompt = f"""你是隔离的 Eval Grader，只评估给定 Runtime 输出，不执行被评任务，不读取外部文件或网络。

场景 ID：{scenario['id']}
Skill：{scenario['skill_name']}

期望行为：
{scenario['expected_behavior']}

逐项 Assertions：
{json.dumps(assertions, ensure_ascii=False, indent=2)}

Runtime 最终输出：
---BEGIN RUNTIME OUTPUT---
{runtime_output}
---END RUNTIME OUTPUT---

要求：
1. 只能根据 Runtime 输出判断，不补充它没有表达的事实；
2. 每条 assertion 分别判定；
3. 只有全部 assertions 都有充分证据时 verdict 才能是 PASS；
4. FAIL 时指出最小缺口；
5. 最终只输出 JSON，不要 Markdown fence，格式必须严格为：
{{
  "scenario_id": "{scenario['id']}",
  "verdict": "PASS" 或 "FAIL",
  "assertions": [
    {{"index": 1, "passed": true 或 false, "evidence": "简短依据"}}
  ],
  "summary": "简短结论"
}}
"""

    with tempfile.TemporaryDirectory(prefix="agentic-dev-eval-grader-") as temp:
        cwd = Path(temp)
        env = os.environ.copy()
        env["CODEX_HOME"] = str(cwd / "codex-home")
        (cwd / "codex-home").mkdir()
        command = [
            codex_bin,
            "exec",
            "--ephemeral",
            "--json",
            "--sandbox",
            "read-only",
            "--skip-git-repo-check",
            "-C",
            str(cwd),
            prompt,
        ]
        try:
            completed = subprocess.run(
                command,
                cwd=cwd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired as exc:
            raise GradeError(
                f"grader timed out after {timeout_seconds}s for {scenario['id']}"
            ) from exc

    if completed.returncode != 0:
        raise GradeError(
            f"grader Codex exited {completed.returncode} for {scenario['id']}: "
            f"{completed.stderr}"
        )
    final = extract_last_agent_message(completed.stdout)
    grade = parse_json_object(final)
    return grade, completed.stdout, completed.stderr


def validate_grade(
    scenario: dict[str, Any],
    grade: dict[str, Any],
) -> bool:
    if grade.get("scenario_id") != scenario["id"]:
        raise GradeError(
            f"grader scenario id mismatch: {grade.get('scenario_id')} != {scenario['id']}"
        )
    verdict = grade.get("verdict")
    if verdict not in {"PASS", "FAIL"}:
        raise GradeError(f"invalid grader verdict for {scenario['id']}: {verdict}")

    expected_assertions = scenario["assertions"]
    results = grade.get("assertions")
    if not isinstance(results, list) or len(results) != len(expected_assertions):
        raise GradeError(
            f"grader assertion count mismatch for {scenario['id']}: "
            f"{len(results) if isinstance(results, list) else 'invalid'} "
            f"!= {len(expected_assertions)}"
        )

    all_passed = True
    for position, item in enumerate(results, start=1):
        if not isinstance(item, dict):
            raise GradeError(f"invalid assertion result for {scenario['id']} #{position}")
        if item.get("index") != position:
            raise GradeError(
                f"grader assertion index mismatch for {scenario['id']}: "
                f"{item.get('index')} != {position}"
            )
        if not isinstance(item.get("passed"), bool):
            raise GradeError(
                f"grader assertion result lacks boolean passed for {scenario['id']} #{position}"
            )
        if not isinstance(item.get("evidence"), str) or not item["evidence"].strip():
            raise GradeError(
                f"grader assertion result lacks evidence for {scenario['id']} #{position}"
            )
        all_passed = all_passed and item["passed"]

    if (verdict == "PASS") != all_passed:
        raise GradeError(
            f"grader verdict/assertion inconsistency for {scenario['id']}: {verdict}"
        )
    return all_passed


def grade_selected(
    codex_bin: str,
    selected: list[str],
    *,
    timeout_seconds: int,
) -> dict[str, Any]:
    cases = load_behavior_cases()
    unknown = sorted(set(selected) - set(cases))
    if unknown:
        raise GradeError(f"unknown behavior scenario(s): {unknown}")

    version = subprocess.run(
        [codex_bin, "--version"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if version.returncode != 0:
        raise GradeError(f"cannot read Codex version: {version.stderr}")
    codex_version = version.stdout.strip() or version.stderr.strip()

    results: list[dict[str, Any]] = []
    for scenario_id in selected:
        scenario = cases[scenario_id]
        jsonl_path = RESULTS / f"{scenario_id}.jsonl"
        metadata_path = RESULTS / f"{scenario_id}.run.json"
        if not jsonl_path.is_file() or not metadata_path.is_file():
            raise GradeError(f"missing runtime result for {scenario_id}")

        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if metadata.get("runtime_mode") != "release-installed":
            raise GradeError(
                f"{scenario_id} was not executed in release-installed runtime"
            )
        if not metadata.get("release_id"):
            raise GradeError(f"{scenario_id} runtime metadata has no release_id")
        if metadata.get("returncode") != 0:
            raise GradeError(f"{scenario_id} runtime process did not exit successfully")

        runtime_output = extract_last_agent_message(
            jsonl_path.read_text(encoding="utf-8")
        )
        grade, raw_stdout, raw_stderr = run_grader(
            codex_bin,
            scenario,
            runtime_output,
            timeout_seconds=timeout_seconds,
        )
        passed = validate_grade(scenario, grade)

        grade_record = {
            "scenario_id": scenario_id,
            "skill_name": scenario["skill_name"],
            "runtime_mode": metadata["runtime_mode"],
            "release_id": metadata["release_id"],
            "source_commit": metadata["source_commit"],
            "runtime_codex_version": metadata["codex_version"],
            "grader_codex_version": codex_version,
            "verdict": grade["verdict"],
            "assertions": grade["assertions"],
            "summary": grade.get("summary"),
        }
        (RESULTS / f"{scenario_id}.grade.json").write_text(
            json.dumps(grade_record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (RESULTS / f"{scenario_id}.grader.jsonl").write_text(
            raw_stdout,
            encoding="utf-8",
        )
        (RESULTS / f"{scenario_id}.grader.stderr.txt").write_text(
            raw_stderr,
            encoding="utf-8",
        )

        metadata["grading"] = "pass" if passed else "fail"
        metadata["grader_codex_version"] = codex_version
        metadata_path.write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        results.append(grade_record)

    passed_count = sum(item["verdict"] == "PASS" for item in results)
    summary = {
        "status": "PASS" if passed_count == len(results) else "FAIL",
        "scenario_count": len(results),
        "passed": passed_count,
        "failed": len(results) - passed_count,
        "grader_codex_version": codex_version,
        "scenarios": [
            {
                "id": item["scenario_id"],
                "skill": item["skill_name"],
                "verdict": item["verdict"],
            }
            for item in results
        ],
    }
    (RESULTS / "runtime-acceptance.summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--behavior", action="store_true", required=True)
    parser.add_argument(
        "--scenario",
        action="append",
        required=True,
        help="behavior scenario id; repeat for multiple scenarios",
    )
    parser.add_argument(
        "--codex-bin",
        default=os.environ.get("CODEX_BIN", "codex"),
    )
    parser.add_argument("--timeout-seconds", type=int, default=180)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        summary = grade_selected(
            args.codex_bin,
            args.scenario,
            timeout_seconds=args.timeout_seconds,
        )
    except (GradeError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False))
        return 2

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
