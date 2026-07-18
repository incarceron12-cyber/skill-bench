# RAID: one correction can nominate a propagation rule, but approval and lexical coverage do not establish expertise transfer

## Source, review status, and charter fit

**Deep review of the complete immutable primary source, appendices, prompt, and official arXiv source package, plus a time-bounded official-page/release audit.** I read the full nine-page paper and its 533-line layout-preserving extraction; inspected all 18 source-package members, including the complete TeX, prompt, figures and bibliography inventory; and checked the author-linked demo and official CAIS page evidence preserved in the release provenance.

- **Paper:** Jiajing Guo, Xueming Li, Jorge Piazentin Ono, Wenbin He, and Liu Ren, *Scaling Expert Feedback with Reflective Edit Propagation in Compositional Knowledge Bases*, arXiv:2606.05023v1 (3 June 2026), DOI `10.1145/3786335.3813201`, <https://arxiv.org/abs/2606.05023v1>
- **Local PDF:** `data/papers/pdfs/2606.05023v1-scaling-expert-feedback-reflective-edit-propagation.pdf` (9 pages; 2,473,944 bytes; SHA-256 `3a134b5386d3ebb3e5f80940f6983a2d81daa4533345afd393e130befca1eece`)
- **Full local text:** `data/papers/text/2606.05023v1-scaling-expert-feedback-reflective-edit-propagation.txt` (56,110 characters; SHA-256 `c1c273fbdcdcb4a1f3d588f3a4a1ebbba533119ed0bffd1b98a85b3ec0f07cd5`)
- **Official source archive:** `data/papers/source/2606.05023v1-source.tar.gz` (SHA-256 `ed3b482c9b998046c37661f002c82808050937c6c3fbdfd863b3f05a140eea34`), extracted under `data/papers/source/2606.05023v1/`
- **Release/page audit:** `data/sources/releases/2606.05023v1-raid-reflective-edit-propagation/provenance.json`
- **Evidence boundary:** the official CAIS page exposes the paper, while the author-linked Notion URL yielded only a dynamic shell to static extraction. A time-bounded search found no author-verifiable code, frozen RxTerms benchmark, model outputs, result ledger, proprietary KB, or user-study records. The public RxTerms resource is upstream data, not the evaluated benchmark snapshot.

This advances charter objectives A, B, C, E, and F through a general question: how should a benchmark represent the transformation of one observed expert correction into candidate consequences elsewhere? The identifier dictionary is a bounded mechanism case, not a proposal to narrow `skill-bench` to pharmaceuticals, semiconductors, or knowledge bases.

## One-sentence contribution

RAID contributes a useful mediated workflow—compare one before/after edit, infer a symbol-level rule, retrieve structurally related entries, generate candidate revisions, and require staged human approval—but its public experiment tests synthetic, model-authored perturbation reversal without baselines or released rows, and its four-person proprietary study reports perceptions rather than proposal dispositions, executed deltas, independent correctness, burden, or utility; the evidence supports a configured propagation prototype, not source-faithful latent-intent capture or scalable expertise transfer.

## Why this matters

A correction is not merely a better final string. It may imply a reusable rule, reveal a hidden decomposition, alter the eligible scope of related records, and create collateral risk when generalized. RAID makes that intermediate transformation inspectable rather than silently treating an edit as local or immediately committing a model-generated generalization. Its staged interface also correctly treats propagation as a proposal under human control.

The decisive validity insight is that **the observed edit and every propagated consequence have different evidentiary status**:

```text
observed before/after edit
→ identified editor and authority for the edited record
→ candidate interpretation of why it changed
→ candidate symbol/rule and applicability conditions
→ eligible related-record set
→ proposed changes and predicted collateral effects
→ human disposition for each proposal and scope
→ actually executed, versioned KB delta
→ independent correctness and collateral-integrity observations
→ downstream use, consequence, burden, and rollback
```

RAID implements UI and model operations around the middle of this chain. The public benchmark supplies synthetic labels for intent class, related-record membership, and generated-description resemblance. The user study supplies a walkthrough, at least eight corrections, three small survey responses per participant, and qualitative reactions. Neither study closes the full chain. That distinction prevents a coherent batch edit, an approving click, or high retrieval recall from being mislabeled as transferred expertise.

