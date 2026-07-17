# Bridge Evidence: document omission identifies configured trajectory dependence, not portable evidence value

- **Paper:** <https://arxiv.org/abs/2607.15253v1>
- **Authors:** Debayan Mukhopadhyay, Utshab Kumar Ghosh, Shubham Chatterjee
- **Date read:** 2026-07-17
- **Source:** complete immutable arXiv v1, submitted 16 July 2026; metadata says “Preprint; extended version in preparation”
- **Local PDF:** `data/papers/pdfs/2607.15253v1-bridge-evidence.pdf` (10 pages; SHA-256 `386320cf1e99962da6deb4182475bdbe53ff4f201120d505425ed4a77ce303a8`)
- **Local text:** `data/papers/text/2607.15253v1-bridge-evidence.txt` (SHA-256 `039d85fcbd342d8429a0c9663b29c6feeb484d12586c219947f0597d09c63869`)
- **Metadata:** `data/papers/source/2607.15253v1-metadata.xml` (SHA-256 `e8860902de47a37c8cf81aa66a4c1da5512b736ff45e0575a563e4862b344dcd`)
- **Release status:** no author-linked code, data, run archive, or project repository appears in v1; exact-title, arXiv-ID, and method-name searches on 2026-07-17 found only arXiv surfaces
- **Tags:** evidence-use, counterfactual-replay, agentic-retrieval, source-packs, causal-validity, trace-intervention, multi-hop-search

## One-sentence contribution

The paper replaces static document relevance with a deletion-and-replay estimate of whether one displayed document changed one configured search trajectory, revealing a valuable evidence-availability→adoption→next-operation→outcome boundary while its composite score, nested observations, selected substrate, and absent release prevent “bridge evidence” from becoming a portable document label or a general causal-utility measure.

## Bottom line

The paper asks the right benchmark-design question: **did evidence merely look relevant, or did its presence change what the agent did and what followed?** It runs a document-level omission intervention over a deterministic ReAct-style Qwen2.5-7B-Instruct agent on a stratified 1,000-question HotpotQA sample. For each displayed document at each search step, the authors delete that document, retain the logged prefix, and regenerate the continuation. Across 23,322 document observations from the surviving multi-step trajectories, their static reader delta and composite Counterfactual Trajectory Utility (CTU) have Spearman correlation −0.0257. A second, selected proxy analysis over 9,600 observations where BM25 and cross-encoder classifications agree also gives near-zero correlation (−0.0161). These are useful falsifications of static relevance as a sufficient proxy for this agent’s trajectory dependence.

The most reusable insight is narrower than the title’s “causal utility.” Evidence can contribute by changing a **future acquisition action** rather than directly supporting a final answer. That matters far beyond web search: a meeting note may supply the identifier needed to inspect a contract; an exception log may nominate the next diagnostic; a workbook note may reveal which dependency to test. Static source relevance, content overlap, citation, and even answer containment can all miss that role.

But the paper’s strongest rhetoric outruns its estimand. CTU is an equal-weighted sum of globally min–max-normalized changes in final-answer F1, next-query gold-document nDCG, and turn count. Positive and negative consequences can compensate. A document can cross the “helpful” threshold while final-answer quality does not improve—or even worsens—if the other terms offset it. Calling every high-CTU/low-static document “causally load bearing” therefore promotes a configured **net composite effect** into necessity and value. The intervention identifies dependence of one deterministic continuation on one removal under one model, prompt, rank list, history, retriever, four-turn cap, and dataset oracle; it does not identify a stable property of the document, a unique mechanism, professional benefit, or evidence that another system should retrieve.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C by connecting source-pack design, trajectory evidence, and causal diagnosis. HotpotQA is only the experimental substrate; the transfer is cross-domain and does not narrow `skill-bench` to question answering or retrieval.

The paper sharpens an evidence-use chain already implicit in the repository:

`available source → displayed view → agent observation → proposition/entity uptake → next decision or acquisition operation → changed evidence/state → artifact/action consequence → recipient or stakeholder outcome`

Each edge needs a distinct observation or warrant. The paper intervenes at displayed availability and observes generated continuation plus benchmark proxies. It does **not** directly observe whether the model semantically adopted a proposition, whether the changed next query is justified, whether retrieved gold evidence is used, whether the final answer is professionally acceptable, or whether the source has value outside this configured continuation.

