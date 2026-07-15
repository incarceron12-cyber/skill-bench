# LLM-generated rubrics: score correlation is a weak substitute for criterion and decision validity

- **Paper:** Hanhua Hong et al., *Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction*
- **Immutable version read:** arXiv:2607.12835v1, submitted 14 July 2026, <https://arxiv.org/abs/2607.12835v1>
- **Date read:** 2026-07-15
- **Full-text evidence:** complete immutable arXiv HTML, including appendices, at <https://arxiv.org/html/2607.12835v1>; local HTML `data/papers/source/2607.12835v1/2607.12835v1.html` (259,062 bytes; SHA-256 `0900cb7cbee49f8f0147454b80193c9e9ae0ee00170b09aec8714dd1143dfd46`); derived local text `data/papers/text/2607.12835v1-llm-rubric-generation-meta-evaluation.txt` (69,758 bytes; SHA-256 `d341c08ac8628535a2f23cfe06ae1031898c8f5b93ff107d9b8b3f7b1e3eba94`).
- **Acquisition provenance:** `data/papers/source/2607.12835v1/provenance.json`; arXiv API response `data/papers/source/2607.12835v1/arxiv-api.xml`.
- **PDF boundary:** the canonical immutable PDF endpoint returned HTTP 404 during this run. This is nevertheless a deep review, not abstract triage: the complete arXiv HTML main text, tables, prompts, category appendix, and threshold appendix were acquired and read. No page claims are made where only section/table locators are available.
- **Official-artifact boundary:** the complete v1 paper links no author-owned code, generated-rubric corpus, human checklist set, repository-score matrix, annotation protocol, prompts as executable files, skill document, or analysis package. Exact empirical replay and item-level audit are therefore unavailable.
- **Tags:** generated-rubrics, meta-evaluation, PaperBench, criterion validity, score alignment, skill distillation, clustering, human baseline

## One-sentence contribution

The paper usefully treats rubric generation as an object of evaluation and shows that in-context examples, an agentic scaffold, and a one-example distilled procedure are associated with higher agreement between generated-rubric and PaperBench repository scores, but its headline “near-human” result is an average of correlations computed from only five repositories per paper under the same unvalidated model evaluator, and therefore establishes neither criterion equivalence nor reliable rubric authorship.

## Why this matters for skill-bench

This review advances charter objectives A, B, C, and F through a cross-domain measurement case: it tests whether expensive human criterion authoring might be partially automated without silently changing what a benchmark measures. The bounded domain is ML-paper reproduction; the general uncertainty is whether a model-authored criterion set can inherit authority from expert criteria by producing similar aggregate scores.

The paper’s strongest contribution is the distinction between **intrinsic rubric resemblance** and **extrinsic induced-score alignment** (Sections 3.3–4.2). That is better than validating generated criteria only by plausible wording. Its most important negative lesson is that neither measure tests the full authority chain. A generated rubric can preserve repository rank while omitting a mandatory requirement, double-counting implementation details, misclassifying applicability, or changing a pass/fail decision. Correlation is especially permissive when there are only five candidate repositories and the same evaluator produces both score vectors.

Useful completion for `skill-bench` is therefore not a new rubric-generation subsystem. It is a strict promotion ladder for generated criteria using existing participation, criterion, grader, metric, task-health, and validity contracts: nomination may be automated, but criterion authority, dependency semantics, alternative-path fairness, decision behavior, and authoring-cost benefit require separate evidence.

## Research question and claim boundary

The paper asks whether LLMs can generate paper-specific reproduction rubrics that align with human-authored evaluation while reducing the authoring bottleneck. It compares four cumulative generation settings with two backbone families:

1. direct prompting with the target paper and instructions;
2. direct prompting plus one human checklist example from another paper;
3. the same materials inside a Claude Code/ReAct-style read/write scaffold; and
4. the scaffold plus a procedural skill distilled by Claude Opus from one rubric-authoring run.

