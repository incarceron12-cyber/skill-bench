# Synthetic API transition and score transport

This bounded zero-call validation slice tests a general benchmark-design hypothesis from the AutomationBench audit: **internal executable-state conformance does not establish that transition semantics or grader verdicts transport to an independently specified behavior surface**. It advances charter objectives B and C through validation and executable infrastructure; it is not a SaaS or HTTP benchmark scope commitment.

## Frozen experiment

`suite.json` freezes one small conditional-resource API, one initial state, seven action sequences, 27 consequence criteria, read sets, invalid-run policy, and claim ceiling. Both adapters receive exactly the same inputs:

1. normal conditional mutation;
2. bearer-token authorization denial;
3. duplicate PUT retry/idempotency;
4. stale conditional read;
5. concurrent update from a stale ETag;
6. invalid payload; and
7. legitimate JSON Merge Patch route.

`ReferenceAdapter` is a local executable interpretation of cited RFC behavior. `SyntheticAdapter` is an intentionally simplified benchmark world with planted omissions: it ignores authorization, conditional GET, and `If-Match`, and emits a second revision/audit effect for an identical retry. The reference is independent of the synthetic transition code but **is not a live service, production oracle, or certification of RFC conformance**.

## Evidence and rationale

`provenance.json` records official RFC URLs, fetched-text hashes, exact sections, and project adaptations. RFC 9110 supplies PUT idempotent intent, ETag preconditions, and 412 behavior; RFC 7396 supplies the alternative partial-update shape; RFC 6750 supplies invalid bearer-token denial semantics. Resource fields, audit behavior, revision policy, criteria, and professional interpretation remain builder-authored design hypotheses. The source review is `papers/agent-benchmarks/2026-07-15-automationbench-workflow-projection-validity.md`, especially lines 127–155 and 204–222.

The runner emits complete pre/post state hashes and transition diffs, criterion read sets, changed-path observer coverage, response sequences, strict conjunctions, criterion-level verdicts, and cross-adapter transport. Expected protocol rejection (400/401/412/304) is a valid observed outcome; only adapter exceptions or missing typed responses are invalid runs and are excluded from the strict denominator while remaining reported.

## Replay

```bash
python pilots/synthetic-api-transition-transport/run.py
python -m unittest tests.test_synthetic_api_transition_transport -v
```

The committed `report.json` must be byte-identical to a fresh replay. Tests also mutate the suite to prove that a stale conditional write, unobserved transition, or unsupported reference expectation fails closed.

## Claim ceiling

The package licenses only claims about exact deterministic behavior of these seven frozen builder-authored cases. It does not establish production API fidelity, representative workflow dynamics, complete consequence coverage, expert/professional validity, agent capability, prevalence, safety, or deployment readiness. A real-service contract test and affected-party consequence validation would be required before raising that ceiling.
