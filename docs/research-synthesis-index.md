# Research Synthesis and Relevance Index

> **Use this file when you want the shortest answer to:** What have the papers taught us as a group, how does each source matter to `skill-bench`, and which sources deserve the most attention?

This is a living navigation and prioritization layer under [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md). It does not replace the detailed reviews or the canonical technical taxonomy.

## How to use the research corpus

| Question | Best file |
|---|---|
| What is the project ultimately trying to achieve? | [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md) |
| What are the grouped research insights and most relevant papers? | **This file** |
| What technical model has the project synthesized from the evidence? | [`benchmark-design-taxonomy.md`](benchmark-design-taxonomy.md) |
| What benchmark families exist externally? | [`state-of-the-art-map.md`](state-of-the-art-map.md) |
| What did one paper actually do, and what are its limitations? | [`papers/agent-benchmarks/`](../papers/agent-benchmarks/) |
| What papers have been acquired, extracted, and reviewed? | [`data/papers/index.json`](../data/papers/index.json) |

## Relevance scale

Relevance is assessed against the charter—not citation count or paper prestige.

- **Tier A — foundational/direct:** changes the central expertise-to-evaluation method, realistic knowledge-work task design, validity model, or expert-participation strategy.
- **Tier B — enabling:** supplies essential machinery for artifacts, workflows, graders, traces, execution, psychometrics, safety, or task generation.
- **Tier C — contextual/specialized:** informs a narrower risk, operating mechanism, or self-improvement process but should not steer the benchmark's overall scope by itself.

A relevance tier is not a quality score. A methodologically weak source can raise a Tier A question while supplying weak evidence; a rigorous Tier C paper can still be valuable for a specialized component.

The four factors are:

1. **Objective directness:** proximity to realistic knowledge work and domain expertise transfer.
2. **Cross-domain leverage:** whether the insight generalizes beyond one pilot.
3. **Implementation consequence:** whether it changes schemas, tasks, graders, trials, or expert workflows.
4. **Evidence strength:** full-text/release inspectability, empirical support, validity, and reproducibility.

## Grouped insights

## 1. Expertise must become an evidence-bearing authoring graph

**Central insight:** Domain expertise should not be reduced directly to a prompt or checklist. Preserve the lineage from expert/source claims to primitives, scenarios, source packs, traps, artifacts, checks, trials, and release decisions. Provenance does not automatically imply approval, and each transformation needs its own warrant.

Most relevant sources:

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [ECBD: Evidence-Centered Benchmark Design](../papers/agent-benchmarks/2026-07-10-ecbd-evidence-centered-benchmark-design.md) | A | Requires explicit warrants from intended use through construct, content, treatment, assembly, response extraction, and score interpretation |
| [Validity-Centered AI Evaluation](../papers/agent-benchmarks/2026-07-10-validity-centered-ai-evaluation.md) | A | Prevents schema-valid measurements from being promoted into unsupported capability or readiness claims |
| [Domain-expert participation ethnography](../papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md) | A | Separates contribution, transformation, authority, approval, reciprocity, and withdrawal rather than treating “expert-authored” as one state |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Makes criterion-level expert reasoning inspectable while exposing dependence, applicability, evidence-view, and calibration problems |
| [Consulting cognitive traps](../papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md) | A | Shows how naive paths, expert-visible cues, operations, consequences, and checks can form testable critical incidents across domains |

**Repository consequence:** [`schemas/expertise-transfer.schema.json`](../schemas/expertise-transfer.schema.json), [`schemas/EXPERTISE_TRANSFER.md`](../schemas/EXPERTISE_TRANSFER.md), validity arguments, participation contracts, and the authoring lifecycle in the canonical taxonomy.

## 2. The benchmark should represent broad knowledge work without pretending a small suite represents all work

