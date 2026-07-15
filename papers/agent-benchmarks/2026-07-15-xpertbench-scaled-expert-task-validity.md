# XpertBench: scale without an auditable validity chain

**Paper:** Xue Liu et al., *Xpertbench: Expert Level Tasks with Rubrics-Based Evaluation*

**Version read:** arXiv:2604.02368v4 (21 April 2026), all 25 pages

**Canonical source:** https://arxiv.org/abs/2604.02368v4

**Immutable PDF:** https://arxiv.org/pdf/2604.02368v4

**Local PDF:** `data/papers/pdfs/2604.02368v4-xpertbench.pdf` (SHA-256 `9c2cc0a0c66a8567f93653c052d17db85de9790a970f38205bbf4c41b02e83f6`)

**Local text:** `data/papers/text/2604.02368v4-xpertbench.txt` (SHA-256 `2970e4a582b08500f1bdbff921ac502eb14e8a5c1c1fd765c673e9b49f7284c0`)

**Version comparison:** immutable v1 PDF/text at `data/papers/pdfs/2604.02368v1-xpertbench.pdf` and `data/papers/text/2604.02368v1-xpertbench.txt`

**Platform/release audit:** `data/sources/releases/2604.02368v4-xpertbench/provenance.json`

**Review status:** deep review of the complete v4 paper, v1 comparison, dated paper-linked platform audit, and inspection of two unverified release leads

## Bottom line

XpertBench's useful contribution is an attempted operating pipeline at unusual scale: recruit credentialed contributors, train them to convert work into tasks, cap submissions per contributor, generate draft rubrics, obtain expert revision and peer review, label one baseline response criterion by criterion, and place that labeled response in an LLM judge's context. The retained inventory is reported as 1,346 tasks across seven domain groupings and more than 80 categories; 245 tasks receive the expensive expert-anchor treatment (Sections 3–5, pp. 4–10).

The paper does **not** establish the chain implied by its strongest language:

```text
large expert pool
→ known contributor sample and feasible participation
→ representative professional episodes
→ valid retained tasks
→ authoritative and internally coherent rubrics
→ reliable expert labels
→ calibrated ShotJudge criterion decisions
→ stable aggregate scores
→ expert-level professional capability
→ practical viability or readiness
```

It gives partial, mostly procedural evidence for the middle of that chain. It gives no auditable submission/attrition table, contributor-level assignment records, compensation or rights information, task-frequency frame, released tasks, complete rubrics, expert labels, judge prompts, generation configurations, repeated trials, uncertainty intervals, or scoring code. More seriously, the appendix contains a direct task–rubric mismatch: the Education example asks for a Confucius–Socrates screenplay, but its rubric grades a differentiated lesson plan for teaching digital clocks (Appendix A.3, pp. 18–19). This is observed projection drift inside the paper's own showcase, not a hypothetical risk.

ShotJudge is also not shown to be calibrated in the statistical sense. One expert-labeled GPT-5 response is disclosed to Gemini 2.5 Pro as an in-context example for each task. The paper reports only `CDR = agreement − disagreement = 52.0%` on an unspecified comparison sample, with no denominator, zero-shot value, uncertainty, expert–expert reliability, held-out design, or criterion/domain slices (Section 4, pp. 7–8). That demonstrates neither criterion accuracy nor generalization. Because Gemini 2.5 Pro is itself an evaluated candidate and GPT-family candidates are evaluated against a GPT-5 anchor, the method retains self-family and reference-similarity pathways that the claimed mitigation does not isolate.

For `skill-bench`, the main lesson is negative but actionable: **expert scale is an acquisition property, not a validity property; a scored expert example is a judge treatment, not proof that expert intent was transmitted.** Existing participation, task-health, criterion-envelope, grader, metric, and validity machinery can absorb the requirements. No new build task is warranted.

## One-sentence contribution

XpertBench describes a scaled expert-task and exemplar-conditioned judging pipeline whose unreleased handoffs and observed appendix defects show why contributor volume and criterion agreement cannot by themselves validate retained tasks, graders, professional capability, or participation feasibility.

