import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/procedural-relation-projection"
SPEC = importlib.util.spec_from_file_location("relation_projection_audit", PILOT / "audit.py")
assert SPEC is not None and SPEC.loader is not None
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class ProceduralRelationProjectionTests(unittest.TestCase):
    def setUp(self):
        self.suite = mod.load()
        self.oracle = mod.load_oracle()

    def test_frozen_sources_clause_spans_and_prior_fixture_are_immutable(self):
        for record in self.suite["source_evidence"].values():
            self.assertEqual(record["sha256"], hashlib.sha256((ROOT / record["path"]).read_bytes()).hexdigest())
        self.assertEqual([], mod.structural_findings(self.suite))
        for world in self.suite["worlds"]:
            for clause in world["clauses"]:
                self.assertEqual({"start": 0, "end": len(clause["text"])}, clause["span"])
                self.assertEqual(mod.sha256_text(clause["text"]), clause["sha256"])

    def test_replay_matches_relation_verdict_and_locus_oracle(self):
        report = mod.replay(self.suite, self.oracle, write=False)
        self.assertEqual(14, report["summary"]["cases"])
        self.assertEqual(0, report["summary"]["relation_selection_errors"])
        self.assertEqual(0, report["summary"]["final_verdict_errors"])
        self.assertEqual(0, report["summary"]["failure_locus_errors"])
        self.assertEqual(2, len(report["summary"]["work_shapes"]))

    def test_trigger_absent_and_priority_override_are_distinct(self):
        rows = {row["case_id"]: row for row in mod.replay(self.suite, self.oracle, write=False)["rows"]}
        self.assertEqual((None, "not_applicable"), (rows["proc-trigger-absent"]["relation_id"], rows["proc-trigger-absent"]["verdict"]))
        self.assertEqual(("proc-override", "relation_satisfied"), (rows["proc-override-hold"]["relation_id"], rows["proc-override-hold"]["verdict"]))
        self.assertEqual(("research-primary", "relation_satisfied"), (rows["research-primary-available"]["relation_id"], rows["research-primary-available"]["verdict"]))

    def test_alternative_paths_and_observer_insufficiency_fail_closed(self):
        rows = {row["case_id"]: row for row in mod.replay(self.suite, self.oracle, write=False)["rows"]}
        self.assertEqual(["hold-for-approval"], rows["proc-alternative-hold"]["accepted_path_ids"])
        self.assertEqual(["clarify-without-claim"], rows["research-alternative-clarify"]["accepted_path_ids"])
        self.assertEqual("inconclusive", rows["proc-observer-insufficient"]["verdict"])
        self.assertEqual("inconclusive", rows["research-observer-insufficient"]["verdict"])

    def test_mixed_evidence_is_retained_before_final_policy(self):
        rows = {row["case_id"]: row for row in mod.replay(self.suite, self.oracle, write=False)["rows"]}
        for case_id, repair_event in (("proc-mixed-repair", "recall_completed"), ("research-mixed-repair", "label_repaired")):
            row = rows[case_id]
            self.assertTrue(row["mixed_evidence"])
            self.assertEqual("relation_violated", row["verdict"])
            self.assertIn(repair_event, {event["event"] for event in row["evidence_events"]})

    def test_mutations_localize_every_projection_boundary_exactly(self):
        rows = mod.mutation_report(self.suite, self.oracle)
        self.assertEqual(set(self.oracle["mutation_expectations"]), {row["mutation"] for row in rows})
        self.assertTrue(all(row["localized_exactly"] for row in rows), rows)

    def test_private_oracle_does_not_leak_expected_outputs_into_suite(self):
        public = json.loads((PILOT / "suite.json").read_text(encoding="utf-8"))
        for case in public["cases"]:
            self.assertTrue({"expected", "relation_id", "verdict", "failure_locus"}.isdisjoint(case))
        oracle_case_ids = {item["case_id"] for item in self.oracle["cases"]}
        self.assertEqual(oracle_case_ids, {item["case_id"] for item in public["cases"]})

    def test_consequence_overclaim_and_private_basis_fail_closed(self):
        for mutation, locus in (("consequence_overclaim", "consequence_interpretation"), ("hidden_public_basis", "public_basis")):
            findings = mod.structural_findings(mod.mutate(self.suite, mutation))
            self.assertEqual({locus}, {item["failure_locus"] for item in findings})


if __name__ == "__main__":
    unittest.main()
