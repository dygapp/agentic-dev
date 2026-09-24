#!/usr/bin/env python3
# agentic-dev-distribution: source-only
"""Validate canonical agentic-dev Skills in an isolated Consumer-like runtime."""

from __future__ import annotations

from contextlib import contextmanager

import argparse
import hashlib
import json
import os
import re
import selectors
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

SKILL_FRONTMATTER_END = "\n---\n"
FORBIDDEN_RUNTIME_NAMESPACES = (
    ".agents/methods",
    ".agents/architecture",
    ".agents/rules",
    ".agents/contracts",
    ".agents/tools",
    ".agents/evals",
    ".agents/release",
)
FORBIDDEN_SKILL_SOURCE_PATHS = (
    "docs/methods/",
    "docs/architecture/",
    "docs/rules/",
    "tools/rule-discovery/",
    "tools/release-build/",
)
class RuntimeAcceptanceError(RuntimeError):
    pass


def _require_codex_cli_allowed() -> None:
    if os.environ.get("WEBCODEX_NPM_WRAPPER") or ".webcodex-managed-worktrees" in str(Path.cwd().resolve()):
        raise RuntimeAcceptanceError(
            "codex-cli execution is disabled in WebCodex Runner context; "
            "run Codex-specific Runtime Under Test only as a separately authorized task "
            "outside WebCodex"
        )


def _run(
    command: list[str],
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeAcceptanceError(
            f"command failed ({completed.returncode}): {' '.join(command)}\n"
            f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
        )
    return completed


def _frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise RuntimeAcceptanceError("SKILL.md has no YAML front matter")
    end = text.find(SKILL_FRONTMATTER_END, 4)
    if end < 0:
        raise RuntimeAcceptanceError("SKILL.md front matter is not closed")
    return text[4:end]


def _scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        value = value[1:-1]
    return value


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _tree_sha256(root: Path) -> str:
    root = root.resolve()
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix().encode("utf-8")
        payload = path.read_bytes()
        digest.update(relative); digest.update(b"\0")
        digest.update(str(len(payload)).encode("ascii")); digest.update(b"\0")
        digest.update(payload); digest.update(b"\0")
    return digest.hexdigest()


def _skill_inventory(skill_root: Path) -> dict[str, dict[str, Any]]:
    skill_root = skill_root.resolve()
    if not skill_root.is_dir():
        raise RuntimeAcceptanceError(f"Skill root is missing: {skill_root}")

    inventory: dict[str, dict[str, Any]] = {}
    for skill_dir in sorted(path for path in skill_root.iterdir() if path.is_dir()):
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.is_file():
            continue
        body = skill_path.read_text(encoding="utf-8")
        frontmatter = _frontmatter(body)
        name = _scalar(frontmatter, "name")
        description = _scalar(frontmatter, "description")
        if not name or not description:
            raise RuntimeAcceptanceError(
                f"Skill {skill_dir.name} must define name and description"
            )
        if name != skill_dir.name:
            raise RuntimeAcceptanceError(
                f"Skill directory/name mismatch: {skill_dir.name} != {name}"
            )
        if name in inventory:
            raise RuntimeAcceptanceError(f"duplicate Skill name: {name}")

        for token in (
            "agentic-dev-release-inputs",
            "agentic-dev-release-target",
            "generated-release-reference",
            "references/release-inputs",
        ):
            if token in body:
                raise RuntimeAcceptanceError(
                    f"Skill {name} still contains retired composition token: {token}"
                )
        for token in FORBIDDEN_SKILL_SOURCE_PATHS:
            if token in body:
                raise RuntimeAcceptanceError(
                    f"Skill {name} depends on provider Source path: {token}"
                )

        inventory[name] = {
            "name": name,
            "description": description,
            "path": skill_path,
            "package_root": skill_dir,
            "package_sha256": _tree_sha256(skill_dir),
            "skill_md_sha256": _sha256_file(skill_path),
        }

    if not inventory:
        raise RuntimeAcceptanceError(f"no Skills found under {skill_root}")
    return inventory


def canonical_skill_inventory(repo_root: Path) -> dict[str, dict[str, Any]]:
    return _skill_inventory(repo_root.resolve() / "skills")


def canonical_skill_set_sha256(repo_root: Path) -> str:
    skill_root = (repo_root.resolve() / "skills").resolve()
    digest = hashlib.sha256()
    for skill_dir in sorted(path for path in skill_root.iterdir() if path.is_dir()):
        if not (skill_dir / "SKILL.md").is_file():
            continue
        for path in sorted(item for item in skill_dir.rglob("*") if item.is_file()):
            relative = path.relative_to(skill_root).as_posix().encode("utf-8")
            payload = path.read_bytes()
            digest.update(relative)
            digest.update(b"\0")
            digest.update(str(len(payload)).encode("ascii"))
            digest.update(b"\0")
            digest.update(payload)
            digest.update(b"\0")
    return digest.hexdigest()


def build_and_install_fixture(
    repo_root: Path,
    work_dir: Path,
    source_sha: str,
) -> dict[str, Any]:
    """Create an isolated Consumer by directly installing canonical Skill packages."""
    repo_root = repo_root.resolve()
    work_dir = work_dir.resolve()
    if work_dir == repo_root or repo_root in work_dir.parents:
        raise RuntimeAcceptanceError(
            "runtime acceptance work directory must be outside the source repository"
        )

    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True)

    source_skills = canonical_skill_inventory(repo_root)
    consumer = work_dir / "consumer"
    consumer.mkdir()
    _run(["git", "init", "-q"], cwd=consumer)

    (consumer / "AGENTS.md").write_text(
        "# Consumer Repository Authority\n\n"
        "Product, requirements, system architecture, technology policy and current state "
        "belong to this Consumer repository.\n"
        "Repository-local Skills live under .agents/skills/**.\n",
        encoding="utf-8",
    )
    (consumer / "docs").mkdir()
    (consumer / "docs/product.md").write_text(
        "# Consumer Product\n\nThis file is Consumer-owned project knowledge.\n",
        encoding="utf-8",
    )

    installed_root = consumer / ".agents" / "skills"
    installed_root.mkdir(parents=True)
    for name, item in source_skills.items():
        shutil.copytree(item["package_root"], installed_root / name)

    return {
        "consumer": consumer,
        "source_skills": source_skills,
        "source_sha": source_sha,
        "skill_set_sha256": canonical_skill_set_sha256(repo_root),
    }


