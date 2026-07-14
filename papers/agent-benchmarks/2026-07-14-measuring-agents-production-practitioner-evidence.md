# MAP: practitioner reports describe selected deployment practice, not what makes agents successful

## Bottom line

*Measuring Agents in Production* (MAP) supplies unusually useful primary descriptive evidence about how selected teams say they build and evaluate agent systems. Its combination of 20 confidential interview cases, a 306-response public survey frame, a clearly identified 86-response production-or-pilot subset, question-specific denominators, and a released 47-question instrument is stronger than an unauditable industry trend report. The most relevant observations for `skill-bench` are that respondents commonly describe bounded workflows, human verification, proprietary and sensitive data, weak benchmark availability, delayed outcome signals, and heterogeneous human/software baselines.

The paper's causal language is not supported by its design. MAP deliberately recruits deployed cases, calls production and pilot systems “successful,” asks respondents mainly about one familiar or most-developed system, and never audits system outcomes. It therefore does not identify technical methods that **enable success**. The survey's headline population also needs care: 306 valid responses were collected, only 111 report deployment stage in the displayed accounting, and the main production/pilot frame consists of 86 responses; individual findings use optional-question denominators from 22 to 69. The v4 abstract's “86 deployed systems practitioners” is clearer than v3's “306 practitioners,” but neither phrase establishes 86 unique practitioners, systems, organizations, or independent deployments.

The strongest transferable insight is a measurement boundary:

> **Reported production practice is authoring and portfolio evidence; practice prevalence is not practice efficacy, reliability, professional validity, or readiness.**

A knowledge-work benchmark should use MAP to ask which workflow conditions and evaluation gaps deserve coverage, then independently establish task provenance, configured-system behavior, artifact/state quality, human burden, downstream acceptance, consequences, and reliability.

## Why this matters: charter relevance and research question

This review advances charter objectives A, B, D, and E through cross-domain production-evaluation evidence. It does not narrow `skill-bench` to enterprise deployment or treat common current practice as a benchmark target.

MAP asks four descriptive questions: what agents are used for, which models/architectures/methods teams use, how teams evaluate them, and what deployment challenges they report (paper pp. 1–3). Its introduction additionally asks what enables “successful agent deployment” and interprets simple, controllable system design as the answer (pp. 1–2, 8–9).

The auditable question is narrower:

> Among 20 purposively recruited production/pilot interview cases and question-specific subsets of a network-recruited 306-response survey, what practices, application attributes, evaluation methods, and priority categories did respondents report from April–November 2025?

That descriptive question is valuable. The study does not compare successful with failed systems, one practice with another under matched conditions, or reported practice with audited behavior and outcomes.

## Sources and reading record

### Immutable primary paper read in full

- Melissa Z. Pan et al., *Measuring Agents in Production*, ICML 2026 oral, PMLR 306.
- Immutable record: <https://arxiv.org/abs/2512.04123v4>
- Immutable PDF: <https://arxiv.org/pdf/2512.04123v4>
- Local PDF: `data/papers/pdfs/2512.04123v4-measuring-agents-in-production.pdf` (47 pages; SHA-256 `6e31108f44fe1f7b4c447bedfa7ed4b7ab597f75dbcf3ce2ea2d758cb59fc779`).
- Local layout-preserving text: `data/papers/text/2512.04123v4-measuring-agents-in-production.txt` (SHA-256 `8bf2839e1a1411f333ac8e4533dad4a07d6f345f74b4e6aa52e905e0076189b9`).
- Provenance: `data/sources/2512.04123v4-measuring-agents-in-production.provenance.json`.
- Date read: 2026-07-14. The complete paper was read through the interview outline, all-data appendix, terminology, full 47-question survey tables, and branching diagrams.

### Version-drift evidence read

