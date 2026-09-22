from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
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

    def test_model_collaboration_activation_stays_read_only_and_defers_enablement(self):
        case = next(item for item in runner.activation_cases() if item["id"] == "A-MC-01")
        self.assertIn("只验证能力选择与边界", case["query"])
        self.assertIn("不修改任何配置或仓库文件", case["query"])
        self.assertIn("Behavior Eval", case["reason"])
        self.assertNotIn("workspace_write", case)

    def test_model_collaboration_behavior_uses_bounded_given_runtime_evidence(self):
        path = EVALS_DIR / "behavior/activate-model-collaboration.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        case = next(item for item in document["evals"] if item["id"] == "B-MC-01")
        self.assertIn("作为本场景当前 runtime evidence", case["prompt"])
        self.assertIn("不要再启动额外 child", case["prompt"])
        self.assertIn("不要修改任何配置或仓库文件", case["prompt"])

    def test_bounded_jsonl_process_reaps_lingering_process_after_turn_completed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            stdout_path = root / "stdout.jsonl"
            stderr_path = root / "stderr.txt"
            command = [
                sys.executable,
                "-c",
                (
                    "import json,time; "
                    "print(json.dumps({'type':'turn.completed'}), flush=True); "
                    "time.sleep(30)"
                ),
            ]
            started = time.monotonic()
            result = runner.run_bounded_jsonl_process(
                command=command,
                cwd=root,
                env=dict(),
                stdout_path=stdout_path,
                stderr_path=stderr_path,
                timeout_seconds=5,
                completion_grace_seconds=0.1,
            )
            elapsed = time.monotonic() - started

            self.assertLess(elapsed, 3)
            self.assertEqual(0, result["returncode"])
            self.assertTrue(result["completion_event_observed"])
            self.assertTrue(result["terminated_after_completion"])
            self.assertFalse(result["timed_out"])
            self.assertNotEqual(0, result["process_returncode"])

    def test_bounded_jsonl_process_times_out_without_turn_completed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            stdout_path = root / "stdout.jsonl"
            stderr_path = root / "stderr.txt"
            command = [sys.executable, "-c", "import time; time.sleep(30)"]
            started = time.monotonic()
            result = runner.run_bounded_jsonl_process(
                command=command,
                cwd=root,
                env=dict(),
                stdout_path=stdout_path,
                stderr_path=stderr_path,
                timeout_seconds=0.2,
                inactivity_timeout_seconds=5,
                completion_grace_seconds=0.1,
            )
            elapsed = time.monotonic() - started

            self.assertLess(elapsed, 3)
            self.assertEqual(124, result["returncode"])
            self.assertFalse(result["completion_event_observed"])
            self.assertFalse(result["terminated_after_completion"])
            self.assertTrue(result["timed_out"])
            self.assertNotEqual(0, result["process_returncode"])

    def test_bounded_jsonl_process_times_out_on_no_observable_progress(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            stdout_path = root / "stdout.jsonl"
            stderr_path = root / "stderr.txt"
            command = [
                sys.executable,
                "-c",
                (
                    "import json,time; "
                    "print(json.dumps({'type':'item.started'}), flush=True); "
                    "time.sleep(30)"
                ),
            ]
            started = time.monotonic()
            result = runner.run_bounded_jsonl_process(
                command=command,
                cwd=root,
                env=dict(),
                stdout_path=stdout_path,
                stderr_path=stderr_path,
                timeout_seconds=5,
                inactivity_timeout_seconds=0.2,
                completion_grace_seconds=0.1,
            )
            elapsed = time.monotonic() - started

            self.assertLess(elapsed, 3)
            self.assertEqual(124, result["returncode"])
            self.assertTrue(result["timed_out"])
            self.assertEqual("inactivity", result["timeout_reason"])
            self.assertFalse(result["completion_event_observed"])

    @unittest.skipUnless(os.name == "posix", "process-group cancellation test is POSIX-specific")
    def test_parent_sigterm_reaps_runtime_process_group(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            child_pid_path = root / "child.pid"
            launcher = root / "launcher.py"
            launcher.write_text(
                "\n".join(
                    [
                        "from pathlib import Path",
                        "import os",
                        "import sys",
                        f"sys.path.insert(0, {str(EVALS_DIR)!r})",
                        "import run_codex_evals as runner",
                        f"root = Path({str(root)!r})",
                        "runner.run_bounded_jsonl_process(",
                        "    command=[sys.executable, '-c', "
                        + repr(
                            "from pathlib import Path; import os,time; "
                            f"Path({str(child_pid_path)!r}).write_text(str(os.getpid())); "
                            "time.sleep(30)"
                        )
                        + "],",
                        "    cwd=root,",
                        "    env=os.environ.copy(),",
                        "    stdout_path=root / 'stdout.jsonl',",
                        "    stderr_path=root / 'stderr.txt',",
                        "    timeout_seconds=20,",
                        "    inactivity_timeout_seconds=20,",
                        ")",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            parent = subprocess.Popen([sys.executable, str(launcher)], cwd=root)
            deadline = time.monotonic() + 3
            while not child_pid_path.exists() and time.monotonic() < deadline:
                time.sleep(0.05)
            self.assertTrue(child_pid_path.exists(), "runtime child did not start")
            child_pid = int(child_pid_path.read_text(encoding="utf-8"))

            parent.terminate()
            parent.wait(timeout=3)
            deadline = time.monotonic() + 3
            while time.monotonic() < deadline:
                try:
                    os.kill(child_pid, 0)
                except ProcessLookupError:
                    break
                time.sleep(0.05)
            else:
                self.fail(f"runtime child {child_pid} survived parent cancellation")

    def test_new_runtime_attempt_clears_stale_scenario_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            result_dir = Path(temp)
            scenario = "A-STALE-01"
            for suffix in (
                ".run.json",
                ".grade.json",
                ".grader.jsonl",
                ".grader.stderr.txt",
            ):
                (result_dir / f"{scenario}{suffix}").write_text("stale\n", encoding="utf-8")
            summary = result_dir / "runtime-acceptance.summary.json"
            summary.write_text("stale\n", encoding="utf-8")

            runner._clear_stale_scenario_evidence(result_dir, scenario)

            self.assertFalse(summary.exists())
            self.assertFalse(any(result_dir.iterdir()))

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
                            "scenario_id": scenario,
                            "source_commit": source_sha,
                            "runtime_mode": "release-installed",
                            "release_id": "agentic-dev@test",
                            "returncode": 0,
                            "grading": "fail",
                            "codex_version": "codex-cli test",
                            "grader_codex_version": "codex-cli test",
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
                            "runtime_mode": "release-installed",
                            "release_id": "agentic-dev@test",
                            "runtime_codex_version": "codex-cli test",
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
