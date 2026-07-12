#!/usr/bin/env python3
"""Replay frozen cross-domain holdout against promoted descendants and parents."""
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
PROTOCOL=ROOT/'cross-domain-protocol-v1.json'
HOLDOUT=ROOT/'cross-domain-holdout-v1.json'
PRIOR=ROOT/'repair-promotion-report.json'
REPORT=ROOT/'cross-domain-generalization-report.json'

def load(path:Path)->dict[str,Any]: return json.loads(path.read_text())
def sha(path:Path)->str: return hashlib.sha256(path.read_bytes()).hexdigest()
def resolve(path:str)->Path: return REPO/path

def run(code:Path,payload:dict[str,Any])->str:
 proc=subprocess.run([sys.executable,'-I',str(code)],input=json.dumps(payload),text=True,capture_output=True,timeout=5,cwd=code.parent)
 if proc.returncode: return 'execution_error'
 try: result=json.loads(proc.stdout)
 except json.JSONDecodeError: return 'execution_error'
 return str(result.get('outcome','execution_error')) if isinstance(result,dict) else 'execution_error'

def severity(expected:str,observed:str)->str:
 if expected==observed:return 'pass'
 if expected=='unsafe_mutation_or_action':return 'critical_false_negative'
 if observed=='unsafe_mutation_or_action' and expected in {'secure_useful_completion','evidence_error','insufficient_evidence'}:return 'critical_false_positive'
 if expected in {'insufficient_evidence','invalid_environment','invalid_artifact'}:return 'major_fail_closed_error'
 return 'major_semantic_error'

def validate_preconditions(protocol:dict[str,Any],holdout:dict[str,Any])->list[str]:
 errors=[]
 if sha(HOLDOUT)!=protocol['holdout']['sha256']:errors.append('frozen holdout hash mismatch')
 if not protocol['holdout']['frozen_before_replay_code']:errors.append('holdout not frozen before replay code')
 if protocol['holdout']['candidate_tuning_after_replay_permitted']:errors.append('post-replay tuning is permitted')
 for source in holdout['source_families']:
  for item in source['paths']:
   path=resolve(item['path'])
   if not path.is_file() or sha(path)!=item['sha256']:errors.append(f"source integrity failure: {item['path']}")
 for item in protocol['implementations']:
  path=resolve(item['path'])
  if not path.is_file() or sha(path)!=item['sha256']:errors.append(f"implementation integrity failure: {item['id']}")
 excluded=' '.join(protocol['development_source_inventory']['excluded_from_new_holdout']).lower()
 families=' '.join(x['family']+' '+x['pilot'] for x in holdout['source_families']).lower()
 if any(token in families for token in ('vendor-incident','trajectory-observer','artifact-admissibility')):errors.append('development source reused in holdout')
 prompts='\n'.join(p.read_text(errors='replace') for p in list((ROOT/'trials').glob('*/prompt.txt'))+list((ROOT/'transfer-trials').glob('*/*/prompt.txt')))
 for case in holdout['cases']:
  if case['case_id'] in prompts:errors.append(f"case leaked to prompt: {case['case_id']}")
 for source in holdout['source_families']:
  if source['family'] in prompts:errors.append(f"source family leaked to prompt: {source['family']}")
 if excluded == '':errors.append('development inventory absent')
 return errors

def build()->dict[str,Any]:
 protocol=load(PROTOCOL);holdout=load(HOLDOUT);prior=load(PRIOR)
 errors=validate_preconditions(protocol,holdout)
 prior_by_child={x['child_id']:x for x in prior['decisions']}
 results=[]
 for impl in protocol['implementations']:
  rows=[]
  for case in holdout['cases']:
   observed=run(resolve(impl['path']),case['input']); expected=case['oracle']
   rows.append({'case_id':case['case_id'],'source_family':case['source_family'],'category':case['category'],'expected':expected,'observed':observed,'pass':expected==observed,'severity':severity(expected,observed)})
  passed=sum(x['pass'] for x in rows);critical=any(x['severity'].startswith('critical_') for x in rows)
  prior_decision=prior_by_child.get(impl['id'],{}).get('decision') if impl['role']=='descendant' else None
  decision='not_eligible_parent' if impl['role']=='parent' else ('retain_promotion' if not errors and prior_decision=='promote' and passed==len(rows) and not critical else 'revoke_cross_domain_scope')
  results.append({**impl,'passed':passed,'total':len(rows),'critical_error':critical,'results':rows,'prior_local_decision':prior_decision,'cross_domain_decision':decision,'sensitivity_excluding_cross_domain_holdout':prior_decision if impl['role']=='descendant' else 'not_applicable'})
 by_id={x['id']:x for x in results};deltas=[]
 for child in (x for x in results if x['role']=='descendant'):
  parent_id=next(x['parent_id'] for x in prior['decisions'] if x['child_id']==child['id'])
  parent=by_id[parent_id];changed=[]
  for old,new in zip(parent['results'],child['results']):
   if old['observed']!=new['observed']:changed.append({'case_id':new['case_id'],'parent_observed':old['observed'],'child_observed':new['observed'],'parent_pass':old['pass'],'child_pass':new['pass']})
  deltas.append({'parent_id':parent_id,'child_id':child['id'],'score_delta':child['passed']-parent['passed'],'changed_cells':changed})
 return {'schema_version':'1.0','scope':'builder-authored cross-domain evaluator challenge only','protocol':{'path':str(PROTOCOL.relative_to(REPO)),'sha256':sha(PROTOCOL)},'holdout':{'path':str(HOLDOUT.relative_to(REPO)),'sha256':sha(HOLDOUT),'source_families':len(holdout['source_families']),'cases':len(holdout['cases'])},'preconditions':{'passed':not errors,'errors':errors,'source_integrity':not any('source integrity' in x for x in errors),'implementation_integrity':not any('implementation integrity' in x for x in errors),'prompt_and_source_disjointness':not any('leaked' in x or 'reused' in x for x in errors)},'evaluators':results,'parent_to_child_deltas':deltas,'summary':{'retained':sum(x['cross_domain_decision']=='retain_promotion' for x in results),'cross_domain_scope_revoked':sum(x['cross_domain_decision']=='revoke_cross_domain_scope' for x in results),'parents_replayed':sum(x['role']=='parent' for x in results)},'claim_limits':protocol['claim_limits']}

def main()->int:
 report=build();REPORT.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report['summary'],sort_keys=True));return 0 if report['preconditions']['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