**Central insight:** Broad occupational or domain coverage is valuable, but a task frame, content pool, administered assembly, and inference population are different denominators. A handful of tasks per occupation does not make a representative sample of work. Pilots should test general principles without becoming accidental scope commitments.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [GDPval](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | A | Demonstrates large-scale expert-authored multimodal occupational task acquisition while exposing sampling, weighting, witness, and inference limitations |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Supplies realistic persona workspaces and file dependencies, while showing that availability, relevance, provenance, observed use, and causal use are distinct |
| [Workflow-GYM](../papers/agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md) | A | Contributes professional workflow/state realism and exposes the need to distinguish task validity, environment validity, and agent failure |
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Demonstrates expert procedural skills, long-horizon artifacts, and observable boundaries without implying one domain should define the full benchmark |

**Repository consequence:** The charter remains cross-domain; pilots must state their general hypothesis, suite assembly needs explicit coverage evidence, and results must bound their inference population.

## 3. Expertise transfer is an intervention that must be separated from the measuring instrument

**Central insight:** When an expert procedure or `SKILL.md` and a rubric come from the same model of expertise, better scores may reflect evaluator-cue compliance rather than genuine transfer. Skills, rubrics, graders, tools, scaffolds, and feedback policies require independent versions and ablations.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Directly motivates public-skill versus private-check boundaries and skill/rubric factorial comparisons |
| [SkillsBench](../papers/agent-benchmarks/2026-07-10-skillsbench-paired-skill-efficacy.md) | A | Sharpens matched skill/no-skill comparisons and the need for repeated paired trials and uncertainty |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Shows why expert-written examples and criteria can improve judge agreement while also anchoring outputs |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Makes the harness and execution boundary explicit so a skill effect is not confused with launcher, tool, or isolation differences |

**Repository consequence:** The benchmark bundle encodes configured-system identity and a no-skill/public-skill × independent/shared-rubric design rather than reporting an unqualified “skill lift.”

## 4. Professional outputs require plural evidence views, not one score

**Central insight:** Final artifacts, workflow states, source use, presentation, safety, efficiency, and human readiness are distinct measurements. A polished artifact can hide unsupported reasoning; a correct final state can coexist with destructive workspace behavior; a grader may lack the representation needed to evaluate its criterion.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [SciVisAgentBench](../papers/agent-benchmarks/2026-07-10-scivisagentbench-multimodal-artifact-evaluation.md) | B | Motivates authoritative artifact views, rendering/control checks, and fail-closed admissibility |
| [MBABench](../papers/agent-benchmarks/2026-07-11-mbabench-spreadsheet-artifact-validity.md) | A | Shows why static values/formulas are weaker than counterfactual recalculation, dependency propagation, rendered communication, and initial-to-final mutation evidence |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Adds persistent workspace identity, protected/mutable zones, mutations, cleanup, and typed dependency evidence |
| [Workflow-GYM](../papers/agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md) | A | Reinforces checkpoint/final-state evidence while warning against attributing invalid environment behavior to the agent |
| [SaaS-Bench](../papers/agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md) | A | Adds deployable cross-application state and dense native checks, while showing that seeded preconditions, dependent consequences, weak joins, and artifact proxies can make a weighted checkpoint score diverge from run-attributable professional progress |
| [GDPval](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | A | Contributes multimodal professional artifacts and expert preference evidence while showing that preference is not an absolute readiness threshold |

**Repository consequence:** Score families remain separate, artifact views have admissibility contracts, and task/trial records preserve both produced artifacts and consequential workspace state. Editable artifacts need native, executable/recalculated, rendered, and trace evidence plus authoritative mutation tests; inherited size and one reference witness do not establish work performed or maintainability. Scored state checks must also distinguish environment readiness from trial-created deltas and identify shared-cause or descendant dependencies.

## 5. Graders and metrics are measured systems with their own failure modes

**Central insight:** Grader outputs are evidence, not ground truth. Every criterion needs an observable predicate, applicable evidence view, provenance, visibility boundary, dependence structure, and uncertainty. Aggregate metrics need explicit eligible populations, missingness policy, clustering, and claim boundaries.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Anthropic agent evaluation lifecycle](concepts/anthropic-agent-evaluation-lifecycle.md) | A | Provides a production vocabulary of tasks, trials, graders, transcripts, and multi-grader evaluation patterns |
| [AgentRewardBench](../papers/agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md) | B | Exposes judge reliability, evidence-view, trajectory, annotation, and observer-access issues |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Contributes inspectable criterion authoring while revealing compensatory mandatory criteria and missing applicability/dependence controls |
| [SaaS-Bench](../papers/agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md) | A | Release audit shows that a checkpoint becomes partial-progress evidence only when it was not pre-satisfied, is attributable to the run, has declared necessity/sufficiency, and does not double-count one upstream event through dependent consequences |
| [Efficient Benchmarking of AI Agents](../papers/agent-benchmarks/2026-07-09-efficient-benchmarking-ai-agents.md) | B | Shows that reduced panels may preserve rank while degrading absolute-score interpretation |
| [Agent Psychometrics](../papers/agent-benchmarks/2026-07-09-agent-psychometrics.md) | B | Treats difficulty as a property of the configured task/system package and motivates response matrices and scaffold-aware reporting |

**Repository consequence:** Criterion/check contracts, metric-monitoring contracts, validity arguments, response matrices, and separate ranking versus absolute-capability claims. Before the second pilot is interpreted, its adversarial audit should plant a pre-satisfied requirement, an unrelated record sharing the expected scalar, a title-only empty artifact, and one upstream defect with several descendant checks; readiness or duplicated consequences must not inflate progress.

## 6. Failures should generate causal diagnostic evidence

**Central insight:** A benchmark should distinguish the surface where failure appeared from the earliest supported cause. Raw traces, failed checks, event locators, recovery chains, attribution confidence, and task/grader/environment validity must remain inspectable.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [STRACE](../papers/agent-benchmarks/2026-07-09-strace.md) | B | Introduces dependency-aware causal slicing and the distinction between surface failure and upstream root cause |
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Adds error → verifier feedback → repair → verification as a measurable recovery chain |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Prevents launcher, permission, tool, and sandbox faults from being mislabeled as capability failures |
| [Amazon production-agent evaluation](concepts/amazon-production-agent-evaluation.md) | B | Adds production-oriented decomposition of tool, memory, reasoning, and end-to-end operational failures |

**Repository consequence:** Root/surface attribution, causal trace slices, recovery records, invalid-trial handling, and task-health lifecycle records.

## 7. Task generation and evolution require conformance, provenance, and rollback

**Central insight:** Shared generated lineage does not guarantee that instructions, environment, witnesses, and checkers remain semantically aligned. Adaptive systems also confound initial ability, feedback exposure, task order, memory changes, retention, and safety drift.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Anchor](../papers/agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md) | B | Motivates a task intermediate representation and bidirectional instruction/environment/witness/check conformance tests |
| [Agentic Context Engineering](../papers/agent-benchmarks/2026-07-10-agentic-context-engineering.md) | C | Shows the value of bounded context deltas while motivating provenance, contradiction, held-out promotion, and rollback controls |
| [Self-evolving agents survey](../papers/agent-benchmarks/2026-07-10-self-evolving-agents-survey.md) | C | Supplies a broad evolution taxonomy and highlights task-order, retention, cost, safety, and feedback confounds |
| [ClawArena](../papers/agent-benchmarks/2026-07-10-clawarena-evolving-information.md) | B | Provides persistent evidence and workspace updates while motivating typed corrections, retractions, supersession, and changed/unchanged checks |

