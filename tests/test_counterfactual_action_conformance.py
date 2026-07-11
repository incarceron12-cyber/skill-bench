import copy
import json
import unittest
from pathlib import Path

from scripts.grade_counterfactual_actions import DEFAULT_CORPUS, grade, validate_and_grade


class CounterfactualActionConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = json.loads(DEFAULT_CORPUS.read_text())
        cls.patterns = {p["id"]: p for p in cls.package["source_patterns"]}

    def test_corpus_replays_with_provenance(self):
        report = validate_and_grade(check_paths=True)
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(len(report["results"]), 11)

    def test_semantic_refusal_survives_lexical_false_reject(self):
        case = next(c for c in self.package["cases"] if c["id"] == "semantic-refusal-lexical-miss")
        result = grade(case, self.patterns[case["pattern"]])
        self.assertEqual(result["outcome"], "pass")
        self.assertFalse(result["lexical_refusal"])

    def test_matched_control_rejects_blanket_refusal(self):
        case = next(c for c in self.package["cases"] if c["id"] == "unsupported-refusal")
        result = grade(case, self.patterns[case["pattern"]])
        self.assertEqual(result["dimensions"]["action_selection"], "fail")
        self.assertEqual(result["outcome"], "fail")

    def test_state_and_action_are_separate(self):
        case = next(c for c in self.package["cases"] if c["id"] == "state-preservation-failure")
        result = grade(case, self.patterns[case["pattern"]])
        self.assertEqual(result["dimensions"]["action_selection"], "pass")
        self.assertEqual(result["dimensions"]["artifact_state"], "fail")

    def test_missing_and_invalid_views_fail_closed(self):
        results = {r["case_id"]: r for r in validate_and_grade()["results"]}
        self.assertEqual(results["missing-state-view"]["outcome"], "insufficient_evidence")
        self.assertEqual(results["invalid-export"]["outcome"], "invalid_artifact")

    def test_claim_limit_removal_is_rejected(self):
        package = copy.deepcopy(self.package)
        package["claim_limits"]["unsupported"].remove("professional validity")
        temporary = DEFAULT_CORPUS.parent / ".invalid-claims.json"
        try:
            temporary.write_text(json.dumps(package))
            report = validate_and_grade(temporary)
            self.assertFalse(report["valid"])
            self.assertTrue(any("claim limits" in error for error in report["errors"]))
        finally:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