## Research question and claim boundary

The paper asks: “How can we efficiently utilize limited human feedback to maintain a massive compositional knowledge base?” (Introduction, p. 1). Its motivating premise is that experts naturally correct assembled identifier descriptions while the correction often belongs to a reusable underlying symbol; a system must reason backward to the symbol and forward to all affected identifiers (pp. 1–2).

The defensible claim is narrow: under one GPT-5-mini/LangChain prototype, synthetic RxTerms correction pairs were usually assigned the authored error class and their structurally linked identifiers were retrieved with high reported recall; four semiconductor-test analysts could operate a proprietary-data prototype after a walkthrough and expressed moderately positive intent-capture perceptions while identifying missing controls and review burden.

The paper does **not** establish:

- recovery of naturally occurring or tacit expert intent from an edit;
- editor identity, authority, evidence, rationale, scope, exceptions, valid time, or disagreement;
- superiority to deterministic symbol joins, exact matching, a non-reflective rule, another prompt/model, or manual batch tooling;
- independent pharmaceutical correctness of generated references, perturbations, or revisions;
- actual accept/reject/edit frequencies, executed KB changes, correctness, collateral preservation, or rollback in the proprietary study;
- reduced expert time or total correction burden relative to entry-by-entry review;
- professional utility, economic value, production reliability, privacy fitness, cross-expert transfer, cross-structure transport, or readiness.

## Methodology

### System and information flow

The frontend is React; Django/PostgreSQL supply the backend; LangChain and GPT-5-mini perform reflection and planning (System §2.3, p. 3). The reflection prompt receives the target identifier, description source, metadata, status, `Human Validated` flag, update time, connected symbols and relationships, plus the original and corrected descriptions (Appendix A.3, pp. 8–9). It then must:

1. identify the textual/pharmacological difference;
2. attribute it to a connected symbol;
3. classify semantic impact; and
4. emit `update_description`, `filter`, and `batch_llm_revise_description` actions in that fixed order.

The system's three conceptual stages are:

1. **Intent Inference:** classify semantic-confusion, granularity, or surface edits and infer the symbol-level update using formative-study examples in the prompt (System §2.1, p. 2).
2. **Reflection-based Planning:** create JSON parameters for symbol update, natural-language search translated into SQL, and batch description generation (Table 1, pp. 2–3).
3. **User Controlled Execution:** expose cards sequentially; the expert approves or modifies the symbol update, search query, and proposed revisions before commit (System §2.2, p. 3).

This architecture is more accurately a **forced typed plan with human checkpoints** than evidence that the model reproduces a human cognitive process. The prompt supplies the current decomposition and connected symbols, strongly constrains the expected attribution and operation order, and says even a surface rephrase must propose all steps while setting `suggest_propagation=false` (Appendix A.3, p. 9). The paper does not release format instructions, few-shot examples, generated SQL, generation prompt, model parameters, retries, or commit semantics.

It also contains an interface contradiction. The demo says users can “accept, reject, or edit individual entries” in the propagation preview (p. 3), while the user-study findings say the current interface permits search-scope adjustment but **not** direct editing of individual revisions (p. 5). This matters because editable proposal disposition is a claimed contribution and the strongest human-control boundary.

### Formative study

Six semiconductor SMEs audited LLM-generated entries: two individual interviews and a four-person focus-group workshop (Appendix A.2, p. 7). The authors derive three findings: corrections often concern an underlying symbol, assembled descriptions fit experts' diagnostic workflow better than symbol metadata, and experts welcome propagation but fear over-propagation. Those findings motivate final authority, exposed reasoning, and flexible intervention.

No recruitment frame, experience distribution, session length, task count, observation/coding procedure, quotations, disagreement, saturation argument, raw edit taxonomy, or ethics/consent/privacy detail is reported. Focus-group dependence and concept priming are not handled. The three edit classes are therefore useful design hypotheses, not validated exhaustive categories or prevalence estimates.

### Public RxTerms benchmark

