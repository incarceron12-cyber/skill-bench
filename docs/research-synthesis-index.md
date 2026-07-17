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
| [PaperBench](../papers/agent-benchmarks/2026-07-15-paperbench-replication-rubric-validity.md) | A | Makes author-assisted long-horizon decomposition and executable artifact evidence inspectable while showing that dense hierarchical local credit is not a validated completion claim |
| [Consulting cognitive traps](../papers/agent-benchmarks/2026-07-10-consulting-cognitive-traps.md) | A | Shows how naive paths, expert-visible cues, operations, consequences, and checks can form testable critical incidents across domains |
| [Data Therapist](../papers/agent-benchmarks/2026-07-11-data-therapist-tacit-knowledge-elicitation.md) | A | Makes the elicitation instrument and its path-dependent selection effects visible; separates annotation yield from corroboration, scope, transformation fidelity, and benchmark utility |
| [YIELD](../papers/agent-benchmarks/2026-07-17-yield-information-elicitation-validity.md) | A | Separates historical next-question style fit from model-caused respondent evidence, objective-relevant claim update, legitimate consequence, and claim-based stopping; its release audit bounds evidence to configured fixed-context adaptation |
| [Organizational tacit-knowledge simulation](../papers/agent-benchmarks/2026-07-17-organizational-tacit-knowledge-simulation-validity.md) | A | Makes planted claim routing and complete traces inspectable while separating possession, referral awareness, topology, exercised contact, authority, semantic preservation, and artifact consequence; it does not validate tacit expertise or organizations |
| [SimInstruct](../papers/agent-benchmarks/2026-07-11-siminstruct-simulated-novice-elicitation.md) | B | Treats simulated interlocutor behavior as an elicitation treatment; motivates productive-friction probes, phase labels, correction lineage, and separate participation-versus-utility outcomes |
| [EnterpriseClawBench](../papers/agent-benchmarks/2026-07-11-enterpriseclawbench-session-derived-validity.md) | A | Separates observed workplace demand from the rewritten counterfactual task; requires projection deltas, hindsight controls, equivalence review, and a claim licensed to the evidence actually preserved |
| [AlphaEval](../papers/agent-benchmarks/2026-07-11-alphaeval-production-grounded-validity.md) | A | Separates current company-demand provenance from requirement projection, grader validity, configured-package comparison, occupational inference, and economic value |
| [$OneMillion-Bench](../papers/agent-benchmarks/2026-07-14-onemillion-professional-value-validity.md) | A | Releases 400 detailed bilingual research tasks and 6,758 criteria while showing why human task cost, rubric score, thresholded acceptance, workflow savings, and realized economic value must remain separate records |
| [Industrial expertise codification](../papers/agent-benchmarks/2026-07-11-industrial-expertise-codification-agent.md) | A | Types codified knowledge by execution semantics and bounds a co-designed package effect away from tacit transfer, expert equivalence, and cross-domain generalization |
| [JobBench](../papers/agent-benchmarks/2026-07-12-jobbench-delegation-desire-validity.md) | A | Makes worker-reported delegation preference a typed portfolio-selection signal while separating it from package fidelity, present consent, workflow uptake, and worker outcomes |
| [Benchmark-to-risk expert elicitation](../papers/agent-benchmarks/2026-07-12-benchmark-to-risk-expert-elicitation.md) | A | Makes the score-to-consequence warrant observable as structured disagreement and separates capability interpretation, scenario use, workflow effect, outcome composition, and decision loss |
| [OfficeEval](../papers/agent-benchmarks/2026-07-12-officeeval-standardized-exam-validity.md) | B | Separates external requirement/weight lineage from the validity of a transformed subset, administration, aggregate, or transported decision threshold |
| [Laboratory workflow twins](../papers/agent-benchmarks/2026-07-13-laboratory-workflow-expert-elicitation.md) | A | Adds claim-level authority gates, mandatory nulls, exact evidence→claim→projection lineage, and masking-channel diagnosis while separating graph executability from knowledge truth or operational validity |
| [Context-Mediated Domain Adaptation](../papers/agent-benchmarks/2026-07-16-context-mediated-domain-adaptation-edit-validity.md) | A | Makes before/after artifact edits a provenance-rich elicitation channel while separating observed delta, model interpretation, contributor acceptance, promotion, delivery, adoption, downstream effect, and transfer |
| [SovereignPA-Bench](../papers/agent-benchmarks/2026-07-13-sovereignpa-consent-mediation-validity.md) | B | Separates current intent, memory, third-party pressure, evidence, consent, and burden while exposing that a hidden author oracle and rubric-matched scaffold do not establish user authority, realized action, or benefit |
| [MapSatisfyBench](../papers/agent-benchmarks/2026-07-15-mapsatisfybench-behavior-grounded-hidden-requirements.md) | A | Retains a valuable future-behavior→candidate-factor→pre-response-evidence firewall while showing that hindsight selection, historical prediction, current applicability, authority/consent, causal consequence, and affected-party acceptance are different warrants |
| [SOP-Bench](../papers/agent-benchmarks/2026-07-14-sop-bench-procedure-task-validity.md) | A | Makes the procedure→schema→row→tool→oracle→parser chain executable, while showing that asserted expert validation and endpoint agreement do not establish procedure fidelity without item-level lineage, conformance contracts, leakage controls, typed comparators, and independent oracle derivation |
| [c-CRAB](../papers/agent-benchmarks/2026-07-17-c-crab-review-test-projection-validity.md) | A | Makes a real human-feedback→fail/pass-test→repair-agent consequence chain unusually inspectable while showing that outcome-informed projection, selection on the evaluation mediator, missing finding-to-action attribution, and unscored false positives bound the result to a configured selected chain rather than review quality generally |

**Repository consequence:** [`schemas/expertise-transfer.schema.json`](../schemas/expertise-transfer.schema.json), [`schemas/EXPERTISE_TRANSFER.md`](../schemas/EXPERTISE_TRANSFER.md), validity arguments, participation contracts, and the authoring lifecycle in the canonical taxonomy. Mixed-initiative or simulated-interlocutor elicitation must preserve an unprompted-before-probed boundary and event lineage for offered, displayed, answered, rejected, revised, withdrawn, skipped, and stopped interactions; requested versus realized resistance and the triggering utterance must remain visible. Dialogue/word volume and conversational fluency are not expertise yield: measure grounded thresholds, contradictions, failure signatures, correction burden, contributor value/privacy, and downstream task/check utility separately. Machine responsiveness checks do not confer epistemic or expert authority. Source-derived tasks are versioned projections: observed demand and resolution, omitted context, transformations, hindsight sources, target counterfactual, equivalence disposition, and licensed use remain distinct. Real provenance can support demand-inspired coverage while replay fidelity remains unsupported.

Objective-grounded elicitation adds a narrower **question-to-consequence chain**:
`question opportunity/form → caused respondent observation or refusal → supported
claim adoption/revision → objective progress → artifact/check uptake or legitimate
consequence`. The objective is itself versioned evidence: beneficiary, decision/use,
required and optional claims, authority, permissible/prohibited questions,
constraints, stop/escalation, burden budget, and loss. Track `confirmed`,
`contradicted`, `unknown`, `inaccessible`, `unauthorized`, `out_of_scope`, and
`escalated` claim states; report premature and unsupported closure separately from
excess-contact/disclosure/time/cost burden.

Network search requires distinct possession, referral-belief, formal-relation,
informal-relation, agent-observed-topology, exercised-route, disclosure-authority/
willingness, semantic-preservation, and downstream-use records. YIELD measures
mostly historical question-distribution fit: generated turns receive no respondent
answer, entity count/progression/length are weak objective proxies, overlapping
windows and speaker/source reuse weaken inference, and unseeded/defective release
paths plus unresolved rights and consent constrain reuse. The organizational study
measures same-family synthetic planted-identifier routing: incomplete seeds,
graph/referral and start-policy mismatches, only three stochastic repetitions per
factorial cell, pooled configuration/topic dependence, weak identifier/model-judge
proxies, and absent metric code block mechanism claims.
Both are useful cross-domain conformance evidence, but neither licenses tacit-
expertise, causal policy-benefit, ecological, professional-validity, or readiness
claims, and neither unblocks the consented real-session gate. Existing evidence,
trace, participation, metric, task-health, and validity machinery suffices; no
elicitation- or organization-specific schema follows.

Executable consequence projection adds another required boundary: if a candidate artifact is scored only after a second agent acts on it, preserve candidate→mediator uptake→action→check attribution, a no-candidate control, mediator identity/sensitivity, and source/projectable/mediator-valid/scored denominators. Endpoint success is otherwise a configured mediation-package observation, not direct candidate correctness. Positive projected checks must be paired with false-positive, collateral-change, and burden evidence; selecting cases on the same mediator's prior success cannot stand in for the source expert-work population.

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

Edit-derived elicitation adds a distinct **delta-to-use chain**: `native artifact
versions and interaction mode → exact edit delta → participant rationale →
model/analyst candidate interpretation → contributor acceptance/correction/rejection
and scope → independent promotion → selected delivery → recipient adoption or
justified rejection → changed artifact/action → independently measured consequence`.
No edge inherits authority from the prior edge. In particular, a direct edit may be
style, local preference, experiment, or factual correction; a prompt-regenerated
delta is jointly authored; and a model explanation linked to an expert's edit is not
expert-approved testimony. The five-person fixed-order study and mutable OSF snapshot
support edit/event capture and model-generated candidate storage, not extraction
validity, realized later presentation, causal quality improvement, burden reduction,
tacit transfer, or cross-domain utility. Preserve capture and use denominators and
map them to existing expertise-transfer, participation, intervention, longitudinal,
metric, and validity records; no edit-memory subsystem follows.

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
| [XpertBench](../papers/agent-benchmarks/2026-07-15-xpertbench-scaled-expert-task-validity.md) | B | Narrates a large cross-domain expert-task and one-shot judge pipeline, while its absent contributor/attrition ledger, observed Education task–rubric mismatch, unidentifiable CDR, unreleased instrument, and unverified release leads show that acquisition scale and a scored exemplar do not establish ecological, criterion, grader, professional, or participation validity |
| [KINA](../papers/agent-benchmarks/2026-07-16-kina-incentive-representativeness-validity.md) | B | Makes a submodular coverage proxy and reviewer-tournament assumptions explicit while showing that a cardinality theorem does not govern quota/duplicate-constrained repair and neither theorem establishes realized coverage, representativeness, contributor behavior, or validity without an instantiation witness |
| [OccuBench](../papers/agent-benchmarks/2026-07-15-occubench-language-simulator-validity.md) | A | Demonstrates cheap cross-domain synthetic tool-environment packaging while separating occupational labels and closed-loop simulator/verifier agreement from transition validity, professional authority, matched fault resilience, and real-environment transport |
| [AutomationBench](../papers/agent-benchmarks/2026-07-15-automationbench-workflow-projection-validity.md) | A | Adds broad executable multi-app state, strict conjunction with negative guards, task-local reset, and tool-discoverability interventions while separating synthetic contract conformance from work-demand provenance, production transition transport, complete consequence coverage, and readiness |
| [HealthAdminBench](../papers/agent-benchmarks/2026-07-16-healthadminbench-workflow-projection-validity.md) | A | Converts observed cross-system administrative work into 135 inspectable tasks and 1,698 checks while showing why path evidence, intermediate state, final consequence, prerequisite masking, strict conjunction, and occupational reliability are non-substitutable |
| [WindowsWorld](../papers/agent-benchmarks/2026-07-17-windowsworld-process-checkpoint-validity.md) | A | Makes 181 cross-application Windows task strings and 899 trajectory-wide milestone judgments inspectable while showing that free-path state appearance is not durable stage completion or process validity; flat checks, screenshot-only evidence, invalid records, unenforced setup, and an empty/final-`FAIL` L4 shortcut block occupational, reliability, safety, and readiness claims |
| [$OneMillion-Bench](../papers/agent-benchmarks/2026-07-14-onemillion-professional-value-validity.md) | A | Adds an auditable equal-cell five-domain portfolio with localized positive/negative criteria, but its purposive outcome-conditioned assembly supports neither professional-work prevalence nor dollar value delivered |
| [Chiron field study](../papers/agent-benchmarks/2026-07-17-human-ai-software-delivery-field-validity.md) | B | Separates recorded delivery measures from scenario-derived labor and exposes why field-cell identity, stable bridge units, actual resource exposure, external consequences, and a credible comparator are prerequisites for workflow-value claims |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Supplies realistic persona workspaces and file dependencies, while showing that availability, relevance, provenance, observed use, and causal use are distinct |
| [HippoCamp](../papers/agent-benchmarks/2026-07-11-hippocamp-personal-context-validity.md) | B | Separates composite contextual evidence and answer agreement from task-time authorization, causal adoption, consequential action, affected-party validation, and faithful personalization |
| [Workflow-GYM](../papers/agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md) | A | Contributes professional workflow/state realism and exposes the need to distinguish task validity, environment validity, and agent failure |
| [DeskCraft](../papers/agent-benchmarks/2026-07-14-deskcraft-interactive-workflow-validity.md) | B | Adds native professional-artifact checks and phased requirement delivery while separating authored interaction opportunity, trigger realization, authority, adoption, state-preserving repair, endpoint effect, burden, recipient uptake, and consequence |
| [HiLSVA](../papers/agent-benchmarks/2026-07-17-hilsva-mixed-initiative-validity.md) | B | Makes editable plans, approval, direct native-tool manipulation, rollback/history, selectable autonomy, and retrieval-based adaptation inspectable while showing that control availability, exercise, semantic uptake, verified artifact/state change, quality effect, burden, and professional value are separate estimands |
| [MAG](../papers/agent-benchmarks/2026-07-15-mag-action-guide-transfer-validity.md) | B | Captures action-linked user-facing instructions over interactive state while showing that source success, one-path text overlap, author-rated reference usefulness, independent recipient execution, transfer, maintenance, and professional consequence are separate claims |
| [User-simulator decision fidelity](../papers/agent-benchmarks/2026-07-15-user-simulator-decision-fidelity.md) | A | Uses real payment-linked dialogue to expose outcome-correlated disengagement error while showing that future-outcome stratification, observable-state sufficiency, person-specific simulation, free-running fidelity, policy transport, and real consequence require separate warrants |
| [WorkArena L1](../papers/agent-benchmarks/2026-07-12-workarena-l1-knowledge-work-validity.md) | B | Makes parameterized enterprise-UI setup, selected native-state predicates, and task-owned cleanup inspectable while separating atomic operation success from work sampling, collateral-state, professional-use, and readiness claims |
| [WorkArena++](../papers/agent-benchmarks/2026-07-11-workarena-plus-compositional-validity.md) | B | Makes executable setup/oracle/validator composition inspectable while showing that longer chains and lower success do not by themselves establish planning, workflow realism, or occupational coverage |
| [TheAgentCompany](../papers/agent-benchmarks/2026-07-11-theagentcompany-workplace-simulation-validity.md) | A | Separates integrated workplace substrate and selected workflow coherence from authority, consequence, sampling, collaboration, and labor-automation validity |
| [EntCollabBench](../papers/agent-benchmarks/2026-07-15-entcollabbench-role-permission-validity.md) | B | Makes static role-scoped tool execution, explicit HTTP routing, task-local state effects, and policy-document decisions inspectable while separating configured capability, usable handoff, delegated authority, approval classification, and authoritative approval effect |
| [Networked Intelligence](../papers/agent-benchmarks/2026-07-16-networked-intelligence-shared-context-validity.md) | B | Adds candidate-recipient selection and unsolicited cross-workstream delivery between shared storage and recipient use, while its one bundled three-expert campaign, reconstructed routes, post-hoc content universe, unequal standalone comparison, unexecuted proposal, and absent release do not identify routing benefit, tacit transfer, scientific validity, productivity, privacy, or readiness |
| [OdysseyBench](../papers/agent-benchmarks/2026-07-11-odysseybench-longitudinal-office-memory-validity.md) | B | Connects dialogue-distributed requirements to office-state action while exposing persistent-memory, evaluator-dispatch, collateral-state, and professional-validity gaps |
| [LongMedBench](../papers/agent-benchmarks/2026-07-14-longmedbench-longitudinal-clinical-validity.md) | B | Separates history volume and factual access from history necessity and consequence validity; its no-history result and retrospective next-event oracle show why a long record alone does not establish longitudinal decision competence |
| [SciAgentArena](../papers/agent-benchmarks/2026-07-14-sciagentarena-scientific-work-validity.md) | B | Adds matched step-wise versus dependent-pipeline scientific workflow evaluation and premise-validity tasks, while showing why mixed task units, configured-system bundles, propagated failures, fallbacks, and incomplete run/release evidence block real-world-science, novelty, autonomy, reliability, impact, or readiness claims |
| [AstaBench](../papers/agent-benchmarks/2026-07-14-astabench-scientific-suite-aggregation-validity.md) | B | Adds versioned common-suite operations, typed tool/openness labels, solve→score separation, artifact-triangulated grading, and score–cost frontiers while showing that incompatible component units, evidence views, metrics, eligibility sets, and policy weights do not form one validated research-assistance scale |
| [ResearchClawBench](../papers/agent-benchmarks/2026-07-15-researchclawbench-scientific-rediscovery-validity.md) | B | Adds 40 inspectable target-study-derived research workspaces and 154 weighted text/image criteria, while its report-only observer, uncalibrated 50-point anchor, public target materials, sparse criteria, and missing paper-run manifest limit the score to reference-content recovery rather than execution validity, discovery, professional capacity, or readiness |
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

