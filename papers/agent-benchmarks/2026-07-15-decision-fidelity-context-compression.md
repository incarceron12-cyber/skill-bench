# When preserving a model's decision is useful—and when it merely preserves the model

## Source and review status

**Deep review of the complete immutable primary source.** I read the full 15-page arXiv v2 paper, including all figures, prompts, and appendices, and verified the preserved PDF/text hashes. The paper links no code, data, run records, product-study protocol, or author-owned repository. Exact-title, arXiv-ID, GitHub, and Hugging Face searches during acquisition found no verifiable official artifact. All experimental and commercial-product results are therefore manuscript-reported rather than independently replayed.

- Paper: Hoyoung Lee et al., *When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis*, arXiv:2606.29251v2, <https://arxiv.org/abs/2606.29251v2>
- Version read: immutable v2, updated 8 July 2026
- Date read: 2026-07-15
- Local PDF: `data/papers/pdfs/2606.29251v2-decision-fidelity-context-compression.pdf` (15 pages; SHA-256 `97de6ed96df4eb0311af628646c61e3c408597de9da7872f3f9c4d2faca05961`)
- Full local text: `data/papers/text/2606.29251v2-decision-fidelity-context-compression.txt` (SHA-256 `2b954e14502faf93edd0d01a9c3cfe3ef03b16c27ab27ace541d7adcaf9f9e58`)
- Evidence status: full paper read; no inspectable study or product release
- Tags: context compression, decision fidelity, decontextualization, model dependence, financial analysis, source-relative measurement

## One-sentence contribution

The paper makes a valuable move from summary similarity to downstream-decision preservation and shows, under one LLM decision instrument, that 20-bullet financial summaries alter source-conditioned bear/neutral/bull outputs much more often than independent rereads of the source; however, its “source-supported decision” is the same model's unstable response rather than an authoritative label, compressor randomness and factuality are unmeasured, the decontextualization analysis is unvalidated LLM annotation, and the opaque product case cannot establish investment quality or production fitness.

## Why this matters for skill-bench

This review advances charter objectives A and B through a bounded finance stress case for a general knowledge-work transformation:

```text
authoritative source
→ compressed evidence view
→ downstream decision instrument
→ action / artifact / state consequence
→ stakeholder outcome
```

A summary can preserve every individually stated fact yet change the balance among caveats, comparators, uncertainty, and headline claims. That is a real gap in factuality-only evaluation. But “the same evaluator chose the same label” is not a universal fidelity certificate. It is one **decision-view preservation result**, conditional on the evaluator, prompt, metadata, label space, threshold, and source reading that define the reference.

The paper therefore adds a missing distinction to the completed ACON review and context-compression conformance slice:

> **State fidelity, task sufficiency, decision-instrument preservation, decision correctness, and stakeholder consequence are separate constructs.**

This is methodological expansion, not a finance scope commitment. Useful completion is a bounded measurement chain, not another compression subsystem.

## Research question and defensible claim boundary

The paper asks whether a fixed-budget compressed representation preserves the belief distribution that a fixed LLM decision model produces from the original financial disclosure, and whether contextualized or multi-candidate source-audited compression reduces the discrepancy (pp. 1–6).

The strongest defensible claim is:

> For 300 fiscal-2025 Q1–Q3 S&P 100 MD&A sections and 297 earnings-call transcripts, under the reported prompts and Gemini-3.1-Flash-Lite bear/neutral/bull instrument, one sampled 20-bullet output from each tested compressor changed the instrument's three-run mean top label and probability vector substantially more than an independent source reread; contextualization and the two-candidate ACC procedure reduced those source-relative discrepancies versus naive or token-pruning baselines in the reported panel.

The paper does **not** establish a correct source-implied investment decision, human-analyst agreement, factual or inferential equivalence, realized-return prediction, calibrated confidence, preservation for other decisions, reliability over compressor samples, causal mediation through omitted context, cross-domain transfer, professional validity, safe deployment, production fitness, or readiness.

## Methodology and system

### Sampling frame, source authority, and missing lineage

