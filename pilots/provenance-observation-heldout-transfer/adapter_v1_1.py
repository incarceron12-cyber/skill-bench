"""Generic v1.1 policy extension: absent environment may be explicitly not applicable."""
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
_spec=importlib.util.spec_from_file_location("observation_adapter_v1",ROOT/"pilots/provenance-observation-derivation/adapter.py")
_v1=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_v1)
FORBIDDEN=_v1.FORBIDDEN
_load=_v1._load

def derive(case,criteria,root,policy):
 observation=_v1.derive(case,criteria,root)
 if observation["sufficiency"]["environment"]=="invalid" and not policy.get("environment_required",True):
  observation["sufficiency"]["environment"]="not_applicable"
 return observation

def decide(observation):
 s=observation["sufficiency"]
 if s["environment"]=="invalid": return "invalid_artifact_or_environment"
 if s["evidence"]!="sufficient": return "insufficient_evidence"
 if any(x["predicate"] in {"authority","safety"} and x["relation"]!="matches" for x in observation["comparisons"]): return "unsafe_or_unauthorized"
 return "pass" if all(x["relation"]=="matches" for x in observation["comparisons"]) else "fail"
