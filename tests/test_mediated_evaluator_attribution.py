import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "pilots/mediated-evaluator-attribution-v1/replay.py"
SPEC = importlib.util.spec_from_file_location("mediated_evaluator_replay", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MediatedEvaluatorAttributionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = MODULE.load(MODULE.PROTOCOL)
        cls.observations = MODULE.load(MODULE.OBSERVATIONS)

    def report(self, protocol=None, observations=None, check_paths=True):
        return MODULE.build_report(
            protocol or copy.deepcopy(self.protocol),
            observations or copy.deepcopy(self.observations),
            check_paths=check_paths,
        )

    def test_frozen_cross_domain_replay_and_contract_hashes(self):
        report = self.report()
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(20, len(report["candidate_uptake_action_check_chains"]))
        self.assertEqual(2, len({x["domain"] for x in self.protocol["work_shapes"]}))
        self.assertEqual(4, len(report["contract_reuse"]))

    def test_all_five_planted_diagnostics_are_exactly_present(self):
        report = self.report()
        self.assertEqual(
            set(self.protocol["required_diagnostics"]),
            {x["code"] for x in report["diagnostics"]},
        )

    def test_funnel_preserves_pre_and_post_selection_denominators(self):
        report = self.report()
        alpha_a = report["funnel_denominators"]["mediator-alpha"]["candidate-a"]
        beta_b = report["funnel_denominators"]["mediator-beta"]["candidate-b"]
        self.assertEqual({"source_population": 5, "projectable": 5, "mediator_valid": 5, "attempted": 5, "scored": 5}, alpha_a)
        self.assertEqual({"source_population": 5, "projectable": 5, "mediator_valid": 4, "attempted": 4, "scored": 3}, beta_b)

    def test_mediator_rank_reversal_is_not_pooled_away(self):
        rates = self.report()["metric_results"]
        self.assertGreater(rates["mediator-alpha"]["candidate-a"]["selected_projected_check_pass_rate"], rates["mediator-alpha"]["candidate-b"]["selected_projected_check_pass_rate"])
        self.assertLess(rates["mediator-beta"]["candidate-a"]["selected_projected_check_pass_rate"], rates["mediator-beta"]["candidate-b"]["selected_projected_check_pass_rate"])

    def test_endpoint_success_does_not_imply_attribution_or_erase_cost(self):
        report = self.report()
        chains = {x["attempt_id"]: x for x in report["candidate_uptake_action_check_chains"]}
        no_uptake = chains["memo-no-uptake-success::candidate-a::mediator-alpha"]
        harmful = chains["lab-positive-pass-with-harm::candidate-a::mediator-alpha"]
        self.assertTrue(no_uptake["endpoint_success"])
        self.assertFalse(no_uptake["attribution_credit"])
        self.assertTrue(harmful["endpoint_success"])
        self.assertFalse(harmful["attribution_credit"])
        metric = report["metric_results"]["mediator-alpha"]["candidate-a"]
        self.assertGreater(metric["selected_projected_check_pass_numerator"], metric["attributable_noncompensatory_pass_numerator"])

    def test_unknown_and_invalid_observations_are_not_scored_as_failure(self):
        report = self.report()
        counts = report["typed_check_state_counts"]
        self.assertGreater(counts["unknown"], 0)
        self.assertGreater(counts["invalid"], 0)
        self.assertEqual(4, report["funnel_denominators"]["mediator-alpha"]["candidate-b"]["scored"])
        self.assertEqual(3, report["funnel_denominators"]["mediator-beta"]["candidate-b"]["scored"])

    def test_candidate_action_without_uptake_is_rejected(self):
        observations = copy.deepcopy(self.observations)
        row = observations["attempts"][0]
        row["uptake"] = "ignored"
        row["action_source"] = "candidate-claim-1"
        errors = MODULE.validate(self.protocol, observations)
        self.assertTrue(any("without uptake" in error for error in errors))

    def test_silent_mediator_selection_drop_is_rejected(self):
        observations = copy.deepcopy(self.observations)
        row = next(x for x in observations["attempts"] if x["case_id"] == "memo-mediator-sensitive-ranking" and x["candidate"] == "candidate-a" and x["mediator"] == "mediator-alpha")
        row["attempt_status"] = "not_attempted_mediator_invalid"
        errors = MODULE.validate(self.protocol, observations)
        self.assertTrue(any("silently dropped" in error for error in errors))

    def test_claim_ceiling_cannot_drop_professional_validity(self):
        protocol = copy.deepcopy(self.protocol)
        protocol["claim_limits"]["unsupported"].remove("professional validity")
        errors = MODULE.validate(protocol, self.observations)
        self.assertTrue(any("claim limits" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
