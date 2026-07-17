# Citation-verifier calibration: criterion error direction is not reward validity

## Source and review status

**Deep review of the complete immutable primary source; no official release was identified within the recorded search boundary.**

- **Paper:** Ethan Leung, Elias Lumer, Corey Feld, Austin Huber, Vamse Kumar Subbiah, and Kevin Paul, *Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs for Deep-Research Source Attribution*, arXiv:2607.08700v1 (9 July 2026), <https://arxiv.org/abs/2607.08700v1>
- **Date read:** 2026-07-17
- **Local PDF:** `data/papers/pdfs/2607.08700v1-citation-verifier.pdf` (17 pages; 372,202 bytes; SHA-256 `947fc082439f4116e5b1371acbfc4315247560f6c1e09c11a072eee681a8dbb1`)
- **Local text:** `data/papers/text/2607.08700v1-citation-verifier.txt` (50,604 bytes; SHA-256 `0ba8105d0a647075467ee8ff05da8579a8bbf6a5b8b5c1c1ebad83d1abf3a27e`)
- **Local HTML / metadata:** `data/papers/source/2607.08700v1.html`; `data/papers/source/2607.08700v1-metadata.xml`
- **Provenance and release-search boundary:** `data/sources/releases/2607.08700v1-citation-verifier/provenance.json`. The complete paper exposes no author-owned release URL. Exact-title, arXiv-ID, benchmark-name, GitHub, and Hugging Face searches on 2026-07-17 found no verifiable official corpus, source snapshots, labels, prompts-as-code, predictions, or analysis package. This bounded search does not prove that no private, unindexed, or later release exists.
- **Evidence status:** paper claims and appendix prompts are inspectable; the benchmark and runs are not independently auditable or reproducible.
- **Tags:** citation verification, criterion-level judging, directional error, reward validity, source evidence, human adjudication, deep research

## One-sentence contribution

The paper usefully shows that eight off-the-shelf LLM citation judges with similar pass-class F1 can have materially different false-accept, false-reject, and pass-rate tendencies on 624 adversarial attribution–citation pairs, but its single synthetic report, council-incorporated gold labels, one under-described human reviewer, overlapping criterion prompts, dependence-blind inference, and absent corpus or predictions support only a bounded configured-judge calibration claim—not citation-reward validity, research quality, training benefit, professional validity, production fitness, or readiness.

## Why this matters for skill-bench

Citation checking is a general knowledge-work primitive. Research memos, market analyses, scientific reports, compliance artifacts, and expert recommendations can all fail because a citation is inaccessible, off topic, non-entailing, stale, weakly authoritative, or applied outside scope. `skill-bench` therefore needs criterion-level evidence rather than a single “citation quality” score.

The paper advances charter objectives A, B, and C by isolating two judge-mediated predicates—source relevance and factual support—and by reporting directional confusion rather than only scalar agreement. Its most reusable observation is that **two graders can achieve similar F1 while inducing different operational incentives**. A false pass and a false rejection are not interchangeable merely because they cancel in one aggregate.

The evidence also reveals a stronger boundary than the authors emphasize. A criterion confusion matrix describes disagreement with a label policy on a fixed population. It does not establish what happens when that grader becomes a training reward. The actual chain is:

```text
source snapshot and attribution unit
→ authorized criterion semantics
→ human/reference label with admissible evidence
→ configured judge observation
→ criterion-specific error vector under one prevalence
→ reward transformation and aggregation
→ policy response under optimization
→ held-out citation behavior
→ artifact quality and downstream consequence
```

This paper observes the middle of that chain. It never trains a policy, tests reward hacking, measures citation count or hedging, evaluates held-out behavior, or connects citation decisions to professional outcomes. “Exactly what a downstream reinforcement-learning loop would reinforce” is therefore a mechanism hypothesis, not an empirical result.

## Research question and claim boundary

The paper asks how capable and expensive an off-the-shelf LLM must be to judge citation relevance and factual support, and whether aggregate accuracy hides directional bias that matters for rubric-based reinforcement learning (Sections 1 and 4–6, pp. 1–11).

The full source supports narrow claims that:

1. the authors constructed one long-form report covering 25 topics and parsed 624 attribution–citation pairs;
2. they report 1,248 human-reviewed binary decisions—624 relevance and 624 factual-support labels—plus deterministic accessibility labels;
3. six LLMs first supplied council labels, a human reviewer reportedly checked every decision, and 378 non-unanimous council decisions received more intensive adjudication;
4. eight named judge endpoints were each applied to all 624 pairs per criterion;
5. reported pass-class F1, Cohen’s kappa, pass-rate drift, FPR, and FNR vary by criterion and judge;
6. GPT-5-mini has the highest reported source-relevance pass-class F1, while factual-support point estimates are closer and their separately bootstrapped intervals overlap; and
7. nominal provider pricing spans a reported 49-fold range and does not monotonically track the paper’s quality summary.

The evidence does **not** establish that:

- the 25 topics, one report, cited pages, or synthetic edit mixture represent real deep-research outputs;
- the human-reviewed council label is a professionally authoritative or independently replicated truth;
- relevance and factual support are cleanly separable under the supplied prompts;
- source quality, authority, freshness, scope, primary-source status, or citation completeness is measured;
- overlapping marginal confidence intervals prove judges are statistically indistinguishable;
- the apparent rankings survive topic clustering, source reuse, prompt changes, endpoint repetition, web drift, or a new report generator;
- a judge’s errors causally change an optimized policy in the hypothesized direction;
- an ensemble reduces shared bias or is cheaper after arbitration;
- nominal API price is realized end-to-end evaluation cost; or
- any tested grader supports general reward validity, report quality, professional capability, production operation, or readiness.

## Methodology and system

### Benchmark construction and unit of analysis

The pipeline begins with clean cited overviews across 25 topics, parses attribution–citation units, and adversarially edits roughly 60% of claims using 19 strategies; some claims receive multiple edits (Figure 1 and Sections 3.1–3.2, pp. 4–5; Appendix B, pp. 16–17). Strategies include wrong dates, entities, numbers, locations, attribution, magnitude, negation, fabricated details, source mismatch, semantic drift, reversed causation, near misses, partial truths, overgeneralization, stale information, exaggeration, and minimization.

This is a useful stress-test vocabulary because it varies topicality and entailment independently. The Taylor-series example is clear: an OpenStax page can be topically relevant while contradicting the “finite sum” claim (Section 3.2, p. 5). It demonstrates why citation presence and source relevance do not establish support.

But “corpus” overstates the sampling structure. Section 3.1 calls the benchmark **a single long-form report** spanning 25 domains, not a sample of independently generated reports. The paper does not identify the clean-report generator, prompts, source-selection policy, retrieval dates, page extraction method, source deduplication, claim segmentation rules, parser error study, edit assignment probabilities, strategy frequencies, multi-edit combinations, or whether edit authors were blinded to the later rubric. Figure 1 says about 60% of claims were edited, while the prose on p. 4 says “most attributed claims are left clean”; those descriptions are internally difficult to reconcile.

The 624 rows are also not shown to be independent. Multiple attributions can share a topic, source, page, generator context, or edit strategy. Resampling pairs treats this hierarchy as if every row were exchangeable. Topic-, page-, and report-level transport remain unknown.

### Predicate semantics are partly entangled

The appendix supplies identical prompts for all eight evaluated judges (Appendix A, pp. 15–16). Each call receives attribution text, URL, and `URL Content`, then returns a score and rationale.

The intended split is sensible:

- **source relevance:** is the page about the same topic and clearly connected to the attribution?
- **factual support:** are the specific facts present, consistent, and non-contradictory?

The relevance prompt nevertheless asks whether the page “provide[s] supporting information for the claims.” The authors acknowledge that this overlap is the most common source of relevance disagreement (Appendix A, p. 16). Relevance is therefore not merely being measured noisily; the instrument itself partially imports entailment. The resulting confusion cannot be assigned wholly to model ability.

The factual-support prompt also maps “contradicted, missing, or unverifiable” into the same zero. Those states have different diagnostic and reward meanings. Missing page content can indicate extraction failure; absent evidence can indicate an incomplete citation; contradiction is positive counterevidence; and an intrinsically unverifiable claim may be a criterion or task defect. A binary label erases those distinctions.

