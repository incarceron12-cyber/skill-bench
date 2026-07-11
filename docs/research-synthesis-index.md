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
| [Data Therapist](../papers/agent-benchmarks/2026-07-11-data-therapist-tacit-knowledge-elicitation.md) | A | Makes the elicitation instrument and its path-dependent selection effects visible; separates annotation yield from corroboration, scope, transformation fidelity, and benchmark utility |
| [SimInstruct](../papers/agent-benchmarks/2026-07-11-siminstruct-simulated-novice-elicitation.md) | B | Treats simulated interlocutor behavior as an elicitation treatment; motivates productive-friction probes, phase labels, correction lineage, and separate participation-versus-utility outcomes |
| [EnterpriseClawBench](../papers/agent-benchmarks/2026-07-11-enterpriseclawbench-session-derived-validity.md) | A | Separates observed workplace demand from the rewritten counterfactual task; requires projection deltas, hindsight controls, equivalence review, and a claim licensed to the evidence actually preserved |

**Repository consequence:** [`schemas/expertise-transfer.schema.json`](../schemas/expertise-transfer.schema.json), [`schemas/EXPERTISE_TRANSFER.md`](../schemas/EXPERTISE_TRANSFER.md), validity arguments, participation contracts, and the authoring lifecycle in the canonical taxonomy. Mixed-initiative or simulated-interlocutor elicitation must preserve an unprompted-before-probed boundary and event lineage for offered, displayed, answered, rejected, revised, withdrawn, skipped, and stopped interactions; requested versus realized resistance and the triggering utterance must remain visible. Dialogue/word volume and conversational fluency are not expertise yield: measure grounded thresholds, contradictions, failure signatures, correction burden, contributor value/privacy, and downstream task/check utility separately. Machine responsiveness checks do not confer epistemic or expert authority. Source-derived tasks are versioned projections: observed demand and resolution, omitted context, transformations, hindsight sources, target counterfactual, equivalence disposition, and licensed use remain distinct. Real provenance can support demand-inspired coverage while replay fidelity remains unsupported.

## 2. The benchmark should represent broad knowledge work without pretending a small suite represents all work

