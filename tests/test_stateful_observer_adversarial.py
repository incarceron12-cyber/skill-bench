from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/stateful-observer-adversarial/conformance.json"
SPEC = importlib.util.spec_from_file_location("stateful_observer_validate", ROOT / "pilots/stateful-observer-adversarial/validate.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)

class StatefulObserverAdversarialTests(unittest.TestCase):
    def setUp(self): self.data = json.loads(FIXTURE.read_text())
    def test_matrix_replays_with_provenance(self):
        report = MODULE.replay(self.data, check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual({"cases": 9, "accepted": 2, "rejected_semantic": 6, "observer_insufficient": 1}, report["summary"])
        self.assertGreaterEqual(len({x["work_shape"] for x in report["results"]}), 2)
    def test_semantic_alternatives_are_accepted(self):
        rows = {x["case_id"]: x for x in MODULE.replay(self.data)["results"]}
        self.assertEqual("accepted", rows["equivalent-filter-order"]["outcome"])
        self.assertEqual("accepted", rows["noncanonical-extensional-result"]["outcome"])
    def test_collateral_duplicate_collision_and_lifecycle_failures_reject(self):
        rows = {x["case_id"]: x for x in MODULE.replay(self.data)["results"]}
        for case_id in ("collateral-field-mutation", "duplicate-unrelated-record", "shared-state-collision", "pre-satisfied-state", "reversed-before-observation", "teardown-orphan-fingerprint-mismatch"):
            self.assertEqual("rejected", rows[case_id]["outcome"])
            self.assertTrue(rows[case_id]["diagnostic"].startswith("semantic_failure:"))
    def test_correct_answer_without_access_abstains(self):
        row = next(x for x in MODULE.replay(self.data)["results"] if x["case_id"] == "correct-answer-without-evidence-access")
        self.assertEqual("insufficient_evidence", row["outcome"])
        self.assertEqual("observer_insufficiency:evidence_access", row["diagnostic"])
    def test_hidden_invariance_fails_closed(self):
        data = copy.deepcopy(self.data); data["cases"][0]["applied_invariances"] = ["url-spelling"]
        report = MODULE.replay(data); self.assertFalse(report["valid"]); self.assertTrue(any("undeclared invariance" in x for x in report["errors"]))
    def test_expected_outcome_cannot_override_observation(self):
        data = copy.deepcopy(self.data); data["cases"][2]["expected"] = {"outcome":"accepted","diagnostic":"semantic_success"}
        report = MODULE.replay(data); self.assertFalse(report["valid"]); self.assertTrue(any("expected" in x for x in report["errors"]))
    def test_claim_upgrade_rejected(self):
        data = copy.deepcopy(self.data); data["claim_limits"]["unsupported"].remove("professional validity")
        self.assertFalse(MODULE.replay(data)["valid"])

if __name__ == "__main__": unittest.main()
