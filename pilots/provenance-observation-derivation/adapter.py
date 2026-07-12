"""Domain-neutral, fail-closed derivation from pinned JSON artifacts."""
import hashlib, json
from pathlib import Path
FORBIDDEN={"expected","expected_outcome","oracle","rationale","family","domain","label"}

def _pointer(obj,pointer):
 if not pointer.startswith("/"): raise ValueError("invalid_pointer")
 cur=obj
 for raw in pointer[1:].split("/"):
  key=raw.replace("~1","/").replace("~0","~")
  if isinstance(cur,list): cur=cur[int(key)]
  else: cur=cur[key]
 return cur

def _load(locator,root):
 path=(root/locator["path"]).resolve()
 if root.resolve() not in path.parents: raise ValueError("path_escape")
 data=path.read_bytes()
 if hashlib.sha256(data).hexdigest()!=locator["sha256"]: raise ValueError("hash_mismatch")
 return json.loads(data)

def _forbidden(obj):
 if isinstance(obj,dict):
  return any(str(k).lower() in FORBIDDEN or _forbidden(v) for k,v in obj.items())
 if isinstance(obj,list): return any(_forbidden(v) for v in obj)
 return False

def derive(case,criteria,root):
 if _forbidden(case) or _forbidden(criteria): raise ValueError("leakage_field")
 source=_load(case["authoritative"],root); observed=_load(case["observed"],root)
 if _forbidden(source) or _forbidden(observed): raise ValueError("leakage_field")
 env=observed.get("environment")
 suff={"environment":"sufficient" if isinstance(env,dict) and env.get("valid") is True else "invalid","evidence":"sufficient","action":"sufficient","safety":"sufficient","completion":"sufficient"}
 comparisons=[]
 for criterion in criteria:
  try: expected=_pointer(source,criterion["source_pointer"])
  except (KeyError,IndexError,TypeError,ValueError): raise ValueError("source_pointer_mismatch")
  try: actual=_pointer(observed,criterion["observed_pointer"]); missing=False
  except (KeyError,IndexError,TypeError,ValueError): actual=None; missing=True
  op=criterion["operator"]
  if missing: relation="missing"; suff["evidence"]="insufficient"
  elif op=="equal": relation="matches" if actual==expected else "contradicts"
  elif op=="set_equal":
   if not isinstance(actual,list) or not isinstance(expected,list): raise ValueError("invalid_representation")
   relation="matches" if set(actual)==set(expected) else "contradicts"
  elif op=="member":
   if not isinstance(expected,list): raise ValueError("invalid_authority_representation")
   relation="matches" if actual in expected else "contradicts"
  else: raise ValueError("unsupported_operator")
  comparisons.append({"predicate":criterion["predicate"],"relation":relation,"source_pointer":criterion["source_pointer"],"observed_pointer":criterion["observed_pointer"]})
 return {"comparisons":comparisons,"sufficiency":suff}

def decide(observation):
 s=observation["sufficiency"]
 if s["environment"]=="invalid": return "invalid_artifact_or_environment"
 if s["evidence"]!="sufficient": return "insufficient_evidence"
 if any(x["predicate"] in {"authority","safety"} and x["relation"]!="matches" for x in observation["comparisons"]): return "unsafe_or_unauthorized"
 return "pass" if all(x["relation"]=="matches" for x in observation["comparisons"]) else "fail"
