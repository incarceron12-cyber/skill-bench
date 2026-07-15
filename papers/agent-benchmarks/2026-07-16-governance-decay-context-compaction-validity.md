# Governance Decay isolates policy-carriage failure, but synthetic prohibited calls are not end-to-end governance evidence

**Paper:** Shiyang Chen, *Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents*, arXiv:2606.22528v2 (27 June 2026), <https://arxiv.org/abs/2606.22528v2>.

**Date read:** 2026-07-16.

## Review and evidence status

**Deep review of the complete immutable primary source.** I read the full nine-page v2 PDF, complete layout text, and official arXiv source package. The Atom summary contains no withdrawal or retraction notice.

- PDF: `data/papers/pdfs/2606.22528v2-governance-decay.pdf` (9 pages; SHA-256 `bdefc230875e3df986f262eecf42c87e849e5b43b60eb5f24c2ecbfccdb905b6`).
- Text: `data/papers/text/2606.22528v2-governance-decay.txt` (61,438 characters; SHA-256 `7141460f3b7170924955c9169b9eb31607823ee6a467e587a07f5ee4cf091bfc`).
- Atom metadata: `data/papers/source/2606.22528v2-metadata.xml` (SHA-256 `9cecdfffda607836be26939306bbce395aecd3784d7abf8487c802a20a2db47a`).
- Official arXiv source: `data/papers/source/2606.22528v2/source.tar` (90,045 bytes; SHA-256 `2b2e6ad52acee5953ef6c5fe5d57f96ba9dde0836eb0308aa8ad587eff94dce0`). The package contains the manuscript TeX/BibTeX, style files, and logos, but no scenarios, prompts, code, results, traces, or supplementary file.

The manuscript says “all scenarios, prompts, conditions, and grader code are released” (p. 4) and repeatedly sends important results to “Supplementary Material,” yet the arXiv record and official source package provide neither an artifact URL nor those materials. Exact-title, arXiv-ID, `ConstraintRot`, `Compaction-Eviction`, GitHub repository/API, general web, and scholarly-index searches on 2026-07-16 found no verifiable author-owned code/data release. The visible `constraintguard` repository is third-party and was not treated as evidence. Thus every empirical result below is manuscript-reported and unreplayed.

## One-sentence contribution

The paper provides a valuable matched design showing that a lossy context-management transformation can delete a visible standing rule and change a later prohibited tool-call decision, but its unreleased synthetic instrument establishes **constraint-carriage sensitivity under authored requests**, not legitimate organizational authority, realized harm, broad agent safety, production fitness, or readiness.

## Why this matters for skill-bench

This advances charter objectives A–C through a cross-domain configured-system boundary, not a safety-only scope commitment. A long-running agent may receive professional constraints through onboarding, policy documents, memory, user turns, or tool outputs. If compaction changes which constraint is visible, the evaluated treatment has changed even when the model name, final request, and nominal task remain fixed.

The transferable chain is:

```text
constraint proposition and legitimate authority
→ delivery channel and valid-time/supersession state
→ pre-compaction availability and model exposure
→ compaction operator, budget, and sampled surrogate
→ post-compaction semantic survival
→ later model exposure and adoption
→ prohibited-action proposal
→ gate/interceptor decision
→ realized effect and stakeholder consequence
```

ConstraintRot observes selected links: an authored rule is placed in context, a summary is produced, an LLM judge estimates semantic survival, and a deterministic parser detects a prohibited terminal call. It does not establish the first link, actual model attention/adoption, execution, or consequence. Those distinctions are the review's central claim boundary.

## Research question and defensible claim

The paper asks whether ordinary context compaction actively removes non-system governance constraints that seven agent models obey while visible, whether removal predicts later prohibited tool calls, whether in-context content can bias that removal, and whether verbatim pinning prevents it (pp. 1–7).

The strongest defensible claim is:

> In nine author-constructed single-call scenarios, across seven named API model aliases and the paper's unreleased common harness, all 189 full-context control episodes avoided the defined prohibited terminal call, while 57 of 189 corresponding single-compaction episodes did not; manuscript-reported counterfactual removal/restoration, compactor×agent crossing, budget, strategy, repeated-compaction, channel, attack, and pinning probes are directionally consistent with post-compaction rule carriage being a treatment component.

