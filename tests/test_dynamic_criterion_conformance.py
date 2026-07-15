import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_dynamic_criteria import (
    DEFAULT_FIXTURE,
    DEFAULT_INSTANCE_FIXTURE,
    grade,
    validate,
    validate_instance_conformance,
)


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


class CrossInstanceConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = json.loads(DEFAULT_INSTANCE_FIXTURE.read_text())

    def mutated_report(self, mutate):
        package = copy.deepcopy(self.package)
        mutate(package)
        with tempfile.NamedTemporaryFile("w", suffix=".json", dir=DEFAULT_INSTANCE_FIXTURE.parent, delete=False) as handle:
            json.dump(package, handle)
            path = Path(handle.name)
        try:
            return validate_instance_conformance(path)
        finally:
            path.unlink(missing_ok=True)

    def test_fixture_hashes_provenance_and_planted_assignments(self):
        report = validate_instance_conformance(check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual([item["conformant"] for item in report["results"]], [True, False, False, True])
        self.assertTrue(report["results"][1]["issues"])
        self.assertTrue(report["results"][2]["issues"])

    def test_nearby_rubric_swap_fails_closed(self):
        def mutate(package):
            package["assignments"][0]["rubric"] = package["assignments"][1]["rubric"]
        report = self.mutated_report(mutate)
        self.assertTrue(report["valid"], report["errors"])
        self.assertFalse(report["results"][0]["conformant"])
        self.assertTrue(any(issue["role"] == "rubric" for issue in report["results"][0]["issues"]))

    def test_same_work_shape_instance_swap_fails_closed(self):
        def mutate(package):
            package["assignments"][3]["rubric"] = package["assignments"][2]["rubric"]
        report = self.mutated_report(mutate)
        self.assertTrue(report["valid"], report["errors"])
        self.assertFalse(report["results"][3]["conformant"])
        self.assertGreaterEqual(len(report["results"][3]["issues"]), 2)

    def test_source_swap_fails_without_assignment_label_or_payload_cues(self):
        def mutate(package):
            package["assignments"][3]["id"] = "renamed"
            package["assignments"][3]["source"] = package["assignments"][0]["source"]
        report = self.mutated_report(mutate)
        self.assertTrue(report["valid"], report["errors"])
        self.assertFalse(report["results"][3]["conformant"])
        self.assertTrue(all(issue["role"] == "source" for issue in report["results"][3]["issues"]))

    def test_alternate_representation_is_admitted(self):
        report = validate_instance_conformance()
        self.assertTrue(report["results"][3]["conformant"])
        reference_id = self.package["assignments"][3]["reference"]
        reference = next(item for item in self.package["components"] if item["id"] == reference_id)
        self.assertIn(("representation", "text/html"), {(item["dimension"], item["value"]) for item in reference["predicates"]})

    def test_payload_hash_tampering_invalidates_package(self):
        report = self.mutated_report(lambda package: package["components"][0].update(payload="tampered"))
        self.assertFalse(report["valid"])
        self.assertTrue(any("payload hash mismatch" in error for error in report["errors"]))

    def test_task_requirement_must_be_grounded(self):
        def mutate(package):
            package["components"][0]["requirements"][0]["value"] = "unbound:value"
        report = self.mutated_report(mutate)
        self.assertFalse(report["valid"])
        self.assertTrue(any("not grounded" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
