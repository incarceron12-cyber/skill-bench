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
| Persistent workspace identity, placement, dependency hypotheses, process observations, mutations, and cleanup are separate | File existence, authored relevance, observed access/write, and causal use are different claims; a correct deliverable can coexist with destructive workspace state. | `papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md` §§ Representative task trace, Unique insight, Transferable benchmark design lessons 1–8 |
| Source authority, exposure, adoption, attempted action, intercepted/realized state, recovery, and utility are separate | Source placement is not exposure; exposure is not adoption; a tool call is not a realized consequence; and refusal is not secure useful completion. | `papers/agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md` §§ Unique insight, Transferable benchmark-design lessons 1–5 |
| Context compression is a versioned, trace-linked state transformation with immutable raw evidence | Terminal reward or token savings cannot establish fidelity, alternate-future sufficiency, or auditability; reset and reformatting are confounds rather than compression effects. | `papers/agent-benchmarks/2026-07-13-acon-context-compression-validity.md` §§ The paper's own examples falsify a strong fidelity claim, Transfer to skill-bench |
| Post-run storage is a typed stock linked to operational utility | Fewer retained bytes dominate only when the same authorized reconstruction, recovery, provenance, diagnosis, handoff, grading, and deletion predicates survive under a matched fixed trace and declared boundary. | `papers/agent-benchmarks/2026-07-15-agentfootprint-storage-reconstructability-validity.md` §§ Unique insight, Transfer to skill-bench |

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

## Task-IR projection conformance

The optional `task.projection_manifest` is a backward-compatible authoring
contract. It does not treat the IR as professional ground truth. Instead, it
records one evidence-backed, versioned hypothesis and requires four separately
hashed projections: public instruction, source/environment affordance, valid
witness consequence, and checker predicate. The semantic validator recomputes
canonical JSON hashes for requirement atoms, the IR, and each rendered output;
requires exactly one projection of each kind; checks requirement-hash lineage;
and enforces bidirectional coverage so an unmapped checker atom is rejected as
a checker-only hidden obligation.

The manifest also pins the sampler and projector hashes, preserves accepted and
rejected sample history, separates solver/model status from executability,
instruction equivalence, professional validity, capability evidence, and
readiness evidence, and records witness/negative/mutation/metamorphic/adversarial
conformance evidence. `capability_evidence` and `readiness_evidence` are fixed to
`false` because this is authoring-instrument calibration, not an agent trial.
Declared representation invariances may be applied only by name and only after
the changed projection output digest is refreshed.

The compact fixture `tests/fixtures/valid-task-projection-manifest.json` cites
`papers/agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md`, which
in turn records the immutable v1 paper and pinned post-v1 release provenance.
Mutation tests change a requirement, affordance, witness consequence, and
checker predicate; test stale digests and checker-only obligations; accept one
declared equivalent wording; and assert that unrelated projection digests stay
stable. These tests establish internal contract behavior only—no expert,
professional, capability, or release-readiness claim.

## Persistent-workspace conformance

Optional `task.workspace` and `trial.workspace` records pin a canonical inventory
root, file roles and valid time, network/permission policy, overlay placement,
protected and mutable zones, authored availability/relevance/provenance
relations, trace-grounded observed access/write, mutations, and cleanup. The
validator recomputes the inventory digest, checks graph endpoints and placement
hashes, derives mutation authorization rather than trusting the recorded flag,
requires event-kind-appropriate process evidence, and rejects causal-use
promotion from path co-occurrence. Alternative source paths remain explicit
authored hypotheses rather than forced canonical routes.

`tests/fixtures/valid-persistent-workspace-conformance.json` is an inert internal
calibration slice grounded in the full Workspace-Bench review and its pinned
task-3 trace. It includes current, obsolete, distractor, alternate, protected,
and output roles; a declared equivalent path; and an unsupported causal-use
record. Mutation tests plant graph/placement drift, protected deletion,
unauthorized creation, missing process evidence, causal overclaim, and failed
cleanup. The fixture establishes contract behavior only: expert validity,
capability, workspace learning, causal use, and readiness remain false.

## Inert adversarial-action conformance

Optional `task.action_safety` and `trial.action_safety` records add an authority
matrix, inert containment policy, four-boundary preflight, and an action-state
ledger without creating a separate safety subsystem. The semantic validator
requires a trace-backed distinction among placement, exposure, adoption,
attempt, mock realization, severity/reversibility, detection, recovery,
residual harm, and benign utility. It derives realization from both interceptor
state and pre/post state identity, rejects live/non-allowlisted targets, and
replays safety and utility counts separately while excluding invalid cases.

`tests/fixtures/valid-adversarial-action-conformance.json` plants exactly eight
internal cases: secure useful completion, over-refusal, non-exposure, blocked
attempt, low-severity token disclosure in a warning, realized mock harm,
repaired mock harm, and an invalid run. Its ordinary source and token are
builder-authored and synthetic. `scripts/run_action_safety_preflight.py`
statically verifies the pinned source, mock-only target namespace, denied
network contract, synthetic credential marker, and absence of absolute or
traversal paths; its preserved output is
`tests/fixtures/action-safety-preflight-report.json`. This proves fixture and
adapter conformance only—not a live host sandbox, expert validity, agent
capability, real-world safety, or readiness.

