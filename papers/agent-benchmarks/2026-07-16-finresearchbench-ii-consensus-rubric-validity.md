# Paper Review: FinResearchBench II — Consensus-Derived Rubric Validity

- **Paper:** https://arxiv.org/abs/2607.12252v2
- **Authors:** Beidi Luan, Rui Sun, Sinuo Wang, Yan Gu, Chao Li, Zhenliang Xiong, Jing Li, and Zuo Bai
- **Date read:** 2026-07-16
- **Venue / source:** arXiv preprint
- **Version read:** immutable v2, 15 July 2026; compared with immutable v1, 14 July 2026
- **Local v2 PDF:** `data/papers/pdfs/2607.12252v2-finresearchbench-ii.pdf` (11 pages; SHA-256 `76002c04527b22ff8844b0162773db6bf20e783a16e1367a94da6d143b27e91e`)
- **Local v2 text:** `data/papers/text/2607.12252v2-finresearchbench-ii.txt` (SHA-256 `859cc0ea1178cfa81dc64aa4419f0e595dbba7f19a419fe2763909405e24348d`)
- **Local v2 HTML / metadata:** `data/papers/source/2607.12252v2.html`; `data/papers/source/2607.12252v2-metadata.xml`
- **Immutable v1 comparison:** `data/papers/pdfs/2607.12252v1-finresearchbench-ii.pdf`; `data/papers/text/2607.12252v1-finresearchbench-ii.txt`; `data/papers/source/2607.12252v1.html`
- **Release status:** no author-owned code or data URL appears in the complete v2 paper, HTML, or API metadata; exact-title and arXiv-ID web searches on 2026-07-16 found no verifiable author-owned release. This is an acquisition-time finding, not proof that none exists.
- **Tags:** generated-rubrics, consensus, llm-judge, selection-bias, report-evaluation, rater-reliability, criterion-authority, validity

## One-sentence contribution

FinResearchBench II offers a computationally cheap method for selecting model-generated binary criteria whose labels are stable across three LLM judges and vary across ten reports, but its evidence validates a **panel-relative, outcome-selected comparison instrument**, not “gold” criterion correctness, expert-equivalent measurement, professional report quality, or readiness.

## Why this matters for skill-bench

The paper targets a real bottleneck in charter objectives B and C: query-specific professional reports can require many checks, while expert authorship and execution are expensive. Its useful design move is to make rubric retention an empirical process rather than accept every plausible generated criterion. A three-judge unanimity screen rejects criteria that the configured panel cannot apply consistently, and a separate non-triviality screen rejects criteria that label all ten reports alike.

The incisive lesson, however, is that **stable execution and observed discrimination are task-health properties, not criterion authority**. FinResearchBench II constructs criteria from the same ten systems' reports, selects criteria using those reports' labels, and reports separation on those labels. The resulting 14,450→3,687→2,600 attrition is evidence that generation produces many unstable or one-sided checks. It is not evidence that the survivors encode professionally necessary, factually correct, complete, fair, or decision-relevant requirements.

This distinction matters across domains. A criterion can be unanimous because it checks an obvious surface feature, discriminate because one evaluated artifact happens to mention that feature, and still be irrelevant to the intended professional decision. Conversely, a crucial but difficult judgment can be legitimately disputed and therefore be deleted. Optimizing only for consensus and score spread risks a benchmark of what the configured judges agree they can see, not what experts need the work product to accomplish.

## Research question and claim boundary

The paper asks whether long-form financial-report rubrics can be generated and executed at scale without experts in the final loop. It operationalizes that question through four narrower tests (Section 5, pp. 5–8):

1. Is one model's batched binary grading stable across three repeated rollouts?
2. Does unanimity among three LLM judges predict unanimity among three financial analysts?
3. How selective are unanimity and cross-system distinguishability filters?
4. Do retained criteria produce stable separation among ten deep-research products?

The evidence supports bounded claims that:

- the authors collected 104 privacy-processed queries from one deployed service in February–March 2026 and generated 1,040 reports;
- one sampled repeated-call diagnostic reports 90.99% identical labels across three runs on 6,625 rubric evaluations;
- on 4,052 sampled rubric–report items, LLM-panel and human-panel majority labels agree 90.42%, while 2,829 of 2,867 jointly unanimous items have the same binary label;
- the configured three-LLM panel retains 3,687/14,450 criteria under an all-reports unanimity rule and 2,600 after requiring both positive and negative outcomes;
- these selected labels yield materially different pass rates for the ten included systems, and broad rank order is insensitive to deleting one panel member or selecting distinguishability on seven of ten systems.

