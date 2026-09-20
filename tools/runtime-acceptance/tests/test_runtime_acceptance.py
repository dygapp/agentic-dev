from __future__ import annotations

import importlib.util
import json
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

    def test_release_installed_fixture_satisfies_static_runtime_contract(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            result = runtime.verify_installed_fixture(fixture["consumer"])
            self.assertEqual("ok", result["status"])
            self.assertEqual(15, result["skill_count"])
            self.assertFalse(result["upstream_runtime_dependency"])
            self.assertEqual(
                [
                    {"name": "external-operation", "kind": "external"},
                    {"name": "github-actions-verification", "kind": "external"},
                ],
                result["execution_contracts"],
            )
            self.assertEqual(
                [
                    "AGENTS.md",
                    ".agents/release/skill-index.json",
                    ".agents/skills/<name>/SKILL.md",
                ],
                result["chatgpt_compatibility_path"],
            )

    def test_tampered_skill_index_path_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            index_path = consumer / ".agents/release/skill-index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["skills"][0]["path"] = "../../outside/SKILL.md"
            index_path.write_text(
                json.dumps(index, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(runtime.RuntimeAcceptanceError, "skill-index mismatch"):
                runtime.verify_installed_fixture(consumer)

    def test_missing_installed_skill_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            manifest = json.loads(
                (consumer / ".agents/release/manifest.json").read_text(encoding="utf-8")
            )
            path = consumer / manifest["skills"][0]["path"]
            path.unlink()
            with self.assertRaisesRegex(runtime.RuntimeAcceptanceError, "installed Skill path is missing"):
                runtime.verify_installed_fixture(consumer)

    def test_provider_style_runtime_namespace_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            forbidden = consumer / ".agents/rules"
            forbidden.mkdir(parents=True)
            (forbidden / "legacy.md").write_text("legacy\n", encoding="utf-8")
            with self.assertRaisesRegex(runtime.RuntimeAcceptanceError, "forbidden provider-style"):
                runtime.verify_installed_fixture(consumer)

    def test_external_execution_contract_missing_token_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            skill = consumer / ".agents/skills/external-operation/SKILL.md"
            text = skill.read_text(encoding="utf-8")
            skill.write_text(
                text.replace("`evidence-recovery`", "`evidence-recovery-missing`"),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                runtime.RuntimeAcceptanceError,
                "incomplete runtime execution contract",
            ):
                runtime.verify_installed_fixture(consumer)

    def test_script_resource_requires_execution_contract_metadata(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            scripts = consumer / ".agents/skills/clarify-intent/scripts"
            scripts.mkdir(parents=True)
            (scripts / "helper.py").write_text("print('helper')\n", encoding="utf-8")
            with self.assertRaisesRegex(
                runtime.RuntimeAcceptanceError,
                "contains scripts without runtime execution contract",
            ):
                runtime.verify_installed_fixture(consumer)

    def test_skill_index_cannot_gain_procedure_fields(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self._fixture(Path(temp))
            consumer = fixture["consumer"]
            index_path = consumer / ".agents/release/skill-index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["skills"][0]["procedure"] = "load everything"
            index_path.write_text(
                json.dumps(index, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(runtime.RuntimeAcceptanceError, "locator metadata only"):
                runtime.verify_installed_fixture(consumer)


if __name__ == "__main__":
    unittest.main()
