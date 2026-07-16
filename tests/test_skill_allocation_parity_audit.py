import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_skill_allocation_parity.py"
MANIFEST = ROOT / "pilots" / "skill-allocation-parity-audit" / "v1" / "manifest.json"
spec = importlib.util.spec_from_file_location("allocation_audit", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SkillAllocationParityAuditTests(unittest.TestCase):
    def setUp(self):
        self.base = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_frozen_replay_retains_all_and_fails_closed_on_estimand(self):
        report = module.run_audit(MANIFEST)
        self.assertTrue(report["integrity_passed"], report["errors"])
        self.assertEqual(report["intended_attempts"], 14)
        self.assertEqual(report["retained_allocation_records"], 14)
        self.assertEqual(report["admissible_matched_contrasts"], 0)
        self.assertEqual(report["allocation_conclusion"], "insufficient_evidence")
        self.assertTrue(all(record["allocation_evidence_status"] == "insufficient_evidence" for record in report["allocation_records"]))
        self.assertTrue(all(not value for value in report["claim_ceiling"].values()))

    def test_rejects_aggregate_token_laundering(self):
        doc = copy.deepcopy(self.base)
        evidence = doc["attempts"][0]["resource_evidence"]
        evidence["allocation_breakdown_available"] = True
        evidence["per_component_locators"] = []
        errors = module.semantic_errors(doc)
        self.assertTrue(any("aggregate-token laundering" in error for error in errors), errors)

    def test_rejects_unmatched_prompt_or_budget_identity(self):
        doc = copy.deepcopy(self.base)
        doc["attempts"][0]["configured_system_sha256"] = "0" * 64
        errors = module.semantic_errors(doc, check_paths=True)
        self.assertTrue(any("unmatched prompt/budget" in error for error in errors), errors)

    def test_rejects_complete_case_substitution(self):
        doc = copy.deepcopy(self.base)
        doc["attempts"].pop(0)
        errors = module.semantic_errors(doc)
        self.assertTrue(any("complete-case substitution" in error for error in errors), errors)

    def test_rejects_public_skill_visibility_as_adoption(self):
        doc = copy.deepcopy(self.base)
        row = next(row for row in doc["attempts"] if row["condition"] == "public_skill")
        row["module_flow_evidence"]["adoption_status"] = "adopted"
        errors = module.semantic_errors(doc)
        self.assertTrue(any("visibility cannot establish adoption" in error for error in errors), errors)

    def test_pair_rejects_state_and_order_mismatch(self):
        report = module.run_audit(MANIFEST)
        left = copy.deepcopy(report["allocation_records"][0])
        right = next(copy.deepcopy(row) for row in report["allocation_records"] if row["study_id"] == left["study_id"] and row["task_id"] == left["task_id"] and row["condition"] != left["condition"])
        for row in (left, right):
            row["allocation_evidence_status"] = "sufficient"
            row["service_status"] = row["environment_status"] = row["grader_status"] = "valid"
            row["initial_shared_state"] = {"status": "observed", "value": "state-a"}
            row["final_shared_state"] = {"status": "observed", "value": "state-b"}
        right["execution_order"] = left["execution_order"] + 1
        right["initial_shared_state"]["value"] = "different-state"
        result = module.assess_pair(left, right, self.base["predeclared_before_outcome_replay"])
        self.assertEqual(result["status"], "insufficient_evidence")
        self.assertIn("unmatched_execution_order", result["reasons"])
        self.assertIn("unmatched_initial_shared_state", result["reasons"])

    def test_rejects_claim_upgrade(self):
        doc = copy.deepcopy(self.base)
        doc["claim_ceiling"]["skill_effect"] = True
        errors = module.semantic_errors(doc)
        self.assertTrue(any("claim upgrade forbidden" in error for error in errors), errors)

    def test_rejects_stale_parent_bytes(self):
        doc = copy.deepcopy(self.base)
        doc["attempts"][0]["artifacts"][0]["sha256"] = "0" * 64
        errors = module.semantic_errors(doc, check_paths=True)
        self.assertTrue(any("stale parent bytes" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
