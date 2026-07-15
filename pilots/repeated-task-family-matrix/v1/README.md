# Repeated task-family matrix v1

This internal synthetic pilot prospectively freezes four task forms in two unlike knowledge-work families, with two exact-configured-system repeats per form. It tests reusable reliability machinery: separate service/trial denominators, deterministic severity-aware grading, within-form repeat observations, and between-family descriptive transport boundaries.

The forms are builder-authored hypotheses, not expert testimony or professional simulations. Their authority, supersession, threshold, and bounded-action patterns derive from the retained vendor-incident and cross-pilot v2 instruments. `protocol.json` records exact provenance status, hashes, schedule, gates, and claim ceilings.

Workflow:

```bash
python run_matrix.py preflight                 # zero model calls
# commit and push every frozen instrument byte
python run_matrix.py preflight --require-pushed
python run_matrix.py execute                   # refuses unless origin/main matches
python run_matrix.py replay
```

Execution is one-shot: no retries, replacement, post-outcome tuning, or outcome-based admission. Missing provider confidence/logprob channels are recorded as `insufficient_evidence`, never inferred.
