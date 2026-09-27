from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


def git(repository: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repository), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class NestedRepositoryLayoutTests(unittest.TestCase):
    def test_ignored_component_is_independent_but_force_add_and_clean_remain_hazards(self):
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp) / "project"
            project.mkdir()
            git(project, "init", "-q")
            (project / ".gitignore").write_text("/backend/\n", encoding="utf-8")
            (project / "AGENTS.md").write_text("# Project Authority\n", encoding="utf-8")
            git(project, "add", "--all")
            git(project, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-q", "-m", "project baseline")

            backend = project / "backend"
            backend.mkdir()
            git(backend, "init", "-q")
            (backend / "AGENTS.md").write_text("# Component Authority\n", encoding="utf-8")
            (backend / "app.txt").write_text("component code\n", encoding="utf-8")
            git(backend, "add", "--all")
            git(backend, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-q", "-m", "component baseline")

            self.assertEqual(str(project), git(project, "rev-parse", "--show-toplevel"))
            self.assertEqual(str(backend), git(backend, "rev-parse", "--show-toplevel"))
            self.assertEqual("", git(project, "status", "--porcelain"))
            self.assertEqual("", git(project, "ls-files", "--stage", "--", "backend"))
            self.assertIn("backend/", git(project, "clean", "-n", "-ffdx"))

            project_head = git(project, "rev-parse", "HEAD")
            backend_head = git(backend, "rev-parse", "HEAD")
            (backend / "app.txt").write_text("changed component code\n", encoding="utf-8")
            git(backend, "add", "--all")
            git(backend, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-q", "-m", "component change")
            self.assertNotEqual(backend_head, git(backend, "rev-parse", "HEAD"))
            self.assertEqual(project_head, git(project, "rev-parse", "HEAD"))
            self.assertEqual("", git(project, "status", "--porcelain"))

            git(project, "add", "-f", "--", "backend")
            self.assertTrue(git(project, "ls-files", "--stage", "--", "backend").startswith("160000 "))


if __name__ == "__main__":
    unittest.main()