The benchmark begins with RxTerms ingredient, dose-form, and route symbols. A rule/Gemini-2.5-flash name-informativeness filter removes every symbol scoring at least 2/10—84% of the pool—and retains 457 opaque ingredient names (Quantitative Evaluation, pp. 3–4). This makes the evaluation deliberately ingredient-only; it does not test the paper's broader claim that analogous related ingredients or dose forms may require reasoning beyond a literal join.

The 457 symbols are deterministically split by error type, then 80 per type are stratified by linked-identifier count: low 1–3, medium 4–10, high 11+ (Appendix B.1, p. 7). GPT-5-mini writes reference descriptions and Gemini-2.5-flash creates:

- 80 semantic confusions using model-generated variation groups;
- 80 vague granularity errors; and
- 80 cosmetic surface edits.

The perturbed-to-reference pair is passed to RAID as a simulated expert edit. For the 160 propagation-positive cases, the symbol-to-identifier mapping defines the “ground-truth” affected set. Metrics are intent classification accuracy; propagation precision/recall/F1; apply/skip revision accuracy; and cosine similarity to the GPT-5-mini reference (pp. 3–4).

This benchmark tests **recovery of its own generation template**, not naturally latent intent. The evaluator provides the corrected reference text directly, the target symbol appears among connected symbols, the prompt enumerates expected pharmacological difference types, and the intended related-record set is an existing structural join. Separating author and perturbation model families avoids one narrow same-model circularity, but does not create expert ground truth or independent clinical validation. No baseline is reported—not even exact symbol matching, a direct SQL join, deterministic string/token matching, prompt-only classification, no-reflection revision, or alternate model.

### Proprietary user study

Four SMEs, each with more than three years of semiconductor test-analysis experience, receive a ten-minute algorithm walkthrough, perform at least two corrections on a proprietary KB while thinking aloud, answer two UMUX-Lite questions and one intent-quality question, then complete a semi-structured interview (User Study, p. 5).

The paper reports mean UMUX-Lite `3.75` and intent quality `4/5`, plus themes: experts wanted second-order propagation to variants such as `GLS2/GLS3`, semantic rather than only syntactic links, editable individual revisions, clearer scope visualization, and relief from entry-by-entry review. These are valuable design findings because they expose exactly where a structural symbol join is too narrow and human verification remains costly.

But study evidence is too sparse to support efficacy. “At least two” leaves the exact correction and propagation denominators unknown. The UMUX-Lite response scale, transformation, item-level values, missingness, and uncertainty are absent. There is no task baseline, time, number of proposals, affected entries, accepted/rejected/edited counts, false-proposal adjudication, executed delta, rollback, independent expert review, inter-expert disagreement, or downstream use. The ten-minute explanation also primes participants with the intended mechanism before asking whether intent inference was good.

## Evidence and results

### Reported public results

Table 2 reports:

- intent accuracy: 98.8% semantic confusion, 100% granularity/surface, 99.6% overall;
- propagation precision: 97.6%, 98.3%, and 100%; recall 100% for all; overall F1 99.3%;
- revision accuracy: 93.9%, 87.9%, 49.7%, and 76.3% overall;
- cosine similarity: 88.6%, 88.4%, 90.3%, and 89.1% overall.

The intent numbers are consistent with 79/80 semantic cases and 239/240 overall. The error analysis says one semantic edit was misclassified, leaving 159 retrieval executions; 153 had no retrieval false positives. Six caused 139 false-positive identifiers through substring collisions, of which 115 became false revisions (pp. 4 and 7–8). This is the paper's strongest evidence: one local lexical overreach can amplify into many collateral writes, and the generative revision layer intercepted only one affected edit family.

### Unresolved denominator and ledger defects

The compact paper leaves several results non-auditable or internally inconsistent:

1. **Surface propagation metrics are undefined as presented.** All 80 surface edits are declared no-propagation cases, yet Table 2 gives 100% precision, recall, and F1 while revision accuracy is 49.7%. Standard set recall over an empty required set is undefined unless a special convention is declared. The prompt still forces a full plan, but the paper does not say which steps execute, what counts as retrieval, or which denominator yields the revision score.
2. **The 2,744 denominator changes meaning.** Appendix B.1 says 160 propagation-positive sampled symbols affect 2,744 identifiers. The main error analysis says the **159 actually executed** edits cover 2,744 identifiers after one edit was skipped. Unless the skipped symbol affected zero identifiers—impossible under the sampled 1+ propagation bins—the same total cannot describe both sets.
3. **False applications exceed retrieval false positives in one row.** Table 3 gives 28 false-positive identifiers for `dextroamphetamine → lisdexamfetamine`; Table 4 gives 29 false applies for that same pair. Under the stated one apply/skip decision per retrieved identifier, a downstream false-apply count cannot exceed its upstream false-positive candidate count.
4. **Overall revision aggregation is unspecified.** The unweighted mean of the three displayed class rates is 77.17%, not 76.3%. A micro-average may differ because candidate counts differ, but no class denominator or aggregation code is supplied.
5. **No uncertainty or repetition exists.** Results are one configured model execution over clustered identifiers nested under 240 symbols and model-generated variation groups. There are no repeated model calls, intervals, cluster-aware analyses, prompt/model sensitivity tests, invalid-call counts, or missingness rules.

These defects do not erase the observed collision pattern, but they prevent exact recomputation and make the headline near-perfect propagation table unsuitable as a calibrated reliability estimate.

## Unique insight

> **Propagation is a multiplicative authority operation: one uncertain interpretation can create many candidate obligations, so human control must attach not only to the originating edit but to scope, each proposed consequence, and the executed delta.**

RAID's most transferable contribution is not “reflection.” It is the explicit **edit-to-consequence fan-out boundary**. A local edit has one observed truth: this actor changed this record from A to B. Everything else—why, which symbol changed, whether sibling records share the same conditions, whether an alternative wording is valid, and whether every proposed rewrite preserves unrelated content—is an inference with its own authority and uncertainty.

The RxTerms failure demonstrates why average precision is inadequate. Only six of 159 retrieval events produce all 139 false candidates, and five produce 115 false revisions. Risk is concentrated by propagation family and fan-out. A benchmark should therefore report per-edit collateral count and severity, maximum/fan-out-tail risk, and approval burden—not only pooled identifier precision. In consequential domains, one broad high-fan-out interpretation can dominate expected loss despite excellent micro-averaged scores.

The user study sharpens the same point from the other direction. Experts ask for semantic connections beyond the existing graph, but expanding relation types also enlarges the review surface and uncertainty. Better recall and lower burden are competing objectives, not jointly implied by “scaling” one edit.

## Reproducibility and operational realism

Operational realism is mixed. Positives include a real enterprise curation problem, a compositional data structure, explicit human checkpoints, proprietary-domain use, observed scope anxiety, concentrated collateral failures, and acknowledgement that reviewing correct proposals is still time-consuming. The public benchmark gives exact high-level sampling strata and a complete reflection prompt.

Inspectability is poor. There is no frozen RxTerms snapshot, retained-symbol list, random seed, informativeness scores, variation groups, reference descriptions, perturbations, per-edit connected sets, prompt examples, format schema, SQL outputs, proposed revisions, apply/skip decisions, embeddings, model snapshots, trial rows, or aggregation code. The proprietary setting lacks participant records, tasks, source/edit/proposal/disposition/execution ledgers, survey instrument/responses, transcripts, coding, timing, correctness labels, and privacy/consent details. The source archive reproduces the manuscript rather than the empirical system.

Exact replay would require pinned datasets and components; complete candidate/exclusion ledgers; prompt/model/tool/database versions; transaction and rollback semantics; per-stage intended/attempted/valid/invalid records; independent correctness observers; clustered repeats; and a full human-review funnel. The official page audit found no author-verifiable empirical release at review time, which is a time-bounded observation rather than proof of permanent nonrelease.

## Limitations and validity threats