- Preserved v3 PDF: `data/papers/pdfs/2512.04123v3-measuring-agents-in-production.pdf` (SHA-256 `3921af01b93a824d83a4c828c9a9c39ce7990246cfee8ac47d2b0f50ec3d87ca`).
- Preserved v3 text: `data/papers/text/2512.04123v3-measuring-agents-in-production.txt` (SHA-256 `affdbb4fe3c2c21c7d958e95dcdef0f3021b647f110c8815e486c2345f89f39a`).
- v3's abstract says “surveyed 306 practitioners across 26 domains”; v4 says “surveyed 86 deployed systems practitioners.” Both versions' bodies state that 306 valid responses were collected and main-paper survey analysis was filtered to 86 production-or-pilot responses, with full-data comparisons in Appendix D (v4 pp. 2–3, 21–29). The v4 abstract is a clarification toward the main estimand, not evidence that the entire study recruited exactly 86 unique deployed-system practitioners.

### OpenReview boundary

The corresponding forum at <https://openreview.net/forum?id=FxNCt9xtOZ> and API/PDF endpoints were retried. OpenReview returned `403 ChallengeRequiredError` or a browser-verification page. No forum record, review, rebuttal, or decision text was acquired or treated as inspected evidence. Search-result snippets are discovery metadata only. The review therefore rests on the full immutable accepted arXiv v4 paper and preserved version evidence, not peer-review content.

## One-sentence contribution

MAP makes selected practitioners' deployment architecture and evaluation reports substantially more inspectable, but its outcome-conditioned recruitment, optional-question attrition, self-report measures, and absent system audit support a practice map—not claims that common methods cause reliability or successful deployment.

## Methodology and system

### Twenty confidential cases

The qualitative arm contains 20 cases: 14 production and six final-pilot deployments serving real users, grouped into five broad sectors and anonymized as C01–C17 because similar cases are merged for confidentiality (pp. 3, 21–24). The sample starts in the authors' professional networks at major technology companies and expands through snowball sampling for application, maturity, and geographic diversity. Participants were hands-on ML/software engineers or technical leads. Each 30–90 minute interview involved two to five participants and an interviewing team of two to five unaffiliated researchers (pp. 3, 23–24).

The protocol covers 11 areas: problem/benefit, metrics and evaluation, architecture and human interaction, system stage and failure, stakeholder constraints, alternatives/ROI, dependencies, users, cost/value, affected stakeholders, and participant role (pp. 24–25). Depending on participant preference, interviews were recorded or captured as detailed notes. At least three researchers independently open-coded **each interview note**, then used focused coding and peer debriefing to resolve disagreements (p. 3).

This is credible exploratory qualitative work, but the evidentiary object is under-specified. The paper does not report total interview-participant count, which cases were recorded, transcript or member-check procedures, codebook, code frequencies, saturation criterion, negative-case analysis, coding agreement, rejected themes, or quote-level evidence. Claims are presented as recurring team reports, not auditable coded records. Mixing recordings and notes creates unequal evidence views, and coding notes can amplify interviewer selection before the nominally independent coding stage.

Most importantly, case eligibility conditions on production or final pilot. The sample includes no matched failures, abandoned attempts, or alternative implementations. The interview outline asks about abandonment, but all admitted cases serve users. The design can describe what selected deployed teams report doing; it cannot show that those practices enabled deployment, beat alternatives, or distinguish success from survivorship.

### Public survey and the population funnel

The survey was piloted with outside development teams and implemented in Qualtrics with dynamic branching. It was distributed from 28 July to 29 October 2025 through Berkeley's Agentic AI Summit, an AI Alliance meetup, a Berkeley MOOC, LinkedIn, Discord, X, and professional networks (pp. 3, 21). Respondents self-identify as practitioners building systems they personally call agents, assistants, or agentic. Of 306 valid responses, 294 say they directly contributed to at least one system (p. 22).

Respondents working on multiple systems are instructed to choose either the system they know best or the **most developed** one, and are invited to submit additional responses for other systems (pp. 30–32). That creates three unaddressed dependence and selection risks:

1. familiarity/maturity selection favors established systems;
2. the same practitioner may contribute multiple system responses; and
3. respondents or organizations may overlap across survey and interviews or within survey submissions.

No respondent, organization, or system deduplication and no cluster identifier are reported. Appendix G nevertheless says the 306 responses highlight breadth across “distinct agent deployments” (p. 32), which the instrument does not establish.

