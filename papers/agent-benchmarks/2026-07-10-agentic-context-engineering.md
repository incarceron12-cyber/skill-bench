# Paper Review: Agentic Context Engineering — Evolving Contexts for Self-Improving Language Models

- **Paper:** https://arxiv.org/abs/2510.04618v3
- **Authors:** Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, and Kunle Olukotun
- **Date read:** 2026-07-10
- **Venue / source:** ICLR 2026 conference paper
- **Tags:** context-adaptation, agent-memory, continual-evaluation, delta-updates, feedback-quality, benchmark-contamination, provenance
- **Version read:** immutable arXiv v3, 29 March 2026
- **Local PDF:** `data/papers/pdfs/2510.04618v3-agentic-context-engineering-evolving-contexts.pdf` (32 pages; SHA-256 `51050ced82df75c143b151262d5af8763916968ca50374bd8ff778f40552b0ad`)
- **Local text:** `data/papers/text/2510.04618v3-agentic-context-engineering-evolving-contexts.txt`
- **Code named by paper:** https://github.com/ace-agent/ace

## One-sentence contribution

ACE replaces repeated whole-prompt rewriting with an itemized playbook updated through Generator → Reflector → Curator stages and deterministic delta merges, producing large reported gains across AppWorld and specialized reasoning while demonstrating that **representation and update semantics—not merely reflection—determine whether an agent’s accumulated experience compounds or collapses**.

## Why this matters for skill-bench

`skill-bench` is itself a compounding system: research, expert elicitation, benchmark runs, and adjudications should improve later tasks without silently erasing evidence or turning benchmark-specific accidents into general doctrine. ACE supplies a useful systems pattern for that loop: immutable identifiers, localized additions, usage feedback, deduplication, and delayed refinement are safer than periodically asking an LLM to rewrite “everything we know” (Sections 2.2 and 3).

The paper’s strongest transfer is therefore not “give agents longer prompts.” It is a **typed, provenance-preserving update protocol**:

`execution evidence → diagnosed failure/success → candidate lesson → bounded delta → validation → promotion or quarantine`.

ACE implements only part of this protocol. Its bullets have IDs plus helpful/harmful counters, but the published curator prompts expose only `ADD`; they do not require source provenance, confidence, contradiction links, scope, expiry, or independent validation (Appendix F, Figures 10–14). Those omissions matter more in benchmark construction than in AppWorld. A plausible but false benchmark-design lesson can contaminate future rubrics and make evaluation appear to improve by learning the test distribution.

## Research question

The paper asks whether contexts can be adapted as comprehensive, evolving playbooks—offline as system prompts or online as memory—without the brevity bias and catastrophic information loss induced by monolithic LLM rewriting. It tests whether modular reflection/curation, incremental updates, and grow-and-refine improve agent and domain-task accuracy across models, supervision settings, and adaptation regimes, and whether this is cheaper than GEPA or Dynamic Cheatsheet.

The evidence strongly supports the narrower claim that itemized incremental updates outperform the authors’ full-rewrite variant in their AppWorld setup. It supports broad task gains, but does not isolate whether those gains come from preserving knowledge, repeated exposure to benchmark-family examples, access to unusually informative feedback, or prompt-specific implementation choices.

## Methodology

### System and update unit

ACE divides adaptation into three roles, all normally instantiated by the same backbone model (Section 3; Section 4.2):

1. **Generator:** solves a query using the current playbook and reports relevant bullet IDs.
2. **Reflector:** compares the trajectory and outcome—optionally ground truth/reference code and unit-test results—to identify errors, root causes, corrections, and helpful/harmful/neutral bullet tags.
3. **Curator:** emits only novel, actionable `ADD` operations rather than rewriting the playbook.
4. **Deterministic merge/refinement:** assigns IDs, updates metadata, and semantically deduplicates entries. Refinement may run after every delta or lazily when the context exceeds a threshold (Sections 3.1–3.2).

A bullet is a small strategy, concept, code fragment, API fact, or failure warning with a unique ID and helpful/harmful counters. Offline adaptation iterates over training examples, up to five epochs and five reflection rounds; online adaptation predicts on each shuffled test item and then updates context from that item. Batch size is one (Sections 4.1–4.2).

The appendix prompts make the method more concrete—and narrower—than the architecture diagram. The AppWorld reflector receives the full trajectory, unit-test report, and, in supervised runs, known-correct ground-truth code. It is explicitly prompted to infer authoritative data sources, filtering errors, API schemas, authentication failures, and step-by-step corrections. The curator receives the current playbook, generated attempt, and reflection and emits JSON additions. The FiNER equivalent compares the predicted answer to ground truth and asks for reusable concepts or calculation rules (Appendix F).

