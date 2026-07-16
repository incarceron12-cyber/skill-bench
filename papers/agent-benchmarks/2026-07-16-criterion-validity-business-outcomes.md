# Criterion association is not outcome prediction: whole-dialogue scores co-vary with selected conversions but do not validate the judge, intervention, or decision

## Source and review status

**Deep review of the complete immutable primary source.** I read the full 29-page arXiv v1 paper, including Appendix A, and verified the layout-preserving extraction against the retained PDF, raw arXiv HTML, metadata, page count, and hashes. The metadata contains no withdrawal or retraction notice.

- **Paper:** Liang Chen, Qi Liu, Wenhuan Lin, and Feng Liang, *Criterion Validity of LLM-as-Judge for Business Outcomes in Conversational Commerce*, arXiv:2604.00022v1 (11 March 2026), <https://arxiv.org/abs/2604.00022v1>
- **Local PDF:** `data/papers/pdfs/2604.00022v1-criterion-validity-business-outcomes.pdf` (29 pages; SHA-256 `78f6ec0adc7003effa0448302875d7028b5fa615c50638f4eb728af666c392bb`)
- **Full local text:** `data/papers/text/2604.00022v1-criterion-validity-business-outcomes.txt` (89,806 bytes; SHA-256 `5080e895fc4b6d4a61714172fa9041345b0f4a93686fae6d7e5d1b61b1d60fb1`)
- **Raw arXiv HTML:** `data/papers/source/2604.00022v1.html` (SHA-256 `24bfc87f5c3f36b3f4396f89c3bc3045d9d18e3e3a7302fc105edbe87b124d45`)
- **Metadata:** `data/papers/source/2604.00022v1-metadata.xml` (SHA-256 `6816bebd2b62fd19e704e171227e6caf89e2e347ccb0a7af67e452bea11c140d`)
- **Release boundary:** neither the paper nor immutable metadata links code, prompts, phase-2 rows, annotations, conversion records, sampling code, model outputs, cross-validation folds, operational-cycle cases, or an official repository. Acquisition-time exact-title, arXiv-ID, and code/data searches found no verifiable author-owned release. The phase-2 statistics and deployment narrative are therefore manuscript-reported and not independently replayable.

## Why this matters for skill-bench

This review advances charter objectives A–C through a bounded test of a central validity bridge:

```text
rubric criterion and configured observer
→ whole-work score
→ external outcome association
→ prospective prediction
→ intervention effect
→ decision utility and stakeholder consequence
```

The paper contributes unusually direct evidence at the third rung: selected rubric scores are compared with payment-linked operational labels. Its most important lesson is also its limit. A score can co-vary with one downstream label without establishing that the judge scored correctly, that the criterion caused the outcome, that optimizing the score will improve the outcome, that the outcome is legitimate or sufficient, or that a threshold supports deployment.

Conversational commerce is a methodological case, not a domain commitment. For `skill-bench`, the reusable question is whether artifact, workflow, judgment, safety, or readiness subscores have **incremental, prospective, transportable, and decision-useful** relations to consequences rather than only plausible names or same-sample associations.

## One-sentence contribution and assessment

**Contribution:** The paper compares seven whole-dialogue rubric dimensions with verified payment conversion in a case-enriched sample of 60 human-agent conversations, finds heterogeneous concurrent associations, and argues that an equal-ish composite can dilute the dimensions most associated with the selected outcome.

**Assessment:** The dimension heterogeneity is a useful hypothesis-generating observation, but different outcome-conditioned eligibility rules, retrospective whole-dialogue scoring, an unvalidated single model judge, uncontrolled user intent and agent/customer clustering, small same-sample weight selection, and absent phase-2 rows mean the study does not establish judge accuracy, predictive validity, incremental prediction, causal mechanism, intervention benefit, population calibration, business value, professional validity, production fitness, or readiness.

## Research question and defensible claim boundary

