from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/source-at-state-omission-conformance"
FIXTURE = PILOT / "fixture.json"
SPEC = importlib.util.spec_from_file_location("source_at_state_validate", PILOT / "validate.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class SourceAtStateOmissionConformanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads(FIXTURE.read_text())

    def test_frozen_matrix_replays_across_two_unlike_shapes(self) -> None:
        report = module.replay(self.data, ROOT)
        self.assertEqual("passed", report["status"])
        self.assertEqual(26, report["matrix_cells"])
        self.assertEqual(2, len(report["work_shapes"]))
        self.assertEqual(2, report["invalid_cells"])
        self.assertEqual("none_noncompensatory_vector", report["effect_aggregation"])

    def test_transition_omission_preserves_harm_despite_effort_gain(self) -> None:
        report = module.replay(self.data, ROOT)
        row = next(r for r in report["results"] if r["shape_id"] == "procurement-memo" and r["condition_id"] == "omit-transition")
        self.assertEqual({"final_acceptance": 1, "next_operation_valid": 1, "safety_preserved": 1, "effort_units": -2}, row["effect"]["vector"])

    def test_single_omission_and_joint_omission_are_not_equivalent(self) -> None:
        report = module.replay(self.data, ROOT)
        rows = {r["condition_id"]: r for r in report["results"] if r["shape_id"] == "incident-brief"}
        self.assertEqual(0, rows["omit-terminal-single"]["effect"]["vector"]["final_acceptance"])
        self.assertEqual(1, rows["omit-terminal-and-substitutes"]["effect"]["vector"]["final_acceptance"])

    def test_source_hash_mutation_fails_closed(self) -> None:
        data = copy.deepcopy(self.data)
        data["scenarios"][0]["sources"][0]["content"] += " mutated"
        self.assertTrue(any("source content hash/length mismatch" in e for e in module.semantic_errors(data, ROOT)))

    def test_context_hash_mutation_fails_closed(self) -> None:
        data = copy.deepcopy(self.data)
        data["scenarios"][0]["conditions"][3]["realized_context_sha256"] = "0" * 64
        self.assertTrue(any("realized context hash mismatch" in e for e in module.semantic_errors(data, ROOT)))

    def test_replay_noise_is_not_zero_effect(self) -> None:
        data = copy.deepcopy(self.data)
        replay = next(c for c in data["scenarios"][0]["conditions"] if c["condition_id"] == "unchanged-replay-2")
        replay["outcome"]["effort_units"] += 1
        self.assertTrue(any("unchanged replay noise gate failed" in e for e in module.semantic_errors(data, ROOT)))

    def test_invalid_state_cannot_be_scored_as_zero_effect(self) -> None:
        data = copy.deepcopy(self.data)
        cell = next(c for c in data["scenarios"][0]["conditions"] if c["condition_id"] == "missing-post-state")
        cell["outcome"]["final_acceptance"] = False
        self.assertTrue(any("invalid state must not carry effect values" in e for e in module.semantic_errors(data, ROOT)))

    def test_neutral_replacement_must_preserve_length(self) -> None:
        data = copy.deepcopy(self.data)
        neutral = next(s for s in data["scenarios"][0]["sources"] if s["role_at_state"] == "neutral_control")
        neutral["byte_length"] += 1
        errors = module.semantic_errors(data, ROOT)
        self.assertTrue(any("neutral replacement is not length preserving" in e for e in errors))

    def test_claim_upgrade_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["claim_boundary"]["unsupported"].remove("portable document utility")
        self.assertTrue(any("required unsupported claim missing" in e for e in module.semantic_errors(data, ROOT)))


if __name__ == "__main__":
    unittest.main()
