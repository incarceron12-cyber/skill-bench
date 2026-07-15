# MemSyco-Bench: post-retrieval authority is the right target, but authored labels and an uncalibrated judge remain the oracle

**Source:** Zhishang Xiang et al., *MemSyco-Bench: Benchmarking Sycophancy in Agent Memory*, arXiv:2607.01071v2 (updated 2 July 2026), 43 pages; https://arxiv.org/abs/2607.01071v2.  
**Local PDF:** `data/papers/pdfs/2607.01071v2-memsyco-benchmarking-sycophancy-in-agent-memory.pdf` (SHA-256 `6a4c25d6c2ecdcf833740f42b29a54448ac741381d553c50e738180ec77c8d59`).  
**Local text read in full:** `data/papers/text/2607.01071v2-memsyco-benchmarking-sycophancy-in-agent-memory.txt` (SHA-256 `10cbef8ce398d71caa097e189cecec39e7d5d858b279f18724c875df99c0e47a`).  
**Official release inspected:** commit `c31e2c85ee8cc3c6f643587b8a6f4b5ad5eb3bf6`, tree `4d4b47fe0ae5cdd1eec49507d6a09c44f6550eff`; https://github.com/XMUDeepLIT/MemSyco-Bench/commit/c31e2c85ee8cc3c6f643587b8a6f4b5ad5eb3bf6.  
**Pinned archive:** `data/sources/releases/2607.01071v2-memsyco/XMUDeepLIT-MemSyco-Bench-c31e2c8.zip` (SHA-256 `1feea7d2b40ce7c122478e61acc495cb3a7027ac5a3a9a426618587377c4299b`).  
**Release provenance:** `data/sources/releases/2607.01071v2-memsyco/provenance.json`.

## Review status and charter fit

This is a **deep paper and release review**. I read the complete immutable v2 paper and inspected the complete 286-file official archive, all 1,550 released records, canonical schema and manifest, data tests, task adapters, five evaluators, judge prompts, aggregation, baseline registry/configuration, and benchmark driver. The pinned commit is dated 7 July 2026, five days after v2; it is official post-v2 implementation evidence, not demonstrated paper-time code or data.

The review advances charter objectives A–C by testing a general knowledge-work question: when historical user information is available, what evidence makes it authorized to influence a current decision? This is a reusable source/scope/time/evidence boundary, not a proposal to narrow `skill-bench` to personal assistants, memory systems, or sycophancy.

## One-sentence contribution

MemSyco-Bench makes the unusually important move from **whether memory was retrieved** to **what decision authority retrieved memory should have**—ignore as evidence, constrain to scope, defer to stronger evidence, supersede with a current preference, or use for personalization—but its synthetic generation/validation lineage, open-ended judge, and configured-system comparisons do not independently establish the authority labels, natural error prevalence, or a general memory capability.

## Why this matters

Every knowledge-work agent encounters relevant historical information that is not automatically authorized for the current decision: a client preference may not be factual evidence, an expert rule may be scope-limited, and a workspace note may be superseded. MemSyco-Bench provides a compact stress-test vocabulary for that boundary. Auditing it clarifies which links `skill-bench` must preserve before it can treat prior dialogue, expert knowledge, or learned procedure as legitimate evidence for an artifact or action.

## Contribution and research question

The paper asks whether long-term-memory agents can avoid “memory-induced sycophancy”: a historical belief or preference re-enters context and receives more authority than the current task warrants. Its five families are a compact decision-policy taxonomy (paper §§3.2–3.4 and Appendix A.3):

1. **Objective Fact Judgment:** preference-like memory is relevant but inadmissible as factual evidence.
2. **Contextual Scope Control:** a valid preference may inform only the subject, audience, or constraint to which it applies.
3. **Memory–Evidence Conflict:** current task evidence should outrank a familiar preference.
4. **Valid Memory Selection:** a current preference should supersede an outdated one.
5. **Personalized Memory Use:** valid preference memory should materially improve a recommendation.

The benchmark therefore does not reward permanent skepticism or permanent personalization. That bidirectional design is its main conceptual improvement over recall-only memory QA: an always-ignore policy should fail the fifth family, while an always-use policy should fail the first four.