The main panel contains 300 10-Q MD&A sections and 297 quarterly earnings-call transcripts from S&P 100 firms over fiscal 2025 Q1–Q3 (p. 4). Filings were collected with an EDGAR-Crawler-based process; transcript origin is not named. The paper supplies no firm/quarter manifest, accession numbers, transcript provider and version, retrieval dates, cleaning rules, duplicate/missing-record flow, source lengths, sector counts, or exclusion ledger. Three hundred MD&A items appear consistent with 100 firms × three quarters, but the paper does not explain the three missing calls or whether every source pair is aligned.

SEC filings are authoritative corporate disclosures, not authoritative bear/neutral/bull labels. Earnings-call transcripts are representations whose authority depends on provider, correction status, prepared-remarks/Q&A boundary, and speaker attribution. None of that lineage is released. The decision prompt also exposes ticker, company, sector, period, and disclosure type (Appendix D.5, p. 15) while telling the model not to use prior knowledge. The paper neither masks identifiers nor tests compliance, despite citing company-specific prior-knowledge bias as a threat (p. 3).

### Compression treatments and budgets

Each method must produce exactly 20 bullets. The naive prompt selects the “most material” single-fact bullets. Contextualization instead asks for roughly 240–250 words that preserve the dominant investment signal, comparisons, caveats, offsets, management framing, guidance, and risks so that a downstream bear/neutral/bull model retains the source's direction and confidence (pp. 3, 13). This is a legitimate task-targeted compressor, but it is trained by explicit evaluator ontology: it optimizes decision sufficiency for the disclosed three-class instrument, not generic state or evidence fidelity.

The main baselines are:

- one-shot outputs from GPT-5.4-Mini, Gemini-3-Flash-Preview, Qwen3.5-397B-A17B, and DeepSeek-V4-Flash;
- fixed-size chunking followed by compression and concatenation;
- LLMLingua and LongLLMLingua token pruning with Finance-Llama3-8B scoring;
- an Integrator that merges GPT-5.4-Mini and DeepSeek-V4-Flash views without raw-source access; and
- Agentic Context Compression (ACC), which generates two contextualized candidates, requires at least four targeted `grep_source`/`read_source_span` checks at disagreements, and selects one intact candidate by overclaim risk and source-locus coverage (pp. 4, 6, 14).

Selecting an intact candidate is a useful restraint: the auditor cannot fabricate a third synthesis. Yet it only inspects disagreements. Shared omissions, shared framing, wrong search terms, evidence outside retrieved spans, and candidate-specific defects unrelated to visible disagreement can survive. The agent model, exact tool implementation, search/span limits, candidate order, stopping behavior, overclaim/coverage scoring implementation, and invalid-run policy are not specified. “At least four checks” is an activity count, not evidence sufficiency.

The reported output/source token ratios are near 4–5%, and Appendix A varies the naive budget from 5 to 40 bullets on two 150-document subsets (pp. 6, 10). The subset selection is unspecified. A bullet count is only a coarse capacity control: word caps differ among prompts, token ratios vary, and chunking/integrator semantics differ. The paper does not report output-length distributions or budget violations.

### Decision-model protocol and estimands

Gemini-3.1-Flash-Lite receives either the full source or fixed compressed text and outputs self-reported probabilities over `bear`, `neutral`, and `bull`, framed as a disclosure-implied next-quarter total-return update with ±5% regime boundaries (pp. 3–4, 15). Three independent calls are averaged for each text. The metrics are:

1. **Decision Flip:** whether the argmax of the compressed three-run mean differs from the source three-run mean; and
2. **TVD:** total-variation distance between those two mean probability vectors.

An independent set of source rereads supplies a no-compression floor: 11.0% top-label flips and 0.078 TVD for MD&A; 8.8% and 0.058 for calls. Across three source reads, top-label self-agreement is 83.7%/85.0% and Fleiss' κ is 0.743/0.720 (pp. 4–6).

