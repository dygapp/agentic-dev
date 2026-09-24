#!/usr/bin/env python3
# agentic-dev-distribution: source-only
"""Run agentic-dev Fresh Runtime evals with isolated Codex CLI sessions.

This runner deliberately stays thin:
- one `codex exec --ephemeral --json` process per scenario;
- Skill activation / behavior runs use external temporary workspaces with Skill copies;
- V4 discovery runs copy only current runtime entry files, Rule Discovery, current Rules,
  current Skills, and scenario fixture inputs; grader-only expectations never enter the workspace;
- the Codex process cwd/PWD matches the isolated workspace so repository paths do not leak;
- behavior runs use explicit Skill invocation, while discovery runs do not invent a Skill;
- B-EU-01 additionally receives a fresh writable fixture and its final snapshot is preserved;
- B-GA-01 receives a deterministic stateful Actions fixture so failure diagnosis, minimal repair, new-subject rerun, and re-verification are executable;
- saves raw JSONL/stdout, stderr, source commit, and Codex CLI version;
- does NOT grade semantic assertions automatically.

No third-party Python packages are required.
"""

from __future__ import annotations

import argparse
import hashlib
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
BEHAVIOR_FILES = sorted((EVALS / "behavior").glob("*.json"))
DISCOVERY_FILE = EVALS / "discovery" / "v4-discriminating.json"
AGENTIC_DEV_DISCOVERY_BOOTSTRAP_PATHS = (
    "AGENTS.md",
    "docs/project/project-roadmap.md",
    "docs/project/project-capability-profile.md",
)
RESULTS = EVALS / "results"
WORKSPACE = EVALS / "workspace"
FIXTURE = EVALS / "fixtures" / "execute-unit-basic"
ARCHITECTURE_FIXTURE = EVALS / "fixtures" / "clarify-architecture-basic"
GITHUB_ACTIONS_FIXTURE = EVALS / "fixtures" / "github-actions-observation"
WORKSPACE_WRITE_BEHAVIOR_SCENARIOS = {"B-AR-01", "B-EU-01", "B-GA-01"}
RUN_CONTEXT = {
    "source_commit": None,
    "codex_version": None,
    "skill_set_sha256": None,
    "timeout_seconds": 180,
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def checked_relative_path(relative: str) -> Path:
    relative_path = Path(relative)
    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise RuntimeError(f"Invalid relative path: {relative}")
    return relative_path


def copy_repo_path(workspace: Path, relative: str) -> None:
    relative_path = checked_relative_path(relative)
    source = (ROOT / relative_path).resolve()
    if not source.is_relative_to(ROOT):
        raise RuntimeError(f"Repository context escapes root: {relative}")
    if not source.exists():
        raise RuntimeError(f"Repository context does not exist: {relative}")

    target = workspace / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, target)
    else:
        shutil.copy2(source, target)


def iter_skill_dirs() -> Iterable[Path]:
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file():
            yield skill_dir


def populate_isolated_skill_copies(workspace: Path) -> None:
    """Copy canonical Skill packages plus minimal installed-runtime provenance."""
    agents_root = workspace / ".agents"
    skill_root = agents_root / "skills"
    skill_root.mkdir(parents=True, exist_ok=True)

    for skill_dir in iter_skill_dirs():
        shutil.copytree(skill_dir, skill_root / skill_dir.name)

    source_commit = RUN_CONTEXT.get("source_commit")
    skill_set_sha256 = RUN_CONTEXT.get("skill_set_sha256")
    if source_commit and skill_set_sha256:
        (agents_root / "README.md").write_text(
            "# Installed agentic-dev Skills\n\n"
            f"source_commit: {source_commit}\n"
            f"skill_set_sha256: {skill_set_sha256}\n"
            "runtime_mode: canonical-skill-copy\n"
            "Provider docs are not runtime dependencies.\n",
            encoding="utf-8",
        )


def canonical_skill_set_sha256() -> str:
    digest = hashlib.sha256()
    for skill_dir in iter_skill_dirs():
        for path in sorted(item for item in skill_dir.rglob("*") if item.is_file()):
            relative = path.relative_to(ROOT / "skills").as_posix().encode("utf-8")
            payload = path.read_bytes()
            digest.update(relative)
            digest.update(b"\0")
            digest.update(str(len(payload)).encode("ascii"))
            digest.update(b"\0")
            digest.update(payload)
            digest.update(b"\0")
    return digest.hexdigest()


