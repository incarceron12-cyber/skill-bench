# Compounding lesson contract v0.1

`compounding-lessons.schema.json` and
`scripts/validate_compounding_lessons.py` implement the benchmark-design knowledge
plane defined separately from agent evolution and benchmark-instrument changes in
`docs/benchmark-design-taxonomy.md` §4.2.

```text
source observation → immutable candidate lesson → held-out validation
                   → promotion/quarantine → downstream dependency → rollback
```

The contract is cross-domain infrastructure. It does not make `skill-bench` a
self-improving-agent benchmark and does not permit a synthetic fixture to become
expert or empirical validation.

## Enforced boundaries

1. **Immutable local delta.** A lesson has an ID, version, exact statement hash,
   authoring-component identity, source observations, scope, exclusions, and
   lifecycle state. Changes create another record/event; they do not rewrite
   history.
2. **Typed feedback authority.** Observations distinguish public task text,
   runtime output, public checks, private checks, references, expert
   adjudication, primary sources, self-assessment, and synthetic calibration.
   Visibility and evaluation splits remain explicit.
3. **Independent promotion.** A `promoted` event must cite a passed validation
   with disjoint source observations, a distinct scenario cluster, an independent
   validator, and passed declared-criterion, safety-regression,
   contradiction-handling, and distribution-shift dimensions. Schema validity or
   a source-task score cannot promote a lesson.
4. **Contradiction before consolidation.** Contradictory promoted lessons and any
   attempt to mark a contradiction as a duplicate/supersession require an
   accepted, evidence-linked resolution. Semantic similarity is not evidence of
   consistency.
5. **Private-evidence firewall.** Private-check/reference-derived lessons cannot
   become public dependencies. They cannot enter an agent-visible target on an
   overlapping evaluation split. Internal quarantine and analysis remain
   possible without disclosing the evidence.
6. **Downstream and rollback lineage.** Every dependent schema, rubric, grader,
   task, skill, or guidance artifact names the promotion event and component
   hash. An applied rollback must reciprocally retire each listed dependency and
   append a rollback lifecycle event; deletion is not rollback.

## Fixture evidence status

`tests/fixtures/valid-compounding-lessons.json` is a **contract-calibration
fixture**, not a record of empirically validated benchmark doctrine. Its
promotion examples are narrow implementation claims checked by repository tests.
One deliberately bad synthetic merge rule is shown as historically promoted,
then disconfirmed and rolled back, so rollback mechanics are exercised without
inventing a real production incident. Any use of this fixture to claim agent
improvement, professional capability, expert validity, or release readiness is
unsupported.

## Design rationale and provenance

| Choice | Rationale | Evidence |
|---|---|---|
| Delta records plus deterministic integration | Whole-context rewriting can erase useful information; transaction semantics reduced collapse in the reviewed setup. | `papers/agent-benchmarks/2026-07-10-agentic-context-engineering.md`, Unique insight and Table 18 discussion |
| Provenance, scope, contradiction, and lifecycle beyond helpful/harmful counters | Counters confound truth, relevance, compliance, and grader quality. | same review, Transferable design patterns 1–2 |
| Independent held-out promotion | Source trajectories cannot both generate and validate durable doctrine. | same review, Transferable design pattern 2; taxonomy invariants 9–10 |
| Split-aware private-evidence firewall | Private checks and references are evaluation treatments and can leak the tested consequence. | same review, Transferable design pattern 3; charter §6 principle 6 |
| Explicit dependencies and rollback events | Localized rollback preserves historical explanation and avoids another whole-memory rewrite. | same review, Transferable design pattern 5 |
| Separate knowledge, agent, and instrument planes | Jointly changing these planes makes capability and difficulty effects unidentified. | `docs/benchmark-design-taxonomy.md` §4.2 |

ACE provides empirical evidence for incremental updates in its AppWorld setup,
not empirical validation of this repository contract. The provenance, firewall,
contradiction, and promotion controls are `skill-bench` adaptations motivated by
ACE's documented omissions and the charter's validity requirements.

## Validate

```bash
python scripts/validate_compounding_lessons.py --check-paths \
  tests/fixtures/valid-compounding-lessons.json
python -m unittest tests.test_validate_compounding_lessons -v
```