This design correctly measures probability movement even without an argmax change and exposes substantial decision-instrument instability. It does not create ground truth. The “source decision” is an LLM response conditioned on one prompt and metadata, not analyst consensus, an expert rubric, or realized return. The reported probabilities are generated JSON, not calibrated model probabilities; no proper scoring, calibration, threshold validation, or human comparison is reported.

Calling the excess over the reread floor “the compression-induced component” is stronger than the design permits (p. 4). Flip rates are nonlinear disagreement probabilities. Subtracting two marginal rates does not identify which item-level changes compression caused, especially with only three decision calls and no shared randomization or repeated compressor outputs. A source–source disagreement floor is a useful comparator; it is not an error term that can simply be removed.

The unit is the document, but firms recur over quarters and source types. The paper reports no confidence intervals, paired tests, firm/quarter clustering, multiplicity control, missing/invalid JSON handling, model-call settings, sampling seeds, endpoint dates, retry policy, or compressor-generation repeats. Each source appears to have one sampled compressed text per method, so model-dependency comparisons mix compressor-policy differences with single-generation variation.

### Main evidence

Table 2 (p. 6) reports, for MD&A / earnings calls:

- naive GPT-5.4-Mini: 33.0% / 23.9% flips and 0.172 / 0.137 TVD;
- contextualization: 21.3% / 22.2% and 0.099 / 0.116;
- LLMLingua: 53.0% / 50.8% and 0.231 / 0.247;
- LongLLMLingua: 50.0% / 39.1% and 0.226 / 0.196;
- Integrator: 24.7% / 22.9% and 0.128 / 0.128; and
- ACC: 20.3% / 18.5% and 0.102 / 0.112.

These point estimates support the narrow conclusion that fixed-length representation choice materially changes this instrument and that targeted contextualization is better than naive salience or token pruning in these cells. ACC is best by flip rate, but contextualization has slightly lower MD&A TVD (0.099 versus 0.102), so ACC does not dominate every fidelity measure. No uncertainty establishes whether 21.3% versus 20.3%, 22.2% versus 18.5%, or TVD differences are distinguishable.

Appendix A reports that increasing naive budgets from 5 to 40 bullets reduces TVD but leaves flips above the reread floor on selected 150-item subsets (p. 10). This is useful evidence against “just add a few bullets,” but the top MD&A flip series is shown as 44%, 44%, 44%, then 39%—a weak/nonmonotonic response—and no repeated compression or uncertainty is supplied.

### Directionality and model dependency

The paper plots signed movement and reports mean pairwise top-decision agreement of about 0.75 among four one-shot compressors over 597 sources (pp. 5, 10–12). This supports a configured-view warning: compressor identity changes what the downstream model sees.

It does not identify a stable bullish or bearish bias. Aggregate flip/TVD metrics are direction-blind; the paper reports no full-panel bear→neutral, bear→bull, neutral→bear, or other transition matrix. Figures 3, 7, and 8 show named ticker examples without a stated selection rule, so they cannot supply prevalence. Nor does one output per compressor distinguish systematic model tilt from generation noise. A benchmark should preserve direction and severity rather than treating all flips as equivalent.

### Decontextualization analysis

The paper uses an offline LLM pipeline to decompose source disclosures into atomic facts, copy a source sentence, and label each fact `headline`, `context`, or `boilerplate`. Context includes caveats, offsets, comparisons, expectation framing, causal drivers, timing/durability, scope/magnitude, and risk conditions (pp. 5–6, 15). In MD&A, reported context share falls from 25% in the source to 9% under naive compression, while contextualized and ACC outputs retain about 22–23%. Earnings calls show less loss.

For flip cases, omitted facts are appended to the summary. Reported source-label recovery is 37% for MD&A context facts versus 16% boilerplate and 19% random facts; calls show 33% versus 19%/27% (p. 6). This is the paper's most useful mechanistic probe: restoring typed contextual evidence is more diagnostic than restoring arbitrary content.

It remains suggestive, not causal proof:

- the decomposition and role labels have no named model, human validation, inter-rater reliability, precision/recall audit, or released records;
- “headline” and “context” are defined using the same downstream investment interpretation, creating criterion dependence;
- fact extraction explicitly skips some boilerplate before role labeling, making the source proportions dependent on an unreported preprocessing filter;
- the selection and number of appended facts are not specified;
- add-back exceeds the original budget and changes input length/order;
- only observed flip cases are analyzed, conditioning on the outcome; and
- 63%/67% of context add-backs still do not recover the source label, while some placebos do.

The experiment supports **context omission as one plausible mediator**, not the claim that it explains all or most flips.

### Factuality and plausibility are asserted, not measured

The abstract and conclusion emphasize fluent, factually plausible or factually accurate summaries (pp. 1, 7), but the study reports no fluency evaluation, factuality metric, atomic entailment accuracy, human audit, unsupported-claim rate, or source-locator precision. ACC's internal overclaim audit is a selection procedure, not an independently evaluated factuality measure. The core result is therefore decision discrepancy under a model instrument; the paper does not empirically show that discrepant summaries passed factuality while failing decision fidelity.

### Cost and operational evidence

Table 2 reports aggregate dollar costs for generative methods, such as $6.69/$3.83 for naive compression and $9.07/$7.52 for ACC (MD&A/calls), but does not define included calls, token prices, model endpoints/dates, retries, decision-evaluation cost, local token-pruning compute, latency, or per-document versus panel accounting (p. 6). Token pruning is shown with no cost, precluding a complete trade-off. ACC's MD&A cost is lower than the simpler Integrator's despite source-audit tool use, with no accounting explanation.

The industry case applies ACC in a “globally deployed commercial equity-forecasting product” over the same S&P 100 fiscal panel. Absolute metrics are withheld. The paper reports >90% token reduction, naive degradation in forecasting information coefficient (IC), ACC improvement of 8.3% over original-source IC and 23.8% over naive IC, and 59.5% fewer source-relative decision flips (p. 7).

This is an unauditable experience report, not independent production validation. The product, forecast target, IC definition, baseline magnitude, horizon, portfolio construction, sample size/unit, leakage controls, transaction costs, deployment dates, live versus retrospective status, significance, model/configuration, failures, and absolute effect are absent. A relative 8.3% change can be trivial or unstable when the denominator is small. Several authors are affiliated with finance firms and LinqAlpha, but organizational access does not substitute for an inspectable protocol. The case neither validates the paper's three-class instrument nor establishes investment performance, institutional usefulness, safety, or readiness.

## Unique insight

The paper's durable contribution is not a new scalar called “information fidelity.” It is the recognition that a compressed representation is an **intervention on the downstream evidence view**, and factual entailment alone cannot validate it.

For `skill-bench`, the repaired chain is:

```text
source/state authority and version
→ compression treatment and sampled output
→ retained / omitted / transformed claim ledger
→ downstream instrument identity and admissible evidence view
→ source-view and compressed-view response distributions
→ directional decision discrepancy with severity
→ independent correctness / expert / outcome evidence
→ bounded claim and stakeholder consequence
```

At least five outcomes must stay separate:

1. **state/evidence fidelity:** authoritative claims, provenance, valid time, contradiction, uncertainty, and artifact state survive;
2. **task sufficiency:** the compressed view supports the realized and alternate valid operations;
3. **decision-instrument preservation:** a named evaluator/policy returns a similar distribution under source and compressed views;
4. **decision correctness:** the resulting decision agrees with independently warranted expert, rule, or outcome evidence; and
5. **consequence fidelity:** policies selected under compression preserve stakeholder-relevant rankings, losses, safety, and burden.

Decision preservation can be undesirable when the source instrument is biased or wrong. Decision change can be desirable when compression removes irrelevant distraction. Neither label agreement nor discrepancy has a fixed valence without an independent decision warrant.

## Evidence and claim boundaries

### Strongly supported by the manuscript

