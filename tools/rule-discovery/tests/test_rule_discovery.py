from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

TOOL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


def _signal_value(value):
    return None if value is None else list(value)


def signals(
    *,
    phases=(),
    activities=(),
    technologies=(),
    artifacts=(),
    risks=(),
):
    return {
        "phases": _signal_value(phases),
        "activities": _signal_value(activities),
        "technologies": _signal_value(technologies),
        "artifacts": _signal_value(artifacts),
        "risks": _signal_value(risks),
    }


def rule_text(
    rule_id: str,
    *,
    status: str = "active",
    phases=("execute",),
    activities=("implementation",),
    technologies=(),
    artifacts=("code",),
    risks=(),
    extra_top: str = "",
) -> str:
    def array(items):
        return "[" + ", ".join(items) + "]"

    return f"""---
id: {rule_id}
type: rule
status: {status}
scope:
  phases: {array(phases)}
  activities: {array(activities)}
  technologies: {array(technologies)}
  artifacts: {array(artifacts)}
  risks: {array(risks)}
{extra_top}---

# Test Rule

Normative body.
"""


class CurrentRepositoryTests(unittest.TestCase):
    def discover(self, value):
        return rd.discover(
            repo_root=REPO_ROOT,
            rule_roots=[Path("docs/rules")],
            signals=value,
        )

    def test_current_repository_lints(self):
        result = rd.lint_repository(
            repo_root=REPO_ROOT,
            rule_roots=[Path("docs/rules")],
        )
        self.assertEqual("ok", result["status"])
        self.assertEqual(11, result["skills"])
        self.assertGreaterEqual(result["rules"], 40)
        self.assertTrue(result["fixture_markdown_excluded"])

    def test_generation_filters_out_data_access_without_signal(self):
        result = self.discover(
            signals(phases=["execute"], activities=["implementation"], artifacts=["code"])
        )
        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:implementation-minimality", ids)
        self.assertIn("rule:surgical-change", ids)
        self.assertNotIn("rule:data-access-boundedness", ids)

    def test_data_access_signal_adds_data_access_rule(self):
        result = self.discover(
            signals(
                phases=["execute"],
                activities=["implementation"],
                artifacts=["code", "data-access"],
            )
        )
        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:data-access-boundedness", ids)

    def test_database_migration_verification_is_discriminating(self):
        result = self.discover(
            signals(
                phases=["converge"],
                activities=["verification"],
                artifacts=["database-migration"],
            )
        )
        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:database-migration-completion-evidence", ids)
        self.assertIn("rule:evidence-type-must-match-claim", ids)
        self.assertNotIn("rule:visual-evidence", ids)

    def test_visual_verification_excludes_database_migration_rule(self):
        result = self.discover(
            signals(
                phases=["execute"],
                activities=["verification"],
                artifacts=["user-interface"],
                risks=["visual-fidelity"],
            )
        )
        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:visual-evidence", ids)
        self.assertIn("rule:evidence-type-must-match-claim", ids)
        self.assertNotIn("rule:database-migration-completion-evidence", ids)

    def test_mixed_vue_typecheck_returns_specific_and_general_rules(self):
        result = self.discover(
            signals(
                phases=["execute"],
                activities=["implementation", "verification"],
                technologies=["vue3", "typescript"],
                artifacts=["code", "vue-sfc"],
                risks=["type-safety"],
            )
        )
        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:implementation-minimality", ids)
        self.assertIn("rule:surgical-change", ids)
        self.assertIn("rule:vue-build-vs-typecheck", ids)
        self.assertIn("rule:evidence-type-must-match-claim", ids)

    def test_unknown_risk_does_not_exclude_risk_scoped_rule(self):
        result = self.discover(
            signals(
                phases=["execute"],
                activities=["implementation"],
                technologies=["vue3"],
                artifacts=["vue-sfc"],
                risks=None,
            )
        )
        ids = {item["id"] for item in result["candidates"]}
        self.assertIn("rule:vue-props-one-way-input", ids)

    def test_known_empty_risk_excludes_risk_scoped_rule(self):
        result = self.discover(
            signals(
                phases=["execute"],
                activities=["implementation"],
                technologies=["vue3"],
                artifacts=["vue-sfc"],
                risks=[],
            )
        )
        ids = {item["id"] for item in result["candidates"]}
        self.assertNotIn("rule:vue-props-one-way-input", ids)

    def test_candidate_output_does_not_leak_metadata(self):
        result = self.discover(
            signals(phases=["execute"], activities=["implementation"], artifacts=["code"])
        )
        self.assertEqual({"status", "scanned", "candidate_count", "candidates"}, set(result))
        for candidate in result["candidates"]:
            self.assertEqual({"id", "path"}, set(candidate))

    def test_overlapping_roots_fail_closed_on_duplicate_physical_rule(self):
        with self.assertRaises(rd.ContractError):
            rd.scan_rules(
                repo_root=REPO_ROOT,
                rule_roots=[Path("docs/rules"), Path("docs/rules/generation")],
            )


