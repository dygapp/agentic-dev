from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402


RULE = """---
id: rule:test-navigation
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code]
  risks: []
---

# Test Rule

Normative body.
"""

README = """---
id: guide:rules-navigation
type: guide
status: active
---

# Rules Navigation

Human-only navigation.
"""


class HumanNavigationTests(unittest.TestCase):
    def test_readme_is_not_discoverable_rule_but_is_repository_resource(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rules = root / "docs/rules/generation"
            rules.mkdir(parents=True)
            (root / "docs/rules/README.md").write_text(README, encoding="utf-8")
            (rules / "test.md").write_text(RULE, encoding="utf-8")

            scanned = rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])
            self.assertEqual(["rule:test-navigation"], [item.id for item in scanned])

            linted = rd.lint_repository(repo_root=root, rule_roots=[Path("docs/rules")])
            self.assertEqual("ok", linted["status"])
            self.assertEqual(1, linted["rules"])
            self.assertEqual(1, linted["markdown_resources"])

    def test_non_readme_markdown_in_rule_root_still_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rules = root / "docs/rules"
            rules.mkdir(parents=True)
            (rules / "navigation.md").write_text(README, encoding="utf-8")

            with self.assertRaises(rd.ContractError):
                rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])


if __name__ == "__main__":
    unittest.main()
