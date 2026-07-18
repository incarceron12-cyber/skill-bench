# Iterate Until Retrieved: discoverability optimization is not correction validation

## Source, review status, and charter fit

**Deep review of the complete immutable primary source and arXiv source package.** I read the full 11-page paper, its complete layout-preserving extraction, API metadata, and the 10-member LaTeX source archive. I inspected the method, production setting, five variants, all result tables, judge study, costs, prompts, classifier calibration, and sanitized worked example. The paper names no code or data release. Exact-title/ID searches of GitHub repositories, Hugging Face models/datasets/spaces, Mosaic's site, and the open web on 18 July 2026 found no official empirical release; search provenance is preserved locally.

- **Paper:** Moshe Hazoom, Gal Patel, Alon Talmor, and Tom Hope, *Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG*, arXiv:2605.25641v1, 25 May 2026, <https://arxiv.org/abs/2605.25641v1>
- **Local PDF:** `data/papers/pdfs/2605.25641v1-factual-nugget-optimization.pdf` (11 pages; SHA-256 `ceddba72ea6ab985e74a7d1cedc81a80315167327be6c86005f741b846925a10`)
- **Local text read in full:** `data/papers/text/2605.25641v1-factual-nugget-optimization.txt` (46,824 characters in the acquisition record; SHA-256 `b62ae6d4025775fd49ccec9312c2c963bbcbb4942ba1bececec21fd99da7f1a3`)
- **API metadata:** `data/papers/source/2605.25641v1-metadata.xml` (SHA-256 `89ed0baeb12f892a16f341f377561a2437953768c1856bee4261fb893372db1c`)
- **Source archive:** `data/papers/source/2605.25641v1-source.tar.gz` (SHA-256 `bec08b5eedf23e06db9cd78a4c5f9b2102ff76a0e3db0e4366ee99e894594b3e`)
- **Release-search provenance:** `data/sources/releases/2605.25641v1-factual-nugget-optimization/provenance.json`
- **Evidence boundary:** real company feedback, corpora, queries, prompts, nuggets, traces, human labels, and trial rows are proprietary and unreleased. Results are author-reported and cannot be recomputed.

This advances charter objectives A, B, D, and E through a cross-domain question: when can a correction become durable context that is discoverable and correctly used later? Product support is a methodological case, not a proposed benchmark scope.

## One-sentence contribution

The paper introduces Iterative Nugget Optimization (INO), which converts selected free-form user corrections into atomic auxiliary knowledge-base documents and repeatedly rewrites their titles, bodies, and retrieval anchors against the deployed retrieval-and-answer stack, producing large reported retrieval and citation gains on selected production-derived queries—but it validates **representation fit to one frozen stack**, not correction authority, semantic preservation, independent factual correctness, temporal validity, or production utility.

## Why this matters

The paper addresses a real failure between “we received a correction” and “a future agent can use it.” Merely storing a lesson is not enough: the lesson must survive indexing, compete with a large corpus, be retrieved for varied future language, enter the generator's evidence view, and affect the answer. That mediation chain is directly relevant to any `skill-bench` intervention, memory, source-pack addition, or expert-derived rule.

Its strongest insight is also its sharpest warning. INO uses the serving stack as an index-time test harness, making artifact discoverability measurable before deployment. Yet the same loop can optimize an unauthorized, stale, over-broad, or subtly changed correction. Retrieval success and answer compliance can therefore rise while epistemic quality falls. `skill-bench` must preserve separate evidence states:

```text
feedback event
→ identified corrector and authority scope
→ supported correction proposition
→ approved nugget and semantic-fidelity check
→ indexed representation under a pinned stack
→ eligible future-query population
→ retrieval
→ generator visibility and citation
→ semantic adoption
→ independently correct answer/action
→ downstream consequence and cost
```

The paper observes useful portions of the middle. It does not validate most joins before or after them.

## Research question and claim boundary