### Research question and detailed contribution

The paper asks whether open-ended professional work can be evaluated at broad domain scale using expert-authored tasks, weighted binary checkpoint rubrics, and an LLM judge conditioned on one expert-scored baseline response (Abstract; Sections 1 and 4, pp. 1–2, 7–8).

Its concrete contributions are:

1. **Inventory construction:** 1,346 reported tasks distributed across Education (329), Engineering & Applied Sciences (275), Finance (244), Law (215), Humanities & Social Sciences (116), Computer Science (92), and Healthcare (75), totaling seven domain groupings and more than 80 categories (Figure 2 and Table 1, pp. 5–6).
2. **Expert funnel:** recruitment through direct registration, referrals, and vendors; background/credential characterization; a domain exam; trial authoring or annotation; senior review; standardized task training; a three-prompt contributor cap; and additional domain review (Section 3.1–3.3, pp. 5–7).
3. **Rubric process:** Claude Opus 4.1 or Gemini 2.5 Pro drafts criteria from the task and reference answer; an author or another annotator edits them into mostly 15–40 binary checkpoints; experts assign qualitative and 1–10 numeric weights and category tags; at least one additional expert reviews each rubric; senior experts spot-check about 30% of tasks (Section 3.3, pp. 6–7).
4. **ShotJudge:** experts label a GPT-5 baseline response at criterion level and supply rationales; a senior cohort cross-verifies those labels; Gemini 2.5 Pro sees that scored response as a one-shot example before assigning binary labels to candidate responses (Section 4, pp. 7–8).
5. **Configured-system observations:** weighted scores for 14 named model configurations on a reported 245-task Gold subset, with five-domain breakdowns and qualitative claims about model specialization (Figures 3 and Table 3, pp. 9–10).

The first four are potentially reusable process designs. The fifth is only a descriptive result under an under-specified and unreleased instrument.

## Methodology and system

### 1. Contributor population, qualification, and participation

The Xpert platform is said to contain approximately 3,000 selected experts. For XpertBench, contributors came from direct registration, peer referral, and vendor partnerships. Approximately 61% were affiliated with Chinese 985/211 or specialist universities; more than 200 came from overseas institutions; every member reportedly had at least three years of practice; and the pool included 183 legal qualifications, 163 medical licenses, plus CFA, CPA, and CATTI holders (Section 3.1 and Section 7.1, pp. 5–6, 12).

These numbers characterize a **pool**, not the realized contributor sample. The paper never reports:

- the number invited, screened, attempted, qualified, active, withdrawn, rejected, or retained;
- contributor counts by domain, credential, institution, geography, employer, or career stage;
- whether one person could hold multiple listed credentials;
- how many tasks each person submitted, authored, reviewed, or anchored;
- exam content, thresholds, pass rates, reliability, or relationship to the authored task type;
- reviewer assignment, conflicts of interest, independence, or disagreements;
- training duration, support, time per contribution, payment, rejected-work payment, attribution, license, consent, ownership, withdrawal, or prohibited-use terms.

The paper alternates among “over 1,000 submissions,” “over 1,000 elite domain experts,” and a platform pool of about 3,000 (Abstract; Section 1, p. 2; Section 7.1, p. 12). Section 3.2 says an initial pool of “over 1,000 submitted prompts” became 1,346 retained prompts (p. 6). “Over 1,000” can arithmetically include more than 1,346, so this is not a formal contradiction; it is an unusable attrition account. There is no exact candidate denominator or mapping from submissions to contributors. The three-prompt cap limits single-author dominance in principle, but without author IDs and counts it does not establish contributor diversity.

The design therefore supplies no evidence that scaled participation was low-cost, equitable, repeatable, or acceptable to experts. Institutional prestige and credentials are weak proxies for authority over each particular task, and neither establishes that the selected episode is frequent, consequential, or representative.

### 2. Task elicitation, selection, and ecological-validity claim

