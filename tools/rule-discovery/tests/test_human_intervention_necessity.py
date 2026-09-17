from __future__ import annotations

from pathlib import Path
import sys
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


class HumanInterventionNecessityTests(unittest.TestCase):
    def test_human_escalation_discovers_necessity_rule(self):
        result = rd.discover(
            repo_root=REPO_ROOT,
            rule_roots=[Path("docs/rules")],
            signals={
                "phases": None,
                "activities": ["human-escalation"],
                "technologies": [],
                "artifacts": [],
                "risks": ["human-intervention"],
            },
        )

        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:human-intervention-necessity", ids)

    def test_ordinary_external_operation_does_not_force_human_intervention_rule(self):
        result = rd.discover(
            repo_root=REPO_ROOT,
            rule_roots=[Path("docs/rules")],
            signals={
                "phases": None,
                "activities": ["external-operation"],
                "technologies": [],
                "artifacts": ["repository"],
                "risks": [],
            },
        )

        ids = {item["id"] for item in result["candidates"]}
        self.assertNotIn("rule:human-intervention-necessity", ids)

    def test_bootstrap_declares_human_escalation_checkpoint_without_copying_rule_body(self):
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        rule = (
            REPO_ROOT / "docs/rules/operations/human-intervention-necessity.md"
        ).read_text(encoding="utf-8")

        self.assertIn("human-escalation", agents)
        self.assertIn("human-intervention", agents)
        self.assertIn("发出人工请求前", agents)
        self.assertIn("机械工作转交人工", rule)
        self.assertIn("最小动作或最小决定", rule)
        self.assertNotIn("connector、API、standard git / GitHub", agents)


if __name__ == "__main__":
    unittest.main()
