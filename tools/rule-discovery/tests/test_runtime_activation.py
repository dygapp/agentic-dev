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
        self.assertIn("这些通过结果 **不能替代** 当前 task signals 的 task-level discovery", agents)
        self.assertIn("preflight infrastructure invocation", agents)

    def test_architecture_distinguishes_ci_from_runtime_discovery(self):
        architecture = (
            REPO_ROOT / "docs/architecture/rule-discovery-architecture.md"
        ).read_text(encoding="utf-8")
        self.assertIn("### 10.1 责任转换检查点", architecture)
        self.assertIn("不能替代 ordinary runtime invocation", architecture)

    def test_pr_and_push_verification_use_exact_subject_identity(self):
        workflow = (REPO_ROOT / ".github/workflows/rule-discovery.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("Checkout exact verification subject", workflow)
        self.assertIn("Verify exact verification subject", workflow)
        self.assertIn("github.event.pull_request.head.sha", workflow)
        self.assertIn("github.sha", workflow)
        self.assertIn("EXPECTED_SHA", workflow)
        self.assertIn("git rev-parse HEAD", workflow)
        self.assertIn("checked-out SHA does not match verification subject", workflow)

    def test_cloud_task_discovery_preserves_exact_sha_and_machine_readable_evidence(self):
        workflow = (REPO_ROOT / ".github/workflows/rule-discovery.yml").read_text(
            encoding="utf-8"
        )
        profile = (REPO_ROOT / "docs/project/project-capability-profile.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("issue_comment:", workflow)
        self.assertIn("target_sha:", workflow)
        self.assertIn("signals_json:", workflow)
        self.assertIn("git rev-parse HEAD", workflow)
        self.assertIn("checked-out SHA does not match requested SHA", workflow)
        self.assertIn("actions/upload-artifact@v4", workflow)
        self.assertIn("task-rule-discovery-result.json", workflow)
        self.assertIn("/rule-discovery <40-char-sha> <signals-json>", profile)
        self.assertIn("`OWNER` / `MEMBER` / `COLLABORATOR`", profile)


if __name__ == "__main__":
    unittest.main()
