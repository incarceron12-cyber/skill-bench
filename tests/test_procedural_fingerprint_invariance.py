import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "pilots" / "procedural-fingerprint-invariance"
SPEC = importlib.util.spec_from_file_location("procedural_fingerprint_analysis", STUDY / "analyze.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProceduralFingerprintInvarianceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = json.loads((STUDY / "protocol.json").read_text(encoding="utf-8"))
        cls.report = json.loads((STUDY / "report.json").read_text(encoding="utf-8"))

    def validate_mutation(self, mutation):
        protocol = copy.deepcopy(self.protocol)
        mutation(protocol)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(protocol, handle)
            path = Path(handle.name)
        try:
            return MODULE.validate(path)
        finally:
            path.unlink(missing_ok=True)

    def test_matrix_replays_exactly_with_provenance(self):
        result = MODULE.validate(report_path=STUDY / "report.json", check_paths=True)
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["report"], self.report)
        self.assertEqual(result["report"]["denominators"], {
            "base_trials": 48,
            "canonical_observations": 96,
            "training_trials": 32,
            "held_out_task_trials": 16,
            "invalid_trials": 0,
            "missing_traces": 0,
        })

    def test_two_unlike_work_shapes_are_fully_crossed(self):
        trials = MODULE.build_trials(self.protocol)
        self.assertEqual({row["family"] for row in trials}, {"evidence_memo", "incident_triage"})
        cells = {(row["task_group"], row["treatment"], row["interface"], row["repeat"]) for row in trials}
        self.assertEqual(len(cells), 48)
        self.assertTrue(all(set(row["canonical"]) == {"canon_v1", "canon_perturbed"} for row in trials))

    def test_vocabulary_selection_is_nested_inside_training_groups(self):
        fitting = self.report["representation_fitting"]
        self.assertEqual(fitting["leakage_check"], "pass")
        self.assertTrue(set(fitting["fit_task_groups"]).isdisjoint(fitting["held_out_task_groups_not_used"]))
        self.assertEqual(fitting["selected_size"], min(item["size"] for item in fitting["selection_results"] if item["mean_group_accuracy"] == 1.0))

    def test_interface_and_observer_nuisance_are_visible(self):
        native = self.report["held_out_interface_treatment_discrimination"]["native_event"]
        canonical = self.report["held_out_interface_treatment_discrimination"]["raw_canonical_atom"]
        self.assertLess(sum(row["accuracy"] for row in native) / 2, 0.5)
        self.assertEqual([row["accuracy"] for row in canonical], [1.0, 1.0])
        sensitivity = self.report["observer_sensitivity"]
        self.assertEqual(sensitivity["unknown_action_mass"]["canon_v1"], 0.0)
        self.assertGreater(sensitivity["unknown_action_mass"]["canon_perturbed"], 0.0)
        self.assertGreater(sensitivity["mean_l1_strict_vs_perturbed"], 0.0)

    def test_artifact_state_outperforms_trace_for_outcome(self):
        associations = self.report["outcome_association_held_out_tasks"]
        self.assertEqual(associations["semantic_artifact_state"]["accuracy"], 1.0)
        self.assertLess(associations["canonical_bigram"]["accuracy"], 1.0)

    def test_repeats_and_fail_closed_denominators_are_reported(self):
        for observer in ("canon_v1", "canon_perturbed"):
            self.assertEqual(self.report["repeated_stability"][observer]["pairs"], 24)
        self.assertIn("invalid_trials", self.report["denominators"])
        self.assertIn("missing_traces", self.report["denominators"])

    def test_claim_promotion_is_rejected(self):
        result = self.validate_mutation(lambda p: p["claim_boundaries"].update(intervention_effect="supported"))
        self.assertFalse(result["valid"])
        self.assertIn("claim boundary must remain unsupported: intervention_effect", result["errors"])

    def test_split_overlap_is_rejected(self):
        def overlap(protocol):
            protocol["design"]["training_task_groups"].append("evidence_memo/h1")
        result = self.validate_mutation(overlap)
        self.assertFalse(result["valid"])
        self.assertTrue(any("training groups mismatch" in error for error in result["errors"]))

    def test_fixture_cannot_be_relabelled_empirical(self):
        result = self.validate_mutation(lambda p: p["outcome_planting"].update(not_empirical=False))
        self.assertFalse(result["valid"])
        self.assertIn("synthetic outcome must be marked not empirical", result["errors"])


if __name__ == "__main__":
    unittest.main()