The displayed stage accounting is especially important. Figure 14 reports only 111 stage responses: 50 production, 36 pilot, 22 prototype, two research, and one retired (p. 21). Main-paper analysis calls the 86 production/pilot responses “deployed agents,” but question-specific denominators fall substantially because questions are optional and branching is dynamic: motivation 66, domain 69, end user 67, latency 53, autonomous steps 60, prompt construction 53, models 22, frameworks 29, evaluation methods 31, and ranked challenges 29 (pp. 1–8, 16–19). The paper provides denominators on figures—a major strength—but no item-missingness table, response-flow counts, missingness mechanism analysis, or comparison of respondents and nonrespondents for each headline measure.

“306 valid responses” is also not operationally defined. The paper reports consent and eligibility branching but no duplicate, bot, partial, contradiction, duration, or quality-screen rule. Survey percentages are best read as **available-case self-report proportions for each displayed question**, not estimates over 306 practitioners or 86 independently sampled deployments.

### Measurement construction

The complete instrument reveals what each headline actually measures:

- productivity and reduced human hours are **target gains**, not achieved outcomes (QN7, pp. 34–35);
- autonomous horizon is the respondent's categorical answer to how many steps/cycles can execute before user input is required, not a trace-derived step count or intervention-quality measure (QN10, p. 35);
- evaluation prevalence comes from methods “currently integrated” that give the respondent confidence in consistent high-quality output, with many submethods collapsed into manual/model/cross-reference/rule categories (QO1, pp. 37–38);
- the challenge ranking bundles reliability with robustness, scalability, real-time responsiveness, and resource constraints under “Core Technical Performance” (QO2, p. 38);
- framework use, model count, prompt length, data access, latency, and modality are respondent estimates, not configuration or telemetry audits.

Application domain is the only reported free-text survey variable used in main analysis. LOTUS proposes categories; three annotators assign multi-label categories, with mean pairwise Cohen's κ=.636 and a fourth adjudicator for unresolved cases (pp. 3, 15–16). This is more transparent than most category construction in practitioner surveys. Yet the reported “26 domains” and displayed nine-category normalization are different levels; no row-level labels, category definitions, coder matrix, adjudication ledger, or confusion pattern is released. κ=.636 over pairwise labels does not itself validate the domain ontology or prevalence.

For categorical comparisons, the paper reports 95% intervals from 1,000 response-level bootstrap resamples (pp. 1, 3, 15). That does not address unknown respondent/organization/system clustering, network recruitment, nonprobability sampling, item nonresponse, or multi-label dependence. The figures' wording “95th percentile intervals” is also insufficient to identify percentile endpoints and implementation. Intervals quantify conditional sample variability, not population representativeness.

## Evidence: what survives and what does not

### Bounded descriptive observations

The following survive as author-reported descriptions of selected, available-case responses and interview cases:

1. **Bounded human-supervised workflows are common in this sample.** Forty-one of 60 step-horizon respondents report at most ten steps/cycles before input, while interviewees commonly describe fixed workflows, read-only modes, approval gates, sandboxes, wrapper APIs, and role-based access (pp. 6–8, 19).
2. **Human review is a common evaluation component.** Twenty-three of 31 evaluation-method respondents select manual/HITL and 16 select model-based evaluation; the methods are multi-select and often combined (pp. 7, 17–18).
3. **Formal task-set benchmarking is uncommon among interview cases.** Fifteen of 20 case teams reportedly do not use benchmark sets, instead drawing on A/B tests, user feedback, monitoring, historical logs/tickets, or expert review (pp. 7–8).
4. **Outcome signals can be delayed and domain-specific.** Interviews cite expert-label expense, proprietary customization, heterogeneous baselines, and consequences such as financial loss or approval delay that arrive too slowly for fast iteration (p. 8).
5. **Sensitive and proprietary context matters.** Twenty of 29 data-handling respondents report confidential-data retrieval and 26 report databases; interviews describe regulatory and integration constraints (pp. 8, 19).
6. **Configuration maintenance is part of the deployment problem.** Interviewees report model-update fragility, custom orchestration, client-specific infrastructure, and prompts accumulating guardrails and exceptions (pp. 5–6, 16–17).
7. **The sample spans diverse application descriptions.** The paper identifies long-tail use cases across business operations, communications, science, DevOps, and combined software/business workflows, though this is diversity evidence rather than a prevalence frame (pp. 15, 21–23).

