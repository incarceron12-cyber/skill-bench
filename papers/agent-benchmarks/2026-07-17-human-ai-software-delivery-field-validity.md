# Chiron field study: complete-looking tables do not identify longitudinal workflow value

## Bottom line

Armesto and Kolb report an unusually legible fifteen-cell table for three software-modernization programs under a traditional configuration and four successive Chiron configurations. The paper correctly separates recorded stage duration, backlog size, validation-stage issues, and first-release coverage from scenario-derived person-days and senior-equivalent effort. Its most useful empirical pattern is that the early agentic configurations V1–V2 are faster but worse on the paper's downstream issue and coverage measures, while V3–V4 add task-centric orchestration, acceptance-criteria validation, repository-native review, and hybrid execution and improve all reported measures.

That pattern is descriptive evidence from one vendor's reconstructed internal record, not an estimate of orchestration value. The paper never establishes what a project-version cell physically is: whether the same modernization was replayed five times, whether cells are estimates reconstructed from one delivery, whether versions were applied to different slices, or how traditional and successive configurations map to calendar time. It gives no dates, stage-event definitions, contemporaneous records, cell-level source provenance, actual staffing or utilization, requirement denominators, raw artifacts, task/issue lineage, adjudicators, customer acceptance records, post-release outcomes, or analysis release. Platform version, model/prompt/tool changes, organizational learning, project mix, workflow maturity, and calendar time are therefore inseparable.

The paper's arithmetic is reproducible from the printed tables, but its estimands are much weaker than the headline. “36.0 to 9.3 weeks” is a sum of three project durations, not a concurrent portfolio makespan. Person-days assume every nominal team member works full-time through the summed stage duration. Senior-equivalent effort additionally counts all six traditional roles as one senior equivalent but four explicitly junior agentic roles as one-half each. The 74.0% issue-load reduction combines a 52.5% reduction in raw validation issues with an 82.8% increase in task count under non-equivalent backlog granularity. Task-weighted coverage weights requirement-completion percentages by task counts, although task count is neither the reported requirement denominator nor stable under the intervention.

For `skill-bench`, the distinctive transfer is a **workflow-value evidence ladder** that keeps event telemetry, derived rates, scenario models, accepted outcomes, and causal comparisons separate. A benchmark package score or shorter stage trace cannot become a productivity, staffing, economic-value, defect-reduction, production-fitness, or readiness claim without explicit unit lineage, denominator invariance, actual resource exposure, external acceptance/consequence evidence, and a comparison that separates configuration from time and learning.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, and E through a bounded production-validity case. Software modernization is the field setting, not a scope commitment. The reusable question is general:

> When an evolving human-agent workflow appears faster and better across successive internal configurations, what evidence distinguishes observed events, transformed metrics, staffing scenarios, accepted work, and causal workflow value?

- **Concrete evidence:** complete immutable arXiv v1 PDF/text and appendix tables, exact arithmetic replay, and an audit of the official current Chiron product page and release search.
- **Uncertainty clarified:** whether whole-workflow field records license duration, quality, effort, productivity, economic-value, or orchestration-effect claims.
- **Mode:** expansion with validation and human-learning implications.
- **Duplication check:** AlphaEval studies production-demand projection; Nubank links selected offline variants to live metrics; criterion-validity work studies score–outcome association; MAP and the oversight study provide self-reported practice. Chiron uniquely mixes complete-looking project-stage tables with retrospective recall and scenario-modeled labor across nonconcurrent platform versions.
- **Useful completion:** preserve the observed-versus-modeled distinction and the early speed/quality trade-off, while defining why neither table completeness nor monotonic version progress identifies production value.

## Sources and reading record

**Deep review of the complete immutable primary source.** I read the full 18-page v1 paper, including all four figures, twelve tables, complete project-version appendix, sensitivity analyses, conflict disclosure, and references.