The paper asks how an enterprise RAG system can turn actionable factual corrections in noisy post-answer feedback into compact, standalone knowledge-base entries that future semantically related queries can retrieve and use. It compares a plain nugget, trigger-query anchoring, synthetic-query anchoring, combined anchoring, and iterative stack-in-the-loop rewriting (paper §§3–5, pp. 3–5).

The defensible claim is narrow: for selected correction-derived nuggets and query sets inside seven customer-specific frozen corpora, the authors' INO configuration increased the frequency with which the same production stack retrieved and cited those nuggets relative to four less adaptive representations. A small answer-level study reports greater agreement with the supplied correction and no measured increase in two model-judge regression labels.

The paper does **not** establish:

- that feedback authors were authorized, qualified, or correct;
- that the actionability classifier preserves all and only reusable corrections;
- that iterative rewrites preserve the correction's exact meaning and scope;
- that citation causes correct semantic adoption;
- that answers are independently factually correct rather than correction-compliant;
- that the method handles conflicting, superseded, tenant-scoped, or expiring facts;
- population-level recall, specificity, utility, or risk across all eligible production traffic;
- a causal production outcome from deployment;
- portability to a different retriever, generator, customer corpus, language, model, or time;
- privacy, rights, security, or approval validity for user-derived enterprise knowledge; or
- readiness for autonomous correction promotion.

## Methodology

### Production substrate and correction capture

The system serves two B2B settings: free-form support questions and support-ticket transcripts. Each customer has an independent corpus and configuration; corpora have a reported median of about 450,000 documents and range to several million (paper §3.1, p. 3). The retrieval stack uses iterative query generation, hybrid dense/sparse retrieval, top-60 candidates, a proprietary in-domain cross-encoder, and an MLP-calibrated threshold before answer generation (paper §3.3, pp. 3–4).

An OpenAI GPT-5.2 classifier/extractor receives conversation history, question, criticized answer, feedback type, free text, and cited documents. It jointly emits usefulness, a `kb_candidate` decision, rationale, and nugget title/body. On a 5,000-event slice, 42.3% of chat feedback and 21.5% of ticket feedback passed. Two annotators and a third adjudicator labeled a separate 200-event calibration set; the paper reports 96.7% classifier agreement (paper §3.1 and Appendix D, pp. 3, 10).

This is not a correction-authority protocol. “Enough information to write a reusable factual nugget” is a sufficiency label, not factual verification, actor authorization, scope approval, or risk triage. Joint classification/extraction saves cost but removes an independent boundary: an extraction error can influence the same call's actionability judgment, and the paper does not separately measure classifier precision/recall, proposition fidelity, or abstention.

There is also a numerical reporting defect: simple binary agreement on exactly 200 rows can only change in 0.5-point increments. `96.7%` is unattainable without a different denominator, averaging, or unreported weighting. The paper supplies no confusion matrix, class balance, raw counts, or explanation.

### Nugget representation and INO loop

A nugget is an auxiliary customer-corpus document containing a title, one-to-three-sentence body, and optional retrieval anchors. It leaves customer-owned source documents unchanged, which makes insertion atomic and locally reversible (paper §3.2, p. 3). The five variants are:

1. **A — standard:** title/body only;
2. **B — trigger anchor:** add a paraphrase of the original query;
3. **C — synthetic anchors:** add five generated future queries;
4. **D — trigger plus synthetic:** one trigger paraphrase plus four nearby queries;
5. **E — INO:** start from D, index into the frozen customer corpus, run the serving stack on the trigger plus 3–5 generated probe paraphrases, inspect failed retrieval/citation/answer traces, rewrite, re-index, and repeat for at most three iterations (paper §4, pp. 4–5).

The reflector may change title, body, and anchors and sees failed queries, retrieved competitors, and generated answers. It is instructed not to add facts beyond the correction and supplied context (Appendix A, p. 9). There is no deterministic proposition diff, source entailment check, independent human approval, contradiction scan, or pre/post scope review.

