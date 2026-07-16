# InKH: context governance is a useful systems hypothesis, but the simulator writes the treatment into its outcomes

**Paper:** Ailiya Borjigin et al., *Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents*, arXiv:2606.01886v1 (1 June 2026), <https://arxiv.org/abs/2606.01886v1>.

## Review and evidence status

**Deep review of the complete immutable primary source.** I read the full 17-page local PDF, the complete local text extraction, and the four-member official arXiv source package. The Atom record contains no withdrawal or retraction notice.

- PDF: `data/papers/pdfs/2606.01886v1-absorbing-complexity.pdf` (17 pages; SHA-256 `e4a9f0362b50bda2dcb46123746d7c5ab681ac9aa876c7261bf3e9da50842ad2`).
- Full text: `data/papers/text/2606.01886v1-absorbing-complexity.txt` (SHA-256 `e8632e248dcca1b2cf54ee2216c5657854941e000c971e0d44128ed427c0737d`).
- Metadata: `data/papers/source/2606.01886v1-metadata.xml` (SHA-256 `0bdd1200ec5c139a0e11a940898c80ae3c2f278bd9a914b620102b5e5ab2e336`).
- Official source archive: `data/papers/source/2606.01886v1.tar.gz` (SHA-256 `8af12f693fd7152762464b8b496da1260e1acabf0bc851b7efdc43552157adf8`), containing only `00README.json`, `main.tex`, one architecture figure, and one logo.
- Acquisition/release audit: `data/sources/releases/2606.01886v1-inkh/provenance.json`.

Appendix A.4 says a “released artifact” contains simulator code, synthetic data, configurations, tables, and figure scripts and gives `python scripts/run_synthetic_suite.py` (p. 17). No author-owned artifact URL appears in the paper or source package. Exact-title, arXiv-ID, filename, True Trading, INC4, GitHub, web, and author-channel searches through 17 July 2026 identified only paper mirrors and an INC4 Hugging Face profile describing InKH as “forthcoming,” not an executable release. GitHub code search also requires authentication and supplied no positive evidence. The appendix formulas and pseudocode are therefore **manuscript specifications, not an inspected or replayable release**.

## Why this matters to `skill-bench`

This review advances charter objectives A and B by testing a general question: when does a governed memory/context architecture produce evidence about fresh, authorized context delivery rather than a score generated from its own design assumptions? Finance is a bounded stress case, not the benchmark’s scope.

## One-sentence contribution

InKH usefully joins event streams, claim-level valid time, maturity, passive bounded context assembly, write-time invalidation, and a separate audit surface, but its reported benchmark is a deterministic architecture simulator whose baseline-specific priors, retrieval bonuses, stale penalties, latency distributions, and gold observers co-author the headline quality, cost, traceability, and staleness results; it validates internal policy realization, not an LLM agent, graph implementation, human decision, or production workflow.

## Research question and intended construct

The paper asks whether a financial agent should receive a compact governed context assembled before reasoning rather than decide when and how to search its own persistent memory. Its product thesis is that adoption improves when a system absorbs “financial cognition friction”: repeated restatement of preferences, judgments, risks, and changing assumptions (abstract and §1, pp. 1–2).

The architecture has five intended components (§§3–4, pp. 4–9):

1. incoming user, market, tool, portfolio, and internal-risk events;
2. knowledge objects carrying type, scope, content, evidence/provenance, confidence, maturity, regime, first-seen, last-validated, and invalidation times;
3. temporal-graph candidate retrieval and budgeted passive injection before the next model step;
4. background extraction, contradiction detection, upsert, decay, maturity transition, and write-time invalidation; and
5. a graph for online retrieval plus a human-readable wiki for audit and review.

The intended comparison is architectural: model-only, tool agent, simple memory, wiki walk, a knowledge harness without invalidation (`KH-NoInv`), and full InKH (Table 1, p. 8). The strongest proposed ablation is InKH versus `KH-NoInv`, because both nominally have the same components and knowledge volume except invalidation.

That is a worthwhile systems hypothesis. The paper does **not**, however, evaluate an operating financial LLM agent. Assumption A1 explicitly models baselines through characteristic token budgets, retrieval behavior, and latency distributions rather than a vendor API; A3 scores against simulator-defined requirements; and the limitations say graph retrieval and serving are abstractly simulated (pp. 10, 13).

## Methodology and system reconstruction

### Knowledge and context lifecycle