AstaBench sharpens suite assembly into a **typed portfolio estimand**:
`component evidence vector + eligibility/missingness vector + resource vector +
aggregation policy + claim boundary`. A shared runner and macro-average do not
make exact-match code items, retrieval estimates, model-judged hypotheses, and
multi-artifact projects commensurate. Preserve each component's construct, unit
hierarchy, source/selection, configured-system and tool eligibility, evidence
view, scorer, metric, intended/valid/invalid/substantive denominators, clustering,
uncertainty, and resource boundary. Make the component vector primary; any scalar
must name its stakeholder weights, hard gates, missingness rule, and loss policy,
with sensitivity to item-weighted, component-macro, category-balanced, and
noncompensatory alternatives. AstaBench's 1,918 test plus 486 validation items,
purposive CS-heavy mixture, unmatched custom/private tools, task-specific invalid
policies, post-v2 code/scorer drift, gated dataset, and absent self-contained run
archive support portfolio-operation evidence—not a latent scientific-capability,
professional-validity, productivity, safety, or readiness claim.

KINA adds a prior **formal-instantiation boundary**: `declared proxy/theorem →
variables and assumptions → immutable implementation binding → realized constrained
selection or participant treatment → independent empirical outcome → validity/use`.
Its fixed-support max-coverage objective is submodular, but quota and duplicate
constraints plus repair remove the cardinality-only guarantee. The public 899-item
corpus instantiates 260 rather than 261 discipline paths, omits advertised source
fields and every anchor/calibration/selection/mechanism record, exposes the claimed
encrypted holdout, and conflicts on licenses. A coverage optimum is therefore an
optimum of an authored proxy, not representativeness. Existing projection,
participation, task-health, release-conformance, metric, and validity contracts host
the requirement; no MCQ or optimizer-specific subsystem follows.

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
environment do not establish professional-work validity. The completed AutomationBench
audit adds broad task-local synthetic multi-app transitions, hidden evidence, and strict
state predicates, but its co-authored task/state/transition/grader loop and absent
reference-service transport support simulator conformance rather than production
automation. The completed WorkArena L1
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

Field records add a complementary **workflow-value and bridge-unit boundary**:
`configured exposure → authoritative events/artifact-state → derived measures with
stable opportunities → observed resource use or typed scenario → independent
acceptance/delayed consequence → credible comparison and bounded value claim`.
Define what each field cell physically is and preserve source/work snapshot,
calendar, assignment, configuration, and evidence type. If the intervention changes
task granularity, stage routing, scope, or acceptance, retain raw numerators and
denominators plus a stable external bridge such as requirements, accepted
capabilities, defect opportunities, decisions, or consequences. Repeated project
labels and equal task counts are not equivalence; nominal headcount × elapsed time is
not observed labor.

The reviewed Chiron paper reports an internally coherent descriptive pattern across
three named modernization programs: later V4 cells are faster and better on its
reported validation-issue and first-release-coverage measures, while early V1/V2
cells trade speed against those downstream measures. But the 15 cells have no
disclosed calendar/physical ontology, cell-level provenance, stable task/requirement
mapping, actual labor, external acceptance, post-release outcome, or empirical
release; workflow version, model/tool changes, organizational learning, and time are
inseparable. This strengthens—not replaces—the AlphaEval, $OneMillion-Bench, AstaBench,
and benchmark-to-decision boundaries. Existing configured-system, trace,
artifact/state, metric, cost, task-health, production-validation, and validity records
are the durable homes; no software-specific schema or orchestration, defect,
productivity, value, professional-validity, production-fitness, or readiness claim
follows.

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

Dense workflow checks require a **dependency-aware consequence graph**, not a flat
list interpreted as independent abilities. Preserve `requirement authority → stage
precondition → admissible evidence acquisition → state/artifact handoff → committed
mutation → downstream affordance → final consequence`, plus alternative valid routes
and collateral invariants. Type path observance, intermediate consequential state,
and final outcome separately. An upstream miss may mask descendants; a prescribed
click may fail despite an equivalent route; and a strict all-check conjunction is an
endpoint policy, not evidence of error propagation or operational reliability.
HealthAdminBench's post-v1 release makes 135 synthetic cross-portal tasks and 1,698
checks unusually inspectable, but omits requirement-level observation/expert lineage,
dependency edges, raw paper runs, and repeated trials. Its observed-work origin,
partially audited expert projection, browser-local replicas, path-heavy checks, and
single shots support configured-instrument evidence—not healthcare-administration
coverage, safety, occupational capability, economic value, production fitness, or
readiness. Existing projection, benchmark-bundle, criterion, trace, task-health,
execution-validity, metric, and validity records are the durable homes.

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
[EntCollabBench](../papers/agent-benchmarks/2026-07-15-entcollabbench-role-permission-validity.md)
(static role/tool isolation and free-text peer routing expose real chain failures,
but do not establish task-scoped authority, accountable delegation, or approval-state effect),
[DELEGATE-52](../papers/agent-benchmarks/2026-07-11-delegate52-delegated-artifact-integrity.md)
(requested delta and preservation are orthogonal),
[Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md)
(availability, access, and causal use differ), and
[ACON](../papers/agent-benchmarks/2026-07-13-acon-context-compression-validity.md)
(task-sufficient compression is not state-faithful). Add
[decision fidelity under context compression](../papers/agent-benchmarks/2026-07-15-decision-fidelity-context-compression.md):
a summary can preserve individually plausible facts while reweighting caveats,
comparators, and offsets enough to change a named downstream policy, but agreement
with that policy remains evaluator-relative and can preserve the policy's error.
State fidelity, task sufficiency, decision-instrument preservation, independent
decision correctness, and stakeholder consequence therefore require separate
records. The paper's one sampled summary per method, three-call generated-probability
instrument, absent clustered uncertainty and factuality audit, unvalidated LLM fact
roles, and unreleased commercial case support no investment, professional, production,
or readiness claim. Existing handoff-usability,
workspace, transition, compression, trace, metric, task-health, and validity
machinery already hosts the requirements. The internal two-shape handoff producer,
consumer, adjudication, and counterfactual records establish only configured
synthetic content-dependence and scorer behavior—not human usability, professional
collaboration, cross-domain causal generalization, capability, safety, production
fitness, or readiness. No coding-specific or resumability subsystem follows.

Routed shared context adds one nonduplicate transformation between storage or
handoff and recipient use: `source proposition/authority/permission → routing
opportunity and candidate-recipient rationale → policy decision and delivered view
→ receipt/inspection → interpretation → adoption/rejection → decision or artifact
delta → authorized action → realized result/collateral state → burden and bounded
route utility`. A graph path is lineage, a delivery is transport, and a narrated
downstream proposal is neither causal adoption nor realized consequence. The
[Networked Intelligence](../papers/agent-benchmarks/2026-07-16-networked-intelligence-shared-context-validity.md)
case makes recipient selection and asynchronous cross-expert routing concrete, but
its three-human week-long package changes expertise, interaction, persistence,
proactivity, tools, compute, and stopping relative to two single standalone runs;
its two route stories are reconstructed, its 26-item content universe is post-hoc,
and the proposed experiment was not executed. No official graph, route, notebook,
campaign, rating, or result package was located. Preserve configured-package
comparison separately from a causal route study. The latter should freeze recipient
state and compare no route, targeted route, manual forwarding, broadcast,
delayed/stale route, and corrupted translation while measuring inspection,
adoption, decision/artifact change, consequences, missed links, overload, recovery,
and burden. Existing participation/authority, information-flow, handoff, workspace,
trace, artifact/state, metric, task-health, and validity machinery already hosts the
chain; no scientific-collaboration or graph subsystem follows.

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

[HiLSVA](../papers/agent-benchmarks/2026-07-17-hilsva-mixed-initiative-validity.md)
adds a complementary **realized-intervention ladder**: `mechanism
availability → decision opportunity/exposure → exercise with typed intent, basis,
and authority → agent receipt and semantic uptake/rejection → authoritative
artifact/state consequence and collateral preservation → independent task/quality
effect → human burden and bounded value`. Plans, approvals, direct edits, rollback,
uncertainty prompts, and retrieved guidance are intervention types, not evidence of
effective oversight merely because the interface exposes them. Preserve frozen
pre-state, exercised control, proposition and scope, agent interpretation, changed
locus and branch, independent native/rendered/export checks, rollback/adoption,
task effect, reliance, time, attention, latency, rework, and recipient consequence.
Use opportunity, exposure, exercise, valid uptake, verified state change, quality,
rollback, and burden denominators separately, with task/participant/order clusters.

The complete immutable-paper, study-instrument, and post-v1 release audit supports
mechanism availability and positive perceived control only. Twelve participants
completed four prescribed ParaView cases and rated the overall bundle highly, but
each mode is realized on a different task within participant, mixed initiative also
enables retrieval-based learning, the timing contrast is nonsignificant, mode-level
exercise and independent artifact-quality evidence are absent, and final autonomy
choice is observational. The release omits allocation, study logs, approvals/edits,
native states and outputs, graders, raw ratings, analysis, and tests; rollback
equivalence, action-guard coverage, persistence/reset, and execution safety remain
unverified. Existing participation/intervention, feedback, artifact/state,
rollback, metric, task-health, and validity records suffice; no visualization or
mixed-initiative subsystem follows, and no oversight-efficacy, expert-equivalence,
general-transfer, professional-utility, safety, or readiness claim is licensed.

Action-derived guidance adds a distinct **trajectory-to-recipient projection
chain**: `source requirement/environment version → executed action and observed
pre/post state → guide proposition with source-event locator → proposition truth,
scope, order, and omission status → assembled procedure and alternatives →
recipient-visible state and authority → interpretation and action → independent
completion, preservation, error, burden, and cost → task/interface/version
transport → maintenance → professional consequence`. Source-task success cannot
certify every narrated step; local target grounding cannot certify procedure
completeness; and one-reference overlap cannot certify recipient utility.