def ensure_consumer_bootstrap(workspace: Path) -> None:
    """Create the thin Consumer runtime authority when a fixture has none."""
    agents = workspace / "AGENTS.md"
    if agents.exists():
        return
    agents.write_text(
        "# Consumer Repository Authority\n\n"
        "The current workspace and its repository-local installed Skills are the "
        "complete runtime inputs for this scenario.\n"
        "Do not read upstream agentic-dev Provider Source or Provider docs to fill gaps.\n",
        encoding="utf-8",
    )


def materialize_workspace_files(workspace: Path, files: dict[str, str]) -> None:
    """Create scenario input files without exposing the corpus itself to the runtime."""
    for relative, content in files.items():
        relative_path = checked_relative_path(relative)
        target = workspace / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def populate_discovery_context(workspace: Path, case: dict) -> None:
    """Build a minimal V4 ordinary-runtime workspace for one discovery scenario."""
    context_mode = case.get("context_mode", "agentic-dev")

    if context_mode == "agentic-dev":
        selected_method = case.get("selected_method")
        for relative in AGENTIC_DEV_DISCOVERY_BOOTSTRAP_PATHS:
            copy_repo_path(workspace, relative)
        if selected_method is not None:
            if not isinstance(selected_method, str) or not selected_method.strip():
                raise RuntimeError(
                    f"Discovery scenario {case['id']} has invalid selected_method"
                )
            copy_repo_path(workspace, selected_method)
    elif context_mode == "consumer-local":
        # Consumer-local AGENTS/README are scenario inputs. Do not copy upstream project state.
        pass
    else:
        raise RuntimeError(f"Unknown discovery context_mode: {context_mode}")

    copy_repo_path(workspace, "docs/rules")
    copy_repo_path(workspace, "tools/rule-discovery/rule_discovery.py")
    populate_isolated_skill_copies(workspace)
    materialize_workspace_files(workspace, case.get("workspace_files", {}))

    if not (workspace / "AGENTS.md").is_file():
        raise RuntimeError(f"Discovery scenario {case['id']} has no AGENTS.md")


def copy_fixture_into(workspace: Path, fixture: Path = FIXTURE) -> None:
    """Copy one executable behavior fixture into an isolated workspace root."""
    for source in fixture.iterdir():
        target = workspace / source.name
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)


def initialize_local_git_baseline(workspace: Path) -> None:
    """Create a deterministic local-only Git baseline for executable behavior fixtures."""
    env = os.environ.copy()
    env.update(
        {
            "GIT_AUTHOR_NAME": "agentic-dev eval",
            "GIT_AUTHOR_EMAIL": "eval@agentic-dev.invalid",
            "GIT_COMMITTER_NAME": "agentic-dev eval",
            "GIT_COMMITTER_EMAIL": "eval@agentic-dev.invalid",
            "GIT_AUTHOR_DATE": "2000-01-01T00:00:00+00:00",
            "GIT_COMMITTER_DATE": "2000-01-01T00:00:00+00:00",
        }
    )
    for command in (
        ["git", "init", "-q"],
        ["git", "add", "-A"],
        ["git", "commit", "-q", "--no-gpg-sign", "-m", "eval baseline"],
    ):
        completed = subprocess.run(
            command,
            cwd=workspace,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"Cannot create behavior Git baseline ({' '.join(command)}): "
                f"{completed.stderr.strip()}"
            )


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


def current_source_commit() -> str:
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"Cannot resolve evaluation source commit ({completed.returncode}): "
            f"{completed.stderr.strip()}"
        )
    commit = completed.stdout.strip()
    if len(commit) != 40:
        raise RuntimeError(f"Unexpected evaluation source commit: {commit!r}")
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if status.returncode != 0:
        raise RuntimeError(f"Cannot inspect evaluation checkout: {status.stderr.strip()}")
    if status.stdout.strip():
        raise RuntimeError(
            "Fresh Runtime evals require a clean checkout so source_commit binds "
            "the exact Skill subject"
        )
    return commit


def check_codex(codex_bin: str) -> str:
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
    if not version:
        raise RuntimeError("Codex CLI version output is empty")
    print(f"Codex: {version}")
    return version


def _clear_stale_scenario_results(result_dir: Path, scenario_id: str) -> None:
    for suffix in (
        ".jsonl", ".stderr.txt", ".run.json", ".grade.json",
        ".grader.jsonl", ".grader.stderr.txt",
    ):
        target = result_dir / f"{scenario_id}{suffix}"
        if target.exists():
            target.unlink()