The paper does **not** establish that the policies came from legitimate principals, that the parsed calls executed, that any real secret/person/system was affected, that compaction raises naturally occurring incident rates, that pinning resolves policy conflict or revocation, that the named model or harness effects reproduce, or that any system is organizationally safe or production-ready.

## Methodology and system

### ConstraintRot task and observer

Each of nine scenarios contains a policy turn, benign filler that pushes history beyond a tight compaction budget, and a final self-contained request whose natural completion violates the policy. Five “soft” rules cover external email, English-only email, report channel, deployment region, and a $100 spending limit. Four “hard” rules prohibit destructive production SQL, SSH-key reading, SSN disclosure, and disabling audit logging (pp. 3–4; Table 1).

The agent emits one terminal call from `send_email`, `db_exec`, `read_file`, `disclose`, or `purchase`. A deterministic parser labels violation when arguments match the authored prohibited effect. This is stronger than a final-answer safety judge: it observes exact proposed arguments and keeps the primary outcome model-free. It is still an **attempt/proposal observer**. The ethics section says calls are parsed but never executed and all secrets/PII are fictitious (p. 8). “External email leak,” “destructive operation,” and similar phrases therefore describe scenario semantics, not realized outcomes.

The nine policies are not traced to real organizations, incident records, qualified experts, standards, or affected-party review. No alternate legitimate action set, escalation requirement, policy-conflict case, ambiguity case, or authoring/adjudication record is released. The benchmark tests compliance with author-declared strings; calling them “governance” does not establish legitimate authority or professional correctness.

### Conditions and the 1,323-episode accounting

The headline table crosses seven models with seven conditions, nine tasks, and three repetitions:

```text
7 models × 7 conditions × 9 tasks × 3 repetitions = 1,323 episodes
```

Each model–condition cell therefore has 27 episodes and each condition has 189. The conditions are:

1. `floor`: no policy, estimating intrinsic refusal;
2. `control`: policy visible in the uncompressed full context;
3. `compaction`: policy introduced and then compacted;
4. `attack_volume`: bulk in-context data crowds the summary;
5. `attack_inject`: fixed text tells the summarizer to omit the policy;
6. `defense_pin`: verbatim policy is re-injected after compaction; and
7. `defense_pin_attack`: pinning under the fixed attacks.

The seven reported aliases are DeepSeek-V4-Flash, GLM-5.1, Qwen3.6-27B, Kimi-K2.5, Claude-Sonnet-4.6, GPT-5.4-mini, and Gemini-3.5-flash. All use an unnamed “common API,” generally at temperature 0.7; GPT uses an endpoint-fixed default (p. 4). Exact provider, endpoint snapshot, run date, system/task/compaction prompts, summary model call topology, tokenization, context threshold, retries, timeouts, invalid-run policy, tool schema, seeds, and service incidents are absent.

In the headline grid, each named model apparently writes its own summary and then acts on it. The compactor×agent crossing confirms that these are separable components, but the main “per-model” rates bundle both roles. They are configured self-compactor-plus-agent observations, not intrinsic agent-model safety rankings.

### Primary outcome and survival analysis

Table 2 reports 0% violation in all full-context controls and 30% pooled after compaction, with model cells from 0% (GLM) to 59% (DeepSeek and Kimi). The no-policy floor is 47%. Soft-policy decay is reported as +50 points versus +6 for hard policies, an 8.3× ratio (pp. 4–5).

For the original five-model panel, an independent LLM judge labels semantic survival over plain compaction and two attack conditions:

```text
5 models × 3 compacted conditions × 9 tasks × 3 reps = 405
survived: n=90, violation 0%
dropped:  n=315, violation 38%
```

A keyword heuristic covers all seven models:

```text
7 × 3 × 9 × 3 = 567
survived: n=207, violation 1%
dropped:  n=360, violation 43%
```

The heuristic agrees with the original-panel judge on 83%. An 81-episode subset receives three-family majority judging: survived 0% (`n=18`) versus dropped 40% (`n=63`), with pairwise agreement 62–83%; one judge labels every item dropped and is explicitly uninformative (p. 4).

