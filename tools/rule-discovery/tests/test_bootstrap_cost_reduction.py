from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]
RUNNER_PATH = REPO_ROOT / "evals" / "run_codex_evals.py"
BASELINE_PATH = REPO_ROOT / "evals" / "bootstrap" / "r3-cost-baseline.json"
SPEC = importlib.util.spec_from_file_location("run_codex_evals_r3", RUNNER_PATH)
assert SPEC and SPEC.loader
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class BootstrapCostReductionTests(unittest.TestCase):
    def baseline(self) -> dict:
        return json.loads(BASELINE_PATH.read_text(encoding="utf-8"))

    def discovery_case(self) -> dict:
        return next(
            case
            for case in runner.discovery_cases()
            if case["id"] == "D-V4-GEN-01"
        )

    def test_fixed_bootstrap_reads_and_context_are_reduced(self):
        baseline = self.baseline()
        current_paths = list(runner.AGENTIC_DEV_DISCOVERY_BOOTSTRAP_PATHS)
        selected_method = self.discovery_case()["selected_method"]

        self.assertEqual(
            [
                "AGENTS.md",
                "docs/project/project-roadmap.md",
                "docs/project/project-capability-profile.md",
            ],
            current_paths,
        )
        self.assertNotIn("README.md", current_paths)
        self.assertNotIn("docs/architecture/method-architecture.md", current_paths)

        current_fixed_chars = sum(
            len((REPO_ROOT / path).read_text(encoding="utf-8"))
            for path in current_paths
        )
        current_pre_discovery_reads = len(current_paths) + 1
        current_pre_discovery_chars = (
            current_fixed_chars
            + len((REPO_ROOT / selected_method).read_text(encoding="utf-8"))
        )

        self.assertLess(current_pre_discovery_reads, baseline["pre_discovery_file_reads"])
        self.assertEqual(4, current_pre_discovery_reads)
        self.assertLess(current_fixed_chars, baseline["fixed_chars"])
        self.assertLess(current_pre_discovery_chars, baseline["pre_discovery_chars"])

    def test_same_task_preserves_method_and_rule_discovery_behavior(self):
        baseline = self.baseline()
        case = self.discovery_case()
        self.assertEqual(baseline["selected_method"], case["selected_method"])

        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            runner.populate_discovery_context(workspace, case)

            profile = (
                workspace / "docs/project/project-capability-profile.md"
            ).read_text(encoding="utf-8")
            method_path = workspace / case["selected_method"]
            method = method_path.read_text(encoding="utf-8")

            self.assertIn(case["selected_method"], profile)
            self.assertIn(baseline["expected_method_id"], profile)
            self.assertIn(f"id: {baseline['expected_method_id']}", method)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(workspace / "tools/rule-discovery/rule_discovery.py"),
                    "--repo-root",
                    str(workspace),
                    "discover",
                    "--signals-json",
                    json.dumps(baseline["rule_signals"], separators=(",", ":")),
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            payload = json.loads(completed.stdout)
            actual_ids = sorted(item["id"] for item in payload["candidates"])
            self.assertEqual(sorted(baseline["expected_rule_ids"]), actual_ids)

    def test_agents_declares_human_and_method_architecture_as_on_demand(self):
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        bootstrap = agents.split("## Fresh Context / Agent 启动", 1)[1].split(
            "## Method 选择", 1
        )[0]

        self.assertIn("`README.md` 属于 Human View", bootstrap)
        self.assertIn("才按需读取 `docs/architecture/method-architecture.md`", bootstrap)
        self.assertNotIn(
            "读取 `README.md`、`docs/project/project-roadmap.md`",
            bootstrap,
        )


if __name__ == "__main__":
    unittest.main()
