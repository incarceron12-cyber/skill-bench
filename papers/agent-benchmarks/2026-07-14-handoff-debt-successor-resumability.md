# Paper Review: Handoff Debt — Resumability Is a State-and-Recipient Effect, Not a Property of Notes Alone

- **Paper:** https://arxiv.org/abs/2606.02875v1
- **Authors:** Dipesh KC and Anjila Budathoki
- **Date read:** 2026-07-14
- **Source:** complete immutable arXiv v1, submitted 1 June 2026
- **Local PDF:** `data/papers/pdfs/2606.02875v1-handoff-debt.pdf` (16 pages; SHA-256 `93b617f7a77b7aae6a50168a0925fce3004da0ca84df9b7718c4d1dba01bc11f`)
- **Local text:** `data/papers/text/2606.02875v1-handoff-debt.txt` (SHA-256 `f0cc217f273370a563bf181c21277ac5e2085b0457291596021f1f12d6878bc7`)
- **Full arXiv source:** `data/papers/source/2606.02875v1/`; archive `data/papers/source/2606.02875v1-source.tar.gz` (SHA-256 `a8c9a911a75ddd22735dfc9b46f991338e8d51fafa11aa22b9e9b9edec8e6556`)
- **Release provenance:** `data/sources/releases/2606.02875v1-handoff-debt/provenance.json`
- **Release status:** no verifiable author-owned empirical release was found at acquisition or review time; current searches returned the paper and third-party descriptions, not code, data, checkpoints, trajectories, payloads, or results
- **Tags:** successor-resumability, handoff-debt, frozen-checkpoints, efficiency-estimands, context-views, configured-systems

## One-sentence contribution

Handoff Debt introduces a useful matched takeover design that freezes an interrupted SWE-bench repository and varies what predecessor context a successor receives, providing credible configured-system evidence that context-bearing views can reduce post-handoff interaction under the tested runtime; however, its cost estimands mix rediscovery with outcome-dependent stopping, omit handoff-generation cost, treat nested checkpoints as independent, and do not establish that structured notes are faithful, professionally sufficient, human-valid, or generally causal.

## Why this matters for skill-bench

This paper studies a unit of knowledge work that endpoint-only benchmarks usually erase: a successor must continue from another worker's partially transformed state. That advances charter objectives A, B, and C without making coding the benchmark's scope. The reusable question is cross-domain:

> Given the same authoritative work state, how do the visible handoff record and receiving system change verification burden, continuation quality, and total lifecycle cost?

The design improves on a simple “artifact exists” check by holding the repository bytes and predecessor trajectory fixed within a handoff point while varying four views. It also separates final resolution from effort. Those are meaningful advances over evaluating only whether one uninterrupted agent eventually finishes.

The claim boundary is nevertheless narrow. The paper evaluates synthetic agent-to-agent succession over public coding tasks, one runtime family, three local model configurations, model-generated notes, and official test resolution. It does not observe human handoffs, professional documentation practice, downstream maintainability, organizational coordination, or consequences beyond tests. The result should inform a resumability protocol, not become evidence that agents collaborate like engineers or that a fixed note schema transfers to other professions.

## Research question and claim boundary

The paper asks which of four views—repository only, raw predecessor trace, free-form summary, or structured note—allows a successor to resume interrupted coding work correctly and efficiently (pp. 1–3).

The strongest defensible claim is:

> For the reported Qwen-predecessor checkpoints and fixed OpenHands-style successor configurations, adding selected predecessor-observable context is associated with fewer post-handoff agent events and cumulative prompt tokens than repository-only takeover, while official-resolution effects are smaller and successor-dependent.

The evidence does **not** establish that:

- the measured difference is purely rediscovery rather than different stopping/outcome distributions;
- structured notes dominate summaries or raw traces;
- the note schema faithfully preserves all decision- or audit-relevant state;
- generated notes reduce total system cost once generation and verification are included;
- continuation-state labels are available without hidden-evaluator leakage;
- results generalize to other checkpoints, predecessor policies, runtimes, task families, human successors, or professional work;
- lower takeover effort implies maintainability, safety, production fitness, or readiness.