It does **not** establish that the query sample represents financial-research demand; that candidate criteria are semantically correct or professionally authoritative; that the human panel supplies a reliable gold standard; that consensus labels are factually grounded; that pass-rate differences represent decision utility; that rankings transport to new systems, dates, sources, languages, or judge panels; or that experts can be removed from rubric definition, validity review, threshold setting, or consequential use.

The authors partly acknowledge this boundary on p. 4: “gold” denotes reproducibility and informativeness under their pipeline, not independent semantic correctness. That caveat is important and should govern interpretation more strongly than the paper's recurring “high-quality,” “expert-free,” and report-quality language.

## Methodology

### Query provenance and sampling

Queries come from user interactions with a deployed financial deep-research service during February–March 2026. The authors report anonymization and PII removal, identify seven broad categories, and say they use stratified random sampling to select 104 queries while balancing analytical complexity, temporal diversity, and entity coverage (Section 3.1, pp. 2–3). Figure 2 then displays 14 finer labels, from Individual Stock Identification (16.0%) to Information Query (2.8%). Appendix B gives one translated example per broad category; original queries are Chinese.

This is stronger demand provenance than brainstormed prompts, but “real-world” does not itself establish ecological validity. The paper omits the source-population size, inclusion/exclusion rules, category classifier and reliability, per-stratum counts, duplication policy, language/region/user mix, query rewrite delta, consent or governance basis, invalid/unsafe-query attrition, and relation between the seven sampling strata and 14 plotted labels. “Balancing” three properties is not reproducible without definitions or a sampling ledger. One service over two months supports current-service demand provenance, not the prevalence or consequence structure of financial research generally.

### Reports and candidate-rubric construction

For every query, the authors collect ten product reports, yielding 1,040 artifacts. LLMs then synthesize binary query-specific criteria “directly from model outputs,” covering Comprehensiveness, Insight, Instruction Following, and Readability, for 14,450 candidates (Section 3.2, p. 3). The average is 138.94 criteria per query.

The candidate-generation stage is the largest unobserved transformation in the pipeline. The paper does not identify the generating model or number of generators, provide the generation prompt, define the four dimensions, report criterion deduplication or atomicity checks, preserve report→criterion locators, specify whether every report contributes symmetrically, or disclose rejected generations. It also does not identify all ten report systems at this stage, generation dates, endpoint versions, retrieval environments, prompts, budgets, retries, missing/invalid reports, artifact lengths, citations, or costs.

This creates **report-conditioned criterion dependence**. Criteria can encode content, omissions, styles, and errors present in the evaluated systems rather than an independent theory of good work. A union of model reports may improve coverage relative to one reference, but it cannot discover a professionally necessary consideration absent from all reports. Nor does extraction from an artifact establish public basis: a generated check can reward an answer fragment that no task instruction or legitimate professional consequence requires.

### Evaluation prompt and evidence view

Appendix A (p. 11) supplies the complete reported grading prompt. A judge receives the user query, one report, and one criterion, is cast as a professional financial-report reviewer, and must return only `Yes` or `No`, without explanation.

The binary interface is operationally simple but epistemically thin. It preserves no evidence quote, report locator, source lookup, confidence, applicability state, ambiguity, contradiction, invalid-output reason, or adjudication trace. The artifact-only evidence view may support presence, readability, and some instruction-following predicates. It cannot independently verify citation existence, source entailment, authority, freshness, calculations, or whether an investment recommendation was justified at task time. “No” conflates absence, falsehood, insufficient evidence, inapplicability, judge failure, and disagreement.

The paper gives no judge system prompts beyond Appendix A, temperatures, seeds, endpoint dates, context/truncation policy, parser, retry policy, call logs, token usage, or monetary cost. The claim that expert removal makes the process scalable is therefore plausible as a call-count argument but unsupported as a measured cost/latency/quality frontier.

### Within-model batched stability

