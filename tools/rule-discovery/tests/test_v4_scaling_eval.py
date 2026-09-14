from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]
RUNNER_PATH = REPO_ROOT / "evals" / "run_v4_scaling.py"
SPEC = importlib.util.spec_from_file_location("run_v4_scaling", RUNNER_PATH)
assert SPEC and SPEC.loader
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class V4ScalingFixtureTests(unittest.TestCase):
    def document(self):
        return runner.load_json(runner.CORPUS)

    def test_scaling_levels_are_exactly_20_100_500(self):
        document = self.document()
        self.assertEqual([20, 100, 500], [case["rule_count"] for case in document["evals"]])
        self.assertEqual(2, len(document["target_rule_paths"]))
        self.assertEqual(2, len(document["expected_candidate_ids"]))

    def test_each_scale_has_exact_rule_count_and_constant_candidates(self):
        document = self.document()
        expected_ids = sorted(document["expected_candidate_ids"])
        for case in document["evals"]:
            with self.subTest(case=case["id"]), tempfile.TemporaryDirectory() as temp_dir:
                workspace = Path(temp_dir)
                runner.populate_scaling_workspace(workspace, document, case)
                rule_files = list((workspace / "docs" / "rules").rglob("*.md"))
                self.assertEqual(case["rule_count"], len(rule_files))

                preflight = runner.preflight_discovery(workspace)
                self.assertEqual(case["rule_count"], preflight["scanned"])
                self.assertEqual(2, preflight["candidate_count"])
                self.assertEqual(expected_ids, sorted(preflight["candidate_ids"]))

    def test_scaling_runtime_does_not_receive_grader_corpus(self):
        document = self.document()
        case = document["evals"][0]
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            runner.populate_scaling_workspace(workspace, document, case)
            self.assertTrue((workspace / "AGENTS.md").is_file())
            self.assertTrue((workspace / "task.md").is_file())
            self.assertTrue((workspace / "tools/rule-discovery/rule_discovery.py").is_file())
            self.assertFalse((workspace / "evals/discovery/v4-scaling.json").exists())
            self.assertFalse((workspace / "evals/results").exists())

    def test_decoys_are_nonmatching_by_stable_phase_boundary(self):
        document = self.document()
        case = next(case for case in document["evals"] if case["rule_count"] == 20)
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            runner.populate_scaling_workspace(workspace, document, case)
            decoy = workspace / "docs/rules/scaling/decoy-0001.md"
            text = decoy.read_text(encoding="utf-8")
            self.assertIn("phases: [specification]", text)
            self.assertIn("activities: [review]", text)
            self.assertNotIn("phases: [execute]", text)


if __name__ == "__main__":
    unittest.main()
