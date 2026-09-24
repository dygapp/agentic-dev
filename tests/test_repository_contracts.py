from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
OBLIGATIONS = ROOT / "tests" / "fixtures" / "legacy-consumer-obligations.json"

EXPECTED_SKILLS = {"activate-model-collaboration", "clarify-architecture", "clarify-intent", "converge", "establish-requirement-baseline", "execute-unit", "external-operation", "github-actions-verification", "human-review", "readiness-check", "review-change", "slice-work", "specify", "systematic-debug", "technical-plan"}
RETIRED_PATHS = (
    "docs/methods",
    "docs/rules",
    "docs/project/project-capability-profile.md",
    "docs/project/distribution-rebuild-specification.md",
    "docs/architecture/consumer-architecture.md",
    "docs/architecture/data-migration-architecture.md",
    "docs/architecture/engineering-capability-architecture.md",
    "docs/architecture/human-review-architecture.md",
    "docs/architecture/method-architecture.md",
    "docs/architecture/model-collaboration-architecture.md",
    "docs/architecture/project-knowledge-architecture.md",
    "docs/architecture/release-architecture.md",
    "docs/architecture/requirement-authority-architecture.md",
    "docs/architecture/rule-architecture.md",
    "docs/architecture/rule-discovery-architecture.md",
    "tools/rule-discovery",
    "tools/release-build",
    "tools/distribution-audit",
    "tools/runtime-acceptance",
    "evals",
    ".github/workflows/rule-discovery.yml",
    ".github/workflows/release-build.yml",
    ".github/workflows/runtime-acceptance.yml",
)
RETIRED_LOCATORS = (
    "docs/methods/",
    "docs/rules/",
    "docs/architecture/consumer-architecture.md",
    "docs/architecture/data-migration-architecture.md",
    "docs/architecture/engineering-capability-architecture.md",
    "docs/architecture/human-review-architecture.md",
    "docs/architecture/method-architecture.md",
    "docs/architecture/model-collaboration-architecture.md",
    "docs/architecture/project-knowledge-architecture.md",
    "docs/architecture/release-architecture.md",
    "docs/architecture/requirement-authority-architecture.md",
    "docs/architecture/rule-architecture.md",
    "docs/architecture/rule-discovery-architecture.md",
    "project-capability-profile",
    "tools/rule-discovery",
    "tools/release-build",
    "evals/run_codex",
    "authenticated_model_acceptance",
)

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def frontmatter_keys(text: str) -> set[str]:
    if not text.startswith("---\n"):
        raise AssertionError("SKILL.md missing frontmatter")
    _, block, _ = text.split("---\n", 2)
    return {line.split(":", 1)[0].strip() for line in block.splitlines() if line.strip() and not line.startswith(" ")}

class RepositoryContractsTests(unittest.TestCase):
    def test_canonical_skill_inventory_and_frontmatter(self):
        actual = {p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file()}
        self.assertEqual(EXPECTED_SKILLS, actual)
        for name in sorted(actual):
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertEqual({"name", "description"}, frontmatter_keys(text), name)

    def test_skills_do_not_depend_on_provider_runtime_docs(self):
        forbidden = ("docs/methods/", "docs/rules/", "docs/architecture/", "project-capability-profile", "rule-discovery", "release-build")
        for path in SKILLS.glob("*/SKILL.md"):
            text = path.read_text(encoding="utf-8")
            for token in forbidden:
                self.assertNotIn(token, text, f"{path}: {token}")

    def test_retired_runtime_paths_are_absent(self):
        for relative in RETIRED_PATHS:
            self.assertFalse((ROOT / relative).exists(), relative)

    def test_active_entrypoints_have_no_retired_locators(self):
        paths = [ROOT / "AGENTS.md", ROOT / "README.md", ROOT / "docs/project/README.md", ROOT / "docs/project/project-charter.md", ROOT / "docs/architecture/README.md", ROOT / "docs/architecture/skill-architecture.md", ROOT / "skills/README.md"]
        paths += sorted((ROOT / "docs/guides").glob("*.md"))
        paths += sorted((ROOT / "docs/governance").glob("*.md"))
        for path in paths:
            text = path.read_text(encoding="utf-8")
            for locator in RETIRED_LOCATORS:
                self.assertNotIn(locator, text, f"{path}: {locator}")

    def test_consumer_install_smoke_preserves_owned_files(self):
        with tempfile.TemporaryDirectory() as temp:
            consumer = Path(temp)
            (consumer / "docs/constraints").mkdir(parents=True)
            agents = consumer / "AGENTS.md"
            policy = consumer / "docs/constraints/policy.md"
            agents.write_text("# Consumer Authority\n", encoding="utf-8")
            policy.write_text("# Consumer Policy\n", encoding="utf-8")
            before = {agents: sha256(agents), policy: sha256(policy)}
            target = consumer / ".agents/skills"
            target.mkdir(parents=True)
            for name in sorted(EXPECTED_SKILLS):
                shutil.copytree(SKILLS / name, target / name, dirs_exist_ok=True)
                shutil.copytree(SKILLS / name, target / name, dirs_exist_ok=True)
            self.assertEqual(EXPECTED_SKILLS, {p.name for p in target.iterdir() if (p / "SKILL.md").is_file()})
            self.assertEqual(before, {agents: sha256(agents), policy: sha256(policy)})

    def test_legacy_obligations_have_current_owners(self):
        obligations = json.loads(OBLIGATIONS.read_text(encoding="utf-8"))["obligations"]
        self.assertEqual([f"GF-{i:02d}" for i in range(1, 27)], [item["id"] for item in obligations])
        for item in obligations:
            kind = item["owner_kind"]
            self.assertIn(kind, {"consumer-local", "files", "all-skills-escalation", "repository-contract"})
            if kind in {"files", "repository-contract"}:
                self.assertTrue(item["owners"], item["id"])
                for relative in item["owners"]:
                    self.assertTrue((ROOT / relative).exists(), f"{item['id']}: {relative}")
        for path in SKILLS.glob("*/SKILL.md"):
            self.assertIn("## 升级", path.read_text(encoding="utf-8"), str(path))

    def test_webcodex_codex_cli_boundary_is_durable(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("WebCodex Runner **不得直接或间接启动 `codex-cli`**", agents)
        for workflow in (ROOT / ".github/workflows").glob("*.yml"):
            text = workflow.read_text(encoding="utf-8")
            self.assertNotIn("codex exec", text)
            self.assertNotIn("codex app-server", text)

if __name__ == "__main__":
    unittest.main()