def _jsonl_has_turn_completed(output: str) -> bool:
    for line in output.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and event.get("type") == "turn.completed":
            return True
    return False


def write_run_metadata(
    result_dir: Path,
    scenario_id: str,
    command: list[str],
    cwd: Path,
    returncode: int,
    *,
    runtime_mode: str,
    timed_out: bool,
    process_exit_timed_out: bool,
    semantic_completed: bool,
) -> None:
    source_commit = RUN_CONTEXT["source_commit"]
    codex_version = RUN_CONTEXT["codex_version"]
    skill_set_sha256 = RUN_CONTEXT["skill_set_sha256"]
    if not source_commit or not codex_version or not skill_set_sha256:
        raise RuntimeError(
            "Run context is incomplete; source commit / Codex version / "
            "Skill-set digest missing"
        )
    metadata = {
        "schema_version": 2,
        "evidence_kind": "agentic-dev-codex-runtime",
        "scenario_id": scenario_id,
        "source_commit": source_commit,
        "skill_set_sha256": skill_set_sha256,
        "codex_version": codex_version,
        "runtime_mode": runtime_mode,
        "cwd": str(cwd.relative_to(ROOT)) if cwd.is_relative_to(ROOT) else str(cwd),
        "command": command,
        "returncode": returncode,
        "timed_out": timed_out,
        "process_exit_timed_out": process_exit_timed_out,
        "semantic_completed": semantic_completed,
        "timeout_seconds": RUN_CONTEXT["timeout_seconds"],
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
    runtime_mode: str = "canonical-skill-copy",
) -> int:
    result_dir = RESULTS / result_group
    result_dir.mkdir(parents=True, exist_ok=True)
    _clear_stale_scenario_results(result_dir, scenario_id)
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
    timed_out = False
    process_exit_timed_out = False
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=runtime_env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
            timeout=int(RUN_CONTEXT["timeout_seconds"]),
        )
        stdout, stderr, returncode = completed.stdout, completed.stderr, completed.returncode
        semantic_completed = _jsonl_has_turn_completed(stdout)
    except subprocess.TimeoutExpired as exc:
        process_exit_timed_out = True
        stdout, stderr = exc.stdout or "", exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        semantic_completed = _jsonl_has_turn_completed(stdout)
        if semantic_completed:
            returncode = 0
            stderr += (
                "\nagentic-dev Codex process-exit timeout after observable "
                "turn.completed; semantic result retained for grading\n"
            )
        else:
            timed_out = True
            returncode = 124
            stderr += (
                f"\nagentic-dev eval timeout after "
                f"{RUN_CONTEXT['timeout_seconds']} seconds before turn.completed\n"
            )

    (result_dir / f"{scenario_id}.jsonl").write_text(stdout, encoding="utf-8")
    (result_dir / f"{scenario_id}.stderr.txt").write_text(stderr, encoding="utf-8")
    write_run_metadata(
        result_dir, scenario_id, command, cwd, returncode,
        runtime_mode=runtime_mode,
        timed_out=timed_out,
        process_exit_timed_out=process_exit_timed_out,
        semantic_completed=semantic_completed,
    )
    if timed_out:
        status = "TIMEOUT"
    elif process_exit_timed_out:
        status = "OK (turn completed; process-exit timeout recorded)"
    else:
        status = "OK" if returncode == 0 else f"EXIT {returncode}"
    print(f"[{scenario_id}] {status}")
    return returncode


def activation_cases() -> list[dict]:
    return load_json(ACTIVATION_FILE)


def behavior_cases() -> Iterable[tuple[str, dict]]:
    for path in BEHAVIOR_FILES:
        document = load_json(path)
        skill_name = document["skill_name"]
        for case in document["evals"]:
            yield skill_name, case


def discovery_cases() -> list[dict]:
    document = load_json(DISCOVERY_FILE)
    return document["evals"]


def scenario_ids_for_mode(args: argparse.Namespace) -> set[str]:
    activation_ids = {case["id"] for case in activation_cases()}
    behavior_ids = {case["id"] for _, case in behavior_cases()}
    discovery_ids = {case["id"] for case in discovery_cases()}

    if args.activation:
        return activation_ids
    if args.behavior:
        return behavior_ids
    if args.discovery:
        return discovery_ids
    return activation_ids | behavior_ids


def run_activation(
    codex_bin: str,
    selected: set[str] | None,
) -> int:
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
            ensure_consumer_bootstrap(cwd)
            failures += run_codex(
                codex_bin=codex_bin,
                scenario_id=scenario_id,
                prompt=case["query"],
                result_group="activation",
                cwd=cwd,
                skip_git_repo_check=True,
            ) != 0
    return failures