For `skill-bench`, the immediate correction is: do not grade source use only by citations, static relevance, or overlap with a reference source set. Preserve source-to-next-operation lineage and, on selected tasks, run matched omission, substitution, or stale-evidence replays. Report criterion-level effect vectors before any scalar. A source that changes only search direction is diagnostically different from one that changes artifact content, safety, effort, or final acceptance.

## Research question and supported claim

The paper asks whether a document’s static usefulness to a history-free reader predicts its causal contribution to a multi-step search agent, and whether discriminative entities explain documents that redirect future search (Sections 1–2, pp. 1–6).

### What the evidence supports

- On this frozen ReAct-style Qwen2.5-7B-Instruct/Wikipedia/BM25/cross-encoder package, omission replay often produces a different continuation even when a history-free reader gains no answer F1 from the removed paragraph.
- Across 23,322 nested document observations, ΔSRU and the paper’s configured CTU composite have negligible rank association: Spearman ρ = −0.0257 (Table 4, p. 6).
- The low-SRU/high-CTU cell contains 8,331 observations (35.72%), although the paper correctly notes this proportion is nearly implied by the marginals because only 3.30% of records have positive ΔSRU (Tables 3–4 and Section 3.6, pp. 6–8).
- On the 9,600-record subset where thresholded BM25 and cross-encoder signals agree, 2,607 observations (27.16%) are proxy-low/CTU-high and the proxy–CTU correlation is −0.0161 (Table 5 and Section 3.4, pp. 7–8).
- High-OER entities appear verbatim in the next query at 6.1% of entity-step observations versus 1.5% for entities absent from gold-supporting documents, a 4.02× descriptive ratio over 227,139 entity-step observations (Table 6, p. 7).
- The authors transparently retract a turn-count interpretation, report that bridge-cell localization of propagating entities did not replicate, and disclose the SRU skew and proxy-subset exclusion (Sections 3.5–3.6, pp. 7–9).

### What the evidence does not support

- That CTU is intrinsic or portable “document utility”; the paper itself types it as a property of document set, agent, and state (Equation 12, p. 4).
- That every high-CTU document was necessary for final success, improved final answer quality, or should be retrieved by another agent.
- That the omitted document’s semantic content—rather than rank-list length, attention allocation, context perturbation, or deterministic path sensitivity—is the unique operative cause.
- That the next-query term measures good reasoning rather than movement toward the dataset’s authored gold-supporting articles.
- That OER mediates the CTU effect. H1 is an observational association between entity class and query string; the bridge-specific H2 is inconclusive and uses a discrepant CTU cutoff.
- That repeated document/entity observations supply independent evidence at the printed sample size.
- That the result transfers to open-ended source packs, contradictory evidence, professional artifacts, non-Wikipedia tools, other agent architectures, or consequential work.
- That static relevance never matters. The experiment rejects sufficiency/predictiveness for this configured population; it does not show that static relevance has zero value in retrieval portfolios.

## Methodology and system reconstruction

### Population and selection

The source population is HotpotQA’s 7,405-question development set. The authors retain questions only when every supporting-article title appears in the top 50 BM25 results for the original question, then draw a fixed-seed stratified sample of 1,000 preserving roughly the dataset’s 70/30 bridge/comparison question-type mix (Section 2.4, p. 3). Seventy-four one-turn trajectories are removed because CTU is said to require a subsequent step (Section 3.1, p. 6).

This creates a **reachable-gold, multi-step, successful-instrument population**, not general search work. It excludes exactly the cases where first-stage retrieval cannot surface the authored evidence and removes short trajectories. The final paper does not report how many of the 1,000 remain after the 74 exclusions in a single denominator table, nor how observations distribute by question, step, rank, or base success. Document records are clustered within steps, trajectories, questions, repeated question–document pairs, and one configured model.

### Agent and retrieval stack

The agent is Qwen2.5-7B-Instruct under a reproduced ReAct-style prompt, with temperature 0, sampling disabled, identical hardware, no repeated query, and at most four searches (Sections 2.2–2.3 and Appendix A, pp. 2–3, 10). BM25 retrieves 50 Wikipedia paragraphs; a cross encoder reranks them; the top ten are displayed. Displayed document IDs are deduplicated across turns, so the analysis uses the records actually shown rather than recomputed ranks.