1. The motivating tens-of-thousands scale has no reported production corpus size, traffic, or correction prevalence.
2. The six-person formative study lacks recruitment, tasks, duration, protocol, coding, disagreement, and saturation evidence.
3. Few-shot examples come from the same formative setting; example content and overlap are unreleased.
4. Three edit classes are treated as exhaustive without validation or naturally occurring prevalence.
5. The prompt supplies connected symbols and strongly cues the expected attribution and error taxonomy.
6. Surface edits must still emit a full three-step plan, blurring classification, planning, and execution.
7. Prompt format instructions, examples, generation prompt, SQL translation, and apply/skip prompt are absent.
8. Model snapshots, parameters, retries, invalid outputs, latency, tokens, and dollar cost are absent.
9. The public filter removes 84% of symbols and every route/dose form, sharply narrowing construct coverage.
10. Gemini participates in filtering, variation grouping, and perturbation without validation.
11. GPT-5-mini reference descriptions are not expert or source ground truth.
12. Giving the corrected reference text converts latent-intent recovery into template classification/attribution.
13. Structural symbol membership defines relevance, excluding semantic variants the user study says matter.
14. No deterministic, non-reflective, alternate-model, manual, or budget-matched baseline exists.
15. The same configured system appears to be evaluated once per case.
16. Symbol, identifier, variation-family, and propagation-count dependence is ignored.
17. Surface precision/recall/F1 lack a declared empty-set convention.
18. The 2,744 affected-identifier total is assigned to incompatible 160-edit and 159-edit sets.
19. One false-apply row exceeds its upstream false-positive count.
20. Overall revision aggregation and class denominators are absent.
21. Cosine similarity to model-authored text does not establish factual or professional equivalence.
22. Apply/skip agreement does not evaluate whether applied text preserves all intended and collateral facts.
23. No alternative-valid revision policy or abstention/ambiguity label is represented.
24. Per-edit fan-out severity is hidden by pooled precision/F1.
25. Four user-study participants and at least eight edits are too sparse for reliability or scaling claims.
26. Participant selection, role authority, relationship to the KB, and edit rights are under-specified.
27. The walkthrough primes the intended mechanism before ratings and think-aloud behavior.
28. UMUX-Lite scale/scoring, responses, missingness, and uncertainty are absent.
29. Intent quality is perception, not source-faithful or independent correctness evidence.
30. Proposal, disposition, repair, execution, rollback, and correctness counts are absent.
31. The paper contradicts itself on whether individual proposed revisions are editable.
32. Human time, review effort, interruption, cognitive load, and baseline burden are unmeasured.
33. No independent reviewer tests approval quality or automation bias.
34. Inter-expert disagreement, scope exceptions, and conflicting corrections are untested.
35. Provenance, valid time, supersession, access control, privacy, and affected-party rights are not evaluated.
36. No downstream retrieval/use, artifact quality, incident, or organizational outcome is measured.
37. Generalization from short compositional identifiers to semantic graphs or hierarchical documents is proposed only.
38. Cross-session heuristic accumulation and cross-expert transfer are future work, not evidence.
39. No code/data/result release permits recomputation or system audit.
40. The evidence does not establish professional utility, economic value, production fitness, or readiness.

## Transfer to skill-bench

### Retain

- Treat an observed professional edit as a **candidate critical incident**, not a self-interpreting rule.
- Preserve the before/after record and then version intent interpretation, candidate scope, plan, proposal, disposition, execution, and verification separately.
- Use staged scope preview and fail-closed human approval before high-fan-out mutations.
- Keep no-propagation/surface cases as first-class negative controls.
- Report retrieval false positives and downstream false revisions as distinct stages.
- Analyze risk per originating edit and fan-out tail, not only pooled descendant precision.
- Let experts modify scope before execution and record those modifications as evidence about missing relationships or exceptions.

### Repair

- Bind each correction to editor identity, role, authority scope, source/evidence locator, rationale status (`stated`, `inferred`, `disputed`), valid time, exceptions, and revocation.
- Represent each candidate relation as syntactic, structural, semantic, temporal, causal, or organizational, with evidence and applicability rather than one undifferentiated search set.
- Require per-proposal dispositions (`accept`, `reject`, `edit`, `abstain`, `escalate`) and preserve who decided, what they saw, and why.
- Record actual transactional writes, pre/post hashes, partial failures, rollback, and unrelated-field integrity.
- Use plural checks: source entailment, scope eligibility, independent correctness, alternative validity, collateral preservation, and downstream consequence.
- Report the full funnel by correction family: eligible, proposed, previewed, accepted, edited, rejected, executed, independently correct, collateral defect, rolled back, and later used.
- Compare against deterministic graph joins, exact matching, no-reflection prompting, and human batch editing under matched information and resource envelopes.
- Measure reviewer time and decision loss jointly with coverage; do not call a method scalable because one edit fans out computationally.