[MAG](../papers/agent-benchmarks/2026-07-15-mag-action-guide-transfer-validity.md)
makes the first links unusually visible by requiring one user-facing instruction
per screenshot-grounded action. Its evidence ceiling is much lower than a reusable
guide claim: the corpus is selected from 581/812 prior-agent-successful WebArena
tasks; only 563 are fully annotated; 21.4% of element steps disappear in the SoM
projection and 3.9% of clicks are mapping-suspect; the 174-task success, 171-guide,
and 167-annotated-test denominators are not fully reconciled; and the claimed
release was unlinked and unlocated at review time. Three research-team annotators
review local guide sentences, while the reported 82% reference “usefulness” is one
author's prospective rating of 50 tasks—not first-time-user execution. Concatenated
single-reference BLEU/ROUGE and the authored 0.4 success gate penalize valid route
divergence and do not observe state alignment, omissions, alternatives, recovery,
or comprehension. Prior guide text is also the producer's only textual memory,
confounding execution scaffolding with external-artifact utility. Existing
procedural-skill, proposition provenance, trace, artifact-admissibility, handoff-
usability, metric, task-health, configured-system, and validity records host the
repair; no web-guide subsystem follows. A useful validation should freeze state
and recipient, cross no/reference/model/corrupted guides, and measure independent
completion, preservation, errors, clarification, burden, total lifecycle cost,
and version drift before any transfer, labor-saving, professional, or readiness
claim.

Outcome-linked dialogue evidence adds a missing gate before this interaction
ladder can be treated as a model of people: `participant realization →
authorized observable-state sufficiency → one-step transition fidelity → free-
running fidelity → agent-policy transport → real consequence`. Communicative
realism and assigned-goal consistency do not validate refusal, stopping,
commitment, or willingness decay. Conversely, stratifying simulator error by a
person's future outcome does not prove that outcome-correlated latent state was
recoverable from the simulator's evidence view. The reviewed production-sales
paper reports a robust buyer/non-buyer contrast under simulator, prompt, and
LLM-instrument swaps, but one private corpus, unspecified non-payment censoring
and customer clustering, no human state-label validation, teacher-forced one-
turn probes, observational tactic analysis, and an unavailable claimed release
block human-equivalence, causal mechanism, policy-effect, cross-domain,
professional-validity, production-agent, safety, and readiness claims. Existing
participant, trace, metric, task-health, validity, consent, and longitudinal
records can carry the gate; no simulator-specific subsystem follows.

## 3. Expertise transfer is an intervention that must be separated from the measuring instrument

**Central insight:** When an expert procedure or `SKILL.md` and a rubric come from the same model of expertise, better scores may reflect evaluator-cue compliance rather than genuine transfer. Skills, rubrics, graders, tools, scaffolds, and feedback policies require independent versions and ablations.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Directly motivates public-skill versus private-check boundaries and skill/rubric factorial comparisons |
| [SkillsBench](../papers/agent-benchmarks/2026-07-10-skillsbench-paired-skill-efficacy.md) | A | Sharpens matched skill/no-skill comparisons and the need for repeated paired trials and uncertainty |
| [Online skill and memory budget value](../papers/agent-benchmarks/2026-07-16-online-skill-memory-budget-value.md) | A | Separates complete configured-package frontier, exact equal-envelope allocation, candidate→promotion→retrieval→adoption mediation, and amortized portfolio value; adds opportunity and complete-resource denominators plus order/state/retry treatment semantics while preserving the paper's approximate-budget, compound-control, three-run, no-release, and web-transport limits |
| [Medical Skill human evaluation](../papers/agent-benchmarks/2026-07-16-skill-augmented-medical-human-evaluation.md) | A | Adds the missing human-measurement warning to package efficacy: package availability, exposure, adoption, criterion conformance, substantive correctness, transfer, and readiness do not inherit one another; one selected 21-output task, bundled OpenClaw/package treatment, unequal model weighting, absent run traces, and negative expert ICC prevent an identified Skill effect |
| [Skills Are Not Islands](../papers/agent-benchmarks/2026-07-15-skill-supply-chain-dependency-risk-validity.md) | B | Shows that a Skill treatment may be a transitive Skill/package/service graph while separating static audit reachability from installed, visible, invoked, vulnerable, and consequential runtime state |
| [Agentic Skills at Scale](../papers/agent-benchmarks/2026-07-15-agentic-skills-at-scale-projection-validity.md) | A | Scales paired Skill/no-Skill authoring to 1,110 released packages while exposing that Skill-derived demand, tasks, instruction rubrics, goal rubrics, and one shared judge identify projected-procedure compliance more directly than independent utility |
| [AFTER](../papers/agent-benchmarks/2026-07-13-after-procedural-memory-transfer-validity.md) | A | Separates source-context gain, equivalent-form reuse, changed-context transport, and cross-model consumption while exposing complete-case selection, configured-system gaps, feedback/authoring overlap, and trace-diversity/volume confounding |
| [SLBench](../papers/agent-benchmarks/2026-07-13-slbench-skill-relation-validity.md) | B | Makes precondition, postcondition, constraint, conjunction, fallback, exception, override, and conflict relations executable, while exposing that LLM-co-designed extraction, case generation, and evidence contracts need independent projection and grader validation |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Shows why expert-written examples and criteria can improve judge agreement while also anchoring outputs |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Makes the harness and execution boundary explicit so a skill effect is not confused with launcher, tool, or isolation differences |
| [Harness-Induced Belief Divergence](../papers/agent-benchmarks/2026-07-17-harness-induced-belief-divergence-validity.md) | B | Makes representation, blocked-branch visibility, repair compression, verification masking, and evidence pruning explicit harness treatments, while its imagined non-executing rollouts, fabricated repair/verifier events, schema-elicited self-reports, one model, and incomplete release bound the evidence to prompt-conditioned report divergence |
| [WildClawBench](../papers/agent-benchmarks/2026-07-17-wildclawbench-native-runtime-transport-validity.md) | A | Adds 60 cross-domain bilingual/multimodal native-CLI tasks, artifact/state/trace grading, time/cost evidence, and negative Skill interactions; its post-v1 release audit shows that privileged networked images, runtime installs, mock/live services, adapter-normalized traces, state-to-prose fallback, absent result ledgers, and corrected live-web ground truth make full task→consequence transport validity a prerequisite for harness, Skill, safety, or reproducibility claims |
| [KWBench](../papers/agent-benchmarks/2026-07-11-kwbench-unprompted-problem-recognition.md) | A | Identifies situation framing before named-workflow execution, while showing that a cold final-artifact gate does not isolate recognition from inquiry, action, domain knowledge, or grading |
| [PM-LLM-Benchmark](../papers/agent-benchmarks/2026-07-17-pm-llm-process-analysis-judge-validity.md) | B | Supplies a broad inventory of process-analysis interactions and explicitly motivates hypothesis refinement, while its one-shot holistic judge collapses observation, candidate cause, discriminating test, evidence update, decision, and consequence; the release audit also shows that raw-result inspectability does not repair score-transform or version-identity drift |
| [Ambig-DS](../papers/agent-benchmarks/2026-07-13-ambig-ds-task-framing-validity.md) | A | Supplies paired full/ambiguous/ideal-clarification interventions and exposes valid-looking artifacts built on unsupported target or objective commitments, while bounding the result to synthetic Kaggle-derived ambiguity and an ideal oracle |
| [Industrial expertise codification](../papers/agent-benchmarks/2026-07-11-industrial-expertise-codification-agent.md) | A | Demonstrates a bounded package effect while exposing representation semantics, authorship overlap, missing component ablations, and the need for held-out independent measurement |
| [Vibe Calibration](../papers/agent-benchmarks/2026-07-16-vibe-calibration-tacit-skill-transfer-validity.md) | A | Adds consequential physical package execution and exposes target-device refinement, unpublished criterion authority, incomplete failure recovery, and terminal-status reconciliation as distinct from faithful tacit transfer, transport, expert equivalence, safety, or readiness |
| [UniClawBench](../papers/agent-benchmarks/2026-07-13-uniclawbench-proactive-closed-loop-validity.md) | A | Makes executor, private supervisor, public simulator, released signal, and repair cycle inspectable while showing that requested-task repair is not proactivity and structural isolation is not semantic non-leakage |
| [EdgeBench](../papers/agent-benchmarks/2026-07-13-edgebench-within-run-learning-validity.md) | A | Separates agent-visible feedback from evaluator-only snapshots and exposes adaptive-query, persistence, censoring, and best-so-far boundaries; its smooth suite fits are not task-level or universal learning laws |
| [AgencyBench](../papers/agent-benchmarks/2026-07-15-agencybench-feedback-artifact-validity.md) | A | Makes cumulative native-artifact repair and plural observer evidence inspectable while separating unaided first attempt, no-information retry, generic revision, consequence-only feedback, criterion-disclosed evaluator repair, and authorized ecological feedback; paper/release drift, observer disagreement, hidden aesthetics, missing human labels, single-run ambiguity, and no real users bound it to configured evaluator-assisted repair |
| [Pista](../papers/agent-benchmarks/2026-07-16-pista-active-oversight-workflow-validity.md) | B | Contributes semantic diffs as operation-level decision-time review artifacts and bounded human inspectability evidence, while its bundled N=16 treatment, unmatched stochastic defects, absent correction/preservation lineage, low endpoint means, and no recipient consequence block effective-oversight, professional-utility, or readiness claims |
| [HANSEL](../papers/agent-benchmarks/2026-07-17-hansel-interactive-verification-validity.md) | B | Adds interactive trajectory-to-page evidence compression and released shared-error human records, while support-path labels omit negative/contradictory routes, snippet recall and replay fidelity are untested, and a bundled N=14 study shows burden/preference more strongly than correct or calibrated verification |
| [Human oversight of agentic systems in practice](../papers/agent-benchmarks/2026-07-17-human-oversight-agentic-systems-practice.md) | B | Locates reported oversight across a priori control, co-planning, monitoring, and post-hoc review and exposes practical plan/test/spot-check/deference heuristics, while a one-company-heavy N=17 retrospective intensity sample with no observed work or outcomes supports lifecycle authoring hypotheses—not prevalence, heuristic correctness, oversight efficacy, or readiness |

**Repository consequence:** The benchmark bundle encodes configured-system identity and a no-skill/public-skill × independent/shared-rubric design rather than reporting an unqualified “skill lift.” Recognition is a different intervention axis: preserve situation-only, minimally framed, and fully specified conditions, positive and negative near neighbors, and separate observations for cue extraction, problem framing, targeted inquiry, action, and artifact consequence. Domain analysis adds a related but distinct inquiry ladder: preserve source-bound observation, anomaly or candidate hypothesis, rivals and uncertainty, predeclared discriminating test, executed evidence, update/rejection, recommendation or escalation, and downstream consequence. Candidate-generation quality must not inherit verification or causal-truth credit from a holistic prose grade. A recognition frame names or narrows the problem; a procedural skill prescribes how to solve it; a rubric or evaluator cue reveals what will be rewarded. Their versions and effects must not be collapsed. The internal problem-recognition replay exercises this staged instrumentation and invalid-environment abstention on builder-authored synthetic cases only; it supplies no expert validity, agent result, treatment effect, prevalence, or cross-domain claim ([replay](../pilots/problem-recognition-intervention/replay-report.json)).

Harness validity adds a runtime projection boundary after source-to-task construction:
`canonical executor/environment/verifier event → declared agent-visible projection
or typed omission → agent response → attempted/realized action → artifact/state →
independently graded outcome`. Harness prose is evidence delivered to the agent, not
world truth. Every visible event needs source-event lineage; every omission needs a
versioned policy, reason, and authority; representation change, blocked-branch
visibility, repair collapse, verification masking, and cost pruning remain distinct.
Invented success, repair, verifier, failure, or action-result events change the world
rather than merely its presentation. Elicited state or “belief” reports are secondary
diagnostics and cannot substitute for behavior, artifacts, or grounded outcomes.

The internal [event-projection conformance slice](../pilots/harness-event-projection-conformance/README.md)
passes 12 clean projections and localizes 10 planted inventions, relabelings,
reorderings, and undeclared omissions across two builder-authored ledgers. It is a
zero-call deterministic validator exercise: no agent acted, no professional task or
paraphrase equivalence was validated, and no harness effect, belief validity,
capability, artifact quality, cross-domain generalization, production fitness, or
readiness claim follows. Existing task projection, configured-system, trace,
execution-validity, artifact/state, metric, task-health, and validity records are the
durable homes; no belief or parallel task-IR subsystem follows.

Skill-treatment evidence now needs two independent chains. **Realization:** `package
version/mounted subset → surfaced/opened module → invocation → semantic adoption or
justified rejection → attributable artifact change`. **Claim promotion:** `shared-
source criterion conformance → independent substantive outcome → held-out transfer →
professional validity/readiness`. The medical study shows why human review does not
bridge them automatically: an exact task-family planner exists, but no run establishes
that it was surfaced or used; the selected 9-versus-12 output contrast changes platform
and package together; and negative expert ICC means the two-rater instrument cannot
stably resolve output quality in that sample. Balance must be defined over the declared
model/task/rater estimand, and criterion-specific reliability is a prerequisite to an
intervention claim rather than a post-hoc footnote. Unlike linked many-facet panels,
a two-rater, one-task study cannot justify severity adjustment or task/rater
population generalization. Existing configured-system, procedural-skill, trace,
artifact-view, rater, metric, task-health, and validity records already host the
chain; no medical or Skill-specific subsystem follows.