For a query–report pair, the executor places its entire query-specific criterion set—around 100 items—into one prompt and requests all binary labels in one shot. A sampled subset is executed three times. Table 1 (p. 5) reports 6,625 rubric evaluations, mean majority share 0.970, 90.99% all-three agreement, and 9.01% with at least one flip. Insight is least stable at 89.96%; Instruction Following is most stable at 93.15%. The reported format-error rate is zero.

The diagnostic does not identify the repeated model, number of query–report batches, sampling scheme, prompt-list order, batch lengths, whether reports or criteria repeat across the 6,625 labels, or uncertainty under query/report clustering. “6,625 rubrics” is a label count, not an independent-trial count. Because all criteria in a report share one prompt and context, label errors can be correlated. Three repetitions estimate one configured model/prompt's short-run repeatability; they do not establish inter-model agreement, stability across endpoint updates, or correctness.

Batching is also a treatment. Criterion order, neighboring criteria, context pressure, and one malformed item can affect many labels. A one-item call and an approximately 100-item call are not measurement-equivalent until tested on matched items.

### Human–LLM comparison

The validation sample contains 4,052 rubric–report items spanning all seven broad query categories and all four rubric dimensions (Section 5.2, pp. 5–6). The three humans are financial analysts with securities-research backgrounds and approximately ten years' experience each. The LLMs are `gpt-5.4`, `claude-opus-4-7`, and `gemini-3-pro-preview`.

The manuscript does not report how the 4,052 items were sampled from the roughly 144,500 candidate rubric–report combinations, how many queries/reports/rubrics they represent, whether sampling was balanced or prevalence-weighted, whether experts were blinded to product identity, whether all labels were independent, what evidence experts could inspect beyond the report, training/calibration, compensation/time, conflicts, response order, missing labels, or adjudication. Pairwise statistics imply a crossed three-by-three labeling design, but exact assignment and batching are not specified.

The observed unanimity matrix is informative but easy to overstate:

- LLMs are unanimous on 3,436/4,052 items (84.80%).
- Humans are unanimous on 3,112/4,052 items (76.80%), inferred from the reported matrix.
- When LLMs are unanimous, humans are unanimous on 2,867/3,436 (83.44%); this is a 6.64-point enrichment over the human-unanimity base rate, not proof of correctness.
- Joint unanimity covers 2,867/4,052 (70.76%) of the sample. The headline 98.67% same-label rate is conditional on this selected subset and excludes 1,185/4,052 (29.24%) items where at least one panel disagrees.
- Across all items, majority-label agreement is 90.42% with κ = 0.8076. Majority voting suppresses internal disagreement, so this is panel-decision concordance, not individual-rater equivalence.
- Mean LLM–human pairwise agreement is 0.848 and mean κ 0.694, while human–human agreement is 0.811 with κ 0.569–0.678 (mean 0.622). Without clustered uncertainty, criterion prevalence, per-rater severity, or matched error analysis, the numerical ordering does not show that LLMs are “better than” experts.

Cohen's κ on jointly unanimous items (`0.9733`) answers a very narrow conditional question: given that both panels independently collapsed to one label, do their labels match? It is not a reliability estimate for the full instrument and cannot validate the retained criteria's authority. Human unanimity itself may reflect shared blind spots, task ambiguity, or an artifact-only evidence view.

### Exact filtering and scoring

The full pipeline applies the three LLM judges once to each of ten reports for every candidate criterion:

1. **Candidate pool:** 14,450 criteria across 104 queries.
2. **Strict consistency:** retain a criterion only if all three judges agree on every one of its ten reports. This leaves 3,687 (25.52%).
3. **Distinguishability:** among survivors, retain a criterion only if its ten unanimous/majority labels include at least one `Yes` and one `No`. This leaves 2,600 (70.52% of stage 2; 17.99% overall).

Among the 1,087 criteria removed at stage 2, 1,056 (97.15%) are always-yes and 31 always-no. Final query-level counts range from 6 to 47, averaging 25.

This is transparent attrition but not a gold-standard derivation. Strict consistency selects **panel executability under one observed labeling pass**. It does not repeat each of the three judges, so it conflates cross-model agreement with temporal reliability. Requiring agreement on all ten reports also makes retention a function of report count and item difficulty. A professionally important criterion with one borderline report is deleted; a trivial surface criterion can survive.