class ContractFailureTests(unittest.TestCase):
    def make_repo(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "docs/rules/test").mkdir(parents=True)
        return temp, root

    def test_unknown_rule_metadata_fails_closed(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        path = root / "docs/rules/test/a.md"
        path.write_text(rule_text("rule:a", extra_top="summary: duplicate body\n"), encoding="utf-8")
        with self.assertRaises(rd.ContractError):
            rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])

    def test_duplicate_rule_id_fails_closed(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        first = root / "docs/rules/test/a.md"
        second = root / "docs/rules/test/b.md"
        first.write_text(rule_text("rule:duplicate"), encoding="utf-8")
        second.write_text(rule_text("rule:duplicate"), encoding="utf-8")
        with self.assertRaises(rd.ContractError):
            rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])

    def test_inactive_discoverable_rule_fails_closed(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        path = root / "docs/rules/test/a.md"
        path.write_text(rule_text("rule:a", status="deprecated"), encoding="utf-8")
        with self.assertRaises(rd.ContractError):
            rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])

    def test_all_wildcard_scope_fails_lint(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        path = root / "docs/rules/test/a.md"
        path.write_text(
            rule_text(
                "rule:a",
                phases=(),
                activities=(),
                technologies=(),
                artifacts=(),
                risks=(),
            ),
            encoding="utf-8",
        )
        with self.assertRaises(rd.ContractError):
            rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])

    def test_invalid_task_signal_shape_fails_closed(self):
        bad = {
            "phases": ["execute"],
            "activities": ["implementation"],
            "technologies": [],
            "artifacts": ["code"],
        }
        with self.assertRaises(rd.ContractError):
            rd.validate_task_signals(bad)

    def test_illegal_task_signal_token_fails_closed(self):
        bad = signals(phases=["Execute"], activities=["implementation"], artifacts=["code"])
        with self.assertRaises(rd.ContractError):
            rd.validate_task_signals(bad)

    def test_signal_synonym_cloud_fails_closed(self):
        bad = signals(
            phases=["execute"],
            activities=[
                "implementation",
                "coding",
                "authoring",
                "editing",
                "modification",
                "generation",
                "development",
            ],
            artifacts=["code"],
        )
        with self.assertRaises(rd.ContractError):
            rd.validate_task_signals(bad)

    def test_directory_path_does_not_change_matching_semantics(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        original = root / "docs/rules/test/a.md"
        original.write_text(rule_text("rule:path-independent"), encoding="utf-8")
        query = signals(phases=["execute"], activities=["implementation"], artifacts=["code"])

        first = rd.discover(repo_root=root, rule_roots=[Path("docs/rules")], signals=query)
        moved_dir = root / "docs/rules/renamed"
        moved_dir.mkdir()
        moved = moved_dir / "moved.md"
        original.rename(moved)
        second = rd.discover(repo_root=root, rule_roots=[Path("docs/rules")], signals=query)

        self.assertEqual(["rule:path-independent"], [c["id"] for c in first["candidates"]])
        self.assertEqual(["rule:path-independent"], [c["id"] for c in second["candidates"]])
        self.assertNotEqual(first["candidates"][0]["path"], second["candidates"][0]["path"])

    def test_front_matter_parser_rejects_deeper_yaml(self):
        text = """---
id: rule:a
type: rule
status: active
scope:
  phases: [execute]
    invalid: deeper
---
body
"""
        with self.assertRaises(rd.ContractError):
            rd.parse_front_matter_text(text, source="inline")


if __name__ == "__main__":
    unittest.main()