def run_behavior(
    codex_bin: str,
    selected: set[str] | None,
) -> int:
    failures = 0
    for skill_name, case in behavior_cases():
        scenario_id = case["id"]
        if selected and scenario_id not in selected:
            continue
        with tempfile.TemporaryDirectory(
            prefix=f"agentic-dev-behavior-{scenario_id}-"
        ) as temp_dir:
            cwd = Path(temp_dir)
            workspace_write = scenario_id in WORKSPACE_WRITE_BEHAVIOR_SCENARIOS
            prompt = "$" + skill_name + " " + case["prompt"]

            if scenario_id == "B-EU-01":
                copy_fixture_into(cwd)
                prompt = (
                    "$execute-unit 读取当前目录的 AGENTS.md 和 unit.md，只实现 "
                    "greeting-01，并按仓库规则验证；完成后记录当前证据并停止。"
                )
            elif scenario_id == "B-AR-01":
                copy_fixture_into(cwd, ARCHITECTURE_FIXTURE)
            elif scenario_id == "B-GA-01":
                copy_fixture_into(cwd, GITHUB_ACTIONS_FIXTURE)

            ensure_consumer_bootstrap(cwd)
            populate_isolated_skill_copies(cwd)
            initialize_local_git_baseline(cwd)
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


def run_discovery(codex_bin: str, selected: set[str] | None) -> int:
    failures = 0

    for case in discovery_cases():
        scenario_id = case["id"]
        if selected and scenario_id not in selected:
            continue

        with tempfile.TemporaryDirectory(
            prefix=f"agentic-dev-discovery-{scenario_id}-"
        ) as temp_dir:
            cwd = Path(temp_dir)
            populate_discovery_context(cwd, case)

            prompt = (
                "这是一个隔离 Fresh Runtime 场景。当前工作目录中的文件与本提示构成"
                "本次全部可用 Repository Context；不要读取或搜索当前工作目录之外的路径，"
                "也不要访问网络。先读取 AGENTS.md，再像普通 Agent 一样处理任务。\n\n"
                f"{case['prompt']}"
            )

            failures += run_codex(
                codex_bin=codex_bin,
                scenario_id=scenario_id,
                prompt=prompt,
                result_group="discovery",
                cwd=cwd,
                skip_git_repo_check=True,
                runtime_mode="legacy-provider-discovery",
            ) != 0

    return failures


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run agentic-dev Fresh Runtime evals with isolated Codex sessions."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--activation", action="store_true", help="run Skill activation corpus")
    mode.add_argument("--behavior", action="store_true", help="run Skill behavior corpus")
    mode.add_argument(
        "--discovery",
        action="store_true",
        help="run legacy Provider Rule Discovery corpus during P5/P6 transition",
    )
    mode.add_argument(
        "--all",
        action="store_true",
        help="run Skill activation then Skill behavior corpora",
    )
    parser.add_argument(
        "--scenario",
        action="append",
        default=[],
        help="run only the given scenario id; repeat for multiple ids",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=180,
        help="per-scenario Codex process timeout (default: 180)",
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
    if args.timeout_seconds <= 0:
        print("--timeout-seconds must be positive", file=sys.stderr)
        return 2

    available = scenario_ids_for_mode(args)
    if not available:
        print("No scenarios are available for the selected mode.", file=sys.stderr)
        return 2

    if selected:
        unavailable = selected - available
        if unavailable:
            print(
                "Scenario id(s) not available in the selected mode: "
                + ", ".join(sorted(unavailable)),
                file=sys.stderr,
            )
            return 2

    RUN_CONTEXT["source_commit"] = current_source_commit()
    RUN_CONTEXT["codex_version"] = check_codex(args.codex_bin)
    RUN_CONTEXT["skill_set_sha256"] = canonical_skill_set_sha256()
    RUN_CONTEXT["timeout_seconds"] = args.timeout_seconds
    print(f"Source commit: {RUN_CONTEXT['source_commit']}")
    print(f"Skill set SHA-256: {RUN_CONTEXT['skill_set_sha256']}")

    RESULTS.mkdir(parents=True, exist_ok=True)

    if args.activation:
        failures = run_activation(args.codex_bin, selected)
    elif args.behavior:
        failures = run_behavior(args.codex_bin, selected)
    elif args.discovery:
        failures = run_discovery(args.codex_bin, selected)
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