## Context-compression fidelity conformance

Optional `task.context_compression`, `trial.context_compression`, and
`context_compression` trace events extend the existing bundle rather than define
a separate benchmark subsystem. The task contract pins an authoritative raw
record, nine typed invariant families, required next-action and alternate-future
probes, treatment arms, and strict non-claims. Each trial event records raw,
previous-summary, and output identities; trigger and compressor configuration;
trace lineage; invariant and probe evidence; and three outcomes that may not be
collapsed: state/evidence fidelity, decision sufficiency, and efficiency.

The semantic validator requires matched full-context, reset-only,
structured-reformat-only, and compression treatments; checks trace and raw-hash
lineage; requires compression configuration only in the compression arm; and
derives fidelity fail-closed from complete invariant evidence. A task-sufficient
event can therefore pass the realized next-action probe while failing fidelity
and an alternate-future probe, even when it records token savings.

`tests/fixtures/valid-context-compression-conformance.json` is internal synthetic
calibration grounded in the complete ACON paper/release audit. Its lossy case
plants entity, answer/value, modality, valid-time, provenance, contradiction,
required-literal, secure-handle, and artifact-state corruption while preserving
the immutable raw fixture at `tests/fixtures/context-compression-raw.json`.
Mutation tests reject fidelity upgrades over failed invariants, missing treatment
controls or trace lineage, raw-input and compressor drift, and incomplete
invariant coverage. These fixtures make no agent-capability, professional-
validity, reliability, production-fitness, or readiness claim.

## Storage-retention utility conformance

Optional `task.storage_retention` and `trial.storage_retention` records extend the
bundle's configured-system resource evidence without introducing a storage-only
subsystem. The task contract declares setup, execution, evaluator, local, remote,
and shared-store boundaries; typed channels; a fixed-trace identity; five matched
retention conditions; ten distinct utility predicates; and strict claim ceilings.
Trial observations separate workspace artifacts from framework/evaluator residue,
logical objects from representations, local stock from shared-store growth,
accepted attempts from failed/provider-invalid residue, and bytes from byte-days.

The semantic validator recomputes retained bytes, byte-days, and shared-store
growth; validates representation/transformation lineage; requires every condition
and utility predicate exactly once; forbids retention-dependent utility claims in
the no-persistence arm; preserves failed and invalid-service attempt residue; and
requires all-channel deletion evidence with no private representation or remote
canary left before selective deletion may pass.

`tests/fixtures/valid-storage-retention-conformance.json` is an internal synthetic
five-condition slice over one fixed recorded trajectory. It plants nested JSON,
SQLite, exact-content CAS lineage, a transformed near duplicate, a changed
same-size representation, shared-store growth, a remote canary, failed and invalid
attempts, summary-only loss, and selective private deletion. The fixture shows why
CAS can preserve replay at fewer bytes while summary-only preserves handoff but
not executable replay, and why raw retention can support diagnosis while failing
deletion. These are contract-calibration outcomes only—not production efficiency,
agent capability, professional validity, reliability, or readiness evidence.

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

## Configured-component lock and realization conformance

Optional `component_dependency_locks` and `trial.component_realization` records
extend configured-system identity without creating a package manager. A lock pins
mixed Skill, package, service, tool, and artifact identities; resolver and
registry snapshots; exact source/version/hash and valid time; typed relation
evidence, confidence, dispute, optionality, activation, phase, and authority;
and explicit cycle/shared-dependency/name-collision clusters. The validator
recomputes each canonical lock hash, fails closed on unresolved collision
laundering, and checks candidate signals against the exact resolved version.
A name-level advisory therefore cannot mark a different locked version affected.

Trial observations preserve seven runtime stages separately: mounted, installed,
visible, selected, invoked, attempted, and realized. Observed-true stages require
trace evidence; invocation cannot be promoted without selection and visibility;
attempts require a policy decision; denied attempts cannot become realized
consequences; and realized consequences require distinct before/after state
hashes. Example-only static mentions cannot silently become installed treatment
state. Paired no-Skill/public-Skill arms declare the intended component factor,
use a validator-recomputed hash of all unrelated components and relations, and
must match that hash across the pair.

`tests/fixtures/valid-component-realization-conformance.json` is an internal
synthetic cross-domain conformance slice grounded in
`papers/agent-benchmarks/2026-07-15-skill-supply-chain-dependency-risk-validity.md`.
It plants two same-name/different-blob candidates, an example-only package, exact
safe-version resolution, a mounted-but-unseen component, a denied mock service
call, and a realized renderer state change. Mutation tests reject identity-cluster
loss, example installation, version drift, safe-version risk promotion, denied
service realization, unchanged-state realization, and unrelated paired-lock
drift. Static reachability and these synthetic records establish no vulnerability,
safety, capability, professional-validity, or readiness claim.

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
