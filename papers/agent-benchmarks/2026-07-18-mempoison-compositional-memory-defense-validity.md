# MemPoison exposes non-local memory risk, but its interaction statistic and utility control do not validate the claimed defense mechanism

## Source, release, and review status

**Deep review of the complete immutable primary source and pinned dataset.** I read the full 30-page arXiv v1 paper and appendices, inspected the complete 29-file arXiv source package, parsed all 1,227 released dataset rows, and audited their nested family, injection, trigger, and target structure. The source package contains the manuscript and figures but no code, run configuration, result rows, materialized-memory traces, judge outputs, calibration split, or validation ledger.

- **Paper:** Jifeng Gao et al., *MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents*, arXiv:2607.14651v1 (16 July 2026), <https://arxiv.org/abs/2607.14651v1>.
- **Local PDF:** `data/papers/pdfs/2607.14651v1-mempoison.pdf` (30 pages; SHA-256 `ef390305b0d699d410bfbb6250b8e0af5bb2ba3859bc2b79d1e971bc5856bb53`).
- **Full text read:** `data/papers/text/2607.14651v1-mempoison.txt` (SHA-256 `7ddf2f974fa681eae07b15d069172efa0a09fab6e5b9e0c35964b5e578df8235`).
- **Official arXiv source:** `data/papers/source/2607.14651v1-source.tar.gz` (SHA-256 `3df5800a81f73264a5dac849881ddf012a9f5a7a3e5e7bd01a198a6108da230c`), extracted at `data/papers/source/2607.14651v1/`.
- **Pinned public dataset:** Hugging Face revision `12d0821a9a304d50485cf08ecf27ec874f98f836`, <https://huggingface.co/datasets/MemPoison/MemPoison/tree/12d0821a9a304d50485cf08ecf27ec874f98f836>.
- **Local dataset:** `data/sources/releases/2607.14651v1-mempoison/huggingface/MemPoison_full1227.json` (SHA-256 `59f78395d2e1628dd6f79bbec8854ed864ad0cda8fa2dd60c5f2cd3c0b5b403c`).
- **Provenance and deterministic inventory:** `data/sources/releases/2607.14651v1-mempoison/provenance.json`; `data/sources/releases/2607.14651v1-mempoison/dataset-audit.json`.

The pinned dataset revision was created on 6 May, 70 days before arXiv v1. Its three-file release has a metadata-only 12-line card, no paper link, and no scripts, results, split manifest, validation decisions, or version statement binding these bytes to the evaluated corpus. Its CC-BY-4.0 declaration makes the rows inspectable and reusable, but paper-time byte identity is not established.

## Relevance, charter fit, and decision filter

This review advances charter objectives A, B, and D by testing a general knowledge-work question: **when can multiple individually admissible records jointly create an unauthorized downstream decision, and what observations distinguish that from retrieval coincidence, target imitation, or a synthetic oracle?** Persistent memory is a methodological case for evidence provenance, authority, longitudinal state, causal diagnosis, and safety—not a proposal to narrow `skill-bench` to security or conversational memory.

The concrete evidence is a paper/source/release audit and a claim-bounded admission-to-consequence chain. Useful completion means retaining the L1/L2/L3 stress-test idea while refusing to promote authored target matches, a mis-signed interaction diagnostic, or clean-context accuracy into compositional mechanism, realized harm, benign-write utility, or deployment claims.

## One-sentence contribution and assessment

MemPoison's genuine contribution is a released, structured family of direct, multi-record, and trigger-conditioned persistent-memory challenges evaluated across three materialization abstractions; however, its final text target is co-authored with the poison, its positive L2 interaction statistic mathematically indicates overlap rather than synergy, its L3 normal-context counterfactual is absent from the release, and its clean-accuracy control does not test benign untrusted writes—so v1 supports configured response sensitivity to authored memory contexts, not the claimed structural defense mechanism or safe-use frontier.

## Research question and intended construct

The paper asks how persistent poisoning changes as harmful content moves farther from what a write-time filter can observe. It defines (paper §§3–4, pp. 3–5):