No criterion asks whether the source is authoritative, primary, current at claim time, scoped to the jurisdiction/population, independent, or appropriate for the decision. Appendix B includes `outdated info`, but the factual prompt provides no explicit valid-time rule or source receipt. A stale source can correctly entail what it once said while being professionally inappropriate for a current claim.

### Gold-label construction and authority

Six LLM council members independently scored the two criteria: GPT-5-mini, GPT-5.2, Claude Opus 4.5, Claude Opus 4.6, Gemini 2.5 Pro, and Gemini 3 Pro (Section 3.3, p. 5). A human reviewer then reportedly examined all decisions, corrected errors found on review, and adjudicated every non-unanimous case. The final counts are 870 unanimous and 378 disagreement decisions, of which 263 concern relevance and 115 factual support. From the rounded pass rates, the gold labels correspond to 495/624 relevance passes and 115/624 factual-support passes; link accessibility is 614/624.

Human review of every row is stronger than adopting model majority labels automatically. The paper does not, however, report the reviewer’s identity, domain qualifications, fact-checking training, independence from construction, compensation, time, source evidence view, browser/snapshot access, blinding to council identities/votes, response order, decision rules, correction count, rationales, uncertainty, repeat labels, second review, or appeal. “Human-reviewed” is process ancestry, not demonstrated label validity.

Two evaluated judges—GPT-5-mini and Claude Opus 4.6—also sit on the labeling council. The paper argues that the human-adjudicated subset offers a council-independent comparison (Section 4.1, p. 6), but this is incomplete:

- the subset is selected by council disagreement, so its composition is council-dependent;
- the human’s adjudication procedure may expose council outputs; blinding is not reported;
- the same evaluated models can influence unanimous labels unless the human independently re-labels from source evidence; and
- the correction rate for unanimous cases is absent.

Thus the tested-model/gold overlap can favor council-compatible policies. The hard subset is useful as a disagreement-conditioned stress slice, not an independent gold test.

The council protocol is internally inconsistent with a strictly binary task. Appendix A asks for only 0 or 1, yet 29% of disagreement cases contain at least one 0.5 score (Section 4.3, p. 7). The paper does not explain which model produced partial scores, whether the parser admitted them by design, how partials entered unanimity, or why evaluated outputs are later binarized at 0.5. This is evidence of a call/parser/rubric realization gap that should be reported as such, not merely ambiguity.

### Evaluated judges and configured-system identity

Table 1 (p. 4) names eight endpoint identifiers across three families and multiple providers: Claude Haiku 4.5, Sonnet 4.6, Opus 4.6, Gemini 3.1 Flash Lite and Pro, GPT-5-mini, GPT-5.4-mini, and GPT-OSS-120B. This is better than product-family labels alone.

Important realization details remain absent: system wrappers beyond the appendix text, generation settings, reasoning effort, seeds, timeout/retry policy, malformed-output handling, score/rationale parser, URL-fetch implementation, content truncation, HTML cleaning, fetch timestamp, cache identity, page-access failures, model access dates, token counts, latency, and raw response logs. Each judge appears to make one decision per pair and criterion, so stochastic repeat stability and endpoint drift are unmeasured.

The paper calls the setting “live web sources,” but the judge receives a supplied `URL Content` field. Without released page snapshots and extraction receipts, it is impossible to determine whether judges saw equivalent evidence, whether dynamic pages changed, whether boilerplate or missing sections mattered, or whether the accessibility check and judge view refer to the same fetch.

### Metrics, dependence, and statistical claims

The paper reports pass-class F1 and Cohen’s kappa per criterion, with pass-rate drift, FPR, and FNR as directional diagnostics (Section 4.1, pp. 6–7). This is a meaningful improvement over accuracy alone. The gold prevalence is deliberately asymmetric: relevance passes 79.3%, while factual support passes only 18.4% (Section 4.2, p. 7). Reporting both error directions is therefore essential.

Confidence intervals use 2,000 bootstrap resamples over the 624 pairs. Three statistical limits matter:

1. **Dependence:** pair-level bootstrap ignores clustering by the single report, 25 topics, sources, and edit strategies.
2. **Comparison:** overlap of two separately estimated 95% intervals is not a valid paired test of their difference. The claim that factual-support judges are “statistically indistinguishable” requires a paired difference distribution or suitable clustered comparison, with a predeclared family and multiplicity policy.
3. **Selective uncertainty:** intervals are shown for F1, but not for kappa, pass-rate drift, FPR, FNR, cost-quality summaries, hard-subset changes, or rankings. The directional quantities central to the paper’s thesis therefore lack reported uncertainty.

