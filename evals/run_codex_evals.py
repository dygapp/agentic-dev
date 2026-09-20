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
- saves raw JSONL/stdout, stderr, source commit, and Codex CLI version;
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
import zipfile
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
RELEASE_BUILDER = ROOT / "tools" / "release-build" / "release_build.py"
RUN_CONTEXT = {
    "source_commit": None,
    "codex_version": None,
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
    """Copy only current Skill packages into an external eval workspace."""
    skill_root = workspace / ".agents" / "skills"
    skill_root.mkdir(parents=True, exist_ok=True)

    for skill_dir in iter_skill_dirs():
        shutil.copytree(skill_dir, skill_root / skill_dir.name)


def _safe_extract_release(archive: Path, destination: Path) -> None:
    destination = destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "r") as zf:
        for info in zf.infolist():
            target = (destination / info.filename).resolve()
            if target != destination and destination not in target.parents:
                raise RuntimeError(f"Release archive path escapes extraction root: {info.filename}")
        zf.extractall(destination)


def build_release_package(source_commit: str):
    """Build one exact-source Release package outside the repository for runtime evals."""
    temp_context = tempfile.TemporaryDirectory(prefix="agentic-dev-eval-release-")
    temp_root = Path(temp_context.name)
    output_dir = temp_root / "output"
    release_version = f"0.0.0-eval.{source_commit[:12]}"
    completed = subprocess.run(
        [
            sys.executable,
            str(RELEASE_BUILDER),
            "build",
            "--repo-root",
            str(ROOT),
            "--output-dir",
            str(output_dir),
            "--source-sha",
            source_commit,
            "--release-version",
            release_version,
            "--evidence-locator",
            "codex-runtime-eval:exact-subject",
        ],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        temp_context.cleanup()
        raise RuntimeError(
            "Release build failed for runtime eval "
            f"({completed.returncode}): {completed.stdout}\n{completed.stderr}"
        )
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        temp_context.cleanup()
        raise RuntimeError(
            f"Release builder did not emit JSON: {completed.stdout}"
        ) from exc

    archive = output_dir / result["archive"]
    package_root = temp_root / "package"
    _safe_extract_release(archive, package_root)
    return temp_context, package_root, result


def install_release_runtime(workspace: Path, package_root: Path) -> None:
    """Install the built Release into an isolated Consumer-like eval workspace."""
    if not (workspace / ".git").exists():
        completed = subprocess.run(
            ["git", "init", "-q"],
            cwd=workspace,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"Cannot initialize eval Consumer repository: {completed.stderr}"
            )

    agents = workspace / "AGENTS.md"
    if not agents.exists():
        agents.write_text(
            "# Consumer Repository Authority\n\n"
            "The current workspace and prompt are the complete Consumer context. "
            "Do not access upstream agentic-dev Source state.\n",
            encoding="utf-8",
        )

    completed = subprocess.run(
        [
            sys.executable,
            str(package_root / "install.py"),
            "--target",
            str(workspace),
        ],
        cwd=workspace,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "Release install failed for runtime eval "
            f"({completed.returncode}): {completed.stdout}\n{completed.stderr}"
        )
    if not (workspace / ".agents/release/manifest.json").is_file():
        raise RuntimeError("Release install did not create installed manifest")


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


def write_run_metadata(
    result_dir: Path,
    scenario_id: str,
    command: list[str],
    cwd: Path,
    returncode: int,
) -> None:
    source_commit = RUN_CONTEXT["source_commit"]
    codex_version = RUN_CONTEXT["codex_version"]
    if not source_commit or not codex_version:
        raise RuntimeError("Run context is incomplete; source commit / Codex version missing")

    metadata = {
        "scenario_id": scenario_id,
        "source_commit": source_commit,
        "codex_version": codex_version,
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
    release_package: Path | None = None,
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
            if release_package is None:
                populate_isolated_skill_copies(cwd)
            else:
                install_release_runtime(cwd, release_package)
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
    release_package: Path | None = None,
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

            workspace_write = False
            prompt = f"${skill_name} {case['prompt']}"

            if scenario_id == "B-EU-01":
                copy_fixture_into(cwd)
                workspace_write = True
                prompt = (
                    "$execute-unit 读取当前目录的 AGENTS.md 和 unit.md，只实现 "
                    "greeting-01，并按仓库规则验证；完成后记录当前证据并停止。"
                )

            if release_package is None:
                populate_isolated_skill_copies(cwd)
            else:
                install_release_runtime(cwd, release_package)

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
        help="run V4 Rule Discovery discriminating corpus",
    )
    mode.add_argument(
        "--all",
        action="store_true",
        help="run Skill activation then Skill behavior corpora (historical behavior)",
    )
    parser.add_argument(
        "--scenario",
        action="append",
        default=[],
        help="run only the given scenario id; repeat for multiple ids",
    )
    parser.add_argument(
        "--release-runtime",
        action="store_true",
        help="build and install the exact-source Release before activation/behavior scenarios",
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

    if args.release_runtime and args.discovery:
        print("--release-runtime is not valid with --discovery", file=sys.stderr)
        return 2

    RUN_CONTEXT["source_commit"] = current_source_commit()
    RUN_CONTEXT["codex_version"] = check_codex(args.codex_bin)
    print(f"Source commit: {RUN_CONTEXT['source_commit']}")

    RESULTS.mkdir(parents=True, exist_ok=True)

    release_context = None
    release_package = None
    try:
        if args.release_runtime:
            release_context, release_package, release_result = build_release_package(
                RUN_CONTEXT["source_commit"]
            )
            print(
                "Release runtime: "
                f"{release_result['release_id']} "
                f"archive_sha256={release_result['archive_sha256']}"
            )

        if args.activation:
            failures = run_activation(args.codex_bin, selected, release_package)
        elif args.behavior:
            failures = run_behavior(args.codex_bin, selected, release_package)
        elif args.discovery:
            failures = run_discovery(args.codex_bin, selected)
        else:
            failures = run_activation(args.codex_bin, selected, release_package)
            failures += run_behavior(args.codex_bin, selected, release_package)
    finally:
        if release_context is not None:
            release_context.cleanup()

    if failures:
        print(f"Codex process failures: {failures}", file=sys.stderr)
        return 1

    print("All selected Codex processes exited successfully.")
    print("Semantic grading is still required; process exit 0 is not an Eval PASS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
