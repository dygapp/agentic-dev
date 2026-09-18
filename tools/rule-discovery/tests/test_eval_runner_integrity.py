from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]
EVALS_DIR = REPO_ROOT / "evals"
sys.path.insert(0, str(EVALS_DIR))

import run_codex_evals as runner  # noqa: E402
import run_governance_evals as governance_runner  # noqa: E402


class EvalRunnerIntegrityTests(unittest.TestCase):
    def run_python(self, script: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), *args],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_behavior_runner_covers_current_behavior_corpus(self):
        expected_files = sorted((EVALS_DIR / "behavior").glob("*.json"))
        self.assertEqual(expected_files, runner.BEHAVIOR_FILES)

        expected_ids: list[str] = []
        for path in expected_files:
            document = json.loads(path.read_text(encoding="utf-8"))
            expected_ids.extend(case["id"] for case in document["evals"])

        actual_ids = [case["id"] for _, case in runner.behavior_cases()]
        self.assertEqual(sorted(expected_ids), sorted(actual_ids))
        self.assertEqual(len(actual_ids), len(set(actual_ids)))
        self.assertIn("B-RV-01", actual_ids)
        self.assertIn("B-HR-01", actual_ids)

    def test_runner_help_entrypoints_import_cleanly(self):
        for script in (
            EVALS_DIR / "run_codex_evals.py",
            EVALS_DIR / "run_governance_evals.py",
        ):
            with self.subTest(script=script.name):
                completed = self.run_python(script, "--help")
                self.assertEqual(0, completed.returncode, completed.stderr)

        self.assertTrue(callable(governance_runner.main))

    def test_governance_context_paths_resolve_current_repository_files(self):
        referenced: set[str] = set()
        for path in governance_runner.GOVERNANCE_FILES:
            document = json.loads(path.read_text(encoding="utf-8"))
            for relative in document["context_paths"]:
                referenced.add(relative)
                self.assertTrue(
                    (REPO_ROOT / relative).exists(),
                    f"{path.name}: missing context path {relative}",
                )

        self.assertNotIn("docs/guides/terminology-guidelines.md", referenced)
        self.assertNotIn("docs/architecture/technology-profile-contract.md", referenced)
        self.assertNotIn("docs/architecture/skill-contracts.md", referenced)
        self.assertNotIn("docs/method/ai-development-method.md", referenced)

    def test_mode_mismatch_fails_before_codex_invocation(self):
        completed = self.run_python(
            EVALS_DIR / "run_codex_evals.py",
            "--behavior",
            "--scenario",
            "D-V4-GEN-01",
            "--codex-bin",
            "false",
        )
        self.assertEqual(2, completed.returncode)
        self.assertIn("not available in the selected mode", completed.stderr)
        self.assertNotIn("Codex CLI version check failed", completed.stderr)

    def test_default_mode_rejects_discovery_only_scenario(self):
        completed = self.run_python(
            EVALS_DIR / "run_codex_evals.py",
            "--scenario",
            "D-V4-GEN-01",
            "--codex-bin",
            "false",
        )
        self.assertEqual(2, completed.returncode)
        self.assertIn("not available in the selected mode", completed.stderr)


if __name__ == "__main__":
    unittest.main()