def verify_installed_fixture(
    consumer: Path,
    *,
    expected_skills: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    consumer = consumer.resolve()
    agents_path = consumer / "AGENTS.md"
    product_path = consumer / "docs/product.md"
    if not agents_path.is_file():
        raise RuntimeAcceptanceError("Consumer AGENTS.md is missing")
    if not product_path.is_file():
        raise RuntimeAcceptanceError("Consumer-owned product doc is missing")

    agents = agents_path.read_text(encoding="utf-8")
    product = product_path.read_text(encoding="utf-8")
    if "Consumer Repository Authority" not in agents:
        raise RuntimeAcceptanceError("Consumer AGENTS.md authority sentinel is missing")
    if ".agents/skills/**" not in agents:
        raise RuntimeAcceptanceError("Consumer AGENTS.md missing local Skill locator")
    if "Consumer-owned" not in product:
        raise RuntimeAcceptanceError("Consumer-owned project knowledge was not preserved")

    for forbidden in FORBIDDEN_SKILL_SOURCE_PATHS:
        if forbidden in agents:
            raise RuntimeAcceptanceError(
                f"Consumer AGENTS.md depends on provider Source path: {forbidden}"
            )

    installed = _skill_inventory(consumer / ".agents/skills")
    if expected_skills is not None:
        if set(installed) != set(expected_skills):
            raise RuntimeAcceptanceError(
                "installed Skill inventory mismatch: "
                f"expected={sorted(expected_skills)}, actual={sorted(installed)}"
            )
        for name, expected in expected_skills.items():
            if installed[name]["package_sha256"] != expected["package_sha256"]:
                raise RuntimeAcceptanceError(
                    f"installed Skill package digest mismatch: {name}"
                )

    for namespace in FORBIDDEN_RUNTIME_NAMESPACES:
        if (consumer / namespace).exists():
            raise RuntimeAcceptanceError(
                f"forbidden provider-style runtime namespace installed: {namespace}"
            )
    if (consumer / ".agents/release").exists():
        raise RuntimeAcceptanceError(
            "legacy release runtime namespace installed: .agents/release"
        )

    return {
        "status": "ok",
        "skill_count": len(installed),
        "skills": sorted(installed),
        "skill_paths": [
            f".agents/skills/{name}/SKILL.md" for name in sorted(installed)
        ],
        "skill_package_sha256": {
            name: installed[name]["package_sha256"] for name in sorted(installed)
        },
        "chatgpt_compatibility_path": [
            "AGENTS.md",
            ".agents/skills/<name>/SKILL.md",
        ],
        "progressive_disclosure": {
            "bootstrap_contains_skill_bodies": False,
            "supporting_content_location": ".agents/skills/<name>/**",
        },
        "provider_source_paths_present": False,
    }


@contextmanager
def upstream_source_unavailable(repo_root: Path, runtime_cwd: Path):
    """Make the provider Source tree unreadable while runtime discovery executes."""
    repo_root = repo_root.resolve()
    runtime_cwd = runtime_cwd.resolve()
    if runtime_cwd == repo_root or repo_root in runtime_cwd.parents:
        raise RuntimeAcceptanceError(
            "upstream negative-control runtime must be outside the source repository"
        )
    if os.name != "posix":
        raise RuntimeAcceptanceError(
            "upstream source unavailability negative control requires POSIX permissions"
        )

    original_cwd = Path.cwd()
    original_mode = stat.S_IMODE(repo_root.stat().st_mode)
    disabled = False
    try:
        os.chdir(runtime_cwd)
        repo_root.chmod(0)
        disabled = True
        probe = subprocess.run(
            [
                sys.executable,
                "-c",
                (
                    "from pathlib import Path\n"
                    "import sys\n"
                    "path = Path(sys.argv[1])\n"
                    "try:\n"
                    "    next(path.iterdir(), None)\n"
                    "except (PermissionError, OSError):\n"
                    "    raise SystemExit(0)\n"
                    "raise SystemExit(1)\n"
                ),
                str(repo_root),
            ],
            cwd=runtime_cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if probe.returncode != 0:
            raise RuntimeAcceptanceError(
                "upstream negative control could still read the provider Source tree"
            )
        yield {
            "status": "ok",
            "mechanism": "source-root-permission-denial",
            "provider_source_read_probe": "denied",
        }
    finally:
        if disabled:
            repo_root.chmod(original_mode)
        os.chdir(original_cwd)


def _read_rpc_response(
    process: subprocess.Popen[str],
    selector: selectors.BaseSelector,
    request_id: int,
    timeout_seconds: float,
) -> dict[str, Any]:
    deadline = time.monotonic() + timeout_seconds
    observed: list[dict[str, Any]] = []
    while time.monotonic() < deadline:
        remaining = max(0.0, deadline - time.monotonic())
        events = selector.select(timeout=remaining)
        if not events:
            break
        line = process.stdout.readline() if process.stdout is not None else ""
        if not line:
            if process.poll() is not None:
                break
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            observed.append(payload)
            if payload.get("id") == request_id:
                if "error" in payload:
                    raise RuntimeAcceptanceError(
                        f"Codex app-server request {request_id} failed: {payload['error']}"
                    )
                return payload
    raise RuntimeAcceptanceError(
        f"timed out waiting for Codex app-server response id={request_id}; "
        f"observed={observed[-5:]}"
    )


def _write_rpc(process: subprocess.Popen[str], payload: dict[str, Any]) -> None:
    if process.stdin is None:
        raise RuntimeAcceptanceError("Codex app-server stdin is unavailable")
    process.stdin.write(json.dumps(payload, ensure_ascii=False) + "\n")
    process.stdin.flush()


def codex_native_discovery(
    consumer: Path,
    codex_bin: str,
    *,
    expected_version: str | None = None,
    timeout_seconds: float = 20.0,
) -> dict[str, Any]:
    _require_codex_cli_allowed()
    consumer = consumer.resolve()
    version = _run([codex_bin, "--version"]).stdout.strip()
    if expected_version and expected_version not in version:
        raise RuntimeAcceptanceError(
            f"unexpected Codex version: expected {expected_version!r}, got {version!r}"
        )

    installed = _skill_inventory(consumer / ".agents/skills")
    expected = {
        name: str(item["path"].resolve()) for name, item in installed.items()
    }

    last_error: Exception | None = None
    for attempt in range(2):
        with tempfile.TemporaryDirectory(prefix="agentic-dev-codex-home-") as codex_home:
            env = os.environ.copy()
            env["CODEX_HOME"] = codex_home
            command = [
                codex_bin,
                "-c",
                "skills.bundled.enabled=false",
                "app-server",
                "--listen",
                "stdio://",
            ]
            process = subprocess.Popen(
                command,
                cwd=consumer,
                env=env,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
            )
            selector = selectors.DefaultSelector()
            if process.stdout is None:
                process.kill()
                raise RuntimeAcceptanceError("Codex app-server stdout is unavailable")
            selector.register(process.stdout, selectors.EVENT_READ)
            try:
                # A short bounded startup delay avoids known early-stdio races while preserving
                # a real app-server handshake and exact runtime observation.
                time.sleep(0.4 + attempt * 0.4)
                _write_rpc(
                    process,
                    {
                        "jsonrpc": "2.0",
                        "id": 1,
                        "method": "initialize",
                        "params": {
                            "clientInfo": {
                                "name": "agentic-dev-runtime-acceptance",
                                "version": "1.0.0",
                            },
                            "capabilities": {"experimentalApi": True},
                        },
                    },
                )
                _read_rpc_response(process, selector, 1, timeout_seconds)
                _write_rpc(
                    process,
                    {"jsonrpc": "2.0", "method": "initialized"},
                )
                _write_rpc(
                    process,
                    {
                        "jsonrpc": "2.0",
                        "id": 2,
                        "method": "skills/list",
                        "params": {
                            "cwds": [str(consumer)],
                            "forceReload": True,
                        },
                    },
                )
                response = _read_rpc_response(process, selector, 2, timeout_seconds)
                result = response.get("result")
                if not isinstance(result, dict) or not isinstance(result.get("data"), list):
                    raise RuntimeAcceptanceError(
                        f"Codex skills/list returned invalid result: {response}"
                    )
                entries = [
                    entry for entry in result["data"]
                    if isinstance(entry, dict) and entry.get("cwd") == str(consumer)
                ]
                if len(entries) != 1:
                    raise RuntimeAcceptanceError(
                        f"Codex skills/list did not return exactly one target cwd entry: {entries}"
                    )
                entry = entries[0]
                if entry.get("errors") not in ([], None):
                    raise RuntimeAcceptanceError(
                        f"Codex skills/list reported discovery errors: {entry.get('errors')}"
                    )
                runtime_skills: dict[str, dict[str, Any]] = {}
                for skill in entry.get("skills", []):
                    if not isinstance(skill, dict):
                        continue
                    path = skill.get("path")
                    name = skill.get("name")
                    if not isinstance(path, str) or not isinstance(name, str):
                        continue
                    resolved = str(Path(path).resolve())
                    local_root = (consumer / ".agents/skills").resolve()
                    path_obj = Path(resolved)
                    if local_root in path_obj.parents:
                        runtime_skills[name] = skill

                if set(runtime_skills) != set(expected):
                    raise RuntimeAcceptanceError(
                        "Codex native Skill inventory mismatch: "
                        f"expected={sorted(expected)}, actual={sorted(runtime_skills)}"
                    )
                for name, expected_path in expected.items():
                    skill = runtime_skills[name]
                    if str(Path(skill["path"]).resolve()) != expected_path:
                        raise RuntimeAcceptanceError(
                            f"Codex native Skill path mismatch for {name}: {skill['path']}"
                        )
                    if skill.get("enabled") is not True:
                        raise RuntimeAcceptanceError(
                            f"Codex native Skill is not enabled: {name}"
                        )

                return {
                    "status": "ok",
                    "codex_version": version,
                    "cwd": str(consumer),
                    "skill_count": len(runtime_skills),
                    "skills": [
                        {
                            "name": name,
                            "path": expected[name],
                            "enabled": True,
                        }
                        for name in sorted(runtime_skills)
                    ],
                    "force_reload": True,
                    "local_skill_inventory_only": True,
                }
            except Exception as exc:  # noqa: BLE001 - preserve exact runtime error
                last_error = exc
            finally:
                selector.close()
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=3)
            # retry only once with a fresh app-server process / CODEX_HOME
    raise RuntimeAcceptanceError(f"Codex native discovery failed: {last_error}")


def _require_exact_clean_subject(repo_root: Path, source_sha: str) -> None:
    repo_root = repo_root.resolve()
    actual = _run(["git", "rev-parse", "HEAD"], cwd=repo_root).stdout.strip()
    if actual != source_sha:
        raise RuntimeAcceptanceError(
            f"runtime subject mismatch: requested={source_sha}, actual={actual}"
        )
    status = _run(["git", "status", "--porcelain"], cwd=repo_root).stdout.strip()
    if status:
        raise RuntimeAcceptanceError(
            "runtime acceptance requires a clean exact-subject checkout"
        )


def accept(
    repo_root: Path,
    work_dir: Path,
    source_sha: str,
    codex_bin: str,
    expected_codex_version: str | None,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    _require_exact_clean_subject(repo_root, source_sha)
    fixture = build_and_install_fixture(repo_root, work_dir, source_sha)
    static = verify_installed_fixture(
        fixture["consumer"], expected_skills=fixture["source_skills"]
    )
    with upstream_source_unavailable(repo_root, fixture["consumer"]) as upstream_control:
        codex = codex_native_discovery(
            fixture["consumer"],
            codex_bin,
            expected_version=expected_codex_version,
        )
    return {
        "status": "ok",
        "source_sha": source_sha,
        "runtime_mode": "canonical-skill-copy",
        "skill_set_sha256": fixture["skill_set_sha256"],
        "installed_runtime": static,
        "upstream_negative_control": {
            **upstream_control,
            "native_discovery_status": codex["status"],
        },
        "codex_native_discovery": codex,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    static = sub.add_parser("static")
    static.add_argument("--consumer", required=True)

    native = sub.add_parser("codex-discovery")
    native.add_argument("--consumer", required=True)
    native.add_argument("--codex-bin", default="codex")
    native.add_argument("--expected-codex-version")

    full = sub.add_parser("accept")
    full.add_argument("--repo-root", default=".")
    full.add_argument("--work-dir", required=True)
    full.add_argument("--source-sha", required=True)
    full.add_argument("--codex-bin", default="codex")
    full.add_argument("--expected-codex-version")
    full.add_argument("--report")

    args = parser.parse_args(argv)
    try:
        if args.command == "static":
            payload = verify_installed_fixture(Path(args.consumer))
        elif args.command == "codex-discovery":
            payload = codex_native_discovery(
                Path(args.consumer),
                args.codex_bin,
                expected_version=args.expected_codex_version,
            )
        else:
            payload = accept(
                Path(args.repo_root),
                Path(args.work_dir),
                args.source_sha,
                args.codex_bin,
                args.expected_codex_version,
            )
            if args.report:
                report = Path(args.report)
                report.parent.mkdir(parents=True, exist_ok=True)
                report.write_text(
                    json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
    except (RuntimeAcceptanceError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "fail-closed", "error": str(exc)}, ensure_ascii=False))
        return 2

    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