- Maximiliano Armesto and Christophe Kolb, *Orchestrating Human-AI Software Delivery: A Retrospective Longitudinal Field Study of Three Software Modernization Programs*.
- Immutable arXiv v1: <https://arxiv.org/abs/2603.20028v1>, submitted 20 March 2026. The retained API metadata contains one normal entry and no withdrawal/retraction notice.
- Local PDF: `data/papers/pdfs/2603.20028v1-orchestrating-human-ai-software-delivery.pdf` (18 pages, 627,273 bytes; SHA-256 `ef0d8463b19b1a5912c1d1fe0e4467affe9cd841889d5dc97905fde7736ef75b`).
- Full layout-preserving text: `data/papers/text/2603.20028v1-orchestrating-human-ai-software-delivery.txt` (48,437 bytes; SHA-256 `34d6e38778c63981a1719f32c137013c93b3aa15297c39c2db83f3ed58bc4ea5`).
- Metadata: `data/papers/source/2603.20028v1-metadata.xml` (SHA-256 `cf1b598f35c0ab925c62807ad44db460a7c1624ab44f3092e7b2cd1b3a280cec`).

The current official Chiron product page, <https://www.tallertechnologies.com/chiron>, describes a commercial execution platform with an agent control plane, shared ontology/knowledge graph, dependency-mapped planning, task-board execution, testing, and repository/workflow integrations. The company research index links the paper. These pages corroborate that Taller markets a platform named Chiron and describe current product concepts; they do **not** identify the V1–V4 study builds, models, projects, dates, records, or results. Exact-title, arXiv-ID, GitHub, Zenodo, OSF, and Hugging Face searches found no verifiable author/company empirical dataset, analysis package, task/issue ledger, version manifest, or replication release. Search snippets and current marketing copy are not treated as result evidence.

## One-sentence contribution

The paper usefully distinguishes recorded delivery measures from scenario-derived labor estimates and reports a coherent speed-first-to-orchestrated-quality trajectory across three internal modernization cases, but absent cell identity, calendar assignment, provenance, denominator equivalence, actual labor, external outcome, and counterfactual evidence bounds it to a vendor-authored retrospective table—not a causal or economic evaluation of human-agent orchestration.

## Research questions and claim boundary

The paper asks how measured durations change across configurations, how validation issues and first-release coverage change, what staffing scenarios imply for effort, and which platform changes are most plausibly associated with the largest gains (paper pp. 4–5; extraction lines 175–200).

The strongest defensible claim is:

> Within one organization's retrospectively compiled fifteen-cell benchmark, all three named modernization cases have lower tabulated four-stage duration, lower validation-issue count per recorded backlog task, and higher tabulated first-release coverage under V4 than under the traditional and V1 configurations; the authors associate the V3–V4 period with broader task-centric orchestration, acceptance-criteria validation, repository-native review, and hybrid execution.

The evidence does **not** establish:

- that all fifteen cells are independent observed deliveries rather than reconstructed or modeled comparisons;
- elapsed portfolio makespan, actual labor hours, utilization, labor substitution, cost, or economic value;
- intrinsic defect reduction, total defect reduction, maintainability, security, performance, post-release reliability, or lifecycle quality;
- requirement-completion comparability across versions;
- causal benefit of orchestration, acceptance criteria, review, hybrid staffing, agents, a model, or any component;
- general software-delivery capability, professional equivalence, cross-domain transfer, safety, production fitness, or readiness.

## Methodology and system

### Chiron versions are compound configurations

Chiron spans repository ingestion, technology/business-logic analysis, documentation synthesis, backlog generation, human/agent assignment, acceptance-criteria validation, pull requests, and repository-native review (pp. 3–4; lines 102–147). The reported evolution is:

- **V1:** tool-centric repository analysis, migration documentation, backlog generation, autonomous task execution, and limited integrated validation/review;
- **V2:** CLI-orchestrated context preparation, implementation, and validation;
- **V3:** shared web workspace, brainstorming, task board, automatic task pickup, and first-generation acceptance-criteria validation;
- **V4:** repository authentication, branch/PR workflows, review, document ingestion, monitoring, and hybrid execution.

This is a valuable configured-system framing. It is also a compound treatment. No model names, versions, prompts, tool versions, retrieval/context policy, task-routing policy, autonomy limits, human decision rights, validation implementation, review rubric, branch policy, compute budget, failure/retry policy, or component hashes are reported. The paper explicitly says versions combine architecture, workflow redesign, and organizational learning (p. 3). It cannot attribute changes to orchestration as opposed to any bundled component or maturation process.

The present-day product page adds claims about a control plane, organizational ontology, dependency mapping, testing, and autonomous task-board work. It does not establish that those current features existed in V4, were exercised in the three cases, or generated the printed outcomes. Current product realization and historical study realization must remain separate.

### Three programs, fifteen cells, but no cell ontology

