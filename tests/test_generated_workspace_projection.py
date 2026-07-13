import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/generated-workspace-projection-conformance"
SPEC = importlib.util.spec_from_file_location("workspace_projection_audit", PILOT / "audit.py")
assert SPEC is not None and SPEC.loader is not None
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class GeneratedWorkspaceProjectionTests(unittest.TestCase):
    def setUp(self):
        self.suite = mod.load()

    def test_frozen_sources_and_projection_hashes(self):
        for record in self.suite["source_evidence"].values():
            self.assertEqual(record["sha256"], hashlib.sha256((ROOT / record["path"]).read_bytes()).hexdigest())
        mod.freeze_checks(self.suite)

    def test_cross_shape_replay_localizes_all_frozen_cases(self):
        report = mod.replay(self.suite, write=False)
        self.assertEqual(12, report["summary"]["cases"])
        self.assertEqual(2, report["summary"]["clean_controls"])
        self.assertEqual(10, report["summary"]["defects"])
        self.assertEqual(12, report["summary"]["exactly_localized"])
        self.assertEqual(2, len(report["summary"]["work_shapes"]))

    def test_hash_and_pointer_mutations_fail_closed(self):
        report = mod.replay(self.suite, write=False)
        rows = {r["case_id"]: r for r in report["rows"]}
        self.assertEqual("projection_hash_mismatch", rows["memo-hash-drift"]["observed_findings"][0]["code"])
        self.assertEqual("objective_infeasible", rows["memo-impossible-objective"]["observed_findings"][0]["code"])

    def test_graph_and_valid_time_mutations_are_distinct(self):
        report = mod.replay(self.suite, write=False)
        codes = {r["case_id"]: {f["code"] for f in r["observed_findings"]} for r in report["rows"]}
        self.assertEqual({"graph_endpoint_missing"}, codes["memo-dangling-endpoint"])
        self.assertEqual({"derivation_cycle"}, codes["lab-derivation-cycle"])
        self.assertEqual({"valid_time_inversion"}, codes["lab-valid-time"])
        self.assertEqual({"stale_derived_artifact"}, codes["memo-stale-derived"])

    def test_fallback_authority_feasibility_and_semantics_are_localized(self):
        report = mod.replay(self.suite, write=False)
        codes = {r["case_id"]: {f["code"] for f in r["observed_findings"]} for r in report["rows"]}
        expected = {
            "lab-fallback-laundering": {"fallback_status_mismatch"},
            "lab-unsupported-claim": {"unsupported_professional_claim"},
            "lab-authority-overreach": {"instruction_outside_authority"},
            "memo-impossible-objective": {"objective_infeasible"},
            "memo-semantic-drift": {"semantic_fidelity_failure"},
        }
        for case_id, wanted in expected.items():
            self.assertEqual(wanted, codes[case_id])

    def test_unrelated_state_and_repair_are_preserved(self):
        report = mod.replay(self.suite, write=False)
        self.assertTrue(all(r["unrelated_projection_hashes_preserved"] for r in report["rows"]))
        self.assertTrue(all(r["repair_restored_clean_baseline"] for r in report["rows"]))

    def test_tampered_frozen_projection_is_rejected_before_replay(self):
        suite = copy.deepcopy(self.suite)
        suite["worlds"][0]["projections"]["plan"]["value"]["as_of"] = "2026-06-16"
        with self.assertRaisesRegex(ValueError, "frozen .* plan hash mismatch"):
            mod.replay(suite, write=False)

    def test_unknown_mutation_inventory_is_rejected(self):
        suite = copy.deepcopy(self.suite)
        suite["cases"][0]["mutation"]["kind"] = "unknown"
        with self.assertRaisesRegex(ValueError, "mutation inventory"):
            mod.replay(suite, write=False)


if __name__ == "__main__":
    unittest.main()
