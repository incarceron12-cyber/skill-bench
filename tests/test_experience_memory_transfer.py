import copy
import json
import unittest
from pathlib import Path

from scripts.validate_experience_memory_transfer import replay, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/experience-memory-transfer/conformance.json"

class ExperienceMemoryTransferTests(unittest.TestCase):
    def setUp(self):
        self.package = json.loads(FIXTURE.read_text())

    def test_fixture_valid_and_paths_resolve(self):
        validate_file(FIXTURE, check_paths=True)

    def test_replay_separates_qa_from_action(self):
        cells = replay(self.package)["memory_cells"]
        self.assertTrue(cells["evidence_only"]["qa_correct"])
        self.assertFalse(cells["evidence_only"]["action_safe"])
        self.assertTrue(cells["evidence_only"]["harmful_transfer"])
        self.assertTrue(cells["provenance_gated_promoted_lesson"]["action_safe"])

    def test_consequence_replay_separates_failure_boundaries(self):
        result = replay(self.package)
        cases = result["consequence_cases"]
        self.assertEqual(cases["summary-omission"]["classification"], "retrieval_failure")
        self.assertEqual(cases["stale-adoption"]["classification"], "stale_evidence_failure")
        self.assertEqual(cases["transition-missed"]["classification"], "state_transition_failure")
        self.assertEqual(cases["collateral-mutation"]["classification"], "collateral_preservation_failure")
        self.assertEqual(cases["unavailable-evaluator"]["classification"], "instrument_invalid")
        self.assertEqual(result["capability_denominator_count"], 5)

    def test_instrument_invalid_cannot_enter_denominator(self):
        p = copy.deepcopy(self.package)
        next(x for x in p["consequence_observations"] if x["id"] == "unavailable-evaluator")["capability_denominator_eligible"] = True
        self.assertTrue(any("denominator eligibility" in e for e in semantic_errors(p)))

    def test_collateral_mutation_cannot_be_labeled_success(self):
        p = copy.deepcopy(self.package)
        next(x for x in p["consequence_observations"] if x["id"] == "collateral-mutation")["expected_classification"] = "success"
        self.assertTrue(any("does not replay" in e for e in semantic_errors(p)))

    def test_stale_adoption_is_not_retrieval_failure(self):
        p = copy.deepcopy(self.package)
        next(x for x in p["consequence_observations"] if x["id"] == "stale-adoption")["expected_classification"] = "retrieval_failure"
        self.assertTrue(any("does not replay" in e for e in semantic_errors(p)))

    def test_adoption_without_access_is_rejected(self):
        p = copy.deepcopy(self.package)
        p["conditions"][1]["action"]["adopted_ids"] = ["traj-safe-alternative"]
        self.assertTrue(any("available -> accessed -> adopted" in e for e in semantic_errors(p)))

    def test_attempt_is_not_realization(self):
        p = copy.deepcopy(self.package)
        failed = next(x for x in p["trajectory_history"] if x["kind"] == "failed_attempt")
        failed["realized"] = True
        self.assertTrue(any("attempt from realization" in e for e in semantic_errors(p)))

    def test_unresolved_stale_contradiction_is_rejected(self):
        p = copy.deepcopy(self.package)
        stale = next(x for x in p["trajectory_history"] if x["kind"] == "stale_observation")
        stale.pop("superseded_by")
        self.assertTrue(any("contradiction and supersession" in e for e in semantic_errors(p)))

    def test_harmful_transfer_requires_rollback_evidence(self):
        p = copy.deepcopy(self.package)
        p["conditions"][1]["action"]["rollback"] = ""
        self.assertTrue(any("harmful transfer, and rollback" in e for e in semantic_errors(p)))

    def test_stochastic_cell_requires_repetition(self):
        p = copy.deepcopy(self.package)
        p["execution"]["stochastic_components"] = ["reader"]
        self.assertTrue(any("require repeated" in e for e in semantic_errors(p)))

    def test_claim_upgrade_is_rejected(self):
        p = copy.deepcopy(self.package)
        p["claim_limits"]["unsupported"].remove("professional competence")
        self.assertTrue(any("non-claims" in e for e in semantic_errors(p)))

if __name__ == "__main__": unittest.main()
