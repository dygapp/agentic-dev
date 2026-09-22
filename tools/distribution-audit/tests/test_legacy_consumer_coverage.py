from __future__ import annotations

import json
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = REPO_ROOT / "evals/fixtures/legacy-consumer-coverage/gate-f.json"
EXPECTED_IDS = {f"GF-{index:02d}" for index in range(1, 27)}
ALLOWED = {
    "release-covered",
    "release-composed",
    "consumer-local",
    "bootstrap-covered",
    "platform-covered",
    "intentionally-retired",
    "gap",
}


class LegacyConsumerCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.document = json.loads(EVIDENCE.read_text(encoding="utf-8"))
        cls.obligations = cls.document["obligations"]

    def test_gate_f_subject_and_acceptance_are_explicit(self) -> None:
        self.assertEqual(self.document["gate"], "F")
        self.assertEqual(self.document["acceptance"], ["DR-AC-31", "DR-AC-32"])
        self.assertRegex(self.document["provider"]["source_sha"], r"^[0-9a-f]{40}$")
        self.assertRegex(self.document["consumer"]["source_sha"], r"^[0-9a-f]{40}$")
        self.assertFalse(self.document["consumer"]["mutated"])

    def test_all_frozen_obligations_are_classified_once(self) -> None:
        ids = [item["id"] for item in self.obligations]
        self.assertEqual(len(ids), 26)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), EXPECTED_IDS)
        for item in self.obligations:
            self.assertIn(item["disposition"], ALLOWED)
            self.assertTrue(item["legacy_consumer_evidence"])
            self.assertTrue(item["current_coverage"])

    def test_consumer_local_dispositions_have_explicit_owner(self) -> None:
        for item in self.obligations:
            if item["disposition"] == "consumer-local":
                self.assertTrue(
                    item["consumer_local_owner"],
                    msg=f"{item['id']} lacks Consumer-local owner",
                )

    def test_exit_summary_is_derived_and_gap_free(self) -> None:
        gap = sum(item["disposition"] == "gap" for item in self.obligations)
        unclassified = sum(item["disposition"] not in ALLOWED for item in self.obligations)
        summary = self.document["summary"]
        self.assertEqual(summary["total"], len(self.obligations))
        self.assertEqual(summary["classified"], len(self.obligations) - unclassified)
        self.assertEqual(summary["unclassified"], unclassified)
        self.assertEqual(summary["gap"], gap)
        self.assertEqual(summary["consumer_mutation"], 0)
        self.assertEqual(unclassified, 0)
        self.assertEqual(gap, 0)


if __name__ == "__main__":
    unittest.main()