1. Twenty-bullet compression materially changes one fixed LLM's source-conditioned bear/neutral/bull output on the reported financial panel.
2. The source-reading instrument itself has nontrivial reread instability, making an identity/no-compression comparator necessary.
3. Naive salience and token pruning show larger reported discrepancy than a decision-targeted contextualization prompt.
4. Different one-shot compressor models expose materially different downstream decision views.
5. Typed caveat/comparison/offset facts are a plausible diagnostic target, and adding them back recovers more flip cases than reported placebos.
6. ACC is a concrete multi-candidate, targeted-source-audit procedure and has the lowest reported flip rate in both source types.

### Partially supported

- **ACC improvement:** point estimates improve versus naive and Integrator, but not every TVD cell, with no uncertainty, compressor repeats, or released runs.
- **Decontextualization mechanism:** LLM role proportions and add-back ordering are consistent with mediation, but labels are unvalidated and the intervention changes budget/order on outcome-selected cases.
- **Model-specific tilt:** compressors disagree and example directions differ, but full directional transition counts and repeated generations are absent.
- **Budget robustness:** selected subsets remain above the reread floor at 40 bullets, but subset provenance and uncertainty are missing.
- **Efficiency:** output ratios are reported, but full cost, compute, latency, and failure accounting are not.

### Not supported

- an authoritative or correct “source-implied” investment decision;
- human analyst agreement or professional decision quality;
- calibrated probability or realized-return prediction;
- factual accuracy, factuality-preserving but decision-changing prevalence, or fluency quality;
- causal identification of compression-induced excess flips by subtracting a reread floor;
- reliable compressor effects across sampled outputs;
- general preservation across downstream users, decisions, domains, or alternate futures;
- reproducible product IC gains or deployment economics;
- professional validity, safety, production fitness, or readiness.

## Limitations

1. The source manifest, transcript provider, cleaning, exclusions, missing-call flow, and firm/quarter lineage are unreleased.
2. Company/ticker/sector metadata may activate prior knowledge despite a prompt prohibition; no masking ablation is run.
3. The source “label” is an LLM reading, not expert or outcome ground truth.
4. Three generated JSON probability calls do not establish calibrated beliefs.
5. The no-compression floor measures reread disagreement but cannot be subtracted as an identified causal component.
6. Only one compressed output per method/source appears to be evaluated; compressor stochasticity is unmeasured.
7. No exact endpoint snapshots, temperatures, seeds, retries, dates, invalid-output policy, or failure ledger are reported.
8. Repeated quarters and two source types within firms are ignored in uncertainty; no intervals or paired/clustered tests are reported.
9. Multiple method, source, budget, model, and diagnostic comparisons have no multiplicity treatment.
10. Fixed bullet count does not ensure equal token capacity; prompt word caps and output distributions differ.
11. Contextualization directly encodes the decision grader's ontology and therefore measures a rubric-aligned intervention.
12. ACC's agent identity and tool realization are incomplete; mandatory searches do not guarantee evidence sufficiency.
13. Disagreement-only audits miss shared omissions and shared framing.
14. The fact inventory and role labels have no human or independent validation.
15. Add-back changes budget and ordering, conditions on flips, and has unspecified fact selection/count.
16. Aggregate flip/TVD hides directional severity and asymmetric consequence.
17. Named-ticker movement figures lack a disclosed selection rule.
18. Factuality and fluency are claimed but never measured.
19. Cost boundaries are incomplete; token-pruning compute and evaluation/latency costs are absent.
20. The product case withholds nearly every quantity required to audit IC, significance, leakage, and operational value.
21. No official artifacts permit result replay or implementation inspection.
22. S&P 100 disclosures from three 2025 quarters do not establish other firms, periods, documents, decisions, or domains.

## Reproducibility and operational realism

Reproducibility is **weak**. The complete prompts are unusually useful, including exact 20-bullet instructions, the ACC runtime contract, the decision JSON schema, and fact-role definitions (pp. 13–15). The paper names principal models, source counts, budgets, formulas, and point estimates.

