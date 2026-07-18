# Pre-task procedure transfer v5: repaired zero-call endpoint freeze

This internal-calibration fork repairs **only** the invalid v4 endpoint instrument. It does not edit or rescore v4. The v4 treatment materials, source families, controls, candidate freeze, and hindsight freeze remain immutable external bindings.

The v5 tasks disclose every required identifier and JSON type in public `input.json` and `public.md` files. Expected consequences are independently recomputed from those public inputs and the frozen v4 source rules. The condition-blind checker enforces typed structure and semantic consequences while accepting any non-empty reason paraphrase.

`fair-basis-crosswalk.json` maps every checked field to its public/source basis. `preflight.py` verifies hashes, endpoint derivation, public basis, checker behavior, assignment parity, zero attempts, all-false claims, and planted arithmetic-contradiction, hidden-literal, hidden-type, and wording-exactness mutations.

Run:

```bash
python pilots/pretask-procedure-transfer-v5/preflight.py --check-paths --report pilots/pretask-procedure-transfer-v5/preflight-report.json
python -m unittest tests.test_pretask_procedure_transfer_v5 -v
```

This freeze authorizes no execution. It makes no transfer, capability, utility, expert-provenance, professional-validity, production-fitness, or readiness claim. Execution requires a separate queue task after review of this pushed freeze.