These observations justify benchmark design attention to human gates, proprietary source packs, delayed consequences, configured-system versioning, heterogeneous baselines, and portfolio diversity.

### Claims that outrun the evidence

1. **Methods enabling success.** There is no outcome audit, failed-system comparison, or causal treatment. Deployment-conditioned cases cannot identify enabling methods.
2. **Reliability as the measured top challenge.** Eleven of 29 respondents rank a broad five-part “Core Technical Performance” bundle first. Reliability is one component, not an isolated survey outcome; the paper's IEEE definition is not operationalized as failure-free probability over time (pp. 8, 18, 38).
3. **Controllability maintains reliability.** Short horizons, fixed workflows, human review, and deployment coexist in selected reports. No failure rates or matched architecture outcomes establish that constraint caused reliability.
4. **Agents outperform human baselines.** Interview anecdotes report large time advantages; only 39% of 31 baseline-question respondents report a formal comparison, and baseline construction, equal-outcome basis, artifacts, measures, and results are absent (pp. 4, 7, 17).
5. **Human judgment is needed because tasks are nuanced.** The association is plausible, but evaluation choice can also reflect absent graders, liability, policy, customer expectations, risk transfer, or maturity. No method-effect comparison validates human judgments.
6. **Production prevalence.** Network and event recruitment, optional responses, maturity-selected focal systems, unknown duplicates, and available-case denominators prevent representative global, industry, or deployment-population estimates.
7. **Production rather than pilot evidence.** The main estimand combines 50 reported production systems with 36 controlled pilots. Those stages have different users, constraints, monitoring, and outcome maturity and are not separated in headline findings.

## Unique insight: practice evidence needs a practice-to-outcome bridge

MAP's useful contribution is not a checklist of fashionable production choices. It exposes a sequence that `skill-bench` should preserve whenever production reports motivate a task or operating requirement:

1. **reporting unit** — respondent, team, organization, system, deployment, version, and whether units overlap;
2. **eligibility and selection** — recruitment channel, stage, outcome conditioning, focal-system rule, optional-question path, and missingness;
3. **reported practice** — architecture, prompt/model policy, human gate, evaluator, monitor, security boundary, and baseline;
4. **practice realization** — immutable configuration or observed trace showing the practice actually operated;
5. **measurement view** — artifact/state/trajectory evidence available to humans, rules, and model graders;
6. **burden and action** — reviewer expertise, sampled fraction, latency, disagreement, override, repair, and escalation;
7. **task outcome** — correct artifact/state, accepted delivery, collateral effects, and downstream use;
8. **operational outcome** — reliability over opportunities/time, delayed labels, incidents, user effects, cost, and loss;
9. **counterfactual** — alternative configuration or workflow with an equal-outcome basis;
10. **licensed claim** — description, association, treatment effect, professional validity, safety, fitness, or readiness.

MAP directly observes stages 1–3 only through confidential self-report and describes fragments of stages 5–6. It does not audit stages 4 or 7–9. Therefore its findings can inform **coverage hypotheses and authoring requirements**, but cannot supply benchmark ground truth, reliability calibration, intervention efficacy, or release thresholds.

This bridge is nonduplicative with production telemetry evidence. The Perplexity production-usage study observes attempt and execution traces but not accepted professional outcomes; MAP observes team-reported architecture and rationale but no traces or outcomes. AgentLens and Nubank contribute trajectory/online-measurement cases; Anthropic and Amazon contribute production prescriptions and experience reports. Together they support a triangulation rule: self-report can identify candidate practices, telemetry can test realization and workflow shape, controlled offline trials can measure configured behavior, and online/field evidence is still needed for downstream consequence. None inherits the validity of another stage automatically.

## Limitations and validity threats

### Sampling and unit validity