Skill value adds a third, orthogonal boundary: a paired package score is not yet a
resource-allocation or portfolio-value claim. Report complete-system frontiers,
exact equal-envelope allocation, candidate/promotion/retrieval/adoption mediation,
and amortized value separately. Type the eligible opportunity population and every
resource used to induce, verify, store, retrieve, inject, interpret, execute, repair,
maintain, and retire the package, including foregone direct action. For stateful
online methods, preserve task/block order, initial/final state hashes, and retry as
a treatment transition. The internal [allocation-parity audit](../pilots/skill-allocation-parity-audit/README.md)
retains 14/14 intended prior-study rows but admits zero exact contrasts; the
[prospective capture envelope](../pilots/prospective-allocation-telemetry/README.md)
passes a zero-call canary yet remains blocked on native per-call phase telemetry.
Neither artifact changes prior descriptive scores or licenses a Skill effect,
allocation effect, cost value, capability, cross-domain, professional, production,
or readiness claim.

Targeted inquiry has its own configured-interface boundary: `available evidence →
selected target → expressed request → parser/router interpretation → realized
access → visible payload → adoption → stop/action → consequence`. The frozen
[matched evidence-acquisition slice](../pilots/evidence-acquisition-matched-agent-v1/README.md)
retained 12/12 valid attempts over two purposive synthetic shapes. Both active
vendor-disposition attempts passed after two requests released two adopted records;
both active segment-release attempts failed the six-check endpoint after the
deterministic free-text parser treated controlling-metric requests as ambiguous,
while all eight supplied-information controls passed. One failed active attempt
eventually received one of two required records; the other received none. This is
instrumentation evidence and a candidate interface failure, not an agent inquiry,
parser-causal, information-supply, expert/professional, cross-domain, safety, or
readiness result: the shapes differ, each cell has two repeats, and no matched
request-interface contrast was run.

The subsequent frozen [v2 protocol](../pilots/evidence-request-interface-v2/protocol.json)
and [executed study](../pilots/evidence-request-interface-v2/execution/study-report.json)
did run that prospective contrast and retained 8/8 valid attempts: two synthetic
shapes × natural/structured interfaces × two purposive repeats, with no shape
pooling. All six structured requests were syntactically valid but unmatched by the
undisclosed exact-synonym map, yielding no releases. Eight natural requests yielded
five matches, three ambiguous parses, five releases, and five terminal citations
to released IDs; citation remains an adoption proxy only. In vendor-disposition,
both natural repeats passed at 1.0 quality/zero decision loss and both structured
repeats scored 0.667/one. In segment-release, natural repeats scored 0.833/zero and
0.667/one, while structured repeats scored 0.667/one and 0.833/zero, so there is no
stable shape-wide endpoint ordering. The
[flow audit](../pilots/evidence-request-interface-v2/execution/flow-audit.json)
preserves selection, expression, parser, access, terminal-citation proxy, stopping,
endpoint, and token cost separately.

The durable v2 conclusion is narrower than “structure helps”: selected topic and
request validity do not imply realizability in a private interface vocabulary, and
parser/access effects do not establish topic-selection quality.

The frozen [v3 protocol](../pilots/evidence-request-receipt-repair-v3/protocol.json)
and [executed study](../pilots/evidence-request-receipt-repair-v3/execution/study-report.json)
then added a non-answer-bearing interpretation receipt and one bounded repair while
holding the natural-request condition, semantic parser, scenarios, budget, release
rules, endpoint grader, and n=2 purposive repeats per cell fixed. Preflight and
replay verified all frozen hashes and retained 8/8 valid attempts. In vendor-
disposition, both conditions made two matched requests, released and terminally
cited the same two records, and passed at 1.0/zero decision loss in both repeats. In
segment-release, the receipt exposed an ambiguous combined request and one repair
was exercised in each receipt/repair repeat; both conditions still released and
terminally cited the same single audit record and scored 5/6 (0.833)/zero because
all four attempts omitted the metric dictionary. The
[v3 flow audit](../pilots/evidence-request-receipt-repair-v3/execution/flow-audit.json)
keeps request, receipt, repair, access, terminal-citation proxy, stop, endpoint, and
cost separate. Reported dollar cost was zero, but retained token use was
14,757–34,980 per attempt and 213,223 total; receipt/repair used more tokens in each
matched pair.

The v3 result demonstrates observability of parser interpretation and executable
bounded recovery, not endpoint improvement. Do not pool the two shapes or treat
identical endpoints as evidence of semantic selection quality, belief adoption,
stable interface benefit, or cost effectiveness. Across v2 and v3, structured
syntax, receipts, and repair are distinct configured-interface interventions.
Neither study supports agent-capability, causal-inquiry-benefit, expert,
professional, clinical, compliance, population, cross-domain, production,
deployment, safety, or readiness claims.

Across Skill-derived tasks, behavior-derived hidden factors, and language-simulated
environments, internal agreement supports a common **projection claim ladder**:
`shared-projection conformance → independently grounded efficacy → equivalent-form
transport → affected-party consequence → professional validity`. No rung inherits
the next. Record separate identities and authority for procedure or behavior source,
demand, task, goal oracle, environment transition/observation/fault, rubric, grader,
equivalent-form author, affected party, and release decision; also record shared
text, model, author, organization, examples, and outcome visibility. Generated
packages are useful calibration instruments, but confirmation needs external demand,
an independently grounded goal oracle, frozen equivalent forms across authoring and
environment boundaries, authoritative consequence evidence, and claim-specific
professional review.

The evidence ceilings are concrete. Agentic Skills at Scale releases 608 declared
top-level Skills and 1,110 tasks despite the paper's approximate 500/1,000 wording,
but no raw trajectories, judge decisions, or typed ledger for the roughly 4,000
nominally missing cells out of 42,180. MapSatisfyBench's restore–identify–filter
method usefully blocks future evidence from the solver view, yet its 500 selected
private-log items, historical-behavior hindsight, passive stochastic user simulator,
hand-set weights, and unreleased instrument do not establish current consent,
acceptance probability, or satisfaction. OccuBench releases 382 model-authored
packages, but only 98 of its 100 metadata-frame scenarios appear in the administered
table; implicit stochastic state, prompt-requested unmatched faults, and a verifier
that defaults to the simulator model support closed-loop synthetic conformance—not
occupational authority, real-environment robustness, or professional validity.
Existing projection, authority/participation, configured-system, environment,
artifact/state, task-health, metric, trace, and validity contracts are the durable
homes; no Skill-, map-, or language-simulator subsystem follows.

Skill packages add a separate **component-realization ladder**:
`declared/reference evidence → version-resolved lock graph → mounted/installed
graph → model/tool-visible graph → selected/invoked graph → attempted action →
realized state or information-flow consequence → diagnosed harm or utility`.
Static transitive reachability is valuable preflight and audit evidence, but no
rung inherits the next. The immutable ASSC paper reports high agreement with its
author-produced SKILL-DEP labels and large inferred graphs, yet releases no code,
labels, schema, snapshot, or outputs; its multi-layer set has 100 depth-selected
Skill graphs, service edges are not recursively resolved, package versions and
valid time are not preserved in the risk counts, and roots are strongly clustered
within a rapidly changing registry. Preserve exact component/version/source and
edge evidence across paired conditions, then observe installation, visibility,
invocation, policy decisions, and consequences separately. Reachability to a
package name, regex, or authority surface is not vulnerability, exploitability,
agent compromise, safety, capability, professional validity, or readiness.

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
AgencyBench adds a finer **feedback-conditioned evidence path**: `initial artifact
evidence → observer-specific defect proposition and authority → executor receipt
and uptake → changed artifact/state locus → criterion-local admissible
re-observation → repair or collateral regression → endpoint, burden, and cost`.
A score gain under criterion disclosure estimates oracle-assisted repairability,
not self-diagnosis or realistic collaboration. The release's text/vision
disagreement and beyond-rubric aesthetics show why adding or averaging observers
cannot repair an inadmissible evidence view or hidden obligation. A reusable pilot
should cross first-attempt only, no-information retry, generic revision,
consequence-only feedback, criterion-level disclosure, and—where genuinely
authorized—ecological feedback while holding the starting artifact, target system,
environment, budget, and grader fixed. Existing feedback/recovery, artifact-view,
configured-system, task-health, metric, validity, and execution records already
host this design; no AgencyBench-specific schema follows.

Pista adds a complementary **semantic-diff oversight path**: `operation-level diff
availability → exposure/inspection → comprehension → matched defect opportunity →
detection/diagnosis → authorized intervention → receipt/adoption or justified
rejection → intended state change → independent correction → collateral preservation
→ calibrated reliance/burden → recipient consequence`. A semantic diff can lower the
unit of inspection without being faithful or complete; generated explanations,
affected ranges, and dependencies require independent comparison with raw native
pre/post state. Pista's bundled two-task study supports perceived inspectability,
richer explanation, branch use, and reduced prompting, not a detection or repair
effect: defects were unmatched, correction lineage and artifact replay were absent,
and requirement success was `0.53` versus `0.50` without equivalence evidence. Read it
with DeskCraft's opportunity→adoption chain, AgencyBench's proposition→repair chain,
and ArtifactCopilot's evidence-packet boundary. Existing interaction,
feedback/recovery, artifact-view, trace, metric, task-health, participation, and
validity records suffice; no spreadsheet or oversight-specific subsystem follows.

HANSEL adds a complementary **loss-accounted evidence-projection path**:
`authoritative raw state/trajectory → typed inclusion and omission decisions →
projected evidence with source/state identity → reviewer exposure and inspection →
supported judgment → correct accept/reject/correct/escalate action → consequence`.
Its 45-trajectory labels concern pages that contributed to the agent's final path,
not every alternative, contradiction, blocked route, or negative observation needed
to verify the answer. Page-count compression and predicted-snippet precision therefore
do not establish minimal sufficiency. The released 14-participant records support a
bundled reduction in time/effort and strong preference, but the accuracy contrast is
nonsignificant and nine of 28 wrong-agent HANSEL opportunities remain wrong with high
confidence. Treat every evidence summary, semantic diff, or review packet as a lossy
projection with an omission ledger, replay/transformation identity, insufficiency
state, reviewer-inspection events, and decision-level calibration. Existing trace,
artifact-view, interaction, metric, task-health, and validity records suffice; no web
or breadcrumb-specific subsystem follows.