Generated and human checklists contain criteria with integer importance scores from 1 to 5. A ChatGPT-4o-mini evaluator assigns criterion-level pass/fail labels after retrieving the ten repository files most relevant to each criterion. The study compares generated-rubric and PaperBench-ground-truth repository scores and also computes lexical/embedding similarity between criterion sets (Sections 3–4; Appendix A).

The evidence supports a narrow descriptive claim: for these 20 PaperBench papers, five pre-existing generated repositories per paper, one evaluator configuration, and the authors’ checklist and prompting realization, later cumulative settings produce higher reported average induced-score correlations than direct prompting. The best reported model setting has **Pearson 0.78 and Spearman 0.70** for Claude Sonnet; the human checklist baseline has **Pearson 0.83 and Spearman 0.75** (Table 1).

It does **not** establish that each augmentation causally contributes, that generated criteria are professionally correct or complete, that generated and human rubrics make equivalent acceptance decisions, that a generated rubric preserves mandatory/dependent requirements, that students are interchangeable with original PaperBench authors, that the effect transfers beyond paper reproduction, or that generation lowers total validated authoring cost.

A manuscript-level numerical problem further tightens the claim ceiling. The abstract and contribution list describe the strongest setting as Spearman 0.78 approaching a human baseline of 0.83. Table 1 labels those values as **Pearson**; the corresponding Spearman values are 0.70 and 0.75. The conclusion does not resolve the discrepancy. Reviewers should use the table labels and treat the headline statistic as internally inconsistent until raw analysis artifacts clarify it.

## Methodology and system

### Task and rubric lineage

The study uses all 20 PaperBench papers. Original PaperBench uses author-assisted hierarchical rubrics with 94–2,551 criteria per paper. This study instead represents rubrics as flat checklist items `(criterion, importance 1–5)` and reports a human checklist average of 83.2 items (Sections 1, 3.1, 4). Research students “with sufficient experience” manually re-annotate the papers in checklist form for the human baseline (Ethical Considerations).

The transformation is central but under-described. The paper does not report:

- annotator count, identity, qualifications by paper, assignment, independence, or compensation;
- whether original paper authors reviewed the flattened checklists;
- a criterion-level mapping from PaperBench tree nodes to checklist items;
- how dependencies, parent weights, execution/result categories, mandatory steps, or alternative implementations survive flattening;
- duplicate annotation, disagreement, adjudication, rejected criteria, or revision rounds; or
- whether the single in-context example and single skill-distillation paper are excluded from their target conditions and analyses.

Thus “human annotation” is not a second independent expert oracle. It is an undocumented student-authored transformation whose induced scores correlate with the original PaperBench instrument. As the existing PaperBench review shows, the original itself is a compensatory partial-reconstruction measure, not a validated successful-replication decision. Agreement with it inherits that claim ceiling.

### Four generation settings are cumulative treatment bundles

Direct prompting asks for comprehensive, critical, code-verifiable criteria and supplies importance definitions (Appendix A, Figure 3). The in-context condition adds one human-authored checklist. The scaffold condition changes not only “reasoning” but file access, iterative calls, intermediate state, termination behavior, and token opportunity. The distilled-skill condition adds a procedure summarized by Claude Opus after one scaffolded example and reuses it across targets (Section 3.2).

This sequence is operationally interesting but not component identification. Conditions are cumulative rather than factorial; run budgets, call counts, token totals, stopping behavior, context utilization, and repeats are not reported. There is no scaffold-without-example arm, skill-without-scaffold arm, random/document-control skill, multiple independently distilled skills, or matched-compute control. Consequently, monotonic table values cannot show that “each component contributes.” Later settings may benefit from more calls, more tokens, an advantageous example, stronger-model knowledge encoded in the skill, or interactions among them.

The procedural skill is also statistically singular. It is distilled once from one paper by one stronger model run. The paper does not release its text, identify the source paper, report source-target similarity, or repeat distillation. Apparent cross-paper benefit could reflect a reusable method, a favorable template, PaperBench-specific evaluator cues, or chance. It does not establish a stable class-level skill treatment.

