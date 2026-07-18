#!/usr/bin/env python3
"""Condition-blind exact endpoint checker; reads no treatment metadata."""
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument("--candidate",type=Path,required=True); p.add_argument("--private",type=Path,required=True); a=p.parse_args()
try:
 candidate=json.loads(a.candidate.read_text()); spec=json.loads(a.private.read_text()); passed=candidate==spec["expected_endpoint"]; reason="exact_endpoint_match" if passed else "endpoint_mismatch"
except (OSError,json.JSONDecodeError,KeyError) as e:
 passed=False; reason="invalid_or_missing_artifact:"+type(e).__name__
print(json.dumps({"passed":passed,"reason":reason},sort_keys=True)); raise SystemExit(0 if passed else 1)
