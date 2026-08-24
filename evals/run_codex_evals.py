#!/usr/bin/env python3
"""Run first-pass agentic-dev Skill evals with fresh Codex CLI sessions.

This runner deliberately stays thin:
- one `codex exec --ephemeral --json` process per scenario;
- activation and behavior runs use external temporary workspaces containing only Skill copies;
- the Codex process cwd/PWD matches the isolated workspace so repository paths do not leak through the launcher;
- behavior runs use explicit Skill invocation;
- B-EU-01 additionally receives a fresh writable fixture and its final snapshot is preserved;
- saves raw JSONL/stdout and stderr;
- does NOT grade semantic assertions automatically.

No third-party Python packages are required.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
ACTIVATION_FILE = EVALS / "activation" / "core-first-pass.json"
BEHAVIOR_FILES = [
    EVALS / "behavior" / "clarify-intent.json",
    EVALS / "behavior" / "specify.json",
    EVALS / "behavior" / "technical-plan.json",
    EVALS / "behavior" / "slice-work.json",
    EVALS / "behavior" / "readiness-check.json",
    EVALS / "behavior" / "execute-unit.json",
    EVALS / "behavior" / "systematic-debug.json",
    EVALS / "behavior" / "converge.json",
]
RESULTS = EVALS / "results"
WORKSPACE = EVALS / "workspace"
FIXTURE = EVALS / "fixtures" / "execute-unit-basic"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def iter_skill_dirs() -> Iterable[Path]:
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file():
            yield skill_dir


def populate_isolated_skill_copies(workspace: Path) -> None:
    """Copy only current Skill packages into an external eval workspace."""
    skill_root = workspace / ".agents" / "skills"
    skill_root.mkdir(parents=True, exist_ok=True)

    for skill_dir in iter_skill_dirs():
        shutil.copytree(skill_dir, skill_root / skill_dir.name)


def copy_fixture_into(workspace: Path) -> None:
    """Copy the executable B-EU-01 fixture into an isolated workspace root."""
    for source in FIXTURE.iterdir():
        target = workspace / source.name
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)


def preserve_execute_fixture_snapshot(workspace: Path) -> None:
    """Persist only fixture files after B-EU-01; exclude runtime-only directories."""
    target = WORKSPACE / "B-EU-01"
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)

    excluded = {".agents", ".codex", ".git"}
    for source in workspace.iterdir():
        if source.name in excluded:
            continue
        destination = target / source.name
        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)


def check_codex(codex_bin: str) -> None:
    try:
        completed = subprocess.run(
            [codex_bin, "--version"],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(f"Codex CLI not found: {codex_bin}") from exc

    if completed.returncode != 0:
        raise RuntimeError(
            f"Codex CLI version check failed ({completed.returncode}): "
            f"{completed.stderr.strip()}"
        )

    version = completed.stdout.strip() or completed.stderr.strip()
    print(f"Codex: {version}")


def write_run_metadata(
    result_dir: Path,
    scenario_id: str,
    command: list[str],
    cwd: Path,
    returncode: int,
) -> None:
    metadata = {
        "scenario_id": scenario_id,
        "cwd": str(cwd.relative_to(ROOT)) if cwd.is_relative_to(ROOT) else str(cwd),
        "command": command,
        "returncode": returncode,
        "grading": "pending",
    }
    (result_dir / f"{scenario_id}.run.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def run_codex(
    *,
    codex_bin: str,
    scenario_id: str,
    prompt: str,
    result_group: str,
    cwd: Path,
    workspace_write: bool = False,
    skip_git_repo_check: bool = False,
) -> int:
    result_dir = RESULTS / result_group
    result_dir.mkdir(parents=True, exist_ok=True)

    command = [codex_bin, "exec", "--ephemeral", "--json"]
    if workspace_write:
        command.extend(["--sandbox", "workspace-write"])
    if skip_git_repo_check:
        command.append("--skip-git-repo-check")
    command.extend(["-C", str(cwd), prompt])

    runtime_env = os.environ.copy()
    runtime_env["PWD"] = str(cwd)
    runtime_env.pop("OLDPWD", None)
    for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"):
        runtime_env.pop(key, None)

    print(f"[{scenario_id}] fresh codex exec")
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=runtime_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )

    (result_dir / f"{scenario_id}.jsonl").write_text(
        completed.stdout,
        encoding="utf-8",
    )
    (result_dir / f"{scenario_id}.stderr.txt").write_text(
        completed.stderr,
        encoding="utf-8",
    )
    write_run_metadata(result_dir, scenario_id, command, cwd, completed.returncode)

    status = "OK" if completed.returncode == 0 else f"EXIT {completed.returncode}"
    print(f"[{scenario_id}] {status}")
    return completed.returncode


def activation_cases() -> list[dict]:
    return load_json(ACTIVATION_FILE)


def behavior_cases() -> Iterable[tuple[str, dict]]:
    for path in BEHAVIOR_FILES:
        document = load_json(path)
        skill_name = document["skill_name"]
        for case in document["evals"]:
            yield skill_name, case


def run_activation(codex_bin: str, selected: set[str] | None) -> int:
    failures = 0

    for case in activation_cases():
        scenario_id = case["id"]
        if selected and scenario_id not in selected:
            continue

        with tempfile.TemporaryDirectory(
            prefix=f"agentic-dev-activation-{scenario_id}-"
        ) as temp_dir:
            cwd = Path(temp_dir)
            populate_isolated_skill_copies(cwd)
            failures += run_codex(
                codex_bin=codex_bin,
                scenario_id=scenario_id,
                prompt=case["query"],
                result_group="activation",
                cwd=cwd,
                skip_git_repo_check=True,
            ) != 0

    return failures


def run_behavior(codex_bin: str, selected: set[str] | None) -> int:
    failures = 0

    for skill_name, case in behavior_cases():
        scenario_id = case["id"]
        if selected and scenario_id not in selected:
            continue

        with tempfile.TemporaryDirectory(
            prefix=f"agentic-dev-behavior-{scenario_id}-"
        ) as temp_dir:
            cwd = Path(temp_dir)
            populate_isolated_skill_copies(cwd)

            workspace_write = False
            prompt = f"${skill_name} {case['prompt']}"

            if scenario_id == "B-EU-01":
                copy_fixture_into(cwd)
                workspace_write = True
                prompt = (
                    "$execute-unit 读取当前目录的 AGENTS.md 和 unit.md，只实现 "
                    "greeting-01，并按仓库规则验证；完成后记录当前证据并停止。"
                )

            failed = run_codex(
                codex_bin=codex_bin,
                scenario_id=scenario_id,
                prompt=prompt,
                result_group="behavior",
                cwd=cwd,
                workspace_write=workspace_write,
                skip_git_repo_check=True,
            ) != 0
            failures += failed

            if scenario_id == "B-EU-01":
                preserve_execute_fixture_snapshot(cwd)

    return failures


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run first-pass agentic-dev Skill evals with fresh Codex CLI sessions."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--activation", action="store_true", help="run activation corpus")
    mode.add_argument("--behavior", action="store_true", help="run behavior corpus")
    mode.add_argument("--all", action="store_true", help="run activation then behavior")
    parser.add_argument(
        "--scenario",
        action="append",
        default=[],
        help="run only the given scenario id; repeat for multiple ids",
    )
    parser.add_argument(
        "--codex-bin",
        default=os.environ.get("CODEX_BIN", "codex"),
        help="Codex CLI executable (default: CODEX_BIN or codex)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.scenario) or None

    known = {case["id"] for case in activation_cases()}
    known.update(case["id"] for _, case in behavior_cases())
    if selected:
        unknown = selected - known
        if unknown:
            print(f"Unknown scenario id(s): {', '.join(sorted(unknown))}", file=sys.stderr)
            return 2

    check_codex(args.codex_bin)
    RESULTS.mkdir(parents=True, exist_ok=True)

    if args.activation:
        failures = run_activation(args.codex_bin, selected)
    elif args.behavior:
        failures = run_behavior(args.codex_bin, selected)
    else:
        failures = run_activation(args.codex_bin, selected)
        failures += run_behavior(args.codex_bin, selected)

    if failures:
        print(f"Codex process failures: {failures}", file=sys.stderr)
        return 1

    print("All selected Codex processes exited successfully.")
    print("Semantic grading is still required; process exit 0 is not an Eval PASS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
