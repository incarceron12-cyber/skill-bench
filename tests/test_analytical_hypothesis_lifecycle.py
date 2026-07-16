import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "pilots/analytical-hypothesis-lifecycle-v1/replay.py"
SPEC = importlib.util.spec_from_file_location("analytical_hypothesis_replay", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AnalyticalHypothesisLifecycleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = MODULE.load(MODULE.PROTOCOL)
        cls.observations = MODULE.load(MODULE.OBSERVATIONS)
        cls.retained_report = json.loads(MODULE.REPORT.read_text())

    def report(self, protocol=None, observations=None, check_paths=True):
        return MODULE.build_report(
            protocol or copy.deepcopy(self.protocol),
            observations or copy.deepcopy(self.observations),
            check_paths=check_paths,
        )

    def test_frozen_cross_domain_replay_matches_retained_report(self):
        rebuilt = self.report()
        self.assertTrue(rebuilt["valid"], rebuilt["errors"])
        self.assertEqual(self.retained_report, rebuilt)
        self.assertEqual(2, len({case["domain"] for case in self.protocol["cases"]}))
        self.assertEqual(4, rebuilt["execution"]["attempts_retained"])
        self.assertEqual(0, rebuilt["execution"]["model_calls"])

    def test_five_scores_remain_separate_without_holistic_scalar(self):
        report = self.report()
        self.assertEqual(set(MODULE.STAGES), set(report["separate_stage_denominators"]))
        self.assertNotIn("holistic_score", report)
        good = next(row for row in report["attempts"] if row["attempt_id"] == "vendor-routing-incident-repeat-1")
        self.assertEqual(
            {"candidate_quality": (4, 4), "test_validity": (4, 4), "evidence_adoption": (3, 3), "final_conclusion": (3, 3), "consequence": (3, 3)},
            {stage: (score["numerator"], score["denominator"]) for stage, score in good["scores"].items()},
        )

    def test_non_discriminating_test_does_not_receive_truth_credit(self):
        report = self.report()
        bad = next(row for row in report["attempts"] if row["attempt_id"] == "vendor-routing-incident-repeat-2")
        self.assertEqual(3, bad["scores"]["test_validity"]["numerator"])
        self.assertEqual(0, bad["scores"]["evidence_adoption"]["numerator"])
        self.assertEqual(0, bad["scores"]["final_conclusion"]["numerator"])
        self.assertEqual(0, bad["scores"]["consequence"]["numerator"])
        codes = {item["code"] for item in bad["diagnostics"]}
        self.assertIn("non_discriminating_test_selected", codes)
        self.assertIn("candidate_promoted_without_test", codes)
        self.assertIn("unsupported_harmful_action", codes)

    def test_typed_evaluator_invalidity_is_not_imputed_as_failure(self):
        report = self.report()
        row = next(item for item in report["attempts"] if item["attempt_id"] == "laboratory-shift-anomaly-repeat-2")
        conclusion = row["scores"]["final_conclusion"]
        self.assertEqual("invalid_output", conclusion["evaluator_state"])
        self.assertIsNone(conclusion["numerator"])
        self.assertEqual(0, conclusion["denominator"])
        self.assertEqual({"intended": 4, "evaluator_valid": 3, "evaluator_invalid": 1}, report["separate_stage_denominators"]["final_conclusion"])

    def test_missing_rival_is_rejected_before_scoring(self):
        protocol = copy.deepcopy(self.protocol)
        protocol["cases"][0]["evidence_graph"]["rival_hypotheses"] = []
        errors = MODULE.validate(protocol, self.observations)
        self.assertTrue(any("rival" in error for error in errors))

    def test_unexecutable_discriminating_test_is_rejected(self):
        protocol = copy.deepcopy(self.protocol)
        protocol["cases"][0]["tests"][1]["operation"] = "judge_the_prose"
        errors = MODULE.validate(protocol, self.observations)
        self.assertTrue(any("not executable" in error for error in errors))

    def test_parseable_observer_cannot_be_labeled_invalid(self):
        observations = copy.deepcopy(self.observations)
        observer = observations["attempts"][-1]["observer_outputs"][3]
        observer["raw_output"] = '{"eligible": true}'
        errors = MODULE.validate(self.protocol, observations)
        self.assertTrue(any("mislabeled invalid" in error for error in errors))

    def test_claim_ceiling_cannot_drop_professional_validity(self):
        protocol = copy.deepcopy(self.protocol)
        protocol["claim_limits"]["unsupported"].remove("professional validity")
        errors = MODULE.validate(protocol, self.observations)
        self.assertTrue(any("claim ceilings" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