The published pseudocode conflicts with the prose. The prose says the candidate is tested against triggering and probe queries and that failures drive revision; Algorithm 1 returns “converged” if the nugget appears in **any** one result, not all required results (paper §4, p. 4; source `main.tex`, algorithm lines 161–166). The authors also report that every nugget passes by iteration three, but do not define whether “pass” follows the permissive pseudocode, all probes, retrieval only, citation, or answer use. This prevents exact reconstruction of the optimization target.

The probe paraphrases are “held-out” only from the anchors embedded in the document. They are repeatedly inspected by INO and therefore are adaptation data for the final nugget, not held-out confirmation. The later 410-query evaluation is the actual external query set.

### Sampling and evaluation populations

The main chat evaluation samples 100 correction-derived nuggets roughly uniformly across seven customers. Every strategy generates a representation for every nugget, inserts it into a frozen corpus, replays queries through the same pinned agent version, and removes it before the next variant. Each variant is run three times because generated anchors vary (paper §5.1, p. 4).

The 410 held-out queries comprise:

- **110 historical queries:** mined from five months of traffic by dense similarity over the original triggering query, then thresholded by a second reranker;
- **300 synthetic queries:** exactly three per trigger, generated by GPT-5.4 using vocabulary first retrieved from the customer corpus and manually spot-checked on an unspecified sample (paper §5.2 and Appendix B, pp. 5, 9).

These are selected semantic neighbors, not a probability sample of future correction-relevant traffic. Historical candidates are selected by model scores from the same trigger, and no human relevance audit, false-negative estimate, duplicate/family clustering, query timestamps relative to the correction, or per-customer count is reported. Some historical queries may precede the correction itself; they demonstrate language variation, not prospective uptake.

A second 160-item correction set uses support-ticket transcripts. It demonstrates a different input format under the same vendor stack, but the paper does not clarify whether customers, correction topics, nugget generation models, or retriever components differ. Calling this “transfer” means package application to another selected internal setting, not transport to unseen companies, corrections, domains, or stacks.

### Outcomes, observers, and aggregation

Three main middle-layer outcomes are reported:

- **retrieval:** nugget passes reranking and reaches the generator;
- **citation:** final answer cites the nugget;
- **answer feedback compliance:** an LLM judge says the answer addresses the original correction.

The answer judge sees original question, original answer, user feedback, extracted nugget, retrieved context, and candidate answer. It labels correction compliance, nugget faithfulness, non-regression, and retrieved-context groundedness (paper §6.3 and Appendix C, pp. 5–6, 9). It does not receive an independent source of truth. “Grounded” means supported by shown retrieved context, so a wrong nugget can be faithfully and groundedly repeated. “Compliance” is anchored to the same feedback transformed into the nugget. These observers establish chain consistency, not factual correctness.

Three in-house annotators label 100 sampled judge decisions; Fleiss' κ reportedly exceeds 0.75 on every axis, and judge-to-majority Cohen's κ exceeds 0.80 after a “small prompt-calibration pass” (paper §6.3, p. 6). The paper does not report exact κ values, label prevalence, sampling frame, condition balance, disagreements, adjudication records, judge model/version, prompt, repeat reliability, or whether the same 100 labels both calibrated and evaluated the prompt. If they did, the agreement is resubstitution rather than held-out judge validation.

The tables report mean ± standard deviation over three generated-representation runs. Query observations are clustered within 100 nuggets, seven customers, shared correction families, and repeated representations; the 300 synthetic queries contribute exactly three siblings per nugget. Standard deviation across only three runs is not uncertainty over nuggets, customers, future queries, or deployments. No paired cluster bootstrap, confidence interval, randomization, customer effect, or multiplicity control is reported. Figure 3 gives McNemar `p ≈ 0.003`, but omits sample size, paired contingency table, run-selection rule, clustering treatment, and multiplicity; it cannot be audited.

## Evidence and results

### Retrieval and citation

