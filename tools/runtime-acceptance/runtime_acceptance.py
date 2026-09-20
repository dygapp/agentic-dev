#!/usr/bin/env python3
# agentic-dev-distribution: source-only
"""Build, install, and validate an agentic-dev Release in an isolated Consumer-like runtime."""

from __future__ import annotations

import argparse
import json
import os
import re
import selectors
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from pathlib import Path
from typing import Any

START = "<!-- agentic-dev-release:start -->"
END = "<!-- agentic-dev-release:end -->"
SKILL_FRONTMATTER_END = "\n---\n"
EXPECTED_LOCAL_LOCATORS = (
    ".agents/README.md",
    ".agents/release/skill-index.json",
    ".agents/skills/**",
)
FORBIDDEN_RUNTIME_NAMESPACES = (
    ".agents/methods",
    ".agents/architecture",
    ".agents/rules",
    ".agents/contracts",
    ".agents/tools",
    ".agents/evals",
)
FORBIDDEN_SKILL_SOURCE_PATHS = (
    "docs/methods/",
    "docs/architecture/",
    "docs/rules/",
    "tools/rule-discovery/",
)
INDEX_SKILL_KEYS = {"id", "name", "description", "path"}


class RuntimeAcceptanceError(RuntimeError):
    pass


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


def _safe_extract(archive: Path, destination: Path) -> None:
    destination = destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "r") as zf:
        for info in zf.infolist():
            target = (destination / info.filename).resolve()
            if target != destination and destination not in target.parents:
                raise RuntimeAcceptanceError(
                    f"archive path escapes extraction root: {info.filename}"
                )
        zf.extractall(destination)


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


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeAcceptanceError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeAcceptanceError(f"expected JSON object: {path}")
    return payload


def build_and_install_fixture(
    repo_root: Path,
    work_dir: Path,
    source_sha: str,
    *,
    release_version: str | None = None,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    work_dir = work_dir.resolve()
    if work_dir == repo_root or repo_root in work_dir.parents:
        raise RuntimeAcceptanceError(
            "runtime acceptance work directory must be outside the source repository"
        )

    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True)

    release_version = release_version or f"0.0.0-runtime.{source_sha[:12]}"
    output_dir = work_dir / "release"
    builder = repo_root / "tools/release-build/release_build.py"
    completed = _run(
        [
            sys.executable,
            str(builder),
            "build",
            "--repo-root",
            str(repo_root),
            "--output-dir",
            str(output_dir),
            "--source-sha",
            source_sha,
            "--release-version",
            release_version,
            "--evidence-locator",
            "runtime-acceptance:exact-subject",
        ]
    )
    try:
        build_result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeAcceptanceError(
            f"release builder did not emit JSON: {completed.stdout}"
        ) from exc

    archive = output_dir / build_result["archive"]
    package_root = work_dir / "package"
    _safe_extract(archive, package_root)

    consumer = work_dir / "consumer"
    consumer.mkdir()
    _run(["git", "init", "-q"], cwd=consumer)
    (consumer / "AGENTS.md").write_text(
        "# Consumer Repository Authority\n\n"
        "Product, requirements, system architecture, technology policy and current state "
        "belong to this Consumer repository.\n",
        encoding="utf-8",
    )
    (consumer / "docs").mkdir()
    (consumer / "docs/product.md").write_text(
        "# Consumer Product\n\nThis file is Consumer-owned project knowledge.\n",
        encoding="utf-8",
    )

    installer = package_root / "install.py"
    _run([sys.executable, str(installer), "--target", str(consumer)])

    return {
        "build_result": build_result,
        "archive": archive,
        "package_root": package_root,
        "consumer": consumer,
    }


