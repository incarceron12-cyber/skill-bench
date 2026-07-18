from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

from scripts.validate_clean_release import validate_release

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIR = ROOT / "pilots/priced-resource-accounting-conformance"
SPEC = importlib.util.spec_from_file_location("priced_resource_replay", PACKAGE_DIR / "replay.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PricedResourceAccountingConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.package = json.loads((PACKAGE_DIR / "package.json").read_text())
        cls.rates = json.loads((PACKAGE_DIR / "rate-sheet.json").read_text())

    def report(self, package=None, rates=None, *, check_paths=False):
        return MODULE.replay(copy.deepcopy(package or self.package), copy.deepcopy(rates or self.rates), check_paths=check_paths)

    def test_retained_cross_shape_report_replays_and_preserves_distinctions(self):
        report = self.report(check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(report, json.loads((PACKAGE_DIR / "replay-report.json").read_text()))
        self.assertEqual(MODULE.REQUIRED_BASES, set(report["price_bases_observed"]))
        self.assertTrue(all(report["planted_distinctions"][key] for key in (
            "higher_cap_lower_spend", "failed_retry_separate_from_retained_valid_cost",
            "cached_counterfactual_separate_from_charge", "denominator_rank_reversal",
        )))
        self.assertIsNone(report["planted_distinctions"]["one_dimensional_rank"])

    def test_every_attempt_and_resource_family_reconciles(self):
        report = self.report()
        incident = report["campaigns"]["incident-evidence-review"]
        sheet = report["campaigns"]["spreadsheet-reconciliation"]
        self.assertEqual((2, 1, 1), (incident["attempt_count"], incident["canonical_valid_count"], incident["success_count"]))
        self.assertEqual((6.0, 2.0), (incident["campaign_charged_spend"], incident["retained_valid_charged_spend"]))
        self.assertEqual((3, 3, 2), (sheet["attempt_count"], sheet["canonical_valid_count"], sheet["success_count"]))
        self.assertEqual({"external_tool", "human_review", "infrastructure", "model_inference"}, set(report["resource_families_observed"]))

    def test_rejects_failed_retry_deleted_from_campaign(self):
        package = copy.deepcopy(self.package)
        package["attempts"] = [row for row in package["attempts"] if row["attempt_id"] != "incident-01-initial"]
        errors = self.report(package)["errors"]
        self.assertTrue(any("retry chain missing" in error for error in errors))
        self.assertTrue(any("higher-cap/lower-spend" in error or "failed retry" in error for error in errors))

    def test_rejects_counterfactual_or_estimate_as_realized_charge(self):
        for basis in ("cached_counterfactual", "amortized_estimate", "human_estimate"):
            with self.subTest(basis=basis):
                package = copy.deepcopy(self.package)
                row = next(resource for attempt in package["attempts"] for resource in attempt["resources"] if resource["price_basis"] == basis)
                row["charged_spend"] = row["priced_amount"]
                self.assertTrue(any("laundered into realized charge" in error or "omitted/transferred" in error for error in self.report(package)["errors"]))

    def test_rejects_rate_basis_and_quantity_drift(self):
        package = copy.deepcopy(self.package)
        resource = package["attempts"][1]["resources"][0]
        resource["priced_amount"] = 99
        self.assertTrue(any("priced amount does not replay" in error for error in self.report(package)["errors"]))
        package = copy.deepcopy(self.package)
        package["attempts"][1]["resources"][0]["price_basis"] = "realized_ledger"
        self.assertTrue(any("price-basis drift" in error for error in self.report(package)["errors"]))

    def test_rejects_one_dimensional_rank_and_denominator_conflation(self):
        package = copy.deepcopy(self.package)
        package["report_policy"]["one_dimensional_cost_rank"] = ["system-higher-cap", "system-lower-cap"]
        self.assertTrue(any("one-dimensional cost ranking" in error for error in self.report(package)["errors"]))
        package = copy.deepcopy(self.package)
        package["denominator_policies"].pop()
        self.assertTrue(any("denominator policies" in error for error in self.report(package)["errors"]))

    def test_blocks_efficiency_utility_operational_fit_risk_and_total_cost(self):
        for claim in MODULE.BLOCKED_CLAIMS:
            with self.subTest(claim=claim):
                package = copy.deepcopy(self.package)
                package["claim_assertions"][claim] = True
                self.assertTrue(any(f"unsupported claim upgrade: {claim}" in error for error in self.report(package)["errors"]))

    def test_rejects_fabricated_stakeholder_consequence(self):
        package = copy.deepcopy(self.package)
        consequence = package["campaigns"][0]["consequence_observation"]
        consequence.update(observed=True, stakeholder_artifact_accepted=True)
        self.assertTrue(any("laundered into stakeholder consequence" in error for error in self.report(package)["errors"]))

    def test_rejects_source_hash_drift(self):
        package = copy.deepcopy(self.package)
        package["component_locks"][0]["sha256"] = "0" * 64
        self.assertTrue(any("locked source hash drift" in error for error in self.report(package, check_paths=True)["errors"]))

    def test_clean_release_manifest_runs_both_zero_call_controls(self):
        observed = validate_release(PACKAGE_DIR / "clean-release-manifest.json")
        retained = json.loads((PACKAGE_DIR / "clean-release-report.json").read_text())
        self.assertTrue(observed["passed"], observed["errors"])
        self.assertEqual(retained, observed)
        self.assertEqual(2, len(observed["control_results"]))
        self.assertTrue(all(row["passed"] for row in observed["control_results"]))


if __name__ == "__main__":
    unittest.main()
