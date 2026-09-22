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
AUTHENTICATED_RUNTIME_EVIDENCE_KIND = "authenticated-model-runtime-acceptance"
AUTHENTICATED_RUNTIME_EVIDENCE_SCHEMA_VERSION = 1
RELEASE_COMPLETION_EVIDENCE_KIND = "release-completion-verification"
RELEASE_COMPLETION_EVIDENCE_SCHEMA_VERSION = 1
PROJECT_CAPABILITY_PROFILE_PATH = Path("docs/project/project-capability-profile.md")
RELEASE_COMPLETION_AUTHORITY_FIELD = "release-completion-authority"
RELEASE_COMPLETION_CLAIM_FIELD = "release-completion-claim"
ACCEPTANCE_RANGE_RE = re.compile(
    r"`(?P<prefix>[A-Z][A-Z0-9-]*-)(?P<start>\d+)`～`(?P=prefix)(?P<end>\d+)`"
)
AUTHENTICATED_RUNTIME_ACTIVATION_SCENARIOS = (
    "A-CI-01",
    "A-RC-01",
    "A-EU-01",
    "A-CG-01",
    "A-RB-01",
    "A-AR-01",
    "A-MC-01",
    "A-EO-01",
)
AUTHENTICATED_RUNTIME_BEHAVIOR_SCENARIOS = (
    "B-RB-01",
    "B-AR-01",
    "B-MC-01",
    "B-EO-01",
    "B-GA-01",
    "B-EU-01",
)


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