## Methodology and system

### Benchmark construction and interruption rule

The study filters SWE-bench Verified to its 15-minute–1-hour and 1–4-hour tiers, fixes random order with seed `20260430`, and takes the first 75 tasks (pp. 4, 14). One Qwen predecessor trajectory per source task yields three observable checkpoint types:

1. first non-test source edit;
2. first validation/build/lint/test result after a source edit;
3. first source edit after the first failed validation.

Every selected run contributes the first two types; 31/75 contribute the third, giving 181 handoff points. The paper labels 110 as `Needs completion`, 61 as `Already solved; preserve`, and 10 as `Existing behavior broken` (pp. 2–4). Four views per point produce 724 runs per successor and 2,172 main takeover runs across Qwen, Gemma, and Devstral successors. These denominators are internally consistent.

Deterministic event boundaries are a strong design choice: checkpoint timing does not use the official solution, and all four views for a point start from the same repository. But “deterministic” is not the same as representative. First-edit and first-validation checkpoints are protocol-selected moments, not sampled interruption hazards from real work. The 31 post-failure checkpoints are available only when the predecessor follows a failure with another edit, making that stratum behavior-conditioned. Multiple checkpoints from the same issue and predecessor trajectory are nested, not 181 independent tasks.

The exact 75 task IDs, 181 checkpoint records, frozen repositories, and predecessor trajectories are not released. Consequently, the claims that every selected predecessor produced both early checkpoints, that all eligible points were retained, and that repository states were byte-equivalent across views cannot be independently replayed.

### Four handoff views

All successors receive a shared takeover instruction, original issue, and frozen repository. The intervention adds:

- **Repository only:** no explicit predecessor history.
- **Raw trace:** predecessor events through the checkpoint.
- **Summary notes:** a Qwen-generated free-form compression of predecessor-observable evidence.
- **Structured notes:** deterministic metadata plus model-generated fields.

The structured record covers changed source files, non-source artifacts, validation after the latest source change, latest validation command/evidence, continuation-state label, problem understanding, completed work, failures, uncertainty, rollback notes, and next action (Appendix C, pp. 15–16). Prompts appropriately tell successors to treat notes as historical evidence and verify them rather than trust them as ground truth.

This is not actually a released “full schema.” The appendix provides a prose field list and shortened generic example, but no machine-readable field names, types, null policy, authority markers, evidence locators, payloads from real tasks, or conformance rules. Nor does the study score summary/structured-note fidelity, omission, contradiction, source entailment, or successor reliance. The three manually reported failure modes—omitted exact evidence, over-trust, and raw-trace noise—have no sampling frame, coding protocol, frequency, agreement, or outcome linkage (p. 16).

A more serious ambiguity concerns `continuation-state label`. Handoff states such as `Already solved; preserve` are defined using official checkpoint resolution, while the structured note exposes that label as a deterministic field. The appendix says model-generated fields contain no hidden tests, but does not explain how the deterministic label is computed, whether official hidden validation contributes, or whether equivalent state information is available to the other views. If the label uses official evaluator knowledge, structured notes receive answer-bearing state unavailable to a real predecessor. If it uses only observed validation, the definitions and counts need that rule. The current paper does not close this boundary.

### Configured systems and execution

All conditions use local OpenAI-compatible vLLM endpoints, an OpenHands-style textual action protocol, disabled provider-native tool calling, a four-hour conversation timeout, and 500 agent steps. The named models are `Qwen/Qwen3.6-27B`, `google/gemma-4-31B-it`, and `mistralai/Devstral-Small-2-24B-Instruct-2512`; serving flags are reported, but context lengths are explicitly not shared across models (pp. 4, 14).