The paper asks whether a seven-dimension dialogue-quality rubric is associated with commercial conversion, which dimensions carry the association, and whether empirical reweighting improves the composite. It explicitly calls the main study concurrent rather than predictive because scores and outcome status come from the same conversations (Section 3.6, pp. 8–9).

The strongest defensible claim is:

> In one author-reported, human-agent-only, outcome-enriched sample of 60 conversations from a Chinese parent-matchmaking platform, one configured Claude judge's whole-transcript scores for Need Elicitation and Pacing Strategy have moderate positive rank associations with a binary payment label, while Contextual Memory has no detectable bivariate association; a phase-1-informed weighted combination is also positively associated in this phase-2 sample.

The paper does **not** establish that those dimensions are accurately measured, independently predictive before conversion, causally responsible for payment, sufficient beyond user intent or agent/customer effects, calibrated to the platform prevalence, useful for selecting future systems, beneficial to customers, transportable to AI-agent conversations or other work, economically valuable, professionally valid, safe, production-fit, or deployment-ready.

## Methodology and system

### Phase 1: a confounded pilot, not criterion confirmation

Phase 1 combines several non-equivalent sources (Table 1 and Sections 3.1–4.1, pp. 6–10):

- 170 exported human-agent “golden” conversations, 30 selected for Trust Ladder annotation;
- 202 AI-agent conversations, split as 100 plus 102 for descriptive funnel work;
- five human conversations drawn from completed transactions and ten AI conversations selected for high engagement;
- fifteen model-scored conversations, with one human `T6` trust-collapse case removed to produce the `n=14` criterion analysis; and
- Trust Ladder `T5` as a conversion proxy because payment-system access was unavailable.

All three deal cases in the 14-row analysis are human and all ten AI cases are no-deal. The paper appropriately concludes that its original “higher quality, worse outcome” paradox was largely an agent-type and sampling confound. Phase 1 is therefore hypothesis generation, not an independent demonstration that quality scoring failed.

Appendix A releases only these 15 phase-1 score rows. I replayed the listed v2.0 weights (`20/20/20/15/10/10/5`) over all rows: every displayed v2.0 total is arithmetically exact, and the reported human and AI means/standard deviations in Table 4 are reproduced. This validates the appendix arithmetic, not the rubric, judge, Trust Ladder, outcome proxy, exclusions, correlations, or phase-2 results.

The phase-1 proxy itself is weak: `T5` is an LLM-assigned “Price Reasonable” state, and only three annotated cases are said to align with payment. Trust Ladder assignment has no human validation or reliability study. One `T6` post-purchase collapse is removed as “ambiguous,” even though it is highly relevant to whether first payment is an adequate business or welfare endpoint.

### Phase 2: outcome-enriched human-only sample

The stated source frame is 59,316 WeChat Work conversations from March–July 2025, with 319 verified conversions (about 0.5%). The authors sample 25 converted and 35 unconverted human-agent conversations (Section 3.2, pp. 6–8):

- converted cases require at least five user messages and are randomly drawn with seed 42 from 170 “golden” conversations;
- unconverted cases require at least eight user messages and are stratified across agents; and
- converted cases are heavily oversampled relative to the operational base rate.

Restricting phase 2 to human agents removes the phase-1 human-versus-AI mixture. It also means the central criterion associations are **not tested on the AI agent** that motivates much of the paper's intervention narrative.

More importantly, the two outcome strata do not share one clearly defined eligibility and sampling rule. Converted cases come from a 170-conversation golden subset with a five-message minimum; unconverted cases use an eight-message minimum and agent stratification. That can condition on variables affected by user intent, agent behavior, conversion, or curation. Case enrichment is compatible with some association or odds-ratio analyses under careful case-control assumptions, but it does not support prevalence, calibration, predictive value, or an unbiased portfolio score. Those assumptions are not established here.

The paper does not report customer IDs, repeat conversations, agent counts, agent-level conversion rates, conversation dates per row, service/product tier, price offered, campaign, traffic source, customer initial intent, demographic mix, prior contact, or follow-up/censoring. Conversations can therefore be dependent through customers, agents, templates, time, or campaign conditions. “Non-converted” has no stated follow-up horizon or handling of later, off-platform, canceled, refunded, duplicate, or externally attributed payments.