Experts were trained to distinguish professional tasks from exam questions and asked to provide context, relevant background or domain knowledge, deliverable requirements, and a reference answer. Each could submit at most three prompts. Internal experts retained tasks that were difficult for state-of-the-art models, typical/high-frequency, objectively evaluable, and not preference-driven (Section 3.2, p. 6).

This pipeline has a valuable shape but unresolved construct conflicts:

- **Difficulty is outcome-conditioned selection.** No screening models, prompts, tools, dates, number of attempts, pass threshold, or inclusion decisions are reported. Selecting after observing model failure can inflate apparent difficulty and favors failure modes of the screening configuration.
- **Typicality is asserted, not measured.** There is no workflow observation, incident log, O*NET-like frame, frequency estimate, consequence estimate, client/manager validation, or rejected-task comparison.
- **A text prompt can only project a workflow.** The paper calls tasks “end-to-end” and “long-horizon,” but reports prompt length only (mean 631, apparently tokens or words but unit unspecified) and presents text-response examples. No task duration, tool actions, environment state, source-pack boundaries, interactive handoffs, artifact types, or workflow completion criteria are reported.
- **High-stakes domains are not high-stakes trials.** Healthcare, law, and finance labels do not create realistic authority, confidentiality, live-state, compliance, or consequence conditions.
- **Purposive coverage is not prevalence coverage.** Education is 24.4% and Healthcare 5.6%, but no target population or weighting principle explains those shares. Category counts show authored breadth, not occupational or economic representativeness.
- **Reference answers may narrow legitimate solution space.** They are inputs to both rubric drafting and task retention, but the paper gives no alternative-valid procedure, counterexample, accepted-equivalence, or reference-authority protocol.

The appendix confirms both useful specificity and severe drift. The Finance task fixes a time window and asks for auditable calculations; the STEM task requires interpreting gel images and biological mechanisms; the HSS task asks for a structured screenplay (Appendix A, pp. 15–25). Yet attachments, source packs, and executable artifacts are not released, and only five domain examples are shown. Computer Science and Healthcare lack appendix examples even though all 245 Gold tasks reportedly contribute to the overall score.

### 3. Rubric construction and integrity

The process explicitly separates LLM drafting, expert refinement, peer review, and partial senior spot-checking. Criterion-level binary decisions and weights are more diagnostic than one holistic preference. These are strengths worth retaining.

The observable artifacts undermine the claim that the process guarantees atomic, objective criteria:

1. **Task–rubric projection failure:** the Education prompt is the Confucius–Socrates screenplay (p. 18), while all listed Education criteria concern a clock-reading lesson plan, differentiated student levels, Seewo games, five lesson stages, and People's Education Press materials (pp. 18–19). The HSS section repeats the screenplay task and supplies the corresponding philosophical/dramatic rubric (pp. 23–25). The Education pair cannot validly score its displayed task.
2. **Non-atomic gates:** the HSS “Qualification review” criterion bundles format completeness, language, setting, historical accuracy, and dialogue balance into one binary item (p. 24). Other HSS criteria conjoin multiple philosophical claims, historical events, plot functions, and trajectory requirements. Binary failure cannot identify which predicate failed.
3. **Dependent and duplicate penalties:** positive legal criteria and “must not” criteria encode overlapping conclusions, allowing one conceptual error to be counted repeatedly (pp. 17–18). No dependency graph, mutual-exclusion rule, or double-penalty policy is defined.
4. **Unstable STEM thresholds:** the STEM rubric says the minimum foreign fragment is `≥19 kb`, gives an illustrative lane calculation of `15.5 kb`, and then calls “at least greater than 15 kb” conservative while saying the actual average is about 20 kb (pp. 21–22). Those may refer to different quantities, but the criterion text does not maintain a clean estimand.
5. **Weighting is uncalibrated:** experts assign 1–10 weights without distribution constraints. The paper offers no elicitation protocol, normalization across experts/tasks, sensitivity analysis, inter-rater agreement, relationship between Essential/Important/Optional tags and numeric weights, or minimum essential-gate policy. In examples, a task can compensate for a missing “Essential” requirement through many other points.
6. **“Objective” is overstated:** criteria such as “three-dimensional,” “profound,” “clever,” “exquisite,” “superior working capital management,” and “highly consistent” require judgment despite binary labels (Appendix A). Specific prose does not eliminate latent thresholds.
7. **Transformation lineage is absent:** the paper does not preserve draft model/version/prompt, edits, reviewer decisions, disputed alternatives, or before/after validity evidence. At least-one peer review and 30% senior spot-checking do not disclose defect rates or agreement.