The second filter explicitly conditions the instrument on observed system outcomes. For every surviving criterion, majority is redundant with unanimity because stage 1 already requires all three judges to agree per report. Selection then requires variance in exactly the labels later averaged into product pass rates. Removing mostly always-yes items must lower pass rates and tends to increase spread; the reported top-to-bottom spread rising from 25.63 to 36.35 points is therefore partly a mathematical consequence of outcome-conditioned item selection, not independent evidence of improved report-quality validity.

The score is an unweighted mean over selected query-specific binary labels. It gives every criterion equal weight, allows rubric-rich queries to dominate the item-level score, and offers query-macro averaging as a second view. Neither aggregation models criterion dependence, dimension balance, severity, applicability, error cost, hard gates, or stakeholder decisions. A 58.58% pass rate has no calibrated meaning such as acceptable report, sound investment analysis, expert equivalence, or readiness.

### Systems, ranking, and sensitivity

Table 3 (p. 7) lists nine public products; an internal system is described separately. On the 2,600 selected criteria, item pass rates range from Kimi at 58.58% through Doubao/Gemini near 53% to Perplexity at 22.23%. Item and query-macro orderings are similar. The paper appropriately warns that Doubao versus Gemini and ChatGPT versus Qwen should be treated as ties rather than statistically meaningful adjacent ranks.

No confidence intervals, query bootstrap, repeated report generation, repeated judge panel draws, missing-run accounting, significance tests, or rank probabilities are reported. Thousands of criterion labels do not create thousands of independent report-quality observations: criteria nest within 104 queries and share reports, prompts, judges, source conditions, and candidate-generation lineage. The effective sample for system transport is much closer to the number and diversity of queries than 2,600.

Two sensitivity analyses are helpful but bounded:

- Leave-one-judge-out rankings correlate `ρ = 0.988` with the full panel. Each two-judge panel overlaps the baseline and uses the same artifact pool, generated criteria, and broad selection logic; this checks panel-member leverage, not judge-family transport or criterion truth.
- Across 120 seven-system selection / three-system holdout splits, full-ranking correlation averages 0.978 (minimum 0.891), and held-out triple order is preserved in 112 splits. But candidates were generated from all ten reports, and the paper says only the distinguishability filter selects on seven systems; it does not establish that candidate generation and consistency filtering exclude held-out reports. This is partial system holdout, not an independent instrument-development split. It tests interpolation among the same ten systems, not transport to a new product, version, time, or report distribution.

The product ordering may be real for this configured panel and artifact snapshot. It is not auditable because queries, reports, criteria, labels, model configurations, and analysis code are unreleased.

### v1-to-v2 boundary

The immutable versions are substantively almost identical. Whitespace-normalized full-text comparison found that v2 adds discussion and a formal reference for the authors' predecessor FinResearchBench logic-tree framework in Sections 2.2–2.3 and the bibliography, plus a disclosure-of-interests statement. Counts, methods, prompts, tables, reported labels, scores, sensitivity analyses, and limitations are unchanged. V2 therefore improves related-work positioning but does not repair the absent generation protocol, release, statistical uncertainty, evidence-view, cost, or validity warrants.

## Evidence and results interpretation

The strongest empirical result is negative: 74.48% of generated criteria fail an all-reports, three-judge consistency rule, and another 1,087 stable criteria are one-sided on the ten systems. Automatic criterion generation produces a large amount of evaluation material that should not be trusted merely because it sounds plausible. This supports task-health screening, immutable criterion lineage, and disagreement diagnostics.

The human comparison supports use of LLM unanimity as a **precision-oriented triage signal for human-panel unanimity** in this sample. It does not support “expert removal” broadly. Experts still define what professional quality means, whether a disputed criterion is essential, what evidence a judge needs, how errors should be weighted, what score warrants an action, and whether the instrument remains valid after systems or markets change. The paper removes expert *execution* from one binary labeling stage after one sampled comparison; it does not remove expert authority from a defensible evaluation lifecycle.

The ranking evidence establishes discrimination by construction and panel-relative score reproducibility more strongly than validity. A high score means the report receives more `Yes` labels on criteria that (a) were generated from this report pool, (b) all three judges labeled identically across this ten-system set, and (c) had at least one positive and one negative outcome. That is a precise instrument definition. It should not be paraphrased as percentage of financial-research quality.