An event updates state `(user, market, risk, workflow/execution, graph)`. Detected entities, intent, and risk select an `h`-hop graph neighborhood. Invalidated objects are removed, governance filters by effective confidence, maturity threshold, and user overlay, and a utility function ranks relevance, structure, maturity, freshness, regime fit, and trust under a token budget. The selected items are compressed and fused into the next working context (§3, pp. 4–5).

After a workflow, a background process extracts candidate knowledge, attaches evidence and trust, canonicalizes entities, detects contradictions, invalidates older claims, upserts the graph, and updates wiki pages. A maintenance tick samples staleness/link/quality/merge/split probes, recomputes confidence and maturity, executes low-risk fixes, and queues high-impact changes for human review (Algorithms 1–3, pp. 8–9).

The formal object is richer than a generic memory string, but several functions remain names rather than operational definitions: entity detection, relation extraction, trust, contradiction score and threshold, regime distance, utility weights, compression fidelity, maturity transition, action-risk class, human review, and “low-risk” auto-fix policy. No implementation or adjudication evidence shows how these behave.

### Synthetic event process and denominator

All reported results come from Stage A, a controlled simulator. Stage B—public replay over FRED, SEC EDGAR, Binance data, simulated dialogue, and human scoring—is specified but not executed (Table 2, pp. 9–10).

Stage A uses:

- 24 seeds;
- four rounds;
- 80 episodes per round;
- four task labels: market analysis, portfolio review, copy-trading evaluation, and trade preparation;
- cold start in round 1, preference signals in round 2, regime/protocol shocks in round 3, and post-shock reuse in round 4.

The arithmetic is internally coherent: `24 × 4 × 80 = 7,680` workflows per baseline and `7,680 × 6 = 46,080` baseline-conditioned rows. The effective randomization/inference unit is the seed, not the 7,680 workflow rows: all tests reduce to 24 seed-level means (p. 10). The paper does not specify how the 80 episodes are sampled among families, how shocks/preferences are generated, whether identical event streams are paired across baselines, what seed controls, or whether later episodes depend on earlier simulator state.

### The simulator authors the quality mechanism

Appendix A.2 gives the core quality equation (pp. 16–17):

```text
Q = clip(q_b + beta_r (round - 1)
         + beta_h * hits
         - beta_m * missing
         - beta_s * stale
         + epsilon)
```

where `q_b` is a **baseline-specific prior**, `beta_h` and `beta_s` vary by baseline, and Gaussian noise has fixed standard deviation `0.018`. Retrieval-hit bonuses are separately capped and parameterized for the knowledge-harness, wiki, and simple-memory families. Every miss costs `0.02`; stale use costs `0.11` for WikiWalk, SimpleMem, and `KH-NoInv`, but only `0.04` for full InKH.

This is the decisive validity fact. Quality is not an independently judged output from an agent solving a task. It is generated from simulator events through coefficients that differ by the architecture being evaluated. Invalidation lowers the simulated stale count, and the full system additionally pays a smaller quality penalty when stale use occurs. Baseline-specific priors and an incompletely specified round coefficient can encode further level and trajectory differences. The paper does not report or justify all coefficients, calibrate them from observed workflows, perform a coefficient-sensitivity analysis, or show that the ranking survives equal scoring weights.

The simulator similarly assigns characteristic token budgets, tool calls, and latency distributions rather than timing executed retrieval/model/database paths (A1–A2, p. 10). Traceability and stale-usage labels are assessed against simulator-defined gold requirements (A3), and the traceability function is not specified. Thus quality, latency, tokens, cost, stale usage, and traceability are neither independent observers nor independent empirical channels.

### Metrics and statistical tests

The paper reports quality, latency, tokens, context precision, stale use, traceability, estimated cost, repeated-error reduction, and quality per thousand tokens (§5, p. 10). Context precision is `gold hits / retrieved items`; repeated-error reduction normalizes the round-1 to round-4 quality change by round-1 error. Cost assumes `$3` per million tokens plus `$0.002` per tool call.

Ninety-five-percent intervals bootstrap 24 seed-level means with 3,000 resamples; paired comparisons use Wilcoxon signed-rank tests over those 24 means (p. 10). Seed-level pairing is preferable to treating 7,680 episodes as independent. But the extremely narrow intervals mostly reflect a high-volume, low-noise deterministic simulator under fixed coefficients, not demonstrated operational reliability. There is no uncertainty over simulator specification, coefficient choice, event generator, task family, observer validity, model sampling, database/service behavior, or human judgment. The paper reports only `p_max` across four outcomes and does not specify multiplicity handling or the mapping from each p-value to each metric.