Within each successor, the runtime treatment is reasonably controlled. Cross-successor comparisons are descriptive because model context, tokenizer, behavior, and baseline cost differ. The paper correctly avoids a leaderboard interpretation. Still absent are an OpenHands commit, environment/container digests, SWE-bench harness version, dependency images, exact system prompt, action parser, event normalizer, token-accounting implementation, sampling parameters for takeover calls, retry/error policy, worker scheduling, and model artifact hashes. Local model names are better than mutable API labels, but they do not freeze the complete configured system.

The predecessor writes both summary and model-filled structured fields at temperature zero with a 1,600-token cap. This makes note authoring a separate model intervention. It is neither a human-authored documentation condition nor a passive transformation of the same trace.

### Outcomes, effort, and statistical analysis

Official SWE-bench resolution is the endpoint outcome. Post-handoff effort is measured as OpenHands trajectory events—LLM actions and tool observations—and cumulative prompt tokens (pp. 2, 4, 14). The main tables report one run per point/view/successor. Context-bearing views reduce displayed median events by 20–59% and prompt tokens by 42–63%; raw-trace solved-rate deltas range from +6.1 to +14.9 points (Tables 2–3, pp. 5–7).

The solved-count arithmetic is coherent. Reconstructing rounded counts from 181 runs gives, for example, Qwen→Qwen 84 repository-only versus 95 raw-trace solves, exactly matching the Table 6 discordant-pair difference `17−6=11`. All nine context-versus-repository discordant differences agree with the rounded rates.

The uncertainty analysis is weaker than the presentation suggests:

1. **Wrong independence unit.** Bootstrap and McNemar analyses operate on 181 handoff points, although points are nested within 75 source issues and share predecessor trajectories, prompts, repositories, and often overlapping state. Resampling handoffs understates task-level uncertainty when within-issue outcomes correlate.
2. **Point estimate and interval target different statistics.** Table 3 displays ratios of marginal event medians (for example 99→41, labeled −59%) but bootstraps matched run-level *relative reductions*. The Qwen→Qwen raw interval is `[−50%, −42%]`, which does not even contain the displayed −59% point. This pattern recurs across rows. The interval can show reductions are below zero, but it is not uncertainty around the headline median-ratio effect.
3. **No prompt-token uncertainty.** Prompt tokens are a primary metric, yet receive no confidence intervals.
4. **Inconsistent prompt-token tables.** Qwen context medians differ between Tables 2 and 3 despite both using all 181 matched points: raw trace is 811k versus 798k, summary 602k versus 572k, and structured 660k versus 646k. No alternate estimand explains the discrepancy.
5. **No multiplicity correction.** Nine solved-rate tests and multiple diagnostic comparisons are reported. The authors disclose this, but nominal `α=.05` language should remain descriptive.
6. **Single main attempt.** The 40-point repeated sensitivity uses three attempts and preserves aggregate event reductions, but it is purposively composed of 30 completion and 10 preservation points, provides no solved outcomes or repeat-aware uncertainty, and releases no IDs or runs.

Most importantly, unconditional event/token cost is not a pure rediscovery estimand. Runs can stop because they solve, decide an already-correct state needs no change, fail, or hit the four-hour/500-step cap. Views also change solved rates. A lower median can reflect better information, early confident preservation, earlier failure, or a shifted mix of terminal outcomes. The paper does not report time-to-resolution with unsolved runs censored, costs stratified by matched terminal outcome, repeated inspection/validation events, or successor action categories. Calling every difference “rediscovery cost” therefore over-identifies the mechanism.

Finally, note-generation events/tokens and preprocessing are excluded by design. Cumulative successor prompt tokens do include the enlarged initial view—raw trace has median 87k initial characters versus roughly 10k for notes—but summary construction itself is free in the reported accounting (pp. 5, 12, 14). The evidence supports lower **takeover-side** cost, not lower total lifecycle cost.

## Evidence and results interpretation

### Strongly supported

