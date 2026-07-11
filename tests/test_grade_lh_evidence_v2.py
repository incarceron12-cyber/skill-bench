from __future__ import annotations

import csv
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.grade_lh_evidence import grade as grade_legacy
from scripts.grade_lh_evidence_v2 import CONTRACT, CONFIG, CONTRACT_VERSION, GRADER_VERSION, grade

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/lh-skill-adoption"
SOURCE = PILOT / "source-pack/decision-evidence.csv"
CORPUS = PILOT / "provenance-v2/conformance-corpus.json"


class LhEvidenceV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.matrix = root / "matrix.csv"
        self.memo = root / "memo.md"
        with SOURCE.open(newline="", encoding="utf-8") as handle:
            sources = list(csv.DictReader(handle))
        with self.matrix.open("w", newline="", encoding="utf-8") as handle:
            fields = ["claim", "evidence_id", "authority", "scope", "caveat", "decision_use"]
            writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader()
            for row in sources:
                writer.writerow({"claim": "Source claim", "evidence_id": row["evidence_id"], "authority": row["authority"], "scope": row["scope"], "caveat": row["caveat"], "decision_use": "Review conservatively"})

    def tearDown(self) -> None:
        self.tmp.cleanup()

    @staticmethod
    def codes(result: dict[str, object]) -> set[str]:
        return {str(item).split(" | ", 1)[0] for item in result["evidence"]}

    def test_frozen_conformance_corpus(self) -> None:
        corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
        seen = set()
        for case in corpus["cases"]:
            with self.subTest(case=case["id"]):
                self.memo.write_text(case["memo_line"] + "\n", encoding="utf-8")
                result = grade(SOURCE, self.matrix, self.memo)
                expected = "passed" if case["expected"] == "passed_with_review_flag" else case["expected"]
                self.assertEqual(expected, result["outcome"])
                self.assertTrue(set(case["expected_codes"]) <= self.codes(result))
                seen.add(case["id"])
        self.assertEqual(12, len(seen))

    def test_versions_and_current_hashes_are_bound(self) -> None:
        self.memo.write_text("Require {{PROSPECTIVE:30 paired runs}}.\n", encoding="utf-8")
        instrument = grade(SOURCE, self.matrix, self.memo)["instrument"]
        self.assertEqual(GRADER_VERSION, instrument["grader_version"])
        self.assertEqual(CONTRACT_VERSION, instrument["contract_version"])
        self.assertEqual(hashlib.sha256(CONFIG.read_bytes()).hexdigest(), instrument["grader_config_sha256"])
        self.assertEqual(hashlib.sha256(CONTRACT.read_bytes()).hexdigest(), instrument["public_contract_sha256"])

    def test_marker_abstains_only_value_check(self) -> None:
        self.memo.write_text("Unsupported source {{PROSPECTIVE:30 runs}} [E99].\n", encoding="utf-8")
        result = grade(SOURCE, self.matrix, self.memo)
        self.assertIn("UNKNOWN_EVIDENCE_ID", self.codes(result))

    def test_legacy_v8_v10_results_replay_byte_for_semantic_byte(self) -> None:
        for pair in ("isolated-agent-pair-v8", "isolated-agent-pair-v10"):
            for arm in ("no-skill", "public-skill"):
                base = PILOT / "ablation" / pair / arm
                actual = grade_legacy(SOURCE, base / "trial/outputs/evidence-matrix.csv", base / "trial/outputs/recommendation.md")
                retained = json.loads((base / "grader-results/evidence-link-grader.json").read_text(encoding="utf-8"))
                self.assertEqual(retained, actual, f"legacy drift in {pair}/{arm}")

    def test_review_records_machine_blind_overbroad_abstention(self) -> None:
        review = (PILOT / "provenance-v2/abstention-boundary-review.md").read_text(encoding="utf-8")
        self.assertIn("semantic-marker", review.lower())
        self.assertIn("cannot establish entailment", review)


if __name__ == "__main__":
    unittest.main()
