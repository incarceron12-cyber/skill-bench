from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "pilots" / "trial-accounting-reconciliation"
SPEC = importlib.util.spec_from_file_location("trial_accounting_reconcile", PACKAGE / "reconcile.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TrialAccountingReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads((PACKAGE / "expected-assignments.json").read_text())
        cls.ledger = json.loads((PACKAGE / "trial-ledger.json").read_text())

    def errors(self, manifest=None, ledger=None, *, check_paths=False):
        report = MODULE.reconcile(
            manifest or copy.deepcopy(self.manifest),
            ledger or copy.deepcopy(self.ledger),
            manifest_path=PACKAGE / "expected-assignments.json" if check_paths else None,
            check_paths=check_paths,
        )
        return report

    def test_retained_cross_shape_report_replays_exactly(self) -> None:
        report = self.errors(check_paths=True)
        retained = json.loads((PACKAGE / "reconciliation-report.json").read_text())
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(retained, report)
        self.assertEqual(8, report["funnel"]["assigned"])
        self.assertEqual(8, sum(report["funnel"]["dispositions"].values()))
        self.assertEqual(0.5, report["estimates"]["task_micro"]["value"])
        self.assertEqual(0.375, report["estimates"]["family_macro"]["value"])
        self.assertEqual(2, len({family["work_shape"] for family in self.manifest["families"]}))
        self.assertEqual(MODULE.DISPOSITIONS, set(report["funnel"]["dispositions"]))

    def test_rejects_silent_90_to_67_shrinkage(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        template = manifest["assignments"][0]
        manifest["assignments"] = [
            template | {"assignment_id": f"complex-{index:03d}", "task_id": f"complex-task-{index:03d}"}
            for index in range(1, 91)
        ]
        ledger = copy.deepcopy(self.ledger)
        ledger["manifest_sha256"] = MODULE.canonical_sha256(manifest)
        ledger["attempts"] = [
            {
                "attempt_id": f"attempt-complex-{index:03d}", "assignment_id": f"complex-{index:03d}",
                "canonical": True, "replacement_for_attempt_id": None, "started": True,
                "disposition": "valid_scored", "result": "pass" if index <= 8 else "fail",
                "exclusion_reason": None, "exclusion_evidence": None,
            }
            for index in range(1, 68)
        ]
        ledger["declared_estimates"] = [
            {"estimand": "task_micro", "numerator": 8, "denominator": 67, "value": 8 / 67},
            {"estimand": "family_macro", "family_rates": {"evidence-handoff": {"numerator": 0, "denominator": 0, "value": None}, "stateful-workflow": {"numerator": 8, "denominator": 67, "value": 8 / 67}}, "value": 8 / 67},
        ]
        report = self.errors(manifest, ledger)
        self.assertFalse(report["valid"])
        self.assertEqual(90, report["funnel"]["assigned"])
        self.assertEqual(67, report["funnel"]["canonical_dispositions"])
        self.assertEqual(23, sum("missing row for assigned attempt" in error for error in report["errors"]))
        self.assertTrue(any("does not reconcile" in error for error in report["errors"]))

    def test_rejects_duplicate_disposition_for_assignment(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        duplicate = copy.deepcopy(ledger["attempts"][0])
        duplicate["attempt_id"] = "attempt-workflow-01-duplicate"
        ledger["attempts"].append(duplicate)
        report = self.errors(ledger=ledger)
        self.assertTrue(any("exactly one canonical disposition" in error for error in report["errors"]))

    def test_rejects_unknown_unassigned_result(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        row = copy.deepcopy(ledger["attempts"][0])
        row.update(attempt_id="attempt-rogue", assignment_id="unassigned-rogue")
        ledger["attempts"].append(row)
        self.assertTrue(any("unknown/unassigned result" in error for error in self.errors(ledger=ledger)["errors"]))

    def test_rejects_missing_assignment_row(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        ledger["attempts"].pop()
        self.assertTrue(any("missing row for assigned attempt" in error for error in self.errors(ledger=ledger)["errors"]))

    def test_rejects_invalid_attempt_included_as_outcome(self) -> None:
        for disposition in ("environment_invalid", "instrument_invalid", "service_failure", "timeout", "missing_artifact", "missing_result"):
            with self.subTest(disposition=disposition):
                ledger = copy.deepcopy(self.ledger)
                ledger["attempts"][0]["disposition"] = disposition
                ledger["attempts"][0]["result"] = "pass"
                self.assertTrue(any("cannot be included as success/failure" in error for error in self.errors(ledger=ledger)["errors"]))

    def test_rejects_retry_replacement_ambiguity(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["assignments"][0]["retry_policy"] = "declared_canonical_attempt"
        ledger = copy.deepcopy(self.ledger)
        ledger["manifest_sha256"] = MODULE.canonical_sha256(manifest)
        retry = copy.deepcopy(ledger["attempts"][0])
        retry.update(attempt_id="attempt-workflow-01-retry", canonical=False, replacement_for_attempt_id=None)
        ledger["attempts"].append(retry)
        self.assertTrue(any("retry replacement chain is ambiguous" in error for error in self.errors(manifest, ledger)["errors"]))

    def test_rejects_micro_macro_conflation(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        macro = next(item for item in ledger["declared_estimates"] if item["estimand"] == "family_macro")
        macro["value"] = 0.5
        self.assertTrue(any("family_macro estimate is conflated" in error for error in self.errors(ledger=ledger)["errors"]))

    def test_rejects_manifest_and_component_hash_drift(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        ledger["manifest_sha256"] = "0" * 64
        ledger["component_locks"][0]["version"] = "drifted"
        errors = self.errors(ledger=ledger)["errors"]
        self.assertTrue(any("manifest hash/version drift" in error for error in errors))
        self.assertTrue(any("component locks drift" in error for error in errors))

    def test_justified_exclusion_requires_auditable_basis(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        row = ledger["attempts"][0]
        row.update(disposition="justified_exclusion", result=None, exclusion_reason=None, exclusion_evidence=None)
        self.assertTrue(any("needs reason and evidence locator" in error for error in self.errors(ledger=ledger)["errors"]))


if __name__ == "__main__":
    unittest.main()