1. **L1 direct corruption:** one record explicitly replaces a fact, preference, instruction, or state;
2. **L2 compositional corruption:** two to four locally plausible writes jointly imply the poisoned target;
3. **L3 dormant corruption:** one conditional write is intended to matter only after a later natural trigger.

The attacker writes through user input, tool output, or cross-agent messages but cannot alter model weights, system prompts, or the database directly. The injection and trigger turns are temporally separated. Each released case contains clean context, candidate writes, three later text prompts, and paired clean/poisoned target strings. It is then materialized as flat chunks, sentence-like facts, or hierarchical raw records/notes/summaries.

That construct is narrower than the title can suggest. The benchmark measures whether a short response resembles an authored target after a simulated memory pipeline. It does not execute the endpoint, command, communication, file mutation, or workflow state named by that response. “Behavioral corruption” is therefore **target-aligned response behavior**, not realized action, affected-party harm, or persistent compromise of a deployed agent.

## Methodology and released instrument

### Family-first construction

The paper reports 100 semantic units from five workflow clusters × four attack types × five scenarios, crossed with three levels and three channels to create 900 prototypes. Surface expansion yields 12,760 candidates; automatic validity filtering leaves 8,139; deduplication/executability filtering leaves 5,924; stratified selection leaves 2,575; and human review plus repair leaves 1,227 (Appendix A.1, pp. 13–16).

The final distribution is exactly reproduced by the pinned JSON:

- difficulty: 353 L1, 253 L2, 621 L3;
- channel: 481 user, 513 tool, 233 cross-agent;
- target: 277 fact, 132 instruction, 661 preference, 157 state;
- domain: 240 coding/terminal, 221 desktop, 307 enterprise, 279 tool/API, 180 web;
- 1,633 injection turns and 3,681 trigger tasks; every case has exactly three trigger tasks;
- L2 uses 108 two-turn, 137 three-turn, and eight four-turn injections; L1/L3 each use one turn.

The release also reveals dependence that headline row counts hide. It has 373 nonempty `seed_family_id` values (maximum 18 rows per ID) and 346 nonempty `family_id` values (maximum 12); 1,110 of 1,227 rows belong to repeated seed IDs. Every released seed ID is confined to one difficulty and one channel, so it does not expose the claimed shared semantic unit across the full level × channel crossing. `family_id` and `multidomain` are absent from 135 rows despite the paper's versioned traceability claim. There is no split or exposure role.

The final triggers and targets are highly templated. Across 3,681 trigger rows there are only 1,871 unique prompts, 154 unique clean targets, and 169 unique poisoned targets; 3,669 trigger rows reuse a clean target and 3,664 reuse a poisoned target. This is legitimate controlled variation, but cases and three within-case prompts are not independent evidence. Inference should cluster at least by semantic source/target family and case, not use trigger rows or surface variants as exchangeable samples.

### Human validation and source authority

The review criteria—realism, writability, non-leaky triggers, target separability, harmfulness, and taxonomy correctness—are appropriate. The paper reports 1,007 rejects and 726 `major_fix` decisions among 2,575 reviewed candidates, with repaired cases included after conservative rewriting (Appendix A.1, pp. 15–16).

But “hand-validated” has no auditable validation lineage. The paper does not identify:

- the number, qualifications, independence, or domain coverage of reviewers;
- whether candidates were double-coded or adjudicated;
- instructions, item-level decisions, agreement, or disagreement reasons;
- provenance, consent, or license for the “real human interaction” seeds;
- which 726 repairs passed, who re-reviewed them, or whether repair changed attack success;
- professional or affected-party authority for the clean target, poisoned harm, severity, or recoverability.

The public `tier=gold_seed` value on all 1,227 rows is a release label, not evidence of independent gold truth. The same authoring process supplies context, poison, trigger, clean target, poisoned target, and harmfulness judgment.

### Configured evaluation

The paper reports ten model families, three substrates, no defense plus eleven named defense rows, paired clean/poisoned conditions, three triggers per case, and five repeats (paper §5 and Appendix B, pp. 6–8, 17–29). Retrieval uses fixed token-overlap ranking with `k=3`. Flat chunks retain turns; fact stores split sentence-like records; hierarchical notes add derived notes and episode summaries.