This appendix mismatch is especially important for benchmark operations: schema-valid task and rubric objects can still point to the wrong instance. `skill-bench` should treat task–rubric–reference–source-pack identity and semantic conformance as a release gate, with planted cross-instance substitution tests.

### 4. ShotJudge information flow

For each Gold task, a primary domain expert labels each criterion on one GPT-5 response and writes a rationale. Senior experts “cross-verify” those labels. Gemini 2.5 Pro then receives the task, rubric, the GPT-5 response, and its validated criterion labels/rationales as an in-context example before scoring a candidate response criterion by criterion (Section 4, pp. 7–8).

The unique idea is to transmit **decision-boundary evidence**, not merely criterion wording. A concrete scored response can reveal how an expert handles entailment, omission, tolerance, and borderline cases. But one example does not identify a boundary: it gives one point in response space, often with many satisfied and failed criteria correlated within the same response.

The design leaves major treatment confounds:

- the baseline response and labels can cause answer/style anchoring rather than expert-reasoning transfer;
- the same GPT-5 anchor is used while GPT-5, GPT-5.2, and GPT-5.4 candidates are evaluated, making family/style similarity a plausible treatment path;
- Gemini 2.5 Pro is both the judge and an evaluated candidate, so self-family preference remains possible;
- the baseline model's exact version, tools, search, prompt, and generation settings are absent;
- there is no randomized zero-shot versus one-shot experiment on the same held-out responses;
- there are no alternative exemplars, counterexamples, criterion-isolated examples, order tests, or exemplar-transfer tests;
- it is unclear whether senior experts independently relabeled, reviewed rationales, adjudicated disagreements, or merely approved them;
- there is no blinded expert scoring of the evaluated candidate responses against which ShotJudge criterion labels are tested.

The paper's term “gold-standard” is therefore too strong. The anchors are reviewed expert labels under an unknown process, not validated ground truth.

### 5. Reliability metric and empirical analysis

The paper defines CDR as `P(agree) − P(disagree)` and reports 52.0%, saying this penalizes “rank reversals” and significantly outperforms zero-shot judging (pp. 8–9). If every comparison is binary and there are no ties or invalids, CDR is just `2 × agreement − 1`, so 52% corresponds to 76% agreement. But the manuscript never specifies:

- whether the unit is a criterion label, response pair, task ranking, or aggregate preference;
- how ties, missing outputs, invalid judge responses, and criterion prevalence are handled;
- number of tasks, responses, criteria, experts, or labels in the alignment sample;
- the zero-shot CDR, effect size, statistical test, or confidence interval;
- expert–expert agreement or adjudication uncertainty;
- domain, criterion, weight, positive/negative class, or author slices;
- whether calibration and evaluation responses are disjoint.

Calling criterion agreement a rank-reversal metric mixes two estimands. Even 76% raw agreement could be weak under class imbalance. Agreement with one reviewed label set is not calibration: no probability forecasts or calibration curve are reported, and binary outputs cannot show confidence calibration.

The Gold subset is described as a “highly curated” stratified sample of 245 tasks, but strata, allocation, inclusion probabilities, selection criteria, seed, and domain counts are absent (p. 9). Computer Science and Healthcare are omitted from fine-grained domain analysis due to small samples while included in the overall score. Consequently the reported overall score's target population is unclear.

