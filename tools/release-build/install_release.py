#!/usr/bin/env python3
# agentic-dev-distribution: release-direct
# agentic-dev-release-target: consumer-installation
"""Install an extracted agentic-dev Release into a Consumer repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

START = "<!-- agentic-dev-release:start -->"
END = "<!-- agentic-dev-release:end -->"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_manifest(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _integrity_map(manifest: dict[str, object]) -> dict[str, str]:
    return {
        item["path"]: item["sha256"]
        for item in manifest["integrity"]["files"]  # type: ignore[index]
    }


def _verify_package(package_root: Path, manifest: dict[str, object]) -> None:
    expected = _integrity_map(manifest)
    for relative, digest in expected.items():
        path = package_root / relative
        if not path.is_file():
            raise ValueError(f"release package missing {relative}")
        if _sha256(path) != digest:
            raise ValueError(f"release package checksum mismatch: {relative}")


def _target_relative(package_relative: str) -> Path | None:
    prefix = "repository/"
    if not package_relative.startswith(prefix):
        return None
    return Path(package_relative[len(prefix):])


def _release_owned_target_integrity(
    manifest: dict[str, object],
) -> dict[str, str]:
    result: dict[str, str] = {}
    for package_relative, digest in _integrity_map(manifest).items():
        relative = _target_relative(package_relative)
        if relative is None:
            continue
        relative_text = relative.as_posix()
        if (
            relative_text == ".agents/README.md"
            or relative_text == ".agents/release/skill-index.json"
            or relative_text.startswith(".agents/skills/")
        ):
            result[relative_text] = digest
    return result


def _verify_existing_release_owned_state(
    target: Path,
    old_manifest: dict[str, object],
) -> None:
    expected = _release_owned_target_integrity(old_manifest)
    for relative_text, digest in expected.items():
        relative = Path(relative_text)
        current = target / relative
        if not current.is_file():
            raise ValueError(f"installed release-owned file is missing: {relative}")
        if _sha256(current) != digest:
            raise ValueError(f"installed release-owned file was locally modified: {relative}")

    for skill in _skill_names(old_manifest):
        prefix = f".agents/skills/{skill}/"
        expected_files = {
            relative for relative in expected if relative.startswith(prefix)
        }
        skill_root = target / ".agents/skills" / skill
        actual_files = {
            path.relative_to(target).as_posix()
            for path in skill_root.rglob("*")
            if path.is_file()
        } if skill_root.is_dir() else set()
        if actual_files != expected_files:
            raise ValueError(
                f"installed release-owned Skill file set was locally modified: {skill}"
            )


def _skill_names(manifest: dict[str, object]) -> set[str]:
    return {item["name"] for item in manifest["skills"]}  # type: ignore[index]


def _bootstrap_block(manifest: dict[str, object]) -> str:
    release_id = manifest["release_id"]
    return f"""{START}
## Agent 开发能力

本仓库已安装 `{release_id}`。

- Consumer Repository Authority 始终优先；
- 人类说明：`.agents/README.md`；
- Skill locator：`.agents/release/skill-index.json`；
- Skill 根：`.agents/skills/**`；
- 普通运行不得在线访问 `agentic-dev` Source Repository 补流程或规则。
{END}"""


def _update_agents(existing: str, block: str) -> str:
    starts = existing.count(START)
    ends = existing.count(END)
    if starts != ends or starts > 1:
        raise ValueError("AGENTS.md contains an invalid agentic-dev release marker block")
    if starts == 1:
        begin = existing.index(START)
        finish = existing.index(END, begin) + len(END)
        return existing[:begin] + block + existing[finish:]
    stripped = existing.rstrip()
    if not stripped:
        return block + "\n"
    return stripped + "\n\n" + block + "\n"


def _check_first_install_conflicts(target: Path, manifest: dict[str, object]) -> None:
    for skill in _skill_names(manifest):
        if (target / ".agents/skills" / skill).exists():
            raise ValueError(f"existing local Skill conflicts with release Skill: {skill}")
    for relative in (
        Path(".agents/README.md"),
        Path(".agents/release/skill-index.json"),
        Path(".agents/release/manifest.json"),
    ):
        if (target / relative).exists():
            raise ValueError(f"existing local asset conflicts with release-owned path: {relative}")


def _preflight_release_payload(
    payload: Path,
    manifest: dict[str, object],
) -> None:
    for skill in _skill_names(manifest):
        source = payload / "skills" / skill
        if not source.is_dir():
            raise ValueError(f"release payload missing Skill directory: {skill}")
    for relative in (
        Path("README.md"),
        Path("release/skill-index.json"),
    ):
        if not (payload / relative).is_file():
            raise ValueError(f"release payload missing required asset: {relative}")


def _check_upgrade_conflicts(
    target: Path,
    old_manifest: dict[str, object],
    manifest: dict[str, object],
) -> None:
    old_skills = _skill_names(old_manifest)
    for skill in sorted(_skill_names(manifest) - old_skills):
        if (target / ".agents/skills" / skill).exists():
            raise ValueError(
                f"existing local Skill conflicts with newly introduced release Skill: {skill}"
            )


def install(package_root: Path, target: Path, dry_run: bool = False) -> dict[str, object]:
    package_root = package_root.resolve()
    target = target.resolve()
    manifest = _load_manifest(package_root / "manifest.json")
    _verify_package(package_root, manifest)

    payload = package_root / "repository/.agents"
    if not payload.is_dir():
        raise ValueError("release package has no repository/.agents payload")
    _preflight_release_payload(payload, manifest)

    old_manifest_path = target / ".agents/release/manifest.json"
    old_manifest = _load_manifest(old_manifest_path) if old_manifest_path.is_file() else None

    if old_manifest is None:
        _check_first_install_conflicts(target, manifest)
    else:
        _verify_existing_release_owned_state(target, old_manifest)
        _check_upgrade_conflicts(target, old_manifest, manifest)

    agents_path = target / "AGENTS.md"
    existing_agents = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""
    new_agents = _update_agents(existing_agents, _bootstrap_block(manifest))

    actions = {
        "release_id": manifest["release_id"],
        "target": str(target),
        "replace_release_skills": sorted(_skill_names(old_manifest)) if old_manifest else [],
        "install_release_skills": sorted(_skill_names(manifest)),
        "update_agents_marker": True,
    }
    if dry_run:
        return {"status": "ok", "dry_run": True, **actions}

    target.mkdir(parents=True, exist_ok=True)
    agents_path.write_text(new_agents, encoding="utf-8", newline="\n")

    skills_root = target / ".agents/skills"
    skills_root.mkdir(parents=True, exist_ok=True)
    if old_manifest:
        for skill in sorted(_skill_names(old_manifest)):
            old_dir = skills_root / skill
            if old_dir.exists():
                shutil.rmtree(old_dir)

    for skill in sorted(_skill_names(manifest)):
        source = payload / "skills" / skill
        destination = skills_root / skill
        if destination.exists():
            raise ValueError(f"unowned local Skill conflicts during install: {skill}")
        shutil.copytree(source, destination)

    release_root = target / ".agents/release"
    release_root.mkdir(parents=True, exist_ok=True)
    shutil.copy2(payload / "README.md", target / ".agents/README.md")
    shutil.copy2(payload / "release/skill-index.json", release_root / "skill-index.json")
    shutil.copy2(package_root / "manifest.json", release_root / "manifest.json")

    return {"status": "ok", "dry_run": False, **actions}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        payload = install(Path(__file__).resolve().parent, Path(args.target), args.dry_run)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "fail-closed", "error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