Model identity is incomplete. The paper names Claude Sonnet, GPT-5.4, Claude Opus, Claude Code, ChatGPT-4o-mini, and Qwen3-Embedding-8B (Section 4), but does not provide exact endpoint IDs for all systems, provider dates, system prompts, temperatures, seeds, context limits, retries, parser behavior, call logs, or hashes. “Claude Sonnet” and “Claude Opus” are product-family labels, not replayable configured components.

### Extrinsic score alignment

For each paper, five reproduction repositories come from two PaperCoder configurations and three HiRAS configurations. Every repository is evaluated with the same ChatGPT-4o-mini under the generated rubric and the ground-truth rubric. For each criterion, the evaluator retrieves top-10 files and returns pass/fail. Importance-weighted pass fractions produce repository scores. Pearson and Spearman correlations are computed across the five repositories for each paper and then averaged across the 20 papers (Sections 3.3 and 4).

This is the study’s most consequential weakness:

1. **Each paper correlation has only five points.** Spearman rank correlation with five items is coarse and highly unstable; one rank swap materially changes it. No confidence interval, bootstrap, permutation test, or per-paper distribution is reported.
2. **The same five generating configurations recur across papers.** Repositories are clustered by reproduction system and paper. Treating paper-level correlations as exchangeable summaries does not model system or paper effects.
3. **The same evaluator grades both rubric conditions.** Shared retrieval, evaluator bias, model prior, and failure mode can inflate correlation. Alignment can mean that the judge reacts similarly, not that the criteria are equivalent.
4. **Correlation ignores calibration and decision loss.** A generated rubric may assign uniformly higher scores, compress gaps, or reverse threshold-near pass/fail decisions while retaining rank correlation. Table 1 supplies no MAE, bias, slope/intercept, threshold agreement, severe-error count, or criterion confusion.
5. **The target is not independent ground truth.** Ground-truth scores are themselves model-judge outputs under the original rubric, not fresh original-author decisions or executable replication outcomes.
6. **Top-10 retrieval changes observability.** Longer/finer generated rubrics create different queries and evidence views. File retrieval error, criterion granularity, and rubric quality are convolved.
7. **No repeated judge calls or invalid-output accounting appears.** Endpoint stochasticity and grading failures are unmeasured.

A high induced-score correlation therefore supports only a bounded **configured evaluator–rubric concordance** claim.

### Intrinsic similarity

For each generated criterion, maximum ROUGE-1/ROUGE-L overlap with any human criterion is averaged. Semantic matching uses Qwen3-Embedding-8B cosine similarity and threshold `τ=0.7`; a generated criterion is precise if it matches at least one human criterion and a human criterion is recalled if any generated criterion matches it (Section 3.3). Appendices test `τ=0.65` and `0.75`.

This many-to-many threshold rule does not establish semantic equivalence. Many generated criteria can all “match” one broad human criterion and count as precise; one generated criterion can match several human criteria and count as covering all of them. The method ignores importance-score agreement, polarity, applicability, dependency, evidence source, criterion type, mandatory status, and contradiction. Embedding similarity can reward paraphrase while missing changed thresholds or causal requirements.

Threshold sensitivity is substantial in absolute terms: human precision/recall/F1 changes from 0.91/0.85/0.88 at 0.65 to 0.62/0.42/0.49 at 0.75 (Appendix D, Tables 5–6). The ordering trend is more stable than the measurement level, but no human validation of criterion matches justifies calling 0.7 a semantic decision boundary.

## Evidence and results

Table 1 reports monotonic extrinsic increases across the cumulative Claude Sonnet conditions: Pearson/Spearman rise from 0.62/0.58 under direct prompting to 0.78/0.70 with the distilled skill. GPT-5.4 rises from 0.55/0.55 to 0.74/0.70. Human checklists score 0.83/0.75. Average generated criterion counts generally move toward the human average, while criterion length remains larger.

These are meaningful descriptive signals: procedural scaffolding and examples may help models construct a checklist whose aggregate use resembles the target instrument. But “approaching human” is not statistically established. There are no intervals or paired paper-level tests for the gap, and the human row is one undocumented reformulation rather than an estimated human distribution. The table also contradicts the paper’s 0.78-Spearman headline.