def _load_json_object(path: Path, label: str) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label}: {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{label} must be a JSON object: {path}")
    return payload


def _authenticated_mode_expected_paths(mode: str, scenarios: tuple[str, ...]) -> set[str]:
    root = f"evals/results/{mode}"
    paths = {f"{root}/runtime-acceptance.summary.json"}
    for scenario in scenarios:
        paths.update(
            {
                f"{root}/{scenario}.run.json",
                f"{root}/{scenario}.grade.json",
                f"{root}/{scenario}.jsonl",
                f"{root}/{scenario}.stderr.txt",
                f"{root}/{scenario}.grader.jsonl",
                f"{root}/{scenario}.grader.stderr.txt",
            }
        )
    return paths


def _validate_authenticated_mode_report(
    mode: str,
    payload: object,
    scenarios: tuple[str, ...],
    release_id: str,
) -> dict[str, str]:
    if not isinstance(payload, dict) or payload.get("status") != "PASS":
        raise ValueError(f"authenticated runtime {mode} evidence is not PASS")
    if payload.get("failed_scenarios") != []:
        raise ValueError(f"authenticated runtime {mode} evidence contains failed scenarios")

    summary = payload.get("summary")
    if not isinstance(summary, dict) or summary.get("status") != "PASS":
        raise ValueError(f"authenticated runtime {mode} summary is not PASS")
    if summary.get("scenario_count") != len(scenarios):
        raise ValueError(f"authenticated runtime {mode} summary has incomplete scenario coverage")

    records = payload.get("scenarios")
    if not isinstance(records, list) or len(records) != len(scenarios):
        raise ValueError(f"authenticated runtime {mode} evidence has incomplete scenario records")
    by_id: dict[str, dict[str, object]] = {}
    for record in records:
        if not isinstance(record, dict):
            raise ValueError(f"authenticated runtime {mode} scenario record is invalid")
        scenario_id = record.get("scenario_id")
        if not isinstance(scenario_id, str) or not scenario_id:
            raise ValueError(f"authenticated runtime {mode} scenario identity is invalid")
        if scenario_id in by_id:
            raise ValueError(f"authenticated runtime {mode} scenario identity is duplicated: {scenario_id}")
        by_id[scenario_id] = record

    if set(by_id) != set(scenarios):
        raise ValueError(f"authenticated runtime {mode} scenario set does not match current acceptance contract")
    for scenario in scenarios:
        record = by_id[scenario]
        if record.get("release_id") != release_id:
            raise ValueError(f"authenticated runtime {mode} scenario release identity mismatch: {scenario}")
        if record.get("verdict") != "PASS":
            raise ValueError(f"authenticated runtime {mode} scenario is not PASS: {scenario}")
        for key in ("runtime_codex_version", "grader_codex_version"):
            value = record.get(key)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(
                    f"authenticated runtime {mode} scenario has no {key}: {scenario}"
                )

    evidence_files = payload.get("evidence_files")
    if not isinstance(evidence_files, list):
        raise ValueError(f"authenticated runtime {mode} evidence file inventory is missing")
    expected_paths = _authenticated_mode_expected_paths(mode, scenarios)
    declared: dict[str, str] = {}
    for item in evidence_files:
        if not isinstance(item, dict):
            raise ValueError(f"authenticated runtime {mode} evidence file record is invalid")
        path = item.get("path")
        digest = item.get("sha256")
        if not isinstance(path, str) or not path or Path(path).is_absolute() or ".." in Path(path).parts:
            raise ValueError(f"authenticated runtime {mode} evidence file path is invalid")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError(f"authenticated runtime {mode} evidence file digest is invalid: {path}")
        if path in declared:
            raise ValueError(f"authenticated runtime {mode} evidence file is duplicated: {path}")
        declared[path] = digest
    if set(declared) != expected_paths:
        raise ValueError(f"authenticated runtime {mode} evidence file inventory is incomplete")
    return declared


def _validate_authenticated_evidence_bundle(
    bundle_path: Path,
    report_path: Path,
    source_sha: str,
    release_id: str,
    evidence_files: dict[str, str],
) -> None:
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
        with zipfile.ZipFile(bundle_path, "r") as zf:
            names = [info.filename for info in zf.infolist()]
            if len(names) != len(set(names)):
                raise ValueError("authenticated runtime evidence bundle contains duplicate entries")
            expected_names = {"authenticated-model-runtime.json", *evidence_files}
            if set(names) != expected_names:
                raise ValueError("authenticated runtime evidence bundle inventory does not match report")
            if zf.read("authenticated-model-runtime.json") != report_path.read_bytes():
                raise ValueError("authenticated runtime evidence bundle report does not match supplied report")
            for path, digest in evidence_files.items():
                if _sha256_bytes(zf.read(path)) != digest:
                    raise ValueError(f"authenticated runtime evidence bundle digest mismatch: {path}")

            for mode, scenarios in (
                ("activation", AUTHENTICATED_RUNTIME_ACTIVATION_SCENARIOS),
                ("behavior", AUTHENTICATED_RUNTIME_BEHAVIOR_SCENARIOS),
            ):
                root = f"evals/results/{mode}"
                mode_report = report.get(mode)
                if not isinstance(mode_report, dict):
                    raise ValueError(f"authenticated runtime bundle {mode} report is invalid")
                records = mode_report.get("scenarios")
                if not isinstance(records, list):
                    raise ValueError(f"authenticated runtime bundle {mode} scenario records are invalid")
                by_id = {
                    record.get("scenario_id"): record
                    for record in records
                    if isinstance(record, dict) and isinstance(record.get("scenario_id"), str)
                }
                summary = json.loads(zf.read(f"{root}/runtime-acceptance.summary.json"))
                if not isinstance(summary, dict) or summary.get("status") != "PASS":
                    raise ValueError(f"authenticated runtime bundle {mode} summary is not PASS")
                if summary.get("scenario_count") != len(scenarios):
                    raise ValueError(f"authenticated runtime bundle {mode} summary is incomplete")
                for scenario in scenarios:
                    record = by_id.get(scenario)
                    if not isinstance(record, dict):
                        raise ValueError(
                            f"authenticated runtime bundle scenario report is missing: {scenario}"
                        )
                    run = json.loads(zf.read(f"{root}/{scenario}.run.json"))
                    grade = json.loads(zf.read(f"{root}/{scenario}.grade.json"))
                    if not isinstance(run, dict) or not isinstance(grade, dict):
                        raise ValueError(f"authenticated runtime bundle scenario evidence is invalid: {scenario}")
                    if run.get("scenario_id") != scenario:
                        raise ValueError(f"authenticated runtime bundle run scenario identity mismatch: {scenario}")
                    if run.get("source_commit") != source_sha:
                        raise ValueError(f"authenticated runtime bundle source SHA mismatch: {scenario}")
                    if run.get("runtime_mode") != "release-installed":
                        raise ValueError(f"authenticated runtime bundle is not release-installed: {scenario}")
                    if run.get("release_id") != release_id:
                        raise ValueError(f"authenticated runtime bundle release identity mismatch: {scenario}")
                    if run.get("returncode") != 0 or run.get("grading") != "pass":
                        raise ValueError(f"authenticated runtime bundle execution is not successful: {scenario}")
                    runtime_version = record.get("runtime_codex_version")
                    grader_version = record.get("grader_codex_version")
                    if run.get("codex_version") != runtime_version:
                        raise ValueError(f"authenticated runtime bundle run runtime identity mismatch: {scenario}")
                    if run.get("grader_codex_version") != grader_version:
                        raise ValueError(f"authenticated runtime bundle run grader identity mismatch: {scenario}")
                    if grade.get("scenario_id") != scenario:
                        raise ValueError(f"authenticated runtime bundle semantic grade scenario identity mismatch: {scenario}")
                    if grade.get("source_commit") != source_sha:
                        raise ValueError(f"authenticated runtime bundle semantic grade source SHA mismatch: {scenario}")
                    if grade.get("runtime_mode") != "release-installed":
                        raise ValueError(f"authenticated runtime bundle semantic grade runtime mode mismatch: {scenario}")
                    if grade.get("release_id") != release_id:
                        raise ValueError(f"authenticated runtime bundle semantic grade release identity mismatch: {scenario}")
                    if grade.get("runtime_codex_version") != runtime_version:
                        raise ValueError(f"authenticated runtime bundle semantic grade runtime identity mismatch: {scenario}")
                    if grade.get("grader_codex_version") != grader_version:
                        raise ValueError(f"authenticated runtime bundle semantic grade grader identity mismatch: {scenario}")
                    if grade.get("verdict") != "PASS":
                        raise ValueError(f"authenticated runtime bundle semantic grade is not PASS: {scenario}")
    except (OSError, zipfile.BadZipFile, KeyError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot validate authenticated runtime evidence bundle: {bundle_path}: {exc}") from exc


def _validate_runtime_evidence(
    source_sha: str,
    runtime_evidence_locator: str | None,
    automated_runtime_evidence: Path | None,
    authenticated_runtime_evidence: Path | None,
    authenticated_runtime_evidence_bundle: Path | None,
) -> dict[str, str] | None:
    supplied = (
        runtime_evidence_locator is not None,
        automated_runtime_evidence is not None,
        authenticated_runtime_evidence is not None,
        authenticated_runtime_evidence_bundle is not None,
    )
    if not any(supplied):
        return None
    if not all(supplied):
        raise ValueError(
            "runtime compatibility verification requires locator, automated runtime evidence, "
            "authenticated runtime evidence, and authenticated runtime evidence bundle together"
        )

    assert runtime_evidence_locator is not None
    assert automated_runtime_evidence is not None
    assert authenticated_runtime_evidence is not None
    assert authenticated_runtime_evidence_bundle is not None
    locator = runtime_evidence_locator.strip()
    if not locator:
        raise ValueError("runtime evidence locator must be non-empty")

    automated_path = automated_runtime_evidence.resolve()
    authenticated_path = authenticated_runtime_evidence.resolve()
    authenticated_bundle_path = authenticated_runtime_evidence_bundle.resolve()
    automated = _load_json_object(automated_path, "automated runtime evidence")
    authenticated = _load_json_object(authenticated_path, "authenticated runtime evidence")

    if automated.get("status") != "ok":
        raise ValueError("automated runtime evidence is not successful")
    if automated.get("source_sha") != source_sha:
        raise ValueError("automated runtime evidence source SHA does not match release source SHA")

    automated_build = automated.get("release_build")
    if not isinstance(automated_build, dict) or automated_build.get("status") != "ok":
        raise ValueError("automated runtime evidence has no successful release build result")
    if automated_build.get("source_sha") != source_sha:
        raise ValueError("automated runtime release build source SHA does not match release source SHA")

    installed_runtime = automated.get("installed_runtime")
    if not isinstance(installed_runtime, dict) or installed_runtime.get("status") != "ok":
        raise ValueError("automated runtime evidence has no successful installed-runtime result")
    if installed_runtime.get("source_sha") != source_sha:
        raise ValueError("installed-runtime evidence source SHA does not match release source SHA")
    if installed_runtime.get("provider_source_paths_present") is not False:
        raise ValueError("installed-runtime evidence does not prove provider Source absence")
    expected_chatgpt_path = [
        "AGENTS.md",
        ".agents/release/skill-index.json",
        ".agents/skills/<name>/SKILL.md",
    ]
    if installed_runtime.get("chatgpt_compatibility_path") != expected_chatgpt_path:
        raise ValueError("automated runtime evidence has invalid ChatGPT compatibility path")

    upstream_control = automated.get("upstream_negative_control")
    if not isinstance(upstream_control, dict) or upstream_control.get("status") != "ok":
        raise ValueError("automated runtime evidence has no successful upstream negative control")
    if upstream_control.get("native_discovery_status") != "ok":
        raise ValueError("automated runtime evidence has no successful native discovery control")

    native_discovery = automated.get("codex_native_discovery")
    if not isinstance(native_discovery, dict) or native_discovery.get("status") != "ok":
        raise ValueError("automated runtime evidence has no successful Codex native discovery")

    if authenticated.get("status") != "PASS":
        raise ValueError("authenticated runtime evidence is not PASS")
    if authenticated.get("evidence_kind") != AUTHENTICATED_RUNTIME_EVIDENCE_KIND:
        raise ValueError("authenticated runtime evidence kind is invalid")
    if authenticated.get("schema_version") != AUTHENTICATED_RUNTIME_EVIDENCE_SCHEMA_VERSION:
        raise ValueError("authenticated runtime evidence schema version is invalid")
    if authenticated.get("source_sha") != source_sha:
        raise ValueError("authenticated runtime evidence source SHA does not match release source SHA")
    release_id = authenticated.get("release_id")
    if not isinstance(release_id, str) or not release_id.endswith(f"+{source_sha[:12]}"):
        raise ValueError("authenticated runtime evidence release identity is invalid")
    codex_version = authenticated.get("codex_version")
    if not isinstance(codex_version, str) or not codex_version.strip():
        raise ValueError("authenticated runtime evidence has no Codex runtime version")
    auth_method = authenticated.get("authentication_method")
    if not isinstance(auth_method, str) or not auth_method.strip():
        raise ValueError("authenticated runtime evidence has no authentication method")
    if authenticated.get("authentication_evidence") != "codex login status":
        raise ValueError("authenticated runtime evidence has no validated authentication status evidence")
    if authenticated.get("failed_scenarios") != []:
        raise ValueError("authenticated runtime evidence contains failed scenarios")
    scenario_count = authenticated.get("scenario_count")
    expected_scenario_count = (
        len(AUTHENTICATED_RUNTIME_ACTIVATION_SCENARIOS)
        + len(AUTHENTICATED_RUNTIME_BEHAVIOR_SCENARIOS)
    )
    if scenario_count != expected_scenario_count:
        raise ValueError("authenticated runtime evidence has incomplete scenario coverage")
    execution = authenticated.get("execution")
    if not isinstance(execution, dict):
        raise ValueError("authenticated runtime evidence has no execution result")
    for mode in ("activation", "behavior"):
        mode_execution = execution.get(mode)
        if not isinstance(mode_execution, dict):
            raise ValueError(f"authenticated runtime {mode} execution result is invalid")
        if mode_execution.get("runtime_returncode") != 0 or mode_execution.get("grader_returncode") != 0:
            raise ValueError(f"authenticated runtime {mode} execution did not complete successfully")

    evidence_files: dict[str, str] = {}
    for mode, scenarios in (
        ("activation", AUTHENTICATED_RUNTIME_ACTIVATION_SCENARIOS),
        ("behavior", AUTHENTICATED_RUNTIME_BEHAVIOR_SCENARIOS),
    ):
        declared = _validate_authenticated_mode_report(
            mode,
            authenticated.get(mode),
            scenarios,
            release_id,
        )
        overlap = set(evidence_files) & set(declared)
        if overlap:
            raise ValueError(f"authenticated runtime evidence file inventory overlaps modes: {sorted(overlap)}")
        evidence_files.update(declared)
    _validate_authenticated_evidence_bundle(
        authenticated_bundle_path,
        authenticated_path,
        source_sha,
        release_id,
        evidence_files,
    )

    return {
        "locator": locator,
        "automated_report_sha256": _sha256_file(automated_path),
        "authenticated_report_sha256": _sha256_file(authenticated_path),
        "authenticated_evidence_bundle_sha256": _sha256_file(authenticated_bundle_path),
    }


def _resolve_repo_file(repo_root: Path, relative: str, label: str) -> Path:
    relative_path = Path(relative)
    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise ValueError(f"{label} must be a repository-relative path")
    resolved = (repo_root / relative_path).resolve()
    if resolved != repo_root and repo_root not in resolved.parents:
        raise ValueError(f"{label} escapes repository root")
    if not resolved.is_file():
        raise ValueError(f"{label} does not exist: {relative}")
    return resolved


def _require_git_tracked_file(repo_root: Path, path: Path, label: str) -> None:
    relative = path.relative_to(repo_root).as_posix()
    result = subprocess.run(
        ["git", "-C", str(repo_root), "ls-files", "--error-unmatch", "--", relative],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"{label} must be tracked by the exact source commit: {relative}")


def _load_release_completion_contract(repo_root: Path) -> dict[str, object]:
    profile_path = _resolve_repo_file(
        repo_root,
        PROJECT_CAPABILITY_PROFILE_PATH.as_posix(),
        "project capability profile",
    )
    _require_git_tracked_file(repo_root, profile_path, "project capability profile")
    profile_text = _read(profile_path)
    frontmatter = _frontmatter(profile_text)
    if frontmatter is None:
        raise ValueError("project capability profile has no front matter")
    authority_relative = _scalar(frontmatter, RELEASE_COMPLETION_AUTHORITY_FIELD)
    claim_id = _scalar(frontmatter, RELEASE_COMPLETION_CLAIM_FIELD)
    if not authority_relative or not claim_id:
        raise ValueError("project capability profile has no release completion contract locator")

    authority_path = _resolve_repo_file(
        repo_root,
        authority_relative,
        "release completion acceptance authority",
    )
    _require_git_tracked_file(
        repo_root,
        authority_path,
        "release completion acceptance authority",
    )
    authority_text = _read(authority_path)
    row_pattern = re.compile(
        rf"^\|\s*`{re.escape(claim_id)}`\s*\|\s*(.*?)\s*\|\s*$",
        re.MULTILINE,
    )
    rows = row_pattern.findall(authority_text)
    if len(rows) != 1:
        raise ValueError(
            f"release completion claim must have exactly one acceptance row in current authority: {claim_id}"
        )
    ranges = list(ACCEPTANCE_RANGE_RE.finditer(rows[0]))
    if len(ranges) != 1:
        raise ValueError(
            f"release completion claim must declare exactly one machine-recoverable acceptance range: {claim_id}"
        )
    match = ranges[0]
    start_text = match.group("start")
    end_text = match.group("end")
    start = int(start_text)
    end = int(end_text)
    if start > end:
        raise ValueError("release completion acceptance range is reversed")
    width = max(len(start_text), len(end_text))
    prefix = match.group("prefix")
    expected_ids = tuple(f"{prefix}{index:0{width}d}" for index in range(start, end + 1))
    if claim_id in expected_ids:
        raise ValueError("release completion claim cannot include itself in its acceptance scope")

    defined_ids = re.findall(r"^\|\s*`([^`]+)`\s*\|", authority_text, re.MULTILINE)
    for acceptance_id in expected_ids:
        if defined_ids.count(acceptance_id) != 1:
            raise ValueError(
                f"release completion acceptance is not uniquely defined by current authority: {acceptance_id}"
            )

    return {
        "claim_id": claim_id,
        "acceptance_ids": expected_ids,
        "authority_path": authority_relative,
        "authority_sha256": _sha256_file(authority_path),
        "profile_sha256": _sha256_file(profile_path),
    }


def _validate_release_completion_evidence(
    repo_root: Path,
    source_sha: str,
    release_id: str,
    verification_evidence_locator: str | None,
    release_completion_evidence: Path | None,
) -> dict[str, object] | None:
    supplied = (
        verification_evidence_locator is not None,
        release_completion_evidence is not None,
    )
    if not any(supplied):
        return None
    if not all(supplied):
        raise ValueError(
            "release completion verification requires locator and machine-readable evidence together"
        )

    assert verification_evidence_locator is not None
    assert release_completion_evidence is not None
    contract = _load_release_completion_contract(repo_root)
    claim_id = str(contract["claim_id"])
    expected_acceptance_ids = tuple(contract["acceptance_ids"])
    locator = verification_evidence_locator.strip()
    if not locator:
        raise ValueError("verification evidence locator must be non-empty")

    evidence_path = release_completion_evidence.resolve()
    evidence = _load_json_object(evidence_path, "release completion evidence")
    if evidence.get("evidence_kind") != RELEASE_COMPLETION_EVIDENCE_KIND:
        raise ValueError("release completion evidence kind is invalid")
    if evidence.get("schema_version") != RELEASE_COMPLETION_EVIDENCE_SCHEMA_VERSION:
        raise ValueError("release completion evidence schema version is invalid")
    if evidence.get("status") != "PASS":
        raise ValueError("release completion evidence is not PASS")
    if evidence.get("source_sha") != source_sha:
        raise ValueError("release completion evidence source SHA does not match release source SHA")
    if evidence.get("release_id") != release_id:
        raise ValueError("release completion evidence release identity does not match release")
    if evidence.get("claim_id") != claim_id:
        raise ValueError("release completion evidence claim identity does not match release claim")
    acceptance_results = evidence.get("acceptance_results")
    if not isinstance(acceptance_results, list) or not acceptance_results:
        raise ValueError("release completion evidence acceptance results are missing")
    acceptance_ids: set[str] = set()
    for record in acceptance_results:
        if not isinstance(record, dict):
            raise ValueError("release completion evidence acceptance result is invalid")
        acceptance_id = record.get("id")
        if not isinstance(acceptance_id, str) or not acceptance_id.strip():
            raise ValueError("release completion evidence acceptance identity is invalid")
        if acceptance_id in acceptance_ids:
            raise ValueError("release completion evidence acceptance identity is duplicated")
        acceptance_ids.add(acceptance_id)
        if acceptance_id not in expected_acceptance_ids:
            raise ValueError(
                f"release completion evidence contains acceptance outside current claim scope: {acceptance_id}"
            )
        if record.get("status") != "PASS":
            raise ValueError(f"release completion evidence acceptance is not PASS: {acceptance_id}")
        evidence_locators = record.get("evidence_locators")
        if (
            not isinstance(evidence_locators, list)
            or not evidence_locators
            or any(not isinstance(item, str) or not item.strip() for item in evidence_locators)
        ):
            raise ValueError(
                f"release completion evidence acceptance has no recoverable evidence locator: {acceptance_id}"
            )

    actual_acceptance_ids = set(acceptance_ids)
    expected_acceptance_set = set(expected_acceptance_ids)
    if actual_acceptance_ids != expected_acceptance_set:
        missing = sorted(expected_acceptance_set - actual_acceptance_ids)
        extra = sorted(actual_acceptance_ids - expected_acceptance_set)
        raise ValueError(
            "release completion evidence acceptance scope does not match current project claim contract; "
            f"missing={missing}, extra={extra}"
        )

    finding_counts = evidence.get("finding_counts")
    if not isinstance(finding_counts, dict):
        raise ValueError("release completion evidence finding counts are missing")
    for key in ("blocking", "medium", "unverified"):
        if finding_counts.get(key) != 0:
            raise ValueError(f"release completion evidence {key} finding count is not zero")

    return {
        "claim_id": claim_id,
        "locator": locator,
        "report_sha256": _sha256_file(evidence_path),
        "acceptance_count": len(expected_acceptance_ids),
        "acceptance_authority": {
            "path": contract["authority_path"],
            "sha256": contract["authority_sha256"],
            "profile_sha256": contract["profile_sha256"],
        },
    }


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
    if not git_dir.exists():
        raise ValueError("release build requires a Git checkout to verify exact source SHA")
    try:
        actual = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("cannot verify exact source SHA from Git HEAD") from exc
    if actual != source_sha:
        raise ValueError(f"source SHA mismatch: expected {source_sha}, actual {actual}")
    try:
        dirty = subprocess.run(
            ["git", "-C", str(repo_root), "status", "--porcelain=v1", "--untracked-files=all"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("cannot verify clean source checkout") from exc
    if dirty:
        raise ValueError("release build requires a clean Git checkout for exact source provenance")


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


def _write_generated_text(path: Path, content: str) -> None:
    if path.exists():
        raise ValueError(f"generated path collision: {path}")
    _write_text(path, content)


def _prepare_generated_reference_root(skill_destination: Path) -> Path:
    reference_root = skill_destination / "references/release-inputs"
    if reference_root.exists():
        raise ValueError(
            f"generated reference namespace collision: {reference_root}"
        )
    reference_root.mkdir(parents=True, exist_ok=False)
    return reference_root


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
    runtime_evidence_locator: str | None = None,
    automated_runtime_evidence: Path | None = None,
    authenticated_runtime_evidence: Path | None = None,
    authenticated_runtime_evidence_bundle: Path | None = None,
    verification_evidence_locator: str | None = None,
    release_completion_evidence: Path | None = None,
) -> dict[str, object]:
    repo_root = repo_root.resolve()
    output_dir = output_dir.resolve()
    _verify_source_sha(repo_root, source_sha)
    if not VERSION_RE.fullmatch(release_version):
        raise ValueError("release version contains unsupported characters")
    if not evidence_locator.strip():
        raise ValueError("build evidence locator must be non-empty")
    release_id = f"agentic-dev@{release_version}+{source_sha[:12]}"
    runtime_evidence = _validate_runtime_evidence(
        source_sha,
        runtime_evidence_locator,
        automated_runtime_evidence,
        authenticated_runtime_evidence,
        authenticated_runtime_evidence_bundle,
    )
    verification_evidence = _validate_release_completion_evidence(
        repo_root,
        source_sha,
        release_id,
        verification_evidence_locator,
        release_completion_evidence,
    )
    if verification_evidence is not None and runtime_evidence is None:
        raise ValueError(
            "release completion verification requires validated Runtime Acceptance evidence"
        )
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

    output_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="agentic-dev-release-") as temp:
        stage = Path(temp)
        shutil.copy2(repo_root / "tools/release-build/install_release.py", stage / "install.py")

        installation_ref_root = stage / "installation/references"
        for identity in sorted(installation_inputs):
            owner = release_inputs[identity]
            _write_generated_text(
                installation_ref_root / _stable_reference_name(identity),
                _generated_reference(owner, source_sha),
            )

        skill_root = stage / "repository/.agents/skills"
        for skill in sorted(skills, key=lambda item: item.name):
            destination = skill_root / skill.name
            _copy_skill_source(skill, destination)
            reference_root = _prepare_generated_reference_root(destination)
            for identity in sorted(skill.release_inputs):
                owner = release_inputs[identity]
                _write_generated_text(
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

        runtime_compatibility_status = (
            "verified" if runtime_evidence else "candidate-unverified-until-runtime-acceptance"
        )
        verified_runtime_locator = runtime_evidence["locator"] if runtime_evidence else None
        verified_completion_locator = verification_evidence["locator"] if verification_evidence else None

        manifest: dict[str, object] = {
            "schema_version": 1,
            "release_id": release_id,
            "release_version": release_version,
            "source_sha": source_sha,
            "distribution_target": "repository-local",
            "verification_evidence_locator": verified_completion_locator,
            "verification_evidence": verification_evidence,
            "build_evidence_locator": evidence_locator,
            "runtime_evidence_locator": verified_runtime_locator,
            "runtime_evidence": runtime_evidence,
            "compatibility": {
                "codex_repository_skills": {
                    "path": ".agents/skills/**",
                    "status": runtime_compatibility_status,
                },
                "chatgpt_github_connector": {
                    "index": ".agents/release/skill-index.json",
                    "status": runtime_compatibility_status,
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
            "verification_evidence_locator": verified_completion_locator,
            "verification_evidence": verification_evidence,
            "build_evidence_locator": evidence_locator,
            "runtime_evidence_locator": verified_runtime_locator,
            "runtime_evidence": runtime_evidence,
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
    build.add_argument("--runtime-evidence-locator")
    build.add_argument("--automated-runtime-evidence")
    build.add_argument("--authenticated-runtime-evidence")
    build.add_argument("--authenticated-runtime-evidence-bundle")
    build.add_argument("--verification-evidence-locator")
    build.add_argument("--release-completion-evidence")

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
                args.runtime_evidence_locator,
                Path(args.automated_runtime_evidence) if args.automated_runtime_evidence else None,
                Path(args.authenticated_runtime_evidence) if args.authenticated_runtime_evidence else None,
                Path(args.authenticated_runtime_evidence_bundle)
                if args.authenticated_runtime_evidence_bundle
                else None,
                args.verification_evidence_locator,
                Path(args.release_completion_evidence) if args.release_completion_evidence else None,
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
