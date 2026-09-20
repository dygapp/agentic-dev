#!/usr/bin/env python3
# agentic-dev-distribution: source-only
"""Run the V4-07 20/100/500 Rule scaling gate with isolated Fresh Codex sessions."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "evals" / "discovery" / "v4-scaling.json"
RESULTS = ROOT / "evals" / "results" / "scaling"
CANONICAL_SIGNALS = {
    "phases": ["execute"],
    "activities": ["implementation"],
    "technologies": [],
    "artifacts": ["code", "data-access"],
    "risks": [],
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def checked_relative_path(relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise RuntimeError(f"Invalid relative path: {relative}")
    return path


def copy_repo_path(workspace: Path, relative: str) -> None:
    relative_path = checked_relative_path(relative)
    source = (ROOT / relative_path).resolve()
    if not source.is_relative_to(ROOT) or not source.exists():
        raise RuntimeError(f"Invalid repository context path: {relative}")
    target = workspace / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, target)
    else:
        shutil.copy2(source, target)


def populate_skills(workspace: Path) -> None:
    target_root = workspace / ".agents" / "skills"
    target_root.mkdir(parents=True, exist_ok=True)
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file():
            shutil.copytree(skill_dir, target_root / skill_dir.name)


def decoy_rule(index: int) -> str:
    return f"""---
id: rule:scale-decoy-{index:04d}
type: rule
status: active
scope:
  phases: [specification]
  activities: [review]
  technologies: [java]
  artifacts: [documentation]
  risks: []
---

# Scaling Decoy {index:04d}

