from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


runtime = _load_module(
    "agentic_dev_runtime_acceptance",
    REPO_ROOT / "tools/runtime-acceptance/runtime_acceptance.py",
)


class RuntimeAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source_sha = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    def _fixture(self, root: Path) -> dict:
        return runtime.build_and_install_fixture(
            REPO_ROOT,
            root / "runtime",
            self.source_sha,
        )

    def test_canonical_skill_fixture_satisfies_static_runtime_contract(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            result = runtime.verify_installed_fixture(
                fixture["consumer"],
                expected_skills=fixture["source_skills"],
            )
            self.assertEqual("ok", result["status"])
            self.assertEqual(15, result["skill_count"])
            self.assertFalse(result["provider_source_paths_present"])
            self.assertEqual(
                [
                    "AGENTS.md",
                    ".agents/skills/<name>/SKILL.md",
                ],
                result["chatgpt_compatibility_path"],
            )
            self.assertFalse((fixture["consumer"] / ".agents/release").exists())
            self.assertEqual(
                runtime.canonical_skill_set_sha256(REPO_ROOT),
                fixture["skill_set_sha256"],
            )

    def test_consumer_owned_files_survive_fixture_install(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            self.assertIn(
                "Consumer Repository Authority",
                (consumer / "AGENTS.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "Consumer-owned",
                (consumer / "docs/product.md").read_text(encoding="utf-8"),
            )

    @unittest.skipIf(
        os.name != "posix" or getattr(os, "geteuid", lambda: -1)() == 0,
        "permission-denial negative control requires a non-root POSIX user",
    )
    def test_upstream_source_unavailable_negative_control_restores_permissions(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "provider-source"
            consumer = root / "consumer"
            source.mkdir()
            consumer.mkdir()
            sentinel = source / "sentinel.txt"
            sentinel.write_text("provider-only\n", encoding="utf-8")

            with runtime.upstream_source_unavailable(source, consumer) as evidence:
                self.assertEqual("ok", evidence["status"])
                self.assertEqual("denied", evidence["provider_source_read_probe"])

            self.assertEqual("provider-only\n", sentinel.read_text(encoding="utf-8"))

    def test_missing_installed_skill_fails_closed_against_canonical_inventory(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            skill = next((consumer / ".agents/skills").glob("*/SKILL.md"))
            skill.unlink()
            with self.assertRaisesRegex(
                runtime.RuntimeAcceptanceError,
                "installed Skill inventory mismatch",
            ):
                runtime.verify_installed_fixture(
                    consumer,
                    expected_skills=fixture["source_skills"],
                )

    def test_tampered_installed_skill_fails_digest_check(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            skill = consumer / ".agents/skills/clarify-intent/SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8") + "\nTAMPERED\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                runtime.RuntimeAcceptanceError,
                "installed Skill package digest mismatch",
            ):
                runtime.verify_installed_fixture(
                    consumer,
                    expected_skills=fixture["source_skills"],
                )

    def test_provider_style_runtime_namespace_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            forbidden = consumer / ".agents/rules"
            forbidden.mkdir(parents=True)
            (forbidden / "legacy.md").write_text("legacy\n", encoding="utf-8")
            with self.assertRaisesRegex(
                runtime.RuntimeAcceptanceError,
                "forbidden provider-style runtime namespace",
            ):
                runtime.verify_installed_fixture(consumer)

    def test_legacy_release_namespace_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            legacy = consumer / ".agents/release"
            legacy.mkdir(parents=True)
            with self.assertRaisesRegex(
                runtime.RuntimeAcceptanceError,
                "forbidden provider-style runtime namespace|legacy release runtime",
            ):
                runtime.verify_installed_fixture(consumer)

    def test_provider_source_dependency_inside_skill_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            skill = consumer / ".agents/skills/clarify-intent/SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8")
                + "\nRead docs/rules/provider-only.md before execution.\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                runtime.RuntimeAcceptanceError,
                "depends on provider Source path",
            ):
                runtime.verify_installed_fixture(consumer)

    def test_old_release_composition_token_inside_skill_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            skill = consumer / ".agents/skills/clarify-intent/SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8")
                + "\nagentic-dev-release-inputs: legacy\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                runtime.RuntimeAcceptanceError,
                "retired composition token",
            ):
                runtime.verify_installed_fixture(consumer)


if __name__ == "__main__":
    unittest.main()
