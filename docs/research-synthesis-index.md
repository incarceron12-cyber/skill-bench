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
| [AlphaEval](../papers/agent-benchmarks/2026-07-11-alphaeval-production-grounded-validity.md) | A | Separates current company-demand provenance from requirement projection, grader validity, configured-package comparison, occupational inference, and economic value |
| [$OneMillion-Bench](../papers/agent-benchmarks/2026-07-14-onemillion-professional-value-validity.md) | A | Releases 400 detailed bilingual research tasks and 6,758 criteria while showing why human task cost, rubric score, thresholded acceptance, workflow savings, and realized economic value must remain separate records |
| [Industrial expertise codification](../papers/agent-benchmarks/2026-07-11-industrial-expertise-codification-agent.md) | A | Types codified knowledge by execution semantics and bounds a co-designed package effect away from tacit transfer, expert equivalence, and cross-domain generalization |
| [JobBench](../papers/agent-benchmarks/2026-07-12-jobbench-delegation-desire-validity.md) | A | Makes worker-reported delegation preference a typed portfolio-selection signal while separating it from package fidelity, present consent, workflow uptake, and worker outcomes |
| [Benchmark-to-risk expert elicitation](../papers/agent-benchmarks/2026-07-12-benchmark-to-risk-expert-elicitation.md) | A | Makes the score-to-consequence warrant observable as structured disagreement and separates capability interpretation, scenario use, workflow effect, outcome composition, and decision loss |
| [OfficeEval](../papers/agent-benchmarks/2026-07-12-officeeval-standardized-exam-validity.md) | B | Separates external requirement/weight lineage from the validity of a transformed subset, administration, aggregate, or transported decision threshold |
| [Laboratory workflow twins](../papers/agent-benchmarks/2026-07-13-laboratory-workflow-expert-elicitation.md) | A | Adds claim-level authority gates, mandatory nulls, exact evidence→claim→projection lineage, and masking-channel diagnosis while separating graph executability from knowledge truth or operational validity |
| [SovereignPA-Bench](../papers/agent-benchmarks/2026-07-13-sovereignpa-consent-mediation-validity.md) | B | Separates current intent, memory, third-party pressure, evidence, consent, and burden while exposing that a hidden author oracle and rubric-matched scaffold do not establish user authority, realized action, or benefit |
| [SOP-Bench](../papers/agent-benchmarks/2026-07-14-sop-bench-procedure-task-validity.md) | A | Makes the procedure→schema→row→tool→oracle→parser chain executable, while showing that asserted expert validation and endpoint agreement do not establish procedure fidelity without item-level lineage, conformance contracts, leakage controls, typed comparators, and independent oracle derivation |

**Repository consequence:** [`schemas/expertise-transfer.schema.json`](../schemas/expertise-transfer.schema.json), [`schemas/EXPERTISE_TRANSFER.md`](../schemas/EXPERTISE_TRANSFER.md), validity arguments, participation contracts, and the authoring lifecycle in the canonical taxonomy. Mixed-initiative or simulated-interlocutor elicitation must preserve an unprompted-before-probed boundary and event lineage for offered, displayed, answered, rejected, revised, withdrawn, skipped, and stopped interactions; requested versus realized resistance and the triggering utterance must remain visible. Dialogue/word volume and conversational fluency are not expertise yield: measure grounded thresholds, contradictions, failure signatures, correction burden, contributor value/privacy, and downstream task/check utility separately. Machine responsiveness checks do not confer epistemic or expert authority. Source-derived tasks are versioned projections: observed demand and resolution, omitted context, transformations, hindsight sources, target counterfactual, equivalence disposition, and licensed use remain distinct. Real provenance can support demand-inspired coverage while replay fidelity remains unsupported.

The combined evidence supports a **demand-to-transfer chain**, not a shortcut:
`demand provenance → elicitation authority → representation/codification →
source-to-task projection → configured intervention → independent measurement →
bounded package/transfer/use claim`. AlphaEval provides meaningful evidence for
prospective partner demand, recurring co-design, package construction, and selected
configured-package outcomes; its seven purposive partners, private 94-task corpus,
unreleased transformations/results, nonfactorial scaffold matrix, winner-only
repeats, and post-v1 framework release block occupational, readiness, causal
scaffold, and economic-value promotion. The Siemens case provides evidence that a
bundled rules/prompt/routing/RAG package improved five selected, rule-aligned
visualization outputs; two eliciting experts, task–rule–criterion co-design, no
component ablations, no rater reliability, and one organization/workflow block
tacit-transfer, expert-equivalence, and cross-domain claims. Confidentiality can
legitimately prevent release, but it remains missing audit evidence rather than
positive validity evidence. Existing participation, expertise-transfer, projection,
configured-system, metric, task-health, and validity records are the durable homes.

JobBench adds a distinct **delegation-demand ladder**:
`historical preference observation → duty-to-package transformation fidelity →
present consent and retained authority → configured-system task measurement →
observed workflow uptake → measured worker outcome`. No rung inherits the next.
Preference is one portfolio signal alongside construct coverage, feasibility,
frequency, consequence, and economic value; it is not a capability weight or a
benefit measure. The immutable v1 paper and pinned post-v1 release support a
purposive, artifact-rich instrument, but not occupational estimates: the frame is
filtered by wages and benchmarkability, occupations have only one to three Main
tasks, and admission uses outcome-conditioned union solvability. Incompatible
GDPval scores, aggregate-only model-judge comparison, incomplete structured and
visual evidence views, a Codex runner with sandboxing disabled, mutable retrieval,
and the paper/release mismatch (130 reported tasks/4,631 criteria versus 128
released tasks/4,576 criteria) further bound interpretation. Existing demand,
participation/consent, task-projection, artifact-admissibility, execution-validity,
task-health, metric, and validity records should carry the links; no new schema or
occupational scope commitment follows.

Consequence promotion adds a separate **benchmark-to-decision chain**:
`benchmark observation → bounded capability interpretation → scenario
applicability/access/use → conditional workflow effect → outcome
composition/frequency/severity → stakeholder threshold/loss`. No link inherits the
next, and expert elicitation is evidence about a warrant rather than a score
transform. Preserve the immutable information packet and task order; initial and
revised estimates with rationale changes; peer/moderator exposure and discussion-
group dependence; disagreement cruxes and estimand forks; calibration/seed status;
pooling, missingness, exclusion, and aggregation sensitivity; unsupported links;
and the next discriminating evidence. The reviewed IDEA-derived pilot shows that
seven complete respondents in two groups can expose rival task-to-work warrants,
but its ordered five-task treatment, generated solution-adjacent summaries,
ambiguous scenario, unauditable baseline, unreported Bayesian specification, and
absence of direct outcomes or decision use support neither calibrated uplift nor
cyber risk. Existing validity, metric-monitoring, participation, and future
elicitation-session records are the durable homes; a direct matched workflow-uplift
study is preferable when feasible, and no new schema, cyber scope commitment,
expected-harm, capability, deployment, professional-validity, or readiness claim
follows.

Authority and observability add another cross-cutting chain:
`source span/probe/channel → authority-gated claim or explicit null → contextual,
valid-time, disagreement-bearing transformation → intermediate representation →
task/public basis/check projection → plural observation → bounded claim`. A role
licenses only the claim layer and use for which it has evidence; provenance does
not imply transformation approval or consent for agent/runtime or private-grader
reuse. Execution-channel success must remain separate from substantive validity:
a `MASKED_BY`-style relation links a supported root invariant to a misleading
surface signal, but is itself a causal/observability hypothesis until incident,
intervention, or independent review supports it. Preserve root evidence, channel
status, independent artifact/state view, detection, recovery, residual consequence,
and unknown states separately.