### Rubric and configured judge

The seven 1–5 dimensions and v2.0 weights are (Table 2, p. 7): Need Elicitation 20%, Emotional Empathy 20%, Pacing Strategy 20%, Objection Handling 15%, Contextual Memory 10%, Product Accuracy 10%, and Brand Consistency 5%.

The observer is identified as Claude Opus 4.6 at temperature zero with chain-of-thought before each score. The paper names four intended bias controls—verbosity, self-enhancement, surface fluency, and emotional overweighting—but does not release the exact prompt, anchors, examples, output schema, provider snapshot/date, decoding/retry/invalid policy, reasoning traces, or phase-2 outputs. Temperature zero does not make a hosted endpoint immutable or establish repeatability.

There is no human dimension scoring, human–human agreement, judge–human agreement, repeated model scoring, alternate model judge, blinded outcome test, or source-style audit. The paper repeatedly says the findings concern rubric design “not judge accuracy” and even asserts that D5 is irrelevant rather than mismeasured. The data cannot identify that distinction. A near-zero D5–conversion association can arise from true irrelevance, restricted range, judge noise, wrong evidence access, construct error, missing-not-at-random scoring, or opposing subgroup effects. Criterion association of one configured score and measurement validity of the underlying dimension are nested questions, not alternatives that can be separated by assertion.

The judge sees the **entire conversation**, including user responses and potentially outcome-adjacent behavior. The paper does not state whether transcripts are truncated before payment, whether purchase links/payment confirmations/post-payment turns are removed, or whether the judge is blinded to explicit outcome cues. Even without direct payment text, D1 and D3 can encode the customer's cooperativeness or intent after it is behaviorally revealed. This is concurrent retrospective description, not a pre-outcome forecast.

### Outcomes, missingness, and statistical analysis

The phase-2 criterion is `is_converted`, described as a completed payment transaction. This is stronger than a role-play label or the phase-1 Trust Ladder proxy. But platform pipeline integrity is not independently checked, and conversion omits refund, cancellation, satisfaction, service quality, lifetime value, complaint, vulnerability, manipulation, and long-term welfare. The paper itself reports that 50% of its golden conversations show post-purchase trust issues and 43% mention refunds (Section 8.3, p. 23), directly challenging first payment as a sufficient optimization target.

Primary analyses use Spearman correlation between ordinal scores and binary conversion, Cohen's `d`, and Bonferroni adjustment across seven dimensions. The paper reports:

- D1: `ρ=0.368`, raw `p=0.004`, adjusted `p=0.027`, `d=0.74`;
- D3: `ρ=0.354`, raw `p=0.006`, adjusted `p=0.039`, `d=0.77`;
- D5: `ρ=0.018`, `p=0.895`, `d≈0`;
- proportional-reweight composite: `ρ=0.272`, `p=0.036`, `d=0.56`; and
- phase-1-informed conversion weighting: `ρ=0.351`, `p=0.006`.

D4 is missing for three conversations and D5 for two because the judge returns N/A. The paper proportionally reweights the remaining dimensions and supplies one median-imputation sensitivity for D5. It calls missingness plausibly random because counts by conversion are small. Yet applicability depends on transcript content and length, which can depend on user intent, agent policy, and outcome. Applicability is itself potentially informative and should be modeled and reported, not assumed away from `3` and `2` cases.

The claim that the composite is “diluted” is numerical, not statistically established. The authors correctly disclose that the difference between D1 and composite correlations is untested and dependent, with wide intervals (Section 4.2, p. 11). They nevertheless use stronger “confirmed” and “structural” language elsewhere. A weak or null component can lower one sample's rank correlation, but a seven-criterion benchmark may intentionally preserve content, safety, or professional obligations that are not expected to maximize one endpoint. Outcome association informs a criterion's use; it does not by itself determine criterion legitimacy or weight.

