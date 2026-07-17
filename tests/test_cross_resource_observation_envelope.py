from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from scripts.validate_benchmark import DEFAULT_SCHEMA, canonical_sha256, resource_envelope_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "pilots/cross-resource-observation-envelope"
ENVELOPE_SCHEMA = ROOT / "schemas/resource-observation-envelope.schema.json"
SPEC = importlib.util.spec_from_file_location("cross_resource_replay", HERE / "replay.py")
assert SPEC is not None and SPEC.loader is not None
REPLAY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPLAY)


class CrossResourceObservationEnvelopeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.package = json.loads((HERE / "package.json").read_text(encoding="utf-8"))

    def errors(self, package):
        return resource_envelope_errors(package["task_resource_envelope"], package["trial_resource_envelope"])

    def test_package_is_schema_and_semantically_valid_without_rewriting_prior_fixture(self):
        schema = json.loads(ENVELOPE_SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual([], list(Draft202012Validator(schema).iter_errors(self.package)))
        self.assertEqual([], self.errors(self.package))
        validate_file(ROOT / "tests/fixtures/valid-benchmark-bundle.json", DEFAULT_SCHEMA, check_paths=True)

    def test_replay_detects_all_eight_plants_and_preserves_claim_ceilings(self):
        report = REPLAY.replay(self.package)
        self.assertTrue(report["all_planted_defects_detected"])
        self.assertEqual(8, len(report["planted_defects"]))
        self.assertEqual(1, report["attempted"])
        self.assertEqual(1, report["failed_attempts"])
        self.assertEqual(1, report["invalid_environment_attempts"])
        self.assertEqual(0, report["real_commits"])
        self.assertEqual({False}, set(report["claim_boundaries"].values()))

    def test_rejects_stale_observer_identity(self):
        package = copy.deepcopy(self.package)
        package["task_resource_envelope"]["observer"]["read_set"].pop()
        self.assertTrue(any("observer comparator/read-set hash is stale" in error for error in self.errors(package)))

    def test_rejects_null_semantics_laundering(self):
        package = copy.deepcopy(self.package)
        null_update = package["trial_resource_envelope"]["mutations"][0]
        null_update["after"] = null_update["before"]
        self.assertTrue(any("intentional null update was not preserved" in error for error in self.errors(package)))

    def test_rejects_escaped_background_write_laundering(self):
        package = copy.deepcopy(self.package)
        result = next(row for row in package["trial_resource_envelope"]["canary_results"] if row["canary_id"] == "table-background")
        result["observed"] = "blocked"
        self.assertTrue(any("background-canary evidence disagree" in error for error in self.errors(package)))

    def test_rejects_incomplete_or_reordered_mutation_ledger(self):
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["mutations"][1]["sequence"] = 1
        self.assertTrue(any("mutation ledger must be complete and ordered" in error for error in self.errors(package)))
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["mutations"][4]["depends_on"] = ["missing-mutation"]
        self.assertTrue(any("dependency is missing or not earlier" in error for error in self.errors(package)))

    def test_rejects_missing_non_table_and_sequence_observation_cases(self):
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["mutations"] = [m for m in package["trial_resource_envelope"]["mutations"] if m["kind"] != "increment"]
        self.assertTrue(any("sequence/global increment case is missing" in error for error in self.errors(package)))
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["mutations"] = [m for m in package["trial_resource_envelope"]["mutations"] if m["resource_id"] != "notification-cache"]
        self.assertTrue(any("non-table blob/cache effect is missing" in error for error in self.errors(package)))

    def test_rejects_ambiguity_promotion_and_undeclared_alternative(self):
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["matches"][0]["outcome"] = "accepted"
        self.assertTrue(any("ambiguous same-resource candidates must fail closed" in error for error in self.errors(package)))
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["matches"][1]["alternative_id"] = "missing-alternative"
        self.assertTrue(any("undeclared or mismatched accepted alternative" in error for error in self.errors(package)))

    def test_rejects_failed_attempt_denominator_laundering(self):
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["attempt"]["disposition"] = "eligible"
        self.assertTrue(any("attempt disposition or denominator" in error for error in self.errors(package)))

    def test_rejects_stale_or_dependency_incomplete_commit(self):
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["commit_assessment"]["decision"] = "commit"
        self.assertTrue(any("commit was not rejected" in error for error in self.errors(package)))
        package = copy.deepcopy(self.package)
        commit = package["trial_resource_envelope"]["commit_assessment"]
        commit["dependency_closure"] = True
        self.assertTrue(any("dependency-closure label does not replay" in error for error in self.errors(package)))

    def test_rejects_overall_conformance_promotion(self):
        package = copy.deepcopy(self.package)
        package["trial_resource_envelope"]["overall_disposition"] = "conformant"
        self.assertTrue(any("overall disposition does not fail closed" in error for error in self.errors(package)))

    def test_observer_hash_is_canonical_and_retained_report_is_fresh(self):
        observer = self.package["task_resource_envelope"]["observer"]
        expected = canonical_sha256({key: value for key, value in observer.items() if key != "component"})
        self.assertEqual(expected, observer["component"]["sha256"])
        retained = json.loads((HERE / "replay-report.json").read_text(encoding="utf-8"))
        self.assertEqual(retained, REPLAY.replay())


if __name__ == "__main__":
    unittest.main()