The laboratory source demonstrates graph population and seven query patterns
after four reported assay sessions in one department. Its proprietary prompts
and load files, absent transcripts and claim-level transformations, uncalibrated
confidence mapping, no independent ground truth, no operational outcomes, and no
cross-domain test block knowledge-accuracy, professional-validity, benefit,
transfer, and readiness claims. Existing expertise-transfer, participation,
evidence-state, projection, artifact-admissibility, trace, root/surface, and
validity records suffice; no graph or masking subsystem follows.

Representative action adds a principal/mediation boundary: `current intent →
memory applicability → third-party proposition → evidence and consent basis →
legitimate terminal set → attempted action/disclosure → policy/environment
decision → realized state/information flow → utility, burden, and affected-party
review`. A current-looking instruction need not come from an authorized principal;
a platform proposition does not inherit authority over the user; and asking for
consent can itself be unnecessary burden. SovereignPA-Bench motivates the typed
signals and plural outcomes, but its unreleased 120 synthetic prompts, hidden
author labels, unspecified metrics, rubric-matched bundled scaffold, parsed rather
than realized actions, and absent represented-user validation support only an
authored prompt-policy stress-test claim. Existing participation/consent,
authority, information-flow, action-safety, state, metric, and validity records
already host this chain; no personal-agent or sovereignty schema follows.

## 2. The benchmark should represent broad knowledge work without pretending a small suite represents all work