## Unique insight

The paper exposes a three-way trade-off that is often hidden in rubric pipelines:

> **criterion authority, execution reliability, and benchmark discrimination are independent axes, and filtering on one can damage another.**

Unanimity filtering can improve operational reliability while preferentially deleting judgment-intensive expertise. Distinguishability filtering can increase score spread while deleting universally satisfied basics or universally failed critical requirements. Expert-free scaling can lower execution cost while freezing the values and blind spots of a model-generated, artifact-conditioned criterion pool.

This suggests a typed criterion-health lifecycle for `skill-bench`:

`candidate authority review → evidence-view admissibility → repeated execution reliability → non-triviality diagnostic → independent outcome/decision validation → operational role`

A criterion should not skip from “three judges agree and systems differ” to “gold.” Depending on evidence, it may become:

- a **regression discriminator** for a frozen system cohort;
- a **panel-stable artifact predicate**;
- a **diagnostic-only check** whose professional importance is unknown;
- a **critical gate** retained despite low cross-rater agreement, with expert adjudication;
- or a rejected criterion due to unfair basis, inadequate evidence view, redundancy, or construct irrelevance.

A second insight is that **disagreement is not merely noise to discard**. The human–human κ range and lower stability for Insight likely identify precisely the criteria where context, authority, or professional judgment needs explicit modeling. Deleting these items can make the benchmark psychometrically cleaner while narrowing the construct from consequential analysis to easy-to-observe compliance.

## Relation to existing evidence

- **ResearchRubrics** invests substantial human author/reviewer labor before scalable judging; FinResearchBench II replaces that authoring authority with report-conditioned generation and filters. Together they show that expert labor and judge calls are not substitutes: authoring/authority, evidence access, label reliability, and aggregation each need separate validation.
- **LLM-generated rubric meta-evaluation** finds aggregate score alignment can coexist with uncertain criterion authority and non-equivalent decisions. FinResearchBench II adds unanimity and distinguishability, but those still establish panel behavior and tested-system separation rather than semantic or decision equivalence.
- **PaperBench** demonstrates dense, author-assisted criteria and partial-progress utility while leaving completion claims bounded. FinResearchBench II is cheaper and less inspectable; binary flat means lose dependency and execution evidence, making readiness promotion even less defensible.
- **AsymmetryZero** separates model-jury agreement, repeated-call reliability, correctness, and decision equivalence. FinResearchBench II empirically illustrates the same separation: Table 1 studies one-model repeatability, Section 5.2 panel/human agreement, and Section 5.3 outcome discrimination, but no result validates decision equivalence.
- **Many-facet rater-effects work** warns that task, criterion, rater severity, system, and interactions should be modeled rather than averaged away. FinResearchBench II reports pairwise κ but no many-facet or clustered analysis; its apparent thousands of labels remain nested in 104 queries and a small fixed rater panel.

## Transferable design patterns

### 1. Keep generation, authority, reliability, and discrimination as separate gates

Record criterion generator and source artifacts, professional warrant, public basis, evidence-access requirements, repeated-call reliability, cross-rater behavior, prevalence/non-triviality, and external decision validity independently. A criterion can pass one gate and fail another.

### 2. Use unanimity for triage, not truth promotion

A precision-oriented unanimity screen can reduce human workload. Preserve the full confusion matrix, selection denominator, excluded-item characteristics, rater identities, evidence views, and uncertainty. Sample both retained and rejected criteria for expert correctness review; otherwise false exclusions and construct narrowing are invisible.

### 3. Split instrument development from evaluation

Generate candidates from an authoring/witness pool, tune reliability on calibration artifacts, select non-trivial criteria on a development system cohort, and estimate performance on unseen queries, reports, systems, and time snapshots. A system holdout is invalid for criterion independence if its report already contributed to candidate generation.

### 4. Treat distinguishability as diagnostic metadata

Store prevalence and information/discrimination estimates, but do not automatically delete always-pass or always-fail criteria. A universal pass may be an important regression guard; a universal fail may be a critical capability frontier. Operational role and decision consequence should determine retention.

### 5. Preserve disputed expertise

When experts disagree, record labels, rationales, context assumptions, source locators, confidence, and adjudication rather than collapsing or deleting. Evaluate whether disagreement reflects a defective criterion, insufficient evidence, legitimate multiple standards, or a genuinely judgment-intensive construct.