The cases are a roughly 30k-LOC COBOL banking migration, roughly 400k-LOC accounting modernization, and roughly 30k-LOC .NET/Angular mortgage modernization (p. 4). The paper defines the unit as a project-version cell and says the complete dataset contains 15 cells (p. 5).

That formal definition hides the study's largest missing fact. The paper never says:

- whether each project was actually executed five times;
- whether V1–V4 were historical phases over different modules or work packages;
- whether the traditional cells are historical projects and later cells are counterfactual reconstructions;
- whether all stages refer to one release, a replay, estimates from records, or practitioner forecasts;
- when each cell started/ended, which versions were concurrent, or whether project scope stayed fixed;
- which people, models, codebase snapshots, requirement sets, or environments belong to each cell.

A modernization normally changes its codebase after one execution, so repeated project labels do not by themselves imply equivalent repeat units. Without assignment and lineage, “longitudinal” means ordered platform labels—not an auditable time series. Platform version, calendar time, staff learning, changing source state, project/module selection, model progress, and workflow refinement cannot be separated.

### Provenance is acknowledged but not repaired

The benchmark was compiled from engineering records and practitioner recall; the source manuscript lacked a cell-level provenance matrix (p. 5; lines 202–218). The authors responsibly tell readers to use a conservative interpretation. Yet labeling stage durations, tasks, issues, and coverage “observed” still outruns the disclosed lineage. A quantity partly reconstructed from memory can be a recorded retrospective value, but its source type, capture time, estimator, uncertainty, and adjudication must be known before it is treated as event telemetry.

The paper supplies no raw ticket IDs, timestamps, repository commits, requirements, acceptance decisions, issue records, staff calendars, version logs, or source-specific confidence. All 15 cells are complete; no missing measurement or imputation is reported despite heterogeneous retrospective sources. Values are coarse—durations mostly to 0.1 weeks, coverages to five percentage points, tasks often identical across all agentic versions—but no rounding or reconstruction protocol is given. This does not prove the values are wrong; it prevents an audit of what each number represents.

### Stage duration is not yet cycle-time telemetry

Four stages—analysis, planning, implementation, validation—are summed, while deployment is excluded because it is not consistently represented (pp. 5–6). The paper does not define start/stop events, overlap, waiting/blocked time, rework attribution, pauses, parallel work, acceptance, canceled scope, or censoring. Summing stages assumes a sequential additive path, but no trace shows that assumption.

The portfolio “weeks” total is explicitly the sum of three project durations, not literal concurrent makespan (p. 7). The paper nevertheless calls `36.0/9.3 = 3.87×` a portfolio speedup. The arithmetic is exact, but the estimand is **summed tabulated stage duration over three labeled cases**. It is not calendar time to deliver a three-project portfolio, throughput under a fixed resource pool, or person-time.

Deployment's exclusion also matters asymmetrically. V4 adds branch/PR/repository integration and may shift effort or defects across review, validation, release, and post-release boundaries. A stage-local reduction can reflect boundary movement rather than total lifecycle compression.

### Task and issue denominators drift under the intervention

The issue measure is validation-stage issues per 100 recorded tasks. The paper correctly warns that it is an escape-to-validation measure, not defect density (pp. 6, 9, 13). Exact replay of Tables 6–9 gives:

| Configuration | Tasks | Validation issues | Issues / 100 tasks |
|---|---:|---:|---:|
| Traditional | 3,200 | 257 | 8.031 |
| V1 | 5,850 | 505 | 8.632 |
| V2 | 5,850 | 478 | 8.171 |
| V3 | 5,850 | 245 | 4.188 |
| V4 | 5,850 | 122 | 2.085 |

From traditional to V4, raw validation issues fall 52.5%, while task count rises 82.8%; together those changes yield the reported 74.0% rate reduction. Because agentic configurations intentionally create more granular backlogs, the denominator is post-treatment and tasks are not semantically equivalent. A task split into two can lower issues-per-task without changing delivered requirements or defects. The V1-to-V4 comparison is less vulnerable to this particular artifact because each project's task count is fixed across V1–V4, but issue definition, scope, detection, and stage routing remain unvalidated.

V4's reported review containment uses approximate pre-validation issue counts of 40, 188, and 23, with 20, 90, and 12 reaching validation, yielding about 51.4% pooled containment (pp. 10–11). This supports only a recorded stage-routing description. There is no issue identity ledger showing creation, detection, duplicate policy, severity, validity, repair, regression, or post-release escape. Earlier configurations lack comparable review-stage counts. Lower validation escape can reflect earlier detection—which is operationally useful—but cannot establish fewer defects created or better final software.

