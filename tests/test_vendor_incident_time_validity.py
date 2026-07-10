from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRADER = ROOT / "pilots/vendor-incident-response/grade_v2.py"
spec = importlib.util.spec_from_file_location("vendor_incident_grade_v2", GRADER)
grade_v2 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(grade_v2)

STATUS = {
    "issued_at": "2026-07-10T15:00:00Z",
    "valid_until": "2026-07-11T15:00:00Z",
}


def context(value: str, authority: str = "benchmark_instrument") -> dict:
    return {"authority": authority, "evaluation_time": value}


class VendorIncidentTemporalBoundaryTests(unittest.TestCase):
    def test_missing_time_is_invalid_environment(self) -> None:
        result = grade_v2.assess_temporal_context(STATUS, [])
        self.assertEqual("invalid_environment", result["state"])
        self.assertEqual("missing_authoritative_evaluation_time", result["reason"])

    def test_conflicting_times_are_invalid_environment(self) -> None:
        result = grade_v2.assess_temporal_context(
            STATUS, [context("2026-07-10T18:00:00Z"), context("2026-07-10T19:00:00Z")]
        )
        self.assertEqual("invalid_environment", result["state"])
        self.assertEqual("conflicting_authoritative_evaluation_times", result["reason"])

    def test_before_window_is_outside_not_environment_invalid(self) -> None:
        result = grade_v2.assess_temporal_context(STATUS, [context("2026-07-10T14:59:59Z")])
        self.assertEqual("outside_validity_window", result["state"])
        self.assertEqual("evaluation_time_before_issued_at", result["reason"])

    def test_within_window_including_boundaries_is_applicable(self) -> None:
        for value in ("2026-07-10T15:00:00Z", "2026-07-10T18:00:00Z", "2026-07-11T15:00:00Z"):
            with self.subTest(value=value):
                result = grade_v2.assess_temporal_context(STATUS, [context(value)])
                self.assertEqual("within_validity_window", result["state"])

    def test_expired_time_is_outside_not_environment_invalid(self) -> None:
        result = grade_v2.assess_temporal_context(STATUS, [context("2026-07-11T15:00:01Z")])
        self.assertEqual("outside_validity_window", result["state"])
        self.assertEqual("evaluation_time_after_valid_until", result["reason"])

    def test_malformed_time_is_invalid_environment(self) -> None:
        result = grade_v2.assess_temporal_context(STATUS, [context("not-a-time")])
        self.assertEqual("invalid_environment", result["state"])
        self.assertEqual("malformed_temporal_input", result["reason"])


if __name__ == "__main__":
    unittest.main()
