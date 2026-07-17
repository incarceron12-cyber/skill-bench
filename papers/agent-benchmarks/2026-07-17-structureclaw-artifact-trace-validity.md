# StructureClaw: an executable evidence chain is stronger than a final answer, but its weakest comparator still defines “engineering success”

## Source and review status

**Deep review of the complete immutable primary source and appendices, plus a timing-bounded audit of the official system and benchmark repositories.**

- **Paper:** Sizhong Qin et al., *StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows*, arXiv:2607.14896v1 (16 July 2026), <https://arxiv.org/abs/2607.14896v1>.
- **Date read:** 2026-07-17.
- **Local PDF:** `data/papers/pdfs/2607.14896v1-structureclaw.pdf` (21 pages; SHA-256 `093179a922378beaa857ca02b2a30fe60d6479df4c06bd844c99ed953fb0994e`).
- **Full local text:** `data/papers/text/2607.14896v1-structureclaw.txt` (SHA-256 `7b739c1df309ede0c43908a21b61f8b6f6b72e2848c9a95e924b5cdfa3b3e6d6`).
- **Release provenance:** `data/sources/releases/2607.14896v1-structureclaw/provenance.json`.
- **Official system release:** <https://github.com/structureclaw/structureclaw>, archived at post-v1 commit `af3d2adc19ede30d2bdf7050cc3645aa73a435c3` as `data/sources/releases/2607.14896v1-structureclaw/structureclaw.zip`. Because that commit is dated 17 July, it is not treated as exact paper-time code. The pre-v1 `v1.1.0` release is separately archived as `structureclaw-v1.1.0.zip`.
- **Official benchmark release:** <https://github.com/structureclaw/structureclaw-benchmark>, archived at pre-v1 default-branch commit `ca100885016800075d3e10ad7b49713852bc4fbc` as `structureclaw-benchmark.zip`. The main repository instead pins older benchmark commit `5d5a35a8c1cfd75ea5ba780db3f3204f5bf317f1`, preserved as `structureclaw-benchmark-submodule.zip`; the two revisions are not silently equated.
- **Release boundary:** the standalone benchmark contains all 150 scenario files, fixtures, runner, and grader source, but no paper result rows, traces, aggregate tables, model outputs, judge outputs, or analysis scripts that regenerate the manuscript figures. Its advertised standalone scenario validation currently fails on eight stale multimodal attachment paths.

## One-sentence contribution

StructureClaw correctly makes the evaluated unit a request-linked executable evidence chain—route, model, validation, provider execution, checks, terminal decision, and report—rather than a fluent endpoint, but 97/150 scenarios ultimately reduce model quality to lower-bounded counts, global coordinate spans, and approximate aggregate loads; no engineer validates alternatives or paper outputs, no repeated run estimates reliability, and the released evidence cannot replay the reported 88.6% versus 56.8% result, so the benchmark establishes controlled configured-workflow conformance, not engineering correctness, code compliance, professional quality, safety, or readiness.

## Why this matters for skill-bench

This is a methodological case for charter objectives A–C, not a proposal to narrow `skill-bench` to structural engineering. Structural work makes an otherwise general benchmark problem unusually visible: a plausible final artifact can be disconnected from the requirements, assumptions, model, computations, validation state, or software execution that supposedly support it.

The useful general chain is:

```text
request + source authority + applicable standards
→ interpreted requirements and assumptions
→ versioned intermediate artifact
→ deterministic validation and unresolved diagnostics
→ bound tool/provider execution
→ raw result and postprocessing
→ domain check and exception state
→ final deliverable claim
→ independent equivalence / quality / safety review
→ downstream professional consequence
```

StructureClaw represents much of the first eight links. It evaluates a narrow operational projection of several of them. It does not reach independent equivalence, professional acceptance, or consequence. That separation is the review's central result.

## Research question and strongest defensible claim

The paper asks whether a governed skill/tool/artifact workbench can preserve an inspectable structural-engineering evidence chain and whether an automatic specialized workflow outperforms a generic-skill configuration on authored standard cases, while safely handling interactive edge cases and reconstructing models from images or DXF files (pp. 1–8, Appendices A–D).