The developer interview evidence adds a complementary **oversight-allocation path**:
`configured authority/task consequence → oversight opportunity at configuration,
planning, execution, or review → available control/evidence/action → exposure and
actual inspection → judgment/intervention → uptake → independently observed state or
consequence → burden and residual risk`. Seventeen purposively recruited experienced
weekly users—12 at one large technology company—reported distributing effort across a
priori control, co-planning, light real-time monitoring, and intensive post-hoc review.
Their plan, test, spot-check, explanation, and cross-agent-agreement heuristics explain
how review is made tractable; retrospective accounts do not validate those proxies or
show that the reported allocation worked. Preserve oversight policy, interface
opportunity, actual human work, judgment/action, and consequence as separate objects.
Task decomposition and seeded plans are human treatment inputs, not free context;
tests and generated summaries are scoped observers, not guarantees; unfamiliarity may
require escalation rather than trust. Existing configured-system, interaction,
feedback/recovery, artifact/state, evidence-view, metric, task-health,
participation/authority, cost, and validity records suffice; no coding or
oversight-specific subsystem follows.

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
| [AIDABench](../papers/agent-benchmarks/2026-07-17-aidabench-end-to-end-artifact-validity.md) | A/B | Routes answers, rendered charts, and generated files to different observers and releases a substantial public package, while a broken reference path, prediction-relative denominators, lossy views, undisclosed judge calibration, mixed score semantics, and post-paper Skills/ConsensusEval show that output routing is not requirement-to-consequence or portfolio-claim closure |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Adds persistent workspace identity, protected/mutable zones, mutations, cleanup, and typed dependency evidence |
| [Workflow-GYM](../papers/agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md) | A | Reinforces checkpoint/final-state evidence while warning against attributing invalid environment behavior to the agent |
| [SaaS-Bench](../papers/agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md) | A | Adds deployable cross-application state and dense native checks, while showing that seeded preconditions, dependent consequences, weak joins, and artifact proxies can make a weighted checkpoint score diverge from run-attributable professional progress |
| [GDPval](../papers/agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | A | Contributes multimodal professional artifacts and expert preference evidence while showing that preference is not an absolute readiness threshold |
| [Agents' Last Exam](../papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md) | A | Shows why deterministic artifact grading still needs clean-start attestation, requested-criterion coverage, alternate-path tests, and verifier falsification |
| [PaperBench](../papers/agent-benchmarks/2026-07-15-paperbench-replication-rubric-validity.md) | A | Adds code, execution-log, and result evidence for long-horizon reconstruction while exposing the need for causal lineage, executable prerequisites, noncompensatory gates, and a separate partial-progress vector |
| [DORA](../papers/agent-benchmarks/2026-07-14-dora-disaster-response-consequence-validity.md) | A | Separates real-source and label truth, one executable analytical witness, endpoint agreement, professional acceptance, recipient uptake, action, and consequence; exposes uncalibrated geometry/numeric tolerances and absent operational evidence |
| [Claw-Eval](../papers/agent-benchmarks/2026-07-15-claw-eval-multichannel-trajectory-validity.md) | A | Reframes final response, action trace, and environment state as criterion-specific evidence routes rather than interchangeable raters; its selected hybrid-only audit, manifest/grader drift, manual reruns, absent fault injector, and incomplete attempt ledger do not calibrate observer accuracy or operational reliability |
| [CutVerse](../papers/agent-benchmarks/2026-07-15-cutverse-temporal-creative-artifact-validity.md) | A | Makes expert-demonstrated temporal work visible while showing that milestone screenshots do not establish native-project integrity, time-indexed rendered behavior, export validity, creative quality, or recipient acceptance; the post-v1 release lacks the paper tasks, evaluator, and results |
| [AgenticVBench](../papers/agent-benchmarks/2026-07-16-agenticvbench-expert-temporal-artifact-validity.md) | A | Repairs CutVerse's task/grader inspectability gap with a full later four-family release and criterion-specific manifest, frame, audio, metadata, and model views; its 13 brief/rubric resolution conflicts, five reversed good-state penalties, absent human/calibration/results records, rights gaps, and unreconciled rollout denominator show that observer richness cannot rescue an incoherent criterion contract |

**Repository consequence:** Score families remain separate, artifact views have admissibility contracts, and task/trial records preserve both produced artifacts and consequential workspace state. Editable artifacts need native, executable/recalculated, rendered, exported, and trace evidence plus authoritative mutation tests; inherited size and one reference witness do not establish work performed or maintainability. Each criterion routes to the authoritative object and temporal scope it actually requires: final prose, a tool request, committed service state, native structure, a rendered interval, exported bytes, or calibrated human judgment. More channels are not automatically redundant truth, and missing or stale decisive views produce `insufficient_evidence` or instrument invalidity rather than a substantive failure. Scored state checks must also distinguish environment readiness from trial-created deltas and identify shared-cause or descendant dependencies. The internal initial-state replay rejects pre-satisfied, stale, copied-witness, and omitted-transition cases, accepts a declared alternative, and abstains on invalid initialization; its seven synthetic matches validate only fixture/scorer behavior ([replay](../pilots/task-initial-state-conformance/replay-report.json)).

Temporal/compositional artifacts add a reusable evidence ladder: `source identity and
time basis → native editable structure → rendered interval behavior → export identity
and decodability → creative/professional acceptance → recipient consequence`. A
single screenshot or progress dialog cannot inherit later rungs. The completed
[11-case temporal conformance replay](../pilots/artifact-transition-conformance/v0.2-temporal/replay-report.json)
separates source, native, render, and export observers; it catches just-outside-
tolerance timing, right appearance at the wrong interval, wrong component, broken
editability behind a plausible render, missing views, export mismatch, and one
declared alternate sequence. This is deterministic builder-authored contract evidence
only—not temporal-observer accuracy, creative quality, expert validity, model
capability, reliability, professional validity, production fitness, or readiness.

AgenticVBench adds a **signed criterion-contract requirement** above those views:
`public basis → proposition → desirable/violation polarity → applicability →
authoritative temporal view → observer/threshold → dependency → score contribution
→ licensed interpretation`. Validate prose, weight sign, inversion flags, public/private
requirements, and aggregation before execution. A multimodal judge cannot decide which
layer is authoritative when the brief and hidden criterion conflict. Preserve a complete
task × configured-system × repeat ledger and separate expert authoring, student-editor
reference, model-grader calibration, artifact conformance, professional acceptance, and
readiness rather than promoting one agreement number or macro score across them.

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
| [Agentic CLEAR](../papers/agent-benchmarks/2026-07-17-agentic-clear-dynamic-diagnostic-validity.md) | B | Makes heterogeneous trace normalization, multi-resolution judge views, open-vocabulary issue induction, and evidence backlinks inspectable while showing that sampled judge-text categories are review hypotheses—not stable prevalence, criterion-valid diagnoses, supported roots, or actionable repairs |
| [Measuring Agents in Production](../papers/agent-benchmarks/2026-07-14-measuring-agents-production-practitioner-evidence.md) | B | Supplies a transparent practitioner instrument and selected reports of bounded workflows, human gates, sensitive context, delayed outcomes, and mixed evaluators; outcome-conditioned recruitment, optional-question denominators, unknown respondent/organization dependence, and no system audit make this portfolio evidence, not representative prevalence or practice efficacy |
| [Agentic Confidence Calibration](../papers/agent-benchmarks/2026-07-14-agentic-confidence-calibration-validity.md) | B | Separates predicted success for one configured trajectory from repeated reliability and causal diagnosis; its unreleased labels/configurations, post-outcome features, clustering omissions, asymmetric transfer, and logprob dependence block decision-utility or universal-calibration claims |
| [ResearchRubrics](../papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | A | Contributes inspectable criterion authoring while revealing compensatory mandatory criteria and missing applicability/dependence controls |
| [FinResearchBench II](../papers/agent-benchmarks/2026-07-16-finresearchbench-ii-consensus-rubric-validity.md) | B | Exposes 14,450→3,687→2,600 generated-criterion attrition and makes panel stability/non-triviality screening operational, while report-conditioned generation, outcome-conditioned selection, a 70.76% joint-unanimity subset, partial holdout, and no release block criterion-authority, transport, professional-validity, and readiness claims |
| [PaperBench](../papers/agent-benchmarks/2026-07-15-paperbench-replication-rubric-validity.md) | A | Provides released leaf labels and a criterion-level judge study while showing that pooled-leaf class-macro F1, invalid-as-zero handling, and local agreement do not validate paper-level scores or replication decisions |
| [AdaRubric](../papers/agent-benchmarks/2026-07-15-adarubric-adaptive-trajectory-instrument-validity.md) | B | Separates task-conditioned criterion generation, step/dimension observation, and filtering, while its absent empirical release and paper/code contradictions show that fixed-rubric score correlation, repeat agreement, and training gains do not validate adaptive criteria, decisions, rewards, or deployment |
| [GrowLoop](../papers/agent-benchmarks/2026-07-17-growloop-human-seeded-rubric-case-coevolution-validity.md) | A | Couples versioned rubrics and case sets and distinguishes anchor refinement from additive/restructuring updates, while showing why unanimity-selected supervision, model-order-conditioned case admission, and one unexecuted outer transition cannot establish tacit-criterion authority, legitimate-disagreement coverage, construct continuity, or living-benchmark validity |
| [BigFinanceBench](../papers/agent-benchmarks/2026-07-14-bigfinancebench-workflow-derivation-validity.md) | A/B | Makes source-to-calculation checkpoints and repeated visible trajectories inspectable on the public subset, while showing that narrated exact values, lossy judge views, dependent criteria, and held-back headline evidence do not establish an audited workflow |
| [GroundEval](../papers/agent-benchmarks/2026-07-14-groundeval-evidence-path-validity.md) | B | Makes actor/time gates, configured evidence paths, and bounded negative-search obligations deterministic, while showing that repeatable code does not establish contract authority/completeness, causal effects, global absence, or observer superiority |
| [Auto Benchmark Audit](../papers/agent-benchmarks/2026-07-14-auto-benchmark-audit-task-defect-validity.md) | B | Makes path-grounded inspection of instruction, environment, reference, and grader scalable while separating configured-auditor labels and selected-finding precision from confirmed-defect prevalence, repaired-instrument validity, and corrected capability |
| [JADE](../papers/agent-benchmarks/2026-07-11-jade-dynamic-professional-grading.md) | B | Separates invariant requirements from response-created claims/consequences, while exposing variable denominators, shared-cue judging, verifier fail-open behavior, and unvalidated score fusion |
| [Adversarial verifier hardening](../papers/agent-benchmarks/2026-07-14-adversarial-verifier-hardening-validity.md) | A/B | Makes iterative false-accept search, patch provenance, and fixed held-out attack replay inspectable, while directly showing that a narrow solver witness can yield 0% attack success together with near-total legitimate-solution rejection |
| [AsymmetryZero](../papers/agent-benchmarks/2026-07-14-asymmetryzero-semantic-eval-contracts.md) | B | Makes criterion, grader mode, panel vote, weight, threshold, cost, and adapter realization inspectable; its private available-case study shows why cross-model dissent, repeated-call instability, criterion correctness, task-decision agreement, and use/decision loss must remain separate |
| [SaaS-Bench](../papers/agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md) | A | Release audit shows that a checkpoint becomes partial-progress evidence only when it was not pre-satisfied, is attributable to the run, has declared necessity/sufficiency, and does not double-count one upstream event through dependent consequences |
| [Efficient Benchmarking of AI Agents](../papers/agent-benchmarks/2026-07-09-efficient-benchmarking-ai-agents.md) | B | Shows that reduced panels may preserve rank while degrading absolute-score interpretation |
| [Agent Psychometrics](../papers/agent-benchmarks/2026-07-09-agent-psychometrics.md) | B | Treats difficulty as a property of the configured task/system package and motivates response matrices and scaffold-aware reporting |
| [Partial agent-benchmark decisions](../papers/agent-benchmarks/2026-07-15-partial-agent-benchmark-decision-validity.md) | A | Adds a distinct reduced-evaluation estimand: preserve a thresholded pairwise decision from one fixed completed record under explicit conditional-error, group-coverage, and deferral targets. Its replay and release audit show that first-sufficient fractions are policy/grid/population properties—not prospective stopping, rank, diagnostic, reliability, or professional-validity evidence. |
| [Expert evaluation and limits of human feedback](../papers/agent-benchmarks/2026-07-11-expert-disagreement-human-feedback-validity.md) | A | Shows in one small clinical panel that shared rubrics can yield stable directional disagreement; motivates framework-indexed observations and policy-explicit aggregation without universalizing the domain result |
| [Many-facet human/AI rater effects](../papers/agent-benchmarks/2026-07-11-many-facet-human-ai-rater-effects.md) | B | Separates agreement, panel-relative severity, model fit, repeat stability, and decision validity; shows why a linked calibration design does not make graders interchangeable |
| [Rubric-modification interventions](../papers/agent-benchmarks/2026-07-11-rubric-modification-human-autorater-agreement.md) | B | Makes examples, context, criterion-call topology, score transformation, and aggregation part of instrument identity; agreement gains can coexist with shared cueing or construct change |
| [AI Agent Reliability](../papers/agent-benchmarks/2026-07-11-agent-reliability-profile.md) | B | Separates accuracy from repeatability, perturbation sensitivity, confidence quality, and violation consequences while binding each estimate to a configured operational profile |
| [Stochastic Agent Evaluations](../papers/agent-benchmarks/2026-07-14-stochastic-agent-evaluations-icc-validity.md) | B | Makes task-level repeats and released response matrices inspectable while showing that the published variance-of-task-means ratio is not ICC(1,1), omitted invalids change the estimand, and repeat budgets are decision- and population-specific |
| [Performance-optimization benchmark reliability](../papers/agent-benchmarks/2026-07-15-performance-optimization-benchmark-reliability.md) | B | Separates executable artifacts from environment-sensitive criterion validity; four-profile/three-round replay and fixed-output rescoring expose reference-signal loss, near-zero margins, and score leverage, while the absent study release and bounded design do not establish machine-invariant transport, causal rank effects, portfolio capability, saturation, or professional validity |
| [Criterion validity against business outcomes](../papers/agent-benchmarks/2026-07-16-criterion-validity-business-outcomes.md) | A/B | Adds a direct score→verified-payment association study and dimension heterogeneity warning, while its whole-dialogue observer, outcome-dependent eligibility, case enrichment, unvalidated judge, small selected reweighting, and absent phase-2 rows separate concurrent association from prediction, intervention benefit, customer value, and readiness |
| [LiveBench](../papers/agent-benchmarks/2026-07-11-livebench-contamination-limited-lifecycle.md) | B | Makes benchmark renewal operational through rotating recent-source forms, temporary private roles, deterministic checks, and reruns, while exposing equivalent-form, outcome-conditioned selection, exposure, and grader-drift limits |
| [WorkBench Revisited](../papers/agent-benchmarks/2026-07-12-workbench-revisited-longitudinal-lifecycle.md) | B | Shows why repaired current measurement and longitudinal continuity need linked forms and task-level score bridges rather than one homogeneous time series |
| [Reasoning/coding benchmark evolution](concepts/reasoning-coding-benchmark-evolution.md) | B | Compares MMLU→MMLU-Pro and HumanEval→LiveCodeBench from full papers and pinned current releases; separates common-interface adoption, demonstrated headroom/prompt stability, executable equivalence, and timestamped renewal from unsupported work-validity and contamination-free claims |
| [BrowserGym](../papers/agent-benchmarks/2026-07-11-browsergym-ecosystem-measurement.md) | B | Separates useful runner/interface interoperability from unsupported evaluator, score, reset, or construct equivalence across adapted benchmark families |

**Repository consequence:** Criterion/check contracts, metric-monitoring contracts, validity arguments, response matrices, and separate ranking versus absolute-capability claims. Grader identity includes rubric/examples, evidence view, criterion execution topology, score transformation, aggregation/tie policy, and configured rater. Agreement, panel-relative severity, fit, repeated-call stability, construct preservation, decision loss, cost, and audit burden remain separate outcomes; adjusted scores never overwrite raw observations or become adjudicated truth. Reliability is a conditional profile—not a system trait—indexed by configured system, task/form population, environment, time, intervention/exposure distribution, and consequence model. Accuracy, repeatability (including consistently wrong behavior), resource variation, perturbation effects, confidence quality, violation frequency, severity, remediation, and loss remain separate. Every perturbation needs independently supported preservation and exposure claims; wrapper recovery cannot count as agent recovery; confidence is licensed only for the decision time and evidence view at which it was elicited. Plural judgments remain immutable observations; aggregation is a versioned stakeholder/error-loss policy rather than discovered ground truth. Specification error, evidence gaps, rater instability, framework-conditioned disagreement, policy selection with dissent, and unresolved value conflict require distinct dispositions. Derivation criteria must also be proof-carrying: source identity and passage, extracted claim, typed operation, dependencies, conclusion, exact observer view, and licensed claim remain distinct. Mentioning an expected value cannot inherit provenance or causal-use credit; one upstream defect and its descendants must not be counted as independent failures. The completed synthetic plural-judgment conformance slice exercises this boundary but supplies no prevalence, professional-consensus, or readiness evidence. Before the second pilot is interpreted, its adversarial audit should plant a pre-satisfied requirement, an unrelated record sharing the expected scalar, a title-only empty artifact, and one upstream defect with several descendant checks; readiness or duplicated consequences must not inflate progress.

Criterion-to-outcome validation adds a separate ladder: `criterion authority →
configured observer validity → score frozen at a declared decision time → eligible
population/base-rate and cluster policy → external outcome and observation window →
concurrent association → incremental prospective prediction → score-targeted
intervention effect → threshold/loss and stakeholder decision`. No rung inherits the
next. Whole-dialogue scores can encode user cooperativeness or outcome-adjacent cues;
case enrichment can support selected associations while invalidating calibration and
predictive value; and an observable payment/acceptance label can remain incomplete or
harmful as an optimization target. Preserve reversals, refunds/rework, burden, safety,
and longer-horizon outcomes rather than zero-weighting legitimate obligations because
they do not correlate with one business endpoint.

The reviewed conversational-commerce v1 supplies manuscript-level evidence that two
of seven configured-judge dimensions have moderate concurrent associations with
payment in a 25-converted/35-unconverted human-only sample, while one dimension has no
detectable bivariate association. Different eligibility rules by outcome, roughly 0.5%
source prevalence, one unvalidated whole-transcript model judge, uncontrolled user
intent and clustering, tiny selected weighting/cross-validation, and absent phase-2
rows block judge-accuracy, predictive, causal, customer-value, professional-validity,
production-fitness, and readiness claims. Existing grader, metric, validity,
task-health, participation, and production-validation records are the durable homes;
the missing work is a frozen pre-outcome empirical episode, not a new schema.

FinResearchBench II adds a reusable **criterion-health and outcome-selection
firewall**: `candidate provenance → authority/public basis → admissible evidence view
→ repeated observer reliability → development-cohort discrimination → independent
confirmation → threshold/loss`. Its three-judge screen is useful triage, but the
98.67% human/LLM same-label result conditions on 2,867/4,052 jointly unanimous items
(70.76%), and the 2,600 survivors are selected to vary on the same ten-report pool
used to construct the instrument. Preserve unanimous and disputed criteria, always-
pass/fail roles, every upstream artifact/system use, and selection-adjusted held-out
estimation. Read with ResearchRubrics for authoring authority and AsymmetryZero for
the jury-substitution ladder: authority, agreement, repeated-call reliability,
discrimination, decision equivalence, and loss do not inherit one another. Existing
criterion, evidence-view, rater, response-matrix, task-health, metric, and validity
records suffice; no finance-specific schema follows.

PaperBench adds a **replication evidence lattice**: `declared method → implemented
mechanism → executed mechanism → produced artifact → result correspondence →
robustness/provenance → licensed claim`. Preserve each link's authoritative artifact
view, execution lineage, dependency type, evidence state, grader validity, and claim
gate. Local criterion credit remains a diagnostic vector. It must not be promoted to
end-to-end completion through compensatory averaging. Judge validation must likewise
name its unit and decision: pooled-leaf class-macro agreement, equal-task agreement,
root-score error, threshold flips, severe-error loss, and invalid-observation burden
are different estimands. The five-example released JudgeEval supports only bounded
leaf-label concordance; it does not validate a replication threshold or expert
substitution. Existing rubric, artifact, trace, metric, task-health, reliability, and
validity records are the durable homes; the queued replay should test this boundary
without creating a science-specific schema.

AdaRubric adds a distinct **adaptive-instrument variance boundary**:
`task/trajectory sample × rubric-generation draw × observer draw × aggregation/filter
policy × decision threshold`. Fixed-rubric repeated judgment estimates only one slice.
Cross independently regenerated rubrics with repeated observer calls, then adjudicate
criterion preservation, omission, spurious additions, applicability, dependencies,
alternative paths, evidence-view shifts, threshold changes, and decision loss. Keep
rubric adaptability, criterion authority, judge repeatability, regenerated-instrument
stability, decision equivalence, and reward usefulness as separate claims. Pearson
score correlation and Krippendorff alpha do not bridge them. The post-v3 official
release further makes implementation correspondence part of validity: it uses one
trajectory-wide call rather than the paper's `K×N` calls, lacks the stated semantic
validation/fallback/cache, has no multimodal evidence path or empirical artifacts,
and multiplies scores by confidence without normalizing by confidence, so low
relevance becomes a quality penalty. Existing criterion, evidence-view, configured-
grader, response-matrix, task-health, metric, and validity records remain the correct
homes; no adaptive-rubric subsystem follows.

GrowLoop adds a coupled **criterion-space × probe-population evolution boundary**:
`typed human observations/disagreement → seed admission and authority → model-proposed
criterion transformation → versioned rubric/score semantics → rubric-conditioned
candidate cases → adaptive admission history → independently observed coverage gap →
authorized refine/add/restructure decision → frozen cross-version bridge → bounded
claim`. Preserve every rejected rubric and case candidate, trigger, model/judge pool,
retirement, rollback, and cost. Unanimity among three undisclosed raters supplies a
clean selected fitting target, not criterion authority; model judgments in a divergent
zone require independent admissibility review rather than author-declared plausibility.
Likewise, repeatedly regenerating cases until one judge recovers a prior four-model
ordering makes discrimination an admission objective, not untouched validity evidence.
The paper executes initial rubric fitting and case regeneration but no fresh-case →
human annotation → revised-rubric outer transition; frozen anchors, rollback, multi-
cycle stability, and cross-domain transport remain future work. Existing participation,
criterion, evidence-view, task-health, configured-grader, metric, response-matrix,
longitudinal, and validity records are the durable homes; no conversation- or self-
evolution-specific schema follows.

Automated benchmark auditing adds a **candidate-defect lifecycle** before score
revision: `immutable instrument → auditor identity and entitled evidence view →
candidate finding → independent adjudication plus missed-defect probe → retain,
quarantine, repair, or retire decision → new version → equivalent-form revalidation
→ historical-score and construct sensitivity`. Static and outcome-visible
trajectory audits are different observer conditions. Path resolution does not
establish entailment; a maintainer change, expert judgment, executable
counterexample, and repaired rerun remain distinct evidence. Keep auditor-label
prevalence, confirmed-defect prevalence, deletion-mask sensitivity, common-task
paired change, repaired-form performance, and rank/decision sensitivity separate.
ABA's purposive capped and clustered portfolio, one unrepeated auditor, selected
positive adjudication, unknown clean-task false negatives, missing 34,285-task
records and exclusion masks, post-v2 release, and no repaired reruns support triage
only—not automatic invalidation, corrected capability, professional validity, or
readiness. Existing task-health, review-selection, metric, grader, validity, and
change-log records host this lifecycle; no audit-specific contract follows.

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

Environment-sensitive artifact criteria add a distinct **criterion operating
envelope** inside this hierarchy: `replayable → criterion-valid here → transport-
supported → decision-stable`. Preserve base/reference/candidate identity; engine,
software, hardware, resources, workload, preparation, cache, concurrency, and
timeout; intended cells and typed invalids; repeated raw observations; paired
contrast and criterion margin; environment/round/interaction structure;
aggregation leverage; and the stakeholder-loss policy. Semantic or artifact
validity does not imply stable runtime, memory, rendering, recalculation, database,
or simulation status. One local threshold crossing does not imply transport, and
fixed-output rank sensitivity does not identify a universally correct aggregator.

The full [performance-optimization reliability review](../papers/agent-benchmarks/2026-07-15-performance-optimization-benchmark-reliability.md)
finds bounded descriptive evidence across 740 official reference patches, four
cloud processor profiles, and three rounds: many references lose their original
admission signal under a strict all-cell rule; one benchmark family has near-zero
reference margin; and harmonic aggregation can concentrate leverage and reorder
fixed public outputs. The study provides no raw-cell release, replicated machine
population, held-out environment, hierarchical transport estimate, repeated agent
trials, or stakeholder loss basis. Its best-of-ten public union is selected
portfolio coverage—not one system's capability or saturation. Saturation remains a
separate use-indexed judgment requiring a declared system/feasible-portfolio
population, attempts, cutoff, exposure, time, cost, milestone, and renewal decision.
Existing execution-validity, task-health, artifact-admissibility, response-matrix,
metric, and validity contracts suffice; no coding- or performance-specific schema
or synthetic pilot follows.

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

[Agentic CLEAR](../papers/agent-benchmarks/2026-07-17-agentic-clear-dynamic-diagnostic-validity.md)
adds a nested **dynamic-diagnosis transformation ladder**:
`raw trace/state → transformed evidence view → judge observation → sampled issue
phrase → induced category/stability → criterion-aligned diagnosis → supported root
→ intervention-tested actionability`. Preserve raw/normalized hashes, omitted and
truncated channels, judge and prompt, eligible/sampled/valid mapping denominators,
sampling probability and order, category cap and merge/split lineage, independent
labels, dependency/rival-cause evidence, and repair outcomes. A recurring phrase
among low-score critiques is neither failure prevalence nor a root. Stability needs
resampling and judge/order/cap perturbations; criterion alignment needs independent
held-out labels; root promotion needs temporal/dependency evidence; actionability
needs matched repair with sham, regression, false-lead, burden, and cost outcomes.
Include successful alarming-language traces, legitimate retries, correct refusals,
and downstream-symptom cases as negatives.

The full immutable-v1/release audit finds useful machinery but a low claim ceiling:
the only category-alignment slice has 117 TRAIL traces and best macro-F1 0.459 with
partial matches. The 1,129-trace corpus is curated and family-imbalanced; adapters
and compact views are lossy; induction is outcome-conditioned and order-dependent;
remapping is self-referential; invalid mappings can become all-zero; repeats,
clustered uncertainty, independent issue-truth/root labels, paper-run records,
human-utility evidence, and intervention tests are absent. Existing trace,
evidence-view, grader, review-selection, root/surface, task-health, metric, recovery,
and validity records suffice; no CLEAR-specific schema follows.

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
| [ProcGrep](../papers/agent-benchmarks/2026-07-16-procgrep-procedural-fingerprint-validity.md) | B | Makes multi-resolution action-sequence regularities inspectable and searchable while showing that configured-system discrimination, repeated stability, matched intervention, skill transfer, monitoring utility, and readiness require separate evidence; its paper-time release omits headline row inputs and exact split lineage |
| [Plans Don't Persist](../papers/agent-benchmarks/2026-07-16-plans-dont-persist-context-eviction-validity.md) | B | Adds forced-prefix replay and a derived-trace contamination warning while showing that broad plan-exchange removal, last-token cosine distance, free behavioral adoption, and broad-history endpoint loss are separate experiments |
| [Who&When Pro](../papers/agent-benchmarks/2026-07-15-whowhen-pro-failure-attribution-validity.md) | B | Makes the injected actor/action/step known under attempted exact-prefix replay, while showing that intervention identity, first divergence, propagated symptom, but-for effect, earliest sufficient cause, natural multi-cause root, and repair utility are distinct claims; its unreleased corpus/code prevents construction and result audit |
| [The Saturation Trap](../papers/agent-benchmarks/2026-07-15-intervention-timing-construct-reliability.md) | B | Separates exact-index, event-window, intervention-type, detector, utility, and decision-validity targets; its one-trajectory labels and post-v1 `Δt=0` audit show target/instrument fragility rather than general timing unreliability |
| [LH-Bench](../papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | A | Adds error → verifier feedback → repair → verification as a measurable recovery chain |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Prevents launcher, permission, tool, and sandbox faults from being mislabeled as capability failures |
| [Amazon production-agent evaluation](concepts/amazon-production-agent-evaluation.md) | B | Adds production-oriented decomposition of tool, memory, reasoning, and end-to-end operational failures |
| [AARRI-Bench](../papers/agent-benchmarks/2026-07-11-aarri-research-judgment-lifecycle.md) | A | Makes stop, refuse, escalate, clarify, and preserve legitimate consequence-bearing outcomes while directly exposing lexical-verifier false rejection |
| [UnderSpecBench](../papers/agent-benchmarks/2026-07-13-underspecbench-action-boundary-validity.md) | B | Separates private intended transition from public authorization, resolvable uncertainty, attempted action, realized effect, and observer coverage |
| [MemoryArena](../papers/agent-benchmarks/2026-07-13-memoryarena-interdependent-experience-action.md) | B | Makes prior-session evidence consequential through dependency-bearing action while exposing feedback, state-reconstruction, retrieval, adoption, and grader confounds |
| [MemOps](../papers/agent-benchmarks/2026-07-15-memops-lifecycle-memory-validity.md) | B | Crosses expected lifecycle events with trigger, target, state, application, and trajectory probes while showing that an authored gold trace is not an observed store mutation, deletion guarantee, adoption record, or causal root |
| [PASB](../papers/agent-benchmarks/2026-07-16-pasb-persistent-state-writing-validity.md) | B | Adds visible profile/memory/skill capture between persist and query, while showing that execution-channel isolation, claim-specific realized delta, post-selection, retrieval/adoption, and consequence need separate evidence; the released OpenClaw runner retains one session across phases |
| [PM-Bench](../papers/agent-benchmarks/2026-07-16-pmbench-prospective-memory-validity.md) | B | Makes delayed obligation activation, updates, hidden-cue monitoring, lures, exact timing, and replay diagnostics executable while showing that an ungraded advance choice is not an ongoing task and query counts are not interference cost |

**Repository consequence:** Root/surface attribution, causal trace slices, recovery records, invalid-trial handling, and task-health lifecycle records. Apparent requests should also admit a counterfactual action contract: observable disqualifying evidence, authority and threshold, legitimate alternatives, required state and communication consequences, abstention/escalation, and collateral harm. Decision, rationale, artifact preservation, communication, cost, and harm remain separate observations. Matched persist/stop and comply/dissent forms are required to distinguish calibrated judgment from generic quitting or contrarianism; substantive action must be tested independently of lexical realization, with paraphrase contrasts and retained semantic adjudication. AARRI's inspectable authored suite motivates this design but its missing sampling frame, contributor accounting, human baseline/agreement, repeats/uncertainty, verifier-wide audit, complete configuration, contamination-safe split, environment evidence, and paper-pinned release prevent researcher-quality or cross-domain capability claims.

Controlled injection adds an **attribution claim ladder**: `declared injected delta → first observed divergence → propagated surface failure → but-for effect under paired replay → earliest sufficient cause → natural multi-cause root → diagnosis-guided repair utility`. No rung inherits the next. A successful seed plus a failed newly sampled continuation identifies the construction treatment, but without repeated paired suffixes, sham/alternative corrections, full state attestation, all-attempt denominators, and recovery tests it does not prove that correcting the injected action would rescue that branch or that the same label transfers to natural failures. Who&When Pro's reported 12,326 retained traces, 100-row label-visible human check, and protocol comparisons make this boundary concrete; success-conditioned seeds, endpoint-failure selection, incomplete replay equivalence, single-mode labels, absent clustered uncertainty, and unreleased data/code restrict it to synthetic intervention-recognition evidence. Existing trace, root/surface, recovery, invalid-trial, task-health, evidence-view, metric, and validity records already host the repair; no injection-specific schema follows.

Descriptive procedural fingerprints add a separate **configured-observation claim ladder**:
`raw event and state → adapter/canonicalizer observation → repeated subsequence → configured-system discrimination → time/task/interface stability → matched procedural intervention → endpoint/artifact consequence → skill transfer → calibrated monitoring decision → production fitness/readiness`. A fingerprint belongs to a task distribution, model, scaffold, interface, observation policy, and time window—not automatically to a base model or skill. Vocabulary induction and tuning must be nested inside training task groups; harness/interface and outcome controls must be crossed; raw, native, canonical, artifact, and state views must remain linked. ProcGrep's inspectable library and bounded post-v1 matched-task comparison support diagnostic use, while missing paper-time row inputs, unclear released task-held-out execution, label-informed vocabulary-size selection, and absent repeated/intervention/decision evidence prohibit stronger promotion.

Intervention timing adds an upstream **policy-target chain**: `frozen decision time
and admissible prefix → candidate opportunity → acceptable event window and
consequence-equivalent action set → reviewer authority/view and repeated judgment
→ configured detector and threshold/capacity policy → executed intervention and
uptake → state/artifact consequence → burden and stakeholder loss`. Exact-index,
window, and type agreement; detector performance; execution; utility; and decision
validity are different estimands. A grader cannot use the current action's resulting
observation to score a pre-action decision, and agreement to one unexplained reviewer
cannot substitute for authority, policy equivalence, or consequence evidence.

The Saturation Trap reproduces sparse-label disagreement on one 56-action successful
coding trace, but three under-specified annotators, a discarded/rebriefed pass, no
rationales or repeat labels, ambiguous pre/post-action indexing, no executed
intervention, and no outcome/loss prevent a general reliability claim. Its pinned
post-v1 release is valuable adverse audit evidence: the v1 replay hard-coded
`Δt=0`, so the reported state persistence is a zero-decay level-trigger result, not
evidence that a wall-clock-calibrated affect monitor structurally saturates. Existing
configured-system, trace/intervention, participation, task-health, metric, and
validity records host the repair; no timing or affect subsystem follows.

The internal [intervention-attribution replay](../pilots/intervention-attribution-rungs-v1/README.md)
crosses two builder-authored work shapes, six conditions, two equivalent forms, and
three frozen observer views in 24 retained attempts. It keeps one replay-diverged
cell invalid, preserves recovered and dual-fault cases, and deterministically shows
eight answer-bearing surface collapses where the full answer-withheld rule retains
upstream localization. This is local contract evidence only: complete valid cells
support paired-repair semantics, while earliest sufficient cause remains unsupported
and natural-failure root prohibited. It supplies no expert/professional validity,
auditor generalization, agent capability, safety, production, or readiness evidence.

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

MemOps sharpens this boundary with an event-type × probe-surface matrix and exact
user-turn evidence spans. Its pinned release also exposes the projection gap: the
2,558 authored operation rows contain triggers, targets, old/new values, validity,
and evidence, but no explicit scope or uniform before/after transition fields, and
the benchmark does not observe actual writes, deletes, retrieval candidates,
adoption, or consequences. Preserve expected projection, attempted operation,
realized store/workspace delta, evidence presentation, adoption, and consequence as
different records. Response non-disclosure is only the first rung of forgetting; it
does not establish active-store, replica, cache, log, or reconstruction deletion.

PASB adds the complementary **two-cut rule for durable-state claims**. An
execution cut must eliminate session history, scratchpads, caches, process state,
and worker leakage; a semantic cut must bind the tested proposition to an
attempted write, quiescent baseline-relative delta, exact evidence span, fresh
exposure, and later adoption. File presence supplies neither cut by itself. The
paper's committed/session-only +27-point association is post-treatment selection,
not a randomized write effect, and the released OpenClaw runner reuses the same
`pasb` session across persist and query. Its 336 compact episodes also lack full
attempt/judge/commit lineage, with 74 OpenClaw records using persist prompts that
differ from canonical release rows. Preserve reset attestation, write attempt,
realized delta, source/status/scope mutation, retrieval/presentation, adoption,
endpoint, and consequence separately; test matched state injection/removal rather
than promoting observational commit gaps into causal memory claims.

PM-Bench adds a complementary **prospective obligation → concurrent work**
boundary. Its near-paper release makes activation, cancellation/rescheduling,
dependencies, cue visibility, monitoring, due sets, lures, timing, and replayed
errors unusually inspectable. But the nominal ongoing activity is an arbitrary,
ungraded `A/B/C` advance token, so the reported score identifies obligation-menu
selection on one synthetic week—not dual-task interference, primary-work quality,
or operational utility. Future delayed-requirement slices must report obligation
reliability jointly with primary artifact/state quality, preservation, query/token/
time cost, collateral effects, and stakeholder-weighted consequences. Neutral
interrupts, channel hints, task reminders, and oracle cues are distinct evidence
interventions; none should be silently labeled an internal memory improvement.

Plans Don't Persist adds a distinct **plan-text → consequence identification
boundary**: `versioned obligation proposition → decision-time visible text and
derived restatements → matched content/position treatment → proposition-specific
recoverability → freely chosen action/adoption → realized artifact or state
consequence → context-policy cost/reliability`. Forced-prefix replay is useful
observer machinery because it holds actions and observations fixed, but for that
same reason it cannot measure whether the stripped condition would use the plan.
The reviewed paper's falling last-token cosine distance follows removal of the
entire guard/plan exchange and remains confounded by length, position, discourse,
and near-decodable step phase; its broad `keep_recent=4` stress test removes
working observations and actions as well as the plan. Directional compatibility
between those experiments does not supply the missing causal links. The strongest
reusable result is the reasoning-trace contamination warning: a nominally removed
treatment can survive in thoughts, summaries, rationales, tools, or memories.
Audit all derived views, atomize live/completed/superseded obligations, cross
irrelevant/corrupted/omitted/restored matched-capacity controls, and join forced
observer replay to separate free-action twins. Existing compression, obligation,
configured-system, trace, artifact/state, metric, task-health, and validity
contracts already host the repair; no plan-persistence schema follows.

The frozen internal [delayed-obligation dual-task pilot](../pilots/delayed-obligation-dual-task/README.md)
implements that repair on two purposive synthetic work shapes and three evidence
treatments. Frozen-component verification and exact replay passed; all six intended
single attempts were retained and service-, environment-, and artifact-valid. All
18 primary-turn checks passed, so the compact primary work is a ceiling rather than
evidence that monitoring has no interference cost. Four cells were exact successes.
The vendor neutral-interrupt cell encoded the original obligation but did not query
or access its replacement update, acted prematurely, and was classified cue-
monitoring/access failure; the vendor oracle-reminder cell received the update and
selected the current action but executed both original and replacement actions
prematurely, yielding a due-status/timing failure. The other cells cannot be pooled
with these or promoted into treatment effects: there is one attempt per shape-
condition cell, treatments change evidence availability, and the oracle reminder is
privileged evaluator-derived evidence—not an internal-memory aid. Agent self-report
fields also do not establish internal memory or causal adoption.

The prospectively frozen [v2 held-out extension](../pilots/delayed-obligation-heldout-v2/README.md)
completed the next machinery gate without establishing the wider construct. It
crossed two unseen forms in each of the same two purposive shapes with all three
conditions. All 12 intended attempts were retained and service-, environment-, and
artifact-valid, producing 36 turn artifacts. Exact outcomes were six successes,
three cue-monitoring/access failures, and three due-status/timing failures. Primary
work passed 35/36 turns. The sole wrong turn-1 decision under an oracle condition
shows that the primary grader can register concurrent loss, but 35/36 is still
near-ceiling and cannot estimate interference.

V2 improves observation rather than claim scope: the harness directly records query
issuance, next-turn channel availability, exact returned evidence, public due cues,
and oracle presentation. It does not observe encoding or adoption. Three of four
neutral attempts neither queried nor received the update; the fourth did both. All
four channel-hint attempts queried and received the update. All four oracle attempts
were exposed to privileged evaluator-derived update/due evidence regardless of the
query path, so oracle reminders remain evidence treatments, not memory aids. Do not
pool v1 with v2 or pool forms, shapes, or conditions within either study; every cell
has one attempt and no treatment effect is identified.

**Stop/continue decision:** do not run the same matrix again merely to add trials.
Continue only after independent or expert form/rubric review and a preregistered
repeated design that names its estimand, unit, cluster structure, contrast,
invalid/service policy, uncertainty method, and decision use. Otherwise stop at
bounded machinery validation. Existing contracts suffice, and the studies support
no internal-memory, general prospective-memory, causal-treatment, capability,
cross-domain, professional-validity, safety, production-fitness, or readiness
claim.

## 7. Task generation and evolution require conformance, provenance, and rollback

**Central insight:** Shared generated lineage does not guarantee that instructions, environment, witnesses, and checkers remain semantically aligned. Adaptive systems also confound initial ability, feedback exposure, task order, memory changes, retention, and safety drift.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [Anchor](../papers/agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md) | B | Motivates a task intermediate representation and bidirectional instruction/environment/witness/check conformance tests |
| [Agentic Context Engineering](../papers/agent-benchmarks/2026-07-10-agentic-context-engineering.md) | C | Shows the value of bounded context deltas while motivating provenance, contradiction, held-out promotion, and rollback controls |
| [Self-evolving agents survey](../papers/agent-benchmarks/2026-07-10-self-evolving-agents-survey.md) | C | Supplies a broad evolution taxonomy and highlights task-order, retention, cost, safety, and feedback confounds |
| [ClawArena](../papers/agent-benchmarks/2026-07-10-clawarena-evolving-information.md) | B | Provides persistent evidence and workspace updates while motivating typed corrections, retractions, supersession, and changed/unchanged checks |
| [LongMemEval-V2](../papers/agent-benchmarks/2026-07-11-longmemeval-v2-environment-experience-memory.md) | B | Separates trajectory-history storage from bounded evidence delivery and shows representation/reader effects; does not measure held-out action transfer or harmful stale guidance |
| [EvoMemBench](../papers/agent-benchmarks/2026-07-15-evomembench-memory-scope-content-validity.md) | B | Adds an in-/cross-episode × knowledge/execution organizing grid and broad adapter substrate while showing that scope/content labels do not identify one construct when task lineage, current-context necessity, write correctness, retrieval, endpoint, grader, missingness, and compute change together |
| [MemSyco-Bench](../papers/agent-benchmarks/2026-07-15-memsyco-memory-authority-validity.md) | B | Separates semantic relevance from decision authority through ignore/constrain/defer/supersede/use policies, while its synthetic labels, uncalibrated judge, missing adoption/action evidence, and nonfactorial families bound conclusions to configured answer behavior |
| [The Compliance Trap](../papers/agent-benchmarks/2026-07-16-compliance-trap-memory-consumption-validity.md) | B | Moves post-retrieval evaluation into action and consequence traces while showing that schedule effects, treatment-selected “compliance,” and baseline-action realignment do not identify proposition entry, dependency propagation, or accepted state repair |

**Repository consequence:** Projection manifests, candidate-lesson lifecycle, longitudinal stream/evolution contracts, immutable hashes, validation gates, and rollback. Experience-derived knowledge needs two linked, non-substitutable estimands: evidence-grounded retrospective retrieval and intervention benefit on held-out action. Failed attempts, realized procedures, inferred causes, environment/version scope, stale claims, safe alternatives, and harmful transfer must remain typed rather than flattened into notes.

EvoMemBench adds a necessary **memory-scope identification rule**: attach
`in-episode`, `cross-episode`, `knowledge`, and `execution` to a frozen
information-flow contract, not to a dataset name. Preserve current-context
sufficiency, reset/persistence, event authority, pre-grading write payload and
correctness status, retrieval query/budget, presented evidence, adoption,
action/answer consequence, observer view, invalid/missing rows, and full compute
as separate links. Cross reset and payload treatments on the same task family
where feasible; otherwise cell differences remain configured-suite interactions.
The audited evidence supports breadth and context-budget effects, not a common
self-evolving-memory score, cross-episode necessity, portable transfer,
professional capability, or readiness. The existing experience-memory-transfer
pilot and longitudinal/configured-system contracts already host the repair.

The internal experience-memory replay now makes that separation executable for one deterministic synthetic fixture: evidence-only memory answers retrospective QA correctly while producing harmful stale transfer, whereas provenance-gated promotion passes both QA and the planted held-out safety check ([replay](../pilots/experience-memory-transfer/replay-report.json)). This validates fixture and validator behavior, not the planted causal story, a general promotion policy, agent-memory improvement, professional competence, or deployment safety. Real validation requires unseen task families, repeated stochastic consumers, source-clustered uncertainty, rollback probes, and expert-grounded action consequences.

MemSyco-Bench adds a complementary **memory-authority rule**: retrieval relevance
does not determine whether historical information may act as factual evidence,
transfer across subjects or recipients, survive a superseding update, defeat a
stronger current source, or control a personalized choice. Preserve source and
represented-subject authority, purpose/recipient/scope, valid time and
supersession, admissible role and precedence, then observe
write → retrieval → presentation → adoption/rejection → action → consequence.
Its released 1,550-row policy suite and retrieved-but-wrong diagnostics make the
problem concrete, but GPT-5.5-assisted authored labels, no independent factual or
represented-user review, nonfactorial task families, a model judge without
calibration/repeats, conditional valid-call denominators, and no paper-run corpus
support only a synthetic configured-system stress-test claim. Existing
source-authority, information-flow, valid-time, experience-memory, state,
invalid-trial, grader, and validity contracts already host the repair; no
personal-assistant or memory-only scope commitment follows.

The Compliance Trap adds the next **opportunity-to-repair chain**:
`versioned prior experience and authority → delivered view/schedule → first actual
proposition-specific opportunity → access and interpretation → adoption/rejection/
deferral and action → induced state delta/reversibility → repeated re-entry or
dependency propagation → correction and repair opportunity → attempted versus
accepted repair → residual/collateral consequence → endpoint and cost`. No link
inherits the next. Report strict assignment/intention-to-treat package effects over
all intended eligible trials, retaining invalids, separately from descriptive
opportunity-, access-, adoption-, divergence-, correction-, and repair-conditioned
rates. A treatment-action-selected complier subset is not an all-task mediation
effect or common principal stratum.

The immutable v1 paper has no verified task, memory, trajectory, label, result, or
runnable-analysis release. Its uncalibrated observers, outcome-selected WebArena
pool, co-authored synthetic instrument, bundled Entry/Grounding treatments,
template clustering, one-run cells, and missing/retry denominator gaps license only
configured-package sensitivity to authored context—not an E–P–R mechanism, safety,
memory capability, professional validity, production fitness, or readiness. A
matched test should freeze the first actual opportunity on two unlike knowledge-
work actions with reversible versus irreversible consequences, cross no/helpful/
conflicting/irrelevant/stale/corrupted evidence before single versus persistent
delivery, and observe adoption, state propagation, accepted repair, residual state,
endpoint, invalidity, and cost. Existing experience-memory, evidence-flow, trace,
state, metric, task-health, and validity machinery suffices; no new schema follows.

These sources are important to the compounding system and adaptive-agent evaluation, but they must not make self-improvement the benchmark's primary objective.

## 8. Safety, contamination, and external validity constrain every result

**Central insight:** Realistic knowledge work includes untrusted content, changing sources, and action consequences. Safety and leakage are not optional score dimensions, and public benchmark artifacts can transition from capability evidence into calibration material after exposure.

| Source | Tier | Main contribution to skill-bench |
|---|---:|---|
| [ClawSafety](../papers/agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md) | C | Adds source-authority-to-action-consequence decomposition and warns against ASR without utility, severity, or released scoring contracts |
| [ToolPrivacyBench](../papers/agent-benchmarks/2026-07-16-toolprivacybench-purpose-bound-flow-validity.md) | B | Adds received-argument auditing for private atom × purpose/tool relations and free-text sinks while showing that a binary necessity matrix, detector-relative hit, and call-conditioned denominator do not establish purpose authority, recipient consequence, privacy compliance, or risk |
| [SafePro](../papers/agent-benchmarks/2026-07-14-safepro-professional-action-safety-validity.md) | B | Adds long file-bearing harmful professional-style tasks while showing that a judge which omits tool arguments, observations, and artifacts and maps non-completion to safety cannot support action, consequence, utility, or professional-safety claims |
| [Context-to-Execution Integrity](../papers/agent-benchmarks/2026-07-14-context-to-execution-integrity-action-authority.md) | B | Separates protected-field selection, sink-interpreted exact-effect, and invocation-event authority and binds all three to one manifest; zero observed mediated-gate escapes remains conditional on policy, validators, provenance, complete mediation, and observer coverage |
| [CAVA](../papers/agent-benchmarks/2026-07-17-cava-runtime-action-canonicalization-validity.md) | B | Makes cross-runtime semantic action identity explicit and inspectable, while its missing paper benchmark and executed open-core defects show that raw-event evidence, a versioned purpose-relative semantic projection, a freshness-bound authorization envelope, and observed effect evidence must remain separate |
| [Governance Decay](../papers/agent-benchmarks/2026-07-16-governance-decay-context-compaction-validity.md) | B | Makes lossy context management a time-varying governance treatment and supplies matched carriage/adoption probes, while its unreleased synthetic calls do not establish legitimate authority, realized harm, production safety, or readiness |
| [Refused in Chat, Written in Code](../papers/agent-benchmarks/2026-07-17-workflow-level-jailbreak-artifact-safety-validity.md) | B | Moves safety observation from chat replies into workflow-generated code/data, while nested prompt outputs in unreleased batch sessions and a bundled treatment support configured artifact-generation evidence—not an isolated mechanism, attack prevalence, realized harm, defense efficacy, or readiness |
| [Search-time contamination](../papers/agent-benchmarks/2026-07-10-search-time-contamination.md) | C | Shows why search exposure, exact source overlap, and post-release role changes must be recorded rather than treated as a universal causal inflation estimate |
| [LiveBench](../papers/agent-benchmarks/2026-07-11-livebench-contamination-limited-lifecycle.md) | B | Shows that recent sources and rolling private forms limit some direct exposure but do not prove contamination absence; source, exposure, instrument, and configured-system clocks must remain separate |
| [Agents' Last Exam](../papers/agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md) | A | Its post-paper split drift shows that a tier label is not suite identity; membership, outcome-selection, exposure, role transition, replacement bridge, and retirement must be versioned |
| [Workspace-Bench](../papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | A | Makes protected state, unauthorized mutation, and cleanup part of workspace validity |
| [Harness-Bench](../papers/agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | B | Contributes execution isolation and side-effect boundaries |

**Repository consequence:** Private-evidence firewalls, role transitions, safety/compliance checks, workspace mutation authorization, and environment-isolation tests. Rolling forms require four independent clocks—source availability, exposure/visibility, instrument version, and configured-system execution. Difficulty-conditioned replacement keeps challenge alive but changes the administered population; without frozen anchors or equivalent-form bridges, rank stability cannot license absolute capability trends. Grader repair creates linked new observations rather than rewriting historical scores. Context management is itself a time-varying configured treatment: bind each compaction event's input/output, operator, trigger/budget, retained/omitted claims, and decision-time evidence view to the authoritative policy version; keep carriage, semantic survival, adoption, admission, realized effect, and consequence separate. Workflow-level safety additionally requires an intent-assembly graph and honest nested units: preserve session → stage → turn → batch → prompt output → artifact delta → downstream consumption → proposal → admission → effect, and do not promote many strings from shared batch sessions into independent workflow trials. A pinned string neither authenticates a principal nor resolves revocation, precedence, or valid time. Safety observers must bind each verdict to decisive tool arguments, observations, native artifact/state views, and recipient effects; when those views are absent they must return insufficient evidence rather than convert non-completion, incapability, timeout, or empty output into safety. Keep justified refusal/escalation, safe alternative completion, over-refusal, invalid execution, unsafe attempt, policy interception, realized harm, recovery, and benign utility separate. At the proposal-to-execution boundary, preserve field-local authority, exact sink-interpreted effect authority, invocation capability, and their common manifest binding; gate acceptance proves neither validator correctness nor professional task quality, while zero observed gate escapes proves neither bypass closure nor universal safety. Purpose-bound flows additionally require `atom/source/subject × legitimate task use × authorized principal/purpose × minimum sufficient representation × actual recipient/sink/surface × received payload × storage/forwarding state × consequence`. A binary private-atom–tool necessity matrix is a useful conformance projection only after those authority and transformation links are warranted. Detector hits and repeated downstream occurrences must remain detector-relative transmission observations, not causal propagation or risk; call-conditioned opportunity rates must be stress-tested against redundant calls, omitted tools, and valid alternate paths. ToolPrivacyBench's immutable paper reports 2,150 cases, sampled pair-label κ=.86, nine agent rows, and rich sink/free-text/path diagnostics, but its official snapshot is only a 479-byte placeholder; the unavailable policies, detector, runs, and implementation block reproduction and all privacy-compliance, professional, safety, and readiness promotion. SafePro's paper-time release has useful authored task packages, but its 276 public rows do not match the 275-row paper suite, 208 reference files are unbundled/mutable, and no run corpus supports its configured-system rates or mitigations. The inert action-safety slice now separates placement, exposure, adoption, attempted and mock-realized action, recovery, residual harm, invalidity, and benign utility across eight synthetic cases with a passing static preflight. This is executable contract evidence only—not a live containment test, agent-capability result, expert validation, or deployment claim.

Workflow intent assembly sharpens the action-safety chain without replacing it.
**Assembly opportunity** records that a stage/state made a sensitive edge possible;
**realized assembly** requires a persistent delta, downstream availability or
consumption, and attributable continuation toward a proposal or effect. Refused in
Chat supports the narrower configured-artifact rung only: its 816 output rows may be
nested in undisclosed shared sessions, the multi-stage treatment is bundled, the
all-positive evaluator set does not calibrate specificity, empirical artifacts are
unreleased, and no consumer, action, harm, defense, benign-utility, or readiness
outcome is observed. A cross-domain test should preserve independent session and
output denominators, equal resource envelopes, frozen checkpoint ablations, mixed-
polarity observers, inert artifacts, synthetic recipients, mock admission/effect
receipts, utility, burden, and clustered uncertainty.

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
| [CentaurEval](../papers/agent-benchmarks/2026-07-17-centaureval-human-ai-collaboration-validity.md) | A | Adds real-participant human-only versus Copilot-assisted hidden-test endpoints and partial direct cost, while unmatched task forms/resource envelopes and absent contribution lineage separate team-package uplift from division of labor, complementarity, necessity, professional value, and readiness |
| [KINA](../papers/agent-benchmarks/2026-07-16-kina-incentive-representativeness-validity.md) | B | Supplies an explicit bonus-on-bar tournament and payoff assumptions while its bundled pay-plus-audit phase comparison and absent assignments, scores, payments, audits, appeals, attrition, and welfare block incentive-effect, contributor-benefit, affordability, and item-validity claims |

**Repository consequence:** Expert-participation contracts, contributor provenance/authority, measured recruitment and review burden, reciprocal outputs, and continued research into near-zero-cost incentives. Benchmark participants must additionally be typed by realization (`real_human`, model simulator, scripted policy, hybrid, or replay), independently of their assigned social role. Participation is a configured treatment vector—prompt, visible participants, channels/tools, information access, action authority, initiative, control threshold, budget, and observer—not an ordinal “agency level.” Preserve the chain `availability → exercise → uptake → effect`; a graph edge, trace event, apparent adoption, and matched outcome effect license different claims. Simulator steps/tokens do not estimate human active time, waiting, interruption, cognitive demand, correction work, privacy exposure, or accountability. HAS-Bench's 397 reported adaptations and scenario-review study support this vocabulary, but its model-backed users, bundled A1/A3/A4 treatments, single rollout per task, unreported process-judge audit, and unverifiable release block human-participation, simulator-parity, professional-collaboration, burden, and readiness claims.

Real-human participation sharpens rather than removes the identification requirement.
For every comparison, bind an immutable task form or validated equivalence block to a
matched information/tool/environment/feedback/time/token/call/retry/intervention
envelope, then join `contribution opportunity → exercise and authority → receipt →
semantic uptake/rejection → exact artifact/state consequence → independent
verification → outcome → burden and complete cost`. Keep team-package uplift,
division of labor, complementarity, necessity, professional value, and readiness as
non-inheriting claim rungs. CentaurEval's paper-reported 17/90 versus 28/90
human-only/team hidden-test passes are meaningful evidence for one selected
participant/Copilot package, not the later rungs: dynamic forms differ across arms,
autonomous conditions use a different static set and execution envelope, assignment
and trace releases are unavailable, clustering and result definitions are not fully
auditable, and no contribution ablation exists. Treat model-relative collaboration
necessity as a versioned task-health role. Validation should cross human-only,
agent-only, team, and selected frozen-state both/neither/component replays over
unlike work shapes while measuring active/wait/review/correction burden, cost,
invalidity, and clustered endpoints.

Formal incentive claims add a separate treatment chain: `mechanism assumptions →
implementation witness → realized assignment/pay/audit/appeal events → effort and
burden → independent contribution quality → benchmark validity`. KINA improves on
ELAIPBench at the theoretical rung by specifying effort costs, score noise, winning
probabilities, and a bonus threshold; ELAIPBench supplies a realized writer–verifier
contest but no formal game or fixed-pay contrast. Neither releases evidence sufficient
to identify an incentive effect or contributor welfare. KINA's observed comparison
changes tournament, bonus, audit regime, and time together, so audit cannot serve as
both hidden treatment and validating outcome authority. A fixed-audit real-participant
comparison remains gated by the pending consented micro-pilot; do not simulate
contributors or treat fixtures as participation evidence.

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
