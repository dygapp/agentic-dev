from __future__ import annotations

from pathlib import Path
import sys
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


class CapabilityModelContractTests(unittest.TestCase):
    def test_canonical_methods_are_parseable_and_selected_by_bootstrap(self):
        expected = {
            "docs/methods/ai-development.md": "method:ai-development",
            "docs/methods/consumer-adoption.md": "method:consumer-adoption",
            "docs/methods/consumer-upgrade.md": "method:consumer-upgrade",
        }
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

        for relative, method_id in expected.items():
            path = REPO_ROOT / relative
            self.assertTrue(path.is_file(), relative)
            parsed = rd.parse_front_matter_file(path)
            self.assertEqual(method_id, parsed.metadata.get("id"))
            self.assertEqual("method", parsed.metadata.get("type"))
            self.assertEqual("active", parsed.metadata.get("status"))
            self.assertIn(relative, agents)

    def test_retired_single_method_and_consumer_lifecycle_paths_are_absent(self):
        self.assertFalse((REPO_ROOT / "docs/method").exists())
        self.assertFalse((REPO_ROOT / "docs/architecture/consumer-lifecycle.md").exists())

    def test_human_navigation_exists_without_becoming_method_selector(self):
        self.assertTrue((REPO_ROOT / "docs/methods/README.md").is_file())
        self.assertTrue((REPO_ROOT / "docs/rules/README.md").is_file())
        self.assertTrue((REPO_ROOT / "docs/guides/README.md").is_file())
        self.assertTrue((REPO_ROOT / "docs/architecture/README.md").is_file())

        methods_readme = (REPO_ROOT / "docs/methods/README.md").read_text(encoding="utf-8")
        self.assertIn("Human View", methods_readme)
        self.assertIn("Agent 的 Method 选择", methods_readme)


if __name__ == "__main__":
    unittest.main()
