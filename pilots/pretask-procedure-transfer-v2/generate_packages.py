#!/usr/bin/env python3
"""One-shot, corpus-only package generator for the frozen v2 procedure study.

This launcher deliberately cannot see task or private-key paths. It performs one
provider call per family, retains stdout/stderr/usage/configuration, and never
repairs a generated package. Re-running after an attempt directory exists is
refused so failed attempts cannot be laundered.
"""
from __future__ import annotations
import hashlib, json, os, shutil, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
HERMES=Path('/home/sam/.hermes/hermes-agent'); PY=Path('/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu')
FAMILIES={'family-alpha':HERE/'families/evidence-decision/corpus.json','family-beta':HERE/'families/incident-control/corpus.json'}
INSTRUCTION=json.loads((HERE/'protocol.json').read_text())['source_task_split']['generator_instruction']
PROMPT=(INSTRUCTION+'\nRead corpus.json. Write outputs/package.json as strict JSON with keys schema_version, package_id, family_id, generator_kind, source_corpus_sha256, clauses, contradictions, thresholds, artifact_conventions, failure_signatures, and claim_boundary. Each clause must have id, instruction, and proposition_basis. Copy proposition IDs exactly. Set generator_kind to model_corpus_only_once and claim_boundary to builder-authored source distillation; not expert-approved or professionally validated. Do not mention or infer downstream tasks. Produce no other task artifact.')

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def inv(p): return {x.relative_to(p).as_posix():{'sha256':sha(x),'bytes':x.stat().st_size} for x in sorted(Path(p).rglob('*')) if x.is_file()}
def profile(dst):
 dst.mkdir(parents=True); src=Path(os.environ.get('HERMES_HOME',str(Path.home()/'.hermes'))); auth=Path.home()/'.hermes/auth.json'
 if auth.exists(): shutil.copy2(auth,dst/'auth.json')
 if (src/'.env').exists(): shutil.copy2(src/'.env',dst/'.env')
 (dst/'config.yaml').write_text('model:\n  default: gpt-5.6-sol\n  provider: openai-codex\nagent:\n  max_turns: 20\nplatform_toolsets:\n  cli:\n    - file\n')
def bwrap(inp,out,prof,cmd):
 return ['bwrap','--die-with-parent','--new-session','--unshare-pid','--proc','/proc','--dev','/dev','--tmpfs','/tmp','--ro-bind','/usr','/usr','--ro-bind','/bin','/bin','--ro-bind','/lib','/lib','--ro-bind','/lib64','/lib64','--ro-bind','/etc','/etc','--dir','/run/systemd','--ro-bind','/run/systemd/resolve','/run/systemd/resolve','--dir','/home','--dir','/home/sam','--dir','/home/sam/.local','--dir','/home/sam/.local/share','--dir','/home/sam/.local/share/uv','--dir','/home/sam/.local/share/uv/python','--ro-bind',str(PY),str(PY),'--dir','/opt/hermes','--ro-bind',str(HERMES),'/opt/hermes','--bind',str(prof),'/run/hermes-profile','--ro-bind',str(inp),'/trial','--bind',str(out),'/trial/outputs','--chdir','/trial','--setenv','HOME','/home/sam','--setenv','HERMES_REAL_HOME','/home/sam','--setenv','HERMES_HOME','/run/hermes-profile','--setenv','TERMINAL_CWD','/trial','--setenv','PYTHONPATH','/opt/hermes','--setenv','SSL_CERT_FILE','/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem','--unsetenv','HERMES_CRON_SESSION','--unsetenv','HERMES_SESSION_ID','--unsetenv','HERMES_SESSION_KEY','--',*cmd]
def validate_package(pkg,fid,corpus_hash):
 if pkg.get('family_id')!=fid or pkg.get('generator_kind')!='model_corpus_only_once' or pkg.get('source_corpus_sha256')!=corpus_hash:return False
 corpus=json.loads(FAMILIES[fid].read_text()); ids={p['id'] for p in corpus['propositions']}; clauses=pkg.get('clauses',[])
 return bool(clauses) and {x for c in clauses for x in c.get('proposition_basis',[])}==ids and all(set(c.get('proposition_basis',[]))<=ids for c in clauses)
def run(fid,corpus):
 root=HERE/'generation'/fid
 if root.exists(): raise RuntimeError(f'attempt already exists: {root}')
 inp=root/'inputs'; out=root/'outputs'; prof=root/'.profile'; inp.mkdir(parents=True); out.mkdir(); profile(prof); shutil.copy2(corpus,inp/'corpus.json'); (inp/'outputs').mkdir()
 (root/'prompt.txt').write_text(PROMPT+'\nFrozen corpus SHA-256: '+sha(corpus)+'\nAssigned family_id: '+fid+'\n')
 cmd=['/opt/hermes/venv/bin/python','/opt/hermes/venv/bin/hermes','-z',(root/'prompt.txt').read_text(),'--usage-file','/trial/outputs/usage.json','--model','gpt-5.6-sol','--provider','openai-codex','--toolsets','file','--safe-mode']
 p=subprocess.run(bwrap(inp,out,prof,cmd),text=True,capture_output=True,timeout=900); (root/'stdout.log').write_text(p.stdout); (root/'stderr.log').write_text(p.stderr); shutil.rmtree(prof,ignore_errors=True)
 ok=False
 try: ok=p.returncode==0 and validate_package(json.loads((out/'package.json').read_text()),fid,sha(corpus))
 except Exception: pass
 report={'family_id':fid,'valid':ok,'returncode':p.returncode,'model':'gpt-5.6-sol','provider':'openai-codex','toolsets':['file'],'safe_mode':True,'prompt_sha256':sha(root/'prompt.txt'),'corpus_sha256':sha(corpus),'input_inventory':inv(inp),'output_inventory':inv(out),'stdout_sha256':sha(root/'stdout.log'),'stderr_sha256':sha(root/'stderr.log'),'attempts':1,'repair_attempts':0}
 (root/'report.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n'); return ok
if __name__=='__main__':
 ok=True
 for fid,p in FAMILIES.items():
  try: ok=run(fid,p) and ok
  except Exception as e: print(e,file=sys.stderr); ok=False
 print(json.dumps({'passed':ok,'package_generation_attempts':2},indent=2)); raise SystemExit(0 if ok else 1)