The strongest defensible empirical claim is:

> In 1,800 reported single attempts over 150 authored fixtures, the full automatic StructureClaw configuration passed all fixture-listed operational assertions on more standard cases than a generic-only configuration for each of ten displayed agent-model configurations; the manuscript reports an unweighted/pooled mean of 88.6% versus 56.8%. Separate auto-only fixture suites identify lower recorded success for invalid numerical inputs and for some multimodal model-matching cases.

This is a **configured package comparison**. It does not isolate skills, routing, prompts, validators, repair, tools, provider adapters, or report generation. It does not establish structural correctness, unique or complete model equivalence, code compliance, human-review equivalence, project suitability, reliability, production value, or autonomous engineering competence.

## Methodology and system

### Typed workflow and artifact state

The system separates:

- a **skill**, which declares triggers, guidance scopes, supported structures, dependencies, conflicts, runtime compatibility, and artifact inputs/outputs;
- a **capability**, the function exposed to the agent;
- a **tool**, a typed state transition such as extract, construct, validate, analyze, check, or report;
- a **provider**, which binds a tool contract to OpenSees, PKPM, YJK, or another backend; and
- an **artifact**, the versioned state/evidence passed between stages (pp. 4, 13–15).

The shared structural-model protocol can hold project context, units, topology, materials, sections, restraints, loads, combinations, and analysis controls. Artifact envelopes can include identity, kind, revision, producer/provider, run, schema, upstream references, dependency fingerprints, provenance, warnings, and payload. Model patches are separate proposed/accepted state transitions whose base revision must match (Appendix A).

This is the paper's strongest design contribution. It distinguishes “a solver-shaped sentence” from a recorded provider invocation and prevents a report's existence from proving that analysis occurred. It also permits clarification, safe non-execution, and unsupported termination as positive terminal states rather than treating every non-completion as failure.

But the paper is unusually candid that the conceptual envelope exceeds the implementation: not every artifact kind or dependency is materialized in every run, the dashed repair graph is an affordance rather than an evaluated automatic loop, and traceability cannot verify an incomplete validator or incorrect solver/adapter (pp. 14–15). The release confirms a rich application and model/tool codebase, but the benchmark observes selected state fields rather than validating the full conceptual graph.

### Scenario portfolio

The released suite has exactly 150 unique JSON scenarios:

- 50 `standard_workflow` text cases;
- 50 `interactive_robustness` text cases; and
- 50 `multimodal_reverse_engineering` cases, including 35 images and 15 DXF files.

Each family contains 25 Chinese and 25 English prompts. Standard cases span beams, steel and concrete frames, trusses, portal frames, continuous beams, columns, and one generic case. Interactive categories include missing, invalid, unrealistic, ambiguous-unit, multi-turn, conflicting, recovery, unsupported, and static-analysis conditions. The suite is deliberately authored and balanced, not sampled from engineering practice (pp. 5, 15; release `README.md`).

This supplies controlled coverage but no ecological sampling warrant. No expert-task authoring protocol, author qualifications by scenario, independent requirement review, code/standard lineage, critical-incident source, field-project comparison, or item-level approval record is reported. “Structural engineering” is therefore the content label of an author-built fixture suite, not its demonstrated inference population.

### Assertions and score

The benchmark release contains 675 typed assertion occurrences across the 150 cases:

- `skill_match` 136;
- `structural_type` 131;
- `has_analysis` 114;
- `model_matches` 97;
- `has_model` 73;
- `no_bad_model` and `should_not_analyze` 32 each;
- `has_interaction_questions` 31;
- `natural_language` 28;
- `engine_match` 18;
- `analysis_or_interaction` 13; and
- `has_report` only 4.

A scenario succeeds only if every required assertion passes. Required unavailable observations fail the primary scenario score; unavailable outcomes are excluded from assertion-diagnostic denominators but disclosed through coverage. Each configuration–scenario pair runs once, with retries disabled and a 15-minute timeout (pp. 5–6, 16–18).

