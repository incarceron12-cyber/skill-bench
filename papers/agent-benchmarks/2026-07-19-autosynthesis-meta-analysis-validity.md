# AutoSynthesis: endpoint proximity does not validate an evidence-synthesis chain

## Bottom line

AutoSynthesis contributes a useful knowledge-work decomposition: turn a natural-language question into a protocol; search and acquire sources; preserve screening decisions; map studies and outcomes; extract and verify statistics; compute effect sizes deterministically; assess heterogeneity and bias; and emit a PRISMA-like report with intermediate records. This is exactly the kind of source-to-artifact pipeline that `skill-bench` should be able to represent and diagnose.

The empirical evidence is much narrower than the paper's broad framing. The immutable v1 reports one end-to-end persuasion meta-analysis, not the claimed several reference cases across human–AI interaction, education, and psychology. Its automatic synthesis retrieves 28 records, quantitatively includes eight papers and 20 effect rows, and shares only seven matched effect estimates with one author-overlapping human benchmark. Those seven estimates have `r=.69`, `p=.085`, and an OLS slope of `1.62`; no extraction-field accuracy, repeated-run reliability, or independent eligibility/risk-of-bias agreement is reported.

Most importantly, endpoint closeness hides a decision reversal. The human meta-analysis reports `g=.020`, 95% CI `[-.048,.093]`, `p=.530`; AutoSynthesis reports `g=.143`, 95% CI `[.059,.226]`, `p<.0008`. One is compatible with no average effect and the other declares a positive effect. Calling the `Δg=.123` “broadly similar” because it falls inside a borrowed `±.20` tolerance ignores the intended interpretation and decision. The automatic model also appears to treat 20 effects from eight included papers as 20 independent units (`df=19`), despite repeated outcomes/components within papers, making its precision, heterogeneity, Egger test, moderator results, and significance difficult to interpret.

The strongest warranted claim is: **one unreleased, single-run, GPT-5.4-mini/OpenRouter workflow produced a complete-looking meta-analysis artifact and a pooled point estimate within `.123` Hedges' g of one related human synthesis, while exposing material retrieval, eligibility, extraction, dependence, statistical-validation, and claim-interpretation gaps.** It demonstrates pipeline feasibility, not accurate automated meta-analysis, PRISMA compliance, cross-domain reliability, scalability, living-review safety, or evidence-based decision support.

## Source and evidence status

**Deep review of the complete immutable arXiv v1 paper, all supplementary prompts/tables, and the complete arXiv source archive; release availability audited, but no official implementation or study release was available.**

- **Paper:** Moein Taherinezhad, Sebastian Maier, Gerardo Vitagliano, Francesco Pierri, and Stefan Feuerriegel, *AutoSynthesis: An agentic system for automated meta-analysis*, arXiv:2607.15247v1 (16 July 2026), <https://arxiv.org/abs/2607.15247v1>.
- **Date read:** 2026-07-19.
- **Local PDF:** `data/papers/pdfs/2607.15247v1-autosynthesis.pdf` (49 pages; SHA-256 `ec4e78b7edb56fe714afa0bb5c2a8e24c474297b9ab55cf9d7271be037c6d99a`).
- **Complete text:** `data/papers/text/2607.15247v1-autosynthesis.txt` (SHA-256 `fb7beb1b60abe53751e7de270e23945845f541dfe9d01e29f8aed5d56a7dcbb3`).
- **Metadata:** `data/papers/source/2607.15247v1-metadata.xml`.
- **Complete source:** `data/papers/source/2607.15247v1-source.tar.gz` (SHA-256 `3c09e6472a5bb7c9a9c9318046338bec1032ff4bed724901314a2710d7f117a0`).
- **Release audit:** `data/sources/releases/2607.15247v1-autosynthesis/provenance.json`.