Pass-class F1 is prevalence- and class-policy-dependent. Figure 3 instead averages pass- and fail-class F1 within criterion and then across criteria. That class-balanced score is a different estimand from Table 2’s pass-class F1. Neither has a calibrated reward-loss interpretation. A task-specific loss function might rationally weight a false acceptance of fabricated evidence more heavily than rejection of a valid citation, or the reverse when excessive strictness suppresses useful claims. FPR/FNR should remain a vector until that policy is declared.

The hard-case analysis is descriptive and selected. Council disagreement defines 378/1,248 decisions—42.1% of relevance rows and 18.4% of support rows. Ranking changes on this slice are useful evidence of interaction with ambiguity. They cannot estimate population error without a target hard-case prevalence, and improvements on factual-support F1 can arise from the slice’s changed class balance. No source- or topic-clustered uncertainty accompanies the slice.

### Cost accounting

The reported cost index uses published June 2026 API prices, assumes one call per attribution–citation criterion, and expresses log cost relative to GPT-OSS-120B (Table 2 and Section 5.3, pp. 6 and 10). This supports only a nominal model-call price comparison. The paper gives no input/output token counts, absolute per-item table, batch size, cache hit rate, retries, failures, latency, URL acquisition cost, human review time, adjudication cost, monitoring, or quality-adjusted decision loss. Prompt batching and caching are proposed as future savings but not tested here. “Cheaper judges remain competitive” is bounded to nominal endpoint prices and reported metrics, not total evaluation economics.

## Evidence and results interpretation

The strongest result is not that one cheap model is “best.” It is that criterion behavior is model-specific:

- source-relevance pass-class F1 ranges from 0.700 to 0.908;
- factual-support point estimates range from 0.649 to 0.750;
- all eight judges under-pass source relevance relative to the 79.3% gold rate;
- factual-support strictness varies, with three models passing more than the 18.4% gold rate;
- factual-support FNR ranges from 0.183 to 0.470; and
- rankings change on the disagreement-conditioned subset (Sections 4.2–5.2, pp. 7–10).

Those patterns justify retaining criterion-specific confusion and prevalence drift. They do not show that source-relevance strictness is harmful. A reviewer may prefer strictness if false relevance credits create costly unsupported recommendations. Nor does a low factual-support FPR alone identify a safe reward; a very high FNR can induce sparse reward, but whether the trained policy hedges, cites less, seeks stronger sources, or learns the judge’s lexical preferences is unobserved.

The adversarial-strategy analysis says edited-claim rejection is roughly 86% to near 100%, while factual-support weakness mainly comes from rejecting clean supported citations (Section 5.2, p. 10). This is useful directional diagnosis, but strategy counts, denominators, uncertainty, multi-edit attribution, and clean-case source conditions are not reported. It cannot establish which semantic edits cause errors or whether a natural report would have the same mixture.

The recommendation to select models per criterion is plausible but untested as a system. A two-model verifier changes call topology, cost, missingness, calibration, and cross-criterion dependence. Likewise, selecting judges with high pairwise agreement or ensembling them does not necessarily reduce reward noise: judges can agree on a shared misconception, shared source-extraction failure, or shared prompt ambiguity. Agreement can reduce variance while preserving bias.

## Unique insight

> **A criterion confusion vector is an instrument property under one labeled population; a reward signal is an intervention whose validity depends on transformation, optimization response, transport, and consequence. The former is necessary evidence for the latter, but it is not the latter.**

The paper correctly resists collapsing judge behavior into one F1. `skill-bench` should go one step further and preserve the following typed ladder:

```text
predicate definition and evidence authority
→ observed label/reference reliability
→ configured grader confusion by task/criterion/context
→ prevalence and loss-weighted operating point
→ reward mapping and aggregation
→ trained-policy response under matched control
→ held-out criterion behavior and severe-error profile
→ artifact/workflow consequence
```

This yields two non-obvious design consequences.