The results section says it evaluates “several” models and initially names four, while Figure 3 lists 14 configurations; the introduction says 12 (pp. 2, 9). Model labels are not reproducible configurations. The paper does not report provider/version snapshots, system prompts, tool/search availability per model, source/index dates, temperature, token budgets, timeout, number of attempts, failures, costs, or candidate-response capture. It later says leading systems are “augmented with retrieval/search capabilities” without specifying comparable retrieval treatments (p. 10).

Scores are weighted fractions of satisfied criteria, not success rates. No task pass threshold exists in Equation 1, so “66% success rate” and “completion rate” misname mean rubric compliance (Abstract; pp. 9–10). The paper reports no repeated trials, standard errors, bootstrap intervals, task-cluster uncertainty, multiple-comparison handling, robustness to weights, or judge swaps. Small domain differences cannot support specialization claims without uncertainty, and selected-task results do not prove architectural or professional capability gaps.

The qualitative claims about retrieval interference, principle hallucination, and cascading errors are not accompanied by a coding protocol, sample, counts, raters, agreement, examples linked to trial records, or causal ablation (Introduction, pp. 2–3). They are hypotheses, not demonstrated failure rates.

## Evidence and claim boundaries

### Supported by the full paper

- The authors specify a multi-stage expert/task/rubric/judge workflow and report a 1,346-task, seven-domain inventory with category counts.
- They report credential characteristics for a broader expert pool, qualification steps, a maximum of three submissions per contributor, at least one additional expert review per rubric, and about 30% senior spot-checking.
- They describe an LLM-drafted/expert-refined weighted-checkpoint rubric process and a one-shot expert-labeled baseline-response treatment.
- They report weighted scores for named candidate systems on 245 Gold tasks and a 52.0% CDR headline.
- The appendix exposes real rubric design patterns and observable integrity defects, including one complete task–rubric mismatch.

### Not supported

- That more than 1,000 distinct contributors authored retained tasks, or that contributor scale was affordable, fair, diverse, or sustainable.
- That the retained tasks probability-sample professional work, reproduce end-to-end workflows, or have superior ecological validity.
- That all rubrics are atomic, objective, authoritative, semantically aligned, dependency-aware, or complete over legitimate alternatives.
- That senior review establishes expert-label reliability.
- That ShotJudge is statistically calibrated, causally improves criterion accuracy, transfers expert reasoning, or removes self-reward/family bias.
- That the 245-task score is stable across model runs, judges, search environments, task samples, rubric weights, or time.
- That 66.2% is a success probability, or that model ordering/domain differences are statistically distinguishable.
- That the benchmark measures professional competence, practical viability, safe delegation, productivity, economic value, or readiness.

## Release, reproducibility, and operational realism

### Official paper-linked sources

The immutable v4 paper links the ByteDance Xpert platform and leaderboard, but no code or dataset. Dated 15 July 2026 fetches of both official URLs returned JavaScript application shells. Those exact responses are preserved with hashes in `data/sources/releases/2604.02368v4-xpertbench/provenance.json`; they contain no static task, rubric, anchor, judgment, trial, contributor, or license records suitable for audit. A public dynamic leaderboard is not an immutable result release.

### Unverified release leads

The inspected `randomtutu/Xpertbench` snapshot at commit `b08e51d...` is a personal-account static homepage repository created 12 April 2026. Its README explicitly says evaluation code is absent. The archive contains only a README, static HTML/CSS, and images; it has no repository license. Its owner/committer identity is not in the v4 author/contributor list and the repository is not under a ByteDance organization. It links a Hugging Face namespace, but this does not prove author ownership.

The `ByteSeedXpert/expertbench` Hugging Face revision `c6d1fdf...`, also dated 12 April, belongs to an unverified three-member organization. That revision contains only `.gitattributes` and a 30-byte README declaring CC-BY-4.0—no tasks, rubrics, judge code, or results. The v4 paper does not link either lead. They are preserved as **unverified**, not official, release evidence.