**Repository consequence:** Projection manifests, candidate-lesson lifecycle, longitudinal stream/evolution contracts, immutable hashes, validation gates, and rollback.

These sources are important to the compounding system and adaptive-agent evaluation, but they must not make self-improvement the benchmark's primary objective.

## 8. Safety, contamination, and external validity constrain every result

**Central insight:** Realistic knowledge work includes untrusted content, changing sources, and action consequences. Safety and leakage are not optional score dimensions, and public benchmark artifacts can transition from capability evidence into calibration material after exposure.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [ClawSafety](../papers/agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md) | C | Adds source-authority-to-action-consequence decomposition and warns against ASR without utility, severity, or released scoring contracts |
| [Search-time contamination](../papers/agent-benchmarks/2026-07-10-search-time-contamination.md) | C | Shows why search exposure, exact source overlap, and post-release role changes must be recorded rather than treated as a universal causal inflation estimate |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Makes protected state, unauthorized mutation, and cleanup part of workspace validity |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Contributes execution isolation and side-effect boundaries |

**Repository consequence:** Private-evidence firewalls, role transitions, safety/compliance checks, workspace mutation authorization, and environment-isolation tests. The inert action-safety slice now separates placement, exposure, adoption, attempted and mock-realized action, recovery, residual harm, invalidity, and benign utility across eight synthetic cases with a passing static preflight. This is executable contract evidence only—not a live containment test, agent-capability result, expert validation, or real-world safety evidence.

## 9. Expert scarcity and participation are design problems, not assumptions

**Central insight:** Expert labor should be concentrated at authority-bearing boundaries: elicitation, disagreement, transformation review, calibration, and release approval. The project must measure actual participation cost and fidelity rather than relying on unsupported market estimates.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Domain-expert participation ethnography](../papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md) | A | Provides concrete governance lessons around purpose, reciprocity, authority, transformation, and consent, albeit from one compensated collaboration |
| [Benchmark Ceiling](../papers/agent-benchmarks/2026-07-10-benchmark-ceiling-expert-labor-scarcity.md) | C | Raises renewal and expert-scarcity questions but does not provide auditable evidence for its headline cost/labor claims |
| [GDPval](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | A | Demonstrates expert task acquisition at scale while leaving important representativeness and expert-ceiling questions unresolved |
| [Consulting cognitive traps](../papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md) | A | Shows the potential value of SME-authored critical incidents while its missing released task/grader artifacts limit reuse evidence |

**Repository consequence:** Expert-participation contracts, contributor provenance/authority, measured recruitment and review burden, reciprocal outputs, and continued research into near-zero-cost incentives.

## Current reading priority

If you want the smallest high-value reading sequence, use:

1. [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md) — objective and anti-drift boundary.
2. [`benchmark-design-taxonomy.md`](benchmark-design-taxonomy.md) — grouped technical synthesis.
3. [LH-Bench review](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) — expertise as procedure and intervention.
4. [ECBD review](../papers/agent-benchmarks/2026-07-10-ecbd-evidence-centered-benchmark-design.md) — validity warrants across the design chain.
5. [GDPval review](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) — broad occupational artifacts and inference limits.
6. [ResearchRubrics review](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) — expert criterion authoring and grader limitations.
7. [Workspace-Bench review](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) — realistic workspaces, files, provenance, and state.
8. [Domain-expert participation review](../papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md) — governance and expert involvement.
9. [STRACE review](../papers/agent-benchmarks/2026-07-09-strace.md) — causal failure diagnosis.
10. [`schemas/README.md`](../schemas/README.md) — how the synthesis is becoming executable.

## Maintenance rules

The consolidator should update this file when:

- a deep review adds a genuinely new insight group;
- a paper materially changes relevance tier;
- a source is superseded, contradicted, or weakened by release inspection;
- a grouped insight becomes executable infrastructure;
- the charter changes its objectives or success criteria.

Do not add every discovered paper. Triage-only and low-relevance sources belong in the paper index or scouting reports until they materially affect a grouped insight.