Several components are not reproducible from v1:

- exact model snapshots, provider dates, decoding parameters, random seeds, and repeat independence;
- the fact splitter, note/summarization implementation, materialized record IDs, and substrate prompts;
- complete defense code, calibration rows, held-out clean split, and threshold-selection records;
- run attempts, invalids, retries, failures, raw outputs, scores, memory states, retrieved slates, and aggregation code.

The source package contains plotted figures rather than underlying result tables. The paper reports approximately 141.54M GPT-4o, 329.61M GPT-5, 163.71M Gemini, and 762.24M DeepSeek-V3 tokens, three A100-days for benchmark/defense evaluation, and eleven A100-days for MID (Appendix B.9, p. 27), but no priced cost, call count, cache policy, or failed-attempt ledger.

## Scoring and evidence

### Deterministic endpoint scorer

Responses are mapped to `clean`, `poisoned`, `ambiguous`, or `unclear` using lowercase token overlap, Jaccard overlap, exact phrase containment, and tokens unique to one target. A score must reach 0.5 and exceed the opposite by 0.1; otherwise 0.34 separates ambiguous from unclear (Appendix B.6, pp. 24–25).

This is reproducible in prose and avoids an opaque LLM judge, but the evaluator code and calibration cases are not released. More importantly, it is coupled to short author-specified strings. Many targets differ by one endpoint, route, protocol, folder, or imperative phrase. A concise answer can match the poisoned string without demonstrating belief change, planned action, attempted execution, or environment effect; a correct paraphrase can miss. No human calibration, paraphrase/negation audit, executable target check, or false-positive/false-negative study validates the thresholds.

### Reported behavior and defense results

Without defense, paper Table 1 reports mean CleanAcc 94.40% and BCR 62.55% across the ten model rows. The reported BCR ladder is 45.37% L1, 51.73% L2, and 76.72% L3; substrate means are 67.91% flat, 56.58% fact store, and 63.14% hierarchical notes (pp. 7, 27–28). These paper tables support a bounded descriptive claim: under the authors' configured text pipeline, target-aligned responses differ substantially by authored level and materialization.

Table 2 reports `MIXed` at 10.70% BCR with 93.77% CleanAcc, compared with 62.55%/94.40% under no defense (pp. 7–8). This is not yet a benign-memory utility frontier:

- the clean condition writes only benchmark `context`, while the poisoned condition adds untrusted candidate writes;
- there is no matched **benign untrusted update** with the same channel, novelty, endpoint-like tokens, and update language as each poison;
- therefore a defense can reject useful user/tool/agent updates without that loss appearing in clean task accuracy;
- the paper says trusted context is admitted directly for some filters, yet CleanAcc varies sharply across defenses (PPL falls to 61.28%), leaving the treatment of clean context inconsistent or defense-specific;
- the held-out clean calibration split, retention estimates, thresholds, and false-positive rows are unavailable.

The results establish lower target imitation under selected filters while old trusted context remains available. They do not establish safe useful memory admission, personalization retention, or a deployable quality–security tradeoff.

No confidence intervals or family/case-clustered tests accompany defense differences. Table subscripts are described as standard deviations from five repeats, but it is unclear whether repeats cover stochastic calls, model means, cases, or another unit; Figure 3 instead uses standard deviation across ten models. Model, substrate, attack level, channel, and target template are strongly dependent, so row-level or repeat-only dispersion cannot license stable defense rankings.

## Unique insight: evaluate latent risk over future query sets, not one record at write time

MemPoison's most important design insight survives these validity limits: **admission safety is not a property of a record alone**. It is a property of a record set under authority, retrieval, transformation, future-query, action, and consequence distributions.

The reusable chain is:

```text
source principal and channel authority
→ candidate proposition(s) and intended scope/valid time
→ write-time evidence view and admit/block/sanitize decision
→ realized durable objects and transformations
→ co-resident claims, contradictions, and composition graph
→ future query/trigger opportunity
→ retrieval candidates and model-visible slate
→ semantic composition or conditional activation
→ adoption/rejection/deferral
→ attempted action or artifact/state mutation
→ gate/interceptor and realized effect
→ affected-party consequence, severity, reversibility
→ detection, quarantine, repair, forgetting, and retained benign utility
```

