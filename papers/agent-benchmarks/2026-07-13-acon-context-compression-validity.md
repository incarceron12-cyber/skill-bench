# Paper and Release Review: ACON — Task Reward Is Not State Fidelity

- **Paper:** https://arxiv.org/abs/2510.00615v3
- **Authors:** Minki Kang, Wei-Ning Chen, Dongge Han, Huseyin A. Inan, Lukas Wutschitz, Yanzhi Chen, Robert Sim, and Saravan Rajmohan
- **Date read:** 2026-07-13
- **Source:** complete immutable arXiv v3, updated 2026-06-01; ICML 2026 / PMLR 306
- **Tags:** context-compression, state-fidelity, prompt-optimization, long-horizon-agents, configured-system-effects, efficiency-validity
- **Local PDF:** `data/papers/pdfs/2510.00615v3-acon.pdf` (57 pages; SHA-256 `fa8ebffc77293ea1a42ecf52db45fc9208b155a86d0f789ae71121c7cd16f2a3`)
- **Local text:** `data/papers/text/2510.00615v3-acon.txt` (SHA-256 `5cd93505f54937291e8df975d9067147abb0ad15748574a40e5318454c8e3f09`)
- **Official repository:** https://github.com/microsoft/acon, inspected at commit `d63f9ae18959dc7215ff62899c94c5e8c56847ae` (root tree `42580055a16d6d7ee470047b7357c02b6a4ec0ab`); provenance: `data/sources/releases/2510.00615v3-acon/provenance.json`
- **Timing boundary:** the inspected commit is 13 days after arXiv v1 and more than seven months before v3. The paper pins no commit, so the tree is release evidence, not exact paper-time implementation evidence.

## One-sentence contribution

ACON optimizes natural-language prompts for compressing either an agent's accumulated history or latest observation by analyzing train-task regressions against an uncompressed trajectory, then optionally distills the compressor—but its terminal task reward and token metrics do not establish that the compressed record is faithful, and the paper's own qualitative examples contain material state and answer corruption.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C. Context compression is not merely an efficiency feature: in realistic knowledge work it is a **lossy state transformation** that can delete source authority, valid-time qualifiers, contradictions, commitments, failed attempts, artifact state, and evidence needed for later audit. The concrete evidence is the complete 57-page paper plus the pinned 802-file official implementation.

This is methodological expansion, not a proposal to narrow `skill-bench` to context compression or productivity agents. Useful completion is a claim boundary: selected task success and lower peak tokens can justify a configured-package efficiency result, but not faithful state preservation, general transfer, professional validity, reliability, production fitness, or readiness.

## Research question and claim ladder

The defensible question is: **Can failure-driven prompt optimization find history/observation compression policies that improve the task-reward/token trade-off for particular agent–compressor–benchmark configurations?**

The stronger implied chain is:

```text
baseline succeeds and compressed run fails
→ compression caused the failure
→ an LLM correctly identifies the lost information
→ a revised guideline preserves essential state
→ selected benchmark reward improves
→ the summary is faithful
→ the compressor transfers across agents/tasks
→ the system is cheaper and deployable
```

Only selected links are tested. Baseline/compressed runs are stochastic and not paired counterfactuals; session reset and context rewriting change more than retained information; candidate prompts are selected on sampled training performance; task reward observes only benchmark-scored consequences; and end-to-end API savings coexist with increased latency. Fidelity, transfer, and deployment require separate evidence.

## Methodology and system

### 1. Compression contract

The agent is modeled as acting in a deterministic POMDP with a fixed policy model and prompt (paper pp. 3–4). Two interventions are evaluated separately:

- **History compression:** once accumulated history exceeds a threshold, an LLM rewrites older interactions into a summary, retains the last action–observation turn, starts a fresh session, and injects the original task plus summary.
- **Observation compression:** once the latest observation exceeds a threshold, an LLM rewrites it before the agent sees it and before it enters history.

The objective is expected terminal reward minus a weighted context-cost term (Eq. 7, p. 4). In experiments, however, the two terms are handled by alternating heuristic prompt updates rather than an identified optimizer. UT seeks reward; CO seeks shorter summaries among successful compressed trajectories (pp. 5–7, 23). No compression-level gold labels or invariant-preservation checks are used.

The implementation makes the treatment more specific than “compression.” `MemoryManager.optimize_history` starts a new conversation session, restores the system and first user prompt, injects the generated summary, and reattaches preserved recent turns (`src/productive_agents/agents/memory.py`, lines 357–498). Therefore the intervention bundles:

1. lossy content selection;
2. content reformatting into structured sections;
3. instruction recency/restatement;
4. session reset;
5. removal of prior reasoning and error loops;
6. changed KV-cache and position effects.

A success gain cannot identify which component helped. “Compression clarifies” is one possible mechanism; reset-induced de-anchoring or renewed task salience is another.

### 2. Failure-driven natural-language optimization

For UT, each training task is run without and with compression. The method retains cases where the no-compression run succeeds and the compressed run fails, gives both trajectories to an optimizer LLM, and asks it to locate the first divergence, missing facts, distorted summaries, lost variables, action errors, and remediations (pp. 5, 23, 26–27). Five candidate prompts are generated and selected by success on a training subset. CO analyzes successful compressed trajectories for removable content and selects by reward–cost (pp. 5, 18, 23).

This is useful because it treats compression failures as diagnostic evidence rather than optimizing summary similarity. But the contrast is not a causal pair:

- the paper acknowledges API nondeterminism despite temperature 0 and seed 42 (p. 18);
- only one trajectory per condition is reported;
- baseline-success/compressed-failure selection enriches stochastic reversals and excludes shared failures, compressed successes, and silent corruptions with no scored consequence;
- an LLM infers causality from two different trajectories without replaying the alleged omitted fact into the same state;
- the released analyzer falls back to all optimized failures when no direct regressions exist and can operate with no baseline at all (`unified_update_history_prompt.py`, lines 239–352, 440–464), weaker than the paper's contrastive story;
- the paper says candidates are selected on a held-out subset of training tasks, but does not report its identity, size, fixed manifest, reuse across rounds, or candidate-selection uncertainty (pp. 18, 23).

There is no separate development set for prompt choice. The test sets remain nominally held out, but prompt-selection optimism inside training is unquantified, and the release contains no run manifests to verify the boundary.

### 3. Data and configured systems

The main evaluations use:

- **AppWorld:** 90 official training tasks for optimization/distillation and all 168 `test-normal` tasks for evaluation; simulated apps/users and executable task-completion scoring (pp. 6, 16).
- **OfficeBench:** OCR tasks removed; 187 remaining tasks randomly split 92/95, stratified by one/two/three-app difficulty, with synthetic testbed files kept disjoint (pp. 16–17; released `split_tasks.py` uses seed 42).
- **8-objective QA:** 100 train and 100 test groups, each formed from eight NaturalQuestions items; BM25 retrieval over a 2018 Wikipedia index; EM/F1 scoring (pp. 6, 17).
- **WebVoyager appendix:** 50 optimization and 70 held-out tasks (pp. 19–20).

The principal agent and compressor are GPT-4.1. Additional cells use GPT-4.1-mini and GPT-5-chat; distilled Qwen3-14B/8B and Phi-4 compressors use one teacher generation per example, LoRA, and 100 examples per domain at most (pp. 7–8, 18, 22–25). All agents are ReAct-style, but benchmark adapters, tool formats, state resets, and graders differ.

“Model-agnostic” is architectural, not empirical. The paper itself limits broad foundation-model generalization, and the evidence is dominated by OpenAI agent/compressor/optimizer combinations (pp. 9, 16).

### 4. Measurements and results

The paper reports benchmark reward plus:

- **steps**;
- **peak input tokens**, excluding static system prompts;
- **dependency**, a token-based approximation to cumulative action-generation computation;
- estimated API price;
- one median wall-clock latency measurement setting (pp. 6, 8–9, 17).

Selected reported results:

- GPT-4.1 history ACON-UTCO on AppWorld: 56.5% versus 56.0% no compression, with peak tokens 7.33k versus 9.93k (Table 1, p. 6).
- GPT-4.1 history ACON-UT on OfficeBench: 74.74% versus 76.84%, with peak 4.93k versus 7.27k; it does not preserve the no-compression score (Table 2, p. 7).
- On 8-objective QA, ACON variants reduce peak/dependency substantially, but no one variant dominates both EM/F1 and efficiency; history UT improves F1 over no compression while EM is similar, whereas UTCO is lower (Table 2, p. 7).
- Combined history+observation compression lowers tokens further but degrades AppWorld accuracy to 45.8%/44.6% from 56.0% (Table 14, p. 25).
- On GPT-5-chat AppWorld, history ACON-UT/UTCO score 58.3%/62.5% versus 66.7% uncompressed; observation UT reaches 65.5% (Table 12, p. 24).
- End-to-end estimated API cost falls from $0.331 to $0.285/$0.272 per AppWorld task, while measured median latency rises from 73.24 seconds to 87.68/101.92 seconds (Table 4, p. 9).