### Confounding and model instability

Bivariate logistic models controlling message count report D3 `OR=3.18` and D1 `OR=2.49`. These show that one measured covariate does not explain the reported association under the fitted model. They do not “rule out” conversation-length confounding, because message count is an imperfect and possibly post-treatment proxy, functional form is not assessed, and selection differs by outcome on minimum message count.

Customer initial intent, agent skill, agent assignment, customer resources, product/price, timing, source channel, prior contact, and transcript outcome cues remain uncontrolled. The paper acknowledges initial intent and reverse causality. That limitation is fundamental: a cooperative high-intent customer can make need elicitation and pacing look better, then pay for reasons not caused by those behaviors.

The full `D1+D3+D5+message_count` model uses 58 rows and 25 events for five stated parameters. It produces a sharp D5 sign reversal (`OR=0.15`, `p=0.005`) and very wide D1/D3 intervals. This suppressor result is unstable evidence, not support for the narrative that memory is counterproductive. The paper acknowledges the low events-per-variable ratio but still describes the model as complementary evidence.

No agent/customer random effects, clustered standard errors, penalized rare-event model, nonlinear terms, interactions, influential-point analysis, calibration, discrimination, threshold loss, or external holdout are reported. Bonferroni covers seven dimension tests, not the full family of phase-1 analyses, composites, six weight schemes, regressions, partial correlations, Trust-Funnel analyses, cycle comparisons, and interpretive probes.

### Reweighting and temporal cross-validation

The selected conversion-informed weights are `D1=10, D2=10, D3=40, D4=15, D5=0, D6=15, D7=10`. They were motivated and optimized on the confounded 14-row phase-1 sample, then compared on phase 2. This gives some temporal separation between initial hypothesis and later sample, but D3 is already privileged by the pilot, many candidate schemes are compared, and phase 2 is used both to report associations and evaluate weights.

The paper later reports four-fold temporal cross-validation within phase 2: train on 45, test on 15, mean trained-weight `ρ=0.294` versus equal-weight `0.179`, with standard deviations `0.393` and `0.403`, and better direction in three of four folds. The optimization objective, constraints, exact fold dates/class counts, treatment of missing dimensions, row-level predictions, and paired fold differences are absent. Four highly variable, tiny folds do not establish prospective prediction. The text also calls the phase-2 source March–July 2025 while the temporal-CV passage says conversations were ordered March–May; this timing discrepancy is unexplained.

Because the 25:35 outcome ratio is artificial, even a stable rank association would not provide operational calibration, positive predictive value, expected conversion, or an actionable threshold at the platform's roughly 0.5% base rate. Reweighting to maximize same-corpus association can also turn a plural quality rubric into an uncalibrated conversion proxy, sacrificing content or safety dimensions whose value is noncompensatory rather than correlational.

### Trust-Funnel mechanism and AI/human comparison

The paper separately analyzes 100 AI conversations and 30 preselected human golden conversations with a six-stage rule detector and an LLM-annotated Trust Ladder. It reports 72% AI closing-stage reach, no `T5` in the scored AI sample, 89.57 versus 26.23 mean stage transitions, repeated rejection override, and empathy immediately followed by sales links.

These observations plausibly identify a pacing failure signature. They do not establish mediation from D3 through trust to conversion:

- AI and human samples have different sources and selection rules;
- Trust Ladder labels have no human validation;
- the funnel detector is manually checked on only five conversations and reported at about 80% maximum-stage accuracy;
- no customer/agent clustering or uncertainty is reported;
- no formal mediation model is run; and
- the AI conversations have no verified conversion labels in the central phase-2 analysis.

The paper appropriately calls the mechanism descriptive and observational in Section 6, but the abstract and conclusion still join these non-equivalent datasets into a stronger causal story than the design supports.

### Two operational cycles and hard-cap rule