1. The paper defines a concrete, inspectable matched-view takeover protocol.
2. Its reported denominator expands 75 source tasks into 181 checkpoint-view blocks and 2,172 main runs consistently.
3. Within the reported configurations, every context view has lower aggregate median successor events and prompt tokens than repository-only takeover.
4. Endpoint effects are more heterogeneous than effort effects; note-based Qwen/Gemma solved-rate gains are small or nominally nonsignificant.
5. Resumability depends on successor configuration: raw, summary, and structured views do not have one universal ranking.
6. The manuscript/source preserve prompts, field lists, model names, runtime limits, serving flags, and aggregate tables.

### Partially supported

- **Rediscovery reduction:** fewer post-handoff events/tokens are consistent with less re-inspection, but event categories are not analyzed and stopping/outcome distributions are not controlled.
- **Cross-predecessor robustness:** 720 additional runs show within-predecessor context reductions for three predecessor models, but exact point selection, state balance, and matched checkpoint equivalence across predecessors are unavailable.
- **Structured continuation contract:** the field list is bounded and operationally plausible, but fidelity, field necessity, semantic validity, and recipient acceptance are not measured.
- **Official correctness:** hidden tests provide a common endpoint for encoded software behavior, not maintainability, reviewability, or professional usefulness.

### Not supported

- a faithful or sufficient universal handoff schema;
- a causal decomposition of added information, compression, prompt cues, state labeling, or extra authoring compute;
- human-handoff or organizational-collaboration validity;
- cross-domain generalization;
- total-cost savings;
- agent capability, professional equivalence, production fitness, safety, or readiness.

## Unique insight

The paper's durable contribution is to make **resumability a matched successor intervention**, but its results show why resumability cannot be a scalar property of a note. It is a relation among:

```text
source task and authoritative requirements
→ predecessor configured system and trajectory
→ interruption rule and frozen work-state hash
→ visible handoff view and generation lineage
→ successor configured system and evidence entitlements
→ verification / continuation actions
→ terminal artifact and preserved-state consequences
→ takeover-side and lifecycle cost
→ bounded claim
```

Three constructs must remain separate:

1. **state fidelity:** does the handoff accurately represent repository/workspace state, evidence, uncertainty, failed paths, authority, and valid time?
2. **recipient sufficiency:** can this successor perform the next operation without unsafe inference, unnecessary rediscovery, or blind trust?
3. **continuation efficiency:** conditional on a defined endpoint and stopping policy, how much additional interaction, time, token use, and verification burden occurs?

A raw trace may be faithful but hard to consume. A short note may be sufficient for the realized next action but omit facts needed for an alternate repair or later audit. A note can reduce events because it leaks “already solved,” not because it explains the work. A successor can solve cheaply by ignoring a false note, while the handoff itself remains invalid. These dimensions require different evidence.

This sharpens adjacent repository findings:

- **AgentCo-op:** typed transport is not semantic or receiver-use validity. Handoff Debt adds a matched recipient-side cost outcome but still does not validate meaning.
- **DELEGATE-52:** preservation of artifact state and correct requested change are orthogonal. A successful takeover must preserve predecessor-correct work as well as finish the requested delta.
- **Workspace-Bench:** file availability, relevance, observed access, and causal use differ. Repository-only takeover does not reveal which rediscovery actions were necessary or correct.
- **ACON/context compression:** task-sufficient compression is not state-faithful compression. Handoff summaries need source-span and invariant checks, not endpoint reward alone.
- **procedural memory:** a handoff is episode-specific state transfer, not a reusable Skill; promoting its clauses across tasks requires a separate transfer edge and held-out evidence.

## Limitations and validity threats