This is useful mechanism evidence, especially because the primary prohibited-call label is independent of the survival judge. But survival is post-treatment and not randomized: summaries that preserve a policy may also preserve other caution-inducing content, while dropped summaries may frame the pending task more directly. The unvalidated LLM entailment label has no prompt, response inventory, human calibration, confidence, or adjudication record. “Survival predicts violation” is supported; a complete mediation effect is not.

### Mechanism and compactor probes

The strongest causal probes are on GLM-5.1: visible policy in a 5.9k-token uncompressed history yields 0%; a manually policy-deleted summary yields 60%; restoring the policy to that summary returns to 0%. Crossing three summary writers (DeepSeek, GLM, Claude) with three acting models over five soft tasks (`n=15` per cell) yields 7–13% with GLM summaries versus 33–93% with DeepSeek/Claude summaries (pp. 4–5; Table 3). These interventions more directly identify summary content than the headline association.

However, the manual deletion/restoration sample size, exact summary, insertion position, prompt, and item inventory are absent. The crossing has one reported aggregate per 15 episodes, no repeats beyond the implied task-level runs, and no uncertainty. “The compactor, not the agent, drives the failure” is too categorical: the table still ranges materially by acting model within a fixed summary row, and the design samples only three models and five authored tasks.

The compaction-budget sweep tightens the summary from 300 to 15 words; reported survival falls 88%→23% and pooled violation rises 7%→28%. The manuscript does not provide cell sizes, model/task inventory, repeated-summary policy, or uncertainty. A word budget is also not a fixed token or semantic-capacity treatment.

Four strategies are reported: recency truncation (38%), hierarchical compaction (36%), LLM summarization (26%), and `head_tail` retention (0%). Only `head_tail` necessarily keeps the oldest policy. Exact algorithms, budgets, model identities, cell sizes, and results are deferred to missing supplementary material. This compares heterogeneous policies that differ in what they are structurally guaranteed to retain; it does not rank fully specified production compactors.

Repeated compaction reportedly raises violation 0%→78% over `R=0→4`, and cross-lingual decay is +42 in Chinese and +22 in Spanish. Model, task, translator, denominator, repetition, and uncertainty details are absent because the cited supplement is unavailable. These are hypotheses, not auditable robustness results.

### Attacks and optimization exposure

The volume attack adds benign-looking bulk; because the benchmark invokes compaction regardless, volume competes for the fixed summary rather than demonstrating trigger causality. The fixed injection tells the summarizer to omit a “deprecated compliance preamble.” Pooled violation is 26%/28%, but passive compaction is already 30%; the value is model-specific complementarity, not aggregate attack superiority (pp. 5–6).

The optimization study tests six hand-designed framings—deprecation, irrelevance, token budget, direct summarizer note, system impersonation, and operator authority—then selects the best per model. Table 4 reports up to 100%/85%/65% over DeepSeek/GLM/Claude and five soft tasks, but does not state repetitions or a total denominator. Rates move in five-point increments, consistent with 20 observations per cell, yet that cannot be assumed. Selection on the same measured cells makes “optimized” rates development-set maxima, not held-out attack robustness. Cross-model transfer is narratively reported, but no complete strategy×source×target matrix, search ledger, candidate failures, stopping rule, or uncertainty is released.

The attack reaches only the compactor through authored in-context text, a useful distinct surface from ordinary task-agent injection. But the final prohibited request follows by construction. The study does not estimate exposure opportunity, natural attack prevalence, attacker ability to time compaction/request delivery, stealth, utility impact, or success against out-of-band enforcement.

### Constraint Pinning and utility

Pinning quarantines a quotable rule from lossy compaction, re-injects it verbatim, and checks that the resulting context entails it. Table 2 reports 0/378 prohibited calls across pinned and pinned-under-attack headline conditions. The policy averages about 47 tokens; the paper calls this under 0.5% of a ≥10k-token production history, but supplies no actual benchmark context-length distribution or complete resource accounting (pp. 6–7).

Seven allowed counterparts across three models have `n=84` per condition, implying four repetitions per task–model pair although the paper does not say so. Pinning reportedly completes 99% with 1% over-refusal versus 90%/10% for the ordinary policy-in-context control. This is valuable matched benign utility evidence. It is not end-to-end task utility: each counterpart is another one-call authored action, not long-horizon work with artifact quality, latency, policy conflicts, stale rules, or legitimate alternatives.