### Coverage has an unobserved denominator and an invalid size proxy

First-release coverage is defined as the fraction of first-release requirements “recorded as completed and accepted at initial handoff” (p. 6). The paper does not report requirement counts, requirement identity/version, scope changes, acceptance authority, evidence, partial credit, rejected work, denominator freeze, or handoff date. Coverage can rise because execution improves, requirements are rescoped, acceptance changes, or difficult items move out of “first release.”

Portfolio coverage weights each project's coverage by **task count**, not requirement count. Task count is intervention-sensitive and not the declared denominator of coverage. The stated rationale is to avoid treating 400k and 30k LOC programs equally, but backlog tasks are not a validated size or consequence weight either. Exact replay gives 77.03% traditional and 90.47% V4 under task weights, versus 81.67% and 91.67% under equal project weights. Neither aggregation is inherently correct; the difference shows that the +13.4-point headline embeds an unvalidated policy weight. A valid aggregate needs requirement/opportunity counts or a declared stakeholder/consequence weighting, plus frozen scope and uncertainty.

### Effort is a scenario transformation, not labor observation

Raw effort is `5 × nominal headcount × summed duration`: six people for the traditional scenario and five for every agentic scenario. This assumes every nominal team member works full-time through all summed stage weeks. There are no time sheets, utilization records, stage-specific role allocations, concurrent work, leave, meetings, agent compute/cost, human review/rework, or staffing actually realized. The reported 1,080 to 232.5 person-days is therefore duration multiplied by a staffing constant, not measured effort.

Senior-equivalent effort adds a stronger policy assumption. The traditional team—one architect, two backend, one frontend, and two QA—is counted as six senior equivalents, although seniority is not given. The agentic team—one senior architect plus four explicitly junior operators/QA—is counted as three senior equivalents under a 0.5 junior weight. Thus `1,080 → 139.5 SEE-days` combines shorter tabulated duration with asymmetric role valuation. The sensitivity table varies only the junior weight; it keeps all traditional roles at 1.0, assumes full utilization, and does not vary actual staffing, wage, productivity, review burden, or role substitution. Calling 0.25–1.0 “reasonable” is a modeling judgment, not empirical validation.

Even the V1-to-V4 comparison, where nominal staffing is fixed, supports only a proportional scenario transformation of the same duration table. It does not establish labor savings because no actual labor exposure is observed.

## Evidence: what survives

### Supported or useful descriptive evidence

1. The printed project tables are arithmetically coherent with the portfolio duration, task, issue-load, coverage, raw-effort, and baseline SEE calculations.
2. Under the paper's recorded values, all three projects show the same broad trajectory: early speed compression with worse V1/V2 downstream measures, followed by better V3/V4 duration, escape load, and coverage.
3. The paper explicitly distinguishes recorded variables from modeled staffing scenarios and discloses that the data mix engineering records with recall.
4. The V1-to-V4 contrast holds the nominal staffing scenario and task counts fixed, so it is descriptively cleaner than traditional-to-V4 for those two transformations.
5. The paper correctly identifies staged defect observation, denominator drift, post-release omission, single-organization scope, bundled evolution, and conflict of interest as major limitations.
6. Both authors disclose executive roles at the company that developed Chiron and state that no independent audit or blinded adjudication occurred (p. 14).

### Partially supported

- **Workflow maturation pattern:** temporally ordered labels and monotonic tables are consistent with maturation, but dates, component manifests, cell realization, and alternative explanations are absent.
- **Earlier containment in V4:** approximate counts are consistent with issue movement from validation to review, but issue lineage and cross-version review observations are absent.
- **First-release improvement:** recorded coverage rises, but requirement scope, denominator, authority, and weighting are unknown.
- **Lower scenario burden:** formulas are transparent under assumptions, but no actual labor, cost, or utilization is measured.

### Not supported

- a causal orchestration effect or component effect;
- a 3.87× real portfolio delivery speedup under comparable work and resources;
- 78.5% labor savings or 87.1% senior-equivalent productivity improvement;
- 74.0% total-defect reduction or improved intrinsic software quality;
- economic value, workforce substitution, or cost effectiveness;
- post-release reliability, maintainability, security, customer benefit, or total lifecycle value;
- representative software-delivery capability, professional equivalence, cross-domain transfer, safety, production fitness, or readiness.