The intended unit is one synthetic history, extracted/retrieved memory context, final open-ended request, generated response, and model-judge verdict. The target users are memory-system and agent developers comparing no-memory, full-dialogue, and external-memory configurations. Outputs are text answers rather than consequential environment actions or professional artifacts.

## Methodology and released instrument

### Construction

The paper describes a four-stage pipeline: define a memory-decision schema; generate related memory fragments, target answers, and memory-aligned failure directions; simulate multi-turn user/assistant histories; then validate semantic relatedness, the memory-use boundary, distinguishability, cue completeness, temporal/causal order, naturalness, and leakage (paper §3.3 and Appendix B). GPT-5.5 supports schema drafting, question generation, dialogue simulation, and consistency checking. User and assistant simulators reportedly receive role-limited information and do not see the target, failure direction, or task label (Appendix B.3).

This is sensible controlled generation, but the paper reports no candidate-pool size, rejection count/rate, human author or reviewer roles, annotation instructions, independent factual verification protocol, inter-annotator agreement, judge calibration, or item-level validation log. “We verify” and “we filter” therefore describe an authoring pipeline, not evidence that independent domain or represented-user authorities endorsed every boundary. The release contains final rows, not the schemas, generation prompts, rejected candidates, validation decisions, or transformation lineage needed to audit the stated leakage firewall.

### Released data

The canonical release contains exactly 1,550 parseable records with unique IDs:

| Task | Rows | Dialogue shape | Memory shape | Notable composition |
|---|---:|---|---|---|
| Contextual Scope Control | 300 | exactly 10 turns each | one active positive preference | 20 topics; two equal 150-row subtypes |
| Memory–Evidence Conflict | 300 | exactly 8 turns each | one active positive preference | 10 topics; one subtype |
| Objective Fact Judgment | 300 | exactly 6/8/10 turns, 100 each | one active reinforced preference | all source-labelled TruthfulQA; 300 distinct source row indices |
| Personalized Memory Use | 300 | 4–10 turns | 1–6 active items | six topics; 590 total memory items |
| Valid Memory Selection | 350 | 9–15 turns | exactly one outdated and one current item | 208 reversals, 104 replacements, 31 narrowing, 4 exceptions, 3 intensity changes |

Across all rows there are 1,217 unique question strings, 1,488 unique dialogue serializations, 952 unique references, and 913 unique concatenated memory-content bundles. Repetition is not automatically defective—Objective Fact Judgment deliberately creates paired variants—but it means uncertainty and split construction should cluster by shared source/schema/dialogue lineage rather than treat 1,550 rows as independent draws. The release supplies no train/private/test role, schema-family IDs, source-cluster split, exposure policy, or contamination-resistant renewal form.

Each row does expose useful authored primitives: dialogue, typed memory items with temporal status, a task policy, reference and preference-aligned answers where applicable, and task-specific rubric fields such as decisive evidence, scope limits, overgeneralization failure, tradeoff, expected behavior, and failure behavior. This is much stronger than a bare question/reference pair.

### Evaluation and aggregation

The post-v2 code adapts canonical rows into task-specific evaluator shapes in `evaluation/_dataset_compat.py`, injects raw dialogue or retrieved memory into an answer prompt, and uses task-specific model-judge prompts. Binary labels are combined into conjunctive passes. The evaluator recomputes internally inconsistent pass labels and normalizes some logically inconsistent judge outputs.

However:

- the judge receives the benchmark-authored memory, reference, expected behavior, failure direction, and in some tasks decisive/preference-supporting evidence; it checks agreement with that oracle rather than independently validating its authority;
- there is no deterministic score for the open-ended families and no released human–judge calibration, repeat-judge stability, false-accept/false-reject audit, or abstention policy;
- API and parse failures are recorded, but headline averages use only `judge_parse_ok` rows. Generation failures are excluded before the judge list is formed, and parse failures are excluded from the denominator while counts are reported. Thus the executable estimand is conditional on successful generation and parse, not the paper’s displayed `|D|` formula unless all calls succeed;
- Objective Fact Judgment has paired no-memory/with-memory branches, while the other four tasks evaluate only a memory-bearing branch. There is no matched irrelevant-memory, oracle-memory, corrupted-memory, or memory-content-substitution arm for those families;
- cached completions improve rerun efficiency but require cache and prompt/model/provider identity to remain part of the configured treatment.