### 6. Match evaluator views to predicates

Presence/readability checks may use the artifact. Factual, citation, calculation, authority, and freshness checks require frozen sources or controlled retrieval plus locators. Professional recommendation quality requires qualified decision-context review or a separately validated proxy. `insufficient_evidence` and `not_applicable` must remain distinct from `No`.

### 7. Report dependence-aware uncertainty and costs

Use query-clustered or hierarchical uncertainty, repeated report generations, repeated judge draws, rank intervals, missing/invalid-call policy, and sensitivity to criterion dependencies. Preserve call topology, prompt/model hashes, tokens, latency, retries, and human time so scalability becomes an observed frontier rather than rhetoric.

## Limitations and validity threats

1. **No reproducible query sampling frame.** The source population, attrition, balancing rules, and seven-to-14 category mapping are absent.
2. **Demand provenance is narrower than ecological validity.** One service and two months do not establish prevalence, consequence, or professional workflow fidelity.
3. **Candidate generation is under-specified.** Generator identities, prompts, criterion definitions, transformations, deduplication, atomicity, and report locators are missing.
4. **Task–report–criterion co-design.** The ten evaluated reports supply the content from which their own criteria are generated.
5. **Coverage ceiling.** A necessary consideration omitted by every report cannot enter a report-derived candidate union.
6. **No criterion-authority validation.** Experts label report satisfaction, not whether criteria are professionally necessary, correct, complete, fair, or appropriately scoped.
7. **Public-basis risk.** Report-derived criteria may reward undisclosed answer fragments rather than fair consequences of the query.
8. **Artifact-only judge view.** Judges cannot independently verify sources, facts, calculations, authority, freshness, or real decision consequences.
9. **Binary outcome collapse.** `No` merges absence, falsity, inapplicability, insufficiency, ambiguity, and evaluator failure.
10. **Batched grading is unvalidated as measurement-equivalent.** Order, neighboring criteria, long context, and shared prompt errors can alter labels.
11. **Repeated-call diagnostic is opaque.** The judge model, batch count, sampling, ordering, nesting, and uncertainty are unreported.
12. **Human study sampling is opaque.** Item selection, query/report/rubric denominators, blinding, evidence access, training, and assignment are missing.
13. **Conditional headline agreement.** The 98.67% result excludes the 29.24% of items without joint panel unanimity.
14. **Human unanimity is not semantic truth.** Moderate human–human κ and absent rationales/adjudication leave authority unresolved.
15. **Pairwise agreement lacks uncertainty and severity modeling.** Nested items and rater/criterion/system interactions are ignored.
16. **Strict consistency selects observability.** One disagreement anywhere among ten reports deletes a criterion, including potentially consequential judgment items.
17. **Distinguishability is outcome-conditioned selection.** The same labels select the instrument and produce its reported spread.
18. **Always-pass/fail deletion can harm validity.** Universal basics and critical unsolved requirements may be operationally important despite low discrimination.
19. **Flat aggregation is uncalibrated.** Equal criterion weights ignore dependence, severity, dimensions, applicability, gates, and loss.
20. **No inferential ranking uncertainty.** Adjacent ties are acknowledged, but no clustered confidence intervals or rank probabilities are estimated.
21. **Partial holdout is not independent transport.** Held-out systems contributed reports to candidate generation; only distinguishability selection is described as held out.
22. **Fixed-panel sensitivity is narrow.** Leave-one-out panels overlap heavily with the baseline and do not test new judge families or endpoint drift.
23. **Temporal and version validity are unresolved.** Financial facts, products, retrieval results, and preview judges can all change.
24. **Scalability is not measured.** No token, latency, dollar, human-time, or quality–cost accounting is reported.
25. **No inspectable release.** Queries, reports, criteria, labels, prompts for generation, configurations, and analysis code are unavailable.
26. **Privacy governance is under-specified.** Anonymization/PII removal is stated, but consent, review, residual re-identification, and release policy are not.
27. **Professional and consequential validity are absent.** No stakeholder decisions, accepted-report threshold, downstream outcome, harm, or expert acceptance study is observed.
28. **V2 does not address methodological gaps.** Its substantive change is predecessor-framework positioning, not additional audit evidence.