First, **direction cannot be interpreted without criterion semantics**. False rejection of a relevant source may be low-cost if the report has redundant stronger evidence, or high-cost if it suppresses a necessary minority source. False acceptance of factual support may be catastrophic for a safety gate but tolerable for a low-weight exploratory note. Preserve FP and FN counts, evidence, severity, and affected requirement; do not turn them into one universal judge score.

Second, **criterion decomposition can reveal bias while creating it**. Relevance and support are nominally separate here, yet the relevance prompt asks about support. A directional error vector is only meaningful after criterion overlap, applicability, evidence sufficiency, and invalid states are audited. Otherwise “model bias” partly measures instrument ambiguity.

## Comparison with existing project evidence

- **Many-Facet Human/AI Rater Effects** separates agreement, rater severity, fit, criterion/task interaction, and decision validity. This paper adds binary directional confusion on a larger criterion-decision set but has only one human label policy, no connected plural-human panel, no repeated judge calls, and no model of topic/source/rater interactions. Pass-rate drift resembles a marginal severity signal; it is not a panel-linked severity estimate or truth.
- **FinResearchBench II** shows that panel consensus and tested-system discrimination are task-health properties, not criterion authority. The citation-verifier paper improves inspectability by publishing exact prompts and using source content, but its six-model council plus one human still cannot convert consensus into gold authority. Its disagreement slice should be retained for diagnosis rather than treated as independent validation.
- **PaperBench and ResearchRubrics** expose dense, expert-linked criteria and partial-progress/report judging, while also showing criterion dependence, evidence-view, and professional-validity limits. Citation verification is narrower and more auditable, but passing relevance/support cannot inherit whole-report correctness, completeness, reasoning quality, or replication/research quality.
- **EnergyEvals** distinguishes source presentation, answer agreement, mutable tool evidence, and professional source-time validity. The present paper supplies URL content but no immutable source receipts or valid-time/authority checks. A page can entail a claim and still be stale, secondary, jurisdictionally wrong, or professionally inadmissible.
- **AgentRewardBench** similarly shows judge quality varies by predicate, evidence view, prevalence, and invalid policy. This paper strengthens the case for preserving FP/FN direction but weakens human authority through one under-described reviewer and tested-judge incorporation into the label council.
- **Existing criterion, grader, metric, task-health, and validity contracts** already provide the right homes: criterion semantics and evidence admissibility; configured grader identity and observations; dependence-aware population metrics; lifecycle roles; and bounded claim promotion. No citation-specific schema is needed.

## Transfer to skill-bench

### Retain

1. Decompose citation evaluation into explicit predicates instead of one holistic score.
2. Preserve per-criterion confusion counts, FPR, FNR, pass-rate drift, invalid/missing rates, and evidence locators.
3. Keep deterministic accessibility observations separate from model-mediated semantic judgments.
4. Maintain hard/disagreement slices as diagnostic strata rather than silently deleting them.
5. Record exact judge endpoint, prompt, evidence view, call topology, and nominal cost.

### Repair

1. **Use a richer citation state model.** Separate citation presence; fetch/access realization; topical relevance; claim entailment; contradiction; evidence absence; source authority; primary/secondary status; valid time; scope/jurisdiction; and citation completeness.
2. **Make evidence receipts immutable.** Bind attribution text, claim segmentation, URL, fetched content hash, extraction method, fetch time, valid-time basis, access result, redirects, and source metadata. A mutable URL alone is not an admissible judge view.
3. **Separate invalid from fail.** Fetch failure, truncated extraction, unsupported media, parser error, partial judge output, and inapplicability must not become substantive zero labels.
4. **Establish reference authority.** Use independently qualified reviewers with preserved initial labels, evidence views, rationales, disagreement, adjudication, repeat samples, authority scope, and severe-error audits. A model council may prioritize cases, but its votes must not silently become truth.
5. **Remove incorporation leakage from confirmation.** Evaluate judges on labels formed without their outputs, or report council-overlap and independent subsets separately. Select hard cases through a fixed external policy or preserve inclusion probabilities.
6. **Validate criterion separability.** Use planted cases that independently vary topicality, entailment, authority, freshness, and scope; audit whether prompts or labels cross those boundaries.
7. **Use dependence-aware comparisons.** Cluster or model report/topic/source/claim lineage, perform paired model-difference inference, declare multiplicity, and attach uncertainty to directional metrics and rank claims.
8. **Calibrate to decision loss, not F1 alone.** Define criterion role, severity, affected stakeholder, FP/FN cost, aggregation, threshold, abstention/escalation policy, and review capacity before choosing an operating point.
9. **Measure realized cost.** Include fetch, calls, tokens, latency, retries, invalids, human calibration/adjudication, monitoring, and severe-error loss.
10. **Require an intervention study before reward claims.** Compare candidate graders under matched training budgets and frozen evaluation; measure citation count, source diversity/authority, entailment, hedging, unsupported claims, reward exploitation, artifact quality, and held-out transport.