1. The 75 tasks are the first seeded order after a tier filter, not a representative sample of software interruptions or knowledge work.
2. Exact task IDs and exclusion/eligibility records are absent.
3. Three protocol-defined checkpoints do not model natural interruption hazards, urgency, ownership, review, or permission transfer.
4. Post-failure availability is conditioned on predecessor behavior.
5. Multiple handoffs per source issue share trajectories and state, but inference treats 181 points as independent.
6. One predecessor trajectory per task dominates the main study.
7. Main cells have one attempt; the repeated subset is small, selected, and incompletely analyzed.
8. No invalid, missing, timeout, crashed-validation, generation-failure, or retry ledger is reported.
9. Frozen-state equivalence across views cannot be verified without checkpoints/manifests.
10. Structured-note `continuation-state label` may encode official state; its derivation and evaluator visibility are not specified.
11. The “full schema” is a prose field list, not a machine-readable released contract.
12. No real handoff payload, fidelity label, evidence locator, contradiction record, or field-level ablation is released.
13. Summary and structured conditions use additional predecessor-side model computation that is excluded from cost.
14. Raw trace, summary, and structured views differ in information volume, transformation, formatting, possible state cues, and generation process; “format” bundles these factors.
15. Event counts combine actions and observations and are not decomposed into inspection, validation, editing, repair, or idle/error events.
16. Unconditional costs conflate rediscovery, outcome quality, stopping, censoring, and preservation decisions.
17. Prompt tokens are tokenizer/configuration dependent and receive no uncertainty analysis.
18. Table 2/3 prompt medians conflict for Qwen context views.
19. Efficiency confidence intervals do not target the displayed median-ratio point estimates.
20. McNemar/bootstrap inference ignores source-task clustering and multiplicity.
21. The predecessor-robustness subset does not disclose common task/point identities or state balance across predecessor models.
22. Different successor context lengths and tokenizers prevent direct cross-model cost interpretation.
23. Public SWE-bench exposure/contamination is not controlled; pairing limits but does not eliminate cue-dependent memorized-solution effects.
24. Official tests do not score maintainability, explanatory adequacy, collateral changes, security, review burden, or downstream usability.
25. No author-owned code, data, run records, analysis, or empirical release permits independent reproduction.
26. Manual failure-mode inspection has no denominator, sampling rule, coding guide, rater reliability, or examples tied to outcomes.
27. Agent-to-agent local-model takeover does not establish human handoff, team coordination, professional realism, or deployment value.

## Reproducibility and operational realism

Reproducibility is **moderate at the protocol-description layer and poor at the result layer**. The immutable PDF and full source provide complete aggregate tables, prompts, field descriptions, seeds, model identifiers, serving flags, generation cap, timeout, step cap, and statistical-test prose. The local arithmetic audit found the run denominators and solved/discordant counts coherent.

Exact reproduction is blocked by absent task IDs, task-order manifest, predecessor runs, checkpoint hashes, frozen repositories, real view payloads, configured runtime/container commits, takeover sampling settings, per-run outcome/event/token records, missingness ledger, validation logs, and analysis code. Aggregate tables cannot diagnose the Table 2/3 token discrepancy or recompute source-clustered uncertainty. Current release searches found no verifiable author-owned artifacts beyond arXiv.

Operational realism is bounded. Real repositories, partial edits, validation evidence, failed attempts, state preservation, and separate successors are valuable. Yet the interruptions are synthetic and evaluator-triggered; successors receive no ticket history, ownership/authorization transfer, code review, stakeholder clarification, CI latency, concurrent edits, branch conflicts, human notes, or downstream maintenance. Four-hour/500-step local runs over public issues test an agent-resumption mechanism, not an organizational handoff.

## Transfer to skill-bench

### Preserve

1. **Freeze the work state across handoff-view conditions.** Store workspace/repository root hash, checkpoint parent, interruption event, open processes, environment state, and protected artifacts.
2. **Keep endpoint quality and continuation cost separate.** A handoff can improve one, both, or neither.
3. **Use multiple recipient configurations.** Resumability is recipient-relative, so the same artifact should be tested across pinned successors without turning the result into a model leaderboard.
4. **Separate completion, preservation, and regression repair.** These are different receiving operations and should have separate denominators.
5. **Treat notes as evidence, not truth.** Require verification and preserve the immutable raw trajectory outside the successor-visible context.

