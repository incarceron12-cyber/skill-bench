import copy
import json
import unittest
from pathlib import Path

from scripts.validate_correction_realization import replay, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/correction-realization/conformance.json"


class CorrectionRealizationTests(unittest.TestCase):
    def setUp(self):
        self.package = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def representation(self, package, representation_id):
        return next(
            representation
            for family in package["families"]
            for representation in family["representations"]
            if representation["representation_id"] == representation_id
        )

    def test_fixture_valid_and_paths_resolve(self):
        validate_file(FIXTURE, check_paths=True)

    def test_replay_separates_realization_from_correctness(self):
        cells = replay(self.package)["families"]["procurement-approval-window"]
        wrong = cells["proc-discoverable-wrong"]
        self.assertTrue(wrong["all_required_adaptation_probes"])
        self.assertTrue(wrong["generator_exposed"])
        self.assertTrue(wrong["semantically_adopted"])
        self.assertFalse(wrong["independently_correct"])
        self.assertFalse(wrong["promotion_gates_pass"])
        self.assertEqual(wrong["rollback"], "applied")
        self.assertTrue(cells["proc-faithful"]["promotion_gates_pass"])

    def test_missing_evidence_locator_is_rejected(self):
        package = copy.deepcopy(self.package)
        faithful = self.representation(package, "reset-faithful")
        faithful["propositions"][0]["evidence_locator"] = ""
        self.assertTrue(any("missing_evidence_locator" in error for error in semantic_errors(package)))

    def test_unsupported_proposition_addition_is_rejected(self):
        package = copy.deepcopy(self.package)
        unsupported = self.representation(package, "reset-unsupported-hidden-ui")
        unsupported["expected_semantic_outcome"] = "passed"
        self.assertTrue(any("unsupported_addition" in error for error in semantic_errors(package)))

    def test_scope_widening_is_rejected(self):
        package = copy.deepcopy(self.package)
        widened = self.representation(package, "reset-scope-widened")
        widened["expected_semantic_outcome"] = "passed"
        self.assertTrue(any("scope_widening" in error for error in semantic_errors(package)))

    def test_modality_drift_is_rejected(self):
        package = copy.deepcopy(self.package)
        faithful = self.representation(package, "proc-faithful")
        faithful["propositions"][0]["modality"] = "recommended"
        self.assertTrue(any("modality_drift" in error for error in semantic_errors(package)))

    def test_valid_time_widening_is_rejected(self):
        package = copy.deepcopy(self.package)
        widened = self.representation(package, "proc-valid-time-widened")
        widened["expected_semantic_outcome"] = "passed"
        self.assertTrue(any("valid_time_widening" in error for error in semantic_errors(package)))

    def test_authority_precedence_inversion_is_rejected(self):
        package = copy.deepcopy(self.package)
        stale = self.representation(package, "proc-stale-authority")
        stale["expected_semantic_outcome"] = "passed"
        self.assertTrue(any("authority_precedence_inversion" in error for error in semantic_errors(package)))

    def test_any_probe_convergence_is_rejected(self):
        package = copy.deepcopy(self.package)
        package["policy"]["convergence_quantifier"] = "any_required_probe"
        self.assertTrue(any("all-required-probe" in error for error in semantic_errors(package)))

    def test_reported_convergence_requires_every_adaptation_probe(self):
        package = copy.deepcopy(self.package)
        faithful = self.representation(package, "reset-faithful")
        faithful["realization"]["probe_retrieval"]["reset-paraphrase"] = False
        self.assertTrue(any("reported convergence" in error for error in semantic_errors(package)))

    def test_same_loop_correctness_cannot_promote(self):
        package = copy.deepcopy(self.package)
        faithful = self.representation(package, "proc-faithful")
        faithful["realization"]["correctness_observer"] = "adaptation_loop_judge"
        self.assertTrue(any("same-loop correctness" in error for error in semantic_errors(package)))

    def test_retrieval_only_readiness_claim_is_rejected(self):
        package = copy.deepcopy(self.package)
        wrong = self.representation(package, "proc-discoverable-wrong")
        wrong["realization"]["readiness_claim"] = True
        self.assertTrue(any("readiness claims" in error for error in semantic_errors(package)))


if __name__ == "__main__":
    unittest.main()
