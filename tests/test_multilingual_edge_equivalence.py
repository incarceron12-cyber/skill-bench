from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/multilingual-edge-equivalence/conformance.json"
SPEC = importlib.util.spec_from_file_location("multilingual_equivalence", ROOT / "pilots/multilingual-edge-equivalence/validate.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class MultilingualEdgeEquivalenceTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_five_matched_forms_and_six_cases_replay(self):
        report = MODULE.replay(self.data)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(5, len(report["matched_forms"]))
        self.assertEqual(6, report["cases_replayed"])

    def test_diagnoses_are_separate_and_fail_closed(self):
        rows = {row["case_id"]: row for row in MODULE.replay(self.data)["results"]}
        self.assertEqual("semantic_transfer", rows["semantic-transfer-negation"]["failure"])
        self.assertEqual("locale_format", rows["locale-number-format"]["failure"])
        self.assertEqual("provenance_loss", rows["provenance-loss"]["failure"])
        self.assertEqual("unsupported_authority", rows["unsupported-authority"]["failure"])
        self.assertEqual("insufficient_evidence", rows["grader-language-bias"]["outcome"])

    def test_expected_result_tampering_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["cases"][1]["expected"] = {"outcome":"passed", "failure":"none"}
        self.assertFalse(MODULE.replay(data)["valid"])

    def test_claim_upgrade_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["claim_limits"]["unsupported"].remove("multilingual capability")
        self.assertFalse(MODULE.replay(data)["valid"])

    def test_review_approval_requires_real_reviewer_record(self):
        data = copy.deepcopy(self.data)
        data["review_gates"]["bilingual_equivalence_review"]["status"] = "passed"
        self.assertFalse(MODULE.replay(data)["valid"])

    def test_environment_must_remain_hash_pinned(self):
        data = copy.deepcopy(self.data)
        data["environment"]["renderer"]["sha256"] = "unpinned"
        self.assertFalse(MODULE.replay(data)["valid"])

if __name__ == "__main__": unittest.main()
