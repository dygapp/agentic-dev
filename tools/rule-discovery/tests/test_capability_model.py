from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


class CapabilityModelContractTests(unittest.TestCase):
    def test_canonical_methods_are_parseable_and_selected_by_project_profile(self):
        expected = {
            "docs/methods/ai-development.md": "method:ai-development",
            "docs/methods/consumer-adoption.md": "method:consumer-adoption",
            "docs/methods/consumer-upgrade.md": "method:consumer-upgrade",
            "docs/methods/model-collaboration-adoption.md": "method:model-collaboration-adoption",
        }
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        method_architecture = (REPO_ROOT / "docs/architecture/method-architecture.md").read_text(
            encoding="utf-8"
        )
        profile = (REPO_ROOT / "docs/project/project-capability-profile.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("docs/architecture/method-architecture.md", agents)
        self.assertIn("docs/project/project-capability-profile.md", agents)
        for relative, method_id in expected.items():
            path = REPO_ROOT / relative
            self.assertTrue(path.is_file(), relative)
            parsed = rd.parse_front_matter_file(path)
            self.assertEqual(method_id, parsed.metadata.get("id"))
            self.assertEqual("method", parsed.metadata.get("type"))
            self.assertEqual("active", parsed.metadata.get("status"))
            self.assertIn(relative, profile)
            self.assertIn(method_id, profile)
            self.assertNotIn(relative, method_architecture)
            self.assertNotIn(relative, agents)

    def test_project_knowledge_owners_exist_and_are_typed(self):
        expected_project = [
            "docs/project/project-charter.md",
            "docs/project/project-capability-profile.md",
            "docs/project/project-roadmap.md",
            "docs/project/project-evolution.md",
        ]
        for relative in expected_project:
            path = REPO_ROOT / relative
            self.assertTrue(path.is_file(), relative)
            parsed = rd.parse_front_matter_file(path)
            self.assertEqual("project", parsed.metadata.get("type"), relative)
            self.assertEqual("active", parsed.metadata.get("status"), relative)

        self.assertTrue((REPO_ROOT / "docs/project/README.md").is_file())
        boundary = REPO_ROOT / "docs/architecture/project-knowledge-architecture.md"
        self.assertTrue(boundary.is_file())
        parsed = rd.parse_front_matter_file(boundary)
        self.assertEqual("architecture", parsed.metadata.get("type"))
        self.assertEqual("active", parsed.metadata.get("status"))

    def test_project_capability_boundary_is_explicit(self):
        project_arch = (
            REPO_ROOT / "docs/architecture/project-knowledge-architecture.md"
        ).read_text(encoding="utf-8")
        consumer_arch = (REPO_ROOT / "docs/architecture/consumer-architecture.md").read_text(
            encoding="utf-8"
        )
        profile = (REPO_ROOT / "docs/project/project-capability-profile.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Project 不传播；Source capability semantics 通过 Distribution Build 发布", project_arch)
        self.assertIn("Source type / path 不直接传播", project_arch)
        self.assertIn("Consumer 安装 Release", consumer_arch)
        self.assertIn("不是 Consumer Release", profile)

    def test_consumer_distribution_contract_is_release_based(self):
        engineering = (
            REPO_ROOT / "docs/architecture/engineering-capability-architecture.md"
        ).read_text(encoding="utf-8")
        consumer = (REPO_ROOT / "docs/architecture/consumer-architecture.md").read_text(
            encoding="utf-8"
        )
        adoption = (REPO_ROOT / "docs/methods/consumer-adoption.md").read_text(
            encoding="utf-8"
        )
        upgrade = (REPO_ROOT / "docs/methods/consumer-upgrade.md").read_text(
            encoding="utf-8"
        )
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("Source Model 与 Distribution Model", engineering)
        self.assertIn("Skill package", engineering)
        self.assertIn(".agents/skills/**", consumer)
        self.assertIn("根 `AGENTS.md` 始终由 Consumer 拥有", consumer)
        self.assertIn("默认**不要求**创建", consumer)
        self.assertIn(".agents/rules/", consumer)
        self.assertIn("不默认安装 upstream Rule tree", consumer)
        self.assertIn("版本化 Release", adoption)
        self.assertIn("current installed release", upgrade)
        self.assertIn("不比较 Consumer tree 与 upstream Source tree", upgrade)
        self.assertIn("普通软件 Consumer 通过版本化 Release", agents)
        self.assertIn("upstream access = 0", agents)

    def test_runtime_instance_locator_has_single_project_owner(self):
        profile = (REPO_ROOT / "docs/project/project-capability-profile.md").read_text(
            encoding="utf-8"
        )
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        discovery_arch = (
            REPO_ROOT / "docs/architecture/rule-discovery-architecture.md"
        ).read_text(encoding="utf-8")
        tool_locator = "tools/rule-discovery/rule_discovery.py"

        self.assertIn(tool_locator, profile)
        self.assertIn("--signals-json '<task-signals-json>'", profile)
        self.assertNotIn(tool_locator, agents)
        self.assertNotIn(tool_locator, discovery_arch)
        self.assertIn("Bootstrap 不复制第二份 Tool path 或完整 invocation contract", agents)
        self.assertIn("workflow_dispatch", profile)
        self.assertIn("issue_comment", profile)

    def test_model_collaboration_ownership_and_local_instance_boundary(self):
        architecture_path = REPO_ROOT / "docs/architecture/model-collaboration-architecture.md"
        method_path = REPO_ROOT / "docs/methods/model-collaboration-adoption.md"
        guide_path = REPO_ROOT / "docs/guides/multi-model-collaboration.md"
        codex_reference_path = REPO_ROOT / "docs/guides/codex-model-collaboration-reference.md"
        research_path = REPO_ROOT / "docs/research/model-collaboration-capability-classification.md"
        profile = (REPO_ROOT / "docs/project/project-capability-profile.md").read_text(
            encoding="utf-8"
        )

        for path, resource_type in [
            (architecture_path, "architecture"),
            (method_path, "method"),
            (guide_path, "guide"),
            (codex_reference_path, "guide"),
            (research_path, "research"),
        ]:
            self.assertTrue(path.is_file(), str(path))
            parsed = rd.parse_front_matter_file(path)
            self.assertEqual(resource_type, parsed.metadata.get("type"), str(path))
            self.assertEqual("active", parsed.metadata.get("status"), str(path))

        architecture = architecture_path.read_text(encoding="utf-8")
        method = method_path.read_text(encoding="utf-8")
        normative = architecture + "\n" + method
        for concrete_model in [
            "gpt-5.6-luna",
            "gpt-5.6-terra",
            "gpt-5.6-sol",
            "gpt-6-astra",
        ]:
            self.assertNotIn(concrete_model, normative)

        self.assertIn("single-writer", architecture)
        self.assertIn("保持权威的交接", architecture)
        self.assertIn("single-agent fallback", architecture)
        self.assertIn("installed release", architecture)
        self.assertIn("functional enablement claim", architecture)
        self.assertIn("efficiency / preferred-default claim", architecture)
        self.assertIn("Confirm Installed Collaboration Capability", method)
        self.assertIn("Detect Runtime Capabilities", method)
        self.assertIn("Plan Local Runtime Integration", method)
        self.assertIn("Validate Collaboration", method)
        self.assertIn("不得绕过 Consumer Release 安装 / 升级", method)
        self.assertIn("## 5. Model Collaboration 实例", profile)
        self.assertIn("status：`disabled`", profile)
        self.assertIn("persistent platform config：none", profile)

        codex_reference = codex_reference_path.read_text(encoding="utf-8")
        self.assertIn("2026-09-14", codex_reference)
        self.assertIn(".codex/agents/", codex_reference)
        self.assertIn("sandbox_mode = \"read-only\"", codex_reference)
        self.assertIn("sandbox_mode = \"workspace-write\"", codex_reference)
        self.assertIn("[agents]", codex_reference)
        self.assertIn("enabled = false", codex_reference)
        self.assertIn("functional enablement", codex_reference)

    def test_skill_architecture_does_not_own_current_inventory(self):
        skill_arch = (REPO_ROOT / "docs/architecture/skill-architecture.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("## 4. 当前分类", skill_arch)
        self.assertNotIn("总数为 11", skill_arch)
        self.assertNotIn("核心 AI Development supporting Skills（8）", skill_arch)
        self.assertIn("Skill 清单归属", skill_arch)

    def test_ai_development_method_owns_phase_identities(self):
        expected_tokens = {
            "clarify-intent",
            "specification",
            "technical-planning",
            "slice-ready",
            "execute",
            "converge",
        }
        ai_method = (REPO_ROOT / "docs/methods/ai-development.md").read_text(encoding="utf-8")
        discovery_arch = (
            REPO_ROOT / "docs/architecture/rule-discovery-architecture.md"
        ).read_text(encoding="utf-8")

        self.assertIn("稳定阶段身份", ai_method)
        for token in expected_tokens:
            self.assertIn(f"`{token}`", ai_method)
            self.assertNotIn(f"`{token}`", discovery_arch)
        self.assertIn("不拥有任何具体 Method 的 phase token 列表", discovery_arch)

    def test_retired_single_method_and_consumer_lifecycle_paths_are_absent(self):
        self.assertFalse((REPO_ROOT / "docs/method").exists())
        self.assertFalse((REPO_ROOT / "docs/methods/principles.md").exists())
        self.assertFalse((REPO_ROOT / "docs/architecture/consumer-lifecycle.md").exists())

    def test_human_navigation_exists_without_becoming_method_selector(self):
        self.assertTrue((REPO_ROOT / "docs/methods/README.md").is_file())
        self.assertTrue((REPO_ROOT / "docs/rules/README.md").is_file())
        self.assertTrue((REPO_ROOT / "docs/guides/README.md").is_file())
        self.assertTrue((REPO_ROOT / "docs/architecture/README.md").is_file())
        self.assertTrue((REPO_ROOT / "docs/project/README.md").is_file())
        self.assertTrue((REPO_ROOT / "skills/README.md").is_file())

        methods_readme = (REPO_ROOT / "docs/methods/README.md").read_text(encoding="utf-8")
        architecture_readme = (REPO_ROOT / "docs/architecture/README.md").read_text(
            encoding="utf-8"
        )
        guides_readme = (REPO_ROOT / "docs/guides/README.md").read_text(encoding="utf-8")
        research_readme = (REPO_ROOT / "docs/research/README.md").read_text(encoding="utf-8")
        self.assertIn("Human View", methods_readme)
        self.assertIn("project-capability-profile.md", methods_readme)
        self.assertIn("model-collaboration-adoption.md", methods_readme)
        self.assertIn("model-collaboration-architecture.md", architecture_readme)
        self.assertIn("multi-model-collaboration.md", guides_readme)
        self.assertIn("codex-model-collaboration-reference.md", guides_readme)
        self.assertIn("model-collaboration-capability-classification.md", research_readme)

    def test_rule_human_inventory_matches_discoverable_rule_corpus(self):
        actual = {
            item.locator
            for item in rd.scan_rules(repo_root=REPO_ROOT, rule_roots=[Path("docs/rules")])
        }
        readme = (REPO_ROOT / "docs/rules/README.md").read_text(encoding="utf-8")
        linked = {
            f"docs/rules/{target}"
            for target in re.findall(r"\]\(([^)]+\.md)\)", readme)
            if not target.startswith("../") and not target.startswith("docs/")
        }
        self.assertEqual(actual, linked)

    def test_upstream_rule_corpus_has_no_technology_knowledge_directory(self):
        self.assertFalse((REPO_ROOT / "docs/rules/technology").exists())

    def test_skill_human_inventory_matches_skill_corpus(self):
        actual = {path.parent.name for path in (REPO_ROOT / "skills").glob("*/SKILL.md")}
        readme = (REPO_ROOT / "skills/README.md").read_text(encoding="utf-8")
        listed = set(re.findall(r"^- `([a-z0-9]+(?:-[a-z0-9]+)*)`$", readme, flags=re.MULTILINE))
        self.assertEqual(actual, listed)


if __name__ == "__main__":
    unittest.main()
