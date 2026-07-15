from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/evidence-route-packet-conformance"
CASES = PILOT / "cases.json"
LABELS = PILOT / "labels.json"
SPEC = importlib.util.spec_from_file_location("evidence_route_validate", PILOT / "validate.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class EvidenceRoutePacketConformanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads(CASES.read_text())
        self.labels = json.loads(LABELS.read_text())
        self.contracts = {item["shape_id"]: item for item in self.data["route_contracts"]}

    def case(self, case_id: str) -> dict:
        return copy.deepcopy(next(item for item in self.data["cases"] if item["case_id"] == case_id))

    def test_frozen_twelve_case_replay_across_two_shapes(self) -> None:
        report = module.replay(self.data, self.labels, ROOT)
        self.assertEqual("passed", report["status"])
        self.assertEqual(12, report["cases_replayed"])
        self.assertEqual(2, len(report["work_shapes"]))
        self.assertFalse(report["checker_oracle_access"])
        self.assertTrue(all(value is False for value in report["claim_boundary"].values()))

    def test_freeze_manifest_pins_cases_labels_and_raw_evidence(self) -> None:
        manifest = json.loads((PILOT / "freeze-manifest.json").read_text())
        self.assertGreaterEqual(len(manifest["files"]), 12)
        for relative, expected in manifest["files"].items():
            with self.subTest(relative=relative):
                self.assertEqual(expected, hashlib.sha256((ROOT / relative).read_bytes()).hexdigest())

    def test_raw_hash_mutation_fails_closed(self) -> None:
        case = self.case("supported-packet")
        case["packet"]["observations"][0]["raw_sha256"] = "0" * 64
        row = module.check_case(case, self.contracts[case["shape_id"]], ROOT)
        self.assertEqual(("invalid", "evidence_invalid", "abstain"), (row["evidence_truth_sufficiency"], row["invalidity"], row["decision_eligibility"]))

    def test_transformed_hash_mutation_fails_closed(self) -> None:
        case = self.case("supported-packet")
        case["packet"]["observations"][0]["transformed_sha256"] = "0" * 64
        row = module.check_case(case, self.contracts[case["shape_id"]], ROOT)
        self.assertEqual("evidence_invalid", row["invalidity"])

    def test_missing_and_traversal_locators_fail_closed(self) -> None:
        for locator in ("pilots/evidence-route-packet-conformance/evidence/missing.json", "../outside.json"):
            with self.subTest(locator=locator):
                case = self.case("supported-packet")
                case["packet"]["observations"][0]["raw_locator"] = locator
                row = module.check_case(case, self.contracts[case["shape_id"]], ROOT)
                self.assertEqual("evidence_invalid", row["invalidity"])

    def test_route_identity_mutation_cannot_retain_coverage(self) -> None:
        case = self.case("supported-packet")
        case["actual_path"]["selected_route_id"] = "unknown-route"
        row = module.check_case(case, self.contracts[case["shape_id"]], ROOT)
        self.assertEqual("incomplete", row["route_coverage"])
        self.assertEqual("abstain", row["decision_eligibility"])

    def test_artifact_identity_mutation_is_not_supported(self) -> None:
        case = self.case("supported-packet")
        contract = copy.deepcopy(self.contracts[case["shape_id"]])
        contract["artifact_id"] = "another-artifact"
        row = module.check_case(case, contract, ROOT)
        self.assertEqual("evidence_invalid", row["invalidity"])

    def test_service_identity_and_version_are_pinned(self) -> None:
        case = self.case("supported-packet")
        case["environment"]["services"][0]["version"] = "9.9"
        row = module.check_case(case, self.contracts[case["shape_id"]], ROOT)
        self.assertEqual("incomplete", row["route_coverage"])
        self.assertNotEqual("eligible", row["decision_eligibility"])

    def test_oracle_and_rationale_fields_are_rejected_from_checker_input(self) -> None:
        case = self.case("supported-packet")
        for key in ("expected", "oracle", "rationale", "planted_defect"):
            with self.subTest(key=key):
                mutated = copy.deepcopy(case)
                mutated[key] = "not checker-visible"
                with self.assertRaisesRegex(ValueError, "forbidden oracle/rationale"):
                    module.check_case(mutated, self.contracts[case["shape_id"]], ROOT)

    def test_independent_label_mutation_is_detected_after_checking(self) -> None:
        labels = copy.deepcopy(self.labels)
        labels["labels"][0]["expected"]["decision_eligibility"] = "failed"
        with self.assertRaisesRegex(ValueError, "independent-label mismatch"):
            module.replay(self.data, labels, ROOT)

    def test_checker_is_invariant_to_domain_tokens(self) -> None:
        case = self.case("supported-packet")
        contract = copy.deepcopy(self.contracts[case["shape_id"]])
        baseline = module.check_case(case, contract, ROOT)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            locator = Path(case["packet"]["observations"][0]["raw_locator"])
            target = root / locator
            target.parent.mkdir(parents=True)
            raw = json.loads((ROOT / locator).read_text())
            raw.update({"artifact_id": "object-alpha", "criterion_id": "predicate-alpha", "service_id": "service-alpha"})
            payload = (json.dumps(raw, separators=(",", ":")) + "\n").encode()
            target.write_bytes(payload)
            case["shape_id"] = "shape-alpha"
            case["actual_path"]["selected_route_id"] = "route-alpha"
            case["actual_path"]["attempts"][0]["route_id"] = "route-alpha"
            case["environment"]["services"][0]["service_id"] = "service-alpha"
            case["packet"]["observations"][0]["raw_sha256"] = hashlib.sha256(payload).hexdigest()
            contract.update({"shape_id": "shape-alpha", "artifact_id": "object-alpha", "criterion_id": "predicate-alpha"})
            contract["routes"][0]["route_id"] = "route-alpha"
            contract["routes"][0]["prerequisites"] = ["service-alpha@1.0"]
            renamed = module.check_case(case, contract, root)
        self.assertEqual(
            {key: baseline[key] for key in module.RESULT_KEYS},
            {key: renamed[key] for key in module.RESULT_KEYS},
        )


if __name__ == "__main__":
    unittest.main()
