# Disposition–realization crosswalk v1

This versioned internal conformance package advances Charter objectives B and C by testing a reusable cross-domain hypothesis: **choosing the right terminal class is distinct from realizing either the action or the handoff correctly**. It crosses `proceed | defer` with `valid | invalid` over two unlike retained knowledge-work shapes—an authority-bounded synthetic incident action and an analysis-to-procurement decision handoff. It does not make either domain the benchmark's scope.

## Immutable evidence and provenance

`manifest.json` binds every reused parent file by repository path and SHA-256. Every credited value is selected through a JSON Pointer in a replay assertion; the producer-to-consumer transport edge is additionally checked by byte hash. The design basis includes the pinned Escalation Bench release audit and its full release review. The crosswalk reads but never modifies the retained action-boundary and handoff-usability records.

The two invalid cells are explicitly builder-planted controls, not altered historical outcomes:

- `proceed--invalid` keeps the observed proceed disposition but substitutes a wrong incident target (`INC-205` instead of authorized `INC-204`);
- `defer--invalid` keeps the intended defer class but plants a wrong recipient and absent transport receipt.

## Replay semantics

`replay.py` emits separate outcomes for:

1. `boundary_judgment`;
2. `proceed_realization`;
3. `handoff_construction`;
4. `handoff_transport`;
5. `continuation`;
6. `consequence`; and
7. `observer_sufficiency`.

Assertions return `pass`, `fail`, `not_applicable`, or `insufficient_evidence`. The last status is deliberate and fail-closed: the action parent has no external receipt, rollback execution, postcondition, or consequence record; the handoff parent has no observed act-versus-defer choice, authorized/available human recipient, human receipt/response, delay, burden, or downstream-impact record.

The retained proceed row passes boundary and exact target/parameter/effect checks, while its continuation, consequence, and observer sufficiency remain insufficient. The retained handoff row passes construction, byte-identical producer/consumer transport, and configured-agent continuation, while boundary judgment, human consequence, and observer sufficiency remain insufficient. The planted controls fail only their realization layers and do not fabricate later outcomes.

## Reproduction

```bash
python pilots/disposition-realization-crosswalk/v1/replay.py --check
python -m unittest tests.test_disposition_realization_crosswalk -v
```

The replay makes zero model calls and is byte-stable. `replay-report.json` records all parent hash checks, exact assertion results, the complete 2×2 matrix, and strict claim ceilings.

## Claim ceiling

This package demonstrates only deterministic internal crosswalk behavior on immutable retained observations and builder-planted controls. It supports no agent-capability, safety, professional-validity, human-handoff-success, production, readiness, cross-domain-generalization, treatment-effect, or historical-regrade claim. In particular, a configured downstream agent writing an artifact is not evidence of a qualified human receiving, understanding, adopting, or benefiting from a handoff.