## Evidence and what it supports

Table 3 reports full InKH at quality `0.815`, latency `900.2 ms`, `1,540.3` tokens, context precision `0.329`, stale usage `0.009`, traceability `0.999`, and estimated cost `$0.0086`. `KH-NoInv` reports `0.765`, `960.0 ms`, `1,550.2` tokens, stale usage `0.271`, and traceability `0.928`; WikiWalk reports `0.707`, `5,281.1 ms`, `8,697.3` tokens, stale usage `0.271`, and traceability `0.538` (p. 11).

Round-wise quality for InKH rises `0.780 → 0.808 → 0.824 → 0.847`, while `KH-NoInv`, SimpleMem, and WikiWalk regress after the round-3 shock and finish roughly flat (Table 5, p. 12). Table 7 reports identical final item, new-item, verified-item, and proven-item means for InKH and `KH-NoInv`, with `2.96` invalidated items only for InKH (p. 14). These are internally consistent outputs of the declared simulator.

The evidence supports a bounded implementation-policy claim:

> Under the manuscript’s synthetic event generator, baseline-specific scoring rules, simulated resource distributions, and gold observers, the full InKH policy produces fewer simulator-labelled stale uses than the no-invalidation policy, and the configured simulator maps that difference to higher quality and traceability at similar simulated token cost.

It also demonstrates that the authors can express an architecture as event, knowledge, context, maintenance, and governance objects and construct an internally coherent count/ablation narrative.

It does **not** establish the headline architectural causal claims in an external system. In particular:

- the WikiWalk latency/token advantage is built from characteristic simulated budgets and distributions, not measured graph/wiki/model execution;
- the quality improvement is partly a direct function of baseline identity, hit/miss/stale events, and unequal stale penalties;
- stale suppression is an expected consequence of a simulator that marks contradictions and removes invalidated records according to authored gold;
- traceability near `0.999` is not a human audit result, provenance-correctness study, or decision reconstruction test;
- “repeated error reduction” is a transformation of the same generated quality score, not an independently observed recurrence of a model error;
- equal inventory size rules out “more simulated items” inside the specification, but does not validate contradiction detection, correct invalidation, safe retention, or downstream use.

## Unique insight: governance must be evaluated outside the policy that generates the world

The paper’s deepest reusable architectural idea is **passive, bounded, governance-aware context assembly with a separate audit projection**. A system should not require a model to rediscover every prior claim, and online retrieval need not use the same representation humans inspect.

Its deepest benchmark lesson is the inverse:

> A governance simulator cannot validate governance when the same authored policy generates events, determines truth and supersession, controls retrieval/invalidation, assigns architecture-specific costs, and computes quality from those internal events.

For `skill-bench`, the full causal/evidence chain should be:

```text
external event/source and authority
→ expected claim-state transition
→ attempted extraction/write/invalidation
→ realized store delta
→ retrieval candidate set
→ governance admission with reason
→ compressed/presented evidence view
→ model access and adoption/rejection
→ answer/action/artifact/state consequence
→ independent criterion observer
→ stakeholder utility, risk, and resource ledger
```

InKH specifies authored versions of several early links and simulates endpoint labels. It does not independently observe extraction correctness, actual store state, context fidelity, model uptake, action, artifact, or consequence. The most important separation is therefore not graph versus wiki; it is **normative policy projection versus realized mechanism versus independent downstream consequence**.

## Limitations and validity threats

### Construct and oracle

1. **Quality is simulator-produced, not task performance.** No LLM output, professional artifact, human rating, environment action, or external answer criterion enters the reported quality equation.
2. **Baseline identity enters the outcome model.** `q_b`, hit/stale coefficients, bonus caps, and stale penalties vary by baseline; full InKH receives a smaller stale penalty than comparator memory systems.
3. **The simulator and observer share one authoring lineage.** Events, preferences, shocks, stale traps, gold requirements, contradiction status, traceability, and scores are not independently validated.
4. **Task-family names do not establish task realism.** “Portfolio review” and “trade preparation” are labels over unspecified synthetic mechanics, not released source packs, instructions, outputs, rubrics, or expert-authored incidents.
5. **Traceability is underdefined.** A score of `0.999` has no disclosed predicate, evidence view, rater, false-positive audit, or reconstruction criterion.
6. **Repeated-error reduction is not an independent construct.** It deterministically re-expresses round-wise simulator quality.
7. **Context precision can reward authored retrieval compatibility.** “Gold” items originate in the same simulator and no independent authority establishes completeness, alternatives, or professionally sufficient context.

