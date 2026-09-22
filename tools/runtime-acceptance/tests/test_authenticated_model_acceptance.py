from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


authenticated = _load_module(
    "agentic_dev_authenticated_model_acceptance",
    REPO_ROOT / "tools/runtime-acceptance/authenticated_model_acceptance.py",
)


class AuthenticatedModelAcceptanceTests(unittest.TestCase):
    def _write_mode_evidence(
        self,
        results: Path,
        *,
        source_sha: str,
        scenario: str = "B-RB-01",
    ) -> Path:
        root = results / "behavior"
        root.mkdir(parents=True)
        release_id = f"agentic-dev@0.0.0-eval.{source_sha[:12]}+{source_sha[:12]}"
        (root / "runtime-acceptance.summary.json").write_text(
            json.dumps({"status": "PASS", "scenario_count": 1}) + "\n",
            encoding="utf-8",
        )
        (root / f"{scenario}.run.json").write_text(
            json.dumps(
                {
                    "scenario_id": scenario,
                    "source_commit": source_sha,
                    "runtime_mode": "release-installed",
                    "release_id": release_id,
                    "returncode": 0,
                    "grading": "pass",
                    "codex_version": "codex-runtime",
                    "grader_codex_version": "codex-grader",
                }
            )
            + "\n",
            encoding="utf-8",
        )
        grade_path = root / f"{scenario}.grade.json"
        grade_path.write_text(
            json.dumps(
                {
                    "scenario_id": scenario,
                    "source_commit": source_sha,
                    "runtime_mode": "release-installed",
                    "release_id": release_id,
                    "runtime_codex_version": "codex-runtime",
                    "grader_codex_version": "codex-grader",
                    "verdict": "PASS",
                }
            )
            + "\n",
            encoding="utf-8",
        )
        for suffix in (
            ".jsonl",
            ".stderr.txt",
            ".grader.jsonl",
            ".grader.stderr.txt",
        ):
            (root / f"{scenario}{suffix}").write_text("", encoding="utf-8")
        return grade_path

    def test_collect_mode_evidence_accepts_bound_grade_identity(self):
        source_sha = "a" * 40
        with tempfile.TemporaryDirectory() as temp:
            repo_root = Path(temp)
            results = repo_root / "evals/results"
            self._write_mode_evidence(results, source_sha=source_sha)
            with (
                mock.patch.object(authenticated, "REPO_ROOT", repo_root),
                mock.patch.object(authenticated, "RESULTS", results),
            ):
                payload = authenticated._collect_mode_evidence(
                    "behavior",
                    ("B-RB-01",),
                    source_sha,
                )
            self.assertEqual(payload["status"], "PASS")
            self.assertEqual(payload["scenarios"][0]["scenario_id"], "B-RB-01")

    def test_collect_mode_evidence_rejects_stale_grade_subject(self):
        source_sha = "a" * 40
        with tempfile.TemporaryDirectory() as temp:
            repo_root = Path(temp)
            results = repo_root / "evals/results"
            grade_path = self._write_mode_evidence(results, source_sha=source_sha)
            grade = json.loads(grade_path.read_text(encoding="utf-8"))
            grade["source_commit"] = "0" * 40
            grade_path.write_text(json.dumps(grade) + "\n", encoding="utf-8")
            with (
                mock.patch.object(authenticated, "REPO_ROOT", repo_root),
                mock.patch.object(authenticated, "RESULTS", results),
            ):
                with self.assertRaisesRegex(
                    authenticated.AuthenticatedRuntimeError,
                    "semantic grade source SHA mismatch",
                ):
                    authenticated._collect_mode_evidence(
                        "behavior",
                        ("B-RB-01",),
                        source_sha,
                    )


if __name__ == "__main__":
    unittest.main()
