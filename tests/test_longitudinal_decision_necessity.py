import copy
import json
import unittest
from pathlib import Path

from scripts.validate_longitudinal_decision_necessity import replay, semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "pilots/longitudinal-decision-necessity/conformance.json"


class LongitudinalDecisionNecessityTests(unittest.TestCase):
    def setUp(self):
        self.suite = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_fixture_valid_and_source_paths_hashes_resolve(self):
        validate_file(FIXTURE, check_paths=True)

    def test_replay_freezes_ten_cells_and_separates_outcomes(self):
        result = replay(self.suite)
        self.assertEqual(result["frozen_denominator"], 10)
        self.assertEqual(result["counts"], {"supported": 8, "missing": 1, "invalid": 1})
        self.assertIsNone(result["performance_estimate"])
        correct = [c for c in result["cells"] if c["condition"] == "correct"]
        self.assertTrue(all(c["boundary_changed_from_absent"] for c in correct))
        self.assertTrue(all(c["selected_action_admissible"] for c in result["cells"]))

    def test_history_access_without_necessity_is_rejected(self):
        p = copy.deepcopy(self.suite)
        scenario = p["scenarios"][0]
        correct = next(c for c in scenario["conditions"] if c["condition"] == "correct")
        absent = next(c for c in scenario["conditions"] if c["condition"] == "absent")
        correct["expected_admissible_action_ids"] = absent["expected_admissible_action_ids"]
        correct["selected_action_id"] = absent["selected_action_id"]
        self.assertTrue(any("access but no necessity" in e for e in semantic_errors(p)))

    def test_retrospective_behavior_cannot_become_normative_oracle(self):
        p = copy.deepcopy(self.suite)
        p["scenarios"][0]["oracle"]["oracle_type"] = "recorded_behavior"
        p["scenarios"][0]["oracle"]["normative_appropriateness"] = True
        self.assertTrue(any("launders retrospective behavior" in e for e in semantic_errors(p)))
        p = copy.deepcopy(self.suite)
        p["scenarios"][0]["recorded_behavior_witness"]["used_as_oracle"] = True
        self.assertTrue(any("cannot inherit normative authority" in e for e in semantic_errors(p)))

    def test_false_unique_chronology_is_rejected(self):
        p = copy.deepcopy(self.suite)
        p["scenarios"][1]["chronology"]["claim"] = "unique"
        self.assertTrue(any("falsely claims a unique chronology" in e for e in semantic_errors(p)))

    def test_denominator_leakage_is_rejected(self):
        p = copy.deepcopy(self.suite)
        p["metric"]["eligible_count"] = 8
        p["metric"]["attempted_count"] = 8
        self.assertTrue(any("denominator must equal all frozen cells" in e for e in semantic_errors(p)))
        p = copy.deepcopy(self.suite)
        p["metric"]["missing_count"] = 0
        self.assertTrue(any("outcome counts do not replay" in e for e in semantic_errors(p)))

    def test_evidence_flow_and_alternative_actions_fail_closed(self):
        p = copy.deepcopy(self.suite)
        correct = p["scenarios"][0]["conditions"][0]
        correct["adopted_ids"] = ["vendor-current-clearance"]
        correct["visible_ids"] = []
        self.assertTrue(any("available -> visible -> adopted" in e for e in semantic_errors(p)))
        p = copy.deepcopy(self.suite)
        p["scenarios"][1]["conditions"][0]["selected_action_id"] = "abstain-publication"
        self.assertTrue(any("not in the admissible set" in e for e in semantic_errors(p)))

    def test_unsupported_claim_upgrade_is_rejected(self):
        p = copy.deepcopy(self.suite)
        p["claim_limits"]["unsupported"].remove("professional validity")
        self.assertTrue(any("unsupported upgrades" in e for e in semantic_errors(p)))


if __name__ == "__main__":
    unittest.main()
