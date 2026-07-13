# Procedural relation projection contrast families

This zero-call pilot converts the SLBench review's relation-projection proposal
into a prospective executable conformance slice. It does **not** reproduce
SLBench: no instrument was released. The two knowledge-work shapes and all
clauses, events, artifacts, and oracle labels here are builder-authored synthetic
records.

## Charter fit and useful completion

The slice advances charter objectives **B** and **C**. Its general hypothesis is
that a procedural relation is evaluable only when source clauses, normalized
propositions, trigger/applicability, priority, public basis, environment
projection, accepted paths, observer coverage, plural evidence, verdict policy,
consequence claim, and root/surface locus remain separately inspectable.
Useful completion means exact relation selection and verdict replay over two
work shapes, plus exact localization of mutations at seven projection
boundaries. It is building and validation, not a procurement or research-domain
scope commitment.

## Prospective freeze and reuse

`suite.json` and `oracle-private.json` were frozen before `audit.py` was
implemented. The public suite contains no expected relation, verdict, or failure
locus. The private oracle contains those expected outputs and mutation loci.
The pre-existing `tests/fixtures/valid-task-projection-manifest.json` is preserved
byte-for-byte and pinned by SHA-256 in the suite.

No schema extension was needed. The sidecar reuses existing machinery:

- `task_projection_manifest` requires instruction, source-environment, witness,
  and check projections with reciprocal coverage and no checker-only obligation;
- `artifact_views` and per-case view states model evidence admissibility;
- criterion-level `events` remain intact before a declared three-way verdict;
- `validity` keeps professional/capability/readiness claims false;
- the private oracle separates relation selection, surface verdict, and earliest
  supported failure locus.

The two families cover precondition/override and fallback/exception relations.
Across 14 cases they include applicable and trigger-absent near-neighbors,
priority changes, alternate valid paths, planted violations, observer-missing
inconclusive outcomes, and mixed violation-plus-repair evidence.

## Evidence and rationale

Primary review: `papers/agent-benchmarks/2026-07-13-slbench-skill-relation-validity.md`.
The immutable PDF/text hashes and the prior projection-fixture hash are pinned in
`suite.json` and verified in tests.

| Executable choice | Review basis |
|---|---|
| Typed relation, trigger, governing priority, and alternatives | Unique insight and transfer, lines 173–203 and 243–250 |
| Exact clause spans/hashes and normalized propositions | Method §2 and transfer, lines 63–69 and 245–247 |
| Applicable/absent, override, alternate, violation, blind-observer contrasts | Relation test family, lines 193–203 |
| Required views and `inconclusive` on missing evidence | Grader semantics and transfer, lines 108–116 and 248–250 |
| Preserve realization and repair evidence before verdict | Mixed-evidence analysis, lines 110–116 and 249 |
| Separate workflow consequence from safety | Outcome semantics, lines 114–116 |
| Separate relation, verdict, and root/surface errors | Projection chain and transfer, lines 173–191 and 252 |

The exact predicates and synthetic clauses are project design hypotheses, not
claims by the source paper or testimony from an expert.

## Replay

```bash
python pilots/procedural-relation-projection/audit.py
python -m unittest tests.test_procedural_relation_projection -v
```

`report.json` reports relation-selection errors separately from final-verdict and
failure-locus errors, retains every evidence event, and counts inconclusive,
not-applicable, and mixed-evidence cases. Mutation tests plant source hash,
trigger, priority, public-basis, accepted-path, observer-view, and consequence
faults and require exact boundary localization.

## Claim ceiling

The only licensed claim is exact deterministic behavior on these 14 frozen,
builder-authored cases. The slice does not establish general skill following,
expert authority, professional validity, agent capability, safety, production
fitness, or deployment readiness.
