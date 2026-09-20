from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import distribution_audit as da  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def owner_text(owner_id: str, distribution: str | None, target: str | None = None) -> str:
    metadata = [
        "---",
        f"id: {owner_id}",
        "type: architecture",
        "status: active",
    ]
    if distribution is not None:
        metadata.append(f"distribution: {distribution}")
    if target is not None:
        metadata.append(f"release-target: {target}")
    metadata.extend(["---", "", "# Owner", ""])
    return "\n".join(metadata)


def skill_text(distribution: str | None, target: str | None = None) -> str:
    lines = [
        "---",
        "name: example",
        'description: "Example skill."',
        "metadata:",
        '  agentic-dev-id: "skill:example"',
        '  agentic-dev-type: "skill"',
        '  agentic-dev-status: "active"',
    ]
    if distribution is not None:
        lines.append(f'  agentic-dev-distribution: "{distribution}"')
    if target is not None:
        lines.append(f'  agentic-dev-release-target: "{target}"')
    lines.extend(["---", "", "# Example", ""])
    return "\n".join(lines)


class DistributionAuditTests(unittest.TestCase):
    def make_repo(self):
        temp = tempfile.TemporaryDirectory()
        return temp, Path(temp.name)

    def test_valid_owner_skill_and_runtime_pass(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        write(root / "docs/architecture/a.md", owner_text("architecture:a", "release-input", "software-development"))
        write(root / "skills/example/SKILL.md", skill_text("release-direct", "software-development"))
        write(root / "tools/example/tool.py", "# agentic-dev-distribution: source-only\n")
        result = da.audit(root)
        self.assertEqual("ok", result["status"])
        self.assertEqual([], result["unclassified"])
        self.assertEqual([], result["orphan_release_input"])

    def test_missing_distribution_fails_closed(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        write(root / "docs/architecture/a.md", owner_text("architecture:a", None))
        result = da.audit(root)
        self.assertEqual("fail-closed", result["status"])
        self.assertEqual(["docs/architecture/a.md"], result["unclassified"])

    def test_release_input_requires_target(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        write(root / "docs/architecture/a.md", owner_text("architecture:a", "release-input"))
        result = da.audit(root)
        self.assertEqual("fail-closed", result["status"])
        self.assertEqual(["docs/architecture/a.md"], result["orphan_release_input"])

    def test_skill_navigation_readme_is_scoped_owner(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        write(
            root / "skills/README.md",
            owner_text("guide:skill-inventory", "source-only"),
        )
        result = da.audit(root)
        self.assertEqual("ok", result["status"])
        self.assertEqual(1, result["scoped_asset_count"])

    def test_generated_python_cache_is_not_repository_asset(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        write(
            root / "docs/architecture/a.md",
            owner_text("architecture:a", "source-only"),
        )
        write(root / "tools/example/__pycache__/tool.cpython-312.pyc", "generated")
        write(root / "evals/__pycache__/runner.cpython-312.pyc", "generated")
        result = da.audit(root)
        self.assertEqual("ok", result["status"])
        self.assertEqual([], result["unexpected_unowned"])
        self.assertEqual(1, result["repository_file_count"])

    def test_duplicate_identity_is_ambiguous(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        write(root / "docs/architecture/a.md", owner_text("architecture:duplicate", "source-only"))
        write(root / "docs/architecture/b.md", owner_text("architecture:duplicate", "source-only"))
        result = da.audit(root)
        self.assertEqual("fail-closed", result["status"])
        self.assertEqual(
            ["docs/architecture/a.md", "docs/architecture/b.md"],
            result["ambiguous_release_owner"],
        )


if __name__ == "__main__":
    unittest.main()