1. Interview cases are purposive, network- and event-recruited, geographically concentrated, and conditioned on production/final pilot.
2. Survey recruitment is nonprobability sampling through events, a course, social media, and professional networks.
3. Respondents may choose their most-developed system and may submit multiple systems, inducing maturity selection and unknown repeated units.
4. Unique practitioners, systems, deployments, teams, and organizations are not distinguished in analysis.
5. Production and pilot are pooled into one “deployed” category despite different validity and maturity.
6. The 306-response frame shrinks to 111 reported stages, 86 production/pilot records, and much smaller available-case denominators without an attrition ledger.
7. The criteria for a “valid” response and deduplication/quality controls are not reported.
8. April–November 2025 spans fast-changing models and systems; versions and temporal changes are not tied to individual observations.

### Measurement and construct validity

9. All survey measures are self-report; no deployment, user count, configuration, artifact, trace, benchmark, monitoring, or outcome is independently verified.
10. Target gains are described as adoption motives and sometimes rhetorically approach achieved benefits.
11. Step-before-input conflates a configured cap, observed horizon, task structure, approval policy, and limitation.
12. “Human evaluation” aggregates expert review, citation verification, crowd review, and red teaming; integration does not establish frequency, authority, agreement, action, or accuracy.
13. “Model based,” “cross-referencing,” and “rule based” similarly collapse heterogeneous evaluator constructs.
14. The top challenge is a broad compound rank category, not a direct measure of reliability probability or failure severity.
15. Domain labels are model-seeded and human-adjudicated, but the ontology and row-level lineage are unavailable.
16. Interview coding is performed over unequal recordings/notes with no codebook, saturation, agreement, quote corpus, or negative-case ledger.
17. Confidentiality prevents case-level cross-checking and may encourage broad, non-falsifiable summaries.
18. Survey wording is sometimes leading: methods are framed as giving confidence in consistent high quality, and agent preference is asked “if it were entirely up to you.”

### Statistical and causal validity

19. Response-level bootstrap intervals ignore unknown clustering, repeated submissions, network structure, and nonprobability sampling.
20. Available-case proportions use sharply varying denominators, but missingness is neither modeled nor bounded.
21. Multi-select outcomes and many descriptive comparisons receive no multiplicity or dependence treatment.
22. Deployed/non-deployed appendix contrasts are not matched and are subject to stage-reporting and optional-question selection.
23. There is no success measure, comparator group of failed systems, practice randomization, temporal ordering, or adjustment for domain/organization/maturity.
24. Explanations such as “deliberately trade capability for controllability to maintain reliability” are interview interpretations, not identified effects.
25. The 20 cases and survey may overlap in organizations or participants, so qualitative/quantitative agreement is not necessarily independent triangulation.

### Ethics, conflicts, and claim incentives

26. The study is reported exempt from institutional review; data are confidential and aggregated, but consent wording, data-retention policy, participant compensation, and withdrawal boundary are not included in the paper.
27. Authors include affiliations with IBM Research and Intesa Sanpaolo, and acknowledgements list gifts from many technology firms. No author conflict-of-interest statement or funder-role statement is visible beyond affiliations and support.
28. Selecting and describing “successful” deployments creates a favorable-survivor frame that should be separated from neutral practice characterization.

## Reproducibility and operational realism

**Primary-source inspectability: moderate to high for instrument design.** The accepted full paper supplies recruitment dates/channels, eligibility language, interview outline, survey wording, branching diagrams, question-specific figure denominators, all-data comparisons, and a useful domain-coding description. Preserving v3 and v4 makes the headline population clarification auditable.

**Computational reproducibility: low.** No response table, item-missingness matrix, organization/system identifiers, codebook, interview evidence, LOTUS outputs, annotation rows, bootstrap code, figure data, analysis script, or preregistration is released. Confidentiality can justify restricted raw data, but not the absence of de-identified response-flow tables, synthetic analysis fixtures, full estimator specifications, codebook/version cards, or auditable aggregate cells.

**Operational realism: high for reported constraints, unverified for realized operation.** The study reaches people responsible for live or pilot systems and captures proprietary integration, human oversight, delayed labels, sensitive data, model migration, latency, and custom workflows that benchmarks often omit. Yet every operational fact remains respondent report; no configured system, trace, artifact, monitor, incident, baseline, or user outcome is inspected.

## Transfer to `skill-bench`

### Retain

