# Benchmark bundle schema v0.3

`benchmark-bundle.schema.json` is the first executable contract for a complete
knowledge-work evaluation evidence chain:

```text
expert model → public procedural skill → task/artifact → versioned trial → rubric result → causal diagnosis
```

It is intentionally a **bundle schema**, not seven disconnected files. A local
schema alone cannot prove that a check names a real grader, that a failed check's
causal slice names real trace events, or that a completed trial covers every
required check and artifact. `scripts/validate_benchmark.py` therefore applies:

1. JSON Schema Draft 2020-12 shape, type, format, and conditional checks;
2. semantic reference and admissibility checks across task, grader, check,
   artifact representation, transformation, trace, and trial records;
3. completed-trial invariants, including weighted aggregate recomputation;
4. optional verification that local provenance paths exist.

Version 0.2 also recomputes each local procedural skill's SHA-256 when
`--check-paths` is enabled.

## Design rationale and evidence

| Contract decision | Why it is explicit | Repository evidence |
|---|---|---|
| Task, trial, grader, trace, and artifact are separate records | Final score alone loses stateful execution evidence and prevents diagnosis. | `docs/production-agent-systems.md`, “Complete evidence chains” |
| Every source/check/task design claim can carry provenance | Benchmark authors must be able to distinguish primary, expert, synthetic, reviewed, and derived claims. | `.hermes.md`, “Evidence standard”; `templates/task-metadata.md` |
| Domain primitives map to sources and checks | Tacit expertise becomes testable through hidden requirements, contradictions, thresholds, conventions, traps, and safety constraints. | `.hermes.md`, “Benchmark-building standard”; `templates/task-metadata.md` §4 |
| Artifact declarations and observed artifacts are separate | The expected professional deliverable and the actual immutable trial output serve different purposes. | `templates/task-metadata.md` §5 |
| Checks identify visibility and grader implementation | Public task material must remain separate from private/hidden verifier internals to control leakage. | `docs/state-of-the-art-map.md`, “Benchmark operation layer” |
| Trials record model, scaffold, skills, tool, and memory policy | Results are agent-system results; recording only the base model creates a scaffold confound. | `papers/agent-benchmarks/2026-07-09-agent-psychometrics.md` |
| Failed/error checks require root, surface, and causal-slice events | Failure location may differ from origin; useful runs preserve a compact causal chain. | `papers/agent-benchmarks/2026-07-09-strace.md` |
| Root-cause vocabulary includes task/grader/environment faults | A benchmark must distinguish agent capability failures from invalid or broken evaluation. | `templates/task-metadata.md` §6 and STRACE review limitations |
| Procedural skills and rubrics have independent versions and hashes | A dual-use skill otherwise confounds execution guidance, rubric quality, and evaluator-cue leakage. | `papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md` §§ Transferable design patterns 1, 4 |
| Every check declares its disclosure boundary and public requirement basis | Private checks may hold out exact consequences, but may not introduce surprise obligations. | LH-Bench review § Transferable design patterns 3 |
| Trial versions are typed for task, skill, rubric, grader, tool interface, harness, and feedback policy | Free-form names cannot detect silent drift or support causal ablations. | LH-Bench review § Concrete changes 2 |
| Recovery is an explicit error → verifier feedback → repair → verification chain | Error count is uninterpretable without feedback specificity and verified recovery. | LH-Bench review §§ Unique insight, Transferable design patterns 5 |
| Artifact views and transforms are typed separately from artifacts | A screenshot, structured state, executable source, and export establish different predicates; derived views require pinned transformations. | `papers/agent-benchmarks/2026-07-10-scivisagentbench-multimodal-artifact-evaluation.md` §§ Unique insight, Transferable design patterns 1–3 |
| Checks can fail closed through an admissibility envelope | Missing views, invalid exports, control/renderer mismatches, and inapplicable criteria are not ordinary zero scores. | SciVisAgentBench review, Sections 5.2–5.5 (pp. 5–6) and Concrete changes 1, 5 |

The fixture `tests/fixtures/valid-benchmark-bundle.json` is deliberately a
failed completed trial. It demonstrates that a score of zero can still preserve
a useful, machine-checkable diagnosis and an unsuccessful but fully observed
recovery chain. Its public skill is a real local file whose hash is verified.

