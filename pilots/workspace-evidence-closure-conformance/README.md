# Workspace evidence-closure conformance slice

This is a **domain-neutral internal calibration artifact**, not a paper-replication benchmark. It operationalizes the distinction between a closed record graph and substantive evidence closure identified in the full review at `papers/agent-benchmarks/2026-07-17-paper-replication-workspace-evidence-validity.md` and its executed release audit at `data/sources/releases/2607.02134v2-paper-replication/release-audit.json`.

## Charter fit and bounded hypothesis

- **Objective:** charter B/C—turn expertise/evidence-transfer design into executable, diagnostically separate checks.
- **Artifact:** one frozen obligation inventory, a base workspace, eight declarative cases, a replay validator, tests, and a machine-readable report.
- **Uncertainty:** whether record closure, predicate execution, obligation denominator coverage, source entailment, execution-to-byte lineage, native-artifact validity, and report freshness can fail independently.
- **Mode:** building plus validation.
- **Anti-narrowing:** the payload is deliberately a generic numeric record and decision label. The machinery applies to memos, spreadsheets, models, investigations, software outputs, or scientific artifacts; it does not introduce a scientific-replication ontology.
- **Useful completion:** all six planted failures are detected at their predeclared layer, the baseline and a different valid implementation pass, and every scientific/professional/reliability/effect/readiness claim remains false.

## Design

`fixture.json` freezes two independently authored obligations before case execution. Its canonical inventory hash makes the denominator immutable. The base workspace then carries separate records for:

1. declared targets and record closure;
2. executable predicates evaluated from accepted payloads;
3. obligation-to-target coverage or reviewed exclusion;
4. source locator, quoted proposition, and entailment review;
5. execution output hash → accepted hash → current payload hash;
6. native required-key validity; and
7. substantive report finding/caveat coverage plus report-source → rendered-artifact freshness.

The cases are mutations of one base workspace, so unrelated evidence remains fixed. `legitimate-alternative-implementation` changes implementation and values while preserving the frozen semantic predicates; this prevents exact witness bytes from becoming the only accepted path.

## Relationship to existing contracts

This slice reuses existing project semantics rather than extending `benchmark-bundle.schema.json`:

- bundle checks already cover artifact/check identities, executable outcomes, and artifact-view admissibility;
- task health owns immutable version revisions and defect adjudication;
- validity arguments own which interpretations or decisions measurements license;
- provenance-boundary tooling owns historical/live dependency identity;
- native/temporal artifact pilots already separate native, rendered, and transformed evidence views.

What was missing was a compact negative-control replay joining those boundaries around an independently frozen obligation denominator. A new general schema would duplicate those contracts and prematurely promote this calibration fixture into an ontology. `run.py` therefore remains a small conformance validator with strict fields and fail-closed statuses.

## Evidence mapping

| Planted case | Expected layer | Source basis |
|---|---|---|
| target omission | `obligation_closure` | Review lines 159–163; release audit `/mutation_probes/0` |
| numerically failing predicate | `predicate_closure` | Review lines 165–169; audit `/mutation_probes/1` |
| stale execution hash | `byte_lineage` | Review lines 177–181; audit `/mutation_probes/3` |
| vacuous source trace | `source_entailment` | Review lines 183–187; audit `/mutation_probes/4` |
| locator-only report | `report_handoff` | Review lines 171–175; audit `/mutation_probes/2` |
| stale render | `report_handoff` | Review lines 293–294; report-freshness repair requirement |
| alternative implementation | no failure | Review lines 289–296; freeze consequences, not one witness path |

The local source paths, SHA-256 values, and section/JSON-pointer locators are preserved in `fixture.json` and checked on every replay.

## Run

```bash
python pilots/workspace-evidence-closure-conformance/run.py \
  --write-report pilots/workspace-evidence-closure-conformance/report.json
python -m unittest tests.test_workspace_evidence_closure_conformance
```

`report.json` is the retained machine-readable result. It reports each layer separately; it does not aggregate closure into a capability or readiness score.
