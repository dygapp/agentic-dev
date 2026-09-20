#!/usr/bin/env python3
# agentic-dev-distribution: source-only
"""Deterministic audit for agentic-dev distribution metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

ALLOWED_DISTRIBUTIONS = {
    "source-only",
    "release-input",
    "release-direct",
    "retired",
}
RELEASE_DISTRIBUTIONS = {"release-input", "release-direct"}
ALLOWED_RELEASE_TARGETS = {"software-development", "consumer-installation"}
MARKER_RE = re.compile(r"^#\s*agentic-dev-distribution:\s*(\S+)\s*$", re.MULTILINE)
TARGET_MARKER_RE = re.compile(r"^#\s*agentic-dev-release-target:\s*(\S+)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Asset:
    path: str
    identity: str
    asset_type: str
    distribution: str | None
    release_target: str | None
    source: str


def _frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[4:end]


def _scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        value = value[1:-1]
    return value


def _metadata_scalar(frontmatter: str, key: str) -> str | None:
    lines = frontmatter.splitlines()
    in_metadata = False
    for line in lines:
        if line.strip() == "metadata:" and not line.startswith((" ", "\t")):
            in_metadata = True
            continue
        if in_metadata:
            if line and not line.startswith((" ", "\t")):
                break
            match = re.match(rf"^\s+{re.escape(key)}:\s*(.+?)\s*$", line)
            if match:
                value = match.group(1).strip()
                if (value.startswith('"') and value.endswith('"')) or (
                    value.startswith("'") and value.endswith("'")
                ):
                    value = value[1:-1]
                return value
    return None


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _markdown_assets(repo_root: Path) -> Iterable[Asset]:
    candidates = [repo_root / "AGENTS.md", repo_root / "README.md"]
    candidates.extend(sorted((repo_root / "docs").rglob("*.md")))
    candidates.extend(sorted((repo_root / "evals").glob("*.md")))
    candidates.extend(sorted((repo_root / "evals").glob("*/README.md")))
    candidates.append(repo_root / "skills" / "README.md")

    seen: set[Path] = set()
    for path in candidates:
        if not path.exists() or path in seen:
            continue
        seen.add(path)
        text = _read(path)
        fm = _frontmatter(text)
        if fm is None:
            continue
        identity = _scalar(fm, "id")
        asset_type = _scalar(fm, "type")
        status = _scalar(fm, "status")
        if not identity or not asset_type or not status:
            continue
        yield Asset(
            path=str(path.relative_to(repo_root)),
            identity=identity,
            asset_type=asset_type,
            distribution=_scalar(fm, "distribution"),
            release_target=_scalar(fm, "release-target"),
            source="frontmatter",
        )


def _skill_assets(repo_root: Path) -> Iterable[Asset]:
    skills_root = repo_root / "skills"
    if not skills_root.exists():
        return
    for path in sorted(skills_root.glob("*/SKILL.md")):
        text = _read(path)
        fm = _frontmatter(text)
        if fm is None:
            yield Asset(
                path=str(path.relative_to(repo_root)),
                identity=str(path.parent.name),
                asset_type="skill",
                distribution=None,
                release_target=None,
                source="skill-frontmatter-missing",
            )
            continue
        name = _scalar(fm, "name") or path.parent.name
        identity = _metadata_scalar(fm, "agentic-dev-id") or f"skill:{name}"
        yield Asset(
            path=str(path.relative_to(repo_root)),
            identity=identity,
            asset_type="skill",
            distribution=_metadata_scalar(fm, "agentic-dev-distribution"),
            release_target=_metadata_scalar(fm, "agentic-dev-release-target"),
            source="skill-metadata",
        )


def _executable_assets(repo_root: Path) -> Iterable[Asset]:
    paths: list[Path] = []
    paths.extend(sorted((repo_root / ".github" / "workflows").glob("*.yml")))
    paths.extend(sorted((repo_root / ".github" / "workflows").glob("*.yaml")))
    paths.extend(
        p
        for p in sorted((repo_root / "tools").glob("*/*.py"))
        if "/tests/" not in p.as_posix()
    )
    paths.extend(sorted((repo_root / "evals").glob("run_*.py")))

    for path in paths:
        text = _read(path)
        distribution_match = MARKER_RE.search(text)
        target_match = TARGET_MARKER_RE.search(text)
        yield Asset(
            path=str(path.relative_to(repo_root)),
            identity=f"runtime:{path.relative_to(repo_root).as_posix()}",
            asset_type="runtime",
            distribution=distribution_match.group(1) if distribution_match else None,
            release_target=target_match.group(1) if target_match else None,
            source="comment-marker",
        )


def collect_assets(repo_root: Path) -> list[Asset]:
    assets = [
        *_markdown_assets(repo_root),
        *_skill_assets(repo_root),
        *_executable_assets(repo_root),
    ]
    return sorted(assets, key=lambda asset: asset.path)


def _is_generated_runtime_file(relative: Path) -> bool:
    if "__pycache__" in relative.parts:
        return True
    if relative.suffix in {".pyc", ".pyo"}:
        return True
    if any(part in {".pytest_cache", ".mypy_cache", ".ruff_cache"} for part in relative.parts):
        return True
    if relative.parts[:2] in {("evals", "results"), ("evals", "workspace")}:
        return True
    return False


def _repository_files(repo_root: Path) -> list[str]:
    result: list[str] = []
    for path in sorted(repo_root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(repo_root)
        if ".git" in relative.parts or _is_generated_runtime_file(relative):
            continue
        result.append(relative.as_posix())
    return result


def _inherited_source_class(path: str, assets_by_path: dict[str, Asset]) -> str | None:
    if path in {".gitignore", "LICENSE"}:
        return "repository-support"
    if path.startswith("evals/") and path.endswith(".json"):
        return "eval-corpus"
    if path.startswith("evals/fixtures/"):
        return "eval-fixture"
    if (
        path.startswith("tools/")
        and "/tests/" in path
        and path.endswith(".py")
    ):
        return "tool-test"

    parts = Path(path).parts
    if (
        len(parts) >= 4
        and parts[0] == "skills"
        and parts[2] in {"references", "scripts", "assets"}
    ):
        owner_path = f"skills/{parts[1]}/SKILL.md"
        owner = assets_by_path.get(owner_path)
        if owner is not None:
            return f"skill-resource:{owner.identity}"

    return None


def audit(repo_root: Path) -> dict[str, object]:
    assets = collect_assets(repo_root)
    unclassified = [
        asset.path
        for asset in assets
        if asset.distribution not in ALLOWED_DISTRIBUTIONS
    ]
    orphan_release_input = [
        asset.path
        for asset in assets
        if asset.distribution in RELEASE_DISTRIBUTIONS and not asset.release_target
    ]
    invalid_release_target = [
        asset.path
        for asset in assets
        if (
            asset.distribution in RELEASE_DISTRIBUTIONS
            and asset.release_target not in ALLOWED_RELEASE_TARGETS
        )
        or (
            asset.distribution in {"source-only", "retired"}
            and asset.release_target is not None
        )
    ]

    identities: dict[str, list[str]] = {}
    for asset in assets:
        identities.setdefault(asset.identity, []).append(asset.path)
    duplicate_identities = {
        identity: paths
        for identity, paths in identities.items()
        if len(paths) > 1
    }

    ambiguous_release_owner = sorted(
        {
            path
            for paths in duplicate_identities.values()
            for path in paths
        }
    )

    scoped_paths = {asset.path for asset in assets}
    assets_by_path = {asset.path: asset for asset in assets}
    inherited_files: dict[str, str] = {}
    unexpected_unowned: list[str] = []
    repository_files = _repository_files(repo_root)
    for path in repository_files:
        if path in scoped_paths:
            continue
        inherited_class = _inherited_source_class(path, assets_by_path)
        if inherited_class is None:
            unexpected_unowned.append(path)
        else:
            inherited_files[path] = inherited_class

    counts: dict[str, int] = {key: 0 for key in sorted(ALLOWED_DISTRIBUTIONS)}
    counts["unclassified"] = 0
    for asset in assets:
        if asset.distribution in ALLOWED_DISTRIBUTIONS:
            counts[asset.distribution] += 1
        else:
            counts["unclassified"] += 1

    result: dict[str, object] = {
        "status": (
            "ok"
            if not unclassified
            and not orphan_release_input
            and not invalid_release_target
            and not ambiguous_release_owner
            and not unexpected_unowned
            else "fail-closed"
        ),
        "repository_file_count": len(repository_files),
        "scoped_asset_count": len(assets),
        "inherited_file_count": len(inherited_files),
        "counts": counts,
        "unclassified": unclassified,
        "orphan_release_input": orphan_release_input,
        "invalid_release_target": invalid_release_target,
        "ambiguous_release_owner": ambiguous_release_owner,
        "unexpected_unowned": unexpected_unowned,
        "inherited_files": inherited_files,
        "duplicate_identities": duplicate_identities,
        "assets": [asdict(asset) for asset in assets],
    }
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit agentic-dev distribution metadata and ownership."
    )
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print only status/counts/failure lists instead of the full inventory.",
    )
    args = parser.parse_args(argv)

    result = audit(Path(args.repo_root).resolve())
    if args.summary:
        result = {
            key: result[key]
            for key in (
                "status",
                "repository_file_count",
                "scoped_asset_count",
                "inherited_file_count",
                "counts",
                "unclassified",
                "orphan_release_input",
                "invalid_release_target",
                "ambiguous_release_owner",
                "unexpected_unowned",
            )
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "ok" else 2


if __name__ == "__main__":
    sys.exit(main())