### Test before promotion

A minimal cross-domain validation should include at least two materially different source regimes—for example, stable technical standards and time-sensitive regulatory/market sources. Build factorial planted cases for:

- relevant and entailing;
- relevant but contradictory;
- relevant but silent;
- irrelevant but lexically overlapping;
- entailing but stale;
- entailing but weakly authoritative;
- authoritative but out of scope or jurisdiction;
- inaccessible or extraction-invalid; and
- multiple sources jointly necessary for support.

Obtain independent expert labels with source receipts, preserve unresolved disagreement, repeat all configured judges, and estimate criterion × source-regime × judge error with clustered uncertainty. Only then use two selected judges as matched reward treatments against a no-citation-reward control. The confirmation set must be untouched by corpus authoring, prompt calibration, judge selection, and policy training. Reward validity requires observed policy response and held-out artifact consequences, not inference from static FPR/FNR alone.

## Limitations and validity threats

1. One synthetic long-form report rather than independently sampled reports.
2. Only 25 author-selected topics; no target population or sampling frame.
3. Clean-report generator, retrieval process, and source-selection policy are absent.
4. Claim parser and segmentation have no precision/recall audit.
5. Roughly 60% edited mixture is artificial and prevalence-dependent.
6. Prose saying most claims are clean conflicts with the roughly 60% edited description.
7. Edit assignment, strategy counts, and multi-edit combinations are unreleased.
8. Pair dependence by report, topic, source, page, and edit lineage is unmodeled.
9. Source relevance and factual support prompts overlap semantically.
10. Factual zero conflates contradiction, missing evidence, and unverifiability.
11. Authority, freshness, valid time, scope, jurisdiction, and source quality are unmeasured.
12. Accessibility as HTTP 200 does not establish readable, stable, complete, or admissible evidence.
13. Page snapshots, fetch times, redirect chains, extraction code, and content hashes are unavailable.
14. A single human reviewer supplies final authority.
15. Reviewer qualifications, independence, training, time, and evidence access are absent.
16. No second human labels, repeat sample, agreement, rationale corpus, or appeal.
17. Human blinding to council votes/model identities is unreported.
18. Correction count for unanimous council labels is unreported.
19. Two tested judges also contribute to the gold-label council.
20. The disagreement subset is council-selected and therefore not council-independent.
21. Partial 0.5 council outputs violate the nominal binary prompt without a documented parser policy.
22. Exact inference settings, retries, failures, and output parsing are absent.
23. Each evaluated judge appears to run once; repeat stability is unknown.
24. Endpoint and web-state drift limit temporal reproduction.
25. Pair-level bootstrap ignores topic/source/report clustering.
26. Overlapping marginal intervals do not prove no paired model difference.
27. No multiplicity policy for eight judges, two criteria, full/hard slices, and several metrics.
28. No uncertainty for kappa, FPR, FNR, drift, hard-slice rankings, or cost-quality claims.
29. Pass-class F1 and Figure 3’s class-balanced average are different estimands.
30. Hard-slice performance is selected on disagreement and class balance may differ.
31. Strategy-level rejection rates omit denominators, uncertainty, and multi-edit attribution.
32. No subgroup/domain/source-type error analysis despite broad topic labels.
33. Nominal price omits tokens, latency, failures, fetching, and human costs.
34. Proposed batching and caching savings are not experimentally measured.
35. No policy training, reward ablation, held-out optimization, or reward-hacking test.
36. Hypothesized under-citing, hedging, and signal sparsity outcomes are unobserved.
37. Pairwise judge agreement or ensembling can preserve shared systematic error.
38. No report-level completeness, uncited-claim, source-diversity, reasoning, or artifact-quality measure.
39. No professional reviewer decision, downstream outcome, harm, or readiness evidence.
40. No official corpus, labels, predictions, source snapshots, or analysis release was identified.