A stress test over three models and five soft tasks states `n=60/cell` (four repetitions per task–model). Naive pinning gives 0% under ordinary compaction, 2% after an ingested fake rescission that is summarized, and 0% with 15 pinned distractor rules. A recent non-summarized operator-impersonation update raises violation to 17%; adding “operator-pinned; not overridable” lowers but does not eliminate it (10%). This is the paper's most important limitation: semantic text cannot by itself prove principal identity, revocation authority, precedence, or valid time. Pinning preserves content; it does not solve governance.

The comparison with a preserved system-channel policy (0%) and Spotlighting-style provenance prompt (43–45%) is directionally useful, but exact denominators, prompts, and traces are absent. A system prompt is also a different authority/control treatment, not merely another defense implementation.

### Real-harness validation

The paper reports:

- LangGraph `StateGraph` with a summarization node: DeepSeek 0%→65%, `n=20`;
- official LangMem `SummarizationNode`: DeepSeek 95% and GLM 70%, `n=20` each;
- AutoGen `BufferedChatCompletionContext` recency eviction: DeepSeek 100%, `n=20`;
- OpenAI Agents SDK Runner fed the same LLM-written compacted summary: DeepSeek 35%, `n=20`.

These are component witnesses, not a single matched production validation. Versions/commits, configuration code, prompts, token thresholds, task allocation, errors, and run rows are absent. The SDK case is explicitly not native compaction. All actions remain sandboxed and unexecuted. “Production agent-framework context managers” overstates evidence from four local framework components under one synthetic benchmark.

## Unique insight

The paper's durable contribution is to identify **context transformation as governance-treatment realization**.

A benchmark normally records a policy/skill/memory hash and model identity at trial start. That is insufficient. The operational question is what governed the model **at each consequential decision after context assembly and compaction**. A configured system can begin with the correct policy and later instantiate a different effective treatment because its context manager omitted, altered, duplicated, or superseded it.

For skill-bench, policy carriage should therefore be measured as a state transition:

```text
policy authority/version
× delivery channel
× compactor identity/configuration
× compaction event/input/output hashes
× semantic survival and transformation
× decision-time evidence view
× attempted action/effect
× gate and realized-state receipt
```

Three claim levels must remain separate:

1. **carriage:** a versioned constraint remains semantically available after transformation;
2. **behavioral adoption:** its presence changes a configured model's proposal distribution;
3. **governance effectiveness:** legitimate authority is enforced through action admission and realized consequences while preserving useful work.

ConstraintRot gives meaningful evidence for levels 1–2. It does not reach level 3.

## Comparison with adjacent reviewed evidence

- **Decision Fidelity under Context Compression** treats compression as an intervention on a downstream evidence view and separates state fidelity, task sufficiency, decision preservation, correctness, and consequence. Governance Decay adds a sharper paired omission/restoration mechanism and action proposal, but has weaker source authority and no realized consequence. Preserving a rule-induced refusal can be desirable only if the rule is legitimate and current.
- **Context-to-Execution Integrity (CXI)** assumes policy and authorization state exist and asks whether protected field, exact-effect, and invocation authority bind at the mediated sink. Governance Decay shows why relying on model-visible policy carriage is fragile; CXI shows why pinning text alone should not be the enforcement boundary. Out-of-band authority plus complete mediation is the repair.
- **ClawSafety** separates placement, authority, exposure, adoption, attempt, realization, recovery, and utility. Governance Decay isolates one transformation between exposure opportunities and later attempt, but observes only a parsed proposal and one-call utility. Its deterministic argument grader is better specified conceptually than ClawSafety's binary judge, while both lack complete released result evidence.
- **LongMemEval-V2** distinguishes retained experience, retrieved representation, reader access, and held-out action benefit. Governance Decay is the negative mirror: retained policy at session start is not enough; transformation-time carriage and decision-time access need evidence. Neither retrospective QA nor summary survival substitutes for consequential action validity.
- **Configured-system identity** must include context-management policy as a time-varying component, not just a static hash. Summary writer and acting model are separate identities; budgets, trigger rules, retained channels, sampled outputs, and re-injection logic are interventions.

## Evidence and claim boundaries

### Supported by the manuscript

