import copy
import json
import unittest
from pathlib import Path

from scripts.validate_released_procedure_adapters import build_report, validate_adapter

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "pilots/procedure-package-released-validation"
SOP = BASE / "sop-bench-aircraft-inspection.adapter.json"
ANCHOR = BASE / "anchor-2000.adapter.json"


class ReleasedProcedureAdapterTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_both_frozen_adapters_validate_and_fail_closed(self):
        sop = build_report(SOP)
        anchor = build_report(ANCHOR)
        self.assertTrue(sop["adapter_valid"], sop["errors"])
        self.assertTrue(anchor["adapter_valid"], anchor["errors"])
        self.assertEqual("reject", sop["conformance_outcome"])
        self.assertEqual("reject", anchor["conformance_outcome"])

    def test_sop_runtime_dependency_gap_is_not_silently_substituted(self):
        replay = build_report(SOP)["runtime_replay"]
        self.assertFalse(replay["available"])
        self.assertIsNone(replay["deterministic"])
        self.assertIn("pandas", replay["reason"])

    def test_mutated_source_hash_is_rejected(self):
        adapter = self.load(ANCHOR)
        adapter["source_files"][0]["sha256"] = "0" * 64
        self.assertIn("source path/hash mismatch", "\n".join(validate_adapter(adapter)))

    def test_role_mapping_cannot_be_dropped(self):
        adapter = self.load(SOP)
        del adapter["role_mappings"]["prohibited_oracle"]
        self.assertIn("six procedure-package roles", "\n".join(validate_adapter(adapter)))

    def test_claim_ceiling_cannot_be_upgraded(self):
        adapter = self.load(ANCHOR)
        adapter["claim_limits"].remove("professional correctness")
        self.assertIn("claim ceilings", "\n".join(validate_adapter(adapter)))

    def test_fail_closed_outcome_cannot_be_promoted(self):
        adapter = self.load(ANCHOR)
        adapter["expected_conformance"] = "pass"
        self.assertIn("fail closed as reject", "\n".join(validate_adapter(adapter)))


if __name__ == "__main__":
    unittest.main()