The source archive contains the manuscript, bibliography/style, overview figure, and sixteen persuasion-analysis figures. It contains no implementation, exact configuration, frozen protocol, search rows, source corpus, parsed documents, screening labels, extraction rows, effect-size inputs, statistical routines, traces, final generated report, or environment lock. The paper says data and code **will** be released but gives no URL (p. 27). Exact-title, ID, author, and GitHub searches found no author-linked release at audit time. A post-v1 third-party repository calling itself “official” was excluded: it is not author-owned or paper-linked and contains placeholder clone/contact text and a wrong 2023 citation year. Search absence is time-bounded, not proof that no later release will appear.

Page references below use PDF pages.

## One-sentence contribution

AutoSynthesis maps a full quantitative evidence-synthesis workflow onto specialized LLM agents plus deterministic statistical modules, but validates only one unreleased end-to-end run whose similar-looking pooled point estimate masks changed study composition, dependent effects, weak stage-level evidence, and a reversed significance conclusion.

## Why this matters to `skill-bench`

This review advances charter objectives A, B, C, and E through a high-consequence, cross-domain knowledge-work question:

> When does an end-to-end professional artifact support only package completion, and when can it support stage correctness, reproducibility, methodological validity, or a stakeholder decision?

Meta-analysis is the case, not a scope boundary. The reusable chain is:

```text
question and intended use
→ frozen protocol and authority
→ search universe and source-access state
→ screening observations and adjudication
→ study/outcome/dependence map
→ source-located statistical extraction
→ transformation and effect-size witness
→ dependence-aware synthesis
→ bias/sensitivity evidence
→ report proposition and uncertainty
→ expert acceptance / correction
→ downstream decision and consequence
```

A pooled estimate close to a reference can result from a valid chain, compensating errors, changed scope, correlated effects, or a forgiving endpoint tolerance. A professionally formatted report cannot distinguish these mechanisms. `skill-bench` should score the joins and preserve noncompensatory stage failures rather than treating endpoint agreement as evidence that the workflow was correct.

## Research question and claim boundary

The paper asks whether an agentic framework can automate the complete meta-analysis workflow from a natural-language question through quantitative synthesis and reporting (pp. 3–5, 17–27). It further frames the system as reproducible, scalable, near-real-time, transparent, cross-domain, and potentially useful for evidence-based decisions and living meta-analyses.

The evaluated construct is much narrower:

- one user question about LLM-generated persuasive messages;
- one default LLM-generated protocol, without expert refinement;
- one July 2026 search realization;
- one GPT-5.4-mini/OpenRouter configured pipeline;
- one related published human meta-analysis, sharing an author with AutoSynthesis;
- 28 retrieved records, eight quantitatively included papers, and 20 selected effect rows; and
- one unreleased final analysis.

This can support a **configured single-run artifact-feasibility claim**. It does not by itself support accurate evidence synthesis, cross-domain transport, cost/time savings, reproducibility, expert substitution, safe living updates, methodological rigor for non-specialists, or decision utility.

## Methodology and system

### Protocol formation

The planning agent converts the user's question into treatment/control labels, outcomes, inclusion/exclusion criteria, search terms, moderators, a start year, and an expected effect direction (pp. 17–18; Supplement pp. 39–40). Human refinement is allowed, but the experiment uses the default generated protocol.

This is a useful explicit intermediate artifact. It is not a registered protocol. No timestamped protocol object, revision log, rationale, expert approval, deviation ledger, or evidence that choices preceded search/results is released. Asking the agent for an “expected direction” can standardize signs, but it also creates directional anchoring. The prompt requires broad criteria and says to err heavily toward inclusion; that is one authored recall/precision policy, not a universal systematic-review rule.

The paper says the search agent generates Boolean queries (p. 19), while the released planning and query prompts explicitly ask for short keyword phrases and say not to use Boolean syntax unless essential (pp. 39–40). This is a small but concrete manuscript–instrument mismatch.

### Search, deduplication, and full-text access

The search layer queries arXiv, Semantic Scholar, CrossRef, OSF Preprints, and PubMed, with configurable proprietary sources (pp. 18–20). Results are capped at 40 per database to control cost, aggregated, deduplicated by normalized title, and initially filtered by regular expressions. Full texts are fetched through source APIs, direct links, DOI resolution, and web fallback, then parsed through MinerU, LlamaParse, Mistral OCR, or conventional extraction.

