# Handoff-usability conformance slice

This internal synthetic calibration slice operationalizes the handoff-centered mapping in `docs/benchmark-design-taxonomy.md` §2.6a, grounded in the immutable full-text review `papers/agent-benchmarks/2026-07-11-design-report-knowledge-work-benchmarks.md` (especially pp. 6–10 and Table C.1, p. 18).

It uses two unlike handoffs: an analysis-to-decision memo and an incident-record-to-operations continuation. Each declares its recipient, next operation, authoritative and prohibited source boundary, required fields, accepted alternatives, and destination conventions. The deterministic grader preserves five dimensions rather than collapsing them:

1. substantive correctness (entailing evidence exists);
2. provenance/boundary integrity (sources are authorized and scope is preserved);
3. destination fit (recipient, format, and fields);
4. recipient usability;
5. next-operation executability.

`missing_evidence` fails closed as `insufficient_evidence`; malformed output is `invalid_artifact`, not substantive failure. The alternate decision brief proves that one reference format is not normative.

Run:

```bash
python pilots/handoff-usability-conformance/grade.py --check-paths
python -m unittest tests.test_handoff_usability_conformance
```

These builder-authored records only test grader semantics. They are not an independent recipient trial and support no expert approval, agent capability, professional validity, downstream-impact, or release-readiness claim.

## Isolated configured-system slice

`launcher.py` reuses the existing bubblewrap/file-only Hermes envelope to run one
predeclared attempt for each handoff shape. The retained `isolated-agent-v3`
records include zero-call preflight canaries, immutable task/source manifests,
redacted stdout traces, artifacts, usage, component hashes, and replayable
five-dimension grader reports. `trials/isolated-agent-v3/diagnostic.md` reports
the bounded cross-case result. Earlier v1/v2 canary failures are retained rather
than silently discarded; they exposed an overly broad canary string matcher.

These runs measure deterministic artifact proxies, not actual recipient use.
They support no human-usability, expert-validity, capability, cross-domain
generalization, treatment-effect, or readiness claim.

`downstream_launcher.py` consumes each frozen v3 handoff in a second isolated
workspace containing no producer source pack, trace, private rubric, or
repository. The predeclared single attempts and invalid outcomes are retained
under `trials/downstream-agent-v1/`; its diagnostic separates an observed
public-path contract defect from producer, environment, and grader evidence.
