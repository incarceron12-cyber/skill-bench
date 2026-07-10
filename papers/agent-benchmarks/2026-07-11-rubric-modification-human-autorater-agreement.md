# Paper Review: Rubric Modifications as Human–Autorater Measurement Interventions

- **Paper:** https://arxiv.org/abs/2605.06283v1
- **Authors:** Jessica Huynh, Alfredo Gomez, Athiya Deviyani, Renee Shelby, Jeffrey P. Bigham, and Fernando Diaz
- **Date read:** 2026-07-11
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, 7 May 2026
- **Local PDF:** `data/papers/pdfs/2605.06283v1-rubric-modifications-human-autorater-agreement.pdf` (17 pages; SHA-256 `f5cc6fed33366065b17ea9de90934b65a14e6a1eae3db626182c2facac268e43`)
- **Local text:** `data/papers/text/2605.06283v1-rubric-modifications-human-autorater-agreement.txt` (SHA-256 `8c5a9e32146bab8f40c46a5d234d7cade781fe2f9df562d468fa4d744b522418`)
- **Official-materials boundary:** immutable v1 identifies no paper-linked code, data snapshot, complete machine-readable rubric variants, analysis notebook, preregistration, or external supplement. Appendix B embeds substantial prompt/context/example text, but not a reproduction package.
- **Tags:** rubric-intervention, llm-judge, human-autorater-agreement, decomposition, examples, aggregation, measurement-validity

## One-sentence contribution

The paper tests holistic versus analytic rubrics and several autorater-only edits across automatic essay scoring and instruction following, finding that examples/context and separate per-criterion calls often raise Kendall agreement while batched analytic grading and conservative aggregation often lower it; but reused historical human labels, bundled interventions, construct-mismatched rubrics, under-specified sampling/bootstrap procedures, and no accuracy or external-validity criterion mean these are **configured agreement effects**, not evidence that an edited rubric makes either rater more correct.

## Why this matters for skill-bench

This source directly advances charter objectives B and C by showing that a rubric is not static documentation around a grader. Its text, examples, decomposition, criterion order, call topology, and aggregation rule jointly define a measurement instrument. Changing any one can alter scores even when the work product and model are fixed.

The most important boundary is visible in Figure 1 and Section 3 (pp. 1, 3–4): humans retain historical scores under the original dataset rubrics, while only autoraters receive the edited variants. Thus an increase in human–autorater agreement identifies movement of a configured autorater toward a fixed historical label procedure. It cannot distinguish better machine interpretation from imitation of dataset-specific anchors, shared cueing, score-distribution compression, or construct narrowing. It says nothing about human improvement under the edit because humans were never rerated.

This is cross-domain measurement evidence, not a proposal to make essay scoring or instruction following the benchmark's scope. For realistic knowledge-work artifacts, the reusable requirement is to version and validate the entire rubric realization—not merely criterion text—and to keep agreement, accuracy, construct preservation, and decision validity separate.

## Research question and claim boundary

The paper asks whether (1) autorater-oriented edits improve agreement with human ratings and (2) analytic decomposition improves agreement over holistic scoring (Section 3, pp. 3–4). It also explores criterion separation versus batching, examples/context, inter-model agreement, and association with human inter-rater agreement.

The evidence supports bounded claims that, on three selected ASAP essay prompts and one InfoBench sample, two named model families produced materially different ordinal-score agreement under the tested prompt realizations; edited analytic prompts often improved GPT-4o agreement in AES; separate criterion calls generally beat batched calls; and analytic-to-holistic aggregation can dominate the apparent effect (Tables 1–4, pp. 6–7; Sections 5.1–5.3, pp. 7–9).

It does **not** establish that edited ratings are more accurate, that examples preserve the intended construct, that criterion separation reduces human confirmation bias, that analytic rubrics are intrinsically better or worse, that effects generalize beyond two domains/models, or that higher agreement licenses replacing experts or making professional-capability decisions.