The layered access design is operationally sensible and makes access failures visible. It is not a reproducible systematic search without:

- exact queries per source;
- API versions, sort/ranking behavior, pagination, returned totals, and dates/times;
- cap-truncation evidence;
- raw result rows and deduplication clusters;
- DOI/version/preprint linkage beyond normalized titles;
- access credentials and fallback chronology;
- parser identity per document, extracted views, and quality checks; and
- explicit handling of corrections, retractions, supplements, figures, and multiple reports of one study.

A cap of 40 per database and only 28 total records may be appropriate for a demonstration, but cannot establish exhaustive retrieval. Title-only deduplication can both split the same study across reports and merge distinct papers with similar titles. Full-text inaccessibility is part of the configured system's observation envelope, not evidence that the underlying study is ineligible.

### Eligibility and study mapping

The eligibility agent checks empirical design, treatment/control comparison, quantitative outcomes, and topic relevance, logging reasons (pp. 20, 40–41). A study-mapping agent then identifies independent data-collection components, treatment/control groups, outcomes, and source sections (pp. 20–21, 40–42).

These are valuable objects for benchmark traces. Their validity is not measured here. The methods promise confusion matrices for eligibility decisions (pp. 25–26), but the results provide only aggregate overlap plus a post-hoc narrative reconciliation. No row-level labels, independent duplicate screening, agreement, adjudication protocol, or false-inclusion/false-exclusion severity is reported.

The human reference is also not an independent oracle. One AutoSynthesis author overlaps with the lead author of the reference meta-analysis and provides qualitative assessment of differences (pp. 24–25). That access is useful for interpretation but should be recorded as informed author adjudication, not blind external validation.

### Statistical extraction, validation, and outcome selection

The extractor first builds linked paper/study/hypothesis/outcome JSON and then extracts only relevant results. A second LLM validates whether core numbers occur verbatim or within rounding in the paper and can correct locatable values or remove unsupported ones (pp. 21–22, 43–44). A relevance classifier assigns outcome class, construct family, granularity, comparison arm, relevance, and priority before an algorithm selects winners (pp. 44–45).

Separating semantic mapping, numeric extraction, checking, and selection is the paper's strongest system-design choice. It still leaves several failure modes:

1. **Text occurrence is not semantic correctness.** A number can be locatable but belong to another group, outcome, model, time point, adjusted analysis, or denominator.
2. **Same-model correlated errors remain.** The extractor and checker use the same model family/configured source representation and no independent deterministic source locator or human adjudicator.
3. **Figures and supplements are weakly observed.** The checker relies on parsed text and captions; many needed statistics reside only in plots, images, footnotes, or supplementary files.
4. **Outcome-selection authority is hidden.** “Primary,” “central,” and “preferred” require protocol and domain judgment; the prompt itself says over-extract when uncertain, while the downstream winner algorithm is unreleased.
5. **The released relevance prompt is persuasion-specific.** Its comparison-arm rules explicitly target LLM/AI interventions and its priority ranks behavior, compliance/persuasion, attitude, intention, resistance, experiential, and mechanism outcomes. This is evidence of a configured persuasion instrument, not a domain-general selector.
6. **No extraction accuracy is reported.** Seven matched effect estimates are compared only through correlation/slope; no field-level exactness, source-locator correctness, sign accuracy, variance accuracy, correction yield, hallucination rate, or adjudicated error taxonomy appears.

### Effect-size computation and synthesis

Deterministic modules convert supported statistics to Cohen's d and Hedges' g, exclude nonconvertible rows, and run a custom Python REML random-effects model initialized with DerSimonian–Laird (pp. 22–23). The system also computes Q, `I²`, `τ²`, moderator analyses, leave-one-out analysis, Egger's test, trim-and-fill, funnel/scatter plots, cumulative synthesis, and risk-of-bias tables.