These are useful trade-off observations, not uniformly improved task success. Abstract/contribution language that ACON improves task success over baselines is true against many compression baselines but can obscure degradation against full context in several configurations.

No confidence intervals, repeated attempts, paired tests, task-clustered uncertainty, invalid-run policy, or multiplicity correction are reported. On 95 OfficeBench tasks, differences of one or two successes can move the displayed percentage by roughly one or two points; without paired outcomes the significance and failure concentration are unknown.

### 5. Distillation

The teacher generates compressed outputs only from tasks it succeeds on, and students clone those outputs (pp. 5, 18). This conditions supervision on teacher success and teaches surface compression behavior rather than verified invariant preservation. Figure 4 supports that some small compressors retain much of teacher-compressor downstream performance for the fixed GPT-4.1 agent. It does not establish semantic equivalence, calibrated omission, or transfer to unseen task families.

The “small agent” result is more bundled. Figure 5 describes Qwen3-14B agents distilled from GPT-4.1 trajectories and combined with distilled compressors (pp. 8, 18–19). The comparison is therefore not solely the causal effect of context compression on an otherwise fixed small agent unless all agent-training data and conditions are matched. Claims that ACON itself yields the full 20–46% gain need this distinction.

## The paper's own examples falsify a strong fidelity claim

The most important audit finding is not a missing metric; it is visible corruption in the published qualitative evidence.

1. **AppWorld date/modality drift.** Compression D.1 starts with the task “Splitwise group invitations over phone text messages yesterday” (p. 44). The UT summary correctly records text messages on 2023-05-17 (pp. 45–46). The UTCO summary changes them to **voice messages from the day before yesterday (2023-05-16)** and changes the user/context to Sierra (p. 46). This is not harmless shortening; it alters modality, valid time, and subject while the prompt says never to invent or alter state variables.
2. **QA answer corruption.** Compression D.2's prompting baseline says the last Dodgers–Yankees World Series was 1981 (p. 47). The UT summary changes the answer to 1955, and UTCO changes it again to 1956 (pp. 47–48). Regardless of which answer is correct, the summaries are not faithful transformations of the displayed source history.
3. **Credential truncation conflict.** UTCO rules say long credentials may become `<token>` unless verbatim reuse is required, while the next session may require the literal token (pp. 31–33). The paper's successful AppWorld example visibly relies on reusing an access token after reset (pp. 41–44). The policy delegates a security- and executability-critical decision to an unverified language model.
4. **Observation output labeling drift.** The final appendix labels an observation-compression UTCO output as “History Compression” (p. 56), a minor documentation defect but further evidence that artifact identity is not tightly controlled.

Terminal success can miss all of these corruptions if the changed fact is not later queried, the agent recovers, or the grader checks only the final state. A compressor can improve average reward while becoming a worse audit record.

## Unique insight

ACON's genuine insight is that compression should be optimized against **downstream consequences**, not generic lexical similarity. For `skill-bench`, the necessary repair is to make consequences plural and fail-closed:

```text
raw evidence/state
→ versioned compression event
→ retained/omitted/transformed claims
→ invariant and authority checks
→ downstream action
→ artifact/state consequence
→ benchmark score
→ bounded validity claim
```

The central distinction is:

> **Task-sufficient compression is not state-faithful compression.**

A record may be sufficient for one realized trajectory yet unsafe for alternate valid actions, later audit, a changed request, error recovery, or downstream reviewers. Conversely, removing an agent's mistaken reasoning may improve performance even though the summary is less historically faithful. `skill-bench` should measure at least three separate constructs:

1. **decision sufficiency** for the next action and viable alternatives;
2. **state/evidence fidelity** to authoritative facts, provenance, uncertainty, contradictions, valid time, commitments, and artifact state;
3. **efficiency consequence** in tokens, cost, latency, calls, and completion quality.

No weighted sum should silently turn one into another.

## Evidence and claim boundaries

### Strongly supported

1. ACON is an implementable prompt-level method for history and observation compression without changing the proprietary agent model.
2. In the reported configurations, optimized prompts usually improve reward over naive generative-compression prompts while reducing peak dynamic-context tokens relative to no compression.
3. UT and CO expose a real reward–compression trade-off; additional or combined compression can materially hurt accuracy.
4. Compressor calls reduce estimated token price in the reported AppWorld setup but add wall-clock latency.
5. The official release exposes substantial runner, prompt-optimizer, compressor, task, and evaluation code for inspection.