## Unique insight: workflow value needs typed transformations and bridge units

The paper's strongest transfer is not “orchestration beats local agents.” It is a warning that an internally coherent workflow table can silently combine five evidence types:

```text
configured workflow version and actual exposure
→ timestamped native events and artifact/state transitions
→ derived stage/rate/coverage measures with stable opportunities
→ staffing, skill, cost, or economic scenario transformations
→ accepted downstream and post-release consequences
→ comparative or causal workflow-value claim
```

Each arrow requires a bridge record.

1. **Realization bridge:** exact component versions, users/agents, code/source state, permissions, task scope, calendar window, and evidence that the configured workflow operated.
2. **Event bridge:** authoritative start/stop/state events, overlap and waiting policy, issue/requirement lineage, missingness, and source provenance.
3. **Denominator bridge:** invariant or mapped opportunities across task decomposition, requirement scope, stage routing, and project weighting.
4. **Resource bridge:** actual role exposure, utilization, human review/rework, agent compute/cost, latency, and shared resources—not headcount multiplied by elapsed time.
5. **Consequence bridge:** independent acceptance, rework, post-release defects, reversals, incidents, maintainability, stakeholder outcome, and observation horizon.
6. **Counterfactual bridge:** concurrent or otherwise credible assignment, stable scope, frozen outcomes, project/time controls, repeated units, uncertainty, and predeclared analysis.

A result can stop legitimately at any rung. Stage telemetry can support a duration description; a denominator-valid rate can support a bounded escape-rate claim; an explicit model can support a scenario estimate. None inherits the validity of the next rung.

This also clarifies **bridge units**. Comparing configurations requires stable identities or explicit mappings for requirements, work packages, issues, source snapshots, stages, roles, and consequence opportunities. “Same project name” and “same task count” are not sufficient bridge evidence. When the intervention recomposes work, the benchmark should preserve both the native intervention-defined units and a frozen external unit such as requirement, accepted capability, defect opportunity, or downstream decision.

## Comparison with adjacent reviewed evidence

- **AlphaEval** has stronger prospective production-demand engagement and task packaging but private transformation history and no live consequence evidence. Chiron has whole-workflow outcome-like tables but weaker cell provenance and no task projection ledger. Together they show that production origin and complete tables are independent of transformation validity.
- **Nubank** reports selected live customer metric deltas and an adaptive candidate genealogy but lacks assignment, denominators, uncertainty, and component isolation. Chiron lacks even the online assignment/calendar layer and transforms duration directly into labor scenarios. Both require exact candidate/version lineage and prospective or concurrent comparisons before workflow-value claims.
- **Criterion validity against business outcomes** reaches an external payment-linked label but cannot infer judge validity, prediction, or intervention effect. Chiron's first-release coverage is closer to an internally adjudicated release proxy and has no released acceptance or post-release outcome. A rubric/stage metric and a consequential external criterion must remain separate.
- **Measuring Agents in Production** maps selected practitioner reports while measuring no realized systems or outcomes. Chiron moves one rung toward internal project records, but unknown cell ontology and mixed recall mean it still cannot identify which practice produced success. Practice report, realization, event telemetry, derived metric, and outcome need distinct evidence.
- **Human oversight in practice** shows that co-planning, monitoring, and review are human labor and configured interventions. Chiron's nominal five-person scenario contains none of the actual specification, review, restart, adjudication, or rework burden needed to value a hybrid package. Human presence in a staffing list is not measured human effort.

## Limitations and validity threats