On 110 selected historical queries, INO reports 77.3% retrieval and 68.1% citation versus 52.3% and 41.3% for a plain nugget. On 300 synthetic paraphrases, INO reports 93.7% and 86.1% versus 64.1% and 57.3% (Table 1, p. 5). The lower historical values are important evidence that LLM paraphrases are materially easier.

On the 100 original trigger queries, INO reports 97.0% retrieval and 89.1% citation versus 67.6% and 60.2% (Table 2, p. 6). This is in-sample representation fit: the trigger itself helps generate anchors and enters the optimization harness.

On 160 ticket samples, INO reports 78.2% retrieval and 70.4% citation versus 35.1% and 29.7% (Table 3, p. 6). The large contrast supports stack-specific discoverability under harder transcript-shaped inputs, subject to the same selection, clustering, and observer limits.

These monotonic gains are credible evidence that generated anchors and failed-retrieval reflection change retriever preference. The comparison is clean in one useful respect: the serving stack and frozen corpus are held fixed while only the new nugget representation changes. It is not a pure “iteration” ablation, however. INO receives extra stack calls, competitor documents, generated answers, adaptive probes, and up to three rewrites relative to Variant D. No matched non-iterative budget, random rewrite, retrieval-only reflection, citation-only reflection, or human rewrite arm identifies which information or compute causes the gain.

### Answer-level outcomes

The paper reports correction compliance of 73.4% for INO versus 52.2% for the plain nugget; misses due to absent retrieval fall from 40% to 13%. Conditional nugget faithfulness is 81.0% versus 54.1%; major regressions fall from 15.6% to 11.6% and hallucinated-groundedness labels from 19.1% to 14.8% (Figure 3 and §6.3, pp. 5–6).

This supports a mediated claim: more available nuggets coincide with more answers judged to reproduce the correction. It does not identify independent correctness, because feedback, nugget, retrieved evidence, and judge rubric share lineage. Conditional faithfulness is also post-treatment selection: INO and baseline deliver different subsets, so 81.0% versus 54.1% is not an effect among equivalent cases.

### Negative-control traffic

With optimized nuggets indexed, 20 of 1,400 random queries retrieve a nugget and 12 cite one. Manual inspection labels all 20 semantically equivalent to a correction topic, yielding reported 0 false positives (paper §6.2, p. 5).

This is a useful collision audit but not specificity. The paper does not state whether all 100 nuggets were simultaneously indexed, how candidate nugget–query pairs were counted, which condition/run produced them, whether inspectors were blinded, how semantic equivalence was defined, or how many relevant random queries were missed. Twenty selected retrieved cases cannot estimate false-negative rate, broad-topic overreach, or answer harm among the 1,380 unretrieved queries. Zero observed errors gives no evidence about rare high-cost collisions without an uncertainty interval and independent labels.

### Cost and deployment

Variants A–D reportedly cost about `$0.012–$0.0124` and 12.9 seconds per nugget. INO adds about `$0.30` and 98.3 seconds, totaling `$0.31` and 111.2 seconds, with no additional query-time latency after indexing. Variant D reaches 84.8% retrieval / 75.1% citation on the combined held-out chat set at a small fraction of that cost (Appendix E, p. 10).

The paper does not disclose model identities for nugget construction/reflection/judging, token counts, per-step calls, retries, embedding/indexing compute, storage, human review, monitoring, removal, incident, or privacy costs. “Best when budget is acceptable” compares retrieval/citation only; it is not a net-value result. The production claim—hundreds of retrieved nuggets weekly—has no denominator for generated, approved, indexed, retrieved, cited, corrected, complained-about, rolled-back, or expired nuggets, and no downstream support-resolution, user-satisfaction, error, or labor outcome.

## Unique insight

> **Discoverability is a separate optimization target from semantic and epistemic validity, and improving it changes the exposure distribution of any correction errors.**

INO contributes a reusable **index-time realization test**: insert one candidate context object into the actual frozen serving environment; probe relevant language; retain retrieval, competitors, and answer traces; revise locally; and verify again. This is stronger than assuming that writing a memory means it will be available in later work.