**Central insight:** Broad occupational or domain coverage is valuable, but a task frame, content pool, administered assembly, and inference population are different denominators. A handful of tasks per occupation does not make a representative sample of work. Pilots should test general principles without becoming accidental scope commitments.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [GDPval](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | A | Demonstrates large-scale expert-authored multimodal occupational task acquisition while exposing sampling, weighting, witness, and inference limitations |
| [$OneMillion-Bench](../papers/agent-benchmarks/2026-07-14-onemillion-professional-value-validity.md) | A | Adds an auditable equal-cell five-domain portfolio with localized positive/negative criteria, but its purposive outcome-conditioned assembly supports neither professional-work prevalence nor dollar value delivered |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Supplies realistic persona workspaces and file dependencies, while showing that availability, relevance, provenance, observed use, and causal use are distinct |
| [HippoCamp](../papers/agent-benchmarks/2026-07-11-hippocamp-personal-context-validity.md) | B | Separates composite contextual evidence and answer agreement from task-time authorization, causal adoption, consequential action, affected-party validation, and faithful personalization |
| [Workflow-GYM](../papers/agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md) | A | Contributes professional workflow/state realism and exposes the need to distinguish task validity, environment validity, and agent failure |
| [DeskCraft](../papers/agent-benchmarks/2026-07-14-deskcraft-interactive-workflow-validity.md) | B | Adds native professional-artifact checks and phased requirement delivery while separating authored interaction opportunity, trigger realization, authority, adoption, state-preserving repair, endpoint effect, burden, recipient uptake, and consequence |
| [WorkArena L1](../papers/agent-benchmarks/2026-07-12-workarena-l1-knowledge-work-validity.md) | B | Makes parameterized enterprise-UI setup, selected native-state predicates, and task-owned cleanup inspectable while separating atomic operation success from work sampling, collateral-state, professional-use, and readiness claims |
| [WorkArena++](../papers/agent-benchmarks/2026-07-11-workarena-plus-compositional-validity.md) | B | Makes executable setup/oracle/validator composition inspectable while showing that longer chains and lower success do not by themselves establish planning, workflow realism, or occupational coverage |
| [TheAgentCompany](../papers/agent-benchmarks/2026-07-11-theagentcompany-workplace-simulation-validity.md) | A | Separates integrated workplace substrate and selected workflow coherence from authority, consequence, sampling, collaboration, and labor-automation validity |
| [OdysseyBench](../papers/agent-benchmarks/2026-07-11-odysseybench-longitudinal-office-memory-validity.md) | B | Connects dialogue-distributed requirements to office-state action while exposing persistent-memory, evaluator-dispatch, collateral-state, and professional-validity gaps |
| [LongMedBench](../papers/agent-benchmarks/2026-07-14-longmedbench-longitudinal-clinical-validity.md) | B | Separates history volume and factual access from history necessity and consequence validity; its no-history result and retrospective next-event oracle show why a long record alone does not establish longitudinal decision competence |
| [SciAgentArena](../papers/agent-benchmarks/2026-07-14-sciagentarena-scientific-work-validity.md) | B | Adds matched step-wise versus dependent-pipeline scientific workflow evaluation and premise-validity tasks, while showing why mixed task units, configured-system bundles, propagated failures, fallbacks, and incomplete run/release evidence block real-world-science, novelty, autonomy, reliability, impact, or readiness claims |
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Demonstrates expert procedural skills, long-horizon artifacts, and observable boundaries without implying one domain should define the full benchmark |
| [Agents' Last Exam](../papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md) | A | Contributes broad executable workflow machinery while separating occupational frame, workflow universe, realized/versioned suite, and licensed inference population |
| [Design Report for Knowledge-Work Benchmarks](../papers/agent-benchmarks/2026-07-11-design-report-knowledge-work-benchmarks.md) | A | Adds a work-activity → tested-setting → persistent-product → licensed-claim reporting chain and makes omitted responsibilities and downstream handoffs explicit; its preliminary 18-label inventory is a revisable vocabulary, not validated coverage |
| [Handoff Debt](../papers/agent-benchmarks/2026-07-14-handoff-debt-successor-resumability.md) | A | Makes successor resumability a matched frozen-state/view experiment and separates endpoint quality from takeover effort, while exposing recipient dependence, outcome-aware cost, checkpoint clustering, continuation-label leakage, and lifecycle-cost limits |
| [Professional benchmark evolution matrix](concepts/professional-benchmark-evolution-matrix.md) | A | Compares AA-Briefcase/Lite, GDPval, $OneMillion-Bench, Workspace-Bench, MBABench, LH-Bench, Workflow-GYM, SaaS-Bench, and Agents' Last Exam as repairs to different links in one evidence chain; distinguishes implemented machinery from demonstrated validity |
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
task acquisition (GDPval/ALE), detailed localized text criteria ($OneMillion-Bench), source/check traceability (AA-Briefcase-Lite),
workspace and state substrates (Workspace-Bench/SaaS-Bench), native artifact
inspection (MBABench), and observable expert procedures (LH-Bench) more strongly
than it supports occupational representativeness, longitudinal project work,
counterfactual artifact integrity, checkpoint progress, or professional
readiness. The completed [OfficeBench audit](../papers/agent-benchmarks/2026-07-11-officebench-cross-application-office-validity.md)
supports typed cross-store state-transition and selected task-predicate claims, but
its synthetic tasks, app-count confounding, narrow evidence views, and mutable
environment do not establish professional-work validity. The completed WorkArena L1
audit supports enterprise-UI and selected native-state operation claims,
not representative knowledge work; WorkArena++ closes the composition-method gap but
not occupational validity.

$OneMillion-Bench adds a sharp **cost-to-value boundary**:
`versioned human task effort/cost → configured-system output distribution →
independent professional acceptance/correction → realized workflow use and
resource change → stakeholder benefit/loss`. Its current release supports the
first two links only. A 0.70 model-judge score and the sum of nominal senior-wage
costs attached to passing items do not establish saved cost, output, revenue,
profit, productivity, or value. Preserve task cost, score, acceptance probability,
review/correction cost, use, and consequence as separate observations; no scalar
score-to-dollar transform is admissible without downstream evidence.

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

Longitudinal claims need a further **volume → access → necessity → consequence**
ladder. Many prior records establish history volume; finding an old fact establishes
access; neither shows that the fact changes a justified later action. LongMedBench's
reported no-history aggregate matches or exceeds every memory condition, while its
released decision generator labels the next recorded EHR event or actual discharge
time. That is useful workflow-sequence evidence but not an independently authorized
appropriateness oracle. A longitudinal-decision task should hold immediate context
fixed while substituting correct, stale, irrelevant, contradictory, or absent prior
evidence; bind each atom's event/availability/valid time and transformation; admit
alternative valid actions or partial orders; and measure the downstream consequence
with trajectory-clustered denominators. Until then, classify evidence as long-input,
retrieval, archive reconstruction, or recorded-behavior prediction rather than
professional longitudinal competence.

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

Interrupted work adds a **frozen-state successor-resumability chain**:
`source work unit/predecessor trajectory → interruption rule and workspace hash →
visible handoff view and generation lineage → recipient configuration/evidence →
verification and continuation → endpoint/preservation consequence → outcome-aware
takeover effort → total lifecycle cost`. State fidelity, recipient sufficiency,
endpoint quality, continuation effort, and lifecycle cost are separate outcomes.
Freeze identical state across views; prohibit successor-visible labels derived from
hidden tests or evaluator-only state; test omissions, stale/false claims,
alternative futures, and preservation; and cluster inference at the source work
unit rather than treating several checkpoints from one trajectory as independent.
Point estimates and intervals must target the same estimand, and lower events or
tokens cannot all be named rediscovery when stopping and solved/failure mixtures
change.

[Handoff Debt](../papers/agent-benchmarks/2026-07-14-handoff-debt-successor-resumability.md)
provides bounded configured-system evidence that context-bearing views can reduce
takeover-side interaction on agent-to-agent coding resumptions, with smaller,
recipient-dependent endpoint effects. It does not release task IDs, checkpoints,
payloads, runs, or analysis; excludes note-generation cost; nests 181 handoffs in
75 issues; and leaves a possible official-state-label leak unresolved. Read it
with [AgentCo-op](../papers/agent-benchmarks/2026-07-11-agentcoop-typed-handoffs-localized-repair.md)
(typed transport is not semantic or receiver-use validity),
[DELEGATE-52](../papers/agent-benchmarks/2026-07-11-delegate52-delegated-artifact-integrity.md)
(requested delta and preservation are orthogonal),
[Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md)
(availability, access, and causal use differ), and
[ACON](../papers/agent-benchmarks/2026-07-13-acon-context-compression-validity.md)
(task-sufficient compression is not state-faithful). Existing handoff-usability,
workspace, transition, compression, trace, metric, task-health, and validity
machinery already hosts the requirements. The internal two-shape handoff producer,
consumer, adjudication, and counterfactual records establish only configured
synthetic content-dependence and scorer behavior—not human usability, professional
collaboration, cross-domain causal generalization, capability, safety, production
fitness, or readiness. No coding-specific or resumability subsystem follows.

External exams and certifications add an **instrument-transport chain**:
`source purpose/population → licensed forms → selection/transformation → configured
administration → score mapping → interpretation → decision threshold`. OfficeEval
provides dense native-artifact checks and externally authored weights, but its
selection, translation, coding interfaces, and aggregation create a new instrument.
The full NCRE pass mark is only a reference line, and community solutions are
positive witnesses rather than a human baseline. Dependent checks also need
prerequisite/cascade graphs so one missing object is not counted as many independent
capability deficits. Existing projection, artifact-view, task-health, metric, and
validity records are the durable homes; no office-specific schema follows.

Interactive families add a parallel boundary. Executable outcome checks are a
real repair over action-sequence imitation because they admit alternative paths,
but a passing selected predicate is not proof of complete, safe, or
professionally usable work. Live web improves ecological substrate while
weakening repeat equivalence; frozen APIs improve reproducibility by simplifying
the world; model-simulated users add interaction while becoming part of the
treatment. Every task therefore needs a projection ledger for native/simulated
substrate, authored initial state, observer coverage, omitted consequences,
simulator identity, reset health, and the claims that survive those choices.

DeskCraft sharpens this into an **interaction-evidence ladder**: `authored
opportunity → trigger realization → call/message → participant identity,
evidence view, and authority → answer → agent receipt → semantic adoption or
justified rejection → pre/post state preservation and repair → endpoint effect →
burden → recipient uptake → consequence`. No rung inherits the next. Type trigger
clocks as environment action, model turn, wall time, or authored schedule, apart
from semantic triggers such as inspected state, subtask boundary, decision point,
or risk. Before causal benefit or proactivity claims, compare matched full-
information, missing-information/no-channel, scripted-answer, simulator, and—only
where consented and justified—human conditions; retain simulator/environment
invalids, task/participant dependence, and agent/simulator/human costs.

The immutable v1 paper and later release support native endpoint machinery and an
authored phase protocol, not human collaboration: the paper-time public tree has
only a license, the inspectable 538-package snapshot is 30 days later, and no
trajectories or result corpus are released. Predominantly early fixed triggers,
task-conditioned ask affordances/prompts, stochastic simulator realization,
disjoint standard/interactive task sets, endpoint-only scoring, and absent burden
or recipient evidence block proactive-clarification, interaction-effect,
professional-validity, capability, safety, production-fitness, and readiness
claims. Existing participation/authority, trace, artifact-transition, task-health,
metric, and validity machinery is the durable home; no desktop-specific schema
follows.

## 3. Expertise transfer is an intervention that must be separated from the measuring instrument

**Central insight:** When an expert procedure or `SKILL.md` and a rubric come from the same model of expertise, better scores may reflect evaluator-cue compliance rather than genuine transfer. Skills, rubrics, graders, tools, scaffolds, and feedback policies require independent versions and ablations.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Directly motivates public-skill versus private-check boundaries and skill/rubric factorial comparisons |
| [SkillsBench](../papers/agent-benchmarks/2026-07-10-skillsbench-paired-skill-efficacy.md) | A | Sharpens matched skill/no-skill comparisons and the need for repeated paired trials and uncertainty |
| [AFTER](../papers/agent-benchmarks/2026-07-13-after-procedural-memory-transfer-validity.md) | A | Separates source-context gain, equivalent-form reuse, changed-context transport, and cross-model consumption while exposing complete-case selection, configured-system gaps, feedback/authoring overlap, and trace-diversity/volume confounding |
| [SLBench](../papers/agent-benchmarks/2026-07-13-slbench-skill-relation-validity.md) | B | Makes precondition, postcondition, constraint, conjunction, fallback, exception, override, and conflict relations executable, while exposing that LLM-co-designed extraction, case generation, and evidence contracts need independent projection and grader validation |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Shows why expert-written examples and criteria can improve judge agreement while also anchoring outputs |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Makes the harness and execution boundary explicit so a skill effect is not confused with launcher, tool, or isolation differences |
| [KWBench](../papers/agent-benchmarks/2026-07-11-kwbench-unprompted-problem-recognition.md) | A | Identifies situation framing before named-workflow execution, while showing that a cold final-artifact gate does not isolate recognition from inquiry, action, domain knowledge, or grading |
| [Ambig-DS](../papers/agent-benchmarks/2026-07-13-ambig-ds-task-framing-validity.md) | A | Supplies paired full/ambiguous/ideal-clarification interventions and exposes valid-looking artifacts built on unsupported target or objective commitments, while bounding the result to synthetic Kaggle-derived ambiguity and an ideal oracle |
| [Industrial expertise codification](../papers/agent-benchmarks/2026-07-11-industrial-expertise-codification-agent.md) | A | Demonstrates a bounded package effect while exposing representation semantics, authorship overlap, missing component ablations, and the need for held-out independent measurement |
| [UniClawBench](../papers/agent-benchmarks/2026-07-13-uniclawbench-proactive-closed-loop-validity.md) | A | Makes executor, private supervisor, public simulator, released signal, and repair cycle inspectable while showing that requested-task repair is not proactivity and structural isolation is not semantic non-leakage |
| [EdgeBench](../papers/agent-benchmarks/2026-07-13-edgebench-within-run-learning-validity.md) | A | Separates agent-visible feedback from evaluator-only snapshots and exposes adaptive-query, persistence, censoring, and best-so-far boundaries; its smooth suite fits are not task-level or universal learning laws |

**Repository consequence:** The benchmark bundle encodes configured-system identity and a no-skill/public-skill × independent/shared-rubric design rather than reporting an unqualified “skill lift.” Recognition is a different intervention axis: preserve situation-only, minimally framed, and fully specified conditions, positive and negative near neighbors, and separate observations for cue extraction, problem framing, targeted inquiry, action, and artifact consequence. A recognition frame names or narrows the problem; a procedural skill prescribes how to solve it; a rubric or evaluator cue reveals what will be rewarded. Their versions and effects must not be collapsed. The internal problem-recognition replay exercises this staged instrumentation and invalid-environment abstention on builder-authored synthetic cases only; it supplies no expert validity, agent result, treatment effect, prevalence, or cross-domain claim ([replay](../pilots/problem-recognition-intervention/replay-report.json)).

Framing interventions add a public-set boundary: `full public package + reviewed
admissible framings → immutable ambiguity edit → decision-relevant unresolved
variable → inspection or authority-dependent question → answer uptake → commitment
→ artifact/state consequence`. Preserve hashes for prompt, source pack, environment,
artifact contract, evaluator, and interaction policy; distinguish publicly
resolvable uncertainty from authority-dependent, unavailable, disputed, and
observer-insufficient states. Recognition, user-visible disclosure, question
information gain, authority routing, uptake, action, consequence, and interruption
burden are separate observations. Include unnecessary-ask and wrong-authority
neighbors; a private intended answer does not defeat another fair public framing.
Ambig-DS supports this paired diagnostic pattern on 51/61 filtered Kaggle-derived
target/objective suites, but its bundled synthetic edits, proprietary one-shot
systems, ideal truthful oracle, absent professional alternative validation, and
missing raw results/configurations/build evidence block natural-ambiguity,
stakeholder, professional-framing, escalation, capability, safety, and readiness
claims. Read it with UnderSpecBench: the latter's unavailable release and fixed
private oracle show why public authorization cannot inherit hidden intent. Existing
authority, participation, public-basis, artifact/state, task-health, metric, trace,
and validity contracts suffice; no ambiguity subsystem follows.

Procedural dependencies add a projection boundary inside the intervention. Preserve
source authority and clause spans; normalized triggers, modalities, scope, valid
time, completion, and governing priority; the typed relation and uncertainty; case
applicability and public basis; environment projection and accepted paths; observer
coverage and raw mixed/insufficient evidence; verdict policy; and consequence
severity as separate links. Test applicable/non-applicable, exception/override,
alternative-path, planted-violation, and observer-insufficient neighbors. A
schema-valid LLM-generated relation plus deterministic checker is one authored
witness, not evidence of extraction validity, grader completeness, general skill
reliability, field safety, or professional readiness. Existing procedural-skill,
task-projection, evidence-view, task-health, validity, trace, and root/surface
records already host this chain; no separate skill-logic subsystem follows.

Procedural adaptation adds a typed source-to-target edge rather than one
“evolution” score: source-context gain, equivalent-form cross-task reuse,
changed-context/role transport, and cross-model consumption have different
denominators and claims. Bind source and target task/form plus authoring/verifier
lineage, procedure versions, source and target solver/harness, trace and feedback
views, updater and candidate/promotion history, attempts, invalid/missing rows,
paired outcomes, clustered uncertainty, cost, forgetting, and negative transfer.
Define context shifts by changed artifact, audience, evidence authority,
threshold, tool, consequence, and obligations—not nominal role alone. Match trace
volume, task coverage, and success/failure composition before attributing gains
to model or task diversity.

AFTER supplies this high-leverage design vocabulary but weak effect evidence.
Its `M1`/`M2` tables conflict; 382 claimed tasks reduce to 129 released test
packages and 111 unexplained complete-case refinement IDs; its 73.1% cross-model
condition lacks target solver, task/Skill and trace denominators, updater,
attempts, failures, and uncertainty. Pooled traces confound diversity with volume
and coverage, while main configurations, traces, evolved procedures, promotion
history, and results are unreleased; oracle isolation is declarative and author
review does not establish expert or occupational authority. The source therefore
supports typed transfer-edge instrumentation, not expert transfer, professional
capability, production fitness, or readiness. Existing procedural-skill,
longitudinal, configured-system, firewall, task-health, metric, and validity
contracts suffice; no parallel schema follows.

Feedback adds another non-substitutable intervention boundary. Preserve the
role-separated chain from private observation through released signal and
feedback proposition to executor uptake and consequence; publish each channel's
authority, visibility, payload/cardinality, cadence, latency, query budget,
stochasticity, and leakage rationale. Cross no feedback, generic nudge,
public-visible critique, private-derived signal, and authorized ecological
feedback where the claim requires them. Report first attempt, current/endpoint,
fixed-cadence hidden, and best-so-far quality separately with new errors, cost,
run-at-risk counts, invalidity, and censoring. State persistence and reset are
independent treatments. UniClawBench supports role-separated synthetic repair but
not proactivity, natural-user fidelity, semantic non-leakage, or causal benefit;
EdgeBench supports dual-channel day-scale measurement and concrete evaluator-
hacking risks but not task-level/universal learning or professional readiness.
The frozen internal [24-cell report](../pilots/closed-loop-feedback-audit/report.json)
(SHA-256 `20deddde50fd93fc32b7af5b8f7eb69b9e9ffdab71c9cc3dd1ea421a41e335be`)
and [six-case adaptive report](../pilots/closed-loop-feedback-audit/adaptive-report.json)
(SHA-256 `0b9f068dfdc9d2b808caa761090415dab294b9eb15ed84dbca49d74f43a30339`)
validate only deterministic builder-authored fixture behavior—not expert or
participant evidence, general detection, capability, learning, causal benefit,
professional validity, production fitness, or readiness. Existing contracts
cover the boundary; no feedback-specific schema follows.

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
| [DORA](../papers/agent-benchmarks/2026-07-14-dora-disaster-response-consequence-validity.md) | A | Separates real-source and label truth, one executable analytical witness, endpoint agreement, professional acceptance, recipient uptake, action, and consequence; exposes uncalibrated geometry/numeric tolerances and absent operational evidence |

**Repository consequence:** Score families remain separate, artifact views have admissibility contracts, and task/trial records preserve both produced artifacts and consequential workspace state. Editable artifacts need native, executable/recalculated, rendered, and trace evidence plus authoritative mutation tests; inherited size and one reference witness do not establish work performed or maintainability. Scored state checks must also distinguish environment readiness from trial-created deltas and identify shared-cause or descendant dependencies. The internal initial-state replay rejects pre-satisfied, stale, copied-witness, and omitted-transition cases, accepts a declared alternative, and abstains on invalid initialization; its seven synthetic matches validate only fixture/scorer behavior ([replay](../pilots/task-initial-state-conformance/replay-report.json)).

DORA adds an **analysis-to-consequence ladder**: `source event/snapshot and valid
time → task requirement and authority → source/label truth → one analytical witness
under a configured tool/perception package → endpoint/artifact observation →
professional acceptance → recipient uptake → authorized attempted/realized action →
intended and collateral consequence`. No link inherits the next. Historical imagery
supports source realism, not automatically the validity of an authored operational
question, constant, objective, route, threshold, recommendation, or use. GT
substitution can stabilize one reference while removing uncertainty faced by the
evaluated or field system; a canonical path is one witness, not an alternative-
complete or safe policy.

Bind each requirement and threshold to source snapshot/valid time, qualified
authority, assumptions and transformations, intended recipient, protected
constraints, and reviewer disposition. Admit reviewed alternative paths/answers,
partial orders, abstention, and escalation. Calibrate scalar and geometry predicates
in physical or decision units against boundary cases and stakeholder loss rather
than convenience. Preserve artifact acceptance, recipient interpretation and uptake,
authorization, attempted versus realized state, collateral effects, and whether an
outcome is observed, simulated, or expert-projected. Cluster estimates by shared
event/task lineage and separate tool/data/perception/interface/task/grader surfaces
from supported roots.

The reviewed DORA v1 reports 515 tasks over 45 historical events and 108 typed tools,
but its model-backed canonical trajectory reaches only 80.48% agreement with the
GT-derived endpoint. Unnamed expert authority, one outcome-derived witness,
uncalibrated 20%/20-pixel/.5-IoU gates, no accepted alternatives, missing cited
Appendices C–H, and no verifiable task/tool/trajectory/result release limit it to an
offline analytical-package design claim. It supplies no operational-response,
safety, professional-validity, capability, production-fitness, or readiness evidence.
Existing authority, evidence-state, artifact, action-safety, trace, root/surface,
task-health, metric, and validity machinery already hosts the boundary; no disaster-
specific schema or pilot follows.

## 5. Graders and metrics are measured systems with their own failure modes

**Central insight:** Grader outputs are evidence, not ground truth. Every criterion needs an observable predicate, applicable evidence view, provenance, visibility boundary, dependence structure, and uncertainty. Aggregate metrics need explicit eligible populations, missingness policy, clustering, and claim boundaries.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Anthropic agent evaluation lifecycle](concepts/anthropic-agent-evaluation-lifecycle.md) | A | Provides a production vocabulary of tasks, trials, graders, transcripts, and multi-grader evaluation patterns |
| [AgentRewardBench](../papers/agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md) | B | Exposes judge reliability, evidence-view, trajectory, annotation, and observer-access issues |
| [Signals trajectory triage](../papers/agent-benchmarks/2026-07-14-signals-trajectory-triage-sampling-validity.md) | B | Separates probability-sentinel monitoring from enriched case discovery and makes the trajectory-population → inclusion policy → review → adjudication → intervention boundary explicit; its unreleased pool and selection ledger support queue-yield evidence, not prevalence or production utility |
| [Measuring Agents in Production](../papers/agent-benchmarks/2026-07-14-measuring-agents-production-practitioner-evidence.md) | B | Supplies a transparent practitioner instrument and selected reports of bounded workflows, human gates, sensitive context, delayed outcomes, and mixed evaluators; outcome-conditioned recruitment, optional-question denominators, unknown respondent/organization dependence, and no system audit make this portfolio evidence, not representative prevalence or practice efficacy |
| [Agentic Confidence Calibration](../papers/agent-benchmarks/2026-07-14-agentic-confidence-calibration-validity.md) | B | Separates predicted success for one configured trajectory from repeated reliability and causal diagnosis; its unreleased labels/configurations, post-outcome features, clustering omissions, asymmetric transfer, and logprob dependence block decision-utility or universal-calibration claims |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Contributes inspectable criterion authoring while revealing compensatory mandatory criteria and missing applicability/dependence controls |
| [BigFinanceBench](../papers/agent-benchmarks/2026-07-14-bigfinancebench-workflow-derivation-validity.md) | A/B | Makes source-to-calculation checkpoints and repeated visible trajectories inspectable on the public subset, while showing that narrated exact values, lossy judge views, dependent criteria, and held-back headline evidence do not establish an audited workflow |
| [GroundEval](../papers/agent-benchmarks/2026-07-14-groundeval-evidence-path-validity.md) | B | Makes actor/time gates, configured evidence paths, and bounded negative-search obligations deterministic, while showing that repeatable code does not establish contract authority/completeness, causal effects, global absence, or observer superiority |
| [JADE](../papers/agent-benchmarks/2026-07-11-jade-dynamic-professional-grading.md) | B | Separates invariant requirements from response-created claims/consequences, while exposing variable denominators, shared-cue judging, verifier fail-open behavior, and unvalidated score fusion |
| [Adversarial verifier hardening](../papers/agent-benchmarks/2026-07-14-adversarial-verifier-hardening-validity.md) | A/B | Makes iterative false-accept search, patch provenance, and fixed held-out attack replay inspectable, while directly showing that a narrow solver witness can yield 0% attack success together with near-total legitimate-solution rejection |
| [AsymmetryZero](../papers/agent-benchmarks/2026-07-14-asymmetryzero-semantic-eval-contracts.md) | B | Makes criterion, grader mode, panel vote, weight, threshold, cost, and adapter realization inspectable; its private available-case study shows why cross-model dissent, repeated-call instability, criterion correctness, task-decision agreement, and use/decision loss must remain separate |
| [SaaS-Bench](../papers/agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md) | A | Release audit shows that a checkpoint becomes partial-progress evidence only when it was not pre-satisfied, is attributable to the run, has declared necessity/sufficiency, and does not double-count one upstream event through dependent consequences |
| [Efficient Benchmarking of AI Agents](../papers/agent-benchmarks/2026-07-09-efficient-benchmarking-ai-agents.md) | B | Shows that reduced panels may preserve rank while degrading absolute-score interpretation |
| [Agent Psychometrics](../papers/agent-benchmarks/2026-07-09-agent-psychometrics.md) | B | Treats difficulty as a property of the configured task/system package and motivates response matrices and scaffold-aware reporting |
| [Expert evaluation and limits of human feedback](../papers/agent-benchmarks/2026-07-11-expert-disagreement-human-feedback-validity.md) | A | Shows in one small clinical panel that shared rubrics can yield stable directional disagreement; motivates framework-indexed observations and policy-explicit aggregation without universalizing the domain result |
| [Many-facet human/AI rater effects](../papers/agent-benchmarks/2026-07-11-many-facet-human-ai-rater-effects.md) | B | Separates agreement, panel-relative severity, model fit, repeat stability, and decision validity; shows why a linked calibration design does not make graders interchangeable |
| [Rubric-modification interventions](../papers/agent-benchmarks/2026-07-11-rubric-modification-human-autorater-agreement.md) | B | Makes examples, context, criterion-call topology, score transformation, and aggregation part of instrument identity; agreement gains can coexist with shared cueing or construct change |
| [AI Agent Reliability](../papers/agent-benchmarks/2026-07-11-agent-reliability-profile.md) | B | Separates accuracy from repeatability, perturbation sensitivity, confidence quality, and violation consequences while binding each estimate to a configured operational profile |
| [Stochastic Agent Evaluations](../papers/agent-benchmarks/2026-07-14-stochastic-agent-evaluations-icc-validity.md) | B | Makes task-level repeats and released response matrices inspectable while showing that the published variance-of-task-means ratio is not ICC(1,1), omitted invalids change the estimand, and repeat budgets are decision- and population-specific |
| [LiveBench](../papers/agent-benchmarks/2026-07-11-livebench-contamination-limited-lifecycle.md) | B | Makes benchmark renewal operational through rotating recent-source forms, temporary private roles, deterministic checks, and reruns, while exposing equivalent-form, outcome-conditioned selection, exposure, and grader-drift limits |
| [WorkBench Revisited](../papers/agent-benchmarks/2026-07-12-workbench-revisited-longitudinal-lifecycle.md) | B | Shows why repaired current measurement and longitudinal continuity need linked forms and task-level score bridges rather than one homogeneous time series |
| [Reasoning/coding benchmark evolution](concepts/reasoning-coding-benchmark-evolution.md) | B | Compares MMLU→MMLU-Pro and HumanEval→LiveCodeBench from full papers and pinned current releases; separates common-interface adoption, demonstrated headroom/prompt stability, executable equivalence, and timestamped renewal from unsupported work-validity and contamination-free claims |
| [BrowserGym](../papers/agent-benchmarks/2026-07-11-browsergym-ecosystem-measurement.md) | B | Separates useful runner/interface interoperability from unsupported evaluator, score, reset, or construct equivalence across adapted benchmark families |

**Repository consequence:** Criterion/check contracts, metric-monitoring contracts, validity arguments, response matrices, and separate ranking versus absolute-capability claims. Grader identity includes rubric/examples, evidence view, criterion execution topology, score transformation, aggregation/tie policy, and configured rater. Agreement, panel-relative severity, fit, repeated-call stability, construct preservation, decision loss, cost, and audit burden remain separate outcomes; adjusted scores never overwrite raw observations or become adjudicated truth. Reliability is a conditional profile—not a system trait—indexed by configured system, task/form population, environment, time, intervention/exposure distribution, and consequence model. Accuracy, repeatability (including consistently wrong behavior), resource variation, perturbation effects, confidence quality, violation frequency, severity, remediation, and loss remain separate. Every perturbation needs independently supported preservation and exposure claims; wrapper recovery cannot count as agent recovery; confidence is licensed only for the decision time and evidence view at which it was elicited. Plural judgments remain immutable observations; aggregation is a versioned stakeholder/error-loss policy rather than discovered ground truth. Specification error, evidence gaps, rater instability, framework-conditioned disagreement, policy selection with dissent, and unresolved value conflict require distinct dispositions. Derivation criteria must also be proof-carrying: source identity and passage, extracted claim, typed operation, dependencies, conclusion, exact observer view, and licensed claim remain distinct. Mentioning an expected value cannot inherit provenance or causal-use credit; one upstream defect and its descendants must not be counted as independent failures. The completed synthetic plural-judgment conformance slice exercises this boundary but supplies no prevalence, professional-consensus, or readiness evidence. Before the second pilot is interpreted, its adversarial audit should plant a pre-satisfied requirement, an unrelated record sharing the expected scalar, a title-only empty artifact, and one upstream defect with several descendant checks; readiness or duplicated consequences must not inflate progress.

Repeated evaluation adds a **decision-keyed estimand hierarchy**, not one
“reliability” scalar: `intended attempt ledger → service availability → execution-
valid trial → grader-valid observation → within-form outcome and severe-failure
recurrence → task/form/family heterogeneity → paired configured-system or
intervention contrast → threshold, cost/loss, and operating decision`. Preserve
the intended, service-valid, trial-valid, grader-valid, and substantively
successful denominators separately. An unconditional operational estimand may
predeclare service failures as zero; a conditional capability estimand may not
silently omit them. Repeat fixed outputs through the grader, or otherwise cross
output and observer repeats, before attributing within-form label variation to
the agent.

The full [Stochastic Agent Evaluations review](../papers/agent-benchmarks/2026-07-14-stochastic-agent-evaluations-icc-validity.md)
recomputes released matrices and shows that the paper/release uses variance of
finite-repeat task means divided by that variance plus pooled within-task
variance. Because it does not remove the within-task sampling contribution from
the numerator, this is **not ICC(1,1)**; its low-repeat “convergence” partly
reflects the estimator itself. Even a correctly specified ICC is conditional on
the benchmark task mixture and induced binary success probabilities—not an
agent-intrinsic consistency trait. Cluster and retain task, form, family,
configured-system, provider/time/batch, and grader identities; test unequal-
repeat and binary-model assumptions, all-success/failure boundaries, easy/hard-
anchor composition, and operational-versus-valid-only missingness policies.
The reported `8–16` and `≥32` counts are descriptive waypoints for selected
GAIA/FRAMES matrices and do not transfer. Freeze repeat budgets against the
actual decision—mean precision, per-form recurrence, severe-failure detection,
paired effect, rank stability, temporal drift, or variance-component precision—
with minimum/maximum attempts, stopping statistic, error/loss target, missing-
event behavior, and held-out validation. Existing response-matrix, reliability,
task-health, metric, configured-system, grader, and validity records suffice; no
new schema or QA/retrieval scope commitment follows, and repeated internal
synthetic trials alone license no professional-validity, production-reliability,
safety, fitness, or readiness claim.

AsymmetryZero adds a specific **jury-substitution ladder**: raw evidence view →
individual observation → criterion decision → task decision/rank → downstream
decision loss. Similar weighted totals can result from cancellation, compensation,
threshold insensitivity, or deterministic-criterion dilution; they do not imply
criterion equivalence. A `5:0`/`4:1`/`3:2` split among different models measures
cross-model heterogeneity, not repeated-call stability. Expert authority and
criterion validity also precede jury execution rather than emerging from majority
agreement. The paper-time framework release is useful plumbing but its private
study corpus is absent, its `ExactMatch` is normalized substring inclusion, and
semantic judges see final text rather than referenced files or traces. Existing
criterion, evidence-view, adapter, task-health, metric, and validity records are
the correct homes; no new schema follows.

Trajectory review adds a prior **selection episode** before grader observation:
`eligible population snapshot → detector and inclusion mechanism → reviewed
evidence view → plural labels and adjudication → supported defect → accepted
intervention → replay/field effect → downstream utility`. Freeze task,
configured-system, harness, time, retry/duplicate, and lineage clusters in the
population record; version detector rules, scores, thresholds, quota/tie policy,
seed, inclusion probability, overlap, nonresponse, and invalid handling. Preserve
the intended downstream use and licensed/prohibited claims. A frozen probability-
sentinel stream can support prevalence, drift, subgroup, and false-negative
estimation; an enriched stream can increase discoveries per review budget. Do not
pool or compare systems from the latter without known support and design weights.
`signal activation`, `review-worthy`, `supported defect`, `accepted fix`,
`replay/field effect`, and `utility` are non-substitutable states.

[Signals](../papers/agent-benchmarks/2026-07-14-signals-trajectory-triage-sampling-validity.md)
reports 82/100 majority-positive signal-selected slots versus 54/100 random slots
in one undisclosed historical τ-bench pool. Missing pool identity, detector/score
policy, overlap, inclusion probabilities, review-time costs, label records, and
task/configuration-clustered inference bound this to case-finding yield under one
annotation target. Its post-v1 Plano implementation is later engineering evidence,
not the empirical release, and materially diverges by emitting quality scores that
also penalize environment exhaustion despite the paper's descriptive/use warning.
Read this with AgentRewardBench for observation validity, AgentLens and the Amazon/
Anthropic lifecycle guidance for diagnosis and task-health routing, Nubank for the
still-unmeasured offline→online outcome bridge, and many-facet evidence for rater
effects. Existing trace, grader, task-health, metric-monitoring, configured-system,
and validity records suffice; no trajectory-only subsystem follows. No prevalence,
comparative-system, causal, professional-validity, capability, safety, production-
fitness, or readiness claim is licensed.

Production-practice reports and trajectory confidence occupy different rungs of
one **practice-to-decision chain**: `selected report and denominator → observed
configured realization → repeated outcome distribution → trial-specific prediction
at a declared evidence time → supported causal diagnosis (separate) → frozen
threshold/action under capacity and loss → review/escalation burden → realized
stakeholder loss`. MAP observes selected self-reports and parts of the human-review
context, not realized configurations or outcomes. Agentic Confidence Calibration
reports post-hoc prediction of one binary label from completed token-confidence
traces, not repeats, causes, or action utility. Neither rung inherits the next.
Preserve reporting unit, stage/version, optional-question denominator, missingness,
and respondent/organization clustering for practice evidence; preserve task/system/
provider/time clusters, label authority, prediction time, feature and logprob
semantics, missingness, transport population, and frozen action policy for confidence
evidence. Use the existing trace, review-selection, reliability, metric, task-health,
and validity machinery; do not turn common reported practice into a rubric or a
calibrated probability into correctness, safety, readiness, or root cause. See the
full [MAP](../papers/agent-benchmarks/2026-07-14-measuring-agents-production-practitioner-evidence.md)
and [confidence](../papers/agent-benchmarks/2026-07-14-agentic-confidence-calibration-validity.md)
reviews for source-specific limits.

Adversarial grader revision needs three independently versioned populations:
counterexamples used to search and patch, legitimate alternatives used to constrain
false rejection, and held-out challenges used after freezing the revision. Report
old/new acceptance matrices, adaptive as well as fixed-corpus attacks, threshold
authority, shared-patch lineage, clustered uncertainty, and negative-effect rates.
Terminal Wrench supplies a large inspectable false-accept corpus, but its 331-task
release versus the later paper's unreconciled 323 count, outcome-conditioned
discovery, limited label audit, and model/prompt/budget dependence prevent a stable
prevalence claim. The KernelBench case directly demonstrates that 0% known-attack
success can coexist with 0% benign pass before post-loop repair. Therefore
`known_exploit_rejected` is task-health regression evidence, not verifier
soundness/completeness, safety, professional validity, or readiness.

Deterministic evidence-path scoring adds a prior contract-validity gate. Preserve
`request → result exposure → content access → model visibility → citation/adoption
→ action → effect`; a blocked request is not a leak, harm, or causal-use result.
Negative claims must be bounded as “not found within U under Q at T,” with universe
authority, source/index coverage, snapshot, query operators, pagination/truncation,
access failures, completeness evidence, and residual uncertainty. Event joins and
shared IDs remain configured dependencies unless intervention or a warranted causal
model supports promotion. Known artifact sets are witness paths, not necessarily
complete paths; admit independently reviewed alternatives and return insufficiency
when the observer or search universe cannot support a verdict.

GroundEval's full v2/release audit supports deterministic behavior for selected
actor/time, configured-artifact, and search-coverage mechanics. It does not validate
the authored contracts or its judge comparison: prose-only judges lacked the private
contract/state supplied to the deterministic scorer. The release also omits the
paper's empirical corpus, questions, trajectories, judge records, and results; Table
6 matches release code rather than published Equation 1, and release aggregation
retains only one of the three stated violation types. Therefore compare deterministic,
model, and human observers predicate by predicate under equal decisive evidence
views. Existing provenance-observation, alternative-path, trace, task-health,
metric, and validity machinery should carry this boundary; no GroundEval-specific
grader or schema is justified.

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

Benchmark maintenance needs three linked products: a frozen **anchor form** for
trend continuity, a corrected **operational form** for fair current measurement,
and a private/recent **renewal form** for exposure and ceiling control. Transitions
need changed-locus identity and old-pass/new-pass matrices from rescored frozen
outputs where possible; only stable or bridged subsets license trends. WorkBench
Revisited preserves valuable v1/v2 routing, but task, ground truth, evaluator, tool
contract, harness, provider, and exposure all changed, so its headline delta is not
a model-capability estimand. Side effects also need opportunity, conditional-on-
failure, severity, reversibility, and affected-party denominators. Exercise existing
task-health, longitudinal, reliability, metric, and validity machinery on a real
revision before adding another lifecycle schema.

## 6. Failures should generate causal diagnostic evidence

**Central insight:** A benchmark should distinguish the surface where failure appeared from the earliest supported cause. Raw traces, failed checks, event locators, recovery chains, attribution confidence, and task/grader/environment validity must remain inspectable.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [STRACE](../papers/agent-benchmarks/2026-07-09-strace.md) | B | Introduces dependency-aware causal slicing and the distinction between surface failure and upstream root cause |
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Adds error → verifier feedback → repair → verification as a measurable recovery chain |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Prevents launcher, permission, tool, and sandbox faults from being mislabeled as capability failures |
| [Amazon production-agent evaluation](concepts/amazon-production-agent-evaluation.md) | B | Adds production-oriented decomposition of tool, memory, reasoning, and end-to-end operational failures |
| [AARRI-Bench](../papers/agent-benchmarks/2026-07-11-aarri-research-judgment-lifecycle.md) | A | Makes stop, refuse, escalate, clarify, and preserve legitimate consequence-bearing outcomes while directly exposing lexical-verifier false rejection |
| [UnderSpecBench](../papers/agent-benchmarks/2026-07-13-underspecbench-action-boundary-validity.md) | B | Separates private intended transition from public authorization, resolvable uncertainty, attempted action, realized effect, and observer coverage |
| [MemoryArena](../papers/agent-benchmarks/2026-07-13-memoryarena-interdependent-experience-action.md) | B | Makes prior-session evidence consequential through dependency-bearing action while exposing feedback, state-reconstruction, retrieval, adoption, and grader confounds |

**Repository consequence:** Root/surface attribution, causal trace slices, recovery records, invalid-trial handling, and task-health lifecycle records. Apparent requests should also admit a counterfactual action contract: observable disqualifying evidence, authority and threshold, legitimate alternatives, required state and communication consequences, abstention/escalation, and collateral harm. Decision, rationale, artifact preservation, communication, cost, and harm remain separate observations. Matched persist/stop and comply/dissent forms are required to distinguish calibrated judgment from generic quitting or contrarianism; substantive action must be tested independently of lexical realization, with paraphrase contrasts and retained semantic adjudication. AARRI's inspectable authored suite motivates this design but its missing sampling frame, contributor accounting, human baseline/agreement, repeats/uncertainty, verifier-wide audit, complete configuration, contamination-safe split, environment evidence, and paper-pinned release prevent researcher-quality or cross-domain capability claims.

The combined evidence adds two non-substitutable boundaries. First, private intent,
public authorization, resolvable uncertainty, legitimate terminal action, attempted
action, realized consequence, and observer sufficiency must remain separate;
clarification, refusal, escalation, and action are calibrated alternatives rather
than an ordinal completion scale. UnderSpecBench contributes a controlled synthetic
pattern but its fixed oracle may become unfair as visible authorization changes.
Second, prior-session relevance does not identify memory causality: preserve
observation → write/feedback → retrieval/presentation → adoption → state
reconstruction → action → consequence, with reset, raw, answer-feedback, oracle,
irrelevant, and corrupted-evidence controls. MemoryArena contributes the
dependency-bearing action shape, while its heterogeneous feedback and graders block
root-cause memory, professional, learning, or readiness claims. Existing contracts
cover both boundaries; the queued cross-domain authority-to-consequence slice is the
appropriate executable follow-up, not a DevOps- or memory-specific schema.

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
| [SafePro](../papers/agent-benchmarks/2026-07-14-safepro-professional-action-safety-validity.md) | B | Adds long file-bearing harmful professional-style tasks while showing that a judge which omits tool arguments, observations, and artifacts and maps non-completion to safety cannot support action, consequence, utility, or professional-safety claims |
| [Context-to-Execution Integrity](../papers/agent-benchmarks/2026-07-14-context-to-execution-integrity-action-authority.md) | B | Separates protected-field selection, sink-interpreted exact-effect, and invocation-event authority and binds all three to one manifest; zero observed mediated-gate escapes remains conditional on policy, validators, provenance, complete mediation, and observer coverage |
| [Search-time contamination](../papers/agent-benchmarks/2026-07-10-search-time-contamination.md) | C | Shows why search exposure, exact source overlap, and post-release role changes must be recorded rather than treated as a universal causal inflation estimate |
| [LiveBench](../papers/agent-benchmarks/2026-07-11-livebench-contamination-limited-lifecycle.md) | B | Shows that recent sources and rolling private forms limit some direct exposure but do not prove contamination absence; source, exposure, instrument, and configured-system clocks must remain separate |
| [Agents' Last Exam](../papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md) | A | Its post-paper split drift shows that a tier label is not suite identity; membership, outcome-selection, exposure, role transition, replacement bridge, and retirement must be versioned |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Makes protected state, unauthorized mutation, and cleanup part of workspace validity |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Contributes execution isolation and side-effect boundaries |

**Repository consequence:** Private-evidence firewalls, role transitions, safety/compliance checks, workspace mutation authorization, and environment-isolation tests. Rolling forms require four independent clocks—source availability, exposure/visibility, instrument version, and configured-system execution. Difficulty-conditioned replacement keeps challenge alive but changes the administered population; without frozen anchors or equivalent-form bridges, rank stability cannot license absolute capability trends. Grader repair creates linked new observations rather than rewriting historical scores. Safety observers must bind each verdict to decisive tool arguments, observations, native artifact/state views, and recipient effects; when those views are absent they must return insufficient evidence rather than convert non-completion, incapability, timeout, or empty output into safety. Keep justified refusal/escalation, safe alternative completion, over-refusal, invalid execution, unsafe attempt, policy interception, realized harm, recovery, and benign utility separate. At the proposal-to-execution boundary, preserve field-local authority, exact sink-interpreted effect authority, invocation capability, and their common manifest binding; gate acceptance proves neither validator correctness nor professional task quality, while zero observed gate escapes proves neither bypass closure nor universal safety. SafePro's paper-time release has useful authored task packages, but its 276 public rows do not match the 275-row paper suite, 208 reference files are unbundled/mutable, and no run corpus supports its configured-system rates or mitigations. The inert action-safety slice now separates placement, exposure, adoption, attempted and mock-realized action, recovery, residual harm, invalidity, and benign utility across eight synthetic cases with a passing static preflight. This is executable contract evidence only—not a live containment test, agent-capability result, expert validation, or real-world safety evidence.

## 9. Expert scarcity and participation are design problems, not assumptions

**Central insight:** Expert labor should be concentrated at authority-bearing boundaries: elicitation, disagreement, transformation review, calibration, and release approval. The project must measure actual participation cost and fidelity rather than relying on unsupported market estimates.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Domain-expert participation ethnography](../papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md) | A | Provides concrete governance lessons around purpose, reciprocity, authority, transformation, and consent, albeit from one compensated collaboration |
| [Benchmark Ceiling](../papers/agent-benchmarks/2026-07-10-benchmark-ceiling-expert-labor-scarcity.md) | C | Raises renewal and expert-scarcity questions but does not provide auditable evidence for its headline cost/labor claims |
| [GDPval](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | A | Demonstrates expert task acquisition at scale while leaving important representativeness and expert-ceiling questions unresolved |
| [Consulting cognitive traps](../papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md) | A | Shows the potential value of SME-authored critical incidents while its missing released task/grader artifacts limit reuse evidence |
| [SimInstruct](../papers/agent-benchmarks/2026-07-11-siminstruct-simulated-novice-elicitation.md) | B | Demonstrates paid asynchronous role-play feasibility in one network while leaving recruitment denominators, actual burden, privacy/consent lineage, tacit-knowledge yield, and downstream utility unmeasured |
| [HAS-Bench](../papers/agent-benchmarks/2026-07-13-hasbench-configurable-human-participation-validity.md) | B | Makes participant roles, authority, channels, and event-conditioned process measures explicit while showing that model-simulated assistance is not evidence about real-human participation or burden |

**Repository consequence:** Expert-participation contracts, contributor provenance/authority, measured recruitment and review burden, reciprocal outputs, and continued research into near-zero-cost incentives. Benchmark participants must additionally be typed by realization (`real_human`, model simulator, scripted policy, hybrid, or replay), independently of their assigned social role. Participation is a configured treatment vector—prompt, visible participants, channels/tools, information access, action authority, initiative, control threshold, budget, and observer—not an ordinal “agency level.” Preserve the chain `availability → exercise → uptake → effect`; a graph edge, trace event, apparent adoption, and matched outcome effect license different claims. Simulator steps/tokens do not estimate human active time, waiting, interruption, cognitive demand, correction work, privacy exposure, or accountability. HAS-Bench's 397 reported adaptations and scenario-review study support this vocabulary, but its model-backed users, bundled A1/A3/A4 treatments, single rollout per task, unreported process-judge audit, and unverifiable release block human-participation, simulator-parity, professional-collaboration, burden, and readiness claims.

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
