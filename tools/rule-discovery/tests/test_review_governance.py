from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


class ReviewGovernanceContractTests(unittest.TestCase):
    def test_current_owner_transition_rule_is_phase_agnostic_and_discoverable(self):
        result = rd.discover(
            repo_root=REPO_ROOT,
            rule_roots=[Path("docs/rules")],
            signals={
                "phases": ["execute"],
                "activities": ["review", "documentation"],
                "technologies": [],
                "artifacts": ["authority", "skill", "rule", "repository-governance"],
                "risks": ["high-impact-change", "authority-lifecycle"],
            },
        )
        self.assertEqual("ok", result["status"])
        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:authoritative-artifact-lifecycle-review", ids)
        self.assertIn("rule:high-impact-ai-review-required", ids)
        self.assertIn("rule:human-facing-content-integrity", ids)

    def test_review_change_owns_bounded_authority_chain_semantic_review(self):
        skill = (REPO_ROOT / "skills/review-change/SKILL.md").read_text(encoding="utf-8")
        lifecycle_rule = (
            REPO_ROOT / "docs/rules/repository/authoritative-artifact-lifecycle-review.md"
        ).read_text(encoding="utf-8")
        rule_ids = {
            item.id
            for item in rd.scan_rules(repo_root=REPO_ROOT, rule_roots=[Path("docs/rules")])
        }

        self.assertIn("## 权威链语义复核", skill)
        self.assertIn("Current owner transition", skill)
        self.assertIn("Downstream observable projection", skill)
        self.assertIn("Replaceability seam", skill)
        self.assertIn("Conflict classification", skill)
        self.assertIn("Source role / promotion boundary", skill)
        self.assertIn("## 有界可再生性挑战", skill)
        self.assertIn("普通代码修复", skill)
        self.assertIn("不因为本模式存在而自动执行 full regenerability", skill)

        self.assertIn("## 当前归属转换完整性", lifecycle_rule)
        self.assertIn("Historical、archive、migration provenance", lifecycle_rule)
        self.assertIn("出现旧标识本身不构成 stale Current dependency", lifecycle_rule)
        self.assertNotIn("rule:current-owner-transition-completeness", rule_ids)

    def test_review_change_behavior_eval_covers_failure_driven_semantics(self):
        path = REPO_ROOT / "evals/behavior/review-change.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual("review-change", payload["skill_name"])
        evals = payload["evals"]
        ids = {item["id"] for item in evals}
        self.assertEqual({"B-RV-01", "B-RV-02", "B-RV-03", "B-RV-04"}, ids)
        for item in evals:
            self.assertTrue(item["prompt"].strip())
            self.assertTrue(item["expected_behavior"].strip())
            self.assertGreaterEqual(len(item["assertions"]), 4)


if __name__ == "__main__":
    unittest.main()
