#!/usr/bin/env python3
"""Build the prospective protocol and freeze every outcome-relevant component."""
from __future__ import annotations
import hashlib, json, random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
COMPONENTS = [
    "pilots/evidence-acquisition-matched-agent-v1/README.md",
    "pilots/evidence-acquisition-matched-agent-v1/instrument/prompt-template.md",
    "pilots/evidence-acquisition-matched-agent-v1/instrument/parser-policy.json",
    "pilots/evidence-acquisition-matched-agent-v1/instrument/grader.py",
    "pilots/evidence-acquisition-matched-agent-v1/instrument/scenarios/compliance.json",
    "pilots/evidence-acquisition-matched-agent-v1/instrument/scenarios/analysis.json",
    "pilots/evidence-acquisition-matched-agent-v1/run_study.py",
    "pilots/configured-artifact-revision/launcher.py",
    "schemas/evidence-acquisition-episode.schema.json",
    "scripts/validate_evidence_acquisition.py",
]

def sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(path: Path, value) -> None: path.write_text(json.dumps(value, indent=2, sort_keys=True)+"\n")

def main() -> int:
    rows=[]
    for repeat in (1,2):
        for scenario in ("vendor-disposition","segment-release"):
            for condition in ("active","full_information","expert_minimal"):
                token=hashlib.sha256(f"{scenario}:{condition}:{repeat}:ea-v1".encode()).hexdigest()[:10]
                rows.append({"attempt_id":f"ea-{token}","scenario_id":scenario,"condition_id":condition,"repeat":repeat})
    random.Random(7122026).shuffle(rows)
    for index,row in enumerate(rows,1): row["execution_order"]=index
    protocol={
      "schema_version":"0.1.0","protocol_id":"evidence-acquisition-matched-agent-v1","frozen_at":"2026-07-15T15:55:00Z",
      "charter_decision_filter":{"objectives":["B: expertise-to-evaluation methodology","C: executable infrastructure"],"artifact":"frozen 2-shape x 3-condition x 2-repeat agent matrix","uncertainty":"whether real configured-agent transitions are representable without feedback leakage","mode":"building and validation","duplication":"extends synthetic contract conformance into execution rather than adding a parallel schema","scope_boundary":"purposive synthetic methods probe, not a domain commitment","useful_completion":"twelve retained declared attempts or exact invalid cells, two schema-valid repeat packages, and replayable separate-shape contrasts"},
      "configured_system":{"model":"gpt-5.6-sol","provider":"openai-codex","toolsets":["file"],"safe_mode":True,"invocation":"fresh oneshot per interaction turn","max_interaction_turns":{"active":4,"supplied":1},"timeout_seconds_per_turn":900,"retries":0,"replacement":"none"},
      "schedule":{"order_seed":7122026,"task_seed":"sha256(scenario:condition:repeat:ea-v1)","rows":rows,"outcome_based_retry":"forbidden"},
      "budgets":{"request_cost_budget":3,"active_max_requests":3,"full_information_supply":"all admissible and delayed atoms at step zero","expert_minimal_supply":"exact builder-marked synthetic minimal set"},
      "parser_access_policy":"instrument/parser-policy.json",
      "terminal_checks":["artifact_valid","decision","evidence_lineage","severe_evidence_used","rationale_present","uncertainty_present"],
      "stopping_loss_rules":{"vendor-disposition":"Escalate when controlling authorization is absent, inactive, or unknown at deadline; otherwise apply disclosed approval rule.","segment-release":"Hold unless authoritative adjusted retention and eligible sample meet both disclosed thresholds; escalate on irreconcilable authority conflict."},
      "invalidity":{"service":"nonzero provider exit, missing usage, completed false, or failed true","environment":"failed isolation/firewall canary or changed read-only inputs","artifact":"missing/malformed turn JSON or terminal fields","eligibility":"endpoint contrasts require service, environment, cost, artifact, and schema validity; invalid attempts remain in intended denominator"},
      "reporting":{"no_shape_pooling":True,"separate_dimensions":["inquiry_selection","access","adoption","stopping","endpoint_quality","cost","severe_omission"],"confidence":"descriptive exact attempts only; no inferential interval with n=2 per cell"},
      "claim_boundaries":{key:False for key in ["causal_inquiry_benefit","agent_capability","professional_capability","clinical_validity","compliance_validity","expert_validity","safety","production_fitness","deployment_readiness","population_representativeness","cross_domain_generality"]},
      "expert_minimal_boundary":"Builder-authored synthetic set; no expert selected, reviewed, or approved it.",
      "frozen_components":[{"path":p,"sha256":sha(ROOT/p)} for p in COMPONENTS],
    }
    dump(HERE/"protocol.json",protocol)
    print(json.dumps({"protocol":str(HERE/"protocol.json"),"sha256":sha(HERE/"protocol.json"),"attempts":len(rows),"components":len(COMPONENTS)},indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
