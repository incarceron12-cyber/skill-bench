from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V4 = ROOT / "pilots/pretask-procedure-transfer-v4"
V5 = ROOT / "pilots/pretask-procedure-transfer-v5"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


checker = module("v5_checker_independent_audit", V5 / "checkers/check_endpoint.py")
builder = module("v5_builder_independent_audit", V5 / "prepare_freeze.py")


def independent_epsilon(task_id: str, case: dict) -> dict:
    """Literal oracle for E-P1..E-P4; does not import the builder deriver."""
    rank = {"signed_scan": 2, "unsigned_note": 1}
    decisions = []
    for batch in case["batches"]:
        observations = [o for o in case["observations"] if o["batch_id"] == batch["batch_id"]]
        controlling = {}
        release = True
        for seal in batch["required_seals"]:
            candidates = [o for o in observations if o["seal"] == seal]
            admissible = [o for o in candidates if case["review_hour"] - o["hour"] <= 24]
            best_rank = max((rank[o["record_type"]] for o in admissible), default=-1)
            best = [o for o in admissible if rank[o["record_type"]] == best_rank]
            if not best or len({o["state"] for o in best}) != 1:
                release = False
                continue
            chosen = max(best, key=lambda o: (o["hour"], o["observation_id"]))
            controlling[seal] = chosen["observation_id"]
            if chosen["state"] != "intact":
                release = False
        decisions.append(
            {
                "batch_id": batch["batch_id"],
                "disposition": "release" if release else "quarantine",
                "controlling_seals": controlling,
                "observation_ids": [o["observation_id"] for o in observations],
                "reason": "independent non-empty explanation",
            }
        )
    return {"task_id": task_id, "decisions": decisions}


def independent_zeta(task_id: str, case: dict) -> dict:
    """Literal oracle for Z-P1..Z-P4, including ancestor rollback per Z-P3."""
    events = sorted(case["events"], key=lambda event: event["seq"])
    stack: list[str] = []
    transactions: dict[str, dict] = {}
    committed: list[str] = []
    rolled: list[str] = []
    valid = len({event["seq"] for event in events}) == len(events)
    for event in events if valid else []:
        operation = event["operation"]
        if operation == "begin":
            stack.append(event["transaction"])
            transactions[event["transaction"]] = {}
        elif operation == "set":
            if not stack:
                valid = False
                break
            transactions[stack[-1]][event["key"]] = event["value"]
        elif operation == "commit":
            if not stack or stack[-1] != event["transaction"]:
                valid = False
                break
            current = stack.pop()
            if stack:
                transactions[stack[-1]].update(transactions.pop(current))
            committed.append(current)
        elif operation == "rollback":
            if event["transaction"] not in stack:
                valid = False
                break
            index = stack.index(event["transaction"])
            discarded = list(reversed(stack[index:]))
            for transaction in discarded:
                transactions.pop(transaction, None)
            rolled.extend(discarded)
            del stack[index:]
        else:
            valid = False
            break
    valid = valid and not stack
    final_state = None
    if valid:
        final_state = {}
        for transaction in committed:
            if transaction in transactions:
                final_state.update(transactions[transaction])
    return {
        "task_id": task_id,
        "journal_id": case["journal_id"],
        "valid": valid,
        "final_state": final_state,
        "committed_transactions": committed,
        "rolled_back_transactions": rolled,
        "reason": "independent non-empty explanation",
    }