## Evidence and what it supports

The main table spans five answer backbones, full dialogue, and seven paper-listed memory methods. It shows large and directionally coherent configured-system effects. For example, Qwen3-8B Objective Fact accuracy falls from 49.12 without memory to 30.62 with full dialogue while the sycophancy rate rises from 27.43 to 44.67. DeepSeek-V4-Flash falls from 74.33/18.67 to 61.67/32.67. On Qwen3-8B Memory–Evidence Conflict, full dialogue reaches 0.67 accuracy and 99.33 sycophancy; several retrieval systems improve this, but not uniformly. Personalized Memory Use sometimes benefits from external memory, while Valid Memory Selection often shows stale-memory contamination (paper Tables 1/3).

The retrieval diagnostics are the strongest mechanistic evidence. Across Mem0, A-Mem, and LightMem, the paper reports that 61–62% of errors occur after relevant information was retrieved. In Qwen3-8B conflict cases, A-Mem retrieves both factual and preference signals for all valid cases but reaches 25.91% conditional accuracy; in update cases it retrieves old and updated memories together for 98.57% and reaches 24.06%. Mem0’s Qwen conflict accuracy is 70.0% with fact only, 36.36% with fact plus preference, and 6.49% with preference only (paper §4.4 and Tables 2/7). These patterns support the narrower conclusion that retrieval sufficiency and post-retrieval answer calibration differ under this configured pipeline.

The guidance experiments also support a useful tradeoff rather than a universal mitigation. A generic caution instruction helps Memory–Evidence Conflict but reduces Personalized Memory Use by 13–21 points across reported settings; “Are you sure?” generally degrades performance and can reinforce old/misleading memory (paper §4.3 and Tables 5–6). This is evidence against one-dimensional “be cautious with memory” policies.

What the point estimates do **not** establish is stable system ranking or population prevalence. The paper reports no repeated runs, seeds, confidence intervals, paired tests, source/schema-clustered uncertainty, judge repeats, or multiplicity handling. The systems also preserve “native” writing, summarization, indexing, and retrieval configurations while sharing some models and top-k values; that is ecologically useful package comparison, not isolated attribution to retrieval, representation, or memory control. The post-v2 archive contains no paper-run outputs or per-item judge records, and its README explicitly says outputs are not included, so tables and diagnostics cannot be recomputed from released evidence.

## Unique insight: memory needs an authority ledger, not only a relevance score

MemSyco-Bench’s deepest reusable insight is that **semantic relevance does not authorize decision influence**. Historical information can be highly retrievable and still be:

- inadmissible as evidence for a factual claim;
- valid only for one subject, recipient, purpose, or constraint;
- defeated by stronger current evidence;
- superseded in valid time;
- legitimately controlling for a personalized choice.

This implies a general benchmark contract:

`historical event/source → represented subject and authority → memory write and status → retrieval/presentation → current task purpose/recipient → admissible role and precedence → model adoption/rejection → answer/action → criterion-specific observer → consequence`

The benchmark observes authored versions of the source content, status, current task, expected role, answer, and judge verdict. It does not independently observe represented-user authorization, real-source authority, whether the solver attended to or adopted a retrieved item, causal dependence on that item, realized action, affected-party outcome, or downstream benefit/harm. Calling every wrong memory-aligned answer “sycophancy” can therefore compress several distinct failures—bad source truth, wrong scope, stale status, retrieval omission, prompt salience, solver arbitration, and judge error—into one label.

For `skill-bench`, the key transfer is not a memory-specific score. It is to make **authority, applicability, precedence, and valid time** explicit for any prior expert statement, client preference, workspace note, or learned procedure, then retain the full available → retrieved → presented → adopted → acted-on → observed chain.

## Limitations and validity threats

### Construct and authority

1. **Authored legitimacy is the oracle.** The same generation/validation process supplies memories, references, expected behavior, and failure directions; there is no independent factual, represented-user, or domain-authority adjudication.
2. **“Sycophancy” is broader than measured motivation.** The scorer observes answer alignment with a memory-shaped direction, not deference motivation. Prompt salience, ordinary factual error, ambiguous recommendation, or generator weakness can produce the same endpoint.
3. **The five policies are not a factorial design.** Task family, topic, dialogue length, number/status/type of memories, answer form, and rubric all change together. Differences between families do not isolate suppress/constrain/defer/update/use policy difficulty.
4. **Personalization has no real user.** Synthetic preferences and author-defined satisfactory recommendations do not establish current consent, preference truth, recipient benefit, or acceptance.
5. **Action and consequence are absent.** Text recommendations are not evidence of later execution, artifact/state quality, collateral effects, or professional utility.