- Sample portfolio conditions beyond coding: asynchronous work, internal/external users, expert augmentation, confidential databases, multimodal inputs, delayed consequences, and client-specific workflows.
- Make human roles explicit: operator, approver, observer, optimizer, domain verifier, and escalation owner should not collapse into “HITL.”
- Treat bounded autonomy as a configurable workflow property—steps, gates, permissions, and approval loci—not a model trait.
- Include mixed evaluation stacks and capture what each grader sees, how often it runs, disagreement, routing, and corrective action.
- Preserve full non-agentic comparators as heterogeneous workflows rather than forcing a single model or software baseline.
- Record model/provider and scaffold migration because apparently stronger updates can break a compound workflow.
- Prefer end-to-end task and downstream metrics where the professional objective is productivity, but keep quality, review, risk, and equal-outcome assumptions separate.

### Repair

1. Add a **practice-provenance record** when MAP or another practitioner study motivates a design choice: source/version, respondent/system unit, recruitment, stage, focal-system selection, question wording, denominator, missingness, clustering, and claim ceiling.
2. Never turn “common among respondents” into a rubric requirement. Require independent expert/source authority and task-specific evidence.
3. Split human evaluation into role, authority, evidence view, sampling policy, decision, burden, disagreement, and action taken.
4. Split autonomy into maximum permitted horizon, observed steps, planned workflow depth, intervention trigger, intervention type, and post-intervention continuation.
5. Define reliability operationally: opportunity population, failure event, time/window, environment, severity, censoring/invalids, recovery, and uncertainty. Do not use MAP's broad challenge rank as a reliability target.
6. Stratify production and pilot evidence; preserve system/version/time and avoid pooling maturity stages by default.
7. Test the claimed control mechanism rather than copying it: matched permission/human-gate/workflow conditions with repeated trials, artifact/state observers, useful completion, human burden, and failure severity.
8. Include hard-to-measure benefits and harms, not only productivity tasks, so current measurability does not become benchmark construct underrepresentation.
9. Use low-latency tasks and high-autonomy cases as controls; a portfolio should test where bounded asynchronous operation generalizes rather than selecting only the modal reported pattern.
10. Require independent field or expert evidence before promoting a synthetic benchmark result to professional validity, production fitness, safety, or readiness.

## Concrete repository actions

- **No new queue task added.** MAP's nonduplicate requirements already have homes in the metric-monitoring, task-health, validity-argument, expert-participation, configured-system, execution-validity, artifact/state, and reliability machinery. A MAP-specific schema would duplicate those contracts.
- Index this review under reliability/production evaluation, with secondary tags for practitioner survey, human evaluation, bounded autonomy, missingness, and operational validity.
- Canonical synthesis need not change yet: MAP strengthens the existing conclusion that production observations must retain unit/selection/denominator and cannot skip the bridge from reported practice or telemetry to realized outcome. It does not overturn an existing grouped conclusion or establish a new relevance tier.
- In a future cross-source consolidation, compare MAP's **reported practice** with AgentLens's observed production trajectories, Nubank's offline/online association, Anthropic/Amazon operating prescriptions, and production-usage telemetry using one evidence-stage matrix rather than averaging their claims.

## Assessment

- **Evidence tier:** Tier B enabling evidence for realistic portfolio conditions and production-evaluation authoring; full accepted immutable paper and instrument, but nonprobability self-report, severe optional-question attrition, no deployment audit, and no released data/code.
- **Most reusable contribution:** a transparent cross-domain instrument and selected practitioner evidence that human gates, sensitive context, delayed labels, heterogeneous baselines, and task-specific evaluation are central deployment conditions.
- **Most important empirical signal:** among the available-case deployed/pilot subset, bounded workflows and mixed human/automated evaluation are frequently reported, while formal benchmark sets and clean alternatives are often absent.
- **Most serious flaw:** the paper asks what makes deployment successful after selecting deployed/pilot cases and measuring neither success nor reliability; common reported practice is interpreted as an enabling mechanism.
- **Claim `skill-bench` may safely make:** MAP provides evidence-backed hypotheses about conditions a realistic knowledge-work benchmark portfolio should represent. It does not establish representative production prevalence, practice effectiveness, professional validity, configured-agent capability, reliability, safety, production fitness, or readiness.