### Treatment and mechanism

8. **Passive injection versus wiki walk is not executed.** Token and latency differences come from architecture-characteristic simulation, not matched implementations on shared hardware, model, graph, cache, and workload.
9. **The invalidation ablation is necessary but not cleanly scored.** It changes realized stale events while baseline-specific quality parameters and an unequal stale penalty remain in the measurement path.
10. **Contradiction and supersession are treated as known.** Real evidence often conflicts because of source authority, scope, timing, conditional applicability, or uncertainty; the simulator supplies the answer.
11. **Maturity is inventory, not validated epistemic status.** “Verified” and “proven” counts are simulator states without reviewer authority, evidence sufficiency, calibration, or downstream predictive validation.
12. **Retrieval does not establish adoption.** Injected items may be available but ignored, misread, over-weighted, or causally irrelevant; no model is present to make these distinctions.
13. **Compression is untested.** The paper invokes `Compress(TopB(...))` but does not measure proposition survival, authority preservation, contradiction distortion, or decision consequence.
14. **Governance admission is authored, not exercised.** The risk threshold, user overlay, and confidence gate have no conflict, exception, forged update, missing authority, over-block, or appeal cases.
15. **The audit surface is asserted.** No human uses the wiki to find, understand, correct, approve, or reject a claim; graph/wiki divergence and update lag are not measured.

### Statistics and reporting

16. **Twenty-four seeds are the inferential sample.** The 46,080 rows increase deterministic averaging precision but do not create 46,080 independent architecture tests.
17. **Specification uncertainty is absent.** Bootstrap intervals condition on one generator and one coefficient set; they do not cover the dominant uncertainty in the benchmark design.
18. **The seed and event process is under-specified.** Pairing, task allocation, shock intensity, preference generation, state dependence, and seed-controlled components are unavailable.
19. **No sensitivity analysis.** The paper does not equalize scoring coefficients, vary stale penalties/priors, perturb contradiction error, or test whether conclusions survive observer noise.
20. **`p_max` is opaque.** Per-outcome p-values, test details, effect threshold, and multiplicity policy are not provided.
21. **Cost is synthetic and incomplete.** A flat token/tool formula omits graph storage/query, extraction, embeddings, contradiction checks, maintenance, wiki generation, human review, cache behavior, concurrency, failures, and infrastructure.

### Reproducibility and operational realism

22. **The claimed release is not discoverable.** No code, data, configuration, per-workflow logs, seeds, result rows, statistical script, or figure generator can be inspected or replayed.
23. **The appendix is insufficient to regenerate results.** It omits full baseline priors/coefficients, event distributions, traceability function, latency/token distributions, tool-call model, task-family mechanics, and state transitions.
24. **Public replay is future work.** FRED/EDGAR/Binance Stage B and human scoring are specified only.
25. **No production graph exists in the experiment.** The paper explicitly simulates graph retrieval and serving behavior.
26. **No live financial claim is licensed.** There are no real users, analysts, portfolios, orders, markets, source disputes, audit events, reviewer burdens, profitability outcomes, or safety consequences.
27. **Adoption is not measured.** Reduced “cognition friction” and product adoption are motivating hypotheses with no user-burden, time, trust, correction, acceptance, or retention evidence.

## Comparison with adjacent reviewed evidence

- **LongMemEval-V2** exposes bounded evidence returned from retained experience to a fixed reader and makes representation effects inspectable, but stops before held-out action. InKH goes further in governance vocabulary while going backward in empirical realization: there is no actual memory implementation or reader.
- **MemOps** crosses expected lifecycle events with probe surfaces and warns that an authored trace is not an observed write/delete/state transition. InKH’s extracted, upserted, invalidated, mature, and audited objects are likewise normative simulator state—not realized store operations.
- **MemSyco-Bench** shows that relevance does not authorize use and types ignore/constrain/defer/supersede/use decisions. InKH includes scope, maturity, risk, and user overlay, but its `Allow` function assumes those authorities are already correct and supplies no represented-user or source adjudication.
- **Governance Decay** provides matched evidence that a lossy context transformation can change a later proposed action, while separating carriage, adoption, admission, and consequence. InKH invokes compression and governance but observes none of those links through an acting model.
- **Decision Fidelity under Context Compression** treats the transformed evidence view as an intervention on a named downstream decision instrument. InKH has a token budget and compression operator but no state-fidelity, decision-preservation, correctness, or consequence study.
- **Online skill and memory budget value** charges auxiliary inference and injected context against acting opportunity and exposes promotion errors. InKH’s low foreground cost excludes extraction, maintenance, validation, audit, review, storage, failure, and amortization and therefore cannot establish net operational value.

