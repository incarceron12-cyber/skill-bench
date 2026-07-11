# Information-flow entitlement contract

This focused contract implements the PiSAs review's cross-domain distinction between source trust/task relevance and permission to access, use, disclose, or retain an information atom. It advances charter objectives B/C with executable diagnostic machinery; it is not a privacy-only benchmark.

## Reuse and boundary

The package links rather than replaces `benchmark-bundle.schema.json` (trials, traces, surfaces), `expert-participation.schema.json` (consent), and `experience-memory-transfer` fixtures (persistent memory). Its smallest new object is:

`atom × subject/source × purpose × recipient × representation × valid time × surface → operation outcome`.

Access does not imply use; use does not imply disclosure; disclosure does not imply retention. A derived representation must name a provenance-preserving transformation, preserve the needed operational consequence, suppress the raw fingerprint, and be authorized for the recipient. Validation unions all observations across messages, memory, tool arguments, artifacts, and responses, so moving raw detail into shared memory remains a violation.

## Evidence and claim boundary

Design evidence: `papers/agent-benchmarks/2026-07-11-pisas-contextual-integrity.md`, especially pp. 3–5 (dual labels), pp. 7–8 and 19–20 (surface substitution), and pp. 19–21/26–27 (decision-critical private attributes and sanitized forms). Immutable source: `data/papers/pdfs/2607.05318v1-pisas-contextual-integrity.pdf`.

The fixture is builder-authored synthetic contract calibration. It tests deterministic policy semantics only. It does not validate organizational norms, professional decisions, leak-detector accuracy, capability, deployment safety, or release readiness.

## Run

```bash
python scripts/validate_information_flow_entitlements.py schemas/fixtures/information-flow-entitlement-conformance.json --check-paths
python -m unittest tests.test_information_flow_entitlements
```
