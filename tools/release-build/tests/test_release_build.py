from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


release_build = _load_module(
    "agentic_dev_release_build",
    REPO_ROOT / "tools/release-build/release_build.py",
)
installer = _load_module(
    "agentic_dev_install_release",
    REPO_ROOT / "tools/release-build/install_release.py",
)


class ReleaseBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source_sha = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    def _build(self, output: Path, version: str = "0.0.0-test") -> tuple[Path, dict]:
        result = release_build.build_release(
            REPO_ROOT,
            output,
            self.source_sha,
            version,
            "test://release-build",
        )
        archive = output / result["archive"]
        return archive, result

    def test_build_is_byte_deterministic_for_same_inputs(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            first, first_result = self._build(root / "a")
            second, second_result = self._build(root / "b")
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(first_result["archive_sha256"], second_result["archive_sha256"])
            self.assertEqual(first_result["manifest_sha256"], second_result["manifest_sha256"])

    def test_release_contains_only_bounded_runtime_and_install_surfaces(self):
        with tempfile.TemporaryDirectory() as temp:
            archive, result = self._build(Path(temp))
            self.assertEqual(result["skill_count"], 15)
            self.assertEqual(result["software_release_input_count"], 26)
            self.assertEqual(result["installation_input_count"], 3)

            with zipfile.ZipFile(archive, "r") as zf:
                names = set(zf.namelist())
                manifest = json.loads(zf.read("manifest.json").decode("utf-8"))
                index = json.loads(
                    zf.read("repository/.agents/release/skill-index.json").decode("utf-8")
                )

            self.assertEqual(len(manifest["skills"]), 15)
            self.assertEqual(len(index["skills"]), 15)
            self.assertIn("repository/.agents/README.md", names)
            self.assertIn("repository/.agents/release/manifest.json", names)
            self.assertIn("install.py", names)
            self.assertFalse(any(name.startswith("docs/project/") for name in names))
            self.assertFalse(any(name.startswith("docs/research/") for name in names))
            self.assertFalse(any(name.startswith("evals/") for name in names))
            self.assertFalse(any(name.startswith("docs/guides/") for name in names))
            self.assertFalse(any(name.startswith("repository/.agents/rules/") for name in names))
            self.assertFalse(any(name.startswith("repository/.agents/methods/") for name in names))
            self.assertFalse(any(name.startswith("repository/.agents/architecture/") for name in names))
            install_refs = {
                name for name in names if name.startswith("installation/references/")
            }
            self.assertEqual(len(install_refs), 3)

    def test_archive_verifier_checks_manifest_integrity(self):
        with tempfile.TemporaryDirectory() as temp:
            archive, result = self._build(Path(temp))
            verified = release_build.verify_archive(archive)
            self.assertEqual(verified["status"], "ok")
            self.assertEqual(verified["release_id"], result["release_id"])
            self.assertEqual(verified["archive_sha256"], result["archive_sha256"])

    def test_install_preserves_consumer_authority_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive, result = self._build(root / "out")
            package = root / "package"
            with zipfile.ZipFile(archive, "r") as zf:
                zf.extractall(package)

            target = root / "consumer"
            target.mkdir()
            (target / "AGENTS.md").write_text(
                "# Consumer Authority\n\nDo not overwrite this content.\n",
                encoding="utf-8",
            )
            (target / "docs").mkdir()
            (target / "docs/product.md").write_text("consumer fact\n", encoding="utf-8")

            first = installer.install(package, target)
            self.assertEqual(first["status"], "ok")
            agents = (target / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("# Consumer Authority", agents)
            self.assertIn("Do not overwrite this content.", agents)
            self.assertEqual(agents.count(installer.START), 1)
            self.assertEqual(agents.count(installer.END), 1)
            self.assertEqual(
                (target / "docs/product.md").read_text(encoding="utf-8"),
                "consumer fact\n",
            )
            self.assertTrue((target / ".agents/README.md").is_file())
            self.assertTrue((target / ".agents/release/manifest.json").is_file())
            self.assertEqual(
                len(list((target / ".agents/skills").glob("*/SKILL.md"))),
                result["skill_count"],
            )

            before = {
                path.relative_to(target).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(target.rglob("*"))
                if path.is_file()
            }
            second = installer.install(package, target)
            self.assertEqual(second["status"], "ok")
            after = {
                path.relative_to(target).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(target.rglob("*"))
                if path.is_file()
            }
            self.assertEqual(before, after)

    def test_first_install_fails_closed_on_unowned_skill_conflict(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive, _ = self._build(root / "out")
            package = root / "package"
            with zipfile.ZipFile(archive, "r") as zf:
                zf.extractall(package)

            target = root / "consumer"
            conflict = target / ".agents/skills/clarify-intent"
            conflict.mkdir(parents=True)
            (conflict / "local.txt").write_text("local skill\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "conflicts with release Skill"):
                installer.install(package, target)


if __name__ == "__main__":
    unittest.main()