Timing further limits correspondence: both leads fall between v1 (27 March) and v4 (21 April). The static page's citation omits contributors added in v4, consistent with a pre-v4 page, but not proof of ownership. A normalized text comparison found v1 and v4 method/results essentially unchanged; v4 mainly fixes references and adds contributors. It does not repair or disclose the missing validity and reproducibility details identified here.

Operationally, XpertBench is therefore not independently runnable or score-replayable from the inspected sources. No one can reconstruct the Gold sample, model responses, expert anchors, judge prompts, criterion labels, aggregate scores, or costs. Current inspectability is substantially below Agents' Last Exam, GDPval, and ResearchRubrics.

## Unique insight

XpertBench makes visible a distinction that should become explicit in `skill-bench`:

> **A contribution funnel and a judging funnel are two separate measurement systems. Their scale and review counts do not compose into validity unless the handoffs are observable.**

The first funnel transforms contributor experience into a retained task and rubric. It needs population, assignment, attrition, authority, consent, compensation, transformation, and disagreement records. The second transforms a response into criterion labels and a score. It needs evidence views, anchor selection, rater identity, call topology, repeated reliability, adjudication, aggregation, and claim boundaries. XpertBench narrates both funnels but publishes neither event ledger. The result is a large headline inventory and a precise-looking score without a recoverable chain between them.

A second insight comes from ShotJudge: an expert-scored example is not merely “calibration data.” It changes the evaluator's information set and may transmit criterion boundaries, answer content, style, or model-family cues simultaneously. It must be represented and tested as a versioned **grader intervention**, with its own estimand, randomization, contamination boundary, and failure modes.

## Comparison with the closest reviewed work

- **Agents' Last Exam:** ALE provides executable environments, artifacts, graders, and a much more inspectable task lineage, while still lacking a probability sample of work and showing evaluator bypass risks. XpertBench adds a larger narrated contributor funnel but releases far less instrument evidence. It cannot inherit ALE's execution-validity support.
- **GDPval:** GDPval constructs an explicit sector/occupation frame, records experienced contributors and review, and releases prompts/references plus later rubric artifacts. Its frame is purposive rather than representative, but it provides a target-population argument. XpertBench's domain proportions have no equivalent occupational/economic denominator.
- **ResearchRubrics:** ResearchRubrics releases criteria and reports judge macro-F1 against expert labels, with ablations showing that examples can help modestly and LLM expansion can harm substantially. XpertBench's one CDR number lacks the sample, baseline, uncertainty, or released labels needed to establish a stronger judge claim; its LLM-draft/expert-edit process has no transformation ablation.
- **ELAIPBench:** ELAIPBench reports explicit payments and role-specific incentives but omits full submission/revision traces. XpertBench reports neither costs nor rights and therefore adds no evidence that its scale is feasible under limited resources.
- **Many-facet human/AI rater study:** that study fully crosses responses and raters and shows severity is prompt- and criterion-dependent. XpertBench uses one primary judge and no reported crossing, so a pooled CDR cannot distinguish task, criterion, expert, anchor, or judge effects.
- **Rubric Modification:** rubric wording, examples, separate-versus-batched calls, and aggregation are all evaluator treatments with model-dependent effects. ShotJudge fixes one bundled treatment but does not isolate which component changes agreement or whether agreement reflects preserved construct meaning.

## Limitations of this review

The paper-linked platform is a dynamic application. The dated static responses prove endpoint availability and app-shell contents, not everything an authenticated browser session might render. No claim is made that inaccessible backend records do not exist. Conversely, unobserved records cannot support a public reproducibility claim.

The review did not treat the personal GitHub or unverified Hugging Face namespace as author-owned. That conservative boundary may exclude a release the authors intended to endorse, but the immutable v4 paper provides no link or ownership bridge. If a signed author/ByteDance source later establishes ownership and publishes substantive artifacts, release inspectability should be reassessed at that revision.

The v1–v4 comparison used complete PDF text extractions. Layout/OCR normalization can obscure cosmetic changes, but the method/results passages and appendix defects were directly checked in v4.

