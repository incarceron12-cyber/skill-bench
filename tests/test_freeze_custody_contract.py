import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

from scripts.validate_freeze_custody import validate_record

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures/freeze-custody/v6-v7-breach-conformance.json"
SCHEMA = ROOT / "schemas/freeze-custody.schema.json"


class FreezeCustodyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def validate_mutation(self, mutate):
        record = copy.deepcopy(self.record)
        mutate(record)
        return validate_record(record)

    def assert_rejected_with(self, mutate, phrase):
        report = self.validate_mutation(mutate)
        self.assertFalse(report["valid"])
        self.assertIn(phrase, "\n".join(report["errors"]))

    def test_schema_and_commit_bound_successor_chain_validate(self):
        report = validate_record(copy.deepcopy(self.record))
        self.assertTrue(report["valid"], report["errors"])
        self.assertEqual(report["freeze_count"], 2)
        self.assertEqual(report["adjudication_count"], 1)
        self.assertEqual(report["closure_count"], 1)
        self.assertTrue(all(value is False for value in self.record["claim_ceiling"].values()))

        result = subprocess.run(
            [sys.executable, "scripts/validate_freeze_custody.py", str(FIXTURE.relative_to(ROOT))],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["valid"])

    def test_rejects_in_place_frozen_byte_reidentification(self):
        def mutate(record):
            binding = record["freezes"][0]["bindings"][2]
            successor = record["freezes"][1]["bindings"][2]
            binding.update({key: successor[key] for key in ("git_oid", "bytes", "sha256")})

        self.assert_rejected_with(mutate, "frozen Git object drift")

    def test_rejects_refreshing_the_audited_manifest_identity(self):
        def mutate(record):
            original = record["freezes"][0]["bindings"][0]
            refreshed = record["freezes"][1]["bindings"][0]
            original.update({key: refreshed[key] for key in ("git_oid", "bytes", "sha256")})

        self.assert_rejected_with(mutate, "frozen Git object drift")

    def test_rejects_omitted_changed_binding(self):
        def mutate(record):
            record["adjudications"][0]["changed_bound_paths"].remove(
                "pilots/pretask-procedure-transfer-v6/preflight.py"
            )

        self.assert_rejected_with(mutate, "omitted or extra changed bindings")

    def test_rejects_replacing_a_failed_observed_gate_with_pass(self):
        def mutate(record):
            record["freezes"][0]["observed_gate_states"][0]["outcome"] = "PASS"

        self.assert_rejected_with(mutate, "gate-state replacement")

    def test_rejects_execution_closure_against_post_hoc_manifest(self):
        def mutate(record):
            record["execution_closures"][0]["manifest_git_blob"] = \
                record["freezes"][1]["bindings"][0]["git_oid"]

        self.assert_rejected_with(mutate, "post-hoc or different manifest")

    def test_historical_bytes_remain_reconstructable_while_head_differs(self):
        old_commit = self.record["freezes"][0]["snapshot"]["git_commit"]
        path = "pilots/pretask-procedure-transfer-v6/canary-report.json"
        historical = subprocess.run(
            ["git", "show", f"{old_commit}:{path}"], cwd=ROOT, check=True, capture_output=True
        ).stdout
        current = (ROOT / path).read_bytes()
        self.assertNotEqual(historical, current)
        self.assertEqual(json.loads(historical)["status"], "FAIL")
        self.assertEqual(json.loads(current)["status"], "PASS")
        self.assertEqual(
            self.record["freezes"][1]["predecessor_freeze_id"],
            self.record["freezes"][0]["freeze_id"],
        )


if __name__ == "__main__":
    unittest.main()