Intrinsic results are weaker and nonmonotonic. For Claude Sonnet, semantic precision falls from 0.76 to 0.74 while recall rises from 0.58 to 0.65; GPT-5.4 precision falls from 0.69 to 0.67 while recall rises from 0.49 to 0.61. The paper interprets recall gains as coverage improvement. That is plausible, but the matching rule permits granularity proliferation to raise recall without preserving atomicity or dependence.

The paper’s category analysis is more diagnostic. Human PaperBench rubrics allocate category-dependent shares among Code Development, Execution, and Result Match, whereas distilled Claude rubrics allocate over 60% to Code Development and under 21% to Result Match across categories. Reinforcement-learning ground truth gives Result Match 48.8% (Section 5.1, Figure 2). This supports a real failure signature: model-authored rubrics regularize diverse papers toward a code-centric template rather than adapting to domain-specific evidentiary priorities.

The qualitative DPO example reinforces this: generated criteria split implementation and hyperparameter details into more leaves with relatively high weights, while human criteria aggregate these details and give outcomes greater discriminative weight (Section 5.3, Table 3). Score-distribution plots show direct prompting concentrated at high importance and later settings becoming more bell-shaped, though all retain a high-score bias (Section 5.2; Appendix B). No quantitative calibration statistic, annotation of over/under-weighting, or link from importance to decision consequence accompanies this visual analysis.

Cost is absent. Eight NVIDIA L40S GPUs are named, but the paper reports no generation/judging calls, tokens, GPU-hours, wall time, dollars, failed calls, human hours for checklist reformulation, or review cost. A scalability motivation without a total-cost and quality-control ledger cannot establish that generated rubrics reduce the scarce expert burden rather than move it into validation and repair.

## Unique insight

The deepest transferable insight is a distinction among three forms of rubric equivalence:

1. **criterion equivalence:** the same obligations, thresholds, applicability conditions, dependencies, alternatives, and evidence authority are represented;
2. **measurement equivalence:** applying each rubric under admissible evidence produces sufficiently similar criterion and aggregate observations, including invalid/insufficient states;
3. **decision equivalence:** the rubrics support the same consequential accept/reject/escalate decisions under a declared loss function.

The paper measures fragments of the first through embedding similarity and a weak rank-based fragment of the second through five-repository score correlation. It does not measure the third. Yet the “reliable rubrics” framing slides among all three.

This distinction explains why aggregate alignment can be actively misleading. Suppose a generated rubric omits one noncompensatory safety or validity gate but adds ten correlated code-style checks. Across five mostly weak repositories, both rubrics may rank systems similarly, yielding high Spearman correlation. On the one repository that crosses a release threshold, the generated rubric can make the wrong decision. Correlation rewards portfolio ordering while concealing exactly the criterion omission that matters.

For `skill-bench`, generated rubrics should be treated as **candidate instrument transformations**, not delegated expert judgments. The promotion chain should be:

`source/expert claim → human-authorized criterion version → generated candidate + transformation lineage → semantic/dependency diff → adversarial alternatives and applicability tests → plural criterion labels → score/decision bridge → bounded release claim`

At each arrow, authority can expire. A distilled procedure may improve nomination coverage without acquiring authority to set thresholds or decide what is professionally mandatory.

## Comparison with existing project evidence

- **PaperBench** contributes dense author-assisted criteria, but its root score is compensatory partial reconstruction and its judge validation is leaf-level. This paper aligns to that instrument; it cannot exceed its replication claim ceiling. Flattening also risks erasing PaperBench’s hierarchy without fixing its missing executable dependencies.
- **ResearchRubrics** shows that decomposition is an executable theory of attention and that examples, dependence, applicability, and authority need explicit records. The present paper reproduces the same code-centric over-decomposition failure at generation time and lacks criterion-level human validation.
- **Rubric Modification** shows that text, examples, call topology, and aggregation are measurement interventions. The four cumulative conditions here change all of these while attributing gains to an augmentation hierarchy.
- **Many-Facet rater analysis** shows that agreement can hide severity and task interactions. This paper reports correlations but no rater/rubric severity, paper interaction, fit, repeat stability, or bridge-item analysis.
- **AgentRewardBench/judge-reliability evidence** requires observer-view and adjudication provenance. Here the same top-10-file model judge supplies both sides of the extrinsic target, creating shared-observer dependence.

