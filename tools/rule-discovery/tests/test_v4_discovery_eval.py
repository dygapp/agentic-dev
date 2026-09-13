from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]
RUNNER_PATH = REPO_ROOT / "evals" / "run_codex_evals.py"
SPEC = importlib.util.spec_from_file_location("run_codex_evals", RUNNER_PATH)
assert SPEC and SPEC.loader
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class DiscoveryCorpusTests(unittest.TestCase):
    def cases(self):
        return runner.discovery_cases()

    def case(self, scenario_id: str):
        return next(case for case in self.cases() if case["id"] == scenario_id)

    def test_required_v4_categories_are_present_once(self):
        cases = self.cases()
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(
            {
                "generation-discovery",
                "verification-discovery",
                "mixed-responsibility",
                "negative-ambiguity",
                "metadata-invalid",
                "skill-vs-rule",
                "consumer-local",
            },
            {case["category"] for case in cases},
        )
        self.assertEqual(7, len(cases))

    def test_agentic_dev_workspace_contains_runtime_not_grader_material(self):
        case = self.case("D-V4-GEN-01")
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            runner.populate_discovery_context(workspace, case)

            self.assertTrue((workspace / "AGENTS.md").is_file())
            self.assertTrue((workspace / "README.md").is_file())
            self.assertTrue((workspace / "docs/project/project-roadmap.md").is_file())
            self.assertTrue((workspace / "docs/rules").is_dir())
            self.assertTrue((workspace / "tools/rule-discovery/rule_discovery.py").is_file())
            self.assertTrue((workspace / ".agents/skills/execute-unit/SKILL.md").is_file())
            self.assertTrue((workspace / "task.md").is_file())
            self.assertFalse((workspace / "evals/discovery/v4-discriminating.json").exists())
            self.assertFalse((workspace / "evals/results").exists())

    def test_consumer_local_workspace_excludes_upstream_project_state(self):
        case = self.case("D-V4-CONSUMER-01")
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            runner.populate_discovery_context(workspace, case)

            agents = (workspace / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("Consumer Repository Authority", agents)
            self.assertTrue((workspace / "docs/rules").is_dir())
            self.assertTrue((workspace / "tools/rule-discovery/rule_discovery.py").is_file())
            self.assertFalse((workspace / "docs/project/project-roadmap.md").exists())
            self.assertFalse((workspace / "evals/discovery/v4-discriminating.json").exists())

    def test_invalid_metadata_scenario_really_corrupts_local_rule_set(self):
        case = self.case("D-V4-INVALID-01")
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            runner.populate_discovery_context(workspace, case)
            invalid = workspace / "docs/rules/eval/invalid-metadata.md"
            self.assertTrue(invalid.is_file())
            text = invalid.read_text(encoding="utf-8")
            self.assertNotIn("  risks:", text)

    def test_scenario_files_cannot_escape_workspace(self):
        case = {
            "id": "D-V4-TEST-ESCAPE",
            "context_mode": "consumer-local",
            "workspace_files": {"../escape.txt": "nope"},
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaises(RuntimeError):
                runner.populate_discovery_context(Path(temp_dir), case)

    def test_current_source_commit_is_precise_git_identity(self):
        commit = runner.current_source_commit()
        self.assertEqual(40, len(commit))
        self.assertTrue(all(char in "0123456789abcdef" for char in commit))

    def test_run_metadata_records_source_commit_and_codex_version(self):
        previous = dict(runner.RUN_CONTEXT)
        runner.RUN_CONTEXT["source_commit"] = "1" * 40
        runner.RUN_CONTEXT["codex_version"] = "codex-cli test-version"
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                result_dir = Path(temp_dir)
                runner.write_run_metadata(
                    result_dir,
                    "D-V4-TEST-META",
                    ["codex", "exec"],
                    result_dir,
                    0,
                )
                data = json.loads(
                    (result_dir / "D-V4-TEST-META.run.json").read_text(encoding="utf-8")
                )
                self.assertEqual("1" * 40, data["source_commit"])
                self.assertEqual("codex-cli test-version", data["codex_version"])
                self.assertEqual("pending", data["grading"])
        finally:
            runner.RUN_CONTEXT.update(previous)


if __name__ == "__main__":
    unittest.main()
