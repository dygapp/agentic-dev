#!/usr/bin/env python3
"""Deterministic GitHub Actions failure-closure transport for B-GA-01."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


INITIAL_RUN_ID = 4242
INITIAL_JOB_ID = 9001
INITIAL_HEAD_SHA = "abc123"
REPAIRED_RUN_ID = 4243
REPAIRED_JOB_ID = 9002
REPAIRED_HEAD_SHA = "def456"
STATE_PATH = Path(".actions-fixture-state.json")
CONFIG_PATH = Path("ci-config.txt")


def emit(payload: dict) -> int:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


def fail(message: str) -> None:
    raise SystemExit(message)


def load_state() -> dict:
    if not STATE_PATH.is_file():
        return {"fix_registered": False, "rerun_dispatched": False}
    payload = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        fail("invalid fixture state")
    return payload


def write_state(payload: dict) -> None:
    STATE_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def require_run(run_id: int) -> None:
    if run_id not in {INITIAL_RUN_ID, REPAIRED_RUN_ID}:
        fail(f"unknown run id: {run_id}")


def require_repaired_run_ready() -> dict:
    state = load_state()
    if not state.get("rerun_dispatched"):
        fail("repaired run has not been dispatched")
    return state


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Deterministic Actions fixture. Observe Run 4242 to failure, recover "
            "diagnostics, apply the authorized minimal ci-config.txt fix, register "
            "the new Head, dispatch Run 4243, then re-verify."
        )
    )
    sub = parser.add_subparsers(dest="command", required=True)

    read_run = sub.add_parser("read-run")
    read_run.add_argument("--run-id", type=int, required=True)
    read_run.add_argument("--poll", type=int, choices=(1, 2), required=True)

    read_jobs = sub.add_parser("read-jobs")
    read_jobs.add_argument("--run-id", type=int, required=True)

    read_log = sub.add_parser("read-log")
    read_log.add_argument("--job-id", type=int, required=True)

    read_artifacts = sub.add_parser("read-artifacts")
    read_artifacts.add_argument("--run-id", type=int, required=True)

    register_fix = sub.add_parser("register-fix")
    register_fix.add_argument("--base-head", required=True)

    dispatch_rerun = sub.add_parser("dispatch-rerun")
    dispatch_rerun.add_argument("--head", required=True)

    args = parser.parse_args()

    if args.command == "read-run":
        require_run(args.run_id)
        if args.run_id == INITIAL_RUN_ID:
            if args.poll == 1:
                return emit(
                    {
                        "id": INITIAL_RUN_ID,
                        "run_attempt": 1,
                        "event": "pull_request",
                        "head_sha": INITIAL_HEAD_SHA,
                        "status": "in_progress",
                        "conclusion": None,
                    }
                )
            return emit(
                {
                    "id": INITIAL_RUN_ID,
                    "run_attempt": 1,
                    "event": "pull_request",
                    "head_sha": INITIAL_HEAD_SHA,
                    "status": "completed",
                    "conclusion": "failure",
                }
            )

        require_repaired_run_ready()
        if args.poll == 1:
            return emit(
                {
                    "id": REPAIRED_RUN_ID,
                    "run_attempt": 1,
                    "event": "pull_request",
                    "head_sha": REPAIRED_HEAD_SHA,
                    "status": "in_progress",
                    "conclusion": None,
                }
            )
        return emit(
            {
                "id": REPAIRED_RUN_ID,
                "run_attempt": 1,
                "event": "pull_request",
                "head_sha": REPAIRED_HEAD_SHA,
                "status": "completed",
                "conclusion": "success",
            }
        )

    if args.command == "read-jobs":
        require_run(args.run_id)
        if args.run_id == INITIAL_RUN_ID:
            return emit(
                {
                    "run_id": INITIAL_RUN_ID,
                    "jobs": [
                        {
                            "id": INITIAL_JOB_ID,
                            "name": "completion-verification",
                            "status": "completed",
                            "conclusion": "failure",
                            "steps": [
                                {
                                    "name": "verify-ci-config",
                                    "status": "completed",
                                    "conclusion": "failure",
                                }
                            ],
                        }
                    ],
                }
            )

        require_repaired_run_ready()
        return emit(
            {
                "run_id": REPAIRED_RUN_ID,
                "jobs": [
                    {
                        "id": REPAIRED_JOB_ID,
                        "name": "completion-verification",
                        "status": "completed",
                        "conclusion": "success",
                        "steps": [
                            {
                                "name": "verify-ci-config",
                                "status": "completed",
                                "conclusion": "success",
                            }
                        ],
                    }
                ],
            }
        )

    if args.command == "read-log":
        if args.job_id == INITIAL_JOB_ID:
            return emit(
                {
                    "job_id": INITIAL_JOB_ID,
                    "log": (
                        "CI configuration defect: ci-config.txt has cache-version=v1; "
                        "completion verification requires cache-version=v2. "
                        "This is a low-risk CI configuration defect within the authorized "
                        "scope; no Product, Business, Architecture, credential, or external "
                        "dependency blocker was observed."
                    ),
                }
            )
        if args.job_id == REPAIRED_JOB_ID:
            require_repaired_run_ready()
            return emit(
                {
                    "job_id": REPAIRED_JOB_ID,
                    "log": (
                        "completion verification passed for exact head def456 with "
                        "cache-version=v2"
                    ),
                }
            )
        fail(f"unknown job id: {args.job_id}")

    if args.command == "read-artifacts":
        require_run(args.run_id)
        if args.run_id == INITIAL_RUN_ID:
            return emit(
                {
                    "run_id": INITIAL_RUN_ID,
                    "artifacts": [
                        {
                            "id": 7000,
                            "name": "failure-diagnostics",
                            "expired": False,
                            "digest": "sha256:" + "b" * 64,
                        }
                    ],
                }
            )
        require_repaired_run_ready()
        return emit(
            {
                "run_id": REPAIRED_RUN_ID,
                "artifacts": [
                    {
                        "id": 7001,
                        "name": "completion-evidence",
                        "expired": False,
                        "digest": "sha256:" + "a" * 64,
                    }
                ],
            }
        )

    if args.command == "register-fix":
        if args.base_head != INITIAL_HEAD_SHA:
            fail(f"unexpected base head: {args.base_head}")
        if not CONFIG_PATH.is_file():
            fail("ci-config.txt is missing")
        if CONFIG_PATH.read_text(encoding="utf-8") != "cache-version=v2\n":
            fail("minimal CI fix not present: ci-config.txt must be exactly cache-version=v2")
        state = load_state()
        state["fix_registered"] = True
        state["new_head_sha"] = REPAIRED_HEAD_SHA
        write_state(state)
        return emit(
            {
                "base_head_sha": INITIAL_HEAD_SHA,
                "new_head_sha": REPAIRED_HEAD_SHA,
                "changed_file": "ci-config.txt",
                "change": "cache-version=v1 -> cache-version=v2",
            }
        )

    if args.command == "dispatch-rerun":
        if args.head != REPAIRED_HEAD_SHA:
            fail(f"unexpected rerun head: {args.head}")
        state = load_state()
        if not state.get("fix_registered"):
            fail("minimal fix has not been registered")
        state["rerun_dispatched"] = True
        write_state(state)
        return emit(
            {
                "accepted": True,
                "event": "pull_request",
                "head_sha": REPAIRED_HEAD_SHA,
                "run_id": REPAIRED_RUN_ID,
                "status": "queued",
            }
        )

    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
