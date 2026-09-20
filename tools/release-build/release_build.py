#!/usr/bin/env python3
# agentic-dev-distribution: source-only
"""Deterministic release builder and verifier for agentic-dev Skill releases."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
VERSION_RE = re.compile(r"^[0-9A-Za-z][0-9A-Za-z._-]{0,127}$")
FRONTMATTER_END = "\n---\n"
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


@dataclass(frozen=True)
class MarkdownOwner:
    path: Path
    identity: str
    distribution: str
    release_target: str | None


@dataclass(frozen=True)
class SkillSource:
    path: Path
    name: str
    identity: str
    description: str
    distribution: str
    release_target: str
    release_inputs: tuple[str, ...]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find(FRONTMATTER_END, 4)
    if end < 0:
        return None
    return text[4:end]


def _body(text: str) -> str:
    fm = _frontmatter(text)
    if fm is None:
        return text
    end = text.find(FRONTMATTER_END, 4)
    return text[end + len(FRONTMATTER_END):]


def _scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        value = value[1:-1]
    return value


def _metadata_scalar(frontmatter: str, key: str) -> str | None:
    in_metadata = False
    for line in frontmatter.splitlines():
        if line.strip() == "metadata:" and not line.startswith((" ", "\t")):
            in_metadata = True
            continue
        if in_metadata and line and not line.startswith((" ", "\t")):
            break
        if in_metadata:
            match = re.match(rf"^\s+{re.escape(key)}:\s*(.+?)\s*$", line)
            if match:
                value = match.group(1).strip()
                if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
                    value = value[1:-1]
                return value
    return None


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _stable_reference_name(identity: str) -> str:
    value = re.sub(r"[^0-9A-Za-z._-]+", "--", identity).strip("-")
    if not value:
        raise ValueError(f"cannot derive stable reference name for {identity!r}")
    return value + ".md"


def _collect_markdown_owners(repo_root: Path) -> dict[str, MarkdownOwner]:
    owners: dict[str, MarkdownOwner] = {}
    for path in sorted((repo_root / "docs").rglob("*.md")):
        text = _read(path)
        fm = _frontmatter(text)
        if fm is None:
            continue
        identity = _scalar(fm, "id")
        distribution = _scalar(fm, "distribution")
        status = _scalar(fm, "status")
        if not identity or not distribution or status != "active":
            continue
        if identity in owners:
            raise ValueError(f"duplicate source identity: {identity}")
        owners[identity] = MarkdownOwner(
            path=path,
            identity=identity,
            distribution=distribution,
            release_target=_scalar(fm, "release-target"),
        )
    return owners


def _collect_skills(repo_root: Path) -> list[SkillSource]:
    result: list[SkillSource] = []
    for path in sorted((repo_root / "skills").glob("*/SKILL.md")):
        text = _read(path)
        fm = _frontmatter(text)
        if fm is None:
            raise ValueError(f"missing Skill front matter: {path}")
        name = _scalar(fm, "name")
        description = _scalar(fm, "description")
        identity = _metadata_scalar(fm, "agentic-dev-id")
        distribution = _metadata_scalar(fm, "agentic-dev-distribution")
        target = _metadata_scalar(fm, "agentic-dev-release-target")
        release_inputs_text = _metadata_scalar(fm, "agentic-dev-release-inputs") or ""
        if not all((name, description, identity, distribution, target)):
            raise ValueError(f"incomplete release Skill metadata: {path}")
        inputs = tuple(
            item.strip()
            for item in release_inputs_text.split(";")
            if item.strip()
        )
        result.append(
            SkillSource(
                path=path,
                name=name,
                identity=identity,
                description=description,
                distribution=distribution,
                release_target=target,
                release_inputs=inputs,
            )
        )
    return result


def _verify_source_sha(repo_root: Path, source_sha: str) -> None:
    if not SHA_RE.fullmatch(source_sha):
        raise ValueError("source SHA must be an exact lowercase 40-character commit id")
    git_dir = repo_root / ".git"
    if git_dir.exists():
        actual = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        if actual != source_sha:
            raise ValueError(f"source SHA mismatch: expected {source_sha}, actual {actual}")


def _run_distribution_audit(repo_root: Path) -> None:
    command = [
        sys.executable,
        str(repo_root / "tools" / "distribution-audit" / "distribution_audit.py"),
        "--repo-root",
        str(repo_root),
        "--summary",
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise ValueError(
            "distribution audit failed before release build:\n"
            + result.stdout
            + result.stderr
        )


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def _generated_reference(owner: MarkdownOwner, source_sha: str) -> str:
    source = _read(owner.path)
    body = _body(source).lstrip()
    return (
        "<!-- generated-release-reference\n"
        f"source-id: {owner.identity}\n"
        f"source-sha: {source_sha}\n"
        "do-not-edit: regenerate from canonical source\n"
        "-->\n\n"
        + body
    )


def _copy_skill_source(source: SkillSource, destination: Path) -> None:
    source_dir = source.path.parent
    shutil.copytree(
        source_dir,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
    )


def _build_skill_index(release_id: str, skills: list[SkillSource]) -> dict[str, object]:
    return {
        "schema_version": 1,
        "release_id": release_id,
        "skills": [
            {
                "id": skill.identity,
                "name": skill.name,
                "description": skill.description,
                "path": f".agents/skills/{skill.name}/SKILL.md",
            }
            for skill in sorted(skills, key=lambda item: item.name)
        ],
    }


def _agents_readme(release_id: str, source_sha: str) -> str:
    return f"""# Agent 开发能力