## Relevance to `skill-bench`

This is a direct test of charter objectives B and F: it exposes where expertise-to-evaluation and expert-participation claims need event-level evidence rather than pool credentials, review counts, and a scalar judge-agreement headline. Its cross-domain inventory is a methodological comparator, not a proposal to narrow `skill-bench` to any listed profession.

## Transferable design requirements

### 1. Make contribution attrition a first-class evidence table

For every expert-authored pack, preserve immutable events from invitation through release:

- contributor and role pseudonyms with scoped authority evidence;
- recruitment channel and target population;
- consent, allowed/prohibited use, compensation, rejected-work policy, attribution/license, withdrawal boundary;
- candidate task ID, originating incident/evidence, submission/revision timestamps, author time;
- qualification instrument/version/result and reviewer assignment;
- acceptance, rejection, revision, withdrawal, and reason codes;
- task/rubric/source/reference transformations and approval expiration;
- denominator reports by domain and contributor, including concentration and unpaid/unused work.

Existing `expert-participation` and `expertise-transfer` contracts are the correct homes. Do not infer feasibility from retained count.

### 2. Add cross-instance semantic conformance to release checks

Before a rubric can score a task, verify more than IDs and hashes:

- every criterion traces to the assigned public requirement, source, artifact state, or fair consequence;
- task entities, dates, deliverables, source pack, reference, and rubric refer to the same instance;
- positive and negative criteria declare dependencies and double-penalty policy;
- multi-predicate criteria are split or explicitly modeled as gates with subchecks;
- numeric thresholds name estimand, unit, tolerance, authority, and alternate-valid cases;
- an adversarial substitution test swaps a nearby task/rubric pair and must fail closed.

The appendix's screenplay/clock mismatch is a concrete calibration case for criterion-operating-envelope consolidation, not a reason to create a new subsystem.

### 3. Treat exemplars as grader interventions

A ShotJudge-like experiment should use matched, held-out candidate responses and cross:

- zero-shot rubric only;
- one positive exemplar;
- one negative or borderline exemplar;
- paired positive/negative criterion-isolated exemplars;
- same-family versus different-family anchors;
- independent judge families;
- expert-only blind labels and adjudicated expert consensus.

Randomize exemplar choice/order, prevent an evaluated response from serving as its own anchor, hash all prompts/responses/rationales, and report criterion-level sensitivity, specificity, invalids, expert–expert reliability, judge severity/differential functioning, task-cluster uncertainty, and cost. Call the outcome agreement or classification performance unless probabilistic calibration is actually measured.

### 4. Keep score families and claims separate

Record, without premature aggregation:

- criterion satisfaction and evidence sufficiency;
- essential-gate failures;
- task-level weighted coverage;
- artifact/workflow success;
- safety/compliance violations;
- repeated-run reliability and cost;
- expert acceptance under blinded review;
- bounded validity claims.

A weighted checkpoint fraction is not a success rate. Domain means require explicit task-population weights and cluster-aware uncertainty. Professional competence and readiness require external workflow/consequence evidence.

### 5. Release immutable evidence, not only a live leaderboard

A minimally auditable release needs task/source manifests, contributor/authority summaries, rubric dependency records, accepted alternatives, Gold-sample IDs and selection, model/harness/tool/search configurations, raw outputs, anchor and judge prompts, criterion decisions/rationales, invalid/failure records, aggregation code, uncertainty, costs, licenses, and dated leaderboard snapshots. Private tasks may remain protected, but public manifests and commitment hashes must make selection and score replay inspectable.

## Concrete repository actions and queue decision

No new task was added. The evidence maps nonduplicatively to existing expertise-transfer, expert-participation, benchmark-bundle/grader, task-health, metric-monitoring, validity-argument, reference-observability, and criterion-operating-envelope work. Useful next implementation is to include the observed Education task–rubric substitution and one-shot-anchor treatment in those existing conformance and rater-ablation fixtures, not to create another XpertBench-specific schema.