This is a well-specified configured-system boundary in prose. It is not a reproduced system identity: v1 names no exact Wikipedia snapshot, paragraph-index build, BM25 implementation/parameters, cross-encoder checkpoint, Qwen revision/runtime, prompt serialization, hardware, seed, deterministic-kernel settings, entity-linker version, or run manifest. No release allows those details or outputs to be inspected.

### Omission intervention

For each displayed document at each search step, the authors remove it from the top-ten list, yielding nine documents, reuse the original prefix, and regenerate from the intervention point (Equation 3 and Section 2.5, p. 3). This is stronger than inferring use from a citation or attention proxy: it creates a matched availability contrast before downstream behavior.

However, “the original run and counterfactual differ in exactly one thing” needs qualification. The assigned treatment is indeed one list-element omission, but that treatment jointly changes document content, list length, later item positions, attention competition, and the serialized context. It estimates the total effect of **this removal operation**, not the isolated semantic contribution of the document. A length-preserving neutral replacement, content-preserving permutation, paraphrase, entity mask, and sham deletion would be needed to separate these mechanisms.

Approximate determinism is another validity condition. One continuation is run per condition. Temperature zero and fixed hardware reduce variation but do not estimate replay noise. Without duplicate unchanged-prefix replays, an observed delta cannot be separated from residual endpoint or kernel nondeterminism at the item level.

### Static RAG Utility

A history-free reader receives the question plus one paragraph and must answer from that document or return `UNANSWERABLE`. ΔSRU is answer F1 with the document minus answer F1 from a no-document parametric baseline (Equations 4–6, pp. 3–4). Subtracting the no-document baseline correctly avoids crediting a paragraph for parametric knowledge.

The instrument is nonetheless poorly matched to multi-hop paragraphs by design. Mean F1 is 0.0170 with a document and 0.0122 without; only 7.50% of records contain the answer string (Table 2 and Section 3.6, pp. 6, 8). Thus ΔSRU ≤ 0 usually means **the reader failed in both conditions**, not affirmative evidence that the paragraph lacks static evidentiary value. The authors acknowledge this. The central result is best phrased as failure of this static answer-improvement instrument to predict CTU, not proof that all low-SRU documents “look useless” under every legitimate static relevance measure.

### Counterfactual Trajectory Utility

The omission continuation is compared with the base on:

1. `Δanswer = F1_base − F1_counterfactual`;
2. `Δnext-query = nDCG@10(base next query) − nDCG@10(counterfactual next query)` against HotpotQA supporting facts;
3. `Δeffort = counterfactual turns − base turns`.

Each component is min–max normalized using observed global ranges and the three normalized values are summed with equal weights (Equations 7–10, p. 4). The resulting zero-raw-change point is 1.4 in this sample because the observed raw ranges are [−1,1], [−1,1], and [−2,3]. CTU > 1.4 is called high/helpful (Equation 11 and Table 1, p. 4).

This is an interpretable exploratory vector but a weak unitary utility:

- global min–max normalization makes values and the 1.4 offset depend on the observed sample ranges;
- equal normalized weights are not justified by stakeholder loss or construct validity;
- final correctness, gold-retrieval direction, and turns are not commensurate;
- signed compensation means a harmful answer delta can be outweighed by query/effort terms;
- nDCG uses the same dataset gold structure that selected reachable questions;
- fewer turns can mean efficiency, premature wrong closure, or inability to continue;
- the paper does not specify complete missing/terminal semantics for the next-query component when a continuation answers instead of searching.

The “natural threshold” is therefore the zero of one chosen compensatory index, not a natural boundary between necessary and unnecessary evidence. `skill-bench` should keep the three effects separate and add safety, artifact, collateral-state, and recipient outcomes where relevant.

### Quadrants and statistics

The main 2×2 table thresholds ΔSRU at zero and CTU at 1.4. Cell C (low static/high CTU) is named bridge evidence. Spearman correlation is also reported overall and by counterfactual turn count. The authors correctly reject the turn-count subgroup pattern after noticing that the grouping variable contains CTU’s effort term.