## Methodology and system

### Domains, samples, and human labels

For automatic essay scoring (AES), the study selects ASAP prompts 1, 4, and 6: argumentative, source-dependent/general, and source-dependent/task-specific prompts. Historical ASAP holistic scores and ASAP++ analytic attribute scores serve as human labels (Section 4.1 and Appendix Table 5, pp. 4–5, 12). The holistic and analytic instruments are not semantically equivalent: ASAP mentions audience awareness and explicitly excludes conventions in places, while ASAP++ includes conventions and omits audience awareness. The authors acknowledge that this makes cross-rubric agreement noisy.

For instruction following (IF), InfoBench supplies 50 instructions × five generated outputs, each scored by three expert annotators both holistically (1–5) and analytically through decomposed binary questions. Three examples represent 100%, 50%, and 0% instruction-following ratios and are translated to holistic scores 5, 3, and 1 (Section 4.1, p. 5). The paper does not report the final analyzed row count after example exclusion for each experiment, AES prompt-level counts, missing labels, or a preserved item manifest.

Historical labels improve cost and reuse, but prohibit controlled claims about how rubric edits affect humans. Human assignments, training, timestamps, and evidence views differ across ASAP, ASAP++, and InfoBench; even AES consolidation differs by prompt—averaging for prompt 1 versus a single or adjudicating third rater for prompts 4/6 (Appendix A.2, pp. 11–12).

### Rubric conditions

The study compares four score families: human holistic (`H_H`), human analytic (`H_A`), autorater holistic (`LLM_H`), and autorater analytic (`LLM_A`). `Δrater` changes rater with rubric type held nominally constant; `Δrubric` changes rubric type with rater held constant; Appendix A.1 also changes both.

AES holistic prompts use either the original 10–18 examples or three selected high/middle/low examples. Analytic variants are:

- **batch:** all subcriteria in one API call;
- **separate:** one criterion per API call;
- **edited:** separate calls plus three examples and contextual instructions.

IF uses analogous zero-/three-example holistic and batch/separate/edited analytic variants (Sections 3.1 and 4.1, pp. 3–5; Appendix B, pp. 12–17). The “edited” treatment therefore bundles at least context, examples, and call separation. It is not a factorial intervention that identifies each component. “Reducing confirmation bias” is the authors' interpretation of separate calls; neither human nor model confirmation bias is directly measured.

Examples are purposively selected extrema/midpoints, not randomized boundary cases. In AES, examples answer the same writing prompt; in IF, they concern different instructions and decomposed questions. This helps explain the observed model/domain interaction but also changes leakage and relevance. The full example text in Appendix B shows that examples can reveal both answer format and substantive decision boundaries.

### Autoraters and score extraction

The autoraters are `gpt-4o-2024-11-20` and Llama-3.1-70B-Instruct (Section 4.2, p. 5). A probability-weighted score is computed from exponentiated token log probabilities over output labels. The paper does not report provider/runtime for Llama, temperature, seed, system prompt, decoding constraints, retry/invalid-output policy, repeated calls, exact log-probability extraction implementation, API dates, or raw outputs. A single rating per condition cannot estimate endpoint or stochastic reliability.

### Agreement and aggregation

Kendall's tau with ties is the headline statistic because human and model score-scale use may differ (Section 4.3, pp. 5–6). For AES analytic-to-holistic comparisons, pairwise order is determined by Pareto dominance: A outranks B only if it is no worse on every analytic attribute and better on at least one. For IF, analytic yes/no labels are reduced to the proportion of instructions followed.

These are not neutral translations. Pareto dominance discards trade-offs and creates many incomparable/tied pairs; one criterion disagreement can reverse comparability. The IF ratio gives every decomposed requirement equal weight. The study itself finds analytic IF agreement collapsing to roughly 0.17 in batch conditions versus holistic values around 0.47–0.54 (Table 2, p. 7), making aggregation and call topology inseparable from the “decomposition” result.