Using deterministic code for arithmetic is preferable to LLM calculation. “Deterministic” does not establish correct statistical specification or implementation. The custom routines are unreleased and are not validated against reference packages, simulation tests, analytic fixtures, or known edge cases. Conversion formula choice, sign coding, small-sample correction, standard-error derivation, zero cells, adjusted estimates, repeated measures, cluster designs, and missing covariance are unspecified.

The most serious issue is dependence. The analysis includes 20 effects from eight papers—2.5 effects per included paper on average. Table S4 contains repeated reports under shared study IDs and multiple study IDs under the same paper title. Yet Figure 2 and Table S2 call these `k=20`, report `Q(df=19)`, and fit an ordinary random-effects model as if each row were independent. No multilevel model, robust variance estimator, covariance matrix, within-study aggregation, cluster sensitivity, or study-level leave-one-out analysis is described. As a result:

- the confidence interval and p-value may be too narrow;
- `I²`, `τ²`, and Q mix within-paper and between-study variation;
- Egger's test treats dependent effects as independent studies;
- leave-one-effect-out is not leave-one-study-out;
- moderator subgroup counts can overstate independent evidence; and
- one paper with many selected outcomes can receive disproportionate influence.

This is not a cosmetic reporting issue. Dependence is part of the scientific construct and must be decided before pooling.

### Risk of bias and report generation

The bias agent is said to choose RoB 2 for randomized trials and ROBINS-I for nonrandomized studies (pp. 23–24). The displayed persuasion dashboard applies ROBINS-I domains across the included rows (p. 9). No domain-level supporting quotations, signaling-question answers, applicability decisions, independent raters, agreement, adjudication, or validation against the human review are released. Some included persuasion experiments appear randomized, so a uniform ROBINS-I display may itself be a tool-selection error; the released evidence is insufficient to resolve the design classification.

The report agent writes a “publication-quality” narrative and a PRISMA 2020 flow diagram (pp. 23–24, 46). The arithmetic in the displayed flow is internally coherent: 28 identified; 3 screened out; 4 full texts unavailable; 2 excluded after assessment; 19 eligible; 11 lacking convertible/extractable statistics; 8 included. That is useful artifact closure. PRISMA alignment is not PRISMA compliance: no completed checklist, registration, full search strategies, source-specific counts, duplicate-screening process, excluded-full-text ledger, data items, certainty assessment, protocol deviations, or reproducible analysis package is provided.

## Evidence and results

### Evidence-base construction

The automatic run retrieves 28 records, screens out three, fails to retrieve four full texts, judges 19 eligible, and includes eight papers with 20 effects (pp. 7–10). Against the seven-paper human evidence base:

- five overlap: raw recall `5/7 = 71.4%`;
- five of eight automatic inclusions overlap: raw precision `5/8 = 62.5%`;
- one human paper is missed by search;
- one is found but unavailable to the automatic full-text path;
- one automatic addition postdates the human search cutoff;
- one comes through a ResearchGate preprint source absent from the human search; and
- one is judged irrelevant by the reference review's lead author because it measures message preference rather than persuasion.

The paper then reports “corrected” recall `6/7 = 85.7%` and precision `7/8 = 87.5%` after qualitative reconciliation (pp. 10–11). These corrected numbers combine system error, access-envelope differences, time-cutoff differences, source-policy differences, and author adjudication. They are useful diagnostic dispositions, but not ordinary prospective precision/recall. A post-cutoff study is not a human false negative under the human protocol; an inaccessible paper is retrieved but not processable; a new source is a treatment difference; and the one substantive eligibility error remains.

Only `8/28 = 28.6%` of retrieved records and `8/19 = 42.1%` of eligible papers reach quantitative synthesis. The exclusions may be legitimate, but without rows they also create a major opportunity for outcome-conditioned attrition.

### Study-level quantitative agreement

Only seven effect estimates can be matched. The paper reports Pearson `r=.69`, two-sided `p=.085`, and an OLS slope of `1.62` when regressing benchmark effects on AutoSynthesis effects (pp. 11–13). This is weak evidence:

- `N=7` is too small for stable calibration;
- the association does not reject zero at `.05` under the paper's own test;
- slope `1.62` is far from identity and no intercept, confidence interval, MAE, signed error, concordance, or Bland–Altman analysis is shown;
- correlation is insensitive to common additive bias;
- matching is selected after both pipelines' retrieval and inclusion decisions; and
- 13 automatic effects and five human effects have no match, so the comparison ignores most rows that drive the endpoint difference.

This does not establish accurate quantitative extraction. It establishes that seven selected paired estimates have a positive but uncertain association.

### Pooled endpoint comparison

The manual benchmark reports:

- seven included papers and 12 effects;
- pooled `g=.020`, 95% CI `[-.048,.093]`, `p=.530`;
- `I²=75.97%`; and
- Egger `p=.018`.

AutoSynthesis reports:

- eight included papers and 20 effects;
- pooled `g=.143`, 95% CI `[.059,.226]`, `p<.0008`;
- `I²=88.3%`; and
- Egger `p=.006` (Table S2, p. 37).

The point-estimate difference is `.123`, inside the paper's borrowed `±.20` tolerance. But the analyses answer different evidence-base and weighting questions and imply different decisions about the null. The manual interval includes zero and its p-value is `.530`; the automatic interval excludes zero and its p-value is below `.001`. “Both estimates overlapped to a large extent” is also ambiguous: their confidence intervals overlap only over `[.059,.093]`, while each interval is an uncertainty statement around a different dependent-data analysis, not an equivalence test.

A tolerance developed for human reanalysis deviations is not automatically a decision threshold for meta-analysis-agent validity. Its relevance depends on domain loss, expected magnitude, outcome scale, direction, evidence composition, and intended use. Endpoint tolerance cannot repair an invalid dependence model or scope mismatch.

### Claimed breadth, robustness, and scalability

The introduction says the system performs several automated meta-analyses across human–AI interaction, education, and psychology and compares against reference cases [7,12] (pp. 4–5). The results, methods, supplementary tables, and source figures report only the LLM-persuasion case against [12]. No education/creativity run, second reference estimate, cross-domain table, or output is present. The phrase “across all reference cases” therefore has no inspectable plural basis in v1.

The discussion also says evaluations show operation across different LLM backbones, including open-weight models (pp. 15–16), but no model matrix, open-weight identity, configuration, result, repeat, or ablation is reported. Early single-agent and Claude Science attempts are described as insufficiently stable, with no run counts or failure ledger (p. 26). These are development observations, not comparative evidence.

One run takes about 0.5 hours, 1M input tokens, 100K output tokens, 200 LLM calls, and about `$1.5` in model cost (p. 26). There is no repeated runtime, failure rate, OCR/API/search charge, infrastructure cost, engineering cost, or human review/adjudication time. Comparing this API subtotal with thousand-hour manual-review estimates would cross incompatible work and cost boundaries.

## Unique insight: endpoint agreement is a lossy checksum over a staged professional artifact

The paper's most useful lesson emerges from its own mismatch. A final pooled estimate behaves like a **lossy checksum** of the evidence-synthesis chain. It can remain numerically close while hiding:

- missing studies and inaccessible sources;
- a changed search cutoff and source universe;
- an irrelevant included construct;
- different outcome-selection rules;
- sign or variance errors;
- dependent effects counted as independent;
- compensating positive and negative extraction errors;
- changed weights and heterogeneity estimates; and
- a reversed inferential conclusion.

Therefore an end-to-end benchmark needs two simultaneous structures:

1. **stage-local admissibility gates** that prevent unsupported evidence from being promoted; and
2. **cross-stage conservation checks** that join each report claim back to source, inclusion authority, extraction, transformation, dependence group, model, and uncertainty.

A plausible final number must not compensate for a missed high-authority source or an invalid analysis model. Conversely, a stage mismatch need not always invalidate the artifact if it is a documented, authorized protocol difference. The benchmark should report both endpoint distance and a typed divergence ledger, with claim ceilings determined by the earliest unresolved consequential break.

A minimal record is:

```yaml
synthesis_claim_lineage:
  question_and_intended_use: ...
  protocol_version_and_approval: ...
  search_sources_queries_caps_and_time: ...
  candidate_and_dedup_cluster_ids: ...
  access_and_representation_state: ...
  independent_screening_observations: ...
  inclusion_adjudication_and_reason: ...
  study_sample_outcome_dependence_ids: ...
  statistic_value_source_locator_and_evidence_view: ...
  transformation_formula_inputs_and_executable_witness: ...
  analysis_model_and_covariance_policy: ...
  sensitivity_and_bias_observations: ...
  report_claim_and_uncertainty: ...
  expert_disposition_and_correction: ...
  downstream_decision_and_consequence: ...
```

These fields belong in existing source-pack, trace, artifact-view, grader, metric, task-health, validity, participation, and consequence machinery; they do not justify a meta-analysis-specific core schema.

## Limitations and validity threats

1. Only one end-to-end application is reported despite plural cross-domain claims.
2. Only one human reference meta-analysis is evaluated.
3. An AutoSynthesis author overlaps with the reference review's lead author, so qualitative adjudication is not blind or independent.
4. The automatic search occurs in July 2026, after the human review's cutoff, changing the eligible source universe.
5. No frozen protocol, registration, approval, or deviation history is released.
6. The default LLM protocol is used even though the paper recognizes that protocol decisions require expert judgment.
7. Expected-effect direction may anchor sign coding and interpretation.
8. Search-query prose says Boolean; the released prompt discourages Boolean syntax.
9. Search databases, ranking, pagination, query strings, and raw result rows are unavailable.
10. A 40-record-per-database cap is cost-driven and no truncation/recall audit is reported.
11. Only 28 records are retrieved for a purported systematic search; comprehensiveness is not established.
12. Deduplication by normalized title does not resolve DOI/preprint/version/report/study lineage.
13. Regex title/abstract filtering is not specified or evaluated.
14. Four full texts are unavailable under the configured access envelope; no alternate human-access audit is provided.
15. Parser choice per paper and parser-view fidelity are not reported.
16. Tables, figures, supplements, scanned pages, and corrected versions may be incompletely represented.
17. No row-level eligibility labels or complete excluded-study ledger is released.
18. No duplicate independent screening, agreement, adjudication, or uncertainty is reported.
19. Post-hoc corrected precision/recall mix system errors with cutoff, source, and access-policy differences.
20. One automatic inclusion is substantively irrelevant by informed author review.
21. Study/component independence judgments are not validated.
22. Numeric occurrence validation does not establish correct semantic binding.
23. Extractor and checker share the same model/configured representation, allowing correlated errors.
24. No source-locator accuracy, field-level extraction accuracy, correction yield, or hallucination rate is reported.
25. Only seven selected matched effects support the quantitative comparison.
26. The matched correlation is `r=.69`, `p=.085`, with no confidence interval.
27. OLS slope `1.62` is not identity calibration; intercept and error metrics are absent.
28. Most effects are unmatched and excluded from study-level agreement analysis.
29. The persuasion-specific relevance prompt contradicts domain-general selection claims.
30. Outcome primacy and admissible alternatives remain model judgments without independent authority.
31. Effect-size conversion formulas and edge-case policies are not specified.
32. Custom REML, Egger, and trim-and-fill implementations are unreleased and unvalidated against reference software or simulations.
33. Twenty effects from eight papers appear to be treated as 20 independent units (`df=19`).
34. No multilevel, robust-variance, covariance, aggregation, or cluster sensitivity analysis is reported.
35. Leave-one-out appears to omit effects, not independent papers/studies.
36. Egger and funnel analyses operate on a small number of independent papers with duplicated effect rows.
37. Moderator subgroups are tiny and inherit the same dependence problem.
38. Cumulative-by-year analysis is interpreted as capability improvement without controlling study/domain/model composition.
39. Risk-of-bias framework selection and domain judgments are not source-located or validated.
40. The displayed ROBINS-I treatment may be inappropriate for randomized included experiments.
41. No certainty-of-evidence assessment connects risk of bias, imprecision, inconsistency, indirectness, and publication bias to a conclusion.
42. The pooled point-estimate tolerance is borrowed rather than justified by intended use or loss.
43. Endpoint closeness is not an equivalence test.
44. The manual and automatic analyses differ on whether the pooled effect excludes zero.
45. The paper calls this broadly similar without a decision-specific interpretation.
46. No repeated run assesses stochastic search, screening, extraction, routing, or provider variability.
47. Hosted model alias, provider defaults, OpenRouter routing, API states, and search indices are mutable.
48. No open-weight model result or backbone comparison supports the robustness claim.
49. No single-agent or commercial-agent run ledger supports architecture superiority.
50. The reported `$1.5` excludes source access, OCR/search services, infrastructure, development, and human audit.
51. No human time, accepted artifact, correction burden, or prospective workflow comparison supports scalability.
52. PRISMA-like output is not independently checked against PRISMA requirements.
53. Complete traces and audit records are claimed but not released.
54. No code, data, exact configuration, statistical routines, final report, or replay environment is public in v1.
55. Training contamination is acknowledged but not tested; deterministic downstream arithmetic does not remove contaminated source interpretation or selection.
56. Living-update claims lack source supersession, correction/retraction, protocol drift, dependence remapping, approval, rollback, and non-regression evidence.
57. No downstream researcher decision, guideline, policy use, intended outcome, or adverse consequence is observed.