### Tasks, comparisons, and metrics

- **AppWorld:** multi-turn API/coding tasks, reported with task-goal completion (TGC) and scenario-goal completion (SGC) on normal and challenge test splits. The base is official ReAct with DeepSeek-V3.1-671B; offline comparisons include ICL and GEPA, online comparison uses Dynamic Cheatsheet (Sections 4.1–4.3).
- **Finance:** FiNER (139-class XBRL entity tagging) and Formula numerical reasoning, exact-match accuracy. Additional offline experiments use DDXPlus medical diagnosis and BIRD-SQL, the latter scored by GPT-4o-mini (Sections 4.1, 4.4; Appendix A.2).
- **Backbones:** the main model is DeepSeek-V3.1; appendices report GPT-OSS-120B, GPT-5.1, and Llama-3.3-70B-Instruct (Section 4.5; Appendix A.1).
- **Cost:** adaptation latency, rollouts, input/output tokens, nominal token cost, and prompt-cache reuse are reported against selected baselines (Section 4.7; Appendix A.3).

All methods use the same shuffled order in online evaluation. Offline contexts are built on training data and evaluated pass@1 on test. The paper does not report repeated shuffle seeds, run-level confidence intervals, or statistical tests.

## Evidence and results

1. **AppWorld:** DeepSeek ReAct averages 42.4 across four TGC/SGC cells. Offline ACE reaches 59.4 with labels and 57.2 without them; online ACE reaches 59.5 versus Dynamic Cheatsheet’s 51.9 (Table 1). The reported main online value includes offline warmup: Table 3 shows online ACE alone at 56.1 and ACE + warmup at 59.5. Thus the headline “online” result is not a clean from-scratch online comparison.
2. **Finance:** supervised offline ACE averages 81.9 versus 72.5 for GEPA and 69.1 base. Unsupervised offline ACE averages 77.1. But weak-feedback online adaptation is unstable: FiNER falls from 70.7 base to 67.3 for ACE and 68.3 for Dynamic Cheatsheet; unsupervised Dynamic Cheatsheet averages 65.4, below base (Table 2). This is direct evidence that memory evolution can amplify error.
3. **Other domains/models:** ACE improves DDXPlus 75.2→90.2 and BIRD-SQL 47.8→52.9. It improves reported base scores across four model families, though Llama FiNER gains are only 1.1–2.4 points (Tables 5–11).
4. **Mechanism evidence:** on AppWorld test-normal, removing incremental updates reduces the ACE average from 70.3 to 56.9; base is 53.3 (Table 18). Adding the Reflector and then multi-epoch adaptation produces stepwise aggregate gains in Table 3. This is the clearest causal evidence in the paper.
5. **Noise stress test:** FiNER is 78.3 under normal ACE and remains 76.1 when an explicitly harmful reflection is injected every five iterations, but drops to 66.7 when every update is harmful (Table 17). This demonstrates tolerance to sparse synthetic corruption, not robust detection of naturally plausible false lessons.
6. **Sensitivity:** 3–5 reflection rounds work best; ten degrade from the five-round setting. Dedup thresholds from 50–90% and pruning triggers from 10K–100K tokens remain above base, although results are not monotonic (Tables 19–21).
7. **Efficiency:** the one-epoch/one-reflection AppWorld cost study reports 39.3M adaptation input tokens for ACE versus 204.1M for GEPA, but ACE uses more rollouts (2,075 versus 1,455). At evaluation, ACE consumes 117.4% more raw input tokens than GEPA. An OpenAI prompt-caching study reports 91.8% cached input and an 82.6% billed-input reduction relative to charging all raw ACE tokens (Section 4.7; Tables 12–15). These are configuration- and serving-dependent economics, not an intrinsic complexity reduction.

## Unique insight

The deepest insight is that **compounding knowledge needs transaction semantics**. Whole-context rewriting gives a probabilistic model permission to delete arbitrary prior evidence. ACE changes the mutation surface: a model proposes a small delta, while deterministic code controls integration. The AppWorld ablation makes this more than an aesthetic preference; most of the measured gain disappears without incremental updates (Table 18).

For benchmark programs, however, append-only is necessary but insufficient. A benchmark memory is not merely advice optimized for near-term score. It is an evidence base whose claims can change tasks, rubrics, and public conclusions. The unit that should persist is therefore not an unqualified bullet, but a **versioned claim with lineage and lifecycle**. Helpful/harmful counts confound at least four things: truth, relevance to the current sample, model compliance, and grader feedback quality. A true rare-case warning can accrue “harmful” marks when over-applied; a benchmark-specific shortcut can appear highly helpful while destroying out-of-distribution validity.