### High-value falsification slice

A cross-domain fixture should instantiate one edit in each of two materially different artifact structures—for example, a structured identifier dictionary and a spreadsheet/model dependency graph—then plant:

1. a literal structural sibling that should update;
2. a substring collision that must not update;
3. a semantic sibling absent from the current graph;
4. a scoped exception sharing the symbol but not the applicability conditions;
5. an alternative-valid wording;
6. an unrelated field vulnerable to collateral rewrite; and
7. a superseded or lower-authority correction.

Run deterministic join, direct model plan, and staged expert-controlled plan conditions with frozen source views. Preserve every inference and disposition, then independently adjudicate correctness and collateral state. Primary estimands should include per-originating-edit false descendants, severe-collateral probability, eligible-scope recall, accepted-edit correctness, review minutes, rollback rate, and downstream task consequence. This tests the general edit-to-consequence hypothesis without turning a KB demo into the benchmark's scope.

## Concrete repository actions

- **No new queue task.** RAID's requirements fit existing expertise-transfer, expert-participation/authority, source provenance, compounding-lesson, artifact/state observation, trace, task-health, metric-monitoring, and validity-argument machinery. A KB-specific schema would duplicate those homes.
- At the next consolidation, add **originating-edit fan-out risk** to correction-promotion guidance: retain per-root descendant counts/severity and prohibit pooled precision from masking concentrated collateral failures.
- At the next cross-domain fixture exercise, use the seven-case falsification slice above to test whether current records can represent inferred rationale, scope exceptions, per-proposal disposition, transaction outcome, and independent collateral checks.

## Comparison with adjacent evidence

- **Context-Mediated Domain Adaptation:** that review separates observed artifact delta from model-generated interpretation and authorized context. RAID adds forward fan-out into candidate related records and staged approval, but still lacks source-author-confirmed rationale and independent consequence evidence.
- **SciDiagramEdit:** revision pairs can become executable tasks and rules, yet raw delta, authored intent, transformed substrate, promoted procedure, and recipient consequence remain distinct. RAID's connected-symbol graph makes candidate scope more explicit, while its synthetic correction pairs are less natural and its artifact integrity checks weaker.
- **Factual Nugget Optimization:** INO tests whether a correction-derived object becomes discoverable and cited in a pinned serving stack. RAID instead tests cross-record candidate propagation. Both need authority and semantic-delta gates before optimizing realization, plus independent correctness and collateral checks afterward.
- **GrowLoop:** generated failures can request criterion evolution, but adaptive fitting and model-order-conditioned admission can silently change the construct. RAID similarly must not promote rejected/edited propagation patterns into cross-expert heuristics without typed authority, frozen bridges, contradiction handling, and untouched transport tests.
- **OpenAI/Thrive Tax AI:** production corrections first require attribution—product defect, unsupported behavior, judgment, downstream change, grader defect, or noise—before task/rule promotion. RAID starts after that missing attribution boundary. Combine attribution first, proposal fan-out second, independent verification and scoped promotion third.

## Bottom line

RAID identifies a real missing operation in expertise-to-evaluation pipelines: an expert's local correction may imply consequences in many related artifacts, and those consequences should be made inspectable before execution. Its staged UI, forced plan structure, public synthetic benchmark, and frank collision analysis provide a useful prototype and a concrete warning: six retrieval mistakes can cascade into 115 false revisions.

The evidence does not support the stronger “scale specialized expertise” interpretation. The public task reverses model-authored perturbations with the corrected text and graph neighborhood supplied, omits every baseline and uncertainty estimate, and contains unresolved denominator/ledger contradictions. The proprietary study has four participants, unknown exact task and proposal counts, perception-only aggregate ratings, no disposition/execution/correctness ledger, and no measured time savings. `skill-bench` should retain the **edit-to-consequence fan-out record and staged approval boundary**, while requiring authority, applicability, per-proposal disposition, executed state, independent correctness/collateral checks, burden, downstream consequence, and cross-domain transport before claiming expertise transfer or scale.