## Reproducibility and operational realism

Reproducibility is weak. The immutable v2 PDF, text, HTML, metadata, exact binary evaluation prompt, aggregate counts, and result tables are preserved locally. The v1 comparison confirms stable reported results. Those artifacts are sufficient to reconstruct the conceptual filter and audit arithmetic.

They are insufficient to reproduce any experiment. There is no query/rubric/report corpus, candidate-generation prompt, model configuration, label table, batching manifest, random seed, run ledger, human annotation file, analysis code, environment, or cost record. The three judge names include a preview endpoint, and report products are mutable services. Even exact reimplementation would evaluate a different configured system and likely different web state.

Operational realism is mixed. Real service queries and long product reports are more realistic than short synthetic QA. Query-specific criteria and report-level comparison address heterogeneous artifacts. But the benchmark observes only final Chinese-language reports through a binary artifact-only judge. It does not inspect research plans, retrieval traces, source custody, calculations, revisions, clarification, stakeholder constraints, or realized decisions. The instrument is best understood as a frozen-cohort **report checklist discriminator**, not an end-to-end financial-research benchmark with demonstrated professional validity.

Release inspectability is currently the principal blocker. Because the 2,600 criteria and 1,040 reports are unavailable, outsiders cannot inspect hidden obligations, criterion duplication/dependence, answer leakage, factual errors, source dates, label asymmetries, system identity, or whether reported statistics replay.

## Concrete changes for skill-bench

1. **Do not add a finance-specific schema.** Existing criterion provenance, artifact-view admissibility, grader evidence-view, task-health, metric-monitoring, validity-argument, and rater-calibration machinery can represent the gaps.
2. **Add an outcome-selection firewall when consolidating criterion guidance.** Record every artifact/system used for candidate generation, reliability calibration, non-triviality selection, thresholding, and final estimation. Reject “held-out” claims when the artifact contributed upstream.
3. **Type criterion status rather than call it gold.** At minimum distinguish `generated_candidate`, `authority_reviewed`, `evidence_admissible`, `panel_stable`, `nontrivial_on_development_cohort`, `externally_validated`, `regression_guard`, and `decision_calibrated`.
4. **Retain prevalence without automatic deletion.** Use always-pass/fail labels to inform task-health roles and retirement decisions, not semantic validity. Require an explicit consequence/coverage argument before removal.
5. **Require selection-adjusted evaluation.** Performance evidence should come from unseen artifacts/systems/queries after instrument generation and selection; report both pre-filter and post-filter estimates with criterion/query clustering.
6. **Audit disagreement as a construct signal.** Sample unanimous and disputed criteria for independent expert authority, fair-basis, evidence-view, and consequence review; compare what unanimity filtering removes by dimension and severity.
7. **Preserve grader evidence.** Require evidence locators, source-view identity, applicability, insufficiency, invalid-output status, model/prompt/configuration hashes, repeated calls, and panel composition for every criterion observation.
8. **Separate seven claims in validity arguments:** label agreement, individual/panel reliability, criterion authority, measurement equivalence, benchmark discrimination, professional transport, and readiness. None should inherit approval from another.
9. **Require a scalability ledger.** Human author/review/adjudication time and model calls/tokens/latency/cost must accompany any expert-removal claim.
10. **Use FinResearchBench II as a negative conformance case.** A bundle with high unanimous agreement and broad score spread must still fail promotion to professional-capability/readiness when criterion authority, independent holdout, evidence access, threshold/loss, and release evidence are absent.

## Action items for repository

- [x] Read the complete immutable v2 PDF/text/HTML and verify metadata, every method, result table, prompt, appendix, disclosure, and limitation.
- [x] Compare immutable v1 and v2; document that v2 adds predecessor-framework positioning/reference and disclosure but no new evaluation evidence.
- [x] Reconstruct exact 14,450→3,687→2,600 attrition and distinguish label agreement, panel reliability, criterion authority, measurement/decision equivalence, discrimination, transport, and readiness.
- [x] Audit the 4,052-item human/LLM denominators and show that the 98.67% headline conditions on 70.76% joint-unanimity coverage.
- [x] Search for an author-owned release and preserve the bounded no-release-found result in `data/papers/index.json`.
- [x] Map implications to existing cross-domain contracts; add no duplicate build task.