### Treatment and diagnosis

6. **Only one family has a paired no-memory contrast in the main runner.** The remaining tasks cannot separate memory necessity from question solvability or generic model ability with equivalent arms.
7. **Retrieval does not establish adoption.** The diagnostic checks whether target evidence appears in retrieved context and compares endpoint correctness, but does not show access, semantic uptake, rejection, or causal dependence.
8. **Native systems differ in more than memory quality.** Writing model, summary policy, index, retrieval granularity, injected context, compute, and external dependencies vary. Results are configured-package behavior.
9. **Shared construction and answer/judge model families create coupling risks.** GPT-5.5 supports dataset construction; DeepSeek-V4-Flash is used for memory construction in cross-backbone experiments and is the release’s default answer/judge model. No model-family swap audit tests whether wording and oracle preferences favor related systems.
10. **No provenance-preserving negative controls.** Irrelevant, corrupted, wrong-subject, wrong-recipient, stale-but-historical-only, and source-authority substitution controls are not crossed on matched instances.

### Grading, statistics, and lifecycle

11. **Judge validity is unmeasured.** No human labels, agreement, repeat-call reliability, evidence-view ablation, or adversarial audit support the semantic binary labels.
12. **Invalid rows change the denominator.** Executable aggregation excludes generation errors and judge-parse failures from averages, contrary to an unconditional dataset denominator unless failure counts are zero.
13. **No uncertainty.** Single point estimates ignore stochastic generation, memory construction, hosted services, judge variation, and shared source/schema clustering.
14. **Public repeated lineage is unmodeled.** Shared questions, dialogues, references, memory bundles, and TruthfulQA sources require clustered reporting and contamination-aware splits.
15. **No result corpus.** Released code/data cannot reproduce the paper tables without mutable paid/hosted endpoints and fresh stochastic calls; exact paper outputs, judgments, retries, invalid rows, seeds, and configurations are absent.

### Release audit and operational realism

16. **The shipped integrity test fails.** Four data hashes match `data/manifest.json`; `objective_fact_judgment.jsonl` hashes to `cd34eb...` while the manifest expects `c6ea7e...`. The expected hash is exactly the CRLF-transcoded variant of the released LF bytes, despite `.gitattributes` requiring LF. `python -m unittest -v dataset.test_dataset` therefore runs three tests with two passes and one failure. This is a line-ending manifest defect, not evidence of row corruption, but it makes the advertised byte-integrity gate red on the pinned release.
17. **The full vendored tree does not compile.** Targeted core evaluator/baseline compilation is possible, but `compileall` reaches `baselines/lightmem/vendor/src/lightmem/memory/graph.py`, which contains only `class GraphMem:` and raises `IndentationError`. A dry run does successfully generate all five RawDialogue evaluator commands. Full baseline installation/execution was not attempted because it requires large optional dependencies, hosted model/embedding services, and credentials.
18. **Post-v2 release identity differs from paper terminology.** The release driver exposes nine peer settings and names `MemZero`, whereas the paper table names `Mem0`; paper-time equivalence is not demonstrated. The archive postdates v2 and has no result artifacts.
19. **Cost accounting is partial.** Paper Table 4 estimates only final answer input/output tokens offline because API usage was not retained. It omits memory writing, embeddings, indexing, storage, judge calls, retries, wall time, provider pricing, and amortization.
20. **Operational realism is bounded.** Short synthetic dialogues and open-ended recommendations are controlled calibration items, not long-term deployed memory, messy evidence work, real preference revision, multi-party authority, or consequential action.

## Comparison with adjacent reviewed benchmarks