## Reproducibility and operational realism

**Conceptual reproducibility is moderate.** The immutable paper preserves the pipeline diagram, topic inventory, judge and council identifiers, metric definitions, aggregate tables, both complete judge prompts, and 19 edit strategies. An independent team could implement a similar experiment.

**Empirical reproducibility is poor.** The actual report, 624 attribution units, source snapshots, edit ledger, council outputs, human corrections/adjudications, evaluated predictions/rationales, fetch/parser code, model settings, and analysis code are unavailable. Exact counts and figures cannot be replayed, and mutable pages and endpoints prevent reconstruction from URLs alone.

**Operational realism is limited.** Claim–source entailment over long-form research is realistic, and criterion-level evaluation is directly relevant to scalable grading. The benchmark nevertheless uses one author-constructed adversarial report, supplied page content, one-shot judges, and nominal prices. It does not exercise production fetching, source governance, version drift, invalid-state routing, reviewer queues, monitoring, escalation, reward training, or professional artifact acceptance. It is best understood as a static configured-judge stress study.

**Release inspectability is the principal audit blocker.** Without row-level labels and predictions, outsiders cannot test criterion overlap, incorporation effects, confusion counts, topic/source dependence, strategy asymmetry, bootstrap choices, or severe cases. The recorded search boundary establishes only that no verifiable author-owned release was found on 2026-07-17.

## Concrete changes for skill-bench

1. **Do not add a citation-specific schema or duplicate queue task.** Existing criterion semantics/provenance, artifact-view admissibility, grader evidence-view, task-health, metric-monitoring, plural judgment, and validity-argument records can absorb these requirements.
2. **Preserve directional criterion errors as vectors.** Store TP/FP/FN/TN and invalid/abstain counts by criterion, task/source cluster, severity, and configured grader; prohibit scalar-only promotion.
3. **Add source-receipt requirements when the existing bundle is next revised.** Semantic citation checks should reference immutable fetched-content identity, extraction, access/valid time, authority/scope metadata, and claim locator.
4. **Use this paper as a validity negative case.** High F1 plus reported directional confusion may support a frozen-corpus concordance claim; it must fail promotion to reward validity, research quality, professional validity, training benefit, production fitness, or readiness without intervention and consequence evidence.
5. **Treat council disagreement as review-routing evidence.** Preserve selection policy and denominators, but do not label council agreement as truth or discard disputed cases.
6. **Require paired, clustered uncertainty for grader selection.** Model differences and directional error costs—not overlap of marginal intervals—should govern selection under a declared use.
7. **Add no new task now.** The next useful evidence is an empirical reward-treatment study with independent source receipts and expert labels; creating more synthetic contract machinery would not resolve that uncertainty.

## Action items completed

- [x] Read the complete immutable v1 PDF/text/HTML, including methods, results, references, judge prompts, and all 19 adversarial strategies.
- [x] Reconstructed report/topic/unit construction, council and human-review flow, eight judge identities, evidence inputs, metrics, nominal cost policy, disagreement slice, and claimed reward mechanism.
- [x] Audited human-label authority, council incorporation, prompt overlap, partial-score protocol drift, source authority/freshness omissions, pair dependence, confidence-interval interpretation, multiplicity, directional uncertainty, and cost boundaries.
- [x] Verified the reported rounded gold prevalences correspond to 495 relevance passes, 115 factual-support passes, and 614 accessibility passes out of 624.
- [x] Inspected the paper, appendices, metadata, and recorded bounded official-release searches; did not infer global absence from the negative search.
- [x] Compared nonduplicatively with Many-Facet rater effects, FinResearchBench II, PaperBench/ResearchRubrics, EnergyEvals, AgentRewardBench, and current contracts.
- [x] Derived retain/repair/test implications while leaving reward validity, report quality, training benefit, professional validity, production fitness, and readiness unclaimed.
- [x] Added no duplicate build or consolidation task.