**Central insight:** Broad occupational or domain coverage is valuable, but a task frame, content pool, administered assembly, and inference population are different denominators. A handful of tasks per occupation does not make a representative sample of work. Pilots should test general principles without becoming accidental scope commitments.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [GDPval](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | A | Demonstrates large-scale expert-authored multimodal occupational task acquisition while exposing sampling, weighting, witness, and inference limitations |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Supplies realistic persona workspaces and file dependencies, while showing that availability, relevance, provenance, observed use, and causal use are distinct |
| [HippoCamp](../papers/agent-benchmarks/2026-07-11-hippocamp-personal-context-validity.md) | B | Separates composite contextual evidence and answer agreement from task-time authorization, causal adoption, consequential action, affected-party validation, and faithful personalization |
| [Workflow-GYM](../papers/agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md) | A | Contributes professional workflow/state realism and exposes the need to distinguish task validity, environment validity, and agent failure |
| [WorkArena++](../papers/agent-benchmarks/2026-07-11-workarena-plus-compositional-validity.md) | B | Makes executable setup/oracle/validator composition inspectable while showing that longer chains and lower success do not by themselves establish planning, workflow realism, or occupational coverage |
| [TheAgentCompany](../papers/agent-benchmarks/2026-07-11-theagentcompany-workplace-simulation-validity.md) | A | Separates integrated workplace substrate and selected workflow coherence from authority, consequence, sampling, collaboration, and labor-automation validity |
| [OdysseyBench](../papers/agent-benchmarks/2026-07-11-odysseybench-longitudinal-office-memory-validity.md) | B | Connects dialogue-distributed requirements to office-state action while exposing persistent-memory, evaluator-dispatch, collateral-state, and professional-validity gaps |
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Demonstrates expert procedural skills, long-horizon artifacts, and observable boundaries without implying one domain should define the full benchmark |
| [Agents' Last Exam](../papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md) | A | Contributes broad executable workflow machinery while separating occupational frame, workflow universe, realized/versioned suite, and licensed inference population |
| [Design Report for Knowledge-Work Benchmarks](../papers/agent-benchmarks/2026-07-11-design-report-knowledge-work-benchmarks.md) | A | Adds a work-activity → tested-setting → persistent-product → licensed-claim reporting chain and makes omitted responsibilities and downstream handoffs explicit; its preliminary 18-label inventory is a revisable vocabulary, not validated coverage |
| [Professional benchmark evolution matrix](concepts/professional-benchmark-evolution-matrix.md) | A | Compares AA-Briefcase/Lite, GDPval, Workspace-Bench, MBABench, LH-Bench, Workflow-GYM, SaaS-Bench, and Agents' Last Exam as repairs to different links in one evidence chain; distinguishes implemented machinery from demonstrated validity |
| [Web/tool/computer benchmark evolution](concepts/web-tool-computer-benchmark-evolution.md) | B | Compares GAIA, WebArena, ToolBench, API-Bank, τ-bench, OSWorld, AndroidWorld, and BrowseComp; shows that interactive realism migrates the oracle into authored state, simulators, lifecycle hooks, and selected predicates |

**Repository consequence:** The charter remains cross-domain; pilots must state their general hypothesis, suite assembly needs explicit coverage evidence, and results must bound their inference population. A nonempty occupation/subdomain/activity cell is coverage, not representativeness or readiness. Map each task many-to-many to target, required, incidental, and explicitly omitted work activities, retaining the source frame and reviewer disposition rather than freezing one occupational vocabulary. Expert submission, engineer implementation, grader construction, and post-transformation expert disposition require separate authority records.

Tested-setting choices are interventions on the supported claim. Preselected
sources, prescribed output forms, clean workspaces, one-shot interaction,
simulators, and executable oracles may make an experiment reproducible while
removing discovery, product choice, coordination, institutional consequence, or
downstream use. Record those removals as explicit claim subtraction. Bind a
persistent product or state to its recipient and next operation, then inspect
source fidelity, scope/boundary compliance, and destination usability separately.
The strongest supported claim and named excluded claims should accompany every
result; visual occupational resemblance does not supply the missing links.

The comparative evolution view adds a second boundary: a newer benchmark is
not automatically a validated successor because it adds more files, longer
trajectories, native state, or deterministic checks. A claimed repair needs a
direct falsification test at the repaired link. Current evidence supports broad
task acquisition (GDPval/ALE), source/check traceability (AA-Briefcase-Lite),
workspace and state substrates (Workspace-Bench/SaaS-Bench), native artifact
inspection (MBABench), and observable expert procedures (LH-Bench) more strongly
than it supports occupational representativeness, longitudinal project work,
counterfactual artifact integrity, checkpoint progress, or professional
readiness. OfficeBench remains an explicit primary-source audit gap; the completed
WorkArena++ audit closes the composition-method gap but not occupational validity.

Executable composition is therefore a construction mechanism, not a construct
argument. A composite task needs a typed obligation DAG with prerequisites,
produced/consumed state, equivalent paths, and reversibility; milestone observations
must be rechecked against terminal invariants, with validator cadence and reset
attestations retained as instrument identity. Compare observed composite outcomes
with matched atomic baselines using family-clustered uncertainty, but interpret any
gap as diagnostic until workflow provenance and controlled horizon, interface, and
information-budget comparisons support a planning or realism claim. The internal
[composite-workflow replay](../pilots/composite-workflow-conformance/README.md)
demonstrates poll-order-independent reversal detection and earliest unsupported-
dependency localization on two synthetic work shapes only; it supplies no agent,
occupational, planning, safety, cross-software, or readiness evidence.

Workplace validity therefore needs a **substrate-to-consequence evidence ladder**:
occupational/task provenance; service and initial-state validity; requirement or
history availability, access, authority recognition, and adoption; actor/NPC
authority; action execution; intended and collateral state deltas; evaluator
dispatch and evidence sufficiency; then a licensed claim. TheAgentCompany supplies
strong integrated-service evidence and some cross-service coherence, but its one
invented software company, convenience/verifier-shaped tasks, unvalidated LLM
coworkers, permissive sampled checks, and unproven shared-service resets leave the
later links weak. OdysseyBench supplies inspectable generated requirement lineage
and evidence-to-office-state tasks, but histories are delivered at evaluation
rather than accumulated, prior work is simulated, source testbeds are external,
and dominant existence/substring predicates omit artifact and collateral-state
quality. Neither licenses occupational sampling, persistent memory, human-like
collaboration, professional validity, capability, labor automation, or readiness.
The internal [experience-memory replay](../pilots/experience-memory-transfer/README.md)
separates raw-history success, summary omission, stale adoption, required-state
failure, collateral mutation, and unavailable-evaluator invalidity in one
deterministic synthetic fixture only; it is implementation evidence, not empirical
support for the planted causal story or any workplace claim.

Context-heavy tasks add an authority boundary before the workplace ladder:
**availability → authorization → access → observation → interpretation → adoption
→ answer/artifact acceptance → state consequence → affected-party validation**.
No rung inherits the next. Corpus-creation consent is not task-time permission for
every inference; an authored minimal support set must admit reviewed alternatives;
and semantic answer agreement cannot prove evidence use, privacy safety, correct
action, or user benefit. HippoCamp supplies multimodal localized-support and
interface evidence from three edited cross-person composites, but no single user
can validate those composite profiles; its answer-only judge cannot inspect
sources, and unavailable corpus/audit/result records prevent independent replay.
Existing consent, artifact-view, trace, workspace-state, task-health, metric, and
validity records implement this ladder; no personal-computing scope commitment or
personalization, professional-capability, privacy-safety, or readiness claim follows.

Interactive families add a parallel boundary. Executable outcome checks are a
real repair over action-sequence imitation because they admit alternative paths,
but a passing selected predicate is not proof of complete, safe, or
professionally usable work. Live web improves ecological substrate while
weakening repeat equivalence; frozen APIs improve reproducibility by simplifying
the world; model-simulated users add interaction while becoming part of the
treatment. Every task therefore needs a projection ledger for native/simulated
substrate, authored initial state, observer coverage, omitted consequences,
simulator identity, reset health, and the claims that survive those choices.

## 3. Expertise transfer is an intervention that must be separated from the measuring instrument

**Central insight:** When an expert procedure or `SKILL.md` and a rubric come from the same model of expertise, better scores may reflect evaluator-cue compliance rather than genuine transfer. Skills, rubrics, graders, tools, scaffolds, and feedback policies require independent versions and ablations.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Directly motivates public-skill versus private-check boundaries and skill/rubric factorial comparisons |
| [SkillsBench](../papers/agent-benchmarks/2026-07-10-skillsbench-paired-skill-efficacy.md) | A | Sharpens matched skill/no-skill comparisons and the need for repeated paired trials and uncertainty |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Shows why expert-written examples and criteria can improve judge agreement while also anchoring outputs |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Makes the harness and execution boundary explicit so a skill effect is not confused with launcher, tool, or isolation differences |
| [KWBench](../papers/agent-benchmarks/2026-07-11-kwbench-unprompted-problem-recognition.md) | A | Identifies situation framing before named-workflow execution, while showing that a cold final-artifact gate does not isolate recognition from inquiry, action, domain knowledge, or grading |

**Repository consequence:** The benchmark bundle encodes configured-system identity and a no-skill/public-skill × independent/shared-rubric design rather than reporting an unqualified “skill lift.” Recognition is a different intervention axis: preserve situation-only, minimally framed, and fully specified conditions, positive and negative near neighbors, and separate observations for cue extraction, problem framing, targeted inquiry, action, and artifact consequence. A recognition frame names or narrows the problem; a procedural skill prescribes how to solve it; a rubric or evaluator cue reveals what will be rewarded. Their versions and effects must not be collapsed. The internal problem-recognition replay exercises this staged instrumentation and invalid-environment abstention on builder-authored synthetic cases only; it supplies no expert validity, agent result, treatment effect, prevalence, or cross-domain claim ([replay](../pilots/problem-recognition-intervention/replay-report.json)).

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
| [Agents' Last Exam](../papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md) | A | Shows why deterministic artifact grading still needs clean-start attestation, requested-criterion coverage, alternate-path tests, and verifier falsification |

**Repository consequence:** Score families remain separate, artifact views have admissibility contracts, and task/trial records preserve both produced artifacts and consequential workspace state. Editable artifacts need native, executable/recalculated, rendered, and trace evidence plus authoritative mutation tests; inherited size and one reference witness do not establish work performed or maintainability. Scored state checks must also distinguish environment readiness from trial-created deltas and identify shared-cause or descendant dependencies. The internal initial-state replay rejects pre-satisfied, stale, copied-witness, and omitted-transition cases, accepts a declared alternative, and abstains on invalid initialization; its seven synthetic matches validate only fixture/scorer behavior ([replay](../pilots/task-initial-state-conformance/replay-report.json)).

## 5. Graders and metrics are measured systems with their own failure modes

**Central insight:** Grader outputs are evidence, not ground truth. Every criterion needs an observable predicate, applicable evidence view, provenance, visibility boundary, dependence structure, and uncertainty. Aggregate metrics need explicit eligible populations, missingness policy, clustering, and claim boundaries.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Anthropic agent evaluation lifecycle](concepts/anthropic-agent-evaluation-lifecycle.md) | A | Provides a production vocabulary of tasks, trials, graders, transcripts, and multi-grader evaluation patterns |
| [AgentRewardBench](../papers/agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md) | B | Exposes judge reliability, evidence-view, trajectory, annotation, and observer-access issues |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Contributes inspectable criterion authoring while revealing compensatory mandatory criteria and missing applicability/dependence controls |
| [JADE](../papers/agent-benchmarks/2026-07-11-jade-dynamic-professional-grading.md) | B | Separates invariant requirements from response-created claims/consequences, while exposing variable denominators, shared-cue judging, verifier fail-open behavior, and unvalidated score fusion |
| [SaaS-Bench](../papers/agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md) | A | Release audit shows that a checkpoint becomes partial-progress evidence only when it was not pre-satisfied, is attributable to the run, has declared necessity/sufficiency, and does not double-count one upstream event through dependent consequences |
| [Efficient Benchmarking of AI Agents](../papers/agent-benchmarks/2026-07-09-efficient-benchmarking-ai-agents.md) | B | Shows that reduced panels may preserve rank while degrading absolute-score interpretation |
| [Agent Psychometrics](../papers/agent-benchmarks/2026-07-09-agent-psychometrics.md) | B | Treats difficulty as a property of the configured task/system package and motivates response matrices and scaffold-aware reporting |
| [Expert evaluation and limits of human feedback](../papers/agent-benchmarks/2026-07-11-expert-disagreement-human-feedback-validity.md) | A | Shows in one small clinical panel that shared rubrics can yield stable directional disagreement; motivates framework-indexed observations and policy-explicit aggregation without universalizing the domain result |
| [Many-facet human/AI rater effects](../papers/agent-benchmarks/2026-07-11-many-facet-human-ai-rater-effects.md) | B | Separates agreement, panel-relative severity, model fit, repeat stability, and decision validity; shows why a linked calibration design does not make graders interchangeable |
| [Rubric-modification interventions](../papers/agent-benchmarks/2026-07-11-rubric-modification-human-autorater-agreement.md) | B | Makes examples, context, criterion-call topology, score transformation, and aggregation part of instrument identity; agreement gains can coexist with shared cueing or construct change |
| [AI Agent Reliability](../papers/agent-benchmarks/2026-07-11-agent-reliability-profile.md) | B | Separates accuracy from repeatability, perturbation sensitivity, confidence quality, and violation consequences while binding each estimate to a configured operational profile |
| [LiveBench](../papers/agent-benchmarks/2026-07-11-livebench-contamination-limited-lifecycle.md) | B | Makes benchmark renewal operational through rotating recent-source forms, temporary private roles, deterministic checks, and reruns, while exposing equivalent-form, outcome-conditioned selection, exposure, and grader-drift limits |
| [Reasoning/coding benchmark evolution](concepts/reasoning-coding-benchmark-evolution.md) | B | Compares MMLU→MMLU-Pro and HumanEval→LiveCodeBench from full papers and pinned current releases; separates common-interface adoption, demonstrated headroom/prompt stability, executable equivalence, and timestamped renewal from unsupported work-validity and contamination-free claims |
| [BrowserGym](../papers/agent-benchmarks/2026-07-11-browsergym-ecosystem-measurement.md) | B | Separates useful runner/interface interoperability from unsupported evaluator, score, reset, or construct equivalence across adapted benchmark families |

**Repository consequence:** Criterion/check contracts, metric-monitoring contracts, validity arguments, response matrices, and separate ranking versus absolute-capability claims. Grader identity includes rubric/examples, evidence view, criterion execution topology, score transformation, aggregation/tie policy, and configured rater. Agreement, panel-relative severity, fit, repeated-call stability, construct preservation, decision loss, cost, and audit burden remain separate outcomes; adjusted scores never overwrite raw observations or become adjudicated truth. Reliability is a conditional profile—not a system trait—indexed by configured system, task/form population, environment, time, intervention/exposure distribution, and consequence model. Accuracy, repeatability (including consistently wrong behavior), resource variation, perturbation effects, confidence quality, violation frequency, severity, remediation, and loss remain separate. Every perturbation needs independently supported preservation and exposure claims; wrapper recovery cannot count as agent recovery; confidence is licensed only for the decision time and evidence view at which it was elicited. Plural judgments remain immutable observations; aggregation is a versioned stakeholder/error-loss policy rather than discovered ground truth. Specification error, evidence gaps, rater instability, framework-conditioned disagreement, policy selection with dissent, and unresolved value conflict require distinct dispositions. The completed synthetic plural-judgment conformance slice exercises this boundary but supplies no prevalence, professional-consensus, or readiness evidence. Before the second pilot is interpreted, its adversarial audit should plant a pre-satisfied requirement, an unrelated record sharing the expected scalar, a title-only empty artifact, and one upstream defect with several descendant checks; readiness or duplicated consequences must not inflate progress.

Open-ended grading adds a two-population boundary. Fixed requirements retain a
common public basis and denominator; response-triggered criteria may inspect only
claims, dependencies, side effects, contradictions, or artifact elements that the
submission actually creates. Each contingent criterion needs a trigger locator,
typed applicability and public basis, authority/evidence view, overlap and
dependency relations, generation identity, and `supported`, `contradicted`,
`insufficient`, or `not_applicable` evidence state. Report fixed completion,
contingent claim reliability, evidence-conditioned reasoning, source authority,
and abstention burden separately until fusion is independently calibrated. JADE's
30-task/180-report human comparison, clustered correlations without uncertainty,
withheld rich skills, shared model cues, outcome-conditioned HealthBench trimming,
mutable live web, unsupported authority tiers/80% threshold, missing result
artifacts, and close post-v1 release bound it to Tier B evaluator-design evidence;
its inspected default fail-open fallback directly motivates capability-claim
abstention when verification is unavailable.

A common runner adds an adapter boundary rather than removing benchmark identity.
For every adapted family, preserve three independent records: the canonical
benchmark contract (task/split, upstream dataset and evaluator, backend/state, and
native defaults), the adapter realization (field/action/reward/termination/error
maps plus transformed or dropped semantics), and the trial policy (agent,
observation/action defaults, budgets, retries, invalid handling, resets, and
aggregation). BrowserGym's inspected MiniWoB, WebArena, AssistantBench, and later
WebArena Verified paths retain materially different reward and evaluator meanings
behind one scalar interface; its 2026 release is not the 2024 paper implementation.
Therefore report family-specific scores and typed retry/reset/invalid ledgers.
Native-versus-adapted differential tests from frozen state—comparing score,
termination, side effects, and evaluator evidence—are required before a semantic-
preservation claim. API compatibility alone licenses no pooled capability,
measurement-equivalence, safety, or professional-validity claim.

## 6. Failures should generate causal diagnostic evidence

**Central insight:** A benchmark should distinguish the surface where failure appeared from the earliest supported cause. Raw traces, failed checks, event locators, recovery chains, attribution confidence, and task/grader/environment validity must remain inspectable.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [STRACE](../papers/agent-benchmarks/2026-07-09-strace.md) | B | Introduces dependency-aware causal slicing and the distinction between surface failure and upstream root cause |
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Adds error → verifier feedback → repair → verification as a measurable recovery chain |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Prevents launcher, permission, tool, and sandbox faults from being mislabeled as capability failures |
| [Amazon production-agent evaluation](concepts/amazon-production-agent-evaluation.md) | B | Adds production-oriented decomposition of tool, memory, reasoning, and end-to-end operational failures |
| [AARRI-Bench](../papers/agent-benchmarks/2026-07-11-aarri-research-judgment-lifecycle.md) | A | Makes stop, refuse, escalate, clarify, and preserve legitimate consequence-bearing outcomes while directly exposing lexical-verifier false rejection |

**Repository consequence:** Root/surface attribution, causal trace slices, recovery records, invalid-trial handling, and task-health lifecycle records. Apparent requests should also admit a counterfactual action contract: observable disqualifying evidence, authority and threshold, legitimate alternatives, required state and communication consequences, abstention/escalation, and collateral harm. Decision, rationale, artifact preservation, communication, cost, and harm remain separate observations. Matched persist/stop and comply/dissent forms are required to distinguish calibrated judgment from generic quitting or contrarianism; substantive action must be tested independently of lexical realization, with paraphrase contrasts and retained semantic adjudication. AARRI's inspectable authored suite motivates this design but its missing sampling frame, contributor accounting, human baseline/agreement, repeats/uncertainty, verifier-wide audit, complete configuration, contamination-safe split, environment evidence, and paper-pinned release prevent researcher-quality or cross-domain capability claims.

## 7. Task generation and evolution require conformance, provenance, and rollback

**Central insight:** Shared generated lineage does not guarantee that instructions, environment, witnesses, and checkers remain semantically aligned. Adaptive systems also confound initial ability, feedback exposure, task order, memory changes, retention, and safety drift.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Anchor](../papers/agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md) | B | Motivates a task intermediate representation and bidirectional instruction/environment/witness/check conformance tests |
| [Agentic Context Engineering](../papers/agent-benchmarks/2026-07-10-agentic-context-engineering.md) | C | Shows the value of bounded context deltas while motivating provenance, contradiction, held-out promotion, and rollback controls |
| [Self-evolving agents survey](../papers/agent-benchmarks/2026-07-10-self-evolving-agents-survey.md) | C | Supplies a broad evolution taxonomy and highlights task-order, retention, cost, safety, and feedback confounds |
| [ClawArena](../papers/agent-benchmarks/2026-07-10-clawarena-evolving-information.md) | B | Provides persistent evidence and workspace updates while motivating typed corrections, retractions, supersession, and changed/unchanged checks |
| [LongMemEval-V2](../papers/agent-benchmarks/2026-07-11-longmemeval-v2-environment-experience-memory.md) | B | Separates trajectory-history storage from bounded evidence delivery and shows representation/reader effects; does not measure held-out action transfer or harmful stale guidance |

**Repository consequence:** Projection manifests, candidate-lesson lifecycle, longitudinal stream/evolution contracts, immutable hashes, validation gates, and rollback. Experience-derived knowledge needs two linked, non-substitutable estimands: evidence-grounded retrospective retrieval and intervention benefit on held-out action. Failed attempts, realized procedures, inferred causes, environment/version scope, stale claims, safe alternatives, and harmful transfer must remain typed rather than flattened into notes.

The internal experience-memory replay now makes that separation executable for one deterministic synthetic fixture: evidence-only memory answers retrospective QA correctly while producing harmful stale transfer, whereas provenance-gated promotion passes both QA and the planted held-out safety check ([replay](../pilots/experience-memory-transfer/replay-report.json)). This validates fixture and validator behavior, not the planted causal story, a general promotion policy, agent-memory improvement, professional competence, or deployment safety. Real validation requires unseen task families, repeated stochastic consumers, source-clustered uncertainty, rollback probes, and expert-grounded action consequences.

These sources are important to the compounding system and adaptive-agent evaluation, but they must not make self-improvement the benchmark's primary objective.

## 8. Safety, contamination, and external validity constrain every result

**Central insight:** Realistic knowledge work includes untrusted content, changing sources, and action consequences. Safety and leakage are not optional score dimensions, and public benchmark artifacts can transition from capability evidence into calibration material after exposure.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [ClawSafety](../papers/agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md) | C | Adds source-authority-to-action-consequence decomposition and warns against ASR without utility, severity, or released scoring contracts |
| [Search-time contamination](../papers/agent-benchmarks/2026-07-10-search-time-contamination.md) | C | Shows why search exposure, exact source overlap, and post-release role changes must be recorded rather than treated as a universal causal inflation estimate |
| [LiveBench](../papers/agent-benchmarks/2026-07-11-livebench-contamination-limited-lifecycle.md) | B | Shows that recent sources and rolling private forms limit some direct exposure but do not prove contamination absence; source, exposure, instrument, and configured-system clocks must remain separate |
| [Agents' Last Exam](../papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md) | A | Its post-paper split drift shows that a tier label is not suite identity; membership, outcome-selection, exposure, role transition, replacement bridge, and retirement must be versioned |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Makes protected state, unauthorized mutation, and cleanup part of workspace validity |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Contributes execution isolation and side-effect boundaries |

**Repository consequence:** Private-evidence firewalls, role transitions, safety/compliance checks, workspace mutation authorization, and environment-isolation tests. Rolling forms require four independent clocks—source availability, exposure/visibility, instrument version, and configured-system execution. Difficulty-conditioned replacement keeps challenge alive but changes the administered population; without frozen anchors or equivalent-form bridges, rank stability cannot license absolute capability trends. Grader repair creates linked new observations rather than rewriting historical scores. The inert action-safety slice now separates placement, exposure, adoption, attempted and mock-realized action, recovery, residual harm, invalidity, and benign utility across eight synthetic cases with a passing static preflight. This is executable contract evidence only—not a live containment test, agent-capability result, expert validation, or real-world safety evidence.

## 9. Expert scarcity and participation are design problems, not assumptions

**Central insight:** Expert labor should be concentrated at authority-bearing boundaries: elicitation, disagreement, transformation review, calibration, and release approval. The project must measure actual participation cost and fidelity rather than relying on unsupported market estimates.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Domain-expert participation ethnography](../papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md) | A | Provides concrete governance lessons around purpose, reciprocity, authority, transformation, and consent, albeit from one compensated collaboration |
| [Benchmark Ceiling](../papers/agent-benchmarks/2026-07-10-benchmark-ceiling-expert-labor-scarcity.md) | C | Raises renewal and expert-scarcity questions but does not provide auditable evidence for its headline cost/labor claims |
| [GDPval](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | A | Demonstrates expert task acquisition at scale while leaving important representativeness and expert-ceiling questions unresolved |
| [Consulting cognitive traps](../papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md) | A | Shows the potential value of SME-authored critical incidents while its missing released task/grader artifacts limit reuse evidence |
| [SimInstruct](../papers/agent-benchmarks/2026-07-11-siminstruct-simulated-novice-elicitation.md) | B | Demonstrates paid asynchronous role-play feasibility in one network while leaving recruitment denominators, actual burden, privacy/consent lineage, tacit-knowledge yield, and downstream utility unmeasured |

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