Synthetic V4-07 non-matching Rule. It exists only to increase tool-side metadata scan size.
"""


def populate_scaling_workspace(workspace: Path, document: dict, case: dict) -> None:
    for relative in (
        "AGENTS.md",
        "README.md",
        "docs/project/project-roadmap.md",
        "tools/rule-discovery/rule_discovery.py",
    ):
        copy_repo_path(workspace, relative)

    populate_skills(workspace)

    target_paths = document["target_rule_paths"]
    rule_count = case["rule_count"]
    if rule_count < len(target_paths):
        raise RuntimeError("Scaling rule_count is smaller than required target Rule count")

    for relative in target_paths:
        copy_repo_path(workspace, relative)

    decoy_root = workspace / "docs" / "rules" / "scaling"
    decoy_root.mkdir(parents=True, exist_ok=True)
    for index in range(1, rule_count - len(target_paths) + 1):
        (decoy_root / f"decoy-{index:04d}.md").write_text(decoy_rule(index), encoding="utf-8")

    (workspace / "task.md").write_text(document["common_task"], encoding="utf-8")

    actual = sum(1 for path in (workspace / "docs" / "rules").rglob("*.md") if path.is_file())
    if actual != rule_count:
        raise RuntimeError(f"Scaling fixture count mismatch: expected {rule_count}, found {actual}")


def current_source_commit() -> str:
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True, check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"Cannot resolve source commit: {completed.stderr.strip()}")
    commit = completed.stdout.strip()
    if len(commit) != 40:
        raise RuntimeError(f"Unexpected source commit: {commit!r}")
    return commit


def codex_version(codex_bin: str) -> str:
    try:
        completed = subprocess.run(
            [codex_bin, "--version"], cwd=ROOT, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True, check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(f"Codex CLI not found: {codex_bin}") from exc
    if completed.returncode != 0:
        raise RuntimeError(f"Codex version check failed: {completed.stderr.strip()}")
    version = completed.stdout.strip() or completed.stderr.strip()
    if not version:
        raise RuntimeError("Codex version output is empty")
    return version


def preflight_discovery(workspace: Path) -> dict:
    command = [
        "python3", "tools/rule-discovery/rule_discovery.py", "--repo-root", ".", "discover",
        "--signals-json", json.dumps(CANONICAL_SIGNALS, separators=(",", ":")),
    ]
    completed = subprocess.run(
        command, cwd=workspace, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"Scaling preflight discovery failed ({completed.returncode}): "
            f"{completed.stdout.strip()} {completed.stderr.strip()}"
        )
    payload = json.loads(completed.stdout)
    return {
        "scanned": payload["scanned"],
        "candidate_count": payload["candidate_count"],
        "candidate_ids": [item["id"] for item in payload["candidates"]],
    }


def extract_usage(stdout: str) -> dict | None:
    usage = None
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "turn.completed" and isinstance(event.get("usage"), dict):
            usage = event["usage"]
    return usage


def run_case(codex_bin: str, document: dict, case: dict, source_commit: str, version: str) -> int:
    scenario_id = case["id"]
    with tempfile.TemporaryDirectory(prefix=f"agentic-dev-scaling-{scenario_id}-") as temp_dir:
        workspace = Path(temp_dir)
        populate_scaling_workspace(workspace, document, case)
        preflight = preflight_discovery(workspace)

        expected_ids = sorted(document["expected_candidate_ids"])
        if preflight["scanned"] != case["rule_count"]:
            raise RuntimeError(f"{scenario_id}: preflight scanned mismatch: {preflight}")
        if preflight["candidate_count"] != len(expected_ids):
            raise RuntimeError(f"{scenario_id}: preflight candidate count mismatch: {preflight}")
        if sorted(preflight["candidate_ids"]) != expected_ids:
            raise RuntimeError(f"{scenario_id}: preflight candidate identity mismatch: {preflight}")

        prompt = (
            "这是一个隔离 Fresh Runtime scaling 场景。当前工作目录中的文件与本提示构成本次全部"
            "可用 Repository Context；不要读取或搜索当前工作目录之外的路径，也不要访问网络。"
            "先读取 AGENTS.md，再像普通 Agent 一样处理任务。\n\n"
            + document["common_prompt"]
        )
        command = [
            codex_bin, "exec", "--ephemeral", "--json", "--skip-git-repo-check",
            "-C", str(workspace), prompt,
        ]
        env = os.environ.copy()
        env["PWD"] = str(workspace)
        env.pop("OLDPWD", None)
        for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"):
            env.pop(key, None)

        completed = subprocess.run(
            command, cwd=workspace, env=env, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True, check=False,
        )

        RESULTS.mkdir(parents=True, exist_ok=True)
        (RESULTS / f"{scenario_id}.jsonl").write_text(completed.stdout, encoding="utf-8")
        (RESULTS / f"{scenario_id}.stderr.txt").write_text(completed.stderr, encoding="utf-8")
        metadata = {
            "scenario_id": scenario_id,
            "source_commit": source_commit,
            "codex_version": version,
            "rule_count": case["rule_count"],
            "fixture_preflight": preflight,
            "usage": extract_usage(completed.stdout),
            "stdout_bytes": len(completed.stdout.encode("utf-8")),
            "cwd": str(workspace),
            "command": command,
            "returncode": completed.returncode,
            "grading": "pending",
        }
        (RESULTS / f"{scenario_id}.run.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

        status = "OK" if completed.returncode == 0 else f"EXIT {completed.returncode}"
        usage = metadata["usage"] or {}
        print(
            f"[{scenario_id}] {status}; rules={case['rule_count']}; "
            f"candidates={preflight['candidate_count']}; input_tokens={usage.get('input_tokens')}"
        )
        return completed.returncode


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run V4-07 Rule Discovery token-scaling evals")
    parser.add_argument("--scenario", action="append", default=[])
    parser.add_argument("--codex-bin", default=os.environ.get("CODEX_BIN", "codex"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    document = load_json(CORPUS)
    cases = document["evals"]
    known = {case["id"] for case in cases}
    selected = set(args.scenario) or known
    unknown = selected - known
    if unknown:
        print(f"Unknown scaling scenario(s): {', '.join(sorted(unknown))}", file=os.sys.stderr)
        return 2

    source_commit = current_source_commit()
    version = codex_version(args.codex_bin)
    print(f"Source commit: {source_commit}")
    print(f"Codex: {version}")

    failures = 0
    for case in cases:
        if case["id"] not in selected:
            continue
        failures += run_case(args.codex_bin, document, case, source_commit, version) != 0

    if failures:
        print(f"Codex process failures: {failures}", file=os.sys.stderr)
        return 1
    print("All selected scaling processes exited successfully. Semantic/token grading is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
