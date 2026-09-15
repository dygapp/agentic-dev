from __future__ import annotations

from pathlib import Path
import sys
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


class RuntimeActivationRegressionTests(unittest.TestCase):
    def test_integration_state_closure_is_discoverable_without_method_phase(self):
        result = rd.discover(
            repo_root=REPO_ROOT,
            rule_roots=[Path("docs/rules")],
            signals={
                "phases": None,
                "activities": ["review"],
                "technologies": [],
                "artifacts": ["roadmap", "repository-state"],
                "risks": ["integration-state"],
            },
        )

        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:integration-state-closure-review", ids)

    def test_bootstrap_requires_task_level_discovery_before_side_effects(self):
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("首个有副作用动作前必须完成本次 task-level discovery", agents)
        self.assertIn("其 PASS 不得替代 ordinary runtime invocation", agents)

    def test_architecture_distinguishes_ci_from_runtime_discovery(self):
        architecture = (
            REPO_ROOT / "docs/architecture/rule-discovery-architecture.md"
        ).read_text(encoding="utf-8")
        self.assertIn("### 10.1 Responsibility transition checkpoint", architecture)
        self.assertIn("不能替代 ordinary runtime invocation", architecture)


if __name__ == "__main__":
    unittest.main()
