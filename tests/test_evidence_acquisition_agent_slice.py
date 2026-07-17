from __future__ import annotations
import importlib.util
import json
import unittest
from pathlib import Path

from scripts.validate_evidence_acquisition_historical import validate_file

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/evidence-acquisition-matched-agent-v1"


def load_module():
    spec = importlib.util.spec_from_file_location("evidence_agent_slice", PILOT / "run_study.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class EvidenceAcquisitionAgentSliceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.runner = load_module()
        cls.report = json.loads((PILOT / "execution/study-report.json").read_text())

    def test_frozen_protocol_and_preflight_remain_valid(self) -> None:
        self.assertTrue(self.runner.verify_protocol(False)["passed"])
        canary = json.loads((PILOT / "preflight/canary-report.json").read_text())
        self.assertTrue(canary["passed"])
        self.assertEqual(0, canary["model_calls"])

    def test_execution_replays_and_preserves_all_denominators(self) -> None:
        rebuilt = self.runner.replay()
        self.assertEqual(self.report, rebuilt)
        self.assertEqual({"intended": 12, "service_valid": 12, "environment_valid": 12, "artifact_valid": 12}, rebuilt["denominators"])
        self.assertTrue(rebuilt["no_pooled_effect"])

    def test_both_repeat_packages_validate_with_hashes(self) -> None:
        for repeat in (1, 2):
            validate_file(PILOT / f"execution/episode-repeat-{repeat}.json", check_paths=True)

    def test_active_parser_failure_signature_is_retained_not_retried(self) -> None:
        cell = self.report["shapes_reported_separately"]["segment-release"]["active"]
        self.assertEqual([2, 2], cell["inquiry_selection"]["request_counts"])
        self.assertEqual([1, 0], cell["access"]["released_counts"])
        self.assertEqual([1, 2], cell["severe_omission"]["counts"])
        for attempt_id in cell["attempt_ids"]:
            attempt = json.loads((PILOT / "execution/attempts" / attempt_id / "trial-report.json").read_text())
            self.assertEqual(1, attempt["launcher_invocations"] - 2)
            self.assertTrue(any(event["status"] == "ambiguous" for event in attempt["access_events"]))


if __name__ == "__main__":
    unittest.main()