The paper reports 1,000-sample bootstrap intervals for differences, with Bonferroni-adjusted bounds for three-condition comparisons (Section 4.3, p. 6). It does not state the resampling unit, whether paired item indices are preserved across conditions, how repeated essays/instructions or pairwise Kendall dependence are handled, or the complete family of hypotheses. There are many prompt × criterion × model × condition comparisons; correcting only within selected three-way contrasts does not control study-wide multiplicity. Exact intervals and sample sizes are not tabulated.

## Evidence and results

Edited analytic AES prompts raise GPT-4o human agreement relative to separate and/or batch variants in most criterion cells, with examples such as prompt-1 word choice rising from 0.439 (batch) to 0.554 (edited). Effects for Llama are less consistent: edited values sometimes fall below separate calls for prompt 1, while context/examples help more on prompts 4 and 6 (Table 1 and Section 5.1, pp. 6–8).

Across both domains, separate analytic calls usually beat batch calls. In IF, GPT-4o human agreement is 0.464 separate, 0.167 batch, and 0.471 edited; Llama is 0.445, 0.166, and 0.426. Adding holistic IF examples raises tau from 0.536 to 0.585 for GPT-4o and 0.470 to 0.578 for Llama, but neither increase is reported significant (Table 2 and Section 5.1, pp. 7–8).

Decomposition does not consistently help. Essay prompt 1's complex holistic rubric sometimes benefits from analytic grading, while prompts 4 and 6 often do not; analytic IF substantially underperforms holistic scoring. The authors reasonably attribute some variation to prompt complexity and aggregation, but complexity is not independently coded or manipulated, so this is a post-hoc explanation (Section 5.2, pp. 8–9).

Higher human agreement strata usually have higher human–autorater tau. InfoBench full/partial/full-disagreement strata show pronounced monotonic drops for holistic ratings (Table 7, p. 12). This is useful task-health evidence: a machine cannot be expected to recover a stable target where human policy is unstable. Yet stratifying on observed human agreement also changes item difficulty, ambiguity, class/tie distributions, and subgroup size; it does not show that raising human agreement would causally raise autorater validity.

Inter-model agreement frequently rises with examples and separate calls (Table 3, p. 10). That is evidence of shared response to a prompt treatment, not corroboration of truth. Two models can converge on the same anchor-induced error.

## Unique insight

The deepest transferable insight is that **rubric editing is a multi-party measurement intervention with at least four distinct outcomes**:

1. **human interpretability** — whether people apply it consistently and legitimately;
2. **autorater stability** — whether repeated configured graders apply it consistently;
3. **cross-rater agreement** — whether human and machine observations coincide;
4. **construct/decision validity** — whether the resulting score measures the intended work and supports a declared use.

This paper measures mainly the third and a weak proxy for inter-model consistency. Its design cannot measure the first under edited rubrics, does not repeat model calls for the second, and supplies no external criterion for the fourth. A rubric edit can therefore increase the reported tau while making the instrument worse—for example, by anchoring both model families to a narrow exemplar, omitting legitimate trade-offs under Pareto aggregation, or moving model outputs toward a historically idiosyncratic human policy.

A second insight is that rubric identity must include **execution topology**. “Rate five criteria” in one call is not the same instrument as five isolated calls: context sharing permits carry-over and consistency, while isolation changes token budget, evidence salience, cost, and error dependence. The paper calls this confirmation-bias reduction, but for `skill-bench` the safer abstraction is a versioned `criterion_execution_plan` whose effects must be measured rather than presumed.

## Comparison with existing project evidence

