import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "pilots/pretask-procedure-transfer-v1"
spec = importlib.util.spec_from_file_location("pretask_v1_validate", STUDY / "validate.py")
assert spec is not None and spec.loader is not None
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PretaskProcedureTransferV1Tests(unittest.TestCase):
    def setUp(self):
        self.protocol = json.loads((STUDY / "protocol.json").read_text())
        self.report = json.loads((STUDY / "feasibility-report.json").read_text())

    def test_frozen_blocker_is_consistent_and_hashes_resolve(self):
        self.assertEqual([], validator.validate(self.protocol, self.report, check_paths=True))

    def test_required_treatment_removal_is_rejected(self):
        changed = copy.deepcopy(self.protocol)
        changed["treatments"].pop()
        self.assertTrue(validator.validate(changed, self.report, check_paths=False))

    def test_claim_upgrade_is_rejected(self):
        changed = copy.deepcopy(self.protocol)
        changed["claim_boundaries"]["utility"] = True
        self.assertTrue(validator.validate(changed, self.report, check_paths=False))

    def test_ineligible_family_cannot_be_laundered(self):
        changed = copy.deepcopy(self.protocol)
        changed["candidate_families"][0]["eligible_for_transfer"] = True
        self.assertTrue(validator.validate(changed, self.report, check_paths=False))

    def test_task_identifier_scrub_cannot_be_removed(self):
        changed = copy.deepcopy(self.protocol)
        changed["leakage_scrubs"]["forbidden_in_pretask_generation_inputs_and_package"].remove("is-pipeline-v1")
        self.assertTrue(validator.validate(changed, self.report, check_paths=False))

    def test_mutation_self_test(self):
        self.assertEqual([], validator.mutation_self_test(self.protocol, self.report))


if __name__ == "__main__":
    unittest.main()