The proposed architecture separates L3 safety hard gates, L2 weighted quality, and L1 business outcomes. This noncompensatory separation is directionally useful. The D3 hard-cap rule limits scores after repeated messages, repeated rejection override, or purchase-link repetition.

The two reported cycles compare Config A and B on P0 pass rate, D3 mean, weighted total, and a GO/NO-GO outcome. Config B reaches 100% P0 in cycle 2 and is approved. But the paper does not provide task/case rows, exact configuration identities, prompts, model versions, assignment, repeats, judge records, dates, deployment exposure, or post-deployment conversion/safety/customer outcomes. Table 14 mentions a 47-case smoke set, while Table 16's 88.9% and 94.4% pass rates imply an unreported denominator or subset. The cycles demonstrate an internal decision procedure as narrated, not that D3 intervention improved conversion or that the gate is calibrated.

The hard cap mixes measurement and policy: it changes a score by rule rather than independently observing a construct. That can be legitimate for a safety gate, but then the object is policy conformance, not evidence that the latent “pacing” score has improved. Repeated-rejection limits should remain noncompensatory safety predicates with their own authority, false-positive/negative analysis, user-benefit evidence, and incident outcomes.

## Evidence and claim ladder

### Supported or usefully evidenced

1. The paper exposes the often-skipped empirical question of whether rubric dimensions have heterogeneous relations to an external operational endpoint.
2. The reported phase-2 sample shows different concurrent score–payment associations by dimension under one configured judge.
3. Phase 1 demonstrates how outcome-conditioned task selection and agent-type mixture can reverse a composite narrative.
4. The released phase-1 table is internally arithmetically consistent under the stated v2.0 weights.
5. The paper explicitly distinguishes concurrent association from prospective prediction and acknowledges reverse causality, sample size, circularity, judge validation, platform transport, and ethics limits.
6. Separating noncompensatory safety gates, plural quality evidence, and a downstream outcome is a useful architecture, provided none is treated as validated by the others.

### Partially supported

- **Dimension heterogeneity:** observed in one small selected sample, but judge validity, clustered uncertainty, eligibility bias, outcome leakage, and replication remain unresolved.
- **Composite dilution:** numerically present, but the dependent correlation difference is untested and “best outcome correlation” is not necessarily the intended plural-quality construct.
- **Weight improvement:** directionally survives a tiny within-sample temporal exercise, but optimization and folds are unreleased and no prospective frozen test exists.
- **Pacing/trust mechanism:** consistent with selected descriptive AI traces, but no identified mediation or randomized strategy effect exists.
- **Operational utility:** two internal cycles are narrated, but neither exact test evidence nor downstream outcome effect is available.

### Not supported

- judge accuracy, reliability, human equivalence, or rubric construct validity;
- predictive validity before outcome observation;
- incremental prediction beyond user, agent, product, channel, and time variables;
- causal effects of D1, D3, Trust Gate, hard caps, or reweighting;
- calibrated conversion probability or deployment threshold at the operational base rate;
- conversion as sufficient customer benefit, quality, welfare, or economic value;
- AI-agent criterion validity, because phase 2 is human-only;
- cross-platform, cross-cultural, cross-domain, or temporal transport;
- professional validity, production fitness, safety, or readiness.

## Unique insight for skill-bench

> **Criterion validity is a typed relationship among a score, an outcome, a timing rule, and a use—not a license to rewrite a plural rubric toward whichever downstream label is available.**

A reusable outcome-validation record must preserve at least:

```text
criterion definition and authority
→ observer identity, exact evidence view, reliability, and accuracy
→ scoring time relative to outcome and any outcome-bearing cues
→ eligible population, inclusion policy, case enrichment, and clustering
→ external outcome definition, provenance, observation window, and missingness
→ association with uncertainty and multiplicity
→ incremental/prospective prediction against declared baselines
→ frozen intervention or promotion rule
→ randomized/quasi-experimental effect on joint intended and adverse outcomes
→ threshold/loss, stakeholder authority, operational decision, and transport boundary
```

