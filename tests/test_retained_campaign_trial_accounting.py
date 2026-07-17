from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "pilots/trial-accounting-reconciliation/retained-campaign-validation-v1"
SPEC = importlib.util.spec_from_file_location("retained_campaign_accounting", PACKAGE / "validate.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RetainedCampaignAccountingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace = json.loads((PACKAGE / "persistent-workspace-reuse-v3-mapping.json").read_text())
        cls.action = json.loads((PACKAGE / "action-boundary-composition-v2-mapping.json").read_text())

    def validate(self, sidecar, *, paths=False):
        return MODULE.validate_sidecar(copy.deepcopy(sidecar), check_paths=paths)

    def test_two_retained_campaigns_replay_exactly(self) -> None:
        expected = {
            "persistent-workspace-reuse-v3": {
                "intended": 24, "attempted": 24, "service_valid": 24,
                "environment_valid": 24, "artifact_valid": 24, "graded": 24, "scored": 24,
            },
            "action-boundary-composition-v2": {
                "intended": 6, "attempted": 5, "service_valid": 1,
                "environment_valid": 4, "artifact_valid": 1, "graded": 1, "scored": 0,
            },
        }
        for sidecar in (self.workspace, self.action):
            with self.subTest(campaign=sidecar["campaign_id"]):
                report = self.validate(sidecar, paths=True)
                retained = json.loads((PACKAGE / f"{sidecar['campaign_id']}-report.json").read_text())
                self.assertTrue(report["valid"], report["errors"])
                self.assertEqual(retained, report)
                for key, value in expected[sidecar["campaign_id"]].items():
                    self.assertEqual(value, report["totals"][key])
        action = self.validate(self.action)
        self.assertFalse(action["protocol_conformant"])
        self.assertEqual(["adjudicated_post_stop_launches"], action["known_adjudicated_defects"])
        self.assertEqual(0, action["totals"]["scored"])

    def test_rejects_dropped_intended_row(self) -> None:
        sidecar = copy.deepcopy(self.workspace)
        sidecar["mappings"].pop()
        errors = self.validate(sidecar)["errors"]
        self.assertTrue(any("exactly preserve frozen protocol assignment order" in item for item in errors))

    def test_rejects_complete_case_denominator_substitution(self) -> None:
        sidecar = copy.deepcopy(self.action)
        sidecar["mappings"] = [row for row in sidecar["mappings"] if row["canonical_disposition"] == "instrument_invalid"]
        sidecar["declared_totals"]["intended"] = 1
        errors = self.validate(sidecar)["errors"]
        self.assertTrue(any("frozen protocol assignment order" in item or "reconcile" in item for item in errors))

    def test_rejects_duplicate_canonical_attempt(self) -> None:
        sidecar = copy.deepcopy(self.workspace)
        sidecar["mappings"].append(copy.deepcopy(sidecar["mappings"][0]))
        errors = self.validate(sidecar)["errors"]
        self.assertTrue(any("exactly one canonical disposition" in item for item in errors))

    def test_rejects_hidden_post_stop_launch(self) -> None:
        sidecar = copy.deepcopy(self.action)
        row = next(row for row in sidecar["mappings"] if row["post_stop_launch"])
        row["post_stop_launch"] = False
        sidecar["declared_totals"]["post_stop_launches"] -= 1
        errors = self.validate(sidecar)["errors"]
        self.assertTrue(any("post-stop launch mapping mismatch" in item for item in errors))

    def test_rejects_retry_or_replacement_laundering(self) -> None:
        sidecar = copy.deepcopy(self.workspace)
        sidecar["mappings"][1]["replacement_for_attempt_id"] = sidecar["mappings"][0]["native_attempt_id"]
        errors = self.validate(sidecar)["errors"]
        self.assertTrue(any("retry/replacement is forbidden" in item for item in errors))

    def test_rejects_invalid_row_scored_as_failure(self) -> None:
        sidecar = copy.deepcopy(self.action)
        row = next(row for row in sidecar["mappings"] if row["canonical_disposition"] == "instrument_invalid")
        row.update(canonical_disposition="valid_scored", result="fail", scored=True)
        errors = self.validate(sidecar)["errors"]
        self.assertTrue(any("canonical disposition/result mismatch" in item for item in errors))
        self.assertTrue(any("cannot be scored as failure" in item for item in errors))

    def test_rejects_unjustified_exclusion(self) -> None:
        sidecar = copy.deepcopy(self.action)
        row = sidecar["mappings"][1]
        row.update(canonical_disposition="justified_exclusion", exclusion_reason=None, exclusion_evidence=None)
        errors = self.validate(sidecar)["errors"]
        self.assertTrue(any("justified exclusion needs reason and evidence locator" in item for item in errors))

    def test_rejects_parent_and_transform_hash_drift(self) -> None:
        sidecar = copy.deepcopy(self.workspace)
        sidecar["parent_locks"][0]["sha256"] = "0" * 64
        sidecar["derivation"]["transform_sha256"] = "f" * 64
        errors = self.validate(sidecar, paths=True)["errors"]
        self.assertTrue(any("parent/hash drift" in item for item in errors))
        self.assertTrue(any("transform identity/hash drift" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