No link inherits the next. An admitted string is not a stored object; storage is not retrieval; co-retrieval is not composition; target-aligned text is not adoption; adoption is not attempt; attempt is not realization; realization is not calibrated harm; blocking poison is not preservation of useful memory; and removing one selected record after the fact is not a safe forgetting guarantee.

For benchmark design, pointwise admission tests should be paired with **set- and future-conditioned challenge generation**: contradiction closure, multi-record entailment, scope/recipient joins, trigger predicates, transformed summaries, and legitimate positive compositions. Defenses must face matched benign compositions, conditional preferences, updates, and handoffs so indiscriminate blocking cannot win.

## MID audit: the mechanism claim exceeds the statistic

MID reruns a trigger after removing designated retrieved poison objects. For L1 it reports a poisoned-target score drop; for L2 it removes fragments individually and jointly; for L3 it compares memory influence under trigger and “normal” contexts (paper §4.4, pp. 5–6; Appendix B.7–B.8, pp. 25–27).

The staged audit—write-blocked, admitted-not-retrieved, retrieved-noncausal, residual-causal—is a useful fate decomposition. Yet the named causal/mechanistic claims have major defects.

### 1. The L2 interaction sign does not show composition

The paper defines

`Ω(i,j) = Δ(i) + Δ(j) − d(full, remove-both)`.

A positive value means the joint-removal effect is **smaller** than the sum of individual-removal effects. Appendix B.7 correctly calls this “overlap or non-additivity” (p. 25), but the main text calls positive `Ω` evidence that corruption “emerges through interaction” and specifically validates L2 composition (pp. 6, 8).

That inference does not follow. Under a simple synergistic/compositional pattern where neither fragment matters alone but the pair matters jointly, both leave-one-out effects are small while joint removal is large, making this `Ω` **negative**, not positive. A positive value is compatible with redundancy, saturation, duplicated target cues, or a nonlinear lexical score. The reported `Ω=0.176` therefore cannot establish the claimed compositional mechanism without explicit null/additive conventions, matched redundant controls, and the full individual/joint response table.

### 2. L2 implementation does not cover the released fragment cardinality cleanly

The release contains L2 cases with two, three, and four injection turns, but the equations and primary interaction are pairwise. The appendix alternates among “pair,” “pair or fragment set,” and “group” without defining higher-order attribution or which pair is designated for 3–4-turn cases. No materialized record-family mapping or MID row is released. Joint-removal target sensitivity can show that an authored set supports the target; it does not decompose higher-order contribution.

### 3. L3 activation lacks a released normal-context arm

ActivationShift requires the same memory's influence under a normal and trigger context. The released L3 rows expose three trigger prompts; 1,791 of 1,863 L3 trigger rows have `natural_trigger_condition`, and 1,608 include that condition as an exact substring of the prompt. There is no separate normal-query field, matched non-trigger prompt, or normal-context output. The reported shift of 0.242 cannot be reproduced from the public instrument, and changing the query as well as trigger status requires matched controls to isolate conditional activation from generic query/target affinity.

### 4. “Causal” is observer- and intervention-relative

Removing an authored poison from the active retrieved slate is a meaningful context intervention, but the effect is measured only by reduction in the same authored poisoned-target lexical score. No negative-control memory removals, target paraphrases, alternative valid answers, common-random-number protocol, or repeated counterfactual ledger separates semantic necessity from stochastic rerun variance and scorer coupling. P2C is additionally conditioned on already-poisoned witness rows, so its 88.9–95.7% values are reversibility among selected successes, not rates over attacks or admitted records.

MID therefore supports an important method proposal—retain intervention, active view, score delta, and pipeline fate separately. V1 does not demonstrate a validated mechanistic decomposition or structural impossibility of write-time defense.

## Limitations and validity threats

### Construct, authority, and realism

