import copy, importlib.util, json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/outcome-evidence-bounds/conformance.json"
SPEC = importlib.util.spec_from_file_location("outcome_evidence_grade", ROOT / "pilots/outcome-evidence-bounds/grade.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)

class OutcomeEvidenceBoundsTests(unittest.TestCase):
    def setUp(self): self.data = json.loads(FIXTURE.read_text())
    def test_locked_fixture_paths_hashes_and_expected_report(self):
        report = MODULE.replay(self.data, check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual({"N": 5, "P": 3, "F": 1, "U": 1}, {k: report["cells"]["workflow-cell"][k] for k in ("N", "P", "F", "U")})
        self.assertEqual(["3/5", "4/5"], report["cells"]["workflow-cell"]["bounds"]["exact"])
    def test_native_labels_evidence_conflicts_and_stronger_conditions_are_preserved(self):
        rows = {r["id"]: r for r in MODULE.replay(self.data)["records"]}
        conflict = rows["workflow-native-failure-contradicted"]
        self.assertEqual("failure", conflict["native_label"]); self.assertEqual("contradicted", conflict["evidence_state"])
        self.assertTrue(conflict["benchmark_conflict"]); self.assertEqual("P", conflict["classification"])
        stronger = rows["workflow-native-success-professional-fail"]
        self.assertEqual("success", stronger["native_label"]); self.assertEqual("fail", stronger["stronger_condition"]); self.assertEqual("P", stronger["classification"])
    def test_unknown_is_not_coerced_by_native_label(self):
        rows = {r["id"]: r for r in MODULE.replay(self.data)["records"]}
        self.assertEqual("U", rows["workflow-native-success-missing-post-state"]["classification"])
        self.assertEqual("U", rows["artifact-unknown-b"]["classification"])
    def test_only_proven_pre_run_invalidity_is_excluded(self):
        cell = MODULE.replay(self.data)["cells"]["workflow-cell"]
        self.assertEqual(5, cell["N"]); self.assertEqual("workflow-pre-run-environment-invalid", cell["excluded"][0]["record_id"])
        data = copy.deepcopy(self.data); data["records"][1]["inclusion"] = {"status": "excluded", "cause": "post_start_failure", "reason": "invalid exclusion"}
        data["locked_records_sha256"] = MODULE.canonical_hash(data["records"])
        self.assertFalse(MODULE.replay(data)["valid"])
    def test_overlapping_intervals_do_not_support_directional_ranking(self):
        comparison = MODULE.replay(self.data)["comparisons"][0]
        self.assertEqual("unresolved_overlapping_identification_intervals", comparison["result"])
    def test_record_tampering_breaks_lock(self):
        data = copy.deepcopy(self.data); data["records"][0]["native_label"] = "failure"
        self.assertIn("locked record hash mismatch", MODULE.replay(data)["errors"])
    def test_claim_upgrade_is_rejected(self):
        data = copy.deepcopy(self.data); data["claim_limits"]["unsupported"].remove("population ranking")
        self.assertFalse(MODULE.replay(data)["valid"])
    def test_stronger_failure_cannot_change_native_aggregate(self):
        data = copy.deepcopy(self.data); row = next(r for r in data["records"] if r["id"] == "workflow-native-success-professional-fail")
        row["stronger_condition"] = "pass"; data["locked_records_sha256"] = MODULE.canonical_hash(data["records"])
        report = MODULE.replay(data)
        self.assertEqual(3, report["cells"]["workflow-cell"]["P"])

if __name__ == "__main__": unittest.main()