This evidence **reinforces rather than changes** the repository’s grouped memory conclusion: expected state, authority, persistence, retrieval, presentation, adoption, action, consequence, and cost are non-substitutable links. No canonical synthesis change or new schema is warranted.

## Transfer to `skill-bench`

### Retain

1. Model context assembly as a first-class, versioned configured-system intervention rather than invisible prompt plumbing.
2. Represent knowledge claims with evidence/provenance, scope, confidence, maturity/review state, regime/applicability, first-seen, last-validated, and invalidation/supersession times.
3. Separate low-latency machine retrieval from a human audit projection, while checking semantic equivalence and update lag between them.
4. Include matched shock/post-shock tasks and a no-invalidation condition with equal initial state and inventory.
5. Report stale-use, context precision, traceability, quality, latency, and cost separately rather than collapsing them.
6. Preserve seed/task/state dependence and perform inference at the actual randomization and lineage level.

### Repair before reuse

1. Use externally grounded source packs and independent authority adjudication for truth, scope, valid time, supersession, risk, and allowed influence.
2. Factor `passive versus agent-driven retrieval` separately from graph/wiki representation, context budget, compression, model, cache, and invalidation.
3. Hold the quality observer fixed across treatments. Never give the favored architecture a different prior, benefit cap, or penalty coefficient.
4. Bind expected extraction/invalidation events to actual store deltas, candidate sets, admitted/rejected items, evidence-view hashes, and audit-page projections.
5. Add matched omission, stale, corrupted, wrong-scope, wrong-authority, superseded, forged-update, valid-update, and legitimate-positive-use controls.
6. Observe model access/adoption and downstream artifact/state consequence; use removal/restoration/substitution interventions before assigning causal roots.
7. Validate compression for proposition survival, authority/valid-time preservation, contradiction handling, and decision consequence.
8. Measure complete resources: extraction, embeddings, graph operations, compression, model calls, storage, maintenance, review, correction, false blocks, retries, latency, and amortized future reuse.
9. Calibrate traceability and maturity against blinded human/expert review, disagreement, correction latency, and accepted alternative interpretations.
10. Separate policy conformance, mechanism realization, professional capability, user benefit, safety, and readiness in the validity argument.

### Do not infer

Do not infer memory quality, financial cognition, professional capability, product adoption, reduced user burden, production latency, safe financial action, auditability, live profitability, or deployment readiness from this simulator. Do not treat a small conditional bootstrap interval as robustness to benchmark specification. Do not call an author-assigned “verified” or “proven” state evidence of real epistemic maturity.

## Concrete repository actions

No new queue task is warranted. Existing source-authority/valid-time records, benchmark traces, context-compression and artifact-view admissibility, compounding-lesson lifecycle, persistent-state and experience-memory slices, configured-system identity, resource accounting, task health, metric monitoring, and validity arguments already provide nonduplicate homes.

For the next relevant longitudinal pilot, incorporate one **observer-independent invalidation calibration** inside existing machinery rather than creating an InKH subsystem:

- two externally sourced claims with explicit authority/scope/valid time;
- one genuine superseding update and one merely conflicting but non-superseding item;
- equal starting store and matched no-invalidation/invalidation conditions;
- actual store-delta and presented-context receipts;
- a held-out artifact/state decision whose criterion is fixed across conditions;
- a legitimate positive-use control and a false-invalidation harm case;
- separate stale delivery, adoption, action consequence, traceability, review burden, and full-resource outcomes.

Useful completion would show whether correct invalidation improves a consequential decision without increasing false invalidation or review burden. Until then, the current review is evidence against adding another synthetic memory contract.

## Claim boundary

The paper provides a coherent architectural specification for event-driven, bounded, provenance-bearing, maturity- and risk-gated context assembly and an internally consistent simulator result showing that its authored invalidation policy suppresses its authored stale-use labels. That is useful hypothesis and instrument-design evidence.

It does **not** provide an executable release, an implemented graph/wiki/LLM system, independent task-quality or traceability observations, calibrated knowledge authority, compression fidelity, realized memory operations, model adoption, downstream action, professional artifacts, user-burden evidence, financial outcomes, production cost, safety, or readiness. Because architecture-specific assumptions enter both simulated resources and the quality equation, the headline improvements are policy-generated outputs, not external validation of the architecture.