The proxy robustness check labels a document high only when both normalized BM25 and cross-encoder scores exceed selected global cutoffs, and low only when both fall below selected cutoffs. It excludes 13,722 of 23,322 observations (58.84%) where signals disagree. The surviving 9,600 records are a consensus-selected subset, not an evenly representative axis or a robustness result over the complete population. It does show that the weak-reader instrument alone cannot explain the pattern.

No uncertainty is clustered by question or trajectory. The Spearman test and OER chi-square operate on heavily nested document/entity observations; 227,139 is not the number of independent experimental units. The paper reports 2,000 bootstrap resamples for propagation intervals but does not say that resampling occurs at the question or trajectory level. Extremely small p-values therefore should not be interpreted as population-level precision.

### Entity propagation mechanism

The authors union top-20 cross-encoder candidates with shown documents per step, derive three relevance levels from HotpotQA supporting facts, link candidate documents with WAT, and calculate Observable Entity Relevance as a support-weighted smoothed log-odds contrast (Section 2.8, pp. 5–6). An exact propagation event occurs when the full normalized entity title appears in the next query; a looser token criterion is secondary.

H1 is supported descriptively: exact propagation is 6.1% for high-OER versus 1.5% for low-OER entity-step observations. This establishes that entities concentrated in gold-supporting candidate documents are more likely to appear verbatim in the next query. It does not establish mediation from omitted document through entity uptake to CTU. Entities are not randomized or masked; baseline occurrence, entity salience, title length, model familiarity, question wording, document rank, and repeated entities are not controlled.

The paper is commendably candid about H2. Bridge-document entities do not robustly propagate more than Cell A entities; the direction changes across pilot/full sample and matching rules, Cell A has only 321 high-OER observations, and Table 7 accidentally uses CTU > 1.6 rather than 1.4 (Section 3.5, pp. 7–8). The claimed specific mechanism—bridge documents earn value by supplying discriminative entities—remains a plausible hypothesis assembled from two findings, not a demonstrated mediator.

## Unique insight

The unique insight is not simply “multi-hop retrieval needs intermediate facts.” It is a measurement correction:

> Evidence role is relational and temporally indexed. A source can have low direct-answer value yet high transition value because it changes the next admissible operation.

That yields a reusable role vocabulary for source packs:

- **terminal support:** directly supports a required claim or artifact field;
- **bridge/transition support:** supplies an identifier, relation, threshold, contradiction, or cue that changes the next operation;
- **verification support:** enables checking or falsifying an existing candidate;
- **boundary support:** changes whether action, clarification, abstention, or escalation is legitimate;
- **redundant support:** contains relevant content but adds no configured marginal effect at that state;
- **distractor or harmful support:** changes behavior without improving the intended consequence;
- **unexercised support:** was available/displayed but has no supported downstream-use edge.

These are **source-at-state roles**, not permanent document labels. The same contract can be terminal in one trajectory, bridge in another, redundant after earlier evidence, and harmful when stale. This is the main addition to `skill-bench`’s existing availability/access/adoption/consequence ladder.

## Limitations and validity threats

