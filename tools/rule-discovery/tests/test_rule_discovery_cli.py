from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOL = Path(__file__).resolve().parents[1] / "rule_discovery.py"
TOOL_DIR = TOOL.parent
sys.path.insert(0, str(TOOL_DIR))
import rule_discovery as rd  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


class DiscoveryCliTests(unittest.TestCase):
    def run_tool(self, *args: str):
        return subprocess.run(
            [sys.executable, str(TOOL), "--repo-root", str(REPO_ROOT), *args],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_discover_cli_returns_locator_only_json(self):
        signals = json.dumps(
            {
                "phases": ["execute"],
                "activities": ["implementation"],
                "technologies": [],
                "artifacts": ["code"],
                "risks": [],
            }
        )
        completed = self.run_tool("discover", "--signals-json", signals)
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("ok", payload["status"])
        self.assertEqual(20, payload["scanned"])
        self.assertEqual(payload["candidate_count"], len(payload["candidates"]))
        self.assertTrue(payload["candidates"])
        self.assertTrue(all(set(item) == {"id", "path"} for item in payload["candidates"]))
        self.assertNotIn("scope", completed.stdout)
        self.assertNotIn("summary", completed.stdout)

    def test_invalid_signal_cli_exits_two_and_returns_no_candidates(self):
        completed = self.run_tool(
            "discover",
            "--signals-json",
            '{"phases":["execute"]}',
        )
        self.assertEqual(2, completed.returncode)
        payload = json.loads(completed.stdout)
        self.assertEqual("fail-closed", payload["status"])
        self.assertEqual([], payload["candidates"])
        self.assertTrue(payload["diagnostics"])

    def test_symlink_directory_in_rule_root_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rule_root = root / "docs/rules"
            rule_root.mkdir(parents=True)
            target = root / "linked-rule-source"
            target.mkdir()
            (target / "a.md").write_text(
                """---
id: rule:linked
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code]
  risks: []
---
# Linked Rule

Body.
""",
                encoding="utf-8",
            )
            link = rule_root / "linked"
            try:
                link.symlink_to(target, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"symlink unavailable: {exc}")

            signals = json.dumps(
                {
                    "phases": ["execute"],
                    "activities": ["implementation"],
                    "technologies": [],
                    "artifacts": ["code"],
                    "risks": [],
                }
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(TOOL),
                    "--repo-root",
                    str(root),
                    "discover",
                    "--signals-json",
                    signals,
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(2, completed.returncode, completed.stderr)
            payload = json.loads(completed.stdout)
            self.assertEqual("fail-closed", payload["status"])
            self.assertEqual([], payload["candidates"])
            self.assertTrue(
                any("symlink directories" in item for item in payload["diagnostics"])
            )

    def test_lint_cli_succeeds_on_current_repository(self):
        completed = self.run_tool("lint")
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("ok", payload["status"])
        self.assertEqual(15, payload["skills"])
        self.assertEqual(20, payload["rules"])


class ScanCompletenessTests(unittest.TestCase):
    def test_missing_rule_root_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaises(rd.ContractError):
                rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])

    def test_missing_front_matter_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rule_dir = root / "docs/rules/x"
            rule_dir.mkdir(parents=True)
            (rule_dir / "a.md").write_text("# no metadata\n", encoding="utf-8")
            with self.assertRaises(rd.ContractError):
                rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])

    def test_missing_scope_dimension_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rule_dir = root / "docs/rules/x"
            rule_dir.mkdir(parents=True)
            (rule_dir / "a.md").write_text(
                """---
id: rule:a
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code]
---
# body
""",
                encoding="utf-8",
            )
            with self.assertRaises(rd.ContractError):
                rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])

    def test_empty_rule_body_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rule_dir = root / "docs/rules/x"
            rule_dir.mkdir(parents=True)
            (rule_dir / "a.md").write_text(
                """---
id: rule:a
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: []
  artifacts: [code]
  risks: []
---
""",
                encoding="utf-8",
            )
            with self.assertRaises(rd.ContractError):
                rd.scan_rules(repo_root=root, rule_roots=[Path("docs/rules")])


if __name__ == "__main__":
    unittest.main()