The nonduplicate synthesis is: generated-rubric validation needs criterion, rater, task, and decision levels; one aggregate correlation cannot substitute for any of them.

## Limitations and validity threats

1. Twenty feasibility-filtered ML papers do not sample scientific or professional knowledge work broadly.
2. Five repositories per paper make each correlation coarse and unstable.
3. Repositories recur as five system configurations across papers, inducing system and paper clustering.
4. No per-paper coefficients, intervals, hypothesis tests, bootstrap, or hierarchical model are reported.
5. The abstract/contribution headline mislabels Pearson 0.78/0.83 as Spearman; Table 1 reports Spearman 0.70/0.75.
6. Correlation does not test score bias, calibration, threshold agreement, severe errors, or decision loss.
7. The same model evaluator grades generated and ground-truth conditions, creating correlated observer error.
8. Top-10 file retrieval conjoins criterion wording, retriever success, evidence view, and judge behavior.
9. No repeated judge calls, invalid-output ledger, or adjudication is reported.
10. PaperBench model-judge scores are treated as ground truth despite their own validity limits.
11. Human checklist transformation has no released mapping, protocol, authority record, agreement, or review lineage.
12. Research students are not shown to have original-author or domain-specific reproduction authority.
13. Flattening hierarchical rubrics may erase prerequisite and category semantics.
14. The four settings are cumulative bundles, not a factorial or compute-matched design.
15. The scaffold changes calls, context, tools, state, and termination, not only reasoning quality.
16. One in-context checklist gives no estimate of example-selection variance.
17. One undisclosed source paper and one Opus run give no estimate of distilled-skill variance or transfer.
18. The skill text and generated rubrics are unavailable for independent inspection.
19. Model/endpoints, prompts, runtime settings, parsers, and API dates are incompletely pinned.
20. Intrinsic many-to-many matching permits duplicate granularity to inflate apparent precision/recall.
21. Embedding matches are not human-validated and ignore weights, thresholds, dependencies, and applicability.
22. Absolute intrinsic values are highly threshold-sensitive.
23. Criterion counts and average lengths do not establish atomicity, coverage, or nonredundancy.
24. Category analysis is descriptive and based on one best setting/model; no uncertainty is reported.
25. Importance “calibration” is inferred from a bell-shaped distribution rather than decision-linked calibration.
26. No independent original-author or expert acceptance of generated criteria is measured.
27. No legitimate-alternative, hidden-obligation, contradiction, or applicability contrast set is tested.
28. No criterion-level confusion matrix identifies omissions, spurious additions, or weight errors.
29. Cost, latency, failed-call burden, validation labor, and net expert-time savings are absent.
30. No code, data, annotations, score vectors, generated rubrics, or analysis package is linked in v1.

## Reproducibility and operational realism

Instrument inspectability is moderate: the immutable HTML supplies definitions, equations, headline tables, base prompts, model-family names, category assignments, and threshold sensitivity. Result reproducibility is weak: the generated and human checklists, five repositories’ exact revisions, criterion labels, top-10 retrieval outputs, score vectors, model responses, skill document, run manifests, analysis code, and cost records are unavailable. The canonical PDF was temporarily unavailable, but the complete official HTML was acquired and preserved; this affects page citation, not main-text coverage.

Operational realism is bounded. Reading a paper, authoring executable-code criteria, and judging repositories are realistic pieces of scientific evaluation. The design does not exercise original-author review of generated criteria, collaborative revision, legitimate alternative implementations, rerunning experiments, scientific adjudication, release decisions, model drift, or rubric maintenance. It measures static corpus alignment under one evaluator, not an operational rubric-authoring service.

## Transfer to skill-bench

### Retain