A second insight is that “self-improvement without labels” is only meaningful after typing the feedback channel. AppWorld’s natural execution signals include unit tests, API errors, and task completion checks—often highly diagnostic proxies for the target. FiNER lacks such signals and degrades online. The relevant variable is not the boolean `GT Labels`; it is the information content, provenance, and independence of feedback. `skill-bench` should distinguish compiler/runtime evidence, deterministic requirement checks, expert adjudication, reference-answer exposure, self-critique, and downstream outcome evidence.

A third insight is methodological: online benchmark adaptation changes the estimand. Once item *i* updates the playbook used on item *i+1*, the score measures a learner over an ordered stream, not independent task competence. Shared shuffle order improves method comparability for one stream but does not establish order robustness, prevent near-duplicate transfer, or quantify contamination. Stream design, reset policy, and adaptation budget become part of the benchmark specification.

## Transferable design patterns

### 1. Treat lessons as evidence-bearing records

Each proposed benchmark-design lesson should carry:

- immutable `lesson_id`, version, and content hash;
- typed claim (`strategy`, `failure_signature`, `tool_fact`, `rubric_rule`, `safety_rule`, `hypothesis`);
- source/trace/adjudication locators and feedback-channel type;
- scope and applicability predicates;
- confidence plus confirming and disconfirming observations;
- contradiction/supersession edges;
- authoring model/prompt/tool versions;
- lifecycle state: `candidate`, `validated`, `promoted`, `quarantined`, `deprecated`;
- downstream tasks/rubrics affected.

This preserves ACE’s localized updates while preventing an LLM-generated reflection from masquerading as durable expert knowledge.

### 2. Separate proposal, validation, and promotion

Do not let the same trajectory both generate a lesson and validate it. Candidate deltas should enter a quarantine layer, run against held-out or counterfactual scenarios, and be promoted only when they improve a declared criterion without regressing safety, contradiction handling, or distribution-shift checks. This adds an independent **Validator** role missing from ACE’s Generator–Reflector–Curator loop.

### 3. Type feedback by authority and leakage risk

Record whether a reflection used public task text, tool/runtime output, public verifier output, private checks, a reference answer, expert adjudication, or model self-assessment. A lesson derived from private test evidence must not flow into an agent-visible playbook for the same evaluation split. Feedback access is a treatment and needs a versioned policy/hash.

### 4. Make continual-evaluation protocols order-aware

A stream benchmark should pin item order and seed, similarity clusters, reset cadence, adaptation budget, warmup data, update visibility, and scoring window. Report at least:

- pre-update performance;
- post-update forward transfer on held-out clusters;
- backward retention/regression;
- worst-order and multi-seed variance;
- memory size and retrieval/caching cost;
- contamination rate from private or same-family evidence.

### 5. Preserve localized rollback

Because each lesson has lineage and downstream references, regressions can trigger targeted rollback rather than another whole-memory rewrite. Deleting or revising a lesson should be an explicit event with rationale; semantic deduplication must not silently merge contradictory requirements merely because their embeddings are close.

## Limitations and validity threats