### Partially supported

- **Generalization:** held-out tasks across several benchmark families and some agent models provide within-family evidence, but guidelines are domain-specific, most configurations use OpenAI models, and no cross-family zero-shot matrix is reported.
- **Distillation:** downstream performance often remains close for selected small compressors, but only task-success-filtered teacher outputs, one generation, and no fidelity labels are used.
- **Improved decision quality:** some fixed benchmark scores improve, especially for smaller agents, but session reset, instruction refresh, agent distillation, and removal of prior reasoning are bundled with compression.
- **Efficiency:** peak tokens and estimated API price improve, but system prompts are excluded, compression generation has its own compute, history rewriting invalidates KV cache, and latency worsens.

### Not supported

- faithful preservation of all decision-relevant or audit-relevant state;
- preservation of provenance, source authority, uncertainty, contradictions, valid-time intervals, commitments, or alternative-action requirements;
- causal attribution of failures or gains to omitted information rather than stochastic runs and reset/reformatting effects;
- reliability across repeated attempts;
- broad model-, agent-, harness-, or task-family agnosticism;
- professional artifact quality or workflow validity;
- production fitness, safety, or deployment readiness;
- exact reproduction of v3 results from the inspected repository revision.

## Limitations

1. The optimization objective is instantiated heuristically; natural-language prompt search has no convergence guarantee (paper p. 16).
2. Baseline/compressed contrasts use single stochastic trajectories and do not replay alleged causes.
3. Outcome-conditioned regression selection excludes silent corruption and shared failure.
4. Candidate prompts are selected on under-specified training subsets without selection-aware uncertainty.
5. No dedicated development split or published split manifest is provided for prompt selection.
6. No direct compression-fidelity labels, contradiction checks, entity/time tracking, or provenance checks are evaluated.
7. Published examples contain material date, modality, subject, and answer drift.
8. Terminal task reward observes only benchmark-scored consequences and may miss latent corruption.
9. History treatment bundles compression, session reset, instruction refresh, recency, and prior-reasoning removal.
10. Observation and history compression are mostly evaluated separately; combining them substantially degrades performance.
11. Thresholds are benchmark-specific and selected from AppWorld ablations without uncertainty.
12. The paper reports point estimates only; no repeated-run or paired-task uncertainty is supplied.
13. Fixed seed and temperature zero do not make proprietary API trajectories deterministic, as the authors acknowledge.
14. “Dependency” is a token-count proxy, not measured compute, KV-cache memory, energy, or price.
15. Peak tokens exclude static system prompts and do not include all optimizer-training costs.
16. API costs use historical list prices and a proxy price for Qwen3-14B; local hardware cost is not measured.
17. Latency comparison changes execution mode and reports medians without dispersion.
18. Distillation uses only teacher-success data, one output per input, 100 examples per domain, and no fidelity supervision.
19. Small-agent gains combine agent distillation and compressor interventions.
20. OfficeBench is author-split after ambiguity filtering; exact removal criteria and full paper-time split manifest are absent.
21. WebVoyager results add domain breadth but no repeated-run or live-web temporal controls.
22. Controlled benchmarks do not establish in-the-wild behavior; the authors acknowledge this (p. 16).
23. The release has no tracked trajectories, result tables, prompt-selection outputs, or paper-time manifests.
24. Upstream AppWorld data and QA retrieval corpora require separate downloads.
25. The inspected commit is neither tagged nor pinned by the paper and cannot establish v3 code identity.

## Reproducibility and operational realism

Reproducibility is **moderate at the mechanism layer and weak at the result layer**. The official tree contains 128 Python files, 16 YAML files, 300 OfficeBench task JSON files, executable benchmark adapters, compressor implementations, prompt optimization, and distillation scripts. Thresholds, prompt templates, model snapshots, seed, temperature, and training hyperparameters are described in the paper (pp. 17–18). The implementation logs LLM sessions, environment history, optimizer history, alignment, results, and token usage when runs are executed.

However, the repository contains no tracked outputs, trajectories, result summaries, optimized-prompt selection records, or paper-time configuration manifest. AppWorld data and the Wikipedia retriever corpus are external; proprietary model snapshots and Azure behavior are not reconstructible indefinitely. README examples contain stale-looking paths such as `configs/context_opt/appworld/gpt-4.1_history_v2.yaml` that are absent from the inspected tree, while present configs use shorter paths. The paper's “held-out subset” candidate-selection rule is not represented by an immutable released manifest. An independent result reproduction was therefore not possible from the release alone.

