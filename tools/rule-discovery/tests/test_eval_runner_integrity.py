from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
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


def load_runtime_acceptance_module():
    path = REPO_ROOT / "tools/runtime-acceptance/runtime_acceptance.py"
    spec = importlib.util.spec_from_file_location(
        "agentic_dev_runtime_acceptance_for_evals",
        path,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


runtime_acceptance = load_runtime_acceptance_module()


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

    def test_requirement_baseline_behavior_eval_scopes_ready_preconditions(self):
        path = EVALS_DIR / "behavior/establish-requirement-baseline.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        case = next(item for item in document["evals"] if item["id"] == "B-RB-01")

        prompt = case["prompt"]
        self.assertIn("其它 project-level Requirement Convergence 条件均已满足", prompt)
        self.assertIn("Capability Human Review", prompt)
        self.assertIn("mandatory independent semantic review", prompt)
        self.assertIn("唯一待收敛内容", prompt)
        self.assertIn(
            "不把场景已明确满足的其它 project-level Ready / review 前提重新制造为 blocker",
            case["assertions"][3],
        )

    def test_isolated_skill_copy_writes_minimal_provenance_locator(self):
        original_context = dict(runner.RUN_CONTEXT)
        try:
            runner.RUN_CONTEXT.update(
                {
                    "source_commit": "a" * 40,
                    "skill_set_sha256": "b" * 64,
                }
            )
            with tempfile.TemporaryDirectory() as temp:
                workspace = Path(temp)
                runner.populate_isolated_skill_copies(workspace)
                locator = (workspace / ".agents/README.md").read_text(
                    encoding="utf-8"
                )
                self.assertIn("source_commit: " + "a" * 40, locator)
                self.assertIn("skill_set_sha256: " + "b" * 64, locator)
                self.assertIn("runtime_mode: canonical-skill-copy", locator)
                self.assertNotIn("docs/rules", locator)
        finally:
            runner.RUN_CONTEXT.clear()
            runner.RUN_CONTEXT.update(original_context)

    def test_behavior_git_baseline_is_clean_and_has_head(self):
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            (workspace / "AGENTS.md").write_text("# fixture\n", encoding="utf-8")
            (workspace / "unit.md").write_text("unit\n", encoding="utf-8")
            runner.initialize_local_git_baseline(workspace)
            status = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=workspace,
                text=True,
                capture_output=True,
                check=False,
            )
            head = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=workspace,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(0, status.returncode, status.stderr)
            self.assertEqual("", status.stdout.strip())
            self.assertEqual(0, head.returncode, head.stderr)
            self.assertEqual(40, len(head.stdout.strip()))

    def test_model_collaboration_behavior_uses_supplied_observed_capability(self):
        document = json.loads(
            (EVALS_DIR / "behavior/activate-model-collaboration.json").read_text(
                encoding="utf-8"
            )
        )
        case = next(item for item in document["evals"] if item["id"] == "B-MC-01")
        self.assertIn("当前 observed capability evidence", case["prompt"])
        self.assertIn("不要在本场景中再次调用", case["prompt"])
        self.assertIn(".agents/README.md", case["prompt"])
        self.assertIn("B-MC-01", runner.WORKSPACE_WRITE_BEHAVIOR_SCENARIOS)
        self.assertIn("B-EU-01", runner.WORKSPACE_WRITE_BEHAVIOR_SCENARIOS)
        self.assertIn("B-GA-01", runner.WORKSPACE_WRITE_BEHAVIOR_SCENARIOS)

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
        with tempfile.TemporaryDirectory() as temp:
            fixture = Path(temp)
            for name in ("actions_fixture.py", "ci-config.txt"):
                source = runner.GITHUB_ACTIONS_FIXTURE / name
                (fixture / name).write_bytes(source.read_bytes())

            script = fixture / "actions_fixture.py"

            def run_fixture(*args: str) -> subprocess.CompletedProcess[str]:
                return subprocess.run(
                    [sys.executable, str(script), *args],
                    cwd=fixture,
                    text=True,
                    capture_output=True,
                    check=False,
                )

            def read_json(*args: str) -> dict:
                completed = run_fixture(*args)
                self.assertEqual(0, completed.returncode, completed.stderr)
                return json.loads(completed.stdout)

            first = read_json("read-run", "--run-id", "4242", "--poll", "1")
            self.assertEqual("abc123", first["head_sha"])
            self.assertEqual("pull_request", first["event"])
            self.assertEqual("in_progress", first["status"])

            failed = read_json("read-run", "--run-id", "4242", "--poll", "2")
            self.assertEqual("completed", failed["status"])
            self.assertEqual("failure", failed["conclusion"])

            jobs = read_json("read-jobs", "--run-id", "4242")
            self.assertEqual("failure", jobs["jobs"][0]["conclusion"])
            self.assertEqual("failure", jobs["jobs"][0]["steps"][0]["conclusion"])

            log = read_json("read-log", "--job-id", "9001")
            self.assertIn("cache-version=v2", log["log"])

            premature = run_fixture("register-fix", "--base-head", "abc123")
            self.assertNotEqual(0, premature.returncode)

            (fixture / "ci-config.txt").write_text(
                "cache-version=v2\n",
                encoding="utf-8",
            )
            fix = read_json("register-fix", "--base-head", "abc123")
            self.assertEqual("def456", fix["new_head_sha"])

            rerun = read_json("dispatch-rerun", "--head", "def456")
            self.assertEqual(4243, rerun["run_id"])

            repaired_running = read_json(
                "read-run", "--run-id", "4243", "--poll", "1"
            )
            self.assertEqual("def456", repaired_running["head_sha"])
            self.assertEqual("in_progress", repaired_running["status"])

            repaired = read_json("read-run", "--run-id", "4243", "--poll", "2")
            self.assertEqual("completed", repaired["status"])
            self.assertEqual("success", repaired["conclusion"])

            repaired_jobs = read_json("read-jobs", "--run-id", "4243")
            self.assertEqual("success", repaired_jobs["jobs"][0]["conclusion"])

            repaired_log = read_json("read-log", "--job-id", "9002")
            self.assertIn("def456", repaired_log["log"])

            artifacts = read_json("read-artifacts", "--run-id", "4243")
            self.assertEqual(
                "completion-evidence",
                artifacts["artifacts"][0]["name"],
            )

    def test_authenticated_runtime_scenario_set_is_bounded_representative_subject(self):
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
                "deterministic_runtime": {
                    "report": "evals/README.md",
                },
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
                        "evals/README.md",
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
                            "schema_version": 2,
                            "evidence_kind": "agentic-dev-codex-runtime",
                            "source_commit": source_sha,
                            "runtime_mode": "canonical-skill-copy",
                            "skill_set_sha256": "b" * 64,
                            "timed_out": False,
                            "process_exit_timed_out": False,
                            "semantic_completed": True,
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
                            "source_commit": source_sha,
                            "runtime_mode": "canonical-skill-copy",
                            "skill_set_sha256": "b" * 64,
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
                self.assertEqual("b" * 64, evidence["scenarios"][0]["skill_set_sha256"])
                self.assertEqual(7, len(evidence["evidence_files"]))
        finally:
            authenticated_runtime.REPO_ROOT = original_root
            authenticated_runtime.RESULTS = original_results

    def test_activation_corpus_covers_current_canonical_skills(self):
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

    def test_canonical_skill_copy_materializes_only_skill_packages(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            workspace = Path(temp_dir)
            runner.populate_isolated_skill_copies(workspace)
            self.assertEqual(
                15,
                len(list((workspace / ".agents/skills").glob("*/SKILL.md"))),
            )
            self.assertFalse((workspace / ".agents/release").exists())
            self.assertFalse((workspace / "docs/rules").exists())
            self.assertFalse((workspace / "tools/rule-discovery").exists())
            self.assertEqual(64, len(runner.canonical_skill_set_sha256()))

    def test_runtime_and_eval_runner_share_skill_set_identity(self):
        self.assertEqual(
            runtime_acceptance.canonical_skill_set_sha256(REPO_ROOT),
            runner.canonical_skill_set_sha256(),
        )

    def test_release_runtime_flag_is_removed(self):
        completed = self.run_python(
            EVALS_DIR / "run_codex_evals.py",
            "--behavior",
            "--release-runtime",
        )
        self.assertEqual(2, completed.returncode)
        self.assertIn("unrecognized arguments: --release-runtime", completed.stderr)

    def test_stale_scenario_results_are_removed_before_rerun(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            scenario = "B-STALE"
            for suffix in (
                ".jsonl", ".stderr.txt", ".run.json", ".grade.json",
                ".grader.jsonl", ".grader.stderr.txt",
            ):
                (root / f"{scenario}{suffix}").write_text("stale\n", encoding="utf-8")
            runner._clear_stale_scenario_results(root, scenario)
            self.assertEqual([], list(root.iterdir()))

    def test_runtime_timeout_is_bounded_and_recorded(self):
        original_results = runner.RESULTS
        original_context = dict(runner.RUN_CONTEXT)
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                root = Path(temp_dir)
                runner.RESULTS = root / "results"
                runner.RUN_CONTEXT.update(
                    {
                        "source_commit": "a" * 40,
                        "codex_version": "codex-cli test",
                        "skill_set_sha256": "b" * 64,
                        "timeout_seconds": 1,
                    }
                )
                timeout = subprocess.TimeoutExpired(
                    cmd=["codex"], timeout=1, output="partial", stderr="waiting"
                )
                with mock.patch.object(runner.subprocess, "run", side_effect=timeout):
                    code = runner.run_codex(
                        codex_bin="codex",
                        scenario_id="B-TIMEOUT",
                        prompt="$clarify-intent test",
                        result_group="behavior",
                        cwd=root,
                        skip_git_repo_check=True,
                    )
                self.assertEqual(124, code)
                metadata = json.loads(
                    (runner.RESULTS / "behavior/B-TIMEOUT.run.json").read_text(
                        encoding="utf-8"
                    )
                )
                self.assertTrue(metadata["timed_out"])
                self.assertTrue(metadata["process_exit_timed_out"])
                self.assertFalse(metadata["semantic_completed"])
                self.assertEqual(1, metadata["timeout_seconds"])
                self.assertEqual("canonical-skill-copy", metadata["runtime_mode"])
        finally:
            runner.RESULTS = original_results
            runner.RUN_CONTEXT.clear()
            runner.RUN_CONTEXT.update(original_context)

    def test_turn_completed_survives_process_exit_timeout(self):
        original_results = runner.RESULTS
        original_context = dict(runner.RUN_CONTEXT)
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                root = Path(temp_dir)
                runner.RESULTS = root / "results"
                runner.RUN_CONTEXT.update(
                    {
                        "source_commit": "a" * 40,
                        "codex_version": "codex-cli test",
                        "skill_set_sha256": "b" * 64,
                        "timeout_seconds": 1,
                    }
                )
                output = (
                    '{"type":"item.completed","item":{"type":"agent_message",'
                    '"text":"done"}}\n'
                    '{"type":"turn.completed","usage":{}}\n'
                )
                timeout = subprocess.TimeoutExpired(
                    cmd=["codex"], timeout=1, output=output, stderr="waiting"
                )
                with mock.patch.object(runner.subprocess, "run", side_effect=timeout):
                    code = runner.run_codex(
                        codex_bin="codex",
                        scenario_id="B-COMPLETED-EXIT-TIMEOUT",
                        prompt="$clarify-intent test",
                        result_group="behavior",
                        cwd=root,
                        skip_git_repo_check=True,
                    )
                self.assertEqual(0, code)
                metadata = json.loads(
                    (
                        runner.RESULTS
                        / "behavior/B-COMPLETED-EXIT-TIMEOUT.run.json"
                    ).read_text(encoding="utf-8")
                )
                self.assertFalse(metadata["timed_out"])
                self.assertTrue(metadata["process_exit_timed_out"])
                self.assertTrue(metadata["semantic_completed"])
        finally:
            runner.RESULTS = original_results
            runner.RUN_CONTEXT.clear()
            runner.RUN_CONTEXT.update(original_context)

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