- **ResearchRubrics** showed that examples can improve criterion-label F1 while verbose expansion harms it, but lacked paired inferential detail. This paper adds explicit within-item agreement comparisons across example/context/call variants, while still not testing semantic preservation or human rerating. Together they justify treating transformations as interventions, not universally prescribing examples.
- **AgentRewardBench** showed that grader reliability depends on predicate, evidence view, prevalence, and loss, and that human labels are not automatic truth. This paper adds rubric realization and aggregation as further grader-identity dimensions, but provides less adjudication and evidence-view detail.
- **Many-Facet human/AI rater analysis** separates agreement, severity, and fit in a connected design. This paper reports agreement shifts but neither rater-severity/scale-use effects nor differential-rater models. Its probability-weighted continuous machine scores versus discrete/aggregated human scores make that omission especially relevant.

The combined lesson is not “optimize the prompt until agreement rises.” It is to model an agreement surface indexed by rater configuration × rubric version × execution plan × aggregation × task family, then independently test construct preservation and consequential decisions.

## Limitations and validity threats

1. **No human rerating under edited rubrics.** Human improvement and symmetric rubric effects are unobservable.
2. **Historical-label heterogeneity.** Dataset-specific training, assignment, context, consolidation, and time are uncontrolled.
3. **Construct mismatch in AES.** ASAP holistic and ASAP++ analytic criteria explicitly differ.
4. **Bundled edited treatment.** Context, examples, separation, and formatting are changed together.
5. **No factorial attribution.** The contribution of each edit and interactions among edits are unidentified.
6. **Purposive example selection.** High/mid/low anchors may improve agreement by cueing expected score regions and narrowing valid interpretations.
7. **Cross-task IF examples.** Examples do not instantiate the same decomposed questions as evaluated items.
8. **“Confirmation bias” is not measured.** Separate calls alter context, cost, dependence, and salience simultaneously.
9. **Aggregation is part of the result.** Pareto dominance and equal-ratio reduction impose different construct and tie structures.
10. **Sample accounting is incomplete.** Final condition-level item counts, exclusions, missing outputs, and tie counts are absent.
11. **Bootstrap procedure is under-specified.** Resampling unit, pairing, clustering, and exact intervals are not reported.
12. **Multiplicity remains broad.** Numerous cells are interpreted while correction is limited to selected within-table contrasts.
13. **No effect-size intervals in tables.** Significance glyphs do not expose interval width or practical uncertainty.
14. **No repeated autorater calls.** Self-consistency under stochastic/provider drift is unmeasured.
15. **Autorater configuration incomplete.** Llama runtime and both models' inference/retry/parser details are missing.
16. **Probability-weighted scores change scale behavior.** Continuous model scores and discrete human scores can alter ties and tau independently of judgment quality.
17. **Inter-model convergence is not truth.** Shared prompting and training may create correlated errors.
18. **Agreement strata are endogenous.** Item ambiguity/difficulty and score prevalence differ across human-agreement groups.
19. **Complexity is post-hoc.** No validated complexity measure or controlled manipulation supports the moderation story.
20. **No accuracy or external criterion.** Agreement is never checked against an authoritative outcome or consequential decision.
21. **No construct-preservation test.** Edited examples/context may change what counts as quality or instruction fulfillment.
22. **Only two domains and two models.** Language, artifact, professional, and model-family generalization are unknown.
23. **English/high-resource only.** The paper acknowledges untested multilingual sensitivity.
24. **No released implementation or data snapshot.** Exact reproduction and independent statistical audit are blocked.
25. **No cost/latency accounting.** Separate calls multiply evaluation cost but the quality–cost trade-off is not measured.

## Reproducibility and operational realism

Reproducibility is weak-to-moderate for reconstructing the intended prompts and weak for reproducing results. The immutable paper preserves main tables, the score equation, substantial context instructions, IF examples, example IDs, model names, and the high-level bootstrap rule. It does not preserve executable prompt files, source dataset revisions/splits, complete condition manifests, raw ratings/log probabilities, code, environment, API logs, random seeds, analysis tables, or exact bootstrap samples. Appendix B ends with embedded prompt examples rather than a full machine-readable release.