1. **Single configured agent.** One Qwen2.5-7B-Instruct prompt and retrieval stack cannot establish cross-model or cross-scaffold transport.
2. **Single synthetic QA substrate.** HotpotQA’s two-hop, authored-support structure is unlike messy professional evidence, alternative valid sources, and open-ended artifacts.
3. **Reachability selection.** Only questions whose gold article titles appear in the original-query BM25 top 50 are eligible.
4. **Multi-step selection.** Seventy-four one-turn trajectories are excluded; applicability is conditional on a generated trajectory property.
5. **No release.** Code, index, source snapshot, prompts as serialized, logs, interventions, outputs, seeds, and analysis tables are unavailable.
6. **Incomplete system identity.** Retriever, reranker, model runtime/revision, corpus snapshot, hardware, and deterministic settings are not pinned.
7. **No sham replay.** Duplicate unchanged-prefix continuations do not estimate residual nondeterminism.
8. **Removal bundles mechanisms.** Content, context length, positions, and attention competition change together.
9. **No replacement control.** A neutral length-preserving replacement or irrelevant-document substitution is absent.
10. **Nested observations.** Documents and entities share steps, trajectories, questions, source articles, and one model; printed n values are not independent units.
11. **Unclustered inference.** Correlations, chi-square p-values, and apparently entity-level bootstrap intervals do not account for question/trajectory clustering.
12. **Weak static reader.** Near-floor F1 makes nonpositive ΔSRU mostly an uninformative tie.
13. **Answer containment is narrow.** Exact answer strings miss legitimate paraphrase and intermediate evidentiary value.
14. **Composite construct.** Answer, next-query nDCG, and turns are added without an empirical or decision-theoretic scale.
15. **Sample-dependent normalization.** CTU values and zero-effect offset depend on global observed ranges.
16. **Compensatory threshold.** Positive and negative effects can cancel; high CTU does not imply improved final answer or necessity.
17. **Gold-shaped local outcome.** Next-query nDCG rewards movement toward HotpotQA’s nominated supporting documents, not all justified acquisition paths.
18. **Terminal/missing semantics under-specified.** The paper does not fully specify next-query scoring when the base or counterfactual continuation answers at the intervention step.
19. **Effort ambiguity.** Turn count omits tokens, latency, calls, retrieval cost, and review burden; early wrong closure can look efficient.
20. **No base-success stratification.** Marginal effects may differ when the original trajectory is correct versus already failed.
21. **Quadrant prevalence depends on marginals.** The 35.72% headline nearly follows mechanically from 3.30% positive SRU and 36.85% high CTU.
22. **Proxy analysis selects agreement.** It discards 58.84% of records, potentially the most diagnostically interesting ranking disagreements.
23. **Thresholded proxy loses rank information.** Global median/75th-percentile conjunctions are not the deployed ranking policy.
24. **Mechanism not mediated.** OER→query association and document omission→CTU are not joined in one controlled mediation analysis.
25. **Confounding in entity propagation.** Rank, salience, title length, prior mention, question wording, and model familiarity are uncontrolled.
26. **Low absolute propagation.** Even high-OER entities propagate exactly only 6.1% of the time.
27. **H2 fails to replicate.** Bridge-specific propagation changes direction and uses an inconsistent 1.6 threshold.
28. **No contradictory/stale evidence.** Deletion tests availability but not precedence, supersession, authority, or harmful adoption.
29. **No alternative-source intervention.** Removing one source may be harmless only because equivalent evidence remains; redundancy is state- and source-set-dependent.
30. **No professional consequence.** Final QA F1 and authored-support retrieval do not establish artifact quality, acceptance, safety, cost, or readiness.

## Reproducibility and operational realism

Reproducibility is **weak**. The immutable ten-page paper provides equations, aggregate tables, three prompts, a high-level stack, and several candid negative results. That is enough to reconstruct the intended instrument and audit its claim logic. It is not enough to reproduce any row. No code/data link appears in v1, and searches found no author-owned release. The paper contains an ACM placeholder DOI and conference boilerplate, while arXiv metadata labels it a preprint with an extended version in preparation.

Operational realism is **moderate for sequential evidence dependence and low for knowledge work**. The intervention occurs inside an actual multi-turn generated trajectory and preserves the prefix, which is substantially more realistic than a history-free document label. Yet the environment is a clean static Wikipedia index, the task has one short answer and authored gold supporting facts, evidence is always text, actions are searches, the horizon is four turns, and there are no permissions, source authority, contradictions, evolving validity, artifact mutations, human handoffs, or external consequences.

The omission sweep is also expensive: each displayed document requires a continuation replay. The paper reports neither model-call counts, token/runtime/GPU totals, failed replay counts, nor amortized cost. A benchmark should reserve such interventions for calibration and diagnostic samples rather than make them a universal grader.

## Transferable design implications for skill-bench

### Retain

1. **Matched prefix replay.** Freeze task, configured system, initial state, evidence order, and trajectory prefix before changing one source exposure.
2. **Source-at-state roles.** Type terminal, transition, verification, boundary, redundant, harmful, and unexercised roles per evidence opportunity rather than globally.
3. **Future-operation effects.** Observe not only final artifacts but also changed search, inspection, query, calculation, escalation, and verification actions.
4. **Parametric/no-source controls.** Separate what a system already produces from what the source contributes.
5. **Negative results and confound audits.** Preserve retracted subgroup interpretations and failed mechanism hypotheses rather than laundering them into the headline.