Strict conjunction is appropriate for dependency-bearing workflows: routing success cannot compensate for no model, and a model cannot compensate for absent analysis. Yet the score is only as strong as its weakest required observer. Conjunction does not turn coarse predicates into engineering validity.

The released graders illustrate the boundary:

- `has_model` requires only a model plus minimum node/element counts.
- `has_analysis` requires a nonempty displacement, reaction, or force field; it does not test equilibrium, convergence, units, boundary conditions, or numerical correctness.
- `has_report` requires more than 100 Markdown characters; only four scenarios request it.
- `engine_match` checks recorded engine/skill identity, not adapter correctness.
- negative safety cases pair no analysis invocation/result and often no computable model with a clarification/semantic requirement. This is stronger than rewarding silence alone.
- `natural_language` sends a compact state summary—structural type, model counts, result keys and one sample, plus the first 500 report characters—to one LLM judge. The judge cannot inspect the complete model, trace, report, source, or solver receipt.

The runner further allows a passing semantic interaction judgment to override a failed deterministic `has_interaction_questions` predicate. That is an explicit observer-composition choice, but it means the exact same “question asked” construct can be satisfied through two unequal evidence views without a human-calibrated equivalence argument.

### The model comparator: executable but materially undercomplete

`model_matches` is the decisive quality observer in 97 scenarios. It checks:

1. agent node count **at least** reference count;
2. agent element count **at least** reference count;
3. global x/y/z coordinate ranges within 0.5 m by default;
4. approximate total, or selected-axis, absolute load magnitude within 20% by default.

It does **not** check graph isomorphism, member connectivity, support equivalence, element orientation, materials, sections, releases, local load placement, load cases/combinations, signs, mass, stiffness, stability, solver settings, or physical-response equivalence (pp. 5, 8, 15–16; release `lib/evaluate.cjs`). Counts are lower bounds, so gratuitous nodes/elements are not penalized. Loads are summed by absolute magnitude, which deliberately loses sign and can collapse distinct load distributions. Missing endpoint references in the comparator's element-length helper default to length one rather than fail closed. A ground-truth zero span or load becomes automatically acceptable for that component.

Thus an artifact can pass while being topologically, materially, or mechanically wrong. Conversely, a valid alternative idealization can fail if counts, ranges, or aggregate loads differ. The authors correctly call fixtures operational targets rather than unique solutions, but the primary scenario score still uses this observer as if pass/fail were resolved.

This creates the benchmark's key validity inversion:

> **The evidence chain is richer than final-answer scoring, but the final claim about that chain is capped by the coarsest edge observer.**

A trace can prove that a value was produced by a recorded stage. It cannot prove that the value means what the stage label implies.

### Automatic versus generic-only comparison

Ten text-agent configurations evaluate the same 50 standard cases in automatic and generic-only modes. The manuscript reports every configuration improving, with lifts from 24 to 46 points and mean Success Rate rising from 56.8% to 88.6% (pp. 6–8). This pairing controls case identity and broad environment better than comparing unrelated benchmark runs.

However, the treatment jointly changes specialized routing, structural priors, artifact expectations, and validation guidance. It is not a skill-only or routing-only effect. The release README additionally documents an `oracle-specialist` mode, but the paper's reported table does not use a complete auto/oracle/generic factorial to isolate routing from specialist guidance. Model/provider aliases are display names without snapshot IDs or decoding receipts.

The continuous-beam reversal is more informative than the average: automatic falls from 48/50 to 38/50 pooled case-configurations, with five configurations losing 40 points on the five-case family (pp. 8, 18–20). This demonstrates a shared path-specific regression and supports family-level release gates. It does not identify the root stage because the reported diagnostics are marginal; they do not require that routing, model, analysis, and report predicates co-occur on the same failed trace.

### Robustness and safe non-execution

Interactive Success Rates range from 88% to 94%, but invalid-value cases pass only 56/79 observed outcomes (70.9%; 56/80 if missing is failure). Unit-ambiguity and static-analysis subsets appear perfect but comprise only 40 and 10 configuration-case outcomes. Negative cases require affirmative clarification/semantic evidence plus absent analysis, reducing the common “do nothing and pass safety” loophole.