Operational realism is similarly bounded. The source uses real student essays and expert-labeled instruction outputs, recognizes that different raters may need different presentation, and studies practical prompt/call choices. But it evaluates static short texts, not long-horizon traces, source-grounded professional artifacts, stakeholder revision, safety gates, dynamic evidence, or decision consequences. Separate per-criterion calls may improve one agreement statistic while multiplying latency/cost and creating inconsistent shared-state interpretations; these operational effects are not measured.

## Transfer to skill-bench

### Treat rubric realization as configured grader identity

For every grader observation, preserve:

- immutable criterion/rubric text and hash;
- examples with type, source, disclosure, representativeness, and exhaustiveness status;
- context/instructions and ordering;
- criterion execution plan (`joint`, `isolated`, staged, or dependent graph);
- model/human rater configuration and actual evidence view;
- output-scale/log-probability transformation;
- aggregation rule, tie/incomparability semantics, and weights;
- missing/invalid/retry behavior, cost, and latency.

Changing any field creates a new instrument version. Historical scores remain attached to the old version.

### Require a rubric-intervention validity matrix

A proposed edit should be evaluated on separate held-out outcomes:

1. human–human reliability under old and new variants;
2. repeated autorater stability;
3. human–autorater agreement with paired clustered uncertainty;
4. criterion confusion and rater-severity/task interactions;
5. construct-preservation review, including legitimate alternative artifacts;
6. external decision agreement or expected loss;
7. cost, latency, invalid-output, and audit burden.

An agreement gain alone should license only “higher agreement on this linked sample,” not “better rubric,” “more accurate grader,” or “professional validity.”

### Separate decomposition from aggregation and execution

Do not label one holistic/analytic contrast as a decomposition effect when criterion text, evidence access, call topology, and aggregation also differ. Use a staged or factorial comparison where feasible. For multi-criterion artifacts, test at least joint versus isolated execution and preserve criterion dependencies; compare aggregation rules against expert decisions rather than selecting Pareto, average, or minimum by intuition.

### Type examples as dual-use evidence

Examples should be marked as boundary cases, non-exhaustive illustrations, counterexamples, score anchors, or reference-answer fragments. Record whether they came from evaluation items or close analogues. Validate that examples improve interpretation without suppressing legitimate solution diversity or leaking private consequences.

## Concrete changes for skill-bench

1. **Refine existing grader/version records, not add a parallel subsystem.** Grader identity should include example set, order, execution topology, score transform, and aggregation hash—not only model and criterion text.
2. **Use the validity-argument contract to block agreement-to-accuracy upgrades.** A rubric edit needs an explicit construct-preservation warrant and decision/loss evidence before supporting capability or readiness claims.
3. **Use task health to track rubric interventions as instrument revisions.** Require bridge items, paired uncertainty, semantic review, and old/new score retention; saturation or increased agreement alone cannot graduate a variant.
4. **Use metric monitoring to declare the eligible task/criterion population, clustering unit, tie policy, multiplicity family, missing outputs, cost, and slices by task/rater/rubric realization.**
5. **When a real plural-grader calibration is run, include a planted shared-cue case.** Two autoraters should agree more after an answer-anchoring example while both become less aligned with an external expert decision; verify that the system reports agreement gain and validity loss separately.
6. **Add no queue task.** Existing bundle, validity, task-health, metric-monitoring, and plural-judgment machinery can absorb these requirements; the next useful work is consolidation or a real calibration, not another schema.

## Action items completed

- [x] Read the complete immutable v1 PDF/text, including appendices and embedded prompt variants.
- [x] Reconstructed domains, human labels, rubric conditions, model scoring, aggregation, bootstrap rule, results, and claim limits with page/table evidence.
- [x] Documented the absence of paper-linked executable materials and exact reproduction artifacts.
- [x] Distinguished agreement, accuracy, shared cueing, construct preservation, and aggregation effects.
- [x] Compared nonduplicatively with ResearchRubrics, AgentRewardBench, and the many-facet rater review.
- [x] Added no duplicate queue task because existing contracts cover the implied implementation work.
