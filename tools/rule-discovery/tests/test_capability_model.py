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

        self.assertIn("Project 不传播，Capability 传播", project_arch)
        self.assertIn("Project 不传播，Capability 传播", consumer_arch)
        self.assertIn("不是可传播给 Consumer 的 capability", profile)

    def test_skill_architecture_does_not_own_current_inventory(self):
        skill_arch = (REPO_ROOT / "docs/architecture/skill-architecture.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("## 4. 当前分类", skill_arch)
        self.assertNotIn("总数为 11", skill_arch)
        self.assertNotIn("核心 AI Development supporting Skills（8）", skill_arch)
        self.assertIn("Skill Inventory Ownership", skill_arch)

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

        self.assertIn("Stable phase identities", ai_method)
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
        self.assertIn("Human View", methods_readme)
        self.assertIn("project-capability-profile.md", methods_readme)

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

    def test_skill_human_inventory_matches_skill_corpus(self):
        actual = {path.parent.name for path in (REPO_ROOT / "skills").glob("*/SKILL.md")}
        readme = (REPO_ROOT / "skills/README.md").read_text(encoding="utf-8")
        listed = set(re.findall(r"^- `([a-z0-9]+(?:-[a-z0-9]+)*)`$", readme, flags=re.MULTILINE))
        self.assertEqual(actual, listed)


if __name__ == "__main__":
    unittest.main()
