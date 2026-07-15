from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots" / "synthetic-api-transition-transport"
sys.path.insert(0, str(PILOT))
spec = importlib.util.spec_from_file_location("transition_transport_run", PILOT / "run.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SyntheticApiTransitionTransportTests(unittest.TestCase):
    def setUp(self):
        self.suite = json.loads((PILOT / "suite.json").read_text())

    def test_frozen_seven_case_replay_and_expected_transport(self):
        report = module.build_report(self.suite)
        adapters = {row["adapter"]: row for row in report["adapters"]}
        self.assertEqual(7, adapters["reference-rfc-derived"]["summary"]["strict_passes"])
        self.assertEqual(3, adapters["synthetic-simplified"]["summary"]["strict_passes"])
        self.assertEqual(3, report["transport"]["strict_cases_transporting"])
        self.assertEqual(7, report["transport"]["strict_cases_total"])
        self.assertEqual(17, report["transport"]["criteria_transporting"])
        self.assertEqual(27, report["transport"]["criteria_total"])

    def test_committed_report_is_exact_replay(self):
        expected = json.loads((PILOT / "report.json").read_text())
        self.assertEqual(expected, module.build_report(self.suite))

    def test_reference_fails_closed_if_stale_write_is_expected_to_win(self):
        changed = copy.deepcopy(self.suite)
        case = next(c for c in changed["cases"] if c["id"] == "concurrent-lost-update")
        case["criteria"][0]["expected"] = [200, 200]
        with self.assertRaisesRegex(ValueError, "reference adapter"):
            module.build_report(changed)

    def test_unknown_criterion_cannot_be_silently_ignored(self):
        changed = copy.deepcopy(self.suite)
        changed["cases"][0]["criteria"][0]["kind"] = "unobserved_magic"
        with self.assertRaisesRegex(ValueError, "unknown criterion"):
            module.build_report(changed)

    def test_every_realized_state_change_has_declared_observer_coverage(self):
        report = module.build_report(self.suite)
        for adapter in report["adapters"]:
            for case in adapter["cases"]:
                self.assertEqual([], case["observer_coverage"]["uncovered_changed_paths"], (adapter["adapter"], case["case_id"]))

    def test_provenance_hashes_match_fetched_primary_sources(self):
        provenance = json.loads((PILOT / "provenance.json").read_text())
        expected = {
            "RFC 9110: HTTP Semantics": "21c1cdce6ab0e5509b04d84a28000836c7a087cf786efe6f04877ebfff47232a",
            "RFC 7396: JSON Merge Patch": "545e1d61667c243ea14d6b1a56212370a26d46e1acd441803805fcdecd9164c6",
            "RFC 6750: OAuth 2.0 Bearer Token Usage": "9dc385cf4ecdd85024e5a95e447ede9230e11700bf35251906b25b37557d604b",
        }
        self.assertEqual(expected, {s["title"]: s["sha256"] for s in provenance["sources"] if "sha256" in s})


if __name__ == "__main__":
    unittest.main()
