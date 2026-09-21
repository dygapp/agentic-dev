from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile


REPO_ROOT = Path(__file__).resolve().parents[3]
EVALS_DIR = REPO_ROOT / "evals"
sys.path.insert(0, str(EVALS_DIR))

import run_codex_evals as runner  # noqa: E402
import run_codex_grader as grader  # noqa: E402
import run_governance_evals as governance_runner  # noqa: E402


def load_authenticated_runtime_module():
    path = REPO_ROOT / "tools/runtime-acceptance/authenticated_model_acceptance.py"
    spec = importlib.util.spec_from_file_location(
        "agentic_dev_authenticated_model_acceptance",
        path,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


authenticated_runtime = load_authenticated_runtime_module()


class EvalRunnerIntegrityTests(unittest.TestCase):
    def run_python(self, script: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), *args],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_behavior_runner_covers_current_behavior_corpus(self):
        expected_files = sorted((EVALS_DIR / "behavior").glob("*.json"))
        self.assertEqual(expected_files, runner.BEHAVIOR_FILES)

        expected_ids: list[str] = []
        for path in expected_files:
            document = json.loads(path.read_text(encoding="utf-8"))
            expected_ids.extend(case["id"] for case in document["evals"])

        actual_ids = [case["id"] for _, case in runner.behavior_cases()]
        self.assertEqual(sorted(expected_ids), sorted(actual_ids))
        self.assertEqual(len(actual_ids), len(set(actual_ids)))
        self.assertIn("B-RV-01", actual_ids)
        self.assertIn("B-HR-01", actual_ids)
        self.assertIn("B-RB-01", actual_ids)
        self.assertIn("B-AR-01", actual_ids)
        self.assertIn("B-MC-01", actual_ids)
        self.assertIn("B-EO-01", actual_ids)

    def test_runner_help_entrypoints_import_cleanly(self):
        for script in (
            EVALS_DIR / "run_codex_evals.py",
            EVALS_DIR / "run_codex_grader.py",
            EVALS_DIR / "run_governance_evals.py",
        ):
            with self.subTest(script=script.name):
                completed = self.run_python(script, "--help")
                self.assertEqual(0, completed.returncode, completed.stderr)

        self.assertTrue(callable(governance_runner.main))

    def test_authenticated_runtime_entrypoint_and_auth_classification(self):
        completed = self.run_python(
            REPO_ROOT / "tools/runtime-acceptance/authenticated_model_acceptance.py",
            "--help",
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(
            "chatgpt",
            authenticated_runtime.infer_auth_method("Logged in using ChatGPT"),
        )
        self.assertEqual(
            "codex-access-token",
            authenticated_runtime.infer_auth_method("Authenticated with access token"),
        )
        self.assertEqual(
            "api-key",
            authenticated_runtime.infer_auth_method("Logged in with API key"),
        )
        self.assertEqual(
            "workload-identity",
            authenticated_runtime.infer_auth_method("workload identity selected"),
        )

    def test_github_actions_fixture_transport_progression(self):
        script = runner.GITHUB_ACTIONS_FIXTURE / "actions_fixture.py"
        self.assertTrue(script.is_file())

        def read_json(*args: str) -> dict:
            completed = subprocess.run(
                [sys.executable, str(script), *args],
                cwd=runner.GITHUB_ACTIONS_FIXTURE,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            return json.loads(completed.stdout)

        first = read_json("read-run", "--run-id", "4242", "--poll", "1")
        self.assertEqual("abc123", first["head_sha"])
        self.assertEqual("pull_request", first["event"])
        self.assertEqual("in_progress", first["status"])

        second = read_json("read-run", "--run-id", "4242", "--poll", "2")
        self.assertEqual("completed", second["status"])
        self.assertEqual("success", second["conclusion"])

        jobs = read_json("read-jobs", "--run-id", "4242")
        self.assertEqual("success", jobs["jobs"][0]["conclusion"])
        self.assertEqual("success", jobs["jobs"][0]["steps"][0]["conclusion"])

        log = read_json("read-log", "--job-id", "9001")
        self.assertIn("abc123", log["log"])

        artifacts = read_json("read-artifacts", "--run-id", "4242")
        self.assertEqual("completion-evidence", artifacts["artifacts"][0]["name"])

    def test_authenticated_runtime_scenario_set_is_exact_gate_e_subject(self):
        self.assertEqual(8, len(authenticated_runtime.ACTIVATION_SCENARIOS))
        self.assertEqual(6, len(authenticated_runtime.BEHAVIOR_SCENARIOS))
        self.assertEqual(
            len(set(authenticated_runtime.ACTIVATION_SCENARIOS)),
            len(authenticated_runtime.ACTIVATION_SCENARIOS),
        )
        self.assertEqual(
            len(set(authenticated_runtime.BEHAVIOR_SCENARIOS)),
            len(authenticated_runtime.BEHAVIOR_SCENARIOS),
        )
        activation_ids = {case["id"] for case in runner.activation_cases()}
        behavior_ids = {case["id"] for _, case in runner.behavior_cases()}
        self.assertTrue(
            set(authenticated_runtime.ACTIVATION_SCENARIOS) <= activation_ids
        )
        self.assertTrue(
            set(authenticated_runtime.BEHAVIOR_SCENARIOS) <= behavior_ids
        )

    def test_authenticated_runtime_evidence_bundle_is_self_contained(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = root / "authenticated-model-runtime.json"
            report.write_text('{"status":"PASS"}\n', encoding="utf-8")
            bundle = root / "evidence.zip"
            payload = {
                "activation": {
                    "evidence_files": [
                        {"path": "AGENTS.md", "sha256": "not-used-here"},
                    ],
                },
                "behavior": {
                    "evidence_files": [
                        {"path": "README.md", "sha256": "not-used-here"},
                    ],
                },
            }
            digest = authenticated_runtime._write_evidence_bundle(
                bundle,
                report,
                payload,
            )
            self.assertEqual(64, len(digest))
            self.assertTrue(bundle.is_file())
            with zipfile.ZipFile(bundle, "r") as zf:
                self.assertEqual(
                    {
                        "authenticated-model-runtime.json",
                        "AGENTS.md",
                        "README.md",
                    },
                    set(zf.namelist()),
                )
                self.assertEqual(
                    (1980, 1, 1, 0, 0, 0),
                    zf.getinfo("authenticated-model-runtime.json").date_time,
                )

    def test_authenticated_runtime_collects_semantic_fail_as_evidence(self):
        original_root = authenticated_runtime.REPO_ROOT
        original_results = authenticated_runtime.RESULTS
        try:
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                results = root / "evals/results"
                behavior = results / "behavior"
                behavior.mkdir(parents=True)

                scenario = "B-TEST-FAIL"
                source_sha = "a" * 40
                (behavior / "runtime-acceptance.summary.json").write_text(
                    json.dumps(
                        {
                            "status": "FAIL",
                            "scenario_count": 1,
                            "passed": 0,
                            "failed": 1,
                        }
                    )
                    + "\n",
                    encoding="utf-8",
                )
                (behavior / f"{scenario}.run.json").write_text(
                    json.dumps(
                        {
                            "source_commit": source_sha,
                            "runtime_mode": "release-installed",
                            "release_id": "agentic-dev@test",
                            "returncode": 0,
                            "grading": "fail",
                            "codex_version": "codex-cli test",
                        }
                    )
                    + "\n",
                    encoding="utf-8",
                )
                (behavior / f"{scenario}.grade.json").write_text(
                    json.dumps(
                        {
                            "scenario_id": scenario,
                            "verdict": "FAIL",
                            "grader_codex_version": "codex-cli test",
                        }
                    )
                    + "\n",
                    encoding="utf-8",
                )
                for suffix in (
                    ".jsonl",
                    ".stderr.txt",
                    ".grader.jsonl",
                    ".grader.stderr.txt",
                ):
                    (behavior / f"{scenario}{suffix}").write_text(
                        "evidence\n",
                        encoding="utf-8",
                    )

                authenticated_runtime.REPO_ROOT = root
                authenticated_runtime.RESULTS = results
                evidence = authenticated_runtime._collect_mode_evidence(
                    "behavior",
                    (scenario,),
                    source_sha,
                )

                self.assertEqual("FAIL", evidence["status"])
                self.assertEqual([scenario], evidence["failed_scenarios"])
                self.assertEqual("FAIL", evidence["scenarios"][0]["verdict"])
                self.assertEqual(7, len(evidence["evidence_files"]))
        finally:
            authenticated_runtime.REPO_ROOT = original_root
            authenticated_runtime.RESULTS = original_results

    def test_activation_corpus_covers_new_release_skills(self):
        ids = {case["id"] for case in runner.activation_cases()}
        self.assertTrue({"A-RB-01", "A-AR-01", "A-MC-01", "A-EO-01"} <= ids)

    def test_grader_extracts_completed_agent_message(self):
        jsonl = "\n".join(
            [
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {"type": "agent_message", "text": "first"},
                    }
                ),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {"type": "agent_message", "text": "final"},
                    }
                ),
                json.dumps({"type": "turn.completed"}),
            ]
        )
        self.assertEqual("final", grader.extract_last_agent_message(jsonl))

    def test_grader_extracts_observable_runtime_trace(self):
        jsonl = "\n".join(
            [
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {
                            "type": "agent_message",
                            "text": "先读取 AGENTS.md 和 unit.md。",
                        },
                    }
                ),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {
                            "type": "command_execution",
                            "command": "sed -n '1,120p' AGENTS.md unit.md greeting.py tests/test_greeting.py",
                            "aggregated_output": "fixture content",
                            "exit_code": 0,
                            "status": "completed",
                        },
                    }
                ),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {
                            "type": "file_change",
                            "changes": [{"path": "greeting.py", "kind": "update"}],
                            "status": "completed",
                        },
                    }
                ),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {"type": "reasoning", "text": "private reasoning"},
                    }
                ),
                json.dumps({"type": "turn.completed"}),
            ]
        )
        trace = grader.extract_observable_runtime_trace(jsonl)
        self.assertIn("AGENTS.md", trace)
        self.assertIn("unit.md", trace)
        self.assertIn("greeting.py", trace)
        self.assertIn("file_change", trace)
        self.assertNotIn("private reasoning", trace)

    def test_grader_parses_plain_and_fenced_json(self):
        payload = {
            "scenario_id": "B-TEST-JSON",
            "verdict": "PASS",
            "assertions": [],
            "summary": "ok",
        }
        raw = json.dumps(payload)
        self.assertEqual(payload, grader.parse_json_object(raw))
        self.assertEqual(
            payload,
            grader.parse_json_object("```json\n" + raw + "\n```"),
        )

    def test_grader_requires_turn_completion_and_agent_message(self):
        with self.assertRaises(grader.GradeError):
            grader.extract_last_agent_message(
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {"type": "agent_message", "text": "partial"},
                    }
                )
            )
        with self.assertRaises(grader.GradeError):
            grader.extract_last_agent_message(json.dumps({"type": "turn.completed"}))

    def test_grader_verdict_must_match_all_assertions(self):
        scenario = {
            "id": "B-TEST-01",
            "assertions": ["one", "two"],
        }
        passing = {
            "scenario_id": "B-TEST-01",
            "verdict": "PASS",
            "assertions": [
                {"index": 1, "passed": True, "evidence": "e1"},
                {"index": 2, "passed": True, "evidence": "e2"},
            ],
        }
        self.assertTrue(grader.validate_grade(scenario, passing))

        inconsistent = {
            "scenario_id": "B-TEST-01",
            "verdict": "PASS",
            "assertions": [
                {"index": 1, "passed": True, "evidence": "e1"},
                {"index": 2, "passed": False, "evidence": "gap"},
            ],
        }
        with self.assertRaises(grader.GradeError):
            grader.validate_grade(scenario, inconsistent)

    def test_release_runtime_materializes_installed_release_not_source_tree(self):
        source_commit = runner.current_source_commit()
        release_context, package_root, release_result = runner.build_release_package(
            source_commit
        )
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                workspace = Path(temp_dir)
                runner.install_release_runtime(workspace, package_root)
                self.assertTrue(
                    (workspace / ".agents/release/manifest.json").is_file()
                )
                self.assertEqual(
                    15,
                    len(list((workspace / ".agents/skills").glob("*/SKILL.md"))),
                )
                self.assertFalse((workspace / "docs/rules").exists())
                self.assertFalse((workspace / "tools/rule-discovery").exists())
                self.assertIn(source_commit[:12], release_result["release_id"])
        finally:
            release_context.cleanup()

    def test_release_runtime_is_not_valid_for_provider_discovery_mode(self):
        completed = self.run_python(
            EVALS_DIR / "run_codex_evals.py",
            "--discovery",
            "--release-runtime",
            "--codex-bin",
            "false",
        )
        self.assertEqual(2, completed.returncode)
        self.assertIn("--release-runtime is not valid with --discovery", completed.stderr)
        self.assertNotIn("Codex CLI version check failed", completed.stderr)

    def test_governance_context_paths_resolve_current_repository_files(self):
        referenced: set[str] = set()
        for path in governance_runner.GOVERNANCE_FILES:
            document = json.loads(path.read_text(encoding="utf-8"))
            for relative in document["context_paths"]:
                referenced.add(relative)
                self.assertTrue(
                    (REPO_ROOT / relative).exists(),
                    f"{path.name}: missing context path {relative}",
                )

        self.assertNotIn("docs/guides/terminology-guidelines.md", referenced)
        self.assertNotIn("docs/architecture/technology-profile-contract.md", referenced)
        self.assertNotIn("docs/architecture/skill-contracts.md", referenced)
        self.assertNotIn("docs/method/ai-development-method.md", referenced)

    def test_mode_mismatch_fails_before_codex_invocation(self):
        completed = self.run_python(
            EVALS_DIR / "run_codex_evals.py",
            "--behavior",
            "--scenario",
            "D-V4-GEN-01",
            "--codex-bin",
            "false",
        )
        self.assertEqual(2, completed.returncode)
        self.assertIn("not available in the selected mode", completed.stderr)
        self.assertNotIn("Codex CLI version check failed", completed.stderr)

    def test_default_mode_rejects_discovery_only_scenario(self):
        completed = self.run_python(
            EVALS_DIR / "run_codex_evals.py",
            "--scenario",
            "D-V4-GEN-01",
            "--codex-bin",
            "false",
        )
        self.assertEqual(2, completed.returncode)
        self.assertIn("not available in the selected mode", completed.stderr)


if __name__ == "__main__":
    unittest.main()