Still, these are author-defined disposition labels. The suite has no engineer/user study of whether clarification, repair, abstention, or unsupported termination was appropriate; no cost of over-abstention; no matched valid/invalid boundary sweep; no severity weighting; and no test that an invalid intermediate artifact was never persisted or exposed before the terminal state. “No `run_analysis` result/call in archived messages” is a bounded trace predicate, not proof of no side effect across all providers or workspace state.

### Multimodal reconstruction

Six agent/vision configurations receive images or DXF files and then use the same artifact workflow. The manuscript reports 60–94% Success Rate, with 84.7% aggregate model matching on 281 recoverable outcomes. It appropriately avoids attributing performance to vision alone because agent and perception roles are not fully crossed (pp. 7–8, 19–20).

The fixtures are generated from the same ground-truth model factory and renderers used by the benchmark, making them reproducible but tightly coupled. Mechanical diagrams, construction-style images, DXFs, and architectural projections are transformations of authored canonical models rather than independently sourced field documents. The comparator observes counts, spans, and aggregate loads, so visually successful reconstruction does not establish topology, supports, materials, sections, or member semantics.

A concrete release defect further weakens operational reproducibility: `npm run validate:scenarios` at commit `ca100885...` fails on eight image cases because attachment paths retain `../../tests/llm-benchmark/fixtures/...` prefixes while the standalone validator resolves them beneath the benchmark root. The files exist, but the released standalone path contract is broken. This is exactly the kind of artifact-edge drift the paper argues should be detected.

## Evidence and claim boundaries

### Supported

1. The paper specifies a coherent artifact-centered architecture with typed skills, tools, providers, model state, validation, execution, terminal decisions, and reports.
2. The official release contains 150 unique scenarios with the stated 50/50/50 family and 25/25 language allocation.
3. Negative cases often require positive clarification evidence plus no model/analysis, rather than crediting absence alone.
4. The primary score is strict conjunction over fixture-required assertions; required missing evidence fails the scenario.
5. Automatic and generic-only modes use the same 50 standard cases and differ as documented configured packages.
6. The displayed manuscript tables report higher automatic-mode Success Rate for all ten configurations and a concentrated continuous-beam regression.
7. The release exposes exact grader semantics, allowing the model-equivalence and evidence-view limits to be audited.

### Partially supported

- **Complete evidence chain:** many stages are represented, but the conceptual envelope is only partly materialized and evaluated.
- **Trace-grounded reporting:** report existence and limited semantic conditions are checked; numerical claim-to-result entailment is not comprehensively verified.
- **Model consistency:** counts, global spans, and approximate loads are checked; topology, supports, properties, combinations, and response equivalence are not.
- **Safe handling:** selected authored dispositions are enforced by trace predicates; real authority, side effects, severity, and over-abstention are unvalidated.
- **Automatic-workflow benefit:** a consistent configured-package contrast is reported, but no component effect, repeated reliability, or released row-level replay is available.
- **Reproducibility:** scenarios, fixtures, runner, and graders are inspectable, but result evidence is absent and standalone validation fails.

### Not supported

- structural, physical-response, or engineering equivalence to the references;
- solver, adapter, unit, convergence, equilibrium, or numerical correctness;
- exhaustive design-code compliance;
- report-level numerical faithfulness or professional communication quality;
- construction-ready artifacts or professional approval;
- reliability of one model on one case, because each pair is attempted once;
- causal attribution to skills, routing, validators, repair, or tools individually;
- language or input-format effects from unmatched subsets;
- representative structural-engineering coverage or task prevalence;
- safe deployment, engineer substitution, production utility, liability fitness, or readiness.

## Unique insight

StructureClaw's distinctive lesson is not merely “score intermediate artifacts.” It is:

> **A professional artifact chain needs both provenance edges and semantic edge obligations. Execution provenance answers “what produced this?”; it does not answer “was this transformation valid?”**

For every handoff, `skill-bench` should preserve two independently graded contracts:

```text
Provenance edge
producer + tool/provider + input hashes + output hash + revision + status + receipt

Semantic edge
applicable requirements + units + assumptions + invariants + admissible alternatives
+ transformation-specific checks + unresolved exceptions + evidence-view sufficiency
```