class PretaskProcedureTransferV5IndependentAudit(unittest.TestCase):
    def test_manifest_and_external_binding_hashes_recompute(self):
        manifest = load(V5 / "freeze-manifest.json")
        for row in manifest["components"] + manifest["external_immutable_bindings"]:
            path = ROOT / row["path"]
            self.assertEqual(row["bytes"], path.stat().st_size, row["path"])
            self.assertEqual(row["sha256"], hashlib.sha256(path.read_bytes()).hexdigest(), row["path"])

    def test_current_endpoints_rederive_without_builder_or_checker_oracle(self):
        for task_id in ("k4n7", "p9c2", "t6v1", "w3d8"):
            case = load(V5 / f"tasks/{task_id}/input.json")
            private = load(V5 / f"tasks/{task_id}/private.json")
            actual = independent_epsilon(task_id, case) if case["family_id"] == "family-epsilon" else independent_zeta(task_id, case)
            expected = copy.deepcopy(private["expected_semantics"])
            if case["family_id"] == "family-epsilon":
                for row in expected["decisions"]:
                    row["reason"] = "independent non-empty explanation"
            else:
                expected["reason"] = "independent non-empty explanation"
            self.assertEqual(expected, actual, task_id)

    def test_assignment_parity_zero_attempts_and_claim_ceiling(self):
        v4_rows = load(V4 / "assignments.json")["rows"]
        v5_rows = load(V5 / "assignments.json")["rows"]
        projection = lambda rows: [(r["schedule_index"], r["task_id"], r["family_id"], r["condition_id"]) for r in rows]
        self.assertEqual(projection(v4_rows), projection(v5_rows))
        self.assertTrue(all(row["attempts"] == 0 for row in v5_rows))
        protocol = load(V5 / "protocol.json")
        self.assertEqual({"model": 0, "provider": 0, "executor": 0, "repair": 0, "retry": 0}, protocol["attempt_ledger"])
        self.assertTrue(protocol["claim_ceiling"] and all(value is False for value in protocol["claim_ceiling"].values()))

    def test_valid_alternatives_and_wrong_consequences(self):
        for task_id in ("k4n7", "p9c2", "t6v1", "w3d8"):
            private = load(V5 / f"tasks/{task_id}/private.json")
            candidate = copy.deepcopy(private["expected_semantics"])
            if private["family_id"] == "family-epsilon":
                candidate["decisions"].reverse()
                for row in candidate["decisions"]:
                    row["reason"] = "  Paraphrased justification.  "
                    row["observation_ids"].reverse()
            else:
                candidate["reason"] = "  Paraphrased justification.  "
            # Reparse deliberately reordered, whitespace-heavy JSON: lexical formatting is not semantic.
            candidate = json.loads(json.dumps(candidate, sort_keys=True, indent=7))
            self.assertTrue(checker.compare(candidate, private)[0], task_id)
            wrong = copy.deepcopy(candidate)
            if private["family_id"] == "family-epsilon":
                wrong["decisions"][0]["disposition"] = "quarantine"
            else:
                wrong["valid"] = not wrong["valid"]
            self.assertFalse(checker.compare(wrong, private)[0], task_id)

    def test_epsilon_threshold_boundary_is_inclusive_and_arithmetic_is_independent(self):
        case = load(V5 / "tasks/k4n7/input.json")
        boundary = copy.deepcopy(case)
        boundary["observations"][2]["hour"] = boundary["review_hour"] - 24
        result = independent_epsilon("boundary", boundary)
        self.assertEqual("release", result["decisions"][0]["disposition"])
        expired = copy.deepcopy(boundary)
        expired["observations"][2]["hour"] -= 1
        result = independent_epsilon("expired", expired)
        self.assertEqual("quarantine", result["decisions"][0]["disposition"])

    def test_omissions_wrong_ids_types_and_cross_family_substitution_are_rejected(self):
        epsilon = load(V5 / "tasks/k4n7/private.json")
        zeta = load(V5 / "tasks/t6v1/private.json")
        for private, field in ((epsilon, "task_id"), (zeta, "journal_id")):
            candidate = copy.deepcopy(private["expected_semantics"])
            candidate.pop(field)
            self.assertFalse(checker.compare(candidate, private)[0])
        candidate = copy.deepcopy(epsilon["expected_semantics"])
        candidate["task_id"] = "p9c2"
        self.assertFalse(checker.compare(candidate, epsilon)[0])
        candidate = copy.deepcopy(zeta["expected_semantics"])
        candidate["valid"] = 1
        self.assertFalse(checker.compare(candidate, zeta)[0])
        self.assertFalse(checker.compare(zeta["expected_semantics"], epsilon)[0])
        self.assertFalse(checker.compare(epsilon["expected_semantics"], zeta)[0])

    def test_fatal_extra_field_and_condition_leakage_signature_is_reproducible(self):
        for task_id in ("k4n7", "t6v1"):
            private = load(V5 / f"tasks/{task_id}/private.json")
            candidate = copy.deepcopy(private["expected_semantics"])
            candidate["condition_id"] = "reference_procedure"
            candidate["uncontracted_payload"] = {"answer_hint": "retained"}
            if private["family_id"] == "family-epsilon":
                candidate["decisions"][0]["uncontracted_payload"] = True
            passed, errors = checker.compare(candidate, private)
            self.assertTrue(passed, (task_id, errors))  # Defect witness: strict/exact public contract is not enforced.

    def test_fatal_final_state_json_type_confusion_signature_is_reproducible(self):
        private = load(V5 / "tasks/t6v1/private.json")
        candidate = copy.deepcopy(private["expected_semantics"])
        candidate["final_state"]["x"] = True  # Python equality treats True == 1; JSON types differ.
        passed, errors = checker.compare(candidate, private)
        self.assertTrue(passed, errors)  # Defect witness.

    def test_derivation_common_mode_ancestor_rollback_signature_is_reproducible(self):
        case = {
            "family_id": "family-zeta",
            "journal_id": "JR",
            "events": [
                {"seq": 1, "operation": "begin", "transaction": "A"},
                {"seq": 2, "operation": "begin", "transaction": "B"},
                {"seq": 3, "operation": "set", "key": "x", "value": 1},
                {"seq": 4, "operation": "rollback", "transaction": "A"},
            ],
        }
        independent = independent_zeta("rollback-probe", case)
        builder_result = builder.derive_zeta("rollback-probe", case)
        self.assertTrue(independent["valid"])
        self.assertEqual(["B", "A"], independent["rolled_back_transactions"])
        self.assertFalse(builder_result["valid"])
        self.assertNotEqual(independent, builder_result)

    def test_source_valid_time_excludes_v5(self):
        for family in ("epsilon", "zeta"):
            corpus = load(V4 / f"families/{family}/corpus.json")
            self.assertIn("v4", corpus["authority_scope"]["valid_time"])
            self.assertTrue(all(proposition["valid_time"] == "v4 only" for proposition in corpus["propositions"]))
            self.assertNotIn("v5", corpus["authority_scope"]["valid_time"])


if __name__ == "__main__":
    unittest.main()
