import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "pilots/prospective-allocation-telemetry/v5/manifest.json"
RULE = ROOT / "pilots/prospective-allocation-telemetry/v5/adoption-observation-rule.json"


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


launcher = module("allocation_pair_launcher_v5_tests", ROOT / "scripts/allocation_pair_launcher_v5.py")


class AllocationPairLauncherV5Tests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.rule = json.loads(RULE.read_text(encoding="utf-8"))

    def test_manifest_binds_v4_identities_order_state_and_both_rubrics(self):
        self.assertEqual(launcher.validate_manifest(self.manifest, check_paths=True), [])
        self.assertEqual(self.manifest["forbidden_attempt_ids"], ["alloc-v4-configured-provider-probe-01"])
        self.assertEqual(self.manifest["state_policy"]["initial_sha256"], self.manifest["state_policy"]["final_sha256"])
        roles = {x["role"] for x in self.manifest["frozen_components"]}
        self.assertTrue({"independent_rubric", "shared_rubric", "coordinate_adapter", "adoption_rule"} <= roles)

    def test_rejects_reorder_retry_and_identity_drift(self):
        cases = []
        reordered = copy.deepcopy(self.manifest)
        reordered["attempt_schedule"].reverse()
        cases.append((reordered, "schedule drift"))
        retry = copy.deepcopy(self.manifest)
        retry["attempt_schedule"][0]["attempt_number"] = 2
        cases.append((retry, "schedule drift"))
        identity = copy.deepcopy(self.manifest)
        identity["comparison_identity_sha256"] = "f" * 64
        cases.append((identity, "identity drift"))
        for value, fragment in cases:
            errors = launcher.validate_manifest(value)
            self.assertTrue(any(fragment in x for x in errors), errors)

    def test_rejects_stale_component_and_claim_upgrade(self):
        stale = copy.deepcopy(self.manifest)
        stale["frozen_components"][0]["sha256"] = "0" * 64
        self.assertTrue(any("stale frozen component" in x for x in launcher.validate_manifest(stale, check_paths=True)))
        claim = copy.deepcopy(self.manifest)
        claim["claim_ceiling"]["allocation_effect"] = True
        self.assertIn("claim ceiling upgrade", launcher.validate_manifest(claim))

    def test_adoption_rule_forbids_presentation_and_similarity_proxies(self):
        self.assertEqual(self.rule["inference_policy"], "presentation_or_artifact_similarity_never_implies_invocation_or_adoption")
        forbidden = set(self.rule["adoption"]["forbidden_proxies"])
        self.assertTrue({"guide_present", "artifact_contains_guide_terms", "shared_rubric_score"} <= forbidden)
        row = self.manifest["attempt_schedule"][1]
        flow = launcher.observe_flow(row, Path("unused-trace"), Path("unused-output"))
        self.assertEqual(flow["presentation"]["status"], "observed")
        self.assertEqual(flow["invocation"]["status"], "unavailable")
        self.assertEqual(flow["adoption"]["status"], "not_observed")
        self.assertIsNone(flow["adoption"]["evidence"])

    def test_no_skill_flow_is_not_applicable(self):
        row = self.manifest["attempt_schedule"][0]
        flow = launcher.observe_flow(row, Path("unused-trace"), Path("unused-output"))
        for key in ("presentation", "invocation", "adoption"):
            self.assertEqual(flow[key]["status"], "not_applicable")


if __name__ == "__main__":
    unittest.main()