本目录由版本化 `agentic-dev` Release **{release_id}** 安装。

- Consumer 的根 `AGENTS.md`、产品 / 需求 / 系统架构 / 技术 / 项目文档继续由当前 Repository 自己拥有；
- 发布 Skill 位于 `.agents/skills/**`；
- 机器生成的 Skill locator 位于 `.agents/release/skill-index.json`；
- installed release provenance 位于 `.agents/release/manifest.json`；
- 普通运行不得在线读取 `agentic-dev` Source Repository 补流程或规则。

本文件只解释安装边界，不复制 Skill Procedure、项目 Roadmap、Current Gate 或手工维护的 Skill inventory。

Source commit: `{source_sha}`
"""


def _json_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _collect_integrity_files(stage: Path) -> list[dict[str, str]]:
    excluded = {
        "manifest.json",
        "repository/.agents/release/manifest.json",
    }
    result: list[dict[str, str]] = []
    for path in sorted(p for p in stage.rglob("*") if p.is_file()):
        relative = path.relative_to(stage).as_posix()
        if relative in excluded:
            continue
        result.append({"path": relative, "sha256": _sha256_file(path)})
    return result


def _write_deterministic_zip(stage: Path, archive: Path) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        archive,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as zf:
        for path in sorted(p for p in stage.rglob("*") if p.is_file()):
            relative = path.relative_to(stage).as_posix()
            info = zipfile.ZipInfo(relative, date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = 0o755 if relative == "install.py" else 0o644
            info.external_attr = (0o100000 | mode) << 16
            zf.writestr(info, path.read_bytes())


def _verify_stage(stage: Path, manifest: dict[str, object]) -> None:
    expected = {
        entry["path"]: entry["sha256"]
        for entry in manifest["integrity"]["files"]  # type: ignore[index]
    }
    actual_files = {
        path.relative_to(stage).as_posix()
        for path in stage.rglob("*")
        if path.is_file()
    }
    ignored = {"manifest.json", "repository/.agents/release/manifest.json"}
    if actual_files != set(expected) | ignored:
        missing = sorted((set(expected) | ignored) - actual_files)
        extra = sorted(actual_files - (set(expected) | ignored))
        raise ValueError(f"artifact file-set mismatch; missing={missing}, extra={extra}")
    for relative, digest in expected.items():
        actual = _sha256_file(stage / relative)
        if actual != digest:
            raise ValueError(f"checksum mismatch for {relative}: {actual} != {digest}")
    root_manifest = _json_bytes(manifest)
    if (stage / "manifest.json").read_bytes() != root_manifest:
        raise ValueError("root manifest does not match canonical manifest bytes")
    if (stage / "repository/.agents/release/manifest.json").read_bytes() != root_manifest:
        raise ValueError("installed manifest copy does not match canonical manifest bytes")


def build_release(
    repo_root: Path,
    output_dir: Path,
    source_sha: str,
    release_version: str,
    evidence_locator: str,
) -> dict[str, object]:
    repo_root = repo_root.resolve()
    output_dir = output_dir.resolve()
    _verify_source_sha(repo_root, source_sha)
    if not VERSION_RE.fullmatch(release_version):
        raise ValueError("release version contains unsupported characters")
    if not evidence_locator.strip():
        raise ValueError("verification evidence locator must be non-empty")
    _run_distribution_audit(repo_root)

    owners = _collect_markdown_owners(repo_root)
    release_inputs = {
        identity: owner
        for identity, owner in owners.items()
        if owner.distribution == "release-input"
    }
    skills = [
        skill
        for skill in _collect_skills(repo_root)
        if skill.distribution == "release-direct"
        and skill.release_target == "software-development"
    ]
    if not skills:
        raise ValueError("no release-direct software-development Skills found")

    software_inputs = {
        identity
        for identity, owner in release_inputs.items()
        if owner.release_target == "software-development"
    }
    installation_inputs = {
        identity
        for identity, owner in release_inputs.items()
        if owner.release_target == "consumer-installation"
    }

    consumed: set[str] = set()
    for skill in skills:
        if not skill.release_inputs:
            raise ValueError(f"release Skill declares no release inputs: {skill.name}")
        for identity in skill.release_inputs:
            owner = release_inputs.get(identity)
            if owner is None:
                raise ValueError(
                    f"Skill {skill.name} references unknown/non-release-input source id: {identity}"
                )
            if owner.release_target != "software-development":
                raise ValueError(
                    f"Skill {skill.name} references non-software release input: {identity}"
                )
            consumed.add(identity)

    uncovered = sorted(software_inputs - consumed)
    if uncovered:
        raise ValueError(f"unconsumed software-development release inputs: {uncovered}")

    release_id = f"agentic-dev@{release_version}+{source_sha[:12]}"
    output_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="agentic-dev-release-") as temp:
        stage = Path(temp)
        shutil.copy2(repo_root / "tools/release-build/install_release.py", stage / "install.py")

        installation_ref_root = stage / "installation/references"
        for identity in sorted(installation_inputs):
            owner = release_inputs[identity]
            _write_text(
                installation_ref_root / _stable_reference_name(identity),
                _generated_reference(owner, source_sha),
            )

        skill_root = stage / "repository/.agents/skills"
        for skill in sorted(skills, key=lambda item: item.name):
            destination = skill_root / skill.name
            _copy_skill_source(skill, destination)
            reference_root = destination / "references/release-inputs"
            for identity in sorted(skill.release_inputs):
                owner = release_inputs[identity]
                _write_text(
                    reference_root / _stable_reference_name(identity),
                    _generated_reference(owner, source_sha),
                )

        _write_text(
            stage / "repository/.agents/README.md",
            _agents_readme(release_id, source_sha),
        )
        skill_index = _build_skill_index(release_id, skills)
        _write_text(
            stage / "repository/.agents/release/skill-index.json",
            _json_bytes(skill_index).decode("utf-8"),
        )

        manifest: dict[str, object] = {
            "schema_version": 1,
            "release_id": release_id,
            "release_version": release_version,
            "source_sha": source_sha,
            "distribution_target": "repository-local",
            "verification_evidence_locator": evidence_locator,
            "compatibility": {
                "codex_repository_skills": {
                    "path": ".agents/skills/**",
                    "status": "candidate-unverified-until-gate-e",
                },
                "chatgpt_github_connector": {
                    "index": ".agents/release/skill-index.json",
                    "status": "candidate-unverified-until-gate-e",
                },
                "installer_python": ">=3.11",
            },
            "skills": [
                {
                    "id": skill.identity,
                    "name": skill.name,
                    "description": skill.description,
                    "path": f".agents/skills/{skill.name}/SKILL.md",
                    "release_inputs": list(skill.release_inputs),
                }
                for skill in sorted(skills, key=lambda item: item.name)
            ],
            "installation_inputs": sorted(installation_inputs),
            "platform_adapters": [],
            "integrity": {
                "algorithm": "sha256",
                "scope": "all artifact files except the two identical manifest copies",
                "files": [],
            },
        }
        manifest["integrity"]["files"] = _collect_integrity_files(stage)  # type: ignore[index]
        manifest_bytes = _json_bytes(manifest)
        (stage / "repository/.agents/release").mkdir(parents=True, exist_ok=True)
        (stage / "manifest.json").write_bytes(manifest_bytes)
        (stage / "repository/.agents/release/manifest.json").write_bytes(manifest_bytes)

        _verify_stage(stage, manifest)

        archive = output_dir / f"agentic-dev-{release_version}.zip"
        _write_deterministic_zip(stage, archive)
        result = {
            "status": "ok",
            "release_id": release_id,
            "source_sha": source_sha,
            "archive": archive.name,
            "archive_sha256": _sha256_file(archive),
            "manifest_sha256": _sha256_bytes(manifest_bytes),
            "skill_count": len(skills),
            "software_release_input_count": len(software_inputs),
            "installation_input_count": len(installation_inputs),
            "verification_evidence_locator": evidence_locator,
        }
        _write_text(
            output_dir / f"agentic-dev-{release_version}.build.json",
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )
        return result


def verify_archive(archive: Path) -> dict[str, object]:
    archive = archive.resolve()
    with tempfile.TemporaryDirectory(prefix="agentic-dev-release-verify-") as temp:
        stage = Path(temp)
        with zipfile.ZipFile(archive, "r") as zf:
            for info in zf.infolist():
                target = (stage / info.filename).resolve()
                if stage.resolve() not in target.parents and target != stage.resolve():
                    raise ValueError(f"archive path escapes extraction root: {info.filename}")
            zf.extractall(stage)
        manifest = json.loads((stage / "manifest.json").read_text(encoding="utf-8"))
        _verify_stage(stage, manifest)
        return {
            "status": "ok",
            "release_id": manifest["release_id"],
            "source_sha": manifest["source_sha"],
            "archive_sha256": _sha256_file(archive),
            "skill_count": len(manifest["skills"]),
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build")
    build.add_argument("--repo-root", default=".")
    build.add_argument("--output-dir", required=True)
    build.add_argument("--source-sha", required=True)
    build.add_argument("--release-version", required=True)
    build.add_argument(
        "--evidence-locator",
        default="github-actions:Release Build",
    )

    verify = sub.add_parser("verify")
    verify.add_argument("--archive", required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            payload = build_release(
                Path(args.repo_root),
                Path(args.output_dir),
                args.source_sha.lower(),
                args.release_version,
                args.evidence_locator,
            )
        else:
            payload = verify_archive(Path(args.archive))
    except (ValueError, OSError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(json.dumps({"status": "fail-closed", "error": str(exc)}, ensure_ascii=False))
        return 2

    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