1. Only three purposively available projects from one company and platform family are included.
2. Project selection, attempted-project denominator, exclusions, failures, cancellations, and survivorship are not reported.
3. The physical meaning of each of the fifteen project-version cells is unspecified.
4. No calendar dates, assignment, concurrency, repeated-delivery, module allocation, or source-snapshot lineage is given.
5. Repeated project names do not establish equivalent work after a modernization changes the codebase.
6. Traditional, V1–V4, model progress, workflow maturation, organizational learning, staffing behavior, and calendar time are inseparable.
7. Version labels are compound packages, not isolated interventions.
8. Models, prompts, tools, context, permissions, validation, review, routing, and feedback policies are unversioned.
9. Current Chiron marketing cannot be used as evidence of historical V4 realization.
10. Records and practitioner recall are pooled without a cell/field provenance matrix.
11. No raw records, timestamps, repository states, tickets, requirements, acceptance records, or issue ledgers are released.
12. No reconstruction protocol, recorder identity, adjudication, confidence, or uncertainty is reported.
13. Complete coarse tables contain no disclosed missingness, imputation, or rounding policy.
14. Stage boundaries, overlap, waiting, blocked time, rework, pauses, scope removal, and censoring are undefined.
15. Summing stage durations assumes additivity and does not establish elapsed portfolio makespan.
16. Deployment is excluded inconsistently and can absorb shifted effort or defects.
17. No fixed resource pool or throughput model supports a portfolio productivity interpretation.
18. Task granularity changes under the intervention; tasks are not equivalent opportunities.
19. The 74.0% issue-load reduction combines raw issue decline with a larger post-treatment denominator.
20. Issue identity, severity, duplicate policy, validity, creation stage, detection, repair, regression, and post-release escape are absent.
21. V4 review containment is approximate and has no comparable earlier-version review ledger.
22. Validation-stage issues are not total defects or intrinsic quality.
23. Requirement counts, identities, versions, scope changes, and acceptance authorities are absent.
24. First-release coverage can change through scope or adjudication rather than delivery quality.
25. Task-weighted requirement coverage uses an intervention-sensitive proxy unrelated to the declared requirement denominator.
26. Equal project, LOC, task, requirement, value, and consequence weighting answer different questions; no aggregation policy is validated.
27. Raw person-days are nominal headcount × duration, not labor logs.
28. Full-time utilization, stage-specific role allocation, parallelism, shared work, meetings, and absence are assumed away.
29. Agent compute, service cost, latency, human oversight, rework, and integration burden are omitted.
30. Traditional headcount differs from agentic headcount, so the traditional-to-V4 raw-effort ratio combines two assumptions.
31. Traditional non-architect roles are counted as full senior equivalents without reported seniority.
32. The junior-weight sensitivity does not vary the asymmetric traditional-role assumption or actual utilization.
33. Leave-one-project-out analysis over three selected cases does not address selection, measurement, or serial dependence.
34. No repeats, uncertainty intervals, measurement error, model-based sensitivity, or negative-control outcome is provided.
35. Same-direction changes across three cases may reflect common reconstruction, version, calendar, or organizational factors.
36. No external recipient independently validates acceptance, quality, usefulness, or project completion.
37. No post-release defect, incident, rollback, security, maintainability, performance, customer, or lifecycle-cost outcome is measured.
38. No failed or abandoned platform version/project denominator is reported.
39. Both authors are executives at the vendor; no independent audit or blinded adjudication occurred.
40. The empirical release is absent, so no central statistic, lineage claim, or comparison is independently replayable beyond printed-table arithmetic.

## Reproducibility and operational realism

**Arithmetic reproducibility is high.** The complete appendix allows exact reconstruction of portfolio duration, modeled effort, pooled issue load, and task-weighted coverage. The paper clearly states its formulas and exposes project-level cells rather than only headline percentages.

**Empirical reproducibility is very low.** No cell source, raw event, requirement, task/issue mapping, staffing exposure, version manifest, analysis code, or output package is available. A third party can verify multiplication and division, not that the inputs were observed, comparable, complete, or correctly interpreted.

**Operational realism is potentially high but evidentially opaque.** The named projects, legacy technologies, staged workflow, repository-native review, human-agent team, acceptance criteria, and first release are much closer to consequential delivery than a coding puzzle. Yet realism claims require inspectable realization. Here the operational substrate is private, reconstructed, and temporally unspecified. The correct evidence status is a conflict-disclosed industrial retrospective with transparent table arithmetic and severe provenance/comparison limits—not a benchmark release, controlled field experiment, productivity estimate, or production-readiness study.

## Transfer to `skill-bench`

### Retain

1. Separate native observed/recorded measures from derived rates and staffing/economic scenarios.
2. Measure full workflows by stages and preserve where defects or corrections are detected rather than only final completion.
3. Keep early speed gains and downstream quality/coverage trade-offs visible; do not optimize time alone.
4. Compare mature orchestration with both a non-agentic workflow and an early tool-centric agent workflow when the units are valid.
5. Preserve project-level trajectories instead of reporting only a pooled endpoint.
6. Disclose vendor/researcher positionality and use independent adjudication where claims affect product value.

### Repair