Then distinguish four outcomes:

1. **missing edge** — no claimed transformation occurred;
2. **invalid provenance** — identity, version, inputs, or execution receipt are absent/inconsistent;
3. **semantic nonconformance** — the transformation occurred but violated a requirement/invariant;
4. **observer insufficiency** — available checks cannot decide equivalence or correctness.

StructureClaw often treats the fourth as pass or fail through a coarse fixture comparator. A diagnostically honest benchmark must allow `insufficient_evidence` rather than promoting global spans and aggregate loads into model validity.

## Reproducibility and operational realism

**Conceptual reproducibility is high.** The paper defines scenario families, terminal states, outcome vocabulary, score equations, single-attempt semantics, mode contrast, diagnostic denominators, missingness, and validity boundaries. The release exposes typed scenarios, generated fixtures, runner, validator, judge prompt, and deterministic comparison code.

**Exact result reproducibility is poor.** The release has no reported result rows, traces, outputs, judge decisions, aggregate files, table/figure scripts, seeds, provider request receipts, model snapshot IDs, or environment/container lock. The main repository pins benchmark commit `5d5a35...`, while the benchmark default branch is `ca100885...`; neither is identified in the paper. The post-v1 system archive is not paper-time code. Paper numbers therefore cannot be replayed from preserved outputs.

**Operational reproducibility is currently defective.** The standalone release's own validator fails eight multimodal attachment paths. Commercial PKPM/YJK execution requires external licensed installations, while exact provider and judge behavior is mutable. Child-process isolation and unified timeout are useful, but no filesystem/network sandbox, provider-state capture, or complete execution receipt is evidenced.

**Operational realism is bounded.** The workflow stages and software backends are domain-plausible, invalid-input handling matters, and generated images/DXF files require actual perception-to-model handoffs. Yet tasks are authored controlled fixtures, mostly small canonical systems, with no field-project coordination, revision history, engineer review, stakeholder acceptance, liability, or downstream construction consequence. The paper itself appropriately labels the suite diagnostic rather than certifying.

## Limitations

1. No task-authoring, expert-authority, independent review, or occupational sampling protocol.
2. Authored balance does not establish prevalence or representative difficulty.
3. Only one attempt per configuration–scenario pair; no run-level variance or reliability.
4. No task/model/judge clustered uncertainty or paired confidence intervals.
5. Auto versus generic changes multiple components.
6. No complete oracle-specialist factorial isolates routing from guidance.
7. Display model names do not identify provider snapshots or decoding state.
8. No paper result rows, outputs, traces, judge rows, or analysis scripts are released.
9. Main and benchmark repository revisions drift and are not paper-identified.
10. Standalone validation fails eight multimodal attachment paths.
11. `has_model` and `has_analysis` are existence checks, not substantive validity.
12. `has_report` is mostly absent and otherwise only length-based.
13. The natural-language judge sees a lossy state summary and truncated report.
14. No judge calibration, repeated labels, expert agreement, or abstention policy.
15. Semantic-judge pass can override a failed deterministic interaction observer.
16. Model matching omits topology, supports, materials, sections, releases, and local load placement.
17. Node/element lower bounds permit extraneous topology.
18. Absolute aggregate loads erase sign and distribution.
19. Missing element endpoints default to unit length in the comparator rather than failing closed.
20. Zero expected spans/loads are automatically accepted for those dimensions.
21. Canonical fixtures are neither unique solutions nor complete equivalence classes.
22. Generated multimodal fixtures share the model factory and renderer with evaluation targets.
23. Agent and vision roles are not fully crossed.
24. Locale and format subsets are compositionally unmatched.
25. Stage diagnostics are marginal and cannot establish within-trace causal order.
26. No code-compliance completeness or solver/adapter correctness study.
27. No independent engineer review of agent artifacts or accepted alternatives.
28. No collateral-state, over-abstention, severity, or downstream consequence measure.
29. Commercial backend availability and authorization limit reproducibility.
30. No production, professional-quality, safety, liability, or readiness evidence.