Operational realism is mixed. AppWorld and OfficeBench exercise multi-application state, file operations, authentication, and long trajectories; QA exercises evidence accumulation. Yet all are controlled, the compression policy is optimized per benchmark, and final reward does not test handoff quality, auditability, later task changes, organizational provenance, or severe-loss consequences. A summary that changes “yesterday text messages” into “day-before-yesterday voice messages” would be unacceptable in many professional workflows even if the current task happened to pass.

## Transfer to skill-bench

### Retain

1. **Treat compression as a separately versioned configured-system component.** Record compressor model, prompt hash, threshold, trigger, retained-turn policy, reset/accumulate rule, and optimizer-training data boundary.
2. **Use contrastive failures diagnostically.** Compare raw and compressed trajectories to generate candidate causes, but label LLM attribution as a hypothesis until replay or intervention confirms it.
3. **Keep reward and efficiency separate.** Report task quality, peak context, cumulative input/output, compressor calls, cost, latency, and invalid runs independently.
4. **Test both history and observation pathways.** They have different fidelity risks: history rewrites accumulated state; observation compression can destroy source content before it is ever preserved.
5. **Preserve raw traces.** Compression should never overwrite the authoritative audit trail.

### Repair

1. **Add compression-event lineage:** raw input hash, previous summary hash, compressed output hash, trigger, model/prompt/config hashes, included source spans, declared omissions, and downstream dependents.
2. **Define typed invariants:** entity/value, units, polarity, modality, authority, provenance locator, valid time, uncertainty, contradiction status, commitment, artifact path/state, required literals, and security-sensitive values.
3. **Use asymmetric loss severity.** Dropping redundant prose is not equivalent to changing a deadline, source authority, account, amount, consent boundary, or unresolved contradiction.
4. **Test alternate futures.** After compression, probe not only the realized next action but also valid alternative actions, request revisions, audit questions, recovery, and delayed handoff.
5. **Factor the treatment:** full context; session reset without compression; structured reformat without omission; compression without reset where feasible; and full ACON. This separates information loss from instruction recency and de-anchoring.
6. **Replay causal hypotheses.** Restore one allegedly omitted fact into the same compressed state and test whether behavior changes under repeated seeds; do not call trajectory comparison causal by itself.
7. **Separate fidelity from sufficiency.** A summary may pass a next-action probe while failing historical truth, provenance, or audit requirements.
8. **Fail closed for secrets and required literals.** Never substitute `<token>` when executable continuation requires the literal; use secure references/handles with availability checks rather than model judgment alone.
9. **Predeclare prompt-selection splits.** Freeze optimization, selection, calibration, and final test tasks; record all candidate prompts and outcomes to quantify search optimism.
10. **Use repeated paired trials and clustered uncertainty.** Compression policy comparisons should share task/environment seeds and report task-level paired effects plus invalid-run and latency distributions.

## Concrete next actions

1. **Add one nonduplicate build task:** create a compact compression-fidelity conformance slice using existing benchmark-bundle, trace, artifact-state, metric, and validity machinery rather than a new subsystem. Plant the exact high-severity corruptions exposed here—entity, modality, valid-time, answer/value, provenance, contradiction, required literal, and artifact-state drift—and require separate fidelity, next-action sufficiency, and efficiency outcomes.
2. In the next context/longitudinal consolidation, explicitly classify compression as a lossy state-transition event whose output cannot become authoritative evidence merely because a task passed.
3. For any future longitudinal pilot, retain immutable raw context outside the agent-visible window and link every compressed claim back to source spans; evaluators should be able to diagnose omission versus hallucination versus stale-state retention.
4. Before claiming a compression benefit, run the reset/reformat/compress factorial and repeated paired trials. A selected single-run package comparison is not a compression-quality estimate.

## Action items

- [x] Read the complete immutable arXiv v3 paper, including all appendices and qualitative examples.
- [x] Pin and inspect the official repository with paper/release timing boundaries.
- [x] Reconstruct observation/history compression, UT/CO optimization, selection, distillation, benchmarks, metrics, and configured systems.
- [x] Audit state fidelity, leakage/selection boundaries, uncertainty, operational cost, and claim ceilings.
- [x] Identify published qualitative state corruption and map it to benchmark checks.
- [ ] Build and execute the compression-fidelity conformance slice before adopting compression in a scored benchmark runner.