1. Evaluate generated rubrics both intrinsically and by downstream behavior; never accept plausible wording alone.
2. Preserve a human-authored baseline and multiple candidate-generation conditions.
3. Inspect category/criterion composition and score distributions, not only one aggregate metric.
4. Treat procedural authoring guidance as a separately versioned intervention that may transfer across tasks.
5. Record qualitative failure signatures such as over-decomposition, high-importance bias, and domain flattening.

### Repair

1. Make criterion comparison typed: obligation, source authority, public basis, polarity, applicability, dependency, alternative path, evidence view, threshold, and consequence.
2. Use one-to-one or explicitly many-to-many adjudicated mappings; report omitted, spurious, split, merged, contradictory, and weight-shifted criteria.
3. Separate candidate nomination from expert authorization. Generated criteria remain unapproved until scoped reviewers accept or revise them.
4. Validate generated variants on held-out artifacts with paired criterion labels, legitimate alternatives, invalid/insufficient cases, and threshold-near decisions.
5. Report score bias, calibration, confusion, acceptance agreement, severe-error loss, and decision equivalence in addition to rank correlation.
6. Model clustering by task, artifact, generator, rubric version, criterion, and grader; repeat stochastic generation and judgment.
7. Factor or compute-match example, scaffold, skill, and stronger-model effects; use multiple source examples and distilled skills.
8. Preserve the full configured realization: component hashes, prompts, examples, skill, tool/call plan, budgets, endpoint IDs, outputs, retries, cost, and dates.
9. Measure net human time: source preparation, generation, criterion diff, expert review, adversarial calibration, repair, and maintenance.
10. Fail closed on the claim: generated-rubric score alignment does not license professional correctness, expert equivalence, scalability, or readiness.

### Test before promotion

A minimal cross-domain validation should use at least two materially different artifact families and include:

- independent expert-authored criterion sets with authority and disagreement records;
- generated candidates from repeated, held-out generation runs;
- planted split/merge, omitted hard-gate, redundant-detail, not-applicable, alternative-valid-path, and evidence-view cases;
- paired human and grader observations with criterion-level adjudication;
- decision thresholds and asymmetric loss, not only score/rank correlation;
- held-out task families and bridge items for rubric-version transport; and
- total authoring plus validation cost.

A generated variant may advance from `candidate` to `reviewed instrument` only when it preserves or explicitly changes the licensed construct and decision boundary. A faster draft that needs equal expert repair is not scalability evidence.

## Concrete changes for skill-bench

1. **Do not add a parallel schema task.** Existing expert-participation lineage, criterion provenance/dependency/applicability fields, configured grader identity, task-health revisions, metric specification, and validity arguments already provide the correct homes. Future fixtures should add a `generated_candidate` authoring origin and transformation record, but only when an executable calibration is scheduled.
2. **Use this source to constrain generated-rubric claims.** Intrinsic match supports only candidate-overlap evidence; induced-score correlation supports configured instrument concordance; neither supports criterion authority, expert equivalence, professional validity, cost reduction, or readiness.
3. **When the next plural-grader/rubric calibration is run, plant one omitted hard gate with compensating redundant criteria.** Require the report to show high possible rank correlation alongside failed decision equivalence. This directly tests the paper’s central blind spot without narrowing the benchmark to paper reproduction.
4. **Add no queue item now.** The evidence implies a validation case inside existing machinery, not a nonduplicate subsystem; the current queue already contains consolidation/build work and no real expert rubric-generation calibration is ready to execute.

## Action items completed

- [x] Acquired and read the complete immutable v1 arXiv HTML, including all appendices; preserved source, derived text, metadata, hashes, and PDF unavailability.
- [x] Reconstructed rubric lineage, four cumulative settings, model/evaluator identities, five-repository extrinsic design, intrinsic matching, human baseline, category analysis, and claim limits.
- [x] Audited the Pearson/Spearman headline contradiction, tiny within-paper correlation sample, shared-evaluator dependence, clustering, transformation authority, cost, and absent release artifacts.
- [x] Compared nonduplicatively with PaperBench, ResearchRubrics, rubric-modification, many-facet rater, and judge-reliability evidence.
- [x] Mapped implications to existing contracts and added no duplicate task.