1. **Authored targets are the oracle.** Context, poison, trigger, clean/poison target, and harmfulness share one construction lineage.
2. **“Real human interaction seeds” are untraceable.** Source locators, consent, transformations, and licenses are absent.
3. **No legitimate authority model.** User, tool, and agent channels receive heuristic trust weights, but authority depends on principal, purpose, subject, recipient, scope, freshness, and corroboration—not channel name alone.
4. **Text response is not action or harm.** No tool invocation, artifact mutation, external state, affected party, severity, reversibility, or recovery is observed.
5. **Preference dominates the pack.** 661/1,227 rows are preferences and 621 are L3; balanced diagnostic coverage and real workload prevalence are different estimands.

### Construction and sampling

6. **Human review cannot be audited.** Reviewer identity, agreement, adjudication, repair lineage, and item decisions are absent.
7. **Selection may favor reliable target induction.** L2 major fixes explicitly revise fragments and triggers when the intended corruption does not emerge; without held-out authoring/evaluation systems, this can co-design items with the target behavior.
8. **Family dependence is not honored statistically.** Repeated source/target families and three prompts per case require clustered inference and split firewalls.
9. **Release lineage is incomplete.** The pinned corpus predates v1, lacks a paper binding, and has 135 rows without `family_id`/`multidomain`.
10. **Public-only lifecycle.** No train/development/private-test role, renewal stream, contamination policy, or frozen anchor/bridge plan is provided.

### Treatment and measurement

11. **Substrates are stylized transformations, not representative systems.** Flat token-overlap retrieval, sentence splitting, and unspecified summary generation do not establish cross-architecture robustness.
12. **Configured components are under-pinned.** Model snapshots, provider dates, decoding, substrate code, defenses, thresholds, prompts, and retries are incomplete.
13. **BCR is target-string agreement.** Deterministic grading is inspectable in prose but uncalibrated against paraphrases, negation, alternative answers, actions, or humans.
14. **Utility omits benign untrusted writes.** Clean accuracy does not measure whether defenses retain legitimate updates resembling attacks.
15. **Missingness and repeats are opaque.** No attempt ledger, invalid denominator, per-repeat rows, or clustered uncertainty supports ranking claims.
16. **MID's L2 statistic is misinterpreted.** Positive `Ω` denotes overlap under the paper's own definition, not the canonical synergistic pattern.
17. **MID's L3 and higher-order inputs are unreleased.** Normal contexts, designated pairs/sets, materialized IDs, and counterfactual results are absent.

### Reproducibility and operational realism

The public dataset is a useful task-specification release: all 1,227 JSON rows parse, IDs are unique, nested injection/trigger fields are inspectable, and headline composition counts match. It cannot reproduce any paper score. The release omits evaluation/substrate/defense/MID code, exact configurations, calibration data, materialized memory states, retrieval logs, responses, judgments, attempts, and results. Reproduction would require large local compute and mutable proprietary APIs. The scenarios are short synthetic answer tasks, not long-running stores with permissions, concurrency, retention, deletion, real tools, professional artifacts, or downstream acceptance.

## Comparison with adjacent reviewed evidence

- **MemSyco-Bench** contributes the missing authority layer: relevant history may need to be ignored, constrained, deferred, superseded, or used. MemPoison adds adversarial multi-record and conditional structures, but its clean target remains author authority and its channel trust weights cannot substitute for principal/scope/precedence.
- **MemOps** separates expected lifecycle event from probe surface and warns that an authored trace is not observed write/delete realization. MemPoison observes simulated admission/retrieval fates in the paper but releases only expected writes and triggers, not realized memory objects or execution traces.
- **The Compliance Trap** moves delivered memory into free actions and endpoint state, while showing that divergence and baseline-like recovery do not identify adoption or repair. MemPoison has cleaner removal interventions but stops at short lexical responses and selected poisoned witnesses.
- **Governance Decay** makes context transformation a time-varying treatment and shows why authority must remain out of band. MemPoison's hierarchical summaries raise the same carriage question, but summary implementation and provenance are unreleased.
- **ClawSafety** supplies the necessary exposure → adoption → attempt → realization → harm → recovery → utility ladder. MemPoison sharply separates admission/retrieval/response, but its BCR reaches only response alignment and its clean control does not establish utility.