### Repair

1. **Keep an effect vector:** final criterion effects, next-operation effects, artifact/state effects, safety/collateral effects, effort/cost, and invalidity. Do not call an equal-weight sum “utility” without stakeholder weights.
2. **Use typed estimands:** `availability_total_effect`, `semantic_content_effect`, `entity_or_cue_mediation`, `necessity_given_source_set`, and `downstream_consequence_effect` are different.
3. **Add controls:** unchanged replay, length-preserving neutral replacement, irrelevant replacement, order permutation, paraphrase, cue/entity masking, stale substitution, and equivalent-source substitution.
4. **Record realization:** source available, displayed, inspected, quoted/cited, proposition/cue adopted or rejected, next operation, new evidence/state, final artifact, and consequence.
5. **Cluster uncertainty:** resample and analyze at the task/trajectory level; report document/entity counts as observation volume, not independent n.
6. **Fail closed:** terminally undefined next operations, replay failures, nondeterminism, missing state, and invalid graders must not become zero effect.
7. **Bound claims to configuration and state:** report exact model/scaffold/tools/source-pack/version/prefix and do not promote marginal effects into document quality.
8. **Measure source-set interactions:** test omission singly and in planned combinations where substitutes, contradictions, or prerequisites exist.

### Test

1. **Cross-domain matched omission matrix:** use at least two unlike knowledge-work shapes, such as a procurement memo and an operational incident brief. Plant one terminal source, one transition cue, one legitimate substitute, one stale contradiction, and one distractor.
2. **Mechanism contrast:** compare true omission, neutral placeholder, entity/cue mask, and semantically equivalent paraphrase under identical length/order.
3. **Effect-vector noncompensation:** include a case where fewer steps produce a wrong unsafe artifact and require the report to preserve the negative final/safety effect despite efficiency gain.
4. **Alternative-evidence interaction:** remove each of two substitutes singly and jointly; distinguish marginal redundancy from set-level necessity.
5. **Replay-noise gate:** run unchanged-prefix duplicates before interpreting small deltas; mark effects below configured noise as unresolved.
6. **Human/recipient consequence:** where feasible, ask an independent recipient to use the resulting artifact and measure correction, decision, burden, and acceptance separately.

## Comparison with reviewed work

- **Workspace-Bench** separates source availability, relevance, provenance, observed use, and causal use. Bridge Evidence contributes a concrete availability intervention but does not observe professional workspace integrity or recipient consequence.
- **LongMedBench** shows that history volume and factual access do not establish history necessity or appropriate downstream action. Bridge Evidence offers the matched omission pattern that a stronger longitudinal test needs, while its HotpotQA oracle remains behaviorally narrow.
- **Search-Time Contamination** argues that exposure audits cannot estimate clean-score inflation without paired masking/replay. This paper demonstrates that replay logic on legitimate intermediate evidence, but not contamination role separation or open-search snapshot validity.
- **STRACE and Who&When Pro** distinguish supported causal slices or controlled injected deltas from surface attribution. Document omission is stronger than verbal root-cause labeling, yet it still needs alternative mechanisms, replay-noise controls, and effect-specific propagation evidence.
- **Context-Mediated Domain Adaptation** records source-to-edit provenance but lacks forward evidence that stored context was retrieved, adopted, or useful. Bridge Evidence supplies one forward-use intervention, while still stopping before expert authority, acceptance, or transfer.
- **EvoMemBench and the experience-memory conformance pilot** already require delivery, adoption, action, and consequence links plus removal/substitution controls. The present paper sharpens the missing transition-role and source-set interaction tests rather than motivating a new retrieval-specific schema.

## Action items for repository

- [x] Preserve and read the complete immutable v1 PDF/text plus versioned arXiv metadata.
- [x] Record the absence of a verifiable author-linked v1 code/data/run release.
- [x] Add this review to the evidence-use/workspace collection in `papers/topic-index.md`.
- [x] Add the source-at-state role and noncompensatory omission-replay implication to `docs/research-synthesis-index.md`.
- [ ] Build one small cross-domain source-at-state omission/substitution conformance matrix using existing trace, evidence-state, artifact, metric, and validity records; do not create a retrieval-specific schema.