7. Define every trial/field cell through source snapshot, requirement set, work-package lineage, calendar window, configuration hashes, people/agents, permissions, stage events, and actual exposure.
8. Type provenance per field: contemporaneous telemetry, durable artifact, manual annotation, retrospective record, practitioner reconstruction, or scenario assumption; retain recorder, locator, timestamp, uncertainty, and adjudication.
9. Use frozen external bridge units when the workflow recomposes tasks: requirements, accepted capabilities, defect opportunities, downstream decisions, or stakeholder-weighted consequences.
10. Report both raw counts and rates. Decompose a rate change into numerator and denominator changes and reject semantic-equivalence claims without a mapping audit.
11. Treat coverage as requirement-level evidence with frozen denominator, scope-change ledger, acceptance authority, accepted alternatives, and unresolved/rejected items.
12. Observe actual human and agent resource use: role-time, active/idle/waiting, review, correction, restart, compute, latency, cost, and downstream rework.
13. Keep scenario models versioned and sensitivity-tested, but label them as transformations; never call headcount × elapsed time measured productivity.
14. Add post-handoff outcomes appropriate to the claim: acceptance, rework, reversal, incidents, defects by stage/severity, maintainability, customer use, and observation horizon.
15. For orchestration effects, use concurrent assignment or another credible design over equivalent work, frozen outcomes, repeated project/task families, component manifests, clustered uncertainty, and negative-result accounting.
16. Where randomized field comparison is infeasible, use interrupted time series, staggered rollout, matched work packages, synthetic controls, or bridge-item repeats—but preserve assumptions and keep causal ceilings explicit.
17. Keep component effects below package effects unless a designed ablation separates orchestration, validation, review, model, prompt, tools, staffing, and learning.

### A minimal workflow-value validation episode

A cross-domain pilot should link existing repository contracts rather than add a software-delivery schema:

```text
immutable task/work package + configured workflow + calendar/exposure record
→ authoritative stage events and native artifact/state observations
→ frozen requirement/defect/consequence opportunities
→ raw numerator/denominator measures and missingness
→ actual human/agent resource ledger
→ independently accepted outcome and delayed consequences
→ matched comparator, uncertainty, and validity argument
→ licensed description, association, package effect, or decision claim
```

Use at least one non-code professional artifact/workflow before claiming cross-domain generality. The purpose is to test whether existing configured-system, trace, artifact/state, metric-monitoring, task-health, validity, participation, cost, and production-validation records can reject the exact failures in this paper: unknown cell identity, post-treatment denominator, scenario labor laundering, internal acceptance proxy, and time/configuration confounding.

## Concrete repository actions

- Added this deep review and updated the paper index from source-acquired/review-pending to deep-review complete.
- Added the review to `papers/topic-index.md` under realistic knowledge work / production validity.
- No new build or consolidation task is added. Existing configured-system, execution-validity, task-health, metric-monitoring, validity-argument, longitudinal, production-validation, artifact/state, participation, and cost machinery already has homes for every requirement. The missing contribution is empirical exercise of those records, not another delivery-specific contract.
- The canonical synthesis need not change: this paper strengthens the existing conclusion that production provenance, telemetry, transformed metrics, outcome validity, and causal workflow value are separate rungs. It does not overturn a grouped conclusion or establish a new benchmark family tier.

## Assessment

- **Evidence tier:** B-/C+ enabling evidence—complete immutable paper and transparent table formulas, real internal program claims, explicit limitations and conflict disclosure; no cell ontology, raw evidence, release, actual labor, external outcomes, or credible counterfactual.
- **Most reusable contribution:** the explicit observed/derived/modeled distinction and the speed-first V1/V2 versus speed-plus-downstream-measure V3/V4 trajectory.
- **Strongest evidence:** printed values are internally coherent and same-direction across all three named cases under V4.
- **Most serious methodological flaw:** the paper defines fifteen project-version cells mathematically without explaining how those cells existed in time or how equivalent work was assigned, observed, and sourced.
- **Most serious measurement flaw:** intervention-sensitive tasks are used to normalize issues and weight requirement coverage, while nominal headcount × duration is promoted into person-day and senior-equivalent scenarios.
- **Safe claim:** one vendor's retrospective internal tables report lower summed four-stage duration, lower validation issues per recorded task, and higher first-release coverage for three named modernization cases under V4 than under traditional/V1 configurations. The evidence does not establish causal orchestration benefit, defect reduction, actual productivity or cost, economic value, professional capability, cross-domain transfer, production fitness, safety, or readiness.