def verify_installed_fixture(consumer: Path) -> dict[str, Any]:
    consumer = consumer.resolve()
    agents_path = consumer / "AGENTS.md"
    readme_path = consumer / ".agents/README.md"
    manifest_path = consumer / ".agents/release/manifest.json"
    index_path = consumer / ".agents/release/skill-index.json"

    for path in (agents_path, readme_path, manifest_path, index_path):
        if not path.is_file():
            raise RuntimeAcceptanceError(f"installed runtime missing required file: {path}")

    manifest = _load_json(manifest_path)
    index = _load_json(index_path)
    manifest_skills = manifest.get("skills")
    index_skills = index.get("skills")
    if not isinstance(manifest_skills, list) or not isinstance(index_skills, list):
        raise RuntimeAcceptanceError("manifest / skill-index has invalid Skill inventory")
    if index.get("release_id") != manifest.get("release_id"):
        raise RuntimeAcceptanceError("skill-index release_id does not match manifest")
    if index.get("schema_version") != 1:
        raise RuntimeAcceptanceError("unsupported skill-index schema_version")

    manifest_by_name: dict[str, dict[str, Any]] = {}
    for item in manifest_skills:
        if not isinstance(item, dict):
            raise RuntimeAcceptanceError("manifest Skill entry is not an object")
        name = item.get("name")
        if not isinstance(name, str) or not name:
            raise RuntimeAcceptanceError("manifest Skill entry has invalid name")
        if name in manifest_by_name:
            raise RuntimeAcceptanceError(f"duplicate manifest Skill: {name}")
        manifest_by_name[name] = item

    index_by_name: dict[str, dict[str, Any]] = {}
    for item in index_skills:
        if not isinstance(item, dict):
            raise RuntimeAcceptanceError("skill-index entry is not an object")
        if set(item) != INDEX_SKILL_KEYS:
            raise RuntimeAcceptanceError(
                f"skill-index entry must remain locator metadata only: {sorted(item)}"
            )
        name = item.get("name")
        if not isinstance(name, str) or not name:
            raise RuntimeAcceptanceError("skill-index entry has invalid name")
        if name in index_by_name:
            raise RuntimeAcceptanceError(f"duplicate skill-index Skill: {name}")
        index_by_name[name] = item

    if set(manifest_by_name) != set(index_by_name):
        raise RuntimeAcceptanceError(
            "manifest and skill-index Skill inventories are inconsistent"
        )

    installed_paths: list[str] = []
    for name in sorted(manifest_by_name):
        manifest_item = manifest_by_name[name]
        index_item = index_by_name[name]
        for key in ("id", "name", "description", "path"):
            if index_item.get(key) != manifest_item.get(key):
                raise RuntimeAcceptanceError(
                    f"skill-index mismatch for {name}: {key}"
                )

        relative = index_item["path"]
        if not isinstance(relative, str) or not relative.startswith(".agents/skills/"):
            raise RuntimeAcceptanceError(f"invalid local Skill path for {name}: {relative}")
        skill_path = (consumer / relative).resolve()
        if consumer not in skill_path.parents:
            raise RuntimeAcceptanceError(f"Skill path escapes Consumer root: {relative}")
        if not skill_path.is_file():
            raise RuntimeAcceptanceError(f"installed Skill path is missing: {relative}")

        text = skill_path.read_text(encoding="utf-8")
        frontmatter = _frontmatter(text)
        if _scalar(frontmatter, "name") != name:
            raise RuntimeAcceptanceError(f"installed Skill name mismatch: {name}")
        if _scalar(frontmatter, "description") != manifest_item.get("description"):
            raise RuntimeAcceptanceError(f"installed Skill description mismatch: {name}")

        for forbidden in FORBIDDEN_SKILL_SOURCE_PATHS:
            if forbidden in text:
                raise RuntimeAcceptanceError(
                    f"installed Skill {name} depends on provider Source path: {forbidden}"
                )
        installed_paths.append(relative)

    for namespace in FORBIDDEN_RUNTIME_NAMESPACES:
        if (consumer / namespace).exists():
            raise RuntimeAcceptanceError(
                f"forbidden provider-style runtime namespace installed: {namespace}"
            )

    agents = agents_path.read_text(encoding="utf-8")
    if agents.count(START) != 1 or agents.count(END) != 1:
        raise RuntimeAcceptanceError("Consumer AGENTS.md has invalid release locator block")
    for locator in EXPECTED_LOCAL_LOCATORS:
        if locator not in agents:
            raise RuntimeAcceptanceError(
                f"Consumer AGENTS.md missing runtime locator: {locator}"
            )
    for forbidden in FORBIDDEN_SKILL_SOURCE_PATHS:
        if forbidden in agents:
            raise RuntimeAcceptanceError(
                f"Consumer AGENTS.md depends on provider Source path: {forbidden}"
            )

    readme = readme_path.read_text(encoding="utf-8")
    if any(name in readme for name in manifest_by_name):
        raise RuntimeAcceptanceError(
            ".agents/README.md must not become a hand-maintained Skill inventory"
        )
    for forbidden in ("## 流程", "generated-release-reference", "source-id:"):
        if forbidden in readme:
            raise RuntimeAcceptanceError(
                f".agents/README.md contains runtime procedure/reference content: {forbidden}"
            )

    index_text = index_path.read_text(encoding="utf-8")
    for forbidden in ("## 流程", "generated-release-reference", "source-id:"):
        if forbidden in index_text:
            raise RuntimeAcceptanceError(
                f"skill-index violates Progressive Disclosure: {forbidden}"
            )

    compatibility = manifest.get("compatibility")
    if not isinstance(compatibility, dict):
        raise RuntimeAcceptanceError("manifest compatibility declaration is missing")
    chatgpt = compatibility.get("chatgpt_github_connector")
    if not isinstance(chatgpt, dict):
        raise RuntimeAcceptanceError("ChatGPT + GitHub Connector compatibility entry missing")
    if chatgpt.get("index") != ".agents/release/skill-index.json":
        raise RuntimeAcceptanceError("ChatGPT compatibility index locator is inconsistent")

    product = consumer / "docs/product.md"
    if not product.is_file() or "Consumer-owned" not in product.read_text(encoding="utf-8"):
        raise RuntimeAcceptanceError("Consumer-owned docs were not preserved")

    return {
        "status": "ok",
        "release_id": manifest.get("release_id"),
        "source_sha": manifest.get("source_sha"),
        "skill_count": len(manifest_by_name),
        "skills": sorted(manifest_by_name),
        "skill_paths": installed_paths,
        "chatgpt_compatibility_path": [
            "AGENTS.md",
            ".agents/release/skill-index.json",
            ".agents/skills/<name>/SKILL.md",
        ],
        "progressive_disclosure": {
            "bootstrap_contains_skill_bodies": False,
            "index_contains_skill_bodies": False,
            "supporting_content_location": ".agents/skills/<name>/references/**",
        },
        "upstream_runtime_dependency": False,
    }


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
    consumer = consumer.resolve()
    version = _run([codex_bin, "--version"]).stdout.strip()
    if expected_version and expected_version not in version:
        raise RuntimeAcceptanceError(
            f"unexpected Codex version: expected {expected_version!r}, got {version!r}"
        )

    manifest = _load_json(consumer / ".agents/release/manifest.json")
    expected = {
        item["name"]: str((consumer / item["path"]).resolve())
        for item in manifest["skills"]
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
                    "upstream_source_fallback": False,
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


def accept(
    repo_root: Path,
    work_dir: Path,
    source_sha: str,
    codex_bin: str,
    expected_codex_version: str | None,
) -> dict[str, Any]:
    fixture = build_and_install_fixture(repo_root, work_dir, source_sha)
    static = verify_installed_fixture(fixture["consumer"])
    codex = codex_native_discovery(
        fixture["consumer"],
        codex_bin,
        expected_version=expected_codex_version,
    )
    return {
        "status": "ok",
        "source_sha": source_sha,
        "release_build": fixture["build_result"],
        "installed_runtime": static,
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
    except (RuntimeAcceptanceError, OSError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(json.dumps({"status": "fail-closed", "error": str(exc)}, ensure_ascii=False))
        return 2

    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