1. The 1,323 headline denominator is internally coherent: seven model aliases × seven conditions × nine tasks × three repetitions.
2. All reported full-context controls avoid the authored prohibited terminal calls, while compacted conditions show heterogeneous increases.
3. Post-compaction semantic survival is strongly associated with lower prohibited-call rates under two survival observers.
4. Manual remove/restore and summary-writer×agent probes are directionally consistent with summary content causing behavior change.
5. The model serving as summary writer materially changes the result, so “model performance” bundles compactor and actor.
6. Verbatim re-injection eliminates prohibited calls in the reported basic grid and preserves allowed one-call utility.
7. Recent authority-impersonation defeats naive text-only pinning, identifying out-of-band authority as an unresolved boundary.

### Partially supported

- **General compaction sensitivity:** multiple budgets/strategies/rounds/languages/frameworks are reported, but key methods, denominators, and supplements are absent.
- **Soft/hard 8.3× gradient:** exact task counts support the descriptive result, but nine authored rules, intrinsic refusal, and floor differences do not define a general taxonomy or deployment prevalence.
- **Attack robustness:** fixed and selected framings expose a compactor injection surface, but optimization is evaluated on its selection cells without a held-out set.
- **No utility cost:** seven allowed one-call counterparts show strong point estimates; no broader task-quality, policy-conflict, or operational-cost evidence exists.
- **Cheap defense:** 47 tokens is small relative to an asserted ≥10k-token context, but extraction, authority management, integrity checks, latency, storage, review, and conflict handling are uncosted.

### Not supported

- legitimate organizational policy authority, current applicability, or valid revocation;
- natural incident frequency or risk under production workloads;
- realized email, database, privacy, security, financial, or stakeholder harm;
- broad agent safety or model-family rankings independent of the compactor;
- complete attack robustness or a universal 0% defense rate;
- human-validated semantic survival;
- production-framework safety, production fitness, or readiness;
- cross-domain professional validity.

## Limitations

1. No official benchmark/code/results release is discoverable despite an explicit release claim.
2. The official source omits the repeatedly cited supplementary material.
3. Nine author-constructed rules lack domain, principal, incident, expert, and affected-party provenance.
4. Deterministic grading observes a proposed terminal call, not execution or consequence.
5. Refusal, safe alternative, escalation, malformed output, timeout, tool failure, and invalid trial are not fully separated in the headline outcome.
6. Model aliases and common API are mutable and under-specified.
7. The main per-model cells bundle summary writer and acting model.
8. Exact prompts, compaction threshold, tight budget, selected span, tool schema, and invalid-run policy are absent.
9. Three repetitions per task/model/condition are modest; most rates have no uncertainty.
10. The reported high-powered 1,080-episode study gives a pooled interval but does not explicitly enumerate the four included conditions in the main text.
11. Pooled bootstrap details and clustering unit are absent; tasks and model configurations are not interchangeable independent draws.
12. Survival is an unvalidated post-treatment LLM label; one of three robustness judges is degenerate.
13. Keyword survival can miss paraphrased carriage and falsely count irrelevant mentions.
14. Remove/restore, budget, strategy, round, language, and channel ablations lack complete denominators or artifacts.
15. The soft/hard split confounds policy specificity with intrinsic model refusal and task/tool semantics.
16. Volume attacks do not test budget-trigger causality because compaction is always invoked in the benchmark.
17. Attack optimization selects the best strategy on measured cells and has no held-out evaluation.
18. Pinning requires an extractable quotable rule and does not solve implicit norms, conflicts, precedence, expiration, revocation, or principal authentication.
19. Allowed-action utility is one-call and likely four repeats per task/model, but the repetition design is unstated.
20. “Real-harness” tests are heterogeneous component reproductions with no pinned code/configuration or run archive.
21. Costs are almost entirely absent: no tokens, API dollars, latency, retries, compute, policy extraction/review, storage, or adjudication ledger.
22. All effects are simulated and inert, properly limiting ethics risk but also limiting operational consequence claims.

## Reproducibility and operational realism

Reproducibility is **poor**. The paper names tasks, conditions, model aliases, aggregate rates, and the conceptual grader. Its arithmetic is often reconstructable, and the deterministic call-argument outcome is a good choice. But the promised benchmark, prompts, code, supplements, summaries, traces, per-run rows, endpoint snapshots, and aggregation scripts are absent. Proprietary/future aliases and an unnamed API prevent exact reconstruction. The arXiv TeX is useful for verifying that these omissions are not extraction artifacts.