But stack-in-the-loop optimization is analogous to training against a grader. It can improve the object the stack prefers without improving the object stakeholders need. The correction pipeline therefore needs two orthogonal gates:

1. **truth/authority gate:** is the proposition supported, correctly scoped, current, approved, and non-conflicting?
2. **realization gate:** does a pinned serving stack retrieve, expose, and correctly use it for eligible queries without collateral effects?

Neither gate can validate the other. A factually perfect nugget may fail retrieval; a highly retrievable nugget may be wrong. The paper mostly validates the second and describes the first as a prompt instruction.

The sanitized example makes the risk concrete. Source feedback says Workspace Owners can reset other users' passwords and Analysts can view but not reset. The final INO text adds that the reset action is **hidden**, an anchor says it is **greyed out**, and the nugget states that the restriction does not apply to self-service reset (Appendix F, pp. 10–11). Those details are not present in the displayed feedback or extracted nugget. They might exist in undisclosed supplied context, but the paper provides no locator or entailment check. The example therefore does not demonstrate the claimed no-new-facts invariant; it demonstrates why every rewritten proposition needs evidence lineage.

A second insight is that auxiliary corrections create a precedence problem. Leaving the customer-owned source untouched makes rollback easy, but now source documents and correction nuggets can disagree. Without authority, valid time, scope, supersession, and conflict-resolution policy, retrieval ranking silently becomes epistemic precedence. The most discoverable text wins, even if it is older, less authoritative, or meant for another product version, role, tenant, or workflow.

## Reproducibility and operational realism

Operational realism is substantial but bounded. The paper uses real negative feedback, customer-specific corpora with hundreds of thousands to millions of documents, proprietary in-domain retrieval, historical traffic, multi-issue support transcripts, deployed agents, index-time latency/cost, and a small collision audit. It acknowledges that real queries are harder than synthetic paraphrases and names one-retriever, English-only, and model-dependence limitations (pp. 5–7).

Inspectability is poor. The source archive contains only manuscript assets; it has no code, prompts verbatim, data, trial rows, retrieval traces, nuggets, query sets, model configuration, human labels, judge outputs, or aggregation scripts. No official empirical release was found. Confidential enterprise data reasonably limits row release, but reproducibility could still include schemas, exact pseudocode, synthetic fixtures, prompt hashes, component manifests, per-nugget aggregate rows, cluster-aware analysis code, proposition diffs, redacted traces, and approval/rollback event formats.

Exact replay additionally requires:

- correction and query eligibility policies;
- customer/nugget/query cluster identities and timestamps;
- exact sampler and selected/excluded counts;
- all model, prompt, embedding, reranker, MLP, threshold, generator, and tool versions;
- the true INO stopping rule;
- insertion/deletion/index-refresh semantics;
- retry, timeout, missing, and invalid trial handling;
- judge model/prompt/calibration split;
- dollar-price basis and token/call ledgers; and
- production promotion, monitoring, expiry, conflict, and rollback policies.

## Limitations and validity threats