This adds four important distinctions to the repository's existing claim ladder:

1. **Concurrent criterion association versus predictive validity.** Whole-artifact evidence can describe the same episode while leaking consequence-adjacent state; a prospective score must freeze its evidence view before the outcome window.
2. **Association versus incremental information.** A rubric score can correlate with an outcome because both encode task/customer difficulty or user intent. Compare against legitimate pre-decision baselines and report added calibration/discrimination or decision value.
3. **Outcome alignment versus outcome authority.** Payment, acceptance, throughput, or stakeholder preference can be observable yet incomplete, manipulable, harmful, or misaligned with professional obligations. Never zero-weight safety, correctness, or rights merely because they do not correlate with a selected business endpoint.
4. **Predictive utility versus intervention utility.** A prognostic marker need not be a causal lever. Validate score-targeted changes with frozen, preferably randomized comparisons on joint quality, safety, burden, and consequence outcomes.

## Comparison with adjacent skill-bench evidence

- **Validity-Centered AI Evaluation** supplies the claim–evidence framework: this paper is a concrete criterion-association case, but it also shows why criterion evidence is nested under content, observer, external, and consequential validity. “Payment-associated under one judge/sample” is a useful narrow claim; “quality,” “business value,” and “readiness” are wider claims requiring different evidence.
- **Nubank production evaluation** reaches farther operationally by reporting live selected deployment outcomes, yet lacks prospective offline predictions, assignment details, denominators, uncertainty, and treatment isolation. The present paper supplies dimension-level association and a base-rate frame, but no live intervention effect. Together they require a frozen offline score/promotion rule before exposure, exact metric funnels, configured candidate lineage, and online effect estimation.
- **User-simulator decision fidelity** uses payment-linked dialogue to expose consequence-stratified simulator error while warning that future outcome may reflect latent information unavailable at decision time. The same warning applies here: whole-dialogue D1/D3 can absorb user cooperativeness and future-revealed intent. Outcome-linked evidence is not automatically a legitimate pre-decision predictor or causal strategy measure.
- **Benchmark-to-risk expert elicitation** separates benchmark observation, capability interpretation, scenario use, workflow effect, outcome composition, and decision loss. This paper empirically observes one score–endpoint link but leaves mechanism, customer welfare, refund/lifetime value, threshold loss, and decision utility open. An observed criterion is stronger than an elicited probability, but it still does not collapse the later links.

## Limitations and validity threats