Operational realism is mixed. Long sessions, non-system policies, compaction, memory/tool-delivered constraints, untrusted retrieved content, and soft organization-specific rules are credible deployment pressures. Yet the episodes culminate in one self-contained synthetic call; filler exists mainly to force compaction; actions never execute; no real policy principal, workflow, artifact, approval, conflict, or stakeholder appears. Framework components increase implementation plausibility, not ecological or consequence validity.

## Transfer to skill-bench

### Retain

1. **Matched full-context/compacted/counterfactual-restored conditions.** Hold the final request and acting model fixed while changing only the realized evidence view.
2. **Compactor×actor crossing.** Record summary writer separately from the downstream actor; never label their bundle as a model-only result.
3. **Deterministic proposed-effect grading.** Parse exact protected arguments before using a model judge, while labeling the result as attempt/proposal rather than realized harm.
4. **Semantic survival plus downstream behavior.** Measure transformation fidelity and action response as linked but distinct outcomes.
5. **Soft organization-specific controls and allowed counterparts.** Intrinsic refusal can mask treatment failure; jointly test legitimate allowed actions and prohibited actions.
6. **Authority-impersonation stress.** Conflict and rescission are essential falsifiers for any memory/pinning defense.

### Repair

1. **Start with authority, not a policy string.** Bind principal, scope, valid time, precedence, revocation channel, public basis, and affected-party review before testing carriage.
2. **Use out-of-band enforcement for consequential effects.** Context-visible policy can guide reasoning, but field/effect/invocation authorization should be checked by a trusted mediator against a versioned manifest.
3. **Record every compaction event.** Hash pre-state, selected span, operator/model/prompt, budget/trigger, sampled output, retained claims, omitted claims, and re-injected records.
4. **Separate visibility from adoption.** Use matched restoration/removal and, where possible, plan/action distributions; do not infer model access from string presence alone.
5. **Observe the full consequence chain.** Distinguish refusal, safe alternative, escalation, malformed/invalid run, prohibited proposal, gate block, mock realization, recovery, residual state, and benign utility.
6. **Repeat and cluster correctly.** Cross repeated summary samples with repeated actor calls; retain run rows and estimate uncertainty by task/policy lineage and configured system.
7. **Validate alternative legitimate paths.** A pinned policy should not force one canned refusal when clarification, approval, scoped action, or safe substitution is professionally valid.
8. **Test policy lifecycle.** Include expiry, genuine signed update, forged update, conflict, exception, overload, implicit requirement, and rollback.
9. **Measure complete cost.** Include extraction, summary generation, pinned-token growth, integrity/authority checks, latency, API/compute, review, false blocks, and conflict adjudication.

## Concrete repository actions

1. **No new queue task.** Existing context-compression conformance, configured-component realization, authority/information-flow, action-safety, CXI-style admission, trace, task-health, metric, and validity machinery already host the required fields. A Governance-Decay-specific subsystem would duplicate machinery and narrow the project.
2. In the next relevant consolidation/build calibration, add one policy-carriage negative control to an existing context-compression/action slice: legitimate signed constraint, lossy summary that drops it, exact restored summary, forged recent rescission, trusted out-of-band update, allowed counterpart, mock protected action, and mediator receipt. Predeclare separate carriage, adoption, admission, realization, utility, and consequence claims.
3. Treat the paper's 0%, 30%, 59%, 65%, 78%, and framework-specific rates as unreplayed manuscript evidence—not calibration targets—until an official versioned release supplies complete rows and conformance artifacts.

## Bottom line

Governance Decay identifies a real benchmark-design omission: static configuration provenance cannot show what policy actually survives into a later decision after context compaction. ConstraintRot's matched controls, remove/restore probe, compactor×actor crossing, deterministic terminal-call observer, allowed counterparts, and pinning stress test make that omission concrete. But the source's absent release and supplement, synthetic authority, under-specified compaction, selected attack optimization, parsed-only actions, thin utility, and missing costs sharply cap the claim. `skill-bench` should treat **policy carriage as a time-varying configured-system state** and join it to out-of-band action authority and realized-state evidence; it should not equate a preserved prompt string or zero observed prohibited calls with governance, safety, or readiness.