However, no source manifest, data snapshot, code, generated summaries, decision calls, fact inventories, ACC traces, run configuration, cost ledger, or result tables are released. Transcript licensing may constrain redistribution, but SEC accession locators and derived run manifests could still have been supplied. Proprietary/future model endpoints and mutable APIs prevent exact reconstruction. The commercial case is not reproducible at all.

Operational realism is mixed. Long corporate disclosures, caveat-sensitive interpretation, fixed evidence budgets, source audit, and downstream forecast integration are realistic pressures. Yet the main task is one model's disclosure-only three-class update—not an analyst workflow with valuation, prior beliefs, market context, portfolio constraints, accountability, or realized stakes. The study evaluates a single transformation, not recurrent agentic compression where omissions compound across handoffs and actions.

## Transfer to skill-bench

### Retain

1. **Measure downstream decision distributions, not only lexical/factual similarity.** Bind every result to the exact decision instrument, prompt, metadata view, label space, threshold, and repeated-call policy.
2. **Keep an identity/reread floor.** Source-view instability is part of the instrument and must not be attributed to compression.
3. **Type contextual relations.** Caveat, offset, comparison, expectation frame, cause, timing/durability, scope/magnitude, and risk condition should link to the headline claim they qualify.
4. **Use candidate disagreement to target source audit.** Preserve the intact candidate and record every search, span, omission, and selection reason.
5. **Report probability movement and direction.** Argmax flips alone discard near-threshold movement and consequence severity.

### Repair

1. **Add an independent decision warrant.** Compare source and compressed views against expert/rule/outcome evidence where legitimate; never equate preserved model output with correctness.
2. **Repeat both stages.** Cross compressor-output samples with repeated decision-instrument reads; estimate task/firm/configuration variance rather than averaging three judge calls only.
3. **Use paired directional estimands.** Report full transition matrices, signed shifts, asymmetric loss, item-level source/source and source/compressed coupling, and clustered uncertainty.
4. **Factor metadata access.** Test named versus masked sources and log whether company identity is legitimately available.
5. **Validate context labels.** Preserve source locators and independent/human dispositions for claim role, target headline, and omission consequence.
6. **Replay mediation at fixed capacity.** Swap or restore one context relation while holding length/order as constant as possible; do not infer causality from an over-budget add-back alone.
7. **Audit shared omissions.** Candidate disagreement is a search trigger, not a completeness oracle; include source-coverage sampling and high-severity invariant checks.
8. **Keep factuality and decision fidelity orthogonal.** A 2×2 design—factually supported/unsupported × decision-preserving/changing—is more diagnostic than prose claims of plausibility.
9. **Preserve raw authority.** Compression outputs remain derived views and cannot overwrite source evidence or become authoritative merely because the policy agrees.
10. **Use a complete resource boundary.** Include compression generation, audit/tool calls, decision reads, retries, failures, tokens, compute, latency, and human review.

## Concrete next actions

1. **No new build task.** The existing context-compression conformance slice already separates raw evidence, reset/reformat/compression treatments, typed invariants, next-action/alternate-future sufficiency, and efficiency. Extend its next calibration only when a real pilot exists: add a versioned decision-instrument response, source/source floor, source/compressed directional distribution shift, and an explicitly independent correctness/consequence field. Do not create a finance-specific subsystem.
2. In the next consolidation, add this source to ACON's conclusion: task reward can miss state corruption, while decision preservation can detect consequence-relevant reweighting—but remains evaluator-relative and can preserve error.
3. Any pilot adopting compression should predeclare the state/task/decision/consequence claim ladder, repeat compressor and downstream-policy calls, cluster by task/source lineage, and preserve immutable raw evidence plus all sampled compressed views.

## Action items

- [x] Read the complete immutable v2 paper, including appendices and exact prompts.
- [x] Reconstruct sampling, compression treatments, decision instrument, metrics, diagnostics, ACC, costs, and product case.
- [x] Separate source authority, state fidelity, task sufficiency, decision preservation, correctness, and consequence.
- [x] Compare nonduplicatively with ACON and the existing conformance slice.
- [x] Verify that no author-owned artifact was available for release inspection.
- [x] Add no duplicate queue task.