1. One platform, language, cultural context, product family, and emotionally vulnerable customer population.
2. Phase 1 is purposive, tiny, outcome/agent confounded, and uses an unvalidated Trust Ladder proxy.
3. The phase-1 criterion exclusion removes a post-purchase trust-collapse case as ambiguous.
4. Phase 2 uses human-agent conversations only; AI-agent criterion validity is untested.
5. Converted and unconverted strata have different minimum-message and sampling rules.
6. Converted cases come from a 170-conversation golden subset rather than a clearly common 59,316-conversation eligible frame.
7. Case enrichment destroys prevalence, predictive-value, and calibration interpretation without reweighting/modeling.
8. Non-conversion follow-up, censoring, later/off-platform payment, cancellation, refund, and duplicates are unspecified.
9. Customer, agent, template, campaign, and calendar clustering are unreported and unmodeled.
10. Customer initial intent, agent experience, product/price, traffic source, prior contact, and time-of-day remain uncontrolled.
11. Message count is post-treatment/possibly outcome-related and differently thresholded by outcome stratum.
12. Controlling one measured covariate cannot “rule out” conversation-length or broader confounding.
13. The judge sees the whole conversation; pre-payment truncation and outcome-cue blinding are unspecified.
14. Reverse causality and user-cooperativeness pathways are fundamental to concurrent whole-dialogue scoring.
15. One unvalidated hosted model judge defines all phase-2 dimensions.
16. Exact rubric prompt, anchors, examples, output schema, endpoint snapshot, reasoning, retries, and invalid policy are absent.
17. Temperature zero does not establish endpoint immutability or repeated-call reliability.
18. No human scoring, agreement, adjudication, alternate judge, or source-style audit exists.
19. The claim that D5 is irrelevant rather than mismeasured is not identified.
20. N/A applicability can depend on intent, policy, length, and outcome; missing-at-random is not established.
21. Phase-2 row-level scores, labels, dates, agent/customer IDs, and exclusions are unreleased.
22. Spearman-with-binary-outcome is an association statistic, not calibration or prospective prediction.
23. No confidence intervals are reported for the principal correlations or their differences.
24. Composite-versus-D1/D3 correlation differences are dependent and untested.
25. Bonferroni covers seven dimensions, not the broader analysis garden of composites, schemes, models, mechanisms, and cycles.
26. Six weight schemes are compared without an untouched confirmation set.
27. Reweighting is informed by a 14-row confounded pilot and further inspected on the phase-2 sample.
28. Four temporal folds contain only 15 rows each and have very high reported variance.
29. Temporal-fold construction, outcome counts, optimization objective, constraints, and predictions are absent.
30. March–July source timing and March–May temporal-CV wording are not reconciled.
31. The full logistic model has few events per parameter, wide intervals, and an unstable D5 sign reversal.
32. No calibration, discrimination, decision curve, threshold loss, or incremental baseline comparison is reported.
33. Trust Ladder labels are entirely model-generated without human validation.
34. Funnel maximum-stage checking covers only five conversations at roughly 80% reported accuracy.
35. Human and AI Trust-Funnel samples are non-equivalent and selected differently.
36. No mediation analysis or randomized pacing strategy identifies the proposed trust mechanism.
37. The two operational cycles lack exact cases, configuration manifests, repeats, denominator reconciliation, and trial records.
38. GO status is based on authored offline gates; no post-GO conversion, safety, burden, refund, or customer-welfare effect is shown.
39. Hard-capping a score after rejection mixes policy conformance with latent-quality measurement.
40. Completed payment is consequential but omits refund, satisfaction, service fulfillment, lifetime value, manipulation, and welfare.
41. The paper reports frequent post-purchase trust/refund issues, undermining conversion as a sufficient optimization target.
42. Platform outcome-pipeline integrity is not independently verified.
43. No formal ethics review occurred; terms of service are not informed research consent.
44. De-identification does not document purpose-specific permission, model-provider data flow, retention, deletion, or participant withdrawal.
45. No code/data release permits phase-2 recomputation, judge replay, cross-validation audit, or operational-cycle verification.
46. No cost, latency, analyst burden, false promotion/rejection, incident loss, or economic-value analysis exists.
47. No evidence supports professional validity, production fitness, safety, or readiness.

## Reproducibility and operational realism

**Conceptual reproducibility is moderate.** The paper names the platform context, two sampling phases, seven dimensions and weights, scoring scale, principal associations, regression variants, missingness handling, weight candidates, and proposed operating architecture. Appendix A permits exact replay of the displayed phase-1 weighted totals.

**Empirical reproducibility is low.** The central 60-row dataset, outcome joins, prompts, judge outputs, labels, sampling script, fold assignment, regression code, confidence calculations, operational test cases, and cycle outputs are unavailable. The full raw HTML does not repair those omissions. Exact phase-2 statistics, clustering, eligibility, leakage, model identity, and deployment decisions cannot be audited.

**Operational realism is mixed.** Real operational dialogue and payment-linked labels are stronger consequence evidence than synthetic tasks or human preference alone. The source also confronts rejection override, emotional vulnerability, safety gates, and post-purchase trust. But the criterion study is retrospective and human-only; the mechanism uses non-equivalent selected samples; and the “deployed” evaluation cycles expose no online assignment or customer outcome. The correct status is a hypothesis-refining criterion-association study plus a narrated internal evaluation workflow, not a validated production decision system.

## Transfer to skill-bench

### Retain