## Transfer to skill-bench

### Retain

1. **Evidence-chain unit.** Evaluate linked intermediate and final artifacts, not just the endpoint.
2. **Skill/tool/provider/artifact separation.** Record guidance, executable operation, backend realization, and state independently.
3. **Versioned artifact dependencies.** Preserve upstream hashes, base revisions, patches, provider identity, warnings, and terminal state.
4. **Positive safe terminals.** Clarification, safe non-execution, and unsupported termination need affirmative evidence, not absence alone.
5. **Strict scenario conjunction.** Required workflow obligations should not average away, while diagnostic rates retain explicit coverage.
6. **Unavailable versus inapplicable.** Missing required evidence must not be relabeled semantic irrelevance.
7. **Family regression gates.** Aggregate improvement cannot conceal a repeatable subgroup/path regression.
8. **Configured-package honesty.** A bundled workflow contrast must not be narrated as a single-skill effect.

### Repair

1. **Pair every provenance edge with semantic obligations.** Tool execution and artifact existence cannot certify transformation validity.
2. **Use typed observer sufficiency.** Emit `insufficient_evidence` when a screenshot, global span, or summary cannot establish topology or claim faithfulness.
3. **Represent alternatives.** Use equivalence classes, invariants, metamorphic relations, and expert-adjudicated alternatives rather than one canonical witness.
4. **Test numerical and physical invariants.** Units, signs, equilibrium, boundary conditions, convergence, conservation, and response should be distinct checks where applicable.
5. **Bind report claims to result locators.** Every consequential numerical claim needs a source artifact, computation receipt, unit, and supported rounding/tolerance.
6. **Calibrate safety boundaries.** Cross invalid/valid near-neighbor cases; measure over-action, over-abstention, side effects, severity, and review burden.
7. **Factor interventions.** Compare generic, specialized guidance, routing, validator, repair, and full package under identical task/tool/provider envelopes.
8. **Repeat stochastic cells.** Estimate run reliability and task/configuration clustering before ranking or release claims.
9. **Freeze executable releases.** Pin the system, benchmark submodule, solver/container, provider protocol, judge, and result rows; run release validation from a clean checkout.
10. **Close with independent acceptance.** Controlled conformance must precede—not substitute for—expert artifact review and consequence evidence.

## Concrete repository actions

1. **No new queue task.** Existing benchmark-bundle artifact/check graphs, configured-component realization, artifact-view admissibility, validity arguments, task health, metric monitoring, execution isolation, and cross-artifact consistency work already have homes for these requirements. A structural-engineering-specific schema would duplicate machinery and narrow scope.
2. In the next cross-artifact pilot, add one planted chain where every provenance edge is valid but the intermediate semantic transformation is wrong; require the grader to return `semantic_nonconformance`, not generic failure.
3. Add one alternative-valid artifact that differs from the canonical witness but preserves declared invariants, and one coarse-summary false positive that matches counts/spans/totals while violating dependency structure. These cases directly test witness completeness and observer sufficiency.
4. Make clean-release conformance include submodule revision resolution, standalone fixture-path validation, immutable result-row capture, and exact table regeneration before any empirical claim is indexed as replayable.

## Bottom line

StructureClaw advances the benchmark design frontier by making an engineering result answerable to an inspectable chain of requirements, artifacts, validators, provider executions, checks, and terminal decisions. Its typed distinction among skills, tools, providers, and artifacts; strict conjunction; positive safe terminals; and family-level regression analysis are worth retaining across knowledge-work domains.

But traceability is not correctness. The principal released comparator accepts models from lower-bounded counts, global spans, and approximate absolute load totals while ignoring the topology, supports, properties, combinations, and physical response that make a structural model what it is. Most report quality is not scored, one lossy LLM observer handles semantic conditions, each stochastic cell runs once, paper outputs are absent, revisions drift, and the standalone validator fails. `skill-bench` should adopt the evidence-chain architecture while enforcing the stronger rule its release makes necessary: **a recorded handoff proves provenance; only a validated semantic edge supports correctness; and when the observer cannot decide, the honest outcome is insufficient evidence—not professional success.**