## Reproducibility and operational realism

**Paper inspectability is moderate to high.** The 49-page immutable source explains the architecture, one workflow, headline counts, selected prompts, tables, cost/token totals, and one result dashboard. The PRISMA count arithmetic and headline endpoint comparison can be audited from the manuscript.

**Empirical replayability is absent.** A replay needs exact source queries and result rows; access and parser logs; source documents or immutable locators; protocol state; screening and adjudication rows; study/outcome maps; extracted numbers with locators; transformations; dependence groups; analysis code and environment; LLM prompts/configuration; traces; retry/invalid records; and the final generated report. None is in the source package, and the promised repository has no URL.

**Operational realism is mixed.** The workflow mirrors real evidence synthesis, includes genuine access and parsing failures, uses source APIs, creates intermediate artifacts, computes quantitative statistics, and emits professional plots/reports. But it omits prospective registration, dual screening/extraction, librarian search review, author contact, correction/retraction handling, dependence adjudication, expert acceptance, certainty assessment, decision use, maintenance, and release closure. One half-hour run on 28 records is a useful prototype, not an operational living-meta-analysis evaluation.

## Transfer to `skill-bench`

### Retain

1. Decompose long knowledge work into protocol, retrieval, access, screening, mapping, extraction, validation, analysis, bias, and report stages.
2. Preserve intermediate structured records and explicit exclusion reasons.
3. Separate LLM semantic work from deterministic calculations.
4. Use cascading source-representation tools, but record which view each decision observed.
5. Require source locators for every extracted quantitative claim.
6. Report endpoint artifact quality together with stage-level diagnostics.
7. Keep missing-source and nonconvertible-statistic states explicit rather than silently dropping them.
8. Include cost, runtime, calls, and human correction burden as separate resource families.

### Repair before reuse

1. Freeze and version the question, intended use, protocol, search scope, expected direction, moderators, and amendment history before outcome access.
2. Record source-specific queries, caps, rankings, timestamps, pages, raw rows, dedup clusters, access attempts, and parser transformations.
3. Obtain independent screening/extraction observations and preserve disagreement/adjudication authority.
4. Distinguish paper, report, study, sample, contrast, outcome, and effect rows; declare dependence before analysis.
5. Validate every numeric extraction on both lexical occurrence and semantic role, with source-view sufficiency.
6. Replay deterministic transformations against trusted software and adversarial fixtures.
7. Use multilevel/robust methods or justified aggregation for correlated effects; run leave-one-independent-study-out sensitivity.
8. Validate risk-of-bias tool applicability and domain judgments separately from report prose.
9. Evaluate endpoint equivalence against an intended-use threshold and decision loss, not a generic tolerance.
10. Treat changed scope and new evidence as protocol differences, not corrected model accuracy.
11. Repeat complete runs over frozen source snapshots and equivalent forms to measure reliability.
12. Require release closure before reproducibility claims and expert disposition before professional-use claims.

