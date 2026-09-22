from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
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
    sys.modules[name] = module
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

    def _build(
        self,
        output: Path,
        version: str = "0.0.0-test",
        runtime_evidence_locator: str | None = None,
        automated_runtime_evidence: Path | None = None,
        authenticated_runtime_evidence: Path | None = None,
        authenticated_runtime_evidence_bundle: Path | None = None,
        verification_evidence_locator: str | None = None,
        release_completion_evidence: Path | None = None,
    ) -> tuple[Path, dict]:
        result = release_build.build_release(
            REPO_ROOT,
            output,
            self.source_sha,
            version,
            "test://release-build",
            runtime_evidence_locator,
            automated_runtime_evidence,
            authenticated_runtime_evidence,
            authenticated_runtime_evidence_bundle,
            verification_evidence_locator,
            release_completion_evidence,
        )
        archive = output / result["archive"]
        return archive, result

    def _write_runtime_evidence(
        self,
        root: Path,
        *,
        source_sha: str | None = None,
        authenticated_status: str = "PASS",
    ) -> tuple[Path, Path, Path]:
        root.mkdir(parents=True, exist_ok=True)
        subject = source_sha or self.source_sha
        automated = root / "automated-runtime.json"
        authenticated = root / "authenticated-runtime.json"
        authenticated_bundle = root / "authenticated-runtime-evidence.zip"
        automated.write_text(
            json.dumps(
                {
                    "status": "ok",
                    "source_sha": subject,
                    "release_build": {"status": "ok", "source_sha": subject},
                    "installed_runtime": {
                        "status": "ok",
                        "source_sha": subject,
                        "provider_source_paths_present": False,
                        "chatgpt_compatibility_path": [
                            "AGENTS.md",
                            ".agents/release/skill-index.json",
                            ".agents/skills/<name>/SKILL.md",
                        ],
                    },
                    "upstream_negative_control": {
                        "status": "ok",
                        "native_discovery_status": "ok",
                    },
                    "codex_native_discovery": {"status": "ok"},
                },
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

        release_id = f"agentic-dev@0.0.0-eval.{subject[:12]}+{subject[:12]}"
        evidence_payloads: dict[str, bytes] = {}
        mode_payloads: dict[str, dict] = {}
        for mode, scenarios in (
            ("activation", release_build.AUTHENTICATED_RUNTIME_ACTIVATION_SCENARIOS),
            ("behavior", release_build.AUTHENTICATED_RUNTIME_BEHAVIOR_SCENARIOS),
        ):
            root_path = f"evals/results/{mode}"
            summary_path = f"{root_path}/runtime-acceptance.summary.json"
            summary_bytes = (
                json.dumps(
                    {"status": "PASS", "scenario_count": len(scenarios)},
                    sort_keys=True,
                )
                + "\n"
            ).encode("utf-8")
            evidence_payloads[summary_path] = summary_bytes
            evidence_files = [
                {
                    "path": summary_path,
                    "sha256": hashlib.sha256(summary_bytes).hexdigest(),
                }
            ]
            records = []
            for scenario in scenarios:
                run_path = f"{root_path}/{scenario}.run.json"
                grade_path = f"{root_path}/{scenario}.grade.json"
                scenario_payloads = {
                    run_path: (
                        json.dumps(
                            {
                                "scenario_id": scenario,
                                "source_commit": subject,
                                "codex_version": "codex-test",
                                "runtime_mode": "release-installed",
                                "release_id": release_id,
                                "returncode": 0,
                                "grading": "pass",
                                "grader_codex_version": "codex-test",
                            },
                            sort_keys=True,
                        )
                        + "\n"
                    ).encode("utf-8"),
                    grade_path: (
                        json.dumps(
                            {
                                "scenario_id": scenario,
                                "source_commit": subject,
                                "runtime_mode": "release-installed",
                                "release_id": release_id,
                                "runtime_codex_version": "codex-test",
                                "grader_codex_version": "codex-test",
                                "verdict": "PASS",
                            },
                            sort_keys=True,
                        )
                        + "\n"
                    ).encode("utf-8"),
                    f"{root_path}/{scenario}.jsonl": b'{"type":"turn.completed"}\n',
                    f"{root_path}/{scenario}.stderr.txt": b"",
                    f"{root_path}/{scenario}.grader.jsonl": b"{}\n",
                    f"{root_path}/{scenario}.grader.stderr.txt": b"",
                }
                evidence_payloads.update(scenario_payloads)
                evidence_files.extend(
                    {
                        "path": path,
                        "sha256": hashlib.sha256(payload).hexdigest(),
                    }
                    for path, payload in scenario_payloads.items()
                )
                records.append(
                    {
                        "scenario_id": scenario,
                        "release_id": release_id,
                        "runtime_codex_version": "codex-test",
                        "grader_codex_version": "codex-test",
                        "verdict": "PASS",
                    }
                )
            mode_payloads[mode] = {
                "status": "PASS",
                "summary": {"status": "PASS", "scenario_count": len(scenarios)},
                "scenarios": records,
                "failed_scenarios": [],
                "evidence_files": sorted(evidence_files, key=lambda item: item["path"]),
            }

        authenticated_payload = {
            "evidence_kind": release_build.AUTHENTICATED_RUNTIME_EVIDENCE_KIND,
            "schema_version": release_build.AUTHENTICATED_RUNTIME_EVIDENCE_SCHEMA_VERSION,
            "status": authenticated_status,
            "source_sha": subject,
            "release_id": release_id,
            "codex_version": "codex-test",
            "authentication_method": "chatgpt",
            "authentication_evidence": "codex login status",
            "scenario_count": (
                len(release_build.AUTHENTICATED_RUNTIME_ACTIVATION_SCENARIOS)
                + len(release_build.AUTHENTICATED_RUNTIME_BEHAVIOR_SCENARIOS)
            ),
            "failed_scenarios": [] if authenticated_status == "PASS" else ["B-EU-01"],
            "execution": {
                "activation": {"runtime_returncode": 0, "grader_returncode": 0},
                "behavior": {"runtime_returncode": 0, "grader_returncode": 0},
            },
            **mode_payloads,
        }
        authenticated.write_text(
            json.dumps(authenticated_payload, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        with zipfile.ZipFile(authenticated_bundle, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("authenticated-model-runtime.json", authenticated.read_bytes())
            for path, payload in sorted(evidence_payloads.items()):
                zf.writestr(path, payload)
        return automated, authenticated, authenticated_bundle

    def _write_release_completion_evidence(
        self,
        root: Path,
        *,
        version: str = "0.0.0-test",
        source_sha: str | None = None,
        status: str = "PASS",
        acceptance_results: list[dict[str, object]] | None = None,
        finding_counts: dict[str, int] | None = None,
        release_id: str | None = None,
        claim_id: str = "DR-AC-37",
    ) -> Path:
        root.mkdir(parents=True, exist_ok=True)
        subject = source_sha or self.source_sha
        evidence = root / "release-completion.json"
        evidence.write_text(
            json.dumps(
                {
                    "evidence_kind": release_build.RELEASE_COMPLETION_EVIDENCE_KIND,
                    "schema_version": release_build.RELEASE_COMPLETION_EVIDENCE_SCHEMA_VERSION,
                    "status": status,
                    "source_sha": subject,
                    "release_id": release_id or f"agentic-dev@{version}+{subject[:12]}",
                    "claim_id": claim_id,
                    "acceptance_results": acceptance_results
                    if acceptance_results is not None
                    else [
                        {
                            "id": f"DR-AC-{index:02d}",
                            "status": "PASS",
                            "evidence_locators": [f"test://gate-g/DR-AC-{index:02d}"],
                        }
                        for index in range(1, 37)
                    ],
                    "finding_counts": finding_counts
                    if finding_counts is not None
                    else {"blocking": 0, "medium": 0, "unverified": 0},
                },
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        return evidence

    def _rewrite_authenticated_bundle_json(
        self,
        authenticated: Path,
        authenticated_bundle: Path,
        evidence_path: str,
        updates: dict[str, str],
    ) -> None:
        with zipfile.ZipFile(authenticated_bundle, "r") as zf:
            entries = {name: zf.read(name) for name in zf.namelist()}

        payload = json.loads(entries[evidence_path].decode("utf-8"))
        payload.update(updates)
        evidence_bytes = (json.dumps(payload, sort_keys=True) + "\n").encode("utf-8")
        entries[evidence_path] = evidence_bytes

        report = json.loads(authenticated.read_text(encoding="utf-8"))
        mode = Path(evidence_path).parts[2]
        for item in report[mode]["evidence_files"]:
            if item["path"] == evidence_path:
                item["sha256"] = hashlib.sha256(evidence_bytes).hexdigest()
                break
        else:
            self.fail(f"evidence path missing from authenticated report: {evidence_path}")

        report_bytes = (json.dumps(report, sort_keys=True) + "\n").encode("utf-8")
        authenticated.write_bytes(report_bytes)
        entries["authenticated-model-runtime.json"] = report_bytes
        with zipfile.ZipFile(
            authenticated_bundle,
            "w",
            compression=zipfile.ZIP_DEFLATED,
        ) as zf:
            for path, content in sorted(entries.items()):
                zf.writestr(path, content)

    def test_source_sha_verification_requires_git_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "requires a Git checkout"):
                release_build._verify_source_sha(Path(temp), self.source_sha)

    def test_source_sha_verification_rejects_mismatched_head(self):
        wrong = "0" * 40 if self.source_sha != "0" * 40 else "1" * 40
        with self.assertRaisesRegex(ValueError, "source SHA mismatch"):
            release_build._verify_source_sha(REPO_ROOT, wrong)

    def test_source_sha_verification_rejects_dirty_checkout(self):
        sentinel = REPO_ROOT / "AGENTIC_DEV_RELEASE_DIRTY_SENTINEL"
        sentinel.write_text("dirty\n", encoding="utf-8")
        try:
            with self.assertRaisesRegex(ValueError, "clean Git checkout"):
                release_build._verify_source_sha(REPO_ROOT, self.source_sha)
        finally:
            sentinel.unlink(missing_ok=True)

    def test_release_completion_contract_is_derived_from_current_project_authority(self):
        contract = release_build._load_release_completion_contract(REPO_ROOT)
        self.assertEqual(contract["claim_id"], "DR-AC-37")
        self.assertEqual(len(contract["acceptance_ids"]), 36)
        self.assertEqual(contract["acceptance_ids"][0], "DR-AC-01")
        self.assertEqual(contract["acceptance_ids"][-1], "DR-AC-36")
        self.assertEqual(
            contract["authority_path"],
            "docs/project/distribution-rebuild-specification.md",
        )

    def test_generated_reference_namespace_collision_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skill"
            reserved = destination / "references/release-inputs"
            reserved.mkdir(parents=True)
            (reserved / "local.md").write_text("local\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "generated reference namespace collision"):
                release_build._prepare_generated_reference_root(destination)

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
            self.assertEqual(result["software_release_input_count"], 28)
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
            self.assertEqual(manifest["build_evidence_locator"], "test://release-build")
            self.assertIsNone(manifest["runtime_evidence_locator"])
            self.assertIsNone(manifest["runtime_evidence"])
            self.assertIsNone(manifest["verification_evidence_locator"])
            self.assertIsNone(manifest["verification_evidence"])
            self.assertEqual(
                manifest["compatibility"]["codex_repository_skills"]["status"],
                "candidate-unverified-until-runtime-acceptance",
            )
            self.assertEqual(
                manifest["compatibility"]["chatgpt_github_connector"]["status"],
                "candidate-unverified-until-runtime-acceptance",
            )

    def test_all_release_skills_include_execution_continuity_rule(self):
        continuity_rule = "rule:execution-continuity-and-stop-condition"
        release_skills = [
            skill
            for skill in release_build._collect_skills(REPO_ROOT)
            if skill.distribution == "release-direct"
        ]
        self.assertTrue(release_skills)
        for skill in release_skills:
            with self.subTest(skill=skill.name):
                self.assertIn(continuity_rule, skill.release_inputs)

    def test_runtime_evidence_promotes_release_compatibility(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            automated, authenticated, authenticated_bundle = self._write_runtime_evidence(
                root / "evidence"
            )
            archive, result = self._build(
                root / "release",
                runtime_evidence_locator="test://runtime-acceptance",
                automated_runtime_evidence=automated,
                authenticated_runtime_evidence=authenticated,
                authenticated_runtime_evidence_bundle=authenticated_bundle,
            )
            with zipfile.ZipFile(archive, "r") as zf:
                manifest = json.loads(zf.read("manifest.json").decode("utf-8"))

            self.assertEqual(result["build_evidence_locator"], "test://release-build")
            self.assertEqual(result["runtime_evidence_locator"], "test://runtime-acceptance")
            self.assertIsNone(result["verification_evidence_locator"])
            self.assertIsNone(result["verification_evidence"])
            self.assertEqual(manifest["build_evidence_locator"], "test://release-build")
            self.assertEqual(manifest["runtime_evidence_locator"], "test://runtime-acceptance")
            self.assertEqual(
                manifest["runtime_evidence"]["automated_report_sha256"],
                hashlib.sha256(automated.read_bytes()).hexdigest(),
            )
            self.assertEqual(
                manifest["runtime_evidence"]["authenticated_report_sha256"],
                hashlib.sha256(authenticated.read_bytes()).hexdigest(),
            )
            self.assertEqual(
                manifest["runtime_evidence"]["authenticated_evidence_bundle_sha256"],
                hashlib.sha256(authenticated_bundle.read_bytes()).hexdigest(),
            )
            self.assertIsNone(manifest["verification_evidence_locator"])
            self.assertIsNone(manifest["verification_evidence"])
            self.assertEqual(
                manifest["compatibility"]["codex_repository_skills"]["status"],
                "verified",
            )
            self.assertEqual(
                manifest["compatibility"]["chatgpt_github_connector"]["status"],
                "verified",
            )

    def test_release_completion_evidence_is_independent_from_build_and_runtime_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            automated, authenticated, authenticated_bundle = self._write_runtime_evidence(
                root / "runtime-evidence"
            )
            completion = self._write_release_completion_evidence(root / "completion-evidence")
            archive, result = self._build(
                root / "release",
                runtime_evidence_locator="test://runtime-acceptance",
                automated_runtime_evidence=automated,
                authenticated_runtime_evidence=authenticated,
                authenticated_runtime_evidence_bundle=authenticated_bundle,
                verification_evidence_locator="test://gate-g-final-review",
                release_completion_evidence=completion,
            )
            with zipfile.ZipFile(archive, "r") as zf:
                manifest = json.loads(zf.read("manifest.json").decode("utf-8"))

            self.assertEqual(result["build_evidence_locator"], "test://release-build")
            self.assertEqual(result["runtime_evidence_locator"], "test://runtime-acceptance")
            self.assertEqual(result["verification_evidence_locator"], "test://gate-g-final-review")
            self.assertEqual(
                result["verification_evidence"]["report_sha256"],
                hashlib.sha256(completion.read_bytes()).hexdigest(),
            )
            self.assertEqual(result["verification_evidence"]["acceptance_count"], 36)
            self.assertEqual(
                result["verification_evidence"]["acceptance_authority"]["path"],
                "docs/project/distribution-rebuild-specification.md",
            )
            self.assertEqual(manifest["verification_evidence_locator"], "test://gate-g-final-review")
            self.assertEqual(manifest["verification_evidence"], result["verification_evidence"])

    def test_release_completion_evidence_requires_verified_runtime_compatibility(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(root / "completion-evidence")
            with self.assertRaisesRegex(
                ValueError,
                "requires validated Runtime Acceptance evidence",
            ):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_requires_locator_and_report_together(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(root / "completion-evidence")
            with self.subTest("locator-only"), self.assertRaisesRegex(
                ValueError,
                "requires locator and machine-readable evidence together",
            ):
                self._build(
                    root / "locator-only",
                    verification_evidence_locator="test://gate-g-final-review",
                )
            with self.subTest("report-only"), self.assertRaisesRegex(
                ValueError,
                "requires locator and machine-readable evidence together",
            ):
                self._build(
                    root / "report-only",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_stale_source_sha(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            stale_sha = "0" * 40 if self.source_sha != "0" * 40 else "1" * 40
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                source_sha=stale_sha,
            )
            with self.assertRaisesRegex(ValueError, "source SHA does not match"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://stale-gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_nonzero_findings(self):
        for finding in ("blocking", "medium", "unverified"):
            with self.subTest(finding=finding), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                counts = {"blocking": 0, "medium": 0, "unverified": 0}
                counts[finding] = 1
                completion = self._write_release_completion_evidence(
                    root / "completion-evidence",
                    finding_counts=counts,
                )
                with self.assertRaisesRegex(ValueError, f"{finding} finding count is not zero"):
                    self._build(
                        root / "release",
                        verification_evidence_locator="test://failed-gate-g-final-review",
                        release_completion_evidence=completion,
                    )

    def test_release_completion_evidence_rejects_incomplete_acceptance_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                acceptance_results=[],
            )
            with self.assertRaisesRegex(ValueError, "acceptance results are missing"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://incomplete-gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_partial_acceptance_scope(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                acceptance_results=[
                    {
                        "id": "DR-AC-01",
                        "status": "PASS",
                        "evidence_locators": ["test://gate-g/DR-AC-01"],
                    }
                ],
            )
            with self.assertRaisesRegex(ValueError, "acceptance scope does not match"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://partial-gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_acceptance_outside_current_scope(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                acceptance_results=[
                    {
                        "id": "DR-AC-99",
                        "status": "PASS",
                        "evidence_locators": ["test://gate-g/DR-AC-99"],
                    }
                ],
            )
            with self.assertRaisesRegex(ValueError, "outside current claim scope"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://extra-gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_acceptance_without_evidence_locator(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                acceptance_results=[
                    {"id": "DR-AC-01", "status": "PASS", "evidence_locators": []},
                ],
            )
            with self.assertRaisesRegex(ValueError, "no recoverable evidence locator"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://invalid-gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_acceptance_non_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                acceptance_results=[
                    {
                        "id": "DR-AC-01",
                        "status": "UNVERIFIED",
                        "evidence_locators": ["test://gate-g/DR-AC-01"],
                    },
                ],
            )
            with self.assertRaisesRegex(ValueError, "acceptance is not PASS: DR-AC-01"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://unverified-gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_release_identity_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                release_id=f"agentic-dev@stale+{self.source_sha[:12]}",
            )
            with self.assertRaisesRegex(ValueError, "release identity does not match"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://mismatched-gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_claim_identity_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                claim_id="OTHER-CLAIM",
            )
            with self.assertRaisesRegex(ValueError, "claim identity does not match"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://mismatched-gate-g-claim",
                    release_completion_evidence=completion,
                )

    def test_release_completion_evidence_rejects_non_pass_status(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completion = self._write_release_completion_evidence(
                root / "completion-evidence",
                status="FAIL",
            )
            with self.assertRaisesRegex(ValueError, "release completion evidence is not PASS"):
                self._build(
                    root / "release",
                    verification_evidence_locator="test://failed-gate-g-final-review",
                    release_completion_evidence=completion,
                )

    def test_runtime_evidence_locator_without_reports_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "requires locator, automated runtime evidence"):
                self._build(
                    Path(temp),
                    runtime_evidence_locator="https://example.invalid/nonexistent-runtime-evidence",
                )

    def test_runtime_evidence_rejects_stale_source_sha(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            stale_sha = "0" * 40 if self.source_sha != "0" * 40 else "1" * 40
            automated, authenticated, authenticated_bundle = self._write_runtime_evidence(
                root / "evidence",
                source_sha=stale_sha,
            )
            with self.assertRaisesRegex(ValueError, "source SHA does not match"):
                self._build(
                    root / "release",
                    runtime_evidence_locator="test://stale-runtime-acceptance",
                    automated_runtime_evidence=automated,
                    authenticated_runtime_evidence=authenticated,
                    authenticated_runtime_evidence_bundle=authenticated_bundle,
                )

    def test_runtime_evidence_rejects_failed_authenticated_report(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            automated, authenticated, authenticated_bundle = self._write_runtime_evidence(
                root / "evidence",
                authenticated_status="FAIL",
            )
            with self.assertRaisesRegex(ValueError, "authenticated runtime evidence is not PASS"):
                self._build(
                    root / "release",
                    runtime_evidence_locator="test://failed-runtime-acceptance",
                    automated_runtime_evidence=automated,
                    authenticated_runtime_evidence=authenticated,
                    authenticated_runtime_evidence_bundle=authenticated_bundle,
                )

    def test_runtime_evidence_rejects_mismatched_embedded_grade_identity(self):
        cases = (
            (
                "scenario-id",
                {"scenario_id": "B-AR-01"},
                "semantic grade scenario identity mismatch",
            ),
            (
                "source-sha",
                {"source_commit": "0" * 40},
                "semantic grade source SHA mismatch",
            ),
            (
                "release-id",
                {"release_id": "agentic-dev@stale+000000000000"},
                "semantic grade release identity mismatch",
            ),
            (
                "runtime-mode",
                {"runtime_mode": "source-skill-copy"},
                "semantic grade runtime mode mismatch",
            ),
            (
                "runtime-version",
                {"runtime_codex_version": "stale-runtime"},
                "semantic grade runtime identity mismatch",
            ),
            (
                "grader-version",
                {"grader_codex_version": "stale-grader"},
                "semantic grade grader identity mismatch",
            ),
        )
        for name, updates, expected_error in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                automated, authenticated, authenticated_bundle = self._write_runtime_evidence(
                    root / "evidence"
                )
                evidence_path = "evals/results/behavior/B-RB-01.grade.json"
                self._rewrite_authenticated_bundle_json(
                    authenticated,
                    authenticated_bundle,
                    evidence_path,
                    updates,
                )
                with self.assertRaisesRegex(ValueError, expected_error):
                    release_build._validate_runtime_evidence(
                        self.source_sha,
                        "test://mismatched-grade-identity",
                        automated,
                        authenticated,
                        authenticated_bundle,
                    )

    def test_runtime_evidence_rejects_summary_only_authenticated_report(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            automated, authenticated, authenticated_bundle = self._write_runtime_evidence(
                root / "evidence"
            )
            authenticated.write_text(
                json.dumps(
                    {
                        "status": "PASS",
                        "source_sha": self.source_sha,
                        "scenario_count": 2,
                        "failed_scenarios": [],
                        "activation": {"status": "PASS"},
                        "behavior": {"status": "PASS"},
                    },
                    sort_keys=True,
                )
                + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "authenticated runtime evidence kind is invalid"):
                self._build(
                    root / "release",
                    runtime_evidence_locator="test://summary-only-runtime-acceptance",
                    automated_runtime_evidence=automated,
                    authenticated_runtime_evidence=authenticated,
                    authenticated_runtime_evidence_bundle=authenticated_bundle,
                )

    def test_runtime_evidence_requires_authenticated_evidence_bundle(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            automated, authenticated, _ = self._write_runtime_evidence(root / "evidence")
            with self.assertRaisesRegex(ValueError, "authenticated runtime evidence bundle together"):
                self._build(
                    root / "release",
                    runtime_evidence_locator="test://runtime-acceptance",
                    automated_runtime_evidence=automated,
                    authenticated_runtime_evidence=authenticated,
                )

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

    def test_upgrade_conflict_fails_before_mutating_consumer(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive, _ = self._build(root / "out")
            package = root / "package"
            with zipfile.ZipFile(archive, "r") as zf:
                zf.extractall(package)

            manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
            introduced_skill = sorted(item["name"] for item in manifest["skills"])[0]
            old_manifest = copy.deepcopy(manifest)
            old_manifest["skills"] = [
                item for item in old_manifest["skills"]
                if item["name"] != introduced_skill
            ]
            prefix = f"repository/.agents/skills/{introduced_skill}/"
            old_manifest["integrity"]["files"] = [
                item for item in old_manifest["integrity"]["files"]
                if not item["path"].startswith(prefix)
            ]

            target = root / "consumer"
            target.mkdir()
            shutil.copytree(package / "repository/.agents", target / ".agents")
            shutil.rmtree(target / ".agents/skills" / introduced_skill)
            local_skill = target / ".agents/skills" / introduced_skill
            local_skill.mkdir(parents=True)
            (local_skill / "local.txt").write_text("consumer local skill\n", encoding="utf-8")
            (target / ".agents/release/manifest.json").write_text(
                json.dumps(old_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            (target / "AGENTS.md").write_text("# Consumer Authority\n", encoding="utf-8")

            before = {
                path.relative_to(target).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(target.rglob("*"))
                if path.is_file()
            }
            with self.assertRaisesRegex(ValueError, "newly introduced release Skill"):
                installer.install(package, target)
            after = {
                path.relative_to(target).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(target.rglob("*"))
                if path.is_file()
            }
            self.assertEqual(before, after)

    def test_upgrade_rejects_extra_file_in_release_owned_skill_before_writing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive, _ = self._build(root / "out")
            package = root / "package"
            with zipfile.ZipFile(archive, "r") as zf:
                zf.extractall(package)

            target = root / "consumer"
            target.mkdir()
            (target / "AGENTS.md").write_text("# Consumer Authority\n", encoding="utf-8")
            installer.install(package, target)

            extra = target / ".agents/skills/clarify-intent/consumer-local-note.md"
            extra.write_text("local extension\n", encoding="utf-8")
            agents_before = (target / "AGENTS.md").read_text(encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "Skill file set was locally modified"):
                installer.install(package, target)

            self.assertTrue(extra.is_file())
            self.assertEqual(
                agents_before,
                (target / "AGENTS.md").read_text(encoding="utf-8"),
            )

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
