from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V6 = ROOT / "pilots/pretask-procedure-transfer-v6"
V7 = ROOT / "pilots/pretask-procedure-transfer-v7"
TASKS = ("k4n7", "p9c2", "t6v1", "w3d8")
ATTEMPTS = {"model": 0, "provider": 0, "executor": 0, "repair": 0, "retry": 0}
CLAIMS = {"agent_capability", "expert_provenance", "production_fitness", "professional_validity", "readiness", "transfer", "utility"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


oracle = module("v7_oracle_independent_audit", V7 / "oracle.py")
checker = module("v7_checker_independent_audit", V7 / "checkers/check_endpoint.py")


def normalized(value):
    result = copy.deepcopy(value)
    if "decisions" in result:
        for row in result["decisions"]:
            row["reason"] = "normalized"
    else:
        result["reason"] = "normalized"
    return result


def import_targets(path: Path) -> set[str]:
    targets: set[str] = set()
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            targets.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            targets.add(node.module)
        elif isinstance(node, ast.Call):
            fn = node.func
            dynamic = (isinstance(fn, ast.Name) and fn.id == "__import__") or (
                isinstance(fn, ast.Attribute) and fn.attr in {"import_module", "spec_from_file_location"}
            )
            if dynamic and node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                targets.add(node.args[0].value)
    return targets


class PretaskProcedureTransferV7IndependentAudit(unittest.TestCase):
    def test_every_component_external_binding_and_v6_failed_record_is_exact(self):
        manifest = load(V7 / "freeze-manifest.json")
        for row in manifest["components"] + manifest["external_immutable_bindings"]:
            path = ROOT / row["path"]
            self.assertTrue(path.is_file(), row["path"])
            self.assertEqual(row["bytes"], path.stat().st_size, row["path"])
            self.assertEqual(row["sha256"], sha(path), row["path"])
        bound = {row["path"] for row in manifest["external_immutable_bindings"]}
        v6_manifest = load(V6 / "freeze-manifest.json")
        self.assertTrue({row["path"] for row in v6_manifest["components"]}.issubset(bound))
        self.assertTrue({
            "pilots/pretask-procedure-transfer-v6/freeze-manifest.json",
            "pilots/pretask-procedure-transfer-v6/canary-report.json",
            "pilots/pretask-procedure-transfer-v6/preflight-report.json",
        }.issubset(bound))

    def test_source_authority_is_hash_bound_and_narrow(self):
        record = load(V7 / "source-applicability.json")
        self.assertEqual("builder-authored internal calibration only", record["authority"])
        self.assertEqual("v7 only", record["valid_time"])
        self.assertFalse(record["supersedes_or_edits_v4_authority"])
        self.assertEqual(sha(V6 / "source-applicability.json"), record["parent_authority"]["sha256"])
        self.assertEqual(8, len(record["proposition_lineage"]))
        for row in record["proposition_lineage"]:
            source = ROOT / row["source_path"]
            proposition = next(item for item in load(source)["propositions"] if item["id"] == row["proposition_id"])
            self.assertEqual(sha(source), row["source_file_sha256"])
            self.assertEqual(hashlib.sha256(proposition["statement"].encode("utf-8")).hexdigest(), row["source_statement_sha256"])
            self.assertEqual("v4 only", row["source_valid_time_retained"])
            self.assertEqual("authorized_internal_calibration_v7_only", row["v7_applicability"])

    def test_oracle_static_dependencies_exclude_builder_checker_and_preflight(self):
        targets = import_targets(V7 / "oracle.py")
        normalized_targets = {piece for target in targets for piece in target.replace("-", "_").split(".")}
        self.assertTrue({"prepare_freeze", "check_endpoint", "preflight"}.isdisjoint(normalized_targets))
        self.assertEqual({"__future__", "argparse", "json", "pathlib", "typing"}, targets)

    def test_literal_fixture_endpoints_and_oracle_agree(self):
        literal = {
            "k4n7": {"task_id": "k4n7", "decisions": [{"batch_id": "L8", "controlling_seals": {"blue": "o3", "red": "o1"}, "disposition": "release", "observation_ids": ["o1", "o2", "o3"], "reason": "normalized"}]},
            "p9c2": {"task_id": "p9c2", "decisions": [{"batch_id": "Q3", "controlling_seals": {"amber": "r2", "green": "r3"}, "disposition": "release", "observation_ids": ["r1", "r2", "r3"], "reason": "normalized"}]},
            "t6v1": {"task_id": "t6v1", "journal_id": "J6", "valid": True, "final_state": {"x": 1}, "committed_transactions": ["A"], "rolled_back_transactions": ["B"], "reason": "normalized"},
            "w3d8": {"task_id": "w3d8", "journal_id": "J9", "valid": False, "final_state": None, "committed_transactions": ["C"], "rolled_back_transactions": [], "reason": "normalized"},
        }
        for task_id in TASKS:
            private = load(V7 / f"tasks/{task_id}/private.json")
            independently_derived = oracle.derive(task_id, load(V7 / f"tasks/{task_id}/input.json"))
            self.assertEqual(literal[task_id], normalized(private["expected_semantics"]), task_id)
            self.assertEqual(literal[task_id], normalized(independently_derived), task_id)

    def test_source_targeted_mutations(self):
        epsilon = {"family_id": "family-epsilon", "review_hour": 100,
                   "batches": [{"batch_id": "B", "required_seals": ["s"]}],
                   "observations": [{"observation_id": "signed", "batch_id": "B", "record_type": "signed_scan", "seal": "s", "state": "broken", "hour": 76},
                                    {"observation_id": "note", "batch_id": "B", "record_type": "unsigned_note", "seal": "s", "state": "intact", "hour": 99}]}
        self.assertEqual("quarantine", oracle.derive_epsilon("at-24", epsilon)["decisions"][0]["disposition"])
        epsilon["observations"][0]["hour"] = 75
        self.assertEqual("release", oracle.derive_epsilon("expired", epsilon)["decisions"][0]["disposition"])

        ancestor_rollback = {"family_id": "family-zeta", "journal_id": "probe", "events": [
            {"seq": 1, "operation": "begin", "transaction": "A"},
            {"seq": 2, "operation": "begin", "transaction": "B"},
            {"seq": 3, "operation": "set", "key": "x", "value": 1},
            {"seq": 4, "operation": "rollback", "transaction": "A"},
        ]}
        result = oracle.derive_zeta("rollback", ancestor_rollback)
        self.assertTrue(result["valid"])
        self.assertEqual(["B", "A"], result["rolled_back_transactions"])
        for events in (
            [{"seq": 1, "operation": "commit", "transaction": "A"}],
            [{"seq": 1, "operation": "begin", "transaction": "A"}, {"seq": 1, "operation": "commit", "transaction": "A"}],
            [{"seq": 1, "operation": "begin", "transaction": "A"}, {"seq": 2, "operation": "begin", "transaction": "B"}, {"seq": 3, "operation": "commit", "transaction": "A"}],
        ):
            case = {"family_id": "family-zeta", "journal_id": "invalid", "events": events}
            self.assertFalse(oracle.derive_zeta("invalid", case)["valid"])

    def test_checker_language_accepts_valid_variants_and_rejects_mutations(self):
        for task_id in TASKS:
            private = load(V7 / f"tasks/{task_id}/private.json")
            canonical = copy.deepcopy(private["expected_semantics"])
            if "reason" in canonical:
                canonical["reason"] = "paraphrase"
            if private["family_id"] == "family-epsilon":
                canonical["decisions"].reverse()
                for row in canonical["decisions"]:
                    row["reason"] = "paraphrase"
                    row["observation_ids"].reverse()
            self.assertTrue(checker.compare(canonical, private)[0], task_id)
            for extra in ("condition_id", "treatment_metadata", "uncontracted_payload"):
                mutant = copy.deepcopy(canonical)
                mutant[extra] = "forbidden"
                self.assertFalse(checker.compare(mutant, private)[0], (task_id, extra))
        with self.assertRaises(checker.DuplicateKey):
            checker.loads_strict('{"a":1,"a":2}')
        with self.assertRaises(ValueError):
            checker.loads_strict('{"a":NaN}')
        private = load(V7 / "tasks/t6v1/private.json")
        for value in (True, False, 0, 1.0, None, {"nested": 1}):
            mutant = copy.deepcopy(private["expected_semantics"])
            mutant["final_state"]["x"] = value
            self.assertFalse(checker.compare(mutant, private)[0], repr(value))

    def test_zero_attempts_false_claims_and_retained_canary_preflight(self):
        manifest, protocol = load(V7 / "freeze-manifest.json"), load(V7 / "protocol.json")
        for record in (manifest, protocol):
            self.assertEqual(ATTEMPTS, record["attempt_ledger"])
            self.assertEqual(CLAIMS, set(record["claim_ceiling"]))
            self.assertTrue(all(value is False for value in record["claim_ceiling"].values()))
        self.assertFalse(manifest["executor_authorized"])
        self.assertFalse(protocol["execution_authorized"])
        self.assertTrue(all(row["attempts"] == 0 for row in load(V7 / "assignments.json")["rows"]))
        for task_id in TASKS:
            private = load(V7 / f"tasks/{task_id}/private.json")
            self.assertEqual(ATTEMPTS, private["attempts"])
            self.assertTrue(all(value is False for value in private["claim_ceiling"].values()))
        canary, preflight = load(V7 / "canary-report.json"), load(V7 / "preflight-report.json")
        self.assertEqual("PASS", canary["status"])
        self.assertTrue(all(arm["passed"] for arm in canary["arms"]))
        self.assertEqual("PASS", preflight["status"])
        self.assertEqual([], preflight["errors"])
        self.assertEqual(0, canary["model_calls"] + canary["provider_calls"] + canary["executor_attempts"])


if __name__ == "__main__":
    unittest.main()
