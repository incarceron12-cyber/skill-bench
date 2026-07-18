from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V7 = ROOT / "pilots/pretask-procedure-transfer-v7"


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec); spec.loader.exec_module(value)
    return value


def load(path: Path):
    return json.loads(path.read_text())


oracle = module("v7_oracle_tests", V7 / "oracle.py")
checker = module("v7_checker_tests", V7 / "checkers/check_endpoint.py")
builder = module("v7_builder_tests", V7 / "prepare_freeze.py")
preflight = module("v7_preflight_tests", V7 / "preflight.py")


def zeta(events):
    return {"family_id": "family-zeta", "journal_id": "probe", "events": events}


class PretaskProcedureTransferV7Tests(unittest.TestCase):
    def test_builder_oracle_and_frozen_endpoints_agree_independently(self):
        for task_id in ("k4n7", "p9c2", "t6v1", "w3d8"):
            case = load(V7 / f"tasks/{task_id}/input.json")
            private = load(V7 / f"tasks/{task_id}/private.json")
            built, independent = builder.expected(task_id, case), oracle.derive(task_id, case)
            if case["family_id"] == "family-epsilon":
                for value in (built, independent, private["expected_semantics"]):
                    for row in value["decisions"]: row["reason"] = "normalized"
            else:
                for value in (built, independent, private["expected_semantics"]): value["reason"] = "normalized"
            self.assertEqual(built, independent, task_id)
            self.assertEqual(independent, private["expected_semantics"], task_id)

    def test_zp3_ancestor_rollback_is_descendant_then_target(self):
        case = zeta([
            {"seq": 1, "operation": "begin", "transaction": "A"},
            {"seq": 2, "operation": "begin", "transaction": "B"},
            {"seq": 3, "operation": "set", "key": "x", "value": 1},
            {"seq": 4, "operation": "rollback", "transaction": "A"},
        ])
        result = oracle.derive_zeta("probe", case)
        self.assertTrue(result["valid"])
        self.assertEqual(["B", "A"], result["rolled_back_transactions"])
        self.assertEqual({}, result["final_state"])

    def test_zeta_source_targeted_invalid_structures(self):
        probes = {
            "duplicate_transaction": [
                {"seq": 1, "operation": "begin", "transaction": "A"},
                {"seq": 2, "operation": "rollback", "transaction": "A"},
                {"seq": 3, "operation": "begin", "transaction": "A"},
                {"seq": 4, "operation": "commit", "transaction": "A"}],
            "ancestor_commit": [
                {"seq": 1, "operation": "begin", "transaction": "A"},
                {"seq": 2, "operation": "begin", "transaction": "B"},
                {"seq": 3, "operation": "commit", "transaction": "A"}],
            "unmatched_close": [{"seq": 1, "operation": "commit", "transaction": "A"}],
            "duplicate_seq": [
                {"seq": 1, "operation": "begin", "transaction": "A"},
                {"seq": 1, "operation": "commit", "transaction": "A"}],
        }
        for name, events in probes.items():
            with self.subTest(name=name):
                result = oracle.derive_zeta(name, zeta(events))
                self.assertFalse(result["valid"])
                self.assertIsNone(result["final_state"])

    def test_zeta_repeated_keys_overwrite_in_sequence(self):
        case = zeta([
            {"seq": 1, "operation": "begin", "transaction": "A"},
            {"seq": 2, "operation": "set", "key": "x", "value": 1},
            {"seq": 3, "operation": "set", "key": "x", "value": 2},
            {"seq": 4, "operation": "commit", "transaction": "A"},
        ])
        self.assertEqual({"x": 2}, oracle.derive_zeta("probe", case)["final_state"])

    def test_epsilon_threshold_and_authority_precedence(self):
        base = {"family_id": "family-epsilon", "review_hour": 100,
                "batches": [{"batch_id": "B", "required_seals": ["s"]}],
                "observations": [{"observation_id": "signed", "batch_id": "B", "record_type": "signed_scan", "seal": "s", "state": "broken", "hour": 76},
                                 {"observation_id": "note", "batch_id": "B", "record_type": "unsigned_note", "seal": "s", "state": "intact", "hour": 99}]}
        self.assertEqual("quarantine", oracle.derive_epsilon("boundary", base)["decisions"][0]["disposition"])
        expired = copy.deepcopy(base); expired["observations"][0]["hour"] = 75
        result = oracle.derive_epsilon("expired", expired)["decisions"][0]
        self.assertEqual("release", result["disposition"])
        self.assertEqual({"s": "note"}, result["controlling_seals"])

    def test_checker_accepts_only_declared_valid_variants(self):
        for task_id in ("k4n7", "p9c2", "t6v1", "w3d8"):
            private = load(V7 / f"tasks/{task_id}/private.json")
            candidate = copy.deepcopy(private["expected_semantics"])
            if private["family_id"] == "family-epsilon":
                candidate["decisions"].reverse()
                for row in candidate["decisions"]:
                    row["observation_ids"].reverse(); row["reason"] = "  paraphrase  "
            else:
                candidate["reason"] = "  paraphrase  "
            reparsed = checker.loads_strict(json.dumps(candidate, sort_keys=True, indent=7))
            self.assertTrue(checker.compare(reparsed, private)[0], task_id)

    def test_closed_keys_reject_condition_and_nested_payloads(self):
        for task_id in ("k4n7", "t6v1"):
            private = load(V7 / f"tasks/{task_id}/private.json")
            candidate = copy.deepcopy(private["expected_semantics"])
            candidate["condition_id"] = "reference_procedure"
            self.assertFalse(checker.compare(candidate, private)[0])
            candidate.pop("condition_id"); candidate["uncontracted_payload"] = {"hint": True}
            self.assertFalse(checker.compare(candidate, private)[0])
            if private["family_id"] == "family-epsilon":
                candidate.pop("uncontracted_payload"); candidate["decisions"][0]["extra"] = None
                self.assertFalse(checker.compare(candidate, private)[0])

    def test_repeated_json_object_key_is_rejected(self):
        with self.assertRaises(checker.DuplicateKey):
            checker.loads_strict('{"task_id":"a","task_id":"b","decisions":[]}')
        private = V7 / "tasks/k4n7/private.json"
        with tempfile.TemporaryDirectory() as tmp:
            candidate = Path(tmp) / "result.json"
            candidate.write_text('{"task_id":"k4n7","task_id":"p9c2","decisions":[]}')
            proc = subprocess.run([sys.executable, str(V7 / "checkers/check_endpoint.py"), "--candidate", str(candidate), "--private", str(private)], capture_output=True, text=True)
            self.assertNotEqual(0, proc.returncode)
            self.assertFalse(json.loads(proc.stdout)["passed"])

    def test_recursive_json_type_collisions_fail(self):
        private = load(V7 / "tasks/t6v1/private.json")
        canonical = private["expected_semantics"]
        mutations = []
        for value in (True, False, 0, 1.0, None, {"nested": 1}):
            candidate = copy.deepcopy(canonical); candidate["final_state"]["x"] = value; mutations.append(candidate)
        candidate = copy.deepcopy(canonical); candidate["valid"] = 1; mutations.append(candidate)
        for candidate in mutations:
            self.assertFalse(checker.compare(candidate, private)[0], candidate)
        invalid_private = load(V7 / "tasks/w3d8/private.json")
        candidate = copy.deepcopy(invalid_private["expected_semantics"]); candidate["valid"] = 0
        self.assertFalse(checker.compare(candidate, invalid_private)[0])
        candidate = copy.deepcopy(invalid_private["expected_semantics"]); candidate["final_state"] = {}
        self.assertFalse(checker.compare(candidate, invalid_private)[0])

    def test_source_applicability_is_proposition_bound_and_v7_only(self):
        record = load(V7 / "source-applicability.json")
        self.assertEqual("v7 only", record["valid_time"])
        self.assertFalse(record["supersedes_or_edits_v4_authority"])
        self.assertEqual(8, len(record["proposition_lineage"]))
        self.assertTrue(all(row["source_valid_time_retained"] == "v4 only" for row in record["proposition_lineage"]))
        parent = record["parent_authority"]
        self.assertEqual("pilots/pretask-procedure-transfer-v6/source-applicability.json", parent["path"])
        self.assertEqual("carry_forward_without_semantic_tuning", parent["decision"])

    def test_oracle_independence_uses_ast_dependencies_not_prose(self):
        oracle_source = (V7 / "oracle.py").read_text()
        dependencies = preflight.dependency_targets(oracle_source)
        self.assertNotIn("prepare_freeze", dependencies)
        self.assertNotIn("check_endpoint", dependencies)
        self.assertNotIn("preflight", dependencies)
        prose_only = '\"\"\"prepare_freeze check_endpoint preflight\"\"\"\nimport json\n'
        self.assertEqual({"json"}, preflight.dependency_targets(prose_only))
        actual_import = "from prepare_freeze import expected\n"
        self.assertEqual({"prepare_freeze"}, preflight.dependency_targets(actual_import))

    def test_canary_stages_nested_writable_mountpoint(self):
        source = (V7 / "run_canaries.py").read_text()
        self.assertLess(source.index('(inputs / "outputs").mkdir()'), source.index("subprocess.run"))
        canary = load(V7 / "canary-report.json")
        self.assertTrue(all(row["staged_mountpoint"] == "inputs/outputs" for row in canary["arms"]))

    def test_zero_call_preflight_and_canaries_pass(self):
        self.assertEqual([], preflight.validate(check_paths=True))
        canary = load(V7 / "canary-report.json")
        self.assertEqual("PASS", canary["status"])
        self.assertEqual(0, canary["model_calls"])
        self.assertEqual(0, canary["provider_calls"])


if __name__ == "__main__":
    unittest.main()
