#!/usr/bin/env python3
"""Preflight, execute once, and replay the frozen evidence-acquisition matrix."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, shutil, subprocess, tempfile
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
PROTOCOL=HERE/"protocol.json"; EXEC=HERE/"execution"; PREFLIGHT=HERE/"preflight"
BASE_PATH=ROOT/"pilots/configured-artifact-revision/launcher.py"
SCENARIO_PATHS={"vendor-disposition":HERE/"instrument/scenarios/compliance.json","segment-release":HERE/"instrument/scenarios/analysis.json"}
UNSUPPORTED=["professional capability","clinical validity","compliance validity","agent capability","causal inquiry benefit","safety","production fitness","deployment readiness","cross-domain generality","expert validity","population representativeness","real expert minimality"]

def module(name:str,path:Path)->Any:
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None:raise RuntimeError(f"cannot import {path}")
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
base=module("ea_base",BASE_PATH); grader=module("ea_grader",HERE/"instrument/grader.py")
def load(path:Path)->Any:return json.loads(path.read_text())
def dump(path:Path,value:Any)->None:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,indent=2,sort_keys=True)+"\n")
def sha(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def inventory(root:Path)->dict[str,dict[str,Any]]:return {p.relative_to(root).as_posix():{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(root.rglob("*")) if p.is_file()}
def git(*args:str)->subprocess.CompletedProcess:return subprocess.run(["git",*args],cwd=ROOT,capture_output=True,text=True)

def verify_protocol(require_pushed:bool)->dict[str,Any]:
    p=load(PROTOCOL); errors=[]
    rows=p["schedule"]["rows"]
    if len(rows)!=12 or len({r["attempt_id"] for r in rows})!=12:errors.append("schedule must have 12 unique attempts")
    for sid in SCENARIO_PATHS:
        for cond in ("active","full_information","expert_minimal"):
            if sum(r["scenario_id"]==sid and r["condition_id"]==cond for r in rows)!=2:errors.append(f"two repeats missing {sid}/{cond}")
    for item in p["frozen_components"]:
        path=ROOT/item["path"]
        if not path.is_file() or sha(path)!=item["sha256"]:errors.append(f"component drift {item['path']}")
    if any(p["claim_boundaries"].values()):errors.append("claim ceiling upgraded")
    pushed=None
    if require_pushed:
        fetch=git("fetch","origin","main")
        if fetch.returncode:errors.append("git fetch failed")
        remote=subprocess.run(["git","show","origin/main:pilots/evidence-acquisition-matched-agent-v1/protocol.json"],cwd=ROOT,capture_output=True)
        if remote.returncode or hashlib.sha256(remote.stdout).hexdigest()!=sha(PROTOCOL):errors.append("protocol bytes not frozen on origin/main")
        else:pushed=git("rev-parse","origin/main").stdout.strip()
    return {"passed":not errors,"errors":errors,"protocol_sha256":sha(PROTOCOL),"pushed_commit":pushed,"component_count":len(p["frozen_components"])}

def scenario_public(s:dict[str,Any])->dict[str,Any]:return {"scenario_id":s["scenario_id"],"target":s["target"],"public_context":s["public_context"]}
def supplied_atoms(s:dict[str,Any],condition:str)->list[dict[str,Any]]:
    if condition=="full_information":chosen=[a for a in s["evidence_atoms"] if a["availability"] in {"admissible","delayed"}]
    elif condition=="expert_minimal":chosen=[a for a in s["evidence_atoms"] if a["minimal_set_member"]]
    else:chosen=[]
    return [{"evidence_id":a["evidence_id"],"content":a["content"],"authority":a["authority"]} for a in chosen]

def materialize(root:Path,s:dict[str,Any],condition:str)->dict[str,Path]:
    if root.exists():raise FileExistsError(root)
    inputs,outputs,profile=root/"inputs",root/"outputs",root/".profile"
    (inputs/"outputs").mkdir(parents=True);outputs.mkdir();base._copy_runtime_profile(profile)
    dump(inputs/"public-scenario.json",scenario_public(s));dump(inputs/"supplied-evidence.json",supplied_atoms(s,condition))
    dump(inputs/"manifest.json",{"condition":condition,"inputs":"read_only","only_writable":"outputs","visible":["public-scenario.json","supplied-evidence.json","manifest.json"],"excluded":["answers","grader","parser-policy","protocol","repository","other attempts"]})
    return {"inputs":inputs,"outputs":outputs,"profile":profile}

def canary()->dict[str,Any]:
    reports=[]
    for sid in SCENARIO_PATHS:
        s=load(SCENARIO_PATHS[sid])
        with tempfile.TemporaryDirectory(prefix="ea-canary-") as td:
            paths=materialize(Path(td)/"trial",s,"active")
            private=["/home/sam/skill-bench/data/work_queue.json","protocol.json","grader.py","parser-policy.json","answers.json","other-attempts"]
            code="PRIVATE="+repr(private)+"\n"+r'''import json,os
from tools.file_tools import read_file_tool,search_tool,write_file_tool
def readable(p):
 t=read_file_tool(p,limit=5).lower();return not any(x in t for x in ("error reading","not found","permission denied","does not exist"))
o={"cwd":os.getcwd(),"visible":{p:readable(p) for p in ["public-scenario.json","supplied-evidence.json","manifest.json"]},"private_denied":{p:not readable(p) for p in PRIVATE},"repo_search":search_tool("skill-bench",target="files",path="/home/sam",limit=10)}
o["write_output"]="error" not in write_file_tool("outputs/canary.txt","ok\n").lower();o["escape_denied"]="error" in write_file_tool("escape.txt","bad\n").lower();print(json.dumps(o))'''
            proc=subprocess.run(base._bwrap(paths,["/opt/hermes/venv/bin/python","-c",code]),capture_output=True,text=True,timeout=120)
            try:obs=json.loads(proc.stdout.strip().splitlines()[-1])
            except Exception:obs={}
            passed=proc.returncode==0 and obs.get("cwd")=="/trial" and all(obs.get("visible",{}).values()) and all(obs.get("private_denied",{}).values()) and "skill-bench" not in str(obs.get("repo_search","")) and obs.get("write_output") is True and obs.get("escape_denied") is True
            reports.append({"scenario_id":sid,"passed":passed,"model_calls":0,"observed":obs,"returncode":proc.returncode,"stderr":proc.stderr[-1000:]})
    template=(HERE/"instrument/prompt-template.md").read_text()
    firewall={"passed":all(term not in template for term in ["correct_decision","severe_required_ids","endpoint_quality"]),"model_calls":0,"allowed_preterminal":["access_status","evidence_content","budget_state"],"forbidden":["grader output","correct decision","private rubric"]}
    result={"passed":all(r["passed"] for r in reports) and firewall["passed"],"model_calls":0,"isolation":reports,"feedback_firewall":firewall,"protocol":verify_protocol(False)}
    result["passed"]&=result["protocol"]["passed"];dump(PREFLIGHT/"canary-report.json",result);return result

def parser(request:dict[str,Any],s:dict[str,Any])->dict[str,Any]:
    if not isinstance(request.get("raw_request"),str):return {"status":"parser_error","mapped_evidence_ids":[],"interpreted_scope":"malformed request","confidence":None}
    text=request["raw_request"].lower();mapped=[a["evidence_id"] for a in s["evidence_atoms"] if any(alias in text for alias in a["aliases"])]
    status="matched" if len(mapped)==1 else "ambiguous" if mapped else "unmatched"
    return {"status":status,"mapped_evidence_ids":mapped,"interpreted_scope":request.get("requested_scope") or request["raw_request"],"confidence":1.0 if status=="matched" else .5 if status=="ambiguous" else 0.0}

def command(prompt:str,usage_name:str)->list[str]:return ["/opt/hermes/venv/bin/python","/opt/hermes/venv/bin/hermes","-z",prompt,"--usage-file",f"/trial/outputs/{usage_name}","--model","gpt-5.6-sol","--provider","openai-codex","--toolsets","file","--safe-mode"]
def prompt_for(s:dict[str,Any],condition:str,transcript:list[dict[str,Any]],turn:int)->str:
    ci={"active":"Request evidence under the frozen budget, then stop with a terminal artifact.","full_information":"All admissible/delayed evidence is supplied; requests are prohibited. Stop now with a terminal artifact.","expert_minimal":"Only the builder-authored synthetic minimal set is supplied; requests are prohibited. Stop now with a terminal artifact."}[condition]
    text=(HERE/"instrument/prompt-template.md").read_text()
    replacements={"{target}":s["target"],"{public_context}":s["public_context"],"{condition_instructions}":ci,"{transcript}":json.dumps(transcript,indent=2),"{turn_file}":f"turn-{turn}.json"}
    for old,new in replacements.items():text=text.replace(old,new)
    return text

def access_from_parse(parsed:dict[str,Any],request_id:str,step:int,s:dict[str,Any],budget:float)->tuple[dict[str,Any],float,dict[str,Any]|None]:
    if parsed["status"]!="matched":return ({"access_event_id":f"access-{step}","step":step,"request_id":request_id,"evidence_id":None,"status":"ambiguous" if parsed["status"]=="ambiguous" else "failed","content_locator":None,"observer_id":"environment.synthetic.v1","transformation":"none","reason":f"Parser status {parsed['status']}; no evidence released."},max(0,budget-.5),None)
    eid=parsed["mapped_evidence_ids"][0];atom=next(a for a in s["evidence_atoms"] if a["evidence_id"]==eid);budget=max(0,budget-atom["cost"])
    if atom["availability"]=="restricted":status="denied";content=None;reason="Restricted evidence denied under frozen policy."
    elif atom["availability"]=="unavailable":status="denied";content=None;reason="Evidence unavailable under frozen policy."
    elif atom["availability"]=="delayed":status="delayed";content=None;reason="Evidence queued for one-step delayed release."
    else:status="released";content=f"transcript.step-{step}.content";reason="Matched admissible evidence released."
    event={"access_event_id":f"access-{step}","step":step,"request_id":request_id,"evidence_id":eid,"status":status,"content_locator":content,"observer_id":"environment.synthetic.v1","transformation":"none","reason":reason}
    pending=atom if status=="delayed" else None
    return event,budget,pending

def run_attempt(p:dict[str,Any],row:dict[str,Any])->dict[str,Any]:
    root=EXEC/"attempts"/row["attempt_id"];s=load(SCENARIO_PATHS[row["scenario_id"]]);condition=row["condition_id"]
    paths=materialize(root/"trial",s,condition);before=inventory(paths["inputs"]);transcript=[];requests=[];events=[];budget=float(p["budgets"]["request_cost_budget"]);pending=None;final={};procs=[]
    for atom in supplied_atoms(s,condition):transcript.append({"kind":"supplied_evidence",**atom,"remaining_budget":budget})
    maxturn=4 if condition=="active" else 1
    for turn in range(1,maxturn+1):
        if pending is not None:
            event={"access_event_id":f"access-{len(events)+1}-release","step":len(requests)+1,"request_id":requests[-1]["request_id"],"evidence_id":pending["evidence_id"],"status":"released","content_locator":f"transcript.turn-{turn}.delayed-content","observer_id":"environment.synthetic.v1","transformation":"none","reason":"Frozen one-step delay elapsed."};events.append(event);transcript.append({"kind":"access","status":"released","evidence_id":pending["evidence_id"],"content":pending["content"],"remaining_budget":budget});pending=None
        out=paths["outputs"]/f"turn-{turn}.json";usage_name=f"usage-turn-{turn}.json";prompt=prompt_for(s,condition,transcript,turn)
        proc=subprocess.run(base._bwrap(paths,command(prompt,usage_name)),capture_output=True,text=True,timeout=900);procs.append(proc)
        (root/f"redacted-trace-turn-{turn}.log").write_text(proc.stdout);(root/f"launcher-stderr-turn-{turn}.log").write_text(proc.stderr)
        try:action=load(out)
        except Exception:action={"action":"invalid","raw_output_locator":f"trial/outputs/turn-{turn}.json"}
        transcript.append({"kind":"agent_action","turn":turn,"action":action})
        if action.get("action")=="terminal":final=action;break
        if condition!="active":final=action;break
        rid=f"request-{len(requests)+1}";parsed=parser(action,s);request={"request_id":rid,"step":len(requests)+1,"raw_request":str(action.get("raw_request",action)),"intent":str(action.get("intent","Unparseable agent request intent.")),"requested_scope":str(action.get("requested_scope","Unspecified scope.")),"expected_value_basis":str(action.get("expected_value_basis","No valid expected-value basis emitted.")),"parser_interpretation":{"parser_id":"parser.deterministic-keyword.v1",**parsed,"evidence_locator":f"trial/outputs/turn-{turn}.json"}};requests.append(request)
        event,budget,pending=access_from_parse(parsed,rid,request["step"],s,budget);events.append(event)
        message={"kind":"access","status":event["status"],"evidence_id":event["evidence_id"],"remaining_budget":budget}
        if event["status"]=="released":message["content"]=next(a["content"] for a in s["evidence_atoms"] if a["evidence_id"]==event["evidence_id"])
        transcript.append(message)
        if budget<=0 and turn<maxturn:transcript.append({"kind":"budget_state","message":"Budget exhausted; terminal action required.","remaining_budget":0})
    if not final:final={"action":"invalid","uncertainty":"No terminal artifact emitted."}
    changed=before!=inventory(paths["inputs"]);usages=[]
    for turn in range(1,len(procs)+1):
        up=paths["outputs"]/f"usage-turn-{turn}.json";usages.append(load(up) if up.is_file() else {})
    service=bool(procs) and all(proc.returncode==0 for proc in procs) and all(u.get("completed") is True and u.get("failed") is False for u in usages)
    cost_valid=all(u.get("cost_status")=="included" and u.get("estimated_cost_usd")==0.0 for u in usages)
    artifact_valid=final.get("action")=="terminal" and isinstance(final.get("evidence_ids"),list)
    released={e["evidence_id"] for e in events if e["status"]=="released"}
    if condition!="active":released={a["evidence_id"] for a in supplied_atoms(s,condition)};events=[{"access_event_id":f"supplied-{i}","step":0,"request_id":None,"evidence_id":a["evidence_id"],"status":"released","content_locator":f"trial/inputs/supplied-evidence.json#{i-1}","observer_id":"environment.synthetic.v1","transformation":"none","reason":"Supplied by frozen matched condition."} for i,a in enumerate(supplied_atoms(s,condition),1)]
    grade=grader.grade(final,s,released,artifact_valid);dump(root/"grade.json",grade)
    report={**row,"launcher_invocations":len(procs),"returncodes":[x.returncode for x in procs],"service_valid":service,"cost_valid":cost_valid,"environment_valid":not changed,"artifact_valid":artifact_valid,"requests":requests,"access_events":events,"released_ids":sorted(released),"final":final,"grade":grade,"usage":usages,"input_integrity":not changed,"artifacts":inventory(paths["outputs"]),"claim_boundaries":p["claim_boundaries"]};dump(root/"trial-report.json",report);shutil.rmtree(paths["profile"],ignore_errors=True);return report

def episode(row:dict[str,Any],trial:dict[str,Any],s:dict[str,Any])->dict[str,Any]:
    condition=row["condition_id"];released=set(trial["released_ids"]);cited=set(trial["final"].get("evidence_ids",[])) & released;event_by_eid={e["evidence_id"]:e for e in trial["access_events"] if e["status"]=="released"}
    adoptions=[{"evidence_id":eid,"access_event_id":event_by_eid[eid]["access_event_id"],"disposition":"adopted","trace_evidence_locator":f"execution/attempts/{row['attempt_id']}/trial/outputs/turn-{trial['launcher_invocations']}.json#evidence_ids","belief_update":"Agent explicitly included released evidence in terminal basis.","action_or_artifact_change":"Terminal rationale and decision cite this evidence ID."} for eid in sorted(cited)]
    reason={"full_information":"all_supplied","expert_minimal":"expert_minimal_set_supplied"}.get(condition,trial["final"].get("stop_reason","abstain"));allowed={"decision_sufficient","marginal_value_below_cost","budget_exhausted","abstain","escalate"};reason=reason if reason not in allowed and condition!="active" else reason if reason in allowed else "abstain"
    if condition=="active" and reason in {"decision_sufficient","marginal_value_below_cost"} and not cited:reason="abstain"
    return {"episode_id":row["attempt_id"],"condition_id":condition,"requests":trial["requests"],"access_events":trial["access_events"],"adoptions":adoptions,"feedback_firewall":{"evaluator_outputs_exposed_before_terminal":False,"allowed_preterminal_feedback":["access_status","evidence_content","budget_state"],"feedback_events":[{"source":"environment","phase":"preterminal","content_kind":"access_status"},{"source":"grader","phase":"post_terminal","content_kind":"endpoint score"}]},"stopping":{"step":max([x["step"] for x in trial["requests"]+trial["access_events"]],default=0),"reason":reason,"basis_evidence_ids":sorted(cited),"considered_unacquired_ids":sorted({a["evidence_id"] for a in s["evidence_atoms"]}-released),"remaining_budget":max(0,3-sum(next(a["cost"] for a in s["evidence_atoms"] if a["evidence_id"]==e) for e in released)),"declared_loss_rule":load(PROTOCOL)["stopping_loss_rules"][s["scenario_id"]],"uncertainty":str(trial["final"].get("uncertainty","No uncertainty statement emitted.")),"terminal_choice":"artifact" if trial["artifact_valid"] else "abstain"},"terminal_consequence":{"action_or_artifact":f"Retained terminal JSON for {row['attempt_id']}","endpoint_evidence_locators":[f"pilots/evidence-acquisition-matched-agent-v1/execution/attempts/{row['attempt_id']}/trial/outputs/turn-{trial['launcher_invocations']}.json",f"pilots/evidence-acquisition-matched-agent-v1/execution/attempts/{row['attempt_id']}/grade.json"],"decision_loss":trial["grade"]["decision_loss"],"severe_omissions":[x.replace("_","-") for x in trial["grade"]["severe_omissions"]],"resource_cost":3-trial.get("remaining_budget",0) if "remaining_budget" in trial else len(released),"claim_scope":"internal_agent_validation_only"}}

def build_package(repeat:int,p:dict[str,Any],trials:list[dict[str,Any]])->dict[str,Any]:
    provenance=[{"path":"papers/agent-benchmarks/2026-07-15-oncorounds-information-seeking-validity.md","sha256":sha(ROOT/"papers/agent-benchmarks/2026-07-15-oncorounds-information-seeking-validity.md"),"locator":"Unique insight and cross-domain pilot design","role":"design_evidence"},{"path":"pilots/evidence-acquisition-matched-agent-v1/protocol.json","sha256":sha(PROTOCOL),"locator":"prospectively frozen matrix","role":"frozen_instrument"}]
    scenarios=[]
    for sid,path in SCENARIO_PATHS.items():
        s=load(path);rows=[r for r in p["schedule"]["rows"] if r["repeat"]==repeat and r["scenario_id"]==sid];eps=[]
        for row in rows:
            trial=next(t for t in trials if t["attempt_id"]==row["attempt_id"]);provenance.append({"path":f"pilots/evidence-acquisition-matched-agent-v1/execution/attempts/{row['attempt_id']}/trial-report.json","sha256":sha(EXEC/"attempts"/row["attempt_id"]/"trial-report.json"),"locator":"retained configured-agent attempt","role":"execution_evidence"});eps.append(episode(row,trial,s))
        atoms=[{"evidence_id":a["evidence_id"],"description":a["description"],"provenance":{"source_id":"synthetic-builder-source","locator":f"instrument.scenarios.{sid}.{a['evidence_id']}","authority":a["authority"],"valid_at":"2026-07-15T00:00:00Z"},"availability":a["availability"],"decision_value":a["decision_value"],"cost":a["cost"],"delay_steps":a["delay_steps"],"risk":a["risk"],"redundancy_group":None,"dependency_ids":[],"contradicts_ids":[],"minimal_set_member":a["minimal_set_member"]} for a in s["evidence_atoms"]]
        scenarios.append({"scenario_id":sid,"work_shape":s["work_shape"],"task_ref_id":f"task.synthetic.{sid}.v1","frozen_target":s["target"],"evidence_atoms":atoms,"episodes":eps})
    return {"schema_version":"0.1.0","package_id":f"evidence-acquisition-agent-repeat-{repeat}","status":"internal_agent_validation_only","provenance":provenance,"reused_contract_refs":{"task_ids":["task.synthetic.vendor-disposition.v1","task.synthetic.segment-release.v1"],"check_ids":["check.endpoint-consequence.v1","check.stopping-ledger.v1"],"grader_ids":["grader.synthetic-acquisition.v1"],"task_health_ids":[],"metric_ids":[],"validity_argument_ids":[]},"conditions":[{"condition_id":"active","delivery_mode":"on_request","agent_may_request":True,"supply_rule":"Frozen deterministic parser/access policy.","feedback_policy":"evaluator_outputs_firewalled_until_terminal"},{"condition_id":"full_information","delivery_mode":"all_admissible_at_start","agent_may_request":False,"supply_rule":"All admissible/delayed atoms supplied.","feedback_policy":"evaluator_outputs_firewalled_until_terminal"},{"condition_id":"expert_minimal","delivery_mode":"frozen_minimal_set_at_start","agent_may_request":False,"supply_rule":"Builder-authored synthetic minimal set only; no expert approval.","feedback_policy":"evaluator_outputs_firewalled_until_terminal"}],"scenarios":scenarios,"claim_limits":{"supported":["Retained exact internal configured-agent transitions under the frozen synthetic instrument."],"unsupported":UNSUPPORTED}}

def report(p:dict[str,Any],trials:list[dict[str,Any]])->dict[str,Any]:
    shapes={}
    for sid in SCENARIO_PATHS:
        cells={}
        for cond in ("active","full_information","expert_minimal"):
            xs=[t for t in trials if t["scenario_id"]==sid and t["condition_id"]==cond];eligible=[t for t in xs if t["service_valid"] and t["cost_valid"] and t["environment_valid"] and t["artifact_valid"]]
            cells[cond]={"intended":2,"eligible":len(eligible),"inquiry_selection":{"request_counts":[len(t["requests"]) for t in xs]},"access":{"released_counts":[len(t["released_ids"]) for t in xs]},"adoption":{"used_evidence_counts":[len(t["final"].get("evidence_ids",[])) for t in xs]},"stopping":{"reasons":[t["final"].get("stop_reason") for t in xs]},"endpoint_quality":[t["grade"]["endpoint_quality"] for t in eligible],"cost":{"total_tokens":[sum(u.get("total_tokens",0) or 0 for u in t["usage"]) for t in xs],"resource_cost":[len(t["released_ids"]) for t in xs]},"severe_omission":{"counts":[len(t["grade"]["severe_omissions"]) for t in eligible]},"attempt_ids":[t["attempt_id"] for t in xs]}
        shapes[sid]=cells
    return {"protocol":{"path":"pilots/evidence-acquisition-matched-agent-v1/protocol.json","sha256":sha(PROTOCOL)},"denominators":{"intended":12,"service_valid":sum(t["service_valid"] for t in trials),"environment_valid":sum(t["environment_valid"] for t in trials),"artifact_valid":sum(t["artifact_valid"] for t in trials)},"shapes_reported_separately":shapes,"no_pooled_effect":True,"claim_boundaries":p["claim_boundaries"],"interpretation":"Exact internal synthetic configured-agent observations only; n=2 purposive repeats per cell do not license causal, capability, expert, professional, safety, readiness, representativeness, or cross-domain claims."}

def execute()->dict[str,Any]:
    pre=canary();verified=verify_protocol(True)
    if not pre["passed"] or not verified["passed"]:result={"status":"blocked_before_model_calls","preflight":pre,"protocol":verified,"model_calls":0};dump(HERE/"feasibility-report.json",result);return result
    if EXEC.exists():raise FileExistsError("execution exists; retries forbidden")
    EXEC.mkdir();p=load(PROTOCOL);trials=[]
    for row in p["schedule"]["rows"]:trials.append(run_attempt(p,row))
    for repeat in (1,2):dump(EXEC/f"episode-repeat-{repeat}.json",build_package(repeat,p,trials))
    result=report(p,trials);dump(EXEC/"study-report.json",result);return result

def replay()->dict[str,Any]:
    p=load(PROTOCOL);trials=[load(EXEC/"attempts"/r["attempt_id"]/"trial-report.json") for r in p["schedule"]["rows"]]
    rebuilt=report(p,trials)
    if rebuilt!=load(EXEC/"study-report.json"):raise ValueError("study report replay mismatch")
    for repeat in (1,2):
        rebuilt_package=build_package(repeat,p,trials)
        if rebuilt_package!=load(EXEC/f"episode-repeat-{repeat}.json"):raise ValueError(f"episode repeat {repeat} replay mismatch")
    return rebuilt

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("mode",choices=["preflight","execute","replay"]);args=ap.parse_args();result=canary() if args.mode=="preflight" else execute() if args.mode=="execute" else replay();print(json.dumps({"mode":args.mode,"status":result.get("status","verified"),"passed":result.get("passed",result.get("status")!="blocked_before_model_calls"),"denominators":result.get("denominators")},indent=2));return 0 if result.get("passed",result.get("status")!="blocked_before_model_calls") else 1
if __name__=="__main__":raise SystemExit(main())