### Falsifiable cross-domain benchmark slice

A reusable validation slice should use at least two unlike knowledge-work structures—for example, a controlled intervention synthesis and a nonintervention association synthesis—without making either the benchmark's permanent scope. Plant:

- duplicate preprint/journal reports from one study;
- one inaccessible but eligible source;
- one semantically adjacent wrong outcome;
- one number that appears verbatim under the wrong group/time point;
- multiple correlated outcomes from one sample;
- one sign-reversal trap;
- one corrected or retracted source;
- one valid alternative analysis model; and
- one pair where extraction errors cancel at the pooled endpoint.

Score separately:

1. protocol and public-basis validity;
2. source-universe recall under declared access;
3. screening and study-lineage accuracy;
4. extraction/source-locator correctness;
5. dependence-map correctness;
6. deterministic calculation replay;
7. analysis-model admissibility;
8. report proposition support;
9. endpoint distance;
10. expert correction time and disposition; and
11. decision loss under declared use.

The key test is whether a numerically close endpoint fails when its chain contains a consequential unresolved break, and whether a numerically different endpoint can pass when it follows an authorized changed protocol and supports a bounded interpretation.

### Existing artifact homes

No new queue task is warranted. The requirements map into existing machinery:

- `schemas/expertise-transfer.schema.json`: protocol authority, hidden requirements, evidence and primitive lineage;
- `schemas/benchmark-bundle.schema.json`: configured systems, source/artifact views, checks, traces, costs, recovery, and outcomes;
- `schemas/metric-monitoring.schema.json`: eligible population, missingness, dependence-aware aggregation, uncertainty, thresholds, and action semantics;
- `schemas/validity-argument.schema.json`: endpoint-to-claim warrant, rebuttals, excluded interpretations, generalization, and decision loss;
- `schemas/task-health.schema.json`: source/release drift, defects, role transitions, and retirement;
- `schemas/expert-participation.schema.json`: reviewer authority, transformation lineage, and approval boundaries;
- `schemas/compounding-lessons.schema.json` and `schemas/LONGITUDINAL_EVALUATION.md`: living-update promotion, supersession, retention, rollback, and leakage;
- `schemas/CLEAN_RELEASE_GATE.md`: code/data/trace/report closure; and
- the existing source-at-state omission conformance pilot: causal tests of source use rather than retrieval alone.

## Action items

1. Add this review to the next canonical synthesis of source-to-artifact and decision-consequence validity: preserve the staged pipeline, but encode **endpoint agreement as a low-resolution observation**, not chain validation.
2. Extend an existing conformance fixture—not a new schema—with correlated effects, duplicate reports, a wrong-group verbatim number, and compensating extraction errors; require dependence-aware analysis and earliest-break diagnosis.
3. In the next artifact-centered pilot, bind every high-level conclusion to an immutable source locator, transformation witness, applicability/dependence decision, and uncertainty record.
4. Require stage-local repeatability and independent adjudication before promoting an end-to-end professional artifact from completion to accuracy.
5. Re-audit release availability only if the authors add a repository URL or a later arXiv version; do not treat the third-party placeholder implementation as official evidence.

## Bottom line

AutoSynthesis is valuable because it exposes a complete professional chain that can become benchmark machinery. Its own evaluation also shows why the chain cannot be replaced by one final number. A `.123` Hedges' g endpoint difference may look small, yet the automatic and human syntheses use different evidence, include different effects, appear to model dependence differently, and cross opposite sides of the null. `skill-bench` should retain the modular, traceable workflow while enforcing the stricter rule: **a plausible professional artifact is not a validated process, a close endpoint is not correct lineage, and neither licenses decision support without dependence-aware, source-grounded, independently reviewed evidence.**
