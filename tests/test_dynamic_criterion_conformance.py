import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_dynamic_criteria import DEFAULT_FIXTURE, grade, validate


class DynamicCriterionConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = json.loads(DEFAULT_FIXTURE.read_text())
        cls.cases = {case["id"]: case for case in cls.package["cases"]}

    def mutated_report(self, mutate):
        package = copy.deepcopy(self.package)
        mutate(package)
        with tempfile.NamedTemporaryFile("w", suffix=".json", dir=DEFAULT_FIXTURE.parent, delete=False) as handle:
            json.dump(package, handle)
            path = Path(handle.name)
        try:
            return validate(path)
        finally:
            path.unlink(missing_ok=True)

    def test_fixture_and_provenance_validate(self):
        report = validate(check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(len(report["results"]), 2)

    def test_missing_trigger_fails(self):
        report = self.mutated_report(lambda p: p["cases"][0]["contingent"][0]["trigger"].update(locator=""))
        self.assertFalse(report["valid"])
        self.assertTrue(any("lacks supported trigger" in error for error in report["errors"]))

    def test_irrelevant_edit_criterion_drift_fails(self):
        report = self.mutated_report(lambda p: p["cases"][1]["irrelevant_edit"]["expected_contingent_ids"].pop())
        self.assertFalse(report["valid"])
        self.assertTrue(any("criterion-set drift" in error for error in report["errors"]))

    def test_duplicate_is_not_double_counted(self):
        result = grade(self.cases["supplier-memo"])
        self.assertNotIn("c-duplicate", result["counted_contingent_ids"])
        self.assertEqual(result["contingent"], {"contradicted": 2, "not_applicable": 1})

    def test_absent_verifier_fails_closed(self):
        result = grade(self.cases["lab-notebook"])
        self.assertEqual(result["contingent"]["insufficient_evidence"], 1)
        self.assertEqual(result["capability_evidence"], "blocked")

    def test_legitimate_not_applicable_abstains(self):
        result = grade(self.cases["supplier-memo"])
        self.assertEqual(result["contingent"]["not_applicable"], 1)

    def test_not_applicable_cannot_be_scored_supported(self):
        def mutate(package):
            package["cases"][0]["contingent"][3]["outcome"] = "supported"
        report = self.mutated_report(mutate)
        self.assertFalse(report["valid"])
        self.assertTrue(any("must abstain" in error for error in report["errors"]))

    def test_claim_boundary_cannot_be_removed(self):
        report = self.mutated_report(lambda p: p["claim_limits"]["unsupported"].remove("expert validity"))
        self.assertFalse(report["valid"])
        self.assertTrue(any("claim limits" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