### Repair

1. **Factor the intervention.** Compare frozen state only; raw trace; deterministic metadata only; free summary only; structured template with the same model-generated content; structured note without outcome/state labels; and, where appropriate, an independently authored note. This separates information amount, compression, formatting, cueing, and authoring compute.
2. **Type every handoff claim.** Link each changed-file, validation, failure, assumption, uncertainty, rollback, and next-action claim to source spans/events, authority, valid time, confidence, and verification status.
3. **Forbid evaluator-derived state leakage.** Continuation labels must be predecessor-observable or private to analysis. If official tests classify checkpoint state, that classification cannot enter the visible handoff unless explicitly treated as oracle assistance.
4. **Measure fidelity and sufficiency independently.** Plant omissions, stale validations, false success labels, contradictory next steps, missing required literals, and benign alternate paths; score state truth, recipient use, and downstream consequence separately.
5. **Use endpoint-aware effort estimands.** Report time/events/tokens to first valid resolution with unsolved runs censored; matched costs among shared solved/failed strata; preservation verification cost; repeated inspection/validation/edit counts; and invalid/provider failures separately.
6. **Report total lifecycle cost.** Include note generation, trace processing, storage/retrieval, verification, retries, wall time, output tokens, and human review—not only successor prompt consumption.
7. **Cluster at source-work unit.** Resample source tasks or higher lineage clusters, preserve within-task checkpoints/views, repeat stochastic runs, and report point estimates whose intervals target the same statistic.
8. **Test alternate futures.** A note sufficient for the realized continuation may fail a request change, rollback, audit, handoff to another role, or delayed resumption.
9. **Bind recipient operation.** Reuse the repository's existing handoff-usability ladder: transport → structural parse → semantic/authority validity → receiver acceptance → next-operation success → downstream consequence.
10. **Keep claim ceilings explicit.** A matched local takeover effect licenses configured resumption evidence, not professional collaboration or readiness.

## Concrete repository actions

1. Add no new build subsystem. Existing handoff-usability, downstream-counterfactual, compression-fidelity, configured-system, metric, task-health, validity, and information-flow machinery already has homes for these requirements.
2. Add one consolidation task to integrate this review into `docs/research-synthesis-index.md` and `docs/benchmark-design-taxonomy.md`: define the frozen-state successor-resumability chain; separate state fidelity, recipient sufficiency, endpoint-aware continuation effort, and lifecycle cost; record the outcome-label leakage boundary and source-task-clustered estimands; compare AgentCo-op, DELEGATE-52, Workspace-Bench, ACON, and the existing cross-domain handoff conformance evidence without adding coding-specific scope.
3. If the existing handoff pilot is extended, use a small matched restart experiment across two unlike work shapes with deterministic-metadata-only and corrupted-note controls. Do not run a large model study until frozen-state hashes, endpoint-aware event accounting, and evaluator-visible-state firewalls pass canaries.

## Action items

- [x] Read the complete immutable v1 PDF/text and all appendices.
- [x] Inspect the complete 30-regular-file arXiv source tree and aggregate result fragments.
- [x] Verify 75 → 181 → 724/model → 2,172 headline denominators.
- [x] Reconcile rounded solved counts with all nine McNemar discordant-pair differences.
- [x] Audit checkpoint construction, four views, successor runtime, note generation, validation, event/token metrics, statistical tests, and limitations.
- [x] Identify nested-task inference, estimand/CI mismatch, prompt-table inconsistency, outcome-dependent effort, excluded authoring cost, and continuation-label leakage risk.
- [x] Recheck author-owned release availability and preserve the no-release boundary.
- [x] Compare adjacent handoff, workspace, compression, memory, configured-system, metric, and validity evidence.
- [ ] Consolidate the bounded resumability protocol into canonical synthesis; no new schema is justified.
