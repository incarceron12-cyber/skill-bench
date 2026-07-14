# Procedure-package conformance contract v0.1

`procedure-package.schema.json` and
`scripts/validate_procedure_package.py` provide a small, format-agnostic adapter
for checking whether a generated procedure/data/tool/oracle package is internally
coherent. It is **not** an SOP-specific benchmark and does not establish that the
procedure is professionally correct.

The package sits between existing authoring and measurement records:

```text
expertise-transfer / task-IR projection
  → procedure-package manifest and replay
  → benchmark-bundle trace, artifact/check observations
  → task health and claim-centered validity
```

It therefore reuses those boundaries rather than replacing them: source claims
and clause basis remain provenance records; accepted events and artifacts remain
observations; runtime, endpoint, and procedure verdicts remain separate; broader
interpretations still require task-health and validity evidence.

## Executable boundaries

The validator:

1. types every package field as public input, hidden evidence, tool result,
   scored endpoint, audit metadata, or prohibited oracle and binds each role to
   one permitted surface;
2. requires metadata and observed columns plus manifest/loaded row counts to
   match exactly, and rejects unresolved merge-conflict markers;
3. freezes generator, loader, runtime, oracle, seed, and time identities;
4. rejects ignored required tool arguments, answer-bearing or prohibited-oracle
   returns, and divergent repeated replay digests;
5. requires an independently versioned, non-circular endpoint derivation and
   exactly one type-compatible comparator per scored endpoint; substring
   matching and null-like collapse are prohibited;
6. links public, provenance-backed clauses through ordering, gate, fallback, and
   declared alternative-path relations;
7. replays tool-call argument/runtime evidence, endpoint equality from the final
   artifact only, relation satisfaction, accepted paths, and joint status; and
8. keeps runtime execution, endpoint agreement, and procedure conformance
   separate, so an endpoint-correct but skipped-gate trace fails the joint policy.

## Internal calibration fixture

`schemas/fixtures/procedure-package-conformance.json` is builder-authored
contract calibration. It imports no SOP-Bench task or answer data. Five cases
cover:

- a canonical path;
- a declared hold alternative;
- an endpoint-correct trace that skips a triggered approval gate;
- an endpoint-correct trace with wrong ordering; and
- an untriggered fallback followed despite an endpoint match.

The fixture retains explicit non-claims for expert approval, professional
correctness, agent capability, safety, production fitness, and deployment
readiness. Sixteen tests mutate oracle exposure, metadata columns/counts,
arguments, replay determinism, comparator policy, null handling, runtime labels,
endpoint evidence source, conflict markers, procedure relations, alternative
paths, and claim ceilings.

## Design rationale and provenance

The full SOP-Bench paper/release audit is
`papers/agent-benchmarks/2026-07-14-sop-bench-procedure-task-validity.md`; pinned
paper/release identities and timing boundaries are in
`data/sources/releases/2506.08119v2-sop-bench/provenance.json`.

| Choice | Evidence and adaptation boundary |
|---|---|
| Explicit field roles and no answer-bearing endpoint tools | Review lines 73–89 and Repair 2 identify missing metadata roles, whole-row fallback exposure, ignored arguments, and tools returning scored columns. The role/surface matrix is a skill-bench adaptation. |
| Frozen replay and exact package inventories | Review lines 121–147 and 191–200 document absent seeds/repetitions, stochastic mock tools, count drift, divergent release surfaces, and conflict markers. |
| Independent oracle plus typed comparators | Review lines 93–106 and Repair 4–6 show trace extraction, substring equivalence, null collapse, and row/oracle coupling. Internal agreement still does not prove oracle correctness. |
| Procedure graph and accepted alternatives | Review lines 97–101 and 191–194 identify absent ordering, gates, fallback triggers, audit obligations, and alternative paths. Clause provenance does not infer expert approval. |
| Separate runtime, endpoint, procedure, and joint verdicts | Review lines 100–106 and Repair 7–8 show that runtime success was called tool accuracy and endpoint values could be recovered from a trace without a final artifact. |
| Fail-closed claim ceiling | Review lines 155–173 bounds the defensible result to configured-system endpoint agreement and rejects procedural fidelity, professional equivalence, safety, and readiness claims. |

## Validate

```bash
python scripts/validate_procedure_package.py --check-paths \
  schemas/fixtures/procedure-package-conformance.json
python -m unittest tests.test_procedure_package_conformance -v
```
