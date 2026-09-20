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
        self.assertIn("Authoritative Default", requirement)
        self.assertIn("Provisional Minimal Default", requirement)
        self.assertIn("不自动等于已确认长期 Requirement", requirement)

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

        self.assertIn("`README.md` — 人类导航 / 使用指南", requirement_architecture)
        self.assertIn("`index.md` — Requirement Authority Index", requirement_architecture)
        self.assertIn("`analysis/` 默认是非 Authority workspace", requirement_architecture)
        self.assertIn("问题门禁", guide)
        self.assertIn("不存在的可能功能是无限集合", guide)

    def test_ai_development_routes_systemic_gaps_to_correct_method(self):
        ai_development = self.read("docs/methods/ai-development.md")

        self.assertIn("method:requirement-baseline-establishment", ai_development)
        self.assertIn("method:architecture-clarification", ai_development)
        self.assertIn("只有已安装 Release 与 Consumer-local Authority 才定义 Consumer 当前可用能力", ai_development)


if __name__ == "__main__":
    unittest.main()
