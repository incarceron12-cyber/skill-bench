from __future__ import annotations
import copy, importlib.util, json, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V1 = ROOT / "pilots/action-boundary-composition/v1"
V2 = ROOT / "pilots/action-boundary-composition/v2"
sys.path.insert(0, str(ROOT))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


run = module("action_boundary_v2_test_runner", V2 / "run.py")


class ActionBoundaryCompositionV2Tests(unittest.TestCase):
    def setUp(self):
        self.v1 = json.loads((V1 / "protocol.json").read_text())
        self.v2 = json.loads((V2 / "protocol.json").read_text())

    def test_protocol_valid_and_claim_ceiling_closed(self):
        self.assertEqual([], run.semantic_errors(self.v2))
        self.assertTrue(run.verify()["passed"])
        self.assertFalse(any(self.v2["claim_boundaries"].values()))

    def test_no_task_rubric_or_expected_outcome_tuning(self):
        for key in ("cells", "conditions", "forms", "configured_system", "strict_denominator", "grading_dimensions", "claim_boundaries", "valid_time", "source_components"):
            self.assertEqual(self.v1[key], self.v2[key], key)
        self.assertFalse(self.v2["replication_provenance"]["outcome_tuning"])
        self.assertEqual([], self.v2["replication_provenance"]["task_rubric_expected_outcome_changes"])

    def test_public_inputs_and_authority_records_are_byte_equivalent(self):
        v1_builder = module("action_boundary_v1_equivalence_builder", V1 / "freeze_protocol.py")
        v2_builder = module("action_boundary_v2_equivalence_builder", V2 / "freeze_protocol.py")
        for form in ("vendor", "lh"):
            self.assertEqual(v1_builder.public_task(form), v2_builder.public_task(form))
            for condition in self.v1["conditions"]:
                self.assertEqual(v1_builder.authority_record(form, condition), v2_builder.authority_record(form, condition))

    def test_zero_call_isolation_and_mutation_gates(self):
        value = run.preflight(False)
        self.assertTrue(value["passed"])
        self.assertEqual(0, value["model_calls"])
        self.assertEqual(6, len(value["isolation"]))
        self.assertTrue(all(row["passed"] for row in value["mutations"]["cases"]))

    def test_wrong_target_and_observer_gap_fail_closed(self):
        cell = next(row for row in self.v2["cells"] if row["condition"] == "current_authorized")
        decision = run.canonical_decision(cell, self.v2)
        decision["target"] = "wrong"
        self.assertFalse(run.grader.realize(decision, cell["private_contract"])["endpoint_applied"])
        decision = run.canonical_decision(cell, self.v2)
        decision["event_log"] = []
        self.assertFalse(run.grader.realize(decision, cell["private_contract"])["endpoint_applied"])

    def test_denominator_and_authority_mutations_are_rejected(self):
        denominator = copy.deepcopy(self.v2)
        denominator["strict_denominator"]["intended"] = 5
        self.assertIn("denominator_drift", run.semantic_errors(denominator))
        authority = copy.deepcopy(self.v2)
        authority["cells"][1]["private_contract"]["expected_behavior"] = "act"
        self.assertIn("authority_laundering", run.semantic_errors(authority))


if __name__ == "__main__":
    unittest.main()