1. **Test each score family against declared external criteria.** Do not assume expert plausibility or judge agreement establishes consequence relevance.
2. **Report dimension-level relations before aggregation.** Heterogeneity, nulls, sign reversals, applicability, and dependence should remain visible.
3. **Use hard outcomes when ethically legitimate.** Preserve source, observation window, join integrity, missingness, and whether the outcome is direct, proxy, simulated, or elicited.
4. **Keep safety noncompensatory.** A quality or outcome gain must not offset a supported safety, rights, or authorization failure.
5. **Treat confounded pilots as hypothesis generation.** Preserve how sampling and system identity produced the initial signal and require a new confirmation population.
6. **Expose the outcome's insufficiency.** Pair acceptance/payment/throughput with reversals, rework, satisfaction, burden, harm, and longer-horizon consequences where the intended use requires them.

### Repair

1. **Freeze the evidence view before the consequence window.** Score pre-outcome artifacts or prefixes; separately score full episodes for retrospective diagnosis; audit outcome-bearing cues.
2. **Use one explicit eligible population.** Preserve inclusion/exclusion by outcome, case enrichment, base-rate weights, customer/agent/task clusters, follow-up, censoring, and all invalid joins.
3. **Validate the observer first and recursively.** Cross human and model raters with identical views, criterion-specific agreement/error, repeated calls, abstention, and blinded outcome status.
4. **Test incremental information.** Compare rubric dimensions against legitimate pre-decision baselines such as task difficulty, source state, user intent, agent identity, and artifact complexity; report calibration, discrimination, and decision value, not correlation alone.
5. **Predeclare weights and claims on a future form.** Keep exploratory feature/weight selection separate from an untouched temporal or organizational confirmation set.
6. **Validate interventions, not only markers.** Randomize or otherwise identify score-targeted changes, preserve configured component deltas, and measure joint quality, safety, burden, and downstream consequences.
7. **Treat criterion weights as use-specific policies.** A business-outcome weight set cannot overwrite a professional-quality vector or safety gate. Record the stakeholder, outcome, time horizon, loss function, and excluded uses.
8. **Preserve negative operational evidence.** Every candidate, gate failure, non-promotion, rollback, incident, missing outcome, and post-release reversal belongs in the episode lineage.

## Concrete repository actions

No new schema or queue task is warranted. Existing rubric criterion, configured-grader/evidence-view, task-health, metric-monitoring, validity-argument, participation/consent, and production-validation machinery already has homes for the requirements. The missing evidence is empirical use, not another contract.

For the next consequential pilot where a legitimate outcome is available, exercise one compact **criterion-to-outcome validation episode**:

- freeze a pre-outcome score and evidence-view hash;
- define the eligible unit, case-enrichment/base-rate policy, clusters, outcome window, missingness, reversals, and adverse outcomes;
- cross the configured observer with independent labels/repeats;
- compare dimension and composite incremental value against declared baselines;
- preregister a weight/threshold on development data and test it on an untouched temporal form;
- if a score-targeted change is made, preserve a matched intervention contrast and joint quality/safety/consequence outcomes; and
- license only the narrow association, prediction, intervention, or decision claim actually supported.

Useful completion is not a larger outcome correlation. It is the ability to reject outcome leakage, unvalidated observation, post-selection weighting, harmful proxy optimization, and unsupported intervention/readiness promotion while preserving a bounded criterion relationship when it survives those tests.

## Bottom line

The paper asks the right neglected question and provides a useful warning: dimensions that sound professionally desirable need not have equal relations to a selected downstream endpoint, and a confounded pilot can invert the apparent story. Its answer remains much narrower than “valid business judge.” A single model scores whole conversations in a small, outcome-enriched, differently eligible human-only sample; two dimensions co-vary with payment, but the observer, timing, clustering, baseline increment, reweighting, mechanism, intervention, customer welfare, and operational decision are not validated. For `skill-bench`, criterion association should be preserved as one typed rung—valuable, falsifiable, and explicitly below prediction, causality, decision utility, professional validity, production fitness, and readiness.