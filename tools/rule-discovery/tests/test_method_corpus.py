from __future__ import annotations

from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parents[3]


class MethodCorpusTests(unittest.TestCase):
    def read(self, path: str) -> str:
        return (REPO_ROOT / path).read_text(encoding="utf-8")

    def test_project_clarification_super_method_is_retired(self):
        self.assertFalse(
            (REPO_ROOT / "docs/methods/software-project-clarification.md").exists()
        )

        current_entries = [
            self.read("docs/methods/README.md"),
            self.read("docs/methods/ai-development.md"),
            self.read("docs/guides/using-agentic-dev.md"),
            self.read("docs/project/project-roadmap.md"),
        ]

        for text in current_entries:
            self.assertNotIn("method:software-project-clarification", text)
            self.assertNotIn("software-project-clarification.md", text)

    def test_requirement_and_architecture_methods_are_canonical(self):
        requirement = self.read(
            "docs/methods/requirement-baseline-establishment.md"
        )
        architecture = self.read("docs/methods/architecture-clarification.md")
        methods_readme = self.read("docs/methods/README.md")

        self.assertIn("id: method:requirement-baseline-establishment", requirement)
        self.assertIn("Requirement Baseline Ready", requirement)
        self.assertIn("Derive → Default → Ask → Review", requirement)

        self.assertIn("id: method:architecture-clarification", architecture)
        self.assertIn("Architecture Context Ready", architecture)
        self.assertIn("不是所有新项目的必经步骤", architecture)

        self.assertIn("requirement-baseline-establishment.md", methods_readme)
        self.assertIn("architecture-clarification.md", methods_readme)

    def test_requirement_authority_boundaries_are_explicit(self):
        requirement_architecture = self.read(
            "docs/architecture/requirement-authority-architecture.md"
        )
        guide = self.read("docs/guides/establishing-requirement-baseline.md")

        self.assertIn("`README.md` — Human Navigation / Usage Guide", requirement_architecture)
        self.assertIn("`index.md` — Requirement Authority Index", requirement_architecture)
        self.assertIn("`analysis/` 默认是非 Authority workspace", requirement_architecture)
        self.assertIn("Question Gate", guide)
        self.assertIn("不存在的可能功能是无限集合", guide)

    def test_ai_development_routes_systemic_gaps_to_correct_method(self):
        ai_development = self.read("docs/methods/ai-development.md")

        self.assertIn("method:requirement-baseline-establishment", ai_development)
        self.assertIn("method:architecture-clarification", ai_development)
        self.assertIn("upstream capability 存在本身不构成 Consumer 的隐式 adoption", ai_development)


if __name__ == "__main__":
    unittest.main()
