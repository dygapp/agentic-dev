from __future__ import annotations

from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]


class RepositoryBootstrapClosureTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (REPO_ROOT / relative).read_text(encoding="utf-8")

    def test_rule_discovery_supports_out_of_process_compute_without_platform_ownership(self):
        architecture = self.read("docs/architecture/rule-discovery-architecture.md")

        self.assertIn("进程外执行契约", architecture)
        self.assertIn("不要求与当前 Agent 位于同一 execution environment", architecture)
        self.assertIn("缺少 worktree、shell、Python", architecture)
        self.assertIn("requested / actual baseline", architecture)
        self.assertIn("locator-only result", architecture)
        self.assertIn("所有 declared transports 都不可用", architecture)
        out_of_process_contract = architecture.split(
            "### 10.2 进程外执行契约", maxsplit=1
        )[1]
        self.assertNotIn("GitHub Actions", out_of_process_contract)

    def test_agentic_dev_profile_owns_transport_selection_and_verification_instance(self):
        profile = self.read("docs/project/project-capability-profile.md")

        self.assertIn("Rule Discovery 传输方式选择", profile)
        self.assertIn("优先使用本地调用", profile)
        self.assertIn("GitHub Actions exact-SHA transport", profile)
        self.assertIn("仓库原生确定性计算 / 验证实例", profile)
        self.assertIn("工作流已启动或请求被接受不构成通过", profile)
        self.assertIn("不维护 workflow catalog", profile)

    def test_consumer_contract_requires_a_local_executable_instance(self):
        consumer = self.read("docs/architecture/consumer-architecture.md")
        adoption = self.read("docs/methods/consumer-adoption.md")
        upgrade = self.read("docs/methods/consumer-upgrade.md")
        combined = "\n".join((consumer, adoption, upgrade))

        for required in (
            "Consumer-local executable instance",
            "direct execution path",
            "automated alternate path",
            "result / Evidence recovery",
            "fail-closed behavior",
            "Fresh Runtime",
        ):
            self.assertIn(required, combined)
        self.assertIn("upstream access = 0", consumer)

    def test_human_guide_explains_layers_without_retired_routing_modes(self):
        guide = self.read("docs/guides/github-agent-workflow.md")

        self.assertIn("Repository Authority / execution transport / verification", guide)
        self.assertIn("actions/checkout", guide)
        self.assertIn("工作流已启动", guide)
        self.assertIn("ancestor Evidence", guide)
        self.assertIn("讨论 → 修改", guide)
        self.assertNotIn("A / B / C", guide)
        self.assertNotIn("Forced B", guide)
        self.assertNotIn("Cloud Repository Runtime", guide)


if __name__ == "__main__":
    unittest.main()
