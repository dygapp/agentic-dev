#!/usr/bin/env python3
# agentic-dev-distribution: source-only
"""Run Gate E model behavior acceptance in the caller's authenticated Codex Runtime."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
EVALS = REPO_ROOT / "evals"
RESULTS = EVALS / "results"

ACTIVATION_SCENARIOS = (
    "A-CI-01",
    "A-RC-01",
    "A-EU-01",
    "A-CG-01",
    "A-RB-01",
    "A-AR-01",
    "A-MC-01",
    "A-EO-01",
)

BEHAVIOR_SCENARIOS = (
    "B-RB-01",
    "B-AR-01",
    "B-MC-01",
    "B-EO-01",
    "B-GA-01",
    "B-EU-01",
)


class AuthenticatedRuntimeError(RuntimeError):
    pass


def _run(
    command: list[str],
    *,
    cwd: Path = REPO_ROOT,
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
        raise AuthenticatedRuntimeError(
            f"command failed ({completed.returncode}): {' '.join(command)}\n"
            f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
        )
    return completed


def _git_head(repo_root: Path) -> str:
    head = _run(["git", "rev-parse", "HEAD"], cwd=repo_root).stdout.strip()
    if len(head) != 40:
        raise AuthenticatedRuntimeError(f"unexpected Git HEAD: {head!r}")
    return head


def _require_clean_checkout(repo_root: Path) -> None:
    dirty = _run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=repo_root,
    ).stdout.strip()
    if dirty:
        raise AuthenticatedRuntimeError(
            "authenticated model acceptance requires a clean exact-subject checkout"
        )


def infer_auth_method(status_text: str) -> str:
    normalized = status_text.lower()
    if "chatgpt" in normalized:
        return "chatgpt"
    if "access token" in normalized or "access-token" in normalized:
        return "codex-access-token"
    if "api key" in normalized or "api-key" in normalized:
        return "api-key"
    if "workload" in normalized and "identity" in normalized:
        return "workload-identity"
    return "authenticated-other"


def _codex_runtime(codex_bin: str) -> tuple[str, str]:
    version = _run([codex_bin, "--version"]).stdout.strip()
    status = _run([codex_bin, "login", "status"])
    combined = "\n".join(
        part for part in (status.stdout.strip(), status.stderr.strip()) if part
    )
    if not combined:
        raise AuthenticatedRuntimeError(
            "codex login status succeeded but returned no authentication status"
        )
    return version, infer_auth_method(combined)


def _scenario_args(scenarios: tuple[str, ...]) -> list[str]:
    result: list[str] = []
    for scenario in scenarios:
        result.extend(["--scenario", scenario])
    return result


def _run_runtime_mode(
    codex_bin: str,
    mode: str,
    scenarios: tuple[str, ...],
) -> dict[str, int]:
    flag = "--activation" if mode == "activation" else "--behavior"
    runtime = subprocess.run(
        [
            sys.executable,
            str(EVALS / "run_codex_evals.py"),
            flag,
            "--release-runtime",
            *_scenario_args(scenarios),
            "--codex-bin",
            codex_bin,
        ],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if runtime.returncode != 0:
        raise AuthenticatedRuntimeError(
            f"{mode} runtime execution failed ({runtime.returncode}): "
            f"{runtime.stdout}\n{runtime.stderr}"
        )

    grader = subprocess.run(
        [
            sys.executable,
            str(EVALS / "run_codex_grader.py"),
            flag,
            *_scenario_args(scenarios),
            "--codex-bin",
            codex_bin,
        ],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if grader.returncode not in {0, 1}:
        raise AuthenticatedRuntimeError(
            f"{mode} semantic grader infrastructure failed ({grader.returncode}): "
            f"{grader.stdout}\n{grader.stderr}"
        )

    return {
        "runtime_returncode": runtime.returncode,
        "grader_returncode": grader.returncode,
    }


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AuthenticatedRuntimeError(f"cannot load evidence JSON {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise AuthenticatedRuntimeError(f"expected JSON object: {path}")
    return payload


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _collect_mode_evidence(
    mode: str,
    scenarios: tuple[str, ...],
    source_sha: str,
) -> dict[str, Any]:
    root = RESULTS / mode
    summary_path = root / "runtime-acceptance.summary.json"
    summary = _load_json(summary_path)
    if summary.get("status") not in {"PASS", "FAIL"}:
        raise AuthenticatedRuntimeError(
            f"{mode} semantic grading has invalid status: {summary}"
        )
    if summary.get("scenario_count") != len(scenarios):
        raise AuthenticatedRuntimeError(
            f"{mode} scenario count mismatch: {summary.get('scenario_count')} != {len(scenarios)}"
        )

    records: list[dict[str, Any]] = []
    evidence_files: list[dict[str, str]] = []
    for scenario in scenarios:
        run_path = root / f"{scenario}.run.json"
        grade_path = root / f"{scenario}.grade.json"
        jsonl_path = root / f"{scenario}.jsonl"
        stderr_path = root / f"{scenario}.stderr.txt"
        grader_path = root / f"{scenario}.grader.jsonl"
        grader_stderr_path = root / f"{scenario}.grader.stderr.txt"
        for path in (
            run_path,
            grade_path,
            jsonl_path,
            stderr_path,
            grader_path,
            grader_stderr_path,
        ):
            if not path.is_file():
                raise AuthenticatedRuntimeError(
                    f"missing {mode} evidence file for {scenario}: {path}"
                )
            evidence_files.append(
                {
                    "path": path.relative_to(REPO_ROOT).as_posix(),
                    "sha256": _sha256(path),
                }
            )

        run = _load_json(run_path)
        grade = _load_json(grade_path)
        if run.get("source_commit") != source_sha:
            raise AuthenticatedRuntimeError(
                f"{scenario} source SHA mismatch: {run.get('source_commit')} != {source_sha}"
            )
        if run.get("runtime_mode") != "release-installed":
            raise AuthenticatedRuntimeError(
                f"{scenario} was not executed in release-installed runtime"
            )
        if not run.get("release_id"):
            raise AuthenticatedRuntimeError(f"{scenario} has no release_id")
        if run.get("returncode") != 0:
            raise AuthenticatedRuntimeError(
                f"{scenario} runtime returncode is not zero: {run.get('returncode')}"
            )
        grading = run.get("grading")
        verdict = grade.get("verdict")
        if grading not in {"pass", "fail"}:
            raise AuthenticatedRuntimeError(
                f"{scenario} runtime grading state is invalid: {grading}"
            )
        if verdict not in {"PASS", "FAIL"}:
            raise AuthenticatedRuntimeError(
                f"{scenario} semantic grade has invalid verdict: {verdict}"
            )
        expected_grading = "pass" if verdict == "PASS" else "fail"
        if grading != expected_grading:
            raise AuthenticatedRuntimeError(
                f"{scenario} runtime/grader semantic state mismatch: "
                f"{grading} != {expected_grading}"
            )
        records.append(
            {
                "scenario_id": scenario,
                "release_id": run["release_id"],
                "runtime_codex_version": run.get("codex_version"),
                "grader_codex_version": grade.get("grader_codex_version"),
                "verdict": grade["verdict"],
            }
        )

    evidence_files.append(
        {
            "path": summary_path.relative_to(REPO_ROOT).as_posix(),
            "sha256": _sha256(summary_path),
        }
    )
    return {
        "status": summary["status"],
        "summary": summary,
        "scenarios": records,
        "failed_scenarios": [
            item["scenario_id"]
            for item in records
            if item["verdict"] == "FAIL"
        ],
        "evidence_files": sorted(evidence_files, key=lambda item: item["path"]),
    }


def _write_evidence_bundle(
    bundle_path: Path,
    report_path: Path,
    payload: dict[str, Any],
) -> str:
    evidence_paths = {
        item["path"]
        for group_name in ("activation", "behavior")
        for item in payload[group_name]["evidence_files"]
    }
    bundle_path = bundle_path.resolve()
    bundle_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        bundle_path,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as zf:
        report_info = zipfile.ZipInfo(
            "authenticated-model-runtime.json",
            date_time=(1980, 1, 1, 0, 0, 0),
        )
        report_info.compress_type = zipfile.ZIP_DEFLATED
        report_info.external_attr = (0o100644 << 16)
        zf.writestr(report_info, report_path.read_bytes())

        for relative in sorted(evidence_paths):
            source = (REPO_ROOT / relative).resolve()
            if REPO_ROOT not in source.parents:
                raise AuthenticatedRuntimeError(
                    f"evidence path escapes repository root: {relative}"
                )
            if not source.is_file():
                raise AuthenticatedRuntimeError(
                    f"evidence file disappeared before bundling: {relative}"
                )
            info = zipfile.ZipInfo(
                relative,
                date_time=(1980, 1, 1, 0, 0, 0),
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 << 16)
            zf.writestr(info, source.read_bytes())
    return _sha256(bundle_path)


def run_authenticated_acceptance(
    codex_bin: str,
    report_path: Path,
    bundle_path: Path,
) -> dict[str, Any]:
    _require_clean_checkout(REPO_ROOT)
    source_sha = _git_head(REPO_ROOT)
    codex_version, auth_method = _codex_runtime(codex_bin)

    execution = {
        "activation": _run_runtime_mode(
            codex_bin,
            "activation",
            ACTIVATION_SCENARIOS,
        ),
        "behavior": _run_runtime_mode(
            codex_bin,
            "behavior",
            BEHAVIOR_SCENARIOS,
        ),
    }

    activation = _collect_mode_evidence(
        "activation",
        ACTIVATION_SCENARIOS,
        source_sha,
    )
    behavior = _collect_mode_evidence(
        "behavior",
        BEHAVIOR_SCENARIOS,
        source_sha,
    )

    release_ids = {
        item["release_id"]
        for group in (activation, behavior)
        for item in group["scenarios"]
    }
    if len(release_ids) != 1:
        raise AuthenticatedRuntimeError(
            f"model acceptance used multiple Release identities: {sorted(release_ids)}"
        )

    overall_status = (
        "PASS"
        if activation["status"] == "PASS" and behavior["status"] == "PASS"
        else "FAIL"
    )
    payload = {
        "status": overall_status,
        "source_sha": source_sha,
        "release_id": next(iter(release_ids)),
        "codex_version": codex_version,
        "authentication_method": auth_method,
        "authentication_evidence": "codex login status",
        "scenario_count": len(ACTIVATION_SCENARIOS) + len(BEHAVIOR_SCENARIOS),
        "failed_scenarios": (
            activation["failed_scenarios"] + behavior["failed_scenarios"]
        ),
        "execution": execution,
        "activation": activation,
        "behavior": behavior,
    }
    report_path = report_path.resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    bundle_sha256 = _write_evidence_bundle(bundle_path, report_path, payload)
    return {
        **payload,
        "report_path": str(report_path),
        "evidence_bundle": str(bundle_path.resolve()),
        "evidence_bundle_sha256": bundle_sha256,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-bin", default=os.environ.get("CODEX_BIN", "codex"))
    parser.add_argument(
        "--report",
        default=str(RESULTS / "authenticated-model-runtime.json"),
    )
    parser.add_argument(
        "--bundle",
        default=str(RESULTS / "authenticated-model-runtime-evidence.zip"),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        payload = run_authenticated_acceptance(
            args.codex_bin,
            Path(args.report),
            Path(args.bundle),
        )
    except (
        AuthenticatedRuntimeError,
        OSError,
        json.JSONDecodeError,
    ) as exc:
        print(
            json.dumps(
                {"status": "FAIL_CLOSED", "error": str(exc)},
                ensure_ascii=False,
            )
        )
        return 2
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