## Artifact-view admissibility

The optional `task.artifact_views`, `check.admissibility`,
`trial.artifact_views`, and check-result admissibility fields are a
backward-compatible extension: bundles without them retain the prior behavior.
When an envelope is present, the semantic validator requires:

1. every required view to identify a checked artifact and include the declared
   authoritative representation;
2. authoritative views to be untransformed and derived views to pin transform,
   software, version, hash, and controls;
3. observed representations, controls, transform identities, and applied
   invariances to match the envelope; and
4. fail-closed outcomes: `insufficient_evidence` for missing views or
   control/transform mismatch, `invalid_artifact` for invalid exports,
   `not_applicable` for inapplicable criteria, and scored `passed`/`failed` only
   after admission.

`tests/fixtures/valid-artifact-admissibility-bundle.json` is internal synthetic
contract calibration, not an agent trial or a professional-validity result. Its
five aborted records plant a visually plausible but structurally wrong artifact,
a structurally correct alternate rendering, a missing side view, an invalid
export, and a different renderer hash. They demonstrate, respectively, admitted
failure, admitted acceptance under a declared invariance, abstention for missing
evidence, invalid-artifact rejection, and abstention for transform mismatch.
Every declaration cites the full SciVisAgentBench paper/release review and its
recorded local provenance.

## Required 2×2 ablation

Trials encode one condition rather than inferring it from filenames:

| `evaluation_versions.condition` | Skill | Rubric relationship | What it identifies |
|---|---|---|---|
| `no_skill_independent_rubric` | `null` | `independent` | Baseline behavior under a measuring instrument not derived from the skill. |
| `no_skill_shared_rubric` | `null` | `shared_expert_model` | Rubric-instrument effect without exposing procedural guidance. |
| `public_skill_independent_rubric` | public skill | `independent` | Skill effect without shared-rubric cue contamination. |
| `public_skill_shared_rubric` | public skill | `shared_expert_model` | Production-like expert guidance plus an instrument derived from the same expert model. |

An optional fifth condition, `exact_rubric_disclosed`, records a public skill
plus the exact disclosed measuring boundary. It estimates upper-bound
evaluator-cue compliance and must not be reported as latent skill transfer.

The semantic validator rejects condition/rubric mismatches and requires `skill:
null` only in the no-skill condition. Compare process and artifact outcomes
separately across matched task seeds; do not collapse them into one score before
checking whether the public skill improves deliverable quality rather than only
rubric compliance.

## Validate

The validator requires Python's `jsonschema` package (tested with 4.26):

```bash
python scripts/validate_benchmark.py --check-paths \
  tests/fixtures/valid-benchmark-bundle.json \
  tests/fixtures/valid-artifact-admissibility-bundle.json
python -m unittest tests.test_validate_benchmark -v
```

`--check-paths` verifies `provenance.local_path` files and recomputes local
`procedural_skills[].content_path` hashes. Trial artifact paths can refer to
external or ephemeral run storage and are not required to be present in the
repository.

## Deliberate v0.3 boundaries

- A bundle contains one task and zero or more trials. Cross-task suites and a
  normalized response-matrix export belong in a later layer.
- Trace payloads are referenced by path rather than embedded, avoiding large or
  sensitive prompt/tool data in benchmark metadata.
- The validator checks edge references and event order, but not dependency-graph
  acyclicity yet.
- Grader entrypoints are contracts, not executed by this slice. Sandboxed grader
  execution and grader-output ingestion remain separate infrastructure work.
- SHA-256 values are required for observed artifacts, but this validator does
  not resolve external run storage or recompute them.

## Task-only ablation preflight contract

`ablation-preflight.schema.json` is a deliberately separate calibration contract for a matched four-condition packaging replay. It requires all 2×2 condition records, typed component and artifact hashes, explicit unexecuted checks, and `capability_evidence: false`. This prevents builder-authored fixtures from being laundered into benchmark trials while still exercising the machinery needed before genuine agent runs. The LH pilot runner and fixture are `scripts/run_lh_ablation_preflight.py` and `pilots/lh-skill-adoption/ablation/preflight-report.json`.
