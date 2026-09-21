#!/usr/bin/env python3
"""Deterministic read-only GitHub Actions observation transport for B-GA-01."""

from __future__ import annotations

import argparse
import json
import sys


RUN_ID = 4242
JOB_ID = 9001
HEAD_SHA = "abc123"


def emit(payload: dict) -> int:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


def require(value: int, expected: int, label: str) -> None:
    if value != expected:
        raise SystemExit(f"unknown {label}: {value}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only deterministic Actions fixture. "
            "Use poll 1 then poll 2 for bounded observation of Run 4242."
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

    args = parser.parse_args()

    if args.command == "read-run":
        require(args.run_id, RUN_ID, "run id")
        if args.poll == 1:
            return emit(
                {
                    "id": RUN_ID,
                    "run_attempt": 1,
                    "event": "pull_request",
                    "head_sha": HEAD_SHA,
                    "status": "in_progress",
                    "conclusion": None,
                }
            )
        return emit(
            {
                "id": RUN_ID,
                "run_attempt": 1,
                "event": "pull_request",
                "head_sha": HEAD_SHA,
                "status": "completed",
                "conclusion": "success",
            }
        )

    if args.command == "read-jobs":
        require(args.run_id, RUN_ID, "run id")
        return emit(
            {
                "run_id": RUN_ID,
                "jobs": [
                    {
                        "id": JOB_ID,
                        "name": "completion-verification",
                        "status": "completed",
                        "conclusion": "success",
                        "steps": [
                            {
                                "name": "verify-current-head",
                                "status": "completed",
                                "conclusion": "success",
                            }
                        ],
                    }
                ],
            }
        )

    if args.command == "read-log":
        require(args.job_id, JOB_ID, "job id")
        return emit(
            {
                "job_id": JOB_ID,
                "log": "completion verification passed for exact head abc123",
            }
        )

    if args.command == "read-artifacts":
        require(args.run_id, RUN_ID, "run id")
        return emit(
            {
                "run_id": RUN_ID,
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

    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