Together these sources argue against one scalar “memory safety” score. The benchmark needs separate authority, operation realization, retrieval/composition, decision adoption, action/effect, harm/recovery, and useful-retention estimands.

## Transfer to skill-bench

### Retain

1. L1 direct, L2 distributed, and L3 conditional records as **challenge structures**, not ordinal universal difficulty labels.
2. Substrate-independent semantic cases materialized under independently versioned storage/transformation implementations.
3. Paired clean/poisoned conditions and trigger-level raw outputs.
4. Explicit admitted, retrieved/co-retrieved, counterfactually influential, and endpoint-aligned fates.
5. Family IDs and variant caps, provided inference and splits actually use them.
6. Deterministic target scoring as one low-cost observer, never the sole evidence for open-ended action or harm.

### Repair

1. Bind every record to principal, represented subject, purpose, recipient, scope, valid time, confidence, corroboration, precedence, and allowed action influence.
2. Preserve actual write attempts, admitted/sanitized objects, transformation lineage, store deltas, candidate/ranked retrieval views, and decision-time presentation—not only expected writes.
3. Define L2 composition with explicit higher-order sets and factorial ablations: full set, each singleton, each leave-one-out set, clean/redundant/contradictory controls, and a predeclared interaction convention whose sign matches the hypothesis.
4. Give L3 a matched normal/trigger pair while holding query semantics fixed as far as possible; include irrelevant and legitimate conditional-memory controls.
5. Add matched benign untrusted writes and benign multi-record compositions from the same channel/template family; measure retention, later utility, over-blocking, and wrong sanitization.
6. Separate response alignment, semantic adoption, attempted action, gate decision, realized state, affected-party consequence, severity, reversibility, quarantine, repair, and forgetting.
7. Freeze family/source splits, model-independent task acceptance, result attempts, invalidity, configurations, costs, and case/family-clustered uncertainty.
8. Calibrate deterministic/model/human observers against paraphrases, negations, alternative valid outputs, insufficient evidence, and executable state consequences.

### Concrete test

In an existing cross-domain knowledge-work pilot, plant a matched quartet around one authorized workflow update:

1. one directly unauthorized record;
2. two individually admissible records whose conjunction becomes unauthorized;
3. one legitimate conditional update with the same surface trigger structure;
4. one malicious dormant update activated by the matched condition.

Cross no memory / each singleton / full set / leave-one-out / wrong-subject / superseded / stronger-evidence conditions. Preserve store and retrieval traces, let the agent produce an artifact or mock state transition, and score authorized utility plus unauthorized attempt/realization separately. This tests the general non-local-admission hypothesis without creating a memory-security vertical.

## Concrete repository action

No new queue task is warranted. Existing source-authority, memory lifecycle, experience-transfer, evidence-to-consequence, artifact/state admissibility, trace/root-cause, task-health, metric, configured-system, safety-conformance, and validity-argument machinery already has homes for every repair above. The nonduplicate action is to carry the **set-conditioned admission test and correctly signed higher-order intervention design** into the next relevant cross-domain pilot or consolidation, rather than create a MemPoison-specific schema.

## Claim boundary

MemPoison v1 provides inspectable evidence that 1,227 released synthetic cases encode direct, multi-record, and trigger-conditioned adversarial memory specifications, and manuscript-reported evidence that selected configured 2026 text pipelines often move toward author-specified poisoned targets across three stylized materializations. Its admission/retrieval/removal decomposition is a useful diagnostic direction.

It does **not** establish that the public bytes are the exact evaluated corpus; that every row was independently hand-validated; that the attack levels form an intrinsic difficulty scale; that `Ω>0` demonstrates compositional synergy; that L3 activation is reproducible; that write-time defenses face a structural impossibility; that `MIXed` preserves useful benign writes; that target-aligned text reflects semantic adoption, action, realized harm, or safe forgetting; or that rankings, professional safety, production fitness, economic value, and deployment readiness are valid.