1. Feedback actionability is not correction truth, authority, or approval.
2. User roles, qualifications, tenant authority, evidence views, and disagreement are absent.
3. The classifier and extractor are one call, with no separate proposition-fidelity metric.
4. Reported 96.7% agreement is arithmetically incompatible with simple agreement on exactly 200 binary rows.
5. No actionability confusion matrix, class balance, precision/recall, or uncertainty is reported.
6. Selected actionability-positive negative-feedback events condition evaluation on the pipeline's own admission policy.
7. Roughly uniform seven-customer sampling does not identify company, traffic, correction, or topic prevalence.
8. The 110 historical queries are similarity/reranker-selected, not randomly sampled future opportunities.
9. Historical query timestamps relative to correction insertion are unspecified.
10. Synthetic paraphrases use corpus vocabulary and are easier by up to 25 points.
11. Probe queries are adaptation evidence for INO, despite being called held-out from embedded anchors.
12. Pseudocode's `any`-retrieval convergence conflicts with prose and leaves “all pass” undefined.
13. Only three stochastic representation runs are reported.
14. Uncertainty ignores nugget, customer, query-family, and synthetic-sibling clustering.
15. No customer-level outcomes or leave-one-customer-out transport test is reported.
16. “Transfer” to tickets changes input format inside the same vendor stack, not an unseen domain/system test.
17. INO adds adaptive evidence and compute; no budget-matched rewrite ablation isolates iteration/reflection.
18. Retrieval and citation are stack behaviors, not semantic use or factual correctness.
19. Conditional faithfulness compares post-treatment-selected subsets.
20. Judge, correction, nugget, and answer evidence share lineage.
21. Judge calibration may reuse the same 100 labels for prompt tuning and reported agreement.
22. Exact agreement, prevalence, sampling, prompt, model, and adjudication details are absent.
23. McNemar's test omits paired counts, denominator, run choice, cluster handling, and multiplicity.
24. The worked example visibly adds details without disclosed evidence locators.
25. No proposition-level pre/post entailment or scope-preservation audit exists.
26. No contradictory-source, stale-fact, retraction, supersession, expiry, or deletion evaluation exists.
27. Auxiliary nuggets can outrank customer-owned sources without an explicit precedence rule.
28. Independent customer corpora are stated but tenant-isolation/security controls are not evaluated.
29. User feedback rights, consent, purpose limitation, privacy, retention, and affected-party governance are absent.
30. The negative control reviews only retrieved cases and cannot estimate missed relevance or pair-level specificity.
31. Manual collision reviewers, blinding, agreement, and equivalence policy are unspecified.
32. No collateral answer-quality or unrelated-document displacement metric is reported.
33. Cost omits token/call detail, indexing resources, storage, humans, monitoring, failures, and maintenance.
34. Production “hundreds weekly” lacks a complete funnel, outcomes, incidents, expiration, or rollback.
35. No code/data/traces/results release permits recomputation.
36. English-only, one retrieval architecture, proprietary models/components, and mutable enterprise corpora sharply bound transport.

## Transfer to skill-bench

### Retain

1. Treat context insertion as an executable, pinned-environment operation rather than a file-write assumption.
2. Record retrieval, generator availability, citation, semantic adoption, answer/action correctness, and consequence separately.
3. Use real and synthetic query forms but report them separately; real forms are the stronger transport evidence.
4. Preserve competing retrieved documents and failed-answer traces for diagnosis.
5. Keep learned context atomic, versioned, locally reversible, and independently identifiable from source documents.
6. Test random or unrelated traffic for collateral exposure in addition to relevant-query recall.
7. Price the index-time realization loop separately from query-time costs.

### Repair

1. Require correction actor, authority, evidence locator, represented subject/tenant, valid time, product/version scope, confidence, approval, and revocation policy before indexing.
2. Represent the correction as atomic propositions; hash and compare pre/post claims on every rewrite; fail closed on unsupported additions, deletions, widened scope, or changed modality.
3. Separate adaptation probes from untouched temporal/equivalent-form confirmation queries.
4. Pin task/corpus/retriever/reranker/threshold/generator/prompt/tool/index versions and record actual insertion/deletion state.
5. Define convergence over explicit required probe predicates; do not allow an `any`/`all` ambiguity.
6. Cross old/new nugget representation with old/new serving stacks to distinguish artifact fit from stack drift.
7. Add authority/valid-time conflict cases where a more discoverable nugget must defer to or supersede another source.
8. Evaluate collateral retrieval at the nugget–query pair level and inspect answer effect, not only whether any nugget appeared.
9. Use independent correctness observers and affected-user outcomes rather than feedback compliance alone.
10. Cluster analysis by customer, correction, query family, and generated representation; retain all invalid/missing calls in the funnel.
11. Measure the complete production lifecycle: candidate, rejected, approved, indexed, retrieved, cited, adopted, corrected, disputed, expired, superseded, removed, incident, and rollback.

### Claim ladder

A future benchmark should not skip levels:

```text
correction captured
≠ correction authorized or true
≠ nugget semantically faithful
≠ indexed successfully
≠ discoverable on eligible queries
≠ visible to the generator
≠ adopted in the answer/action
≠ independently correct
≠ beneficial or safe in production
≠ transferable or ready
```

## Concrete repository actions

No RAG-specific schema, benchmark family, or pilot is warranted. The evidence maps into existing participation/authority, source provenance, context lifecycle, compounding lesson, configured-system, trace, task-health, metric-monitoring, resource, and validity machinery.

At the next consolidation or fixture exercise, apply three general checks:

1. **Correction-to-context promotion:** reject any context object lacking typed authority, proposition evidence, scope/valid time, approval, contradiction handling, and revocation.
2. **Semantic-delta gate:** reject iterative representation changes when any proposition lacks a source locator or when scope/modal/time semantics drift, even if retrieval improves.
3. **Realization-to-correctness boundary:** require untouched query forms and an independent correctness observer before promoting retrieval/citation/compliance gains into expertise, quality, production-utility, or readiness claims.

These requirements overlap current machinery and the completed OpenAI/Thrive Tax AI review, so no duplicate queue task is added.

## Comparison with adjacent evidence

- **OpenAI/Thrive Tax AI:** both cases start with in-workflow corrections. Tax AI's strongest pattern is attribution before correction promotion: a difference can be product error, unsupported behavior, judgment/preference, downstream change, grader defect, or noise. INO instead gates on enough free text to write a fact, then optimizes representation. INO adds a concrete correction→index→retrieval→citation realization test and quantitative selected-query contrasts; Tax AI adds the stronger cause/authority review and targeted/regression engineering loop. Combined: perform attribution and approval first, realization optimization second, untouched correctness/consequence validation third.
- **Agentic Context Engineering (ACE):** ACE shows that bounded delta transactions preserve context better than whole rewrites, but its lessons need provenance, contradiction, held-out promotion, and rollback. INO supplies a production corpus realization test for one atomic object, yet allows the model to rewrite title/body/anchors without proposition lineage. Both demonstrate that optimization against the downstream harness is useful and dangerous: same-loop score gains cannot certify lesson truth.
- **ClawArena / MemSyco-Bench:** those reviews separate static conflict, temporal supersession, valid scope, stronger evidence, and legitimate personalization. INO has no corresponding authority or valid-time model. An auxiliary nugget should not win because it is easier to retrieve; its decision role must be explicit.
- **Bridge Evidence / LongMemEval-V2:** retrieval and availability do not establish adoption or causal use. INO's citation and correction-compliance layers move further than recall-only evaluation, but no nugget removal/substitution or independent correctness test identifies semantic dependence and benefit.
- **Who Grades the Grader?:** optimizing a context object against the serving stack resembles co-evolving an intervention and evaluator. Preserve untouched external forms and frozen observers so stack affinity is not mistaken for general correction quality.

## Bottom line

INO isolates an important and often ignored systems problem: a correct-looking lesson can be operationally useless if the deployed stack cannot find it. On selected real and synthetic query forms in seven proprietary customer corpora, adaptive title/body/anchor rewriting produces large, monotonic retrieval and citation gains, with a small same-lineage answer-judge study suggesting better correction compliance. The production substrate, frozen-stack comparison, real-query split, collision audit, and offline cost report make this more operationally informative than a generic memory benchmark.

The paper's validity boundary stops before its strongest practical risk. It does not establish that the original correction is authorized or true, that rewrites preserve semantics, that competing sources are resolved correctly, that retrieved nuggets cause independently correct answers, or that hundreds of weekly production nuggets improve outcomes safely. The worked example itself adds undisclosed propositions, the actionability agreement is numerically irreconcilable as stated, and the algorithm's permissive stopping rule conflicts with the prose. `skill-bench` should retain the **index-time realization test**, but only downstream of a correction-authority and semantic-delta gate and upstream of untouched correctness and consequence evaluation.