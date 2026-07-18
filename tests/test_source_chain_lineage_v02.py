from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/source-at-state-omission-conformance"
FIXTURE = PILOT / "lineage-fixture-v0.2.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load_module("source_lineage_builder_v02", PILOT / "build_lineage_v02.py")
validator = load_module("source_lineage_validator_v02", PILOT / "validate_lineage_v02.py")


class SourceChainLineageV02Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads(FIXTURE.read_text())

    def test_builder_exactly_reproduces_frozen_fixture(self) -> None:
        self.assertEqual(self.data, builder.build())

    def test_matrix_separates_endpoint_proximity_from_chain_acceptance(self) -> None:
        report = validator.replay(self.data, ROOT)
        self.assertEqual("passed", report["status"])
        self.assertEqual(10, report["case_count"])
        self.assertEqual(2, report["shape_count"])
        self.assertEqual(6, report["close_endpoint_blocked_chains"])
        self.assertEqual(2, report["authorized_protocol_differences"])
        duplicate_rows = [row for row in report["results"] if "duplicate-report" in row["case_id"]]
        self.assertEqual({"study_map"}, {row["earliest_consequential_break"] for row in duplicate_rows})

    def test_parent_hash_drift_fails_closed(self) -> None:
        data = copy.deepcopy(self.data)
        data["immutable_parent"]["sha256"] = "0" * 64
        self.assertTrue(any("immutable_parent path/hash mismatch" in error for error in validator.semantic_errors(data, ROOT)))

    def test_dangling_or_skipped_lineage_fails_closed(self) -> None:
        data = copy.deepcopy(self.data)
        data["cases"][0]["chain"][3]["input_artifact_ids"] = ["missing-artifact"]
        errors = validator.semantic_errors(data, ROOT)
        self.assertTrue(any("cross-stage conservation failure" in error for error in errors))
        self.assertTrue(any("dangling lineage reference" in error for error in errors))

    def test_wrong_earliest_break_attribution_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        target = next(case for case in data["cases"] if "duplicate-report" in case["case_id"])
        target["expected"]["earliest_consequential_break"] = "analyze"
        self.assertTrue(any("expected earliest_consequential_break" in error for error in validator.semantic_errors(data, ROOT)))

    def test_close_endpoint_cannot_promote_compensating_errors(self) -> None:
        data = copy.deepcopy(self.data)
        target = next(case for case in data["cases"] if "compensating-errors" in case["case_id"])
        target["expected"]["stage_chain_accepted"] = True
        target["expected"]["disposition"] = "chain_valid"
        errors = validator.semantic_errors(data, ROOT)
        self.assertTrue(any("expected stage_chain_accepted" in error for error in errors))
        self.assertTrue(any("expected disposition" in error for error in errors))

    def test_unauthorized_protocol_difference_cannot_be_promoted(self) -> None:
        data = copy.deepcopy(self.data)
        target = next(case for case in data["cases"] if "authorized-protocol-difference" in case["case_id"])
        target["protocol_difference"]["authorized"] = False
        target["protocol_difference"]["authority_locator"] = None
        errors = validator.semantic_errors(data, ROOT)
        self.assertTrue(any("unauthorized protocol difference cannot be promoted" in error for error in errors))
        self.assertTrue(any("expected stage_chain_accepted" in error for error in errors))

    def test_claim_upgrade_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["claim_boundary"]["unsupported"].remove("professional validity")
        self.assertIn("claim ceiling upgrade", validator.semantic_errors(data, ROOT))


if __name__ == "__main__":
    unittest.main()
