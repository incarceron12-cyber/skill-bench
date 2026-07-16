# Grounded harness event-projection conformance

This is a **zero-call, builder-authored internal conformance pilot** for the runtime boundary between canonical world events and agent-visible harness views. It does not run or evaluate an agent, simulate expert testimony, or establish professional task validity.

## Charter fit and useful completion

- **Objectives:** B (expertise-to-evaluation methodology) and C (executable benchmark infrastructure).
- **Mode:** bounded building and validation.
- **General hypothesis:** an agent-facing harness view is auditable only when each visible claim cites one immutable executor/environment/verifier event and every omission is explicit, typed, and allowed by the frozen view policy.
- **Artifact/evidence:** two unlike builder-authored event ledgers, twelve matched derived views, twenty-two replay cases, a deterministic validator, tests, and a generated report.
- **Uncertainty clarified:** whether runtime event projection can fail closed on evidence invention and omission without duplicating the existing source-to-task projection contract.
- **Useful completion:** all clean controls pass while balanced planted failure, repair, verifier-result, action-result, relabeling, reordering, and undeclared-omission defects are localized.

This slice is deliberately cross-domain in work shape: one structured allocation artifact includes a grounded failure/repair sequence; one evidence-to-decision memo includes authority ordering and a blocked action. These are contract-calibration examples, not claims that either workflow is professionally representative.

## Runtime boundary

The fixture separates three layers:

1. **Canonical world truth:** append-only, hash-pinned events produced by the source pack, deterministic executor, environment, artifact store, verifier, and outcome grader.
2. **Agent evidence:** one of six views, where every visible entry preserves its source event ID, event kind, canonical payload/hash, rendered bytes/hash, and representation type. Missing events require a source hash and policy-authorized omission reason.
3. **Response and endpoints:** agent response, action, artifact, outcome, and optional elicited belief report remain separate. The zero-call pilot collects no agent response or belief report; a belief report is explicitly secondary diagnostic evidence.

This begins **after task construction**. `tests/fixtures/valid-task-projection-manifest.json` remains the source-to-task requirement/projection contract. The reusable integration path is to export real benchmark-bundle trace events into this canonical ledger envelope, then run the audit before treating a rendered transcript as valid agent evidence. The pilot does not add another task-IR schema.

## Frozen views

Each scenario derives the same six policies from one canonical ledger:

- `raw`: lossless, ordered control;
- `structured`: lossless structured-envelope control;
- `blocked_log`: lossless control that retains blocked branches;
- `repair_collapsed`: may omit only `failure` and `repair` events with `repair_collapse` reasons; it cannot invent a net success;
- `verification_masked`: may omit only `verifier_result` events with `verification_mask` reasons;
- `cost_pruned`: may omit only `observation` events with `cost_pruning` reasons.

The validator checks lineage and omission authorization, not semantic equivalence of arbitrary natural-language summaries. Real renderers need additional metamorphic or human validation before a structured paraphrase can be called meaning-preserving.

## Defects and endpoints

The conformance corpus has twelve clean controls (six per work shape) and ten balanced planted defects (five per shape). It explicitly rejects:

- invented failure and repair events;
- invented verifier success and action results;
- a valid event relabeled as another kind;
- reordered event/authority presentation;
- an event silently dropped without an omission record;
- canonical payload drift, stale hashes, and unauthorized omission reasons (mutation tests).

Reports preserve action, artifact, formal outcome, agent response, and elicited-report endpoint families rather than aggregating them into one harness score.

## Provenance and claim boundary

Design fields map to the full local review of *Harness-Induced Belief Divergence*, especially its visibility-state model, matched-world recommendation, warning against fabricated repair/verifier events, and concrete repository actions:

- `papers/agent-benchmarks/2026-07-17-harness-induced-belief-divergence-validity.md`
- `data/papers/pdfs/2607.04528v1-harness-induced-belief-divergence.pdf`

The fixture pins those files and the adjacent source-to-task projection fixture by SHA-256. The reviewed paper provides prompt-mediated self-report evidence, not environment-grounded behavior evidence; this pilot therefore uses no reported paper outcome as ground truth.

Supported claim: the repository validator distinguishes the declared clean and planted builder-authored cases. Unsupported claims include agent capability, belief validity, behavioral mediation, harness treatment effects, artifact quality, task-success prevalence, professional validity, cross-domain generalization, production fitness, and deployment readiness.

## Reproduce

```bash
python scripts/build_event_projection_fixture.py
python scripts/validate_event_projection_conformance.py \
  pilots/harness-event-projection-conformance/conformance.json \
  --check-paths \
  --report pilots/harness-event-projection-conformance/report.json
python -m unittest tests.test_event_projection_conformance -v
```

The generator makes fixture construction and all hashes reproducible. `report.json` is generated evidence, not an empirical trial result.