1. **The strongest “online” AppWorld result includes offline warmup.** Table 1’s 59.5 corresponds to Table 3’s `ACE + offline warmup`, while from-scratch online ACE is 56.1. This blurs the adaptation-regime claim and gives ACE extra prior exposure relative to a strict online baseline.
2. **Feedback richness is not controlled.** Ground-truth code and unit-test reports can provide substantially different information from exact labels, execution errors, or self-generated feedback. The binary label/no-label column hides the causal variable that Table 2 itself shows is critical.
3. **Sequential test adaptation creates order dependence and possible family leakage.** Only one shared shuffled order is reported. No reset-by-scenario, semantic-neighbor audit, multiple-order variance, or forward-transfer isolation is shown.
4. **No uncertainty for accuracy gains.** Results are presented as point estimates without repeated agent runs, confidence intervals, significance tests, or seed variance. AppWorld cells are modest enough that stochastic and order effects may matter.
5. **Ablations are incomplete and partly bundled.** The main Table 3 jointly removes Reflector and multi-epoch in one row; it does not independently ablate Curator, bullet attribution, helpful/harmful counters, semantic deduplication, structured sections, or retrieval. Table 18 isolates incremental updating but not whether the gain comes from preservation, extra length, or different prompts.
6. **Natural corruption is not modeled by the harmful-reflector test.** Explicitly adversarial injected text every N iterations differs from persuasive, correlated, partially correct, or distribution-specific reflections—the failures most likely to survive deduplication.
7. **Append-only prompt/implementation mismatch.** The prose says existing bullets can be updated in place and harmful entries filtered, but published curator prompts permit only `ADD`; the exact algorithms for counter updates, pruning, and harmful filtering are insufficiently specified in the paper.
8. **Semantic deduplication is not contradiction management.** No embedding model, calibration procedure, false-merge analysis, contradiction detector, or provenance-preserving merge rule is reported. Similarity thresholds show downstream accuracy only.
9. **Cost comparisons depend on mismatched search procedures and infrastructure.** GEPA uses held-out validation and `auto="heavy"`; ACE uses different queries and update loops. The headline lower rollout claim in Table 4 (357) differs from the appendix’s one-epoch count (2,075), apparently because configurations/definitions differ. Evaluation raw input is more than double GEPA’s, and cache savings depend on provider behavior.
10. **Model and benchmark breadth does not establish operational realism.** AppWorld is a controlled simulator; FiNER, Formula, DDXPlus, and BIRD-SQL are answer tasks. The paper does not test changing policies, human override, privacy deletion, poisoned feedback, irreversible side effects, or long-lived multi-user memory.
11. **Leaderboard comparison is contextual, not controlled.** The paper acknowledges IBM CUGA differs architecturally and is not a methodological baseline. Similar aggregate scores cannot attribute parity to ACE.
12. **BIRD-SQL uses an LLM judge without validation details here.** The paper does not report judge-human agreement or sensitivity for the claimed transfer result.

## Reproducibility and operational realism

The paper is unusually useful at the prompt/interface level: it publishes Generator, Reflector, and Curator templates; names backbones, datasets, baseline implementations, epoch/reflection caps, batch size, metrics, and cost components; and links an official code repository. The immutable v3 PDF and full local text above preserve the reviewed artifact.

Exact reproduction still requires more than the manuscript provides: pinned repository commit and dependencies, model snapshots and decoding parameters, AppWorld task order/seed, exact playbook serialization, embedding model and dedup implementation, pruning/merge rules, cache-pricing date, raw per-run outputs, and reconciled rollout definitions. The proprietary or time-varying model APIs and large token budgets also make “reasonable computational resources” a weak description: the appendix reports tens to hundreds of millions of adaptation input tokens.

Operationally, ACE tests real iterative tool use and records latency/cost, but assumes that all accumulated lessons can be shared safely. Production benchmark systems need tenant/task boundaries, provenance-aware deletion, approval for policy-level changes, private-check non-disclosure, and rollback. The paper gestures toward selective unlearning but does not evaluate it (Section 5).

## Concrete changes for skill-bench

1. **Add a compounding-knowledge contract upstream of benchmark bundles.** Represent candidate lessons with provenance, feedback authority, scope, contradiction/supersession edges, lifecycle, and downstream dependency links. Never overwrite the historical record during consolidation.
2. **Gate promotion with held-out evidence.** Require at least one independent confirming observation and a regression suite before a candidate lesson can alter task templates, schemas, rubrics, or public benchmark guidance.
3. **Add feedback-channel provenance to trials and authoring evidence.** Replace `has_ground_truth`-style booleans with typed visibility and authority: runtime, deterministic public check, private grader, reference artifact, expert, or self-reflection.
4. **Define a continual-evaluation protocol before using cross-task memory.** Pin orders/seeds, similarity groups, reset policy, warmup, update budget, and private-evidence firewall; report transfer, retention, regression, and order variance separately from static pass@1.
5. **Test context-collapse and memory-pollution failure signatures.** Include sudden token/entry loss, unsupported lesson promotion, contradictory merge, overgeneralized rare-case rule, stale policy retention, private-check leakage, and score gains limited to near-duplicate tasks.
6. **Keep context efficiency as a measured property, not an assumption.** Record raw/cached tokens, retrieval rate, latency, and provider-independent costs. A longer playbook is justified only when held-out quality or diagnosability improves.

## Action items for repository

- [x] Read and preserve the complete immutable v3 PDF and 32-page local extraction.
- [x] Document the ACE transaction pattern, feedback-quality dependence, online-evaluation estimand, and benchmark-specific validity threats.
- [ ] Build a provenance-bearing candidate-lesson/promotion schema with rollback and private-evidence firewall.
- [ ] Pilot it on review-derived design claims using held-out contradiction and regression checks before allowing promoted lessons to change benchmark artifacts.