- **LongMemEval-V2** makes trajectory-history evidence delivery and representation inspectable but stops at retrospective QA. MemSyco adds explicit post-retrieval role/precedence policies; neither establishes held-out action benefit.
- **MemoryArena** makes earlier experience affect later actions, but feedback, state reconstruction, and heterogeneous graders confound the memory cause. MemSyco is more controlled and less consequential.
- **EvoMemBench** broadens scope/content and memory architectures but changes task, feedback, endpoint, and observer across cells. MemSyco’s policy taxonomy is cleaner, yet its five families still are not matched factorial treatments.
- **ClawArena** contributes corrections, retractions, and supersession in evolving workspaces. MemSyco adds preference-specific update and scope failures but lacks persistent state/action consequences.
- **SovereignPA-Bench** exposes current intent, historical memory, third-party pressure, consent, and burden. It reminds us that an author-defined memory policy is not represented-user authority; MemSyco does not measure consent or burden.
- The existing **action-and-memory synthesis** and `pilots/experience-memory-transfer/` already preserve reset, current-context sufficiency, provenance/status, retrieval/presentation/adoption, held-out action, supersession, harmful transfer, rollback, state deltas, and observer sufficiency. MemSyco sharpens the authority/precedence vocabulary but does not justify another memory schema or pilot.

## Transfer to skill-bench

### Retain

1. The five-way **ignore / constrain / defer / supersede / use** policy vocabulary as cross-domain decision roles for historical information.
2. A required positive-use family so indiscriminate skepticism cannot pass.
3. Explicit memory-aligned failure directions alongside target behavior.
4. Separate endpoint correctness and characteristic memory-contamination labels.
5. Retrieval-group diagnostics that distinguish absent target evidence from retrieved-but-wrong outcomes.
6. Matched lightweight policy interventions that reveal caution–personalization tradeoffs.

### Repair

1. Bind each prior item to source authority, represented subject, purpose, recipient, valid time, scope, confidence, supersession relation, and admissible decision role.
2. Cross policy treatments on matched base scenarios while holding current evidence, task, solver, observer, and answer format fixed.
3. Add no-memory, oracle-memory, irrelevant, wrong-subject, wrong-recipient, stale, corrupted, and evidence-authority substitution arms.
4. Record write, retrieval, presentation, access, adoption/rejection, action, and consequence separately; use memory removal/substitution to test causal use.
5. Preserve candidate generation, rejection reasons, validator identity, factual sources, schema-family IDs, and transformation hashes. Obtain plural authoritative review where factual, professional, or represented-user boundaries matter.
6. Calibrate each judge predicate against blinded human/expert decisions, repeated calls, paraphrases, borderline cases, and deliberately insufficient evidence. Treat abstention as instrument invalidity, not model failure.
7. Keep all attempted rows in the primary denominator; report generation, memory, provider, parse, and judge-invalid outcomes separately.
8. Repeat stochastic components and cluster uncertainty by source/schema/dialogue lineage. Version data, evaluator, judge, provider, cache, and exposure role independently.

### Test

Use the existing experience-memory-transfer and authority-to-consequence machinery rather than starting a memory-only project. Add matched checks only when they can exercise a general knowledge-work hypothesis: an expert/client statement that is (a) relevant but inadmissible as evidence, (b) valid only for one recipient/purpose, (c) superseded, (d) defeated by a stronger source, or (e) legitimately controlling. Require both a correct decision and a provenance-preserving artifact/state consequence.

## Concrete repository action

No new queue task is warranted. The review’s build implications duplicate completed or existing contracts for source authority, information flow, valid time/supersession, experience-memory transfer, evidence-to-consequence state, plural judgment, invalid-trial handling, configured-system identity, and grader calibration. The durable action is this review plus synthesis/landscape indexing; a future builder should exercise these roles inside a cross-domain slice already selected by the queue rather than create a MemSyco-specific schema.

## Claim boundary

MemSyco-Bench v2 provides credible evidence that selected configured 2026 answer-and-memory pipelines respond differently when synthetic historical preferences are authored to be irrelevant, scope-limited, evidence-defeated, superseded, or useful. Its retrieval diagnostics support the important conclusion that retrieving relevant information does not ensure correct post-retrieval arbitration, and its caution experiment exposes a real calibration tradeoff inside this instrument.

It does **not** establish natural prevalence of memory-induced sycophancy, independently validated factual or user-preference authority, represented-user benefit, causal adoption of retrieved memory, a common memory capability, stable system rankings, reliable judge labels, professional knowledge-work validity, safety, production fitness, economic value, or deployment readiness.
