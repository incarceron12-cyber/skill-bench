# Self-GC: recoverable object lifecycles are a better runtime abstraction, but future-continuation judging is not recovery or utility evidence

## Source and review status

**Deep review of the complete immutable primary source and appendices, plus an audit of the official arXiv source package and a timing-bounded search for author-owned artifacts.**

- **Paper:** Xubin Hao, Hongjin Meng, Xin Yin, Jiawei Zhu, and Chenpeng Cao, *Self-GC: Self-Governing Context for Long-Horizon LLM Agents*, arXiv:2607.00692v1 (1 July 2026), <https://arxiv.org/abs/2607.00692v1>.
- **Date read:** 2026-07-17.
- **Local PDF:** `data/papers/pdfs/2607.00692v1-self-gc-self-governing-context-long-horizon-agents.pdf` (15 pages; SHA-256 `ef861029b7c689dd0024a15ba7a291e77ea634b67d8b605c4c3376f71193cb5d`).
- **Full local text:** `data/papers/text/2607.00692v1-self-gc-self-governing-context-long-horizon-agents.txt` (71,710 characters; SHA-256 `37bdd38fdce8b3e4433c357837a7a417569622b8c5ea4bfbbb62f015545d68e4`).
- **Immutable HTML and metadata:** `data/papers/source/2607.00692v1.html` and `data/papers/source/2607.00692v1-metadata.xml`; the Atom summary contains no withdrawal or retraction notice.
- **Official arXiv source:** `data/papers/source/2607.00692v1-source.tar` (SHA-256 `aa09c03cad6b5bdb8bd4f2663eb02b3ca2b2c83dc4f1da44f1bc7f6d2d15dca0`). Its 25-entry tree contains manuscript TeX/BibTeX/style files and seven figures, but no code, sanitized sessions, prompts as executable files, planner or judge outputs, result rows, sidecars, recovery traces, online protocol, or supplement.
- **Release boundary:** the paper and source package link no repository or dataset. Exact-title, arXiv-ID, author-name, GitHub repository/API, Hugging Face, and general-web searches on 2026-07-17 found no verifiable author-owned release. This agrees with the paper's reproducibility checklist, which says no sanitized artifact package or source code is released (p. 15). All empirical results are therefore manuscript-reported and unreplayed.

## One-sentence contribution

Self-GC usefully reframes active agent context as indexed objects governed by typed `fold`, `mask`, and `prune` transitions under harness-enforced rehearsal, sidecars, safe commits, lineage repair, and cache economics; however, its evidence compares unequal pruning operating points using one future-aware model judge, never executes recovery or a held-out continuation, leaves the production-derived sampling frame and online split under-specified, and therefore establishes a promising runtime design plus configured judge preference—not semantic equivalence, recoverability, task quality, net cost, production utility, or readiness.

## Why this matters for skill-bench

This advances charter objectives A–C through a cross-domain runtime-validity question, not a commitment to context management as the benchmark's domain. Real knowledge-work agents accumulate source evidence, locators, editable artifacts, instructions, failed attempts, current blockers, and handoff state. A context policy can preserve the nominal task while silently changing which evidence and obligations are available at a later decision.

Self-GC adds an important object-lifecycle layer to the existing compression evidence:

```text
authoritative source / artifact / obligation
→ indexed context object and parent lineage
→ active, folded, masked, or pruned lifecycle transition
→ active-view route and sidecar state
→ decision-time discovery and recovery attempt
→ proposition / locator / artifact reconstruction
→ behavioral adoption and valid action
→ artifact / environment consequence
→ quality, efficiency, and stakeholder utility
```

The paper directly specifies the first four links. Its GPT-5.5 observer estimates whether the retained view *appears* adequate for the realized future. It does not execute the recovery, downstream action, artifact mutation, or consequence links. That boundary is the review's central result.

## Research question and defensible claim

The paper asks whether a side-channel planner plus deterministic harness controls can choose object-level context edits that remove tokens while preserving dependencies needed by real later turns, and whether the deployed policy reduces main-agent input tokens (pp. 1–8).

The strongest defensible claim is:

> On 33 selected high-tool-pressure private sessions and 332 private production-derived sessions, at one reported threshold and under a single diff-grounded GPT-5.5 binary observer, Self-GC planner configurations received more `no-impact` labels while pruning fewer tokens than four hand-written policies. A deterministic account split also showed lower aggregate main-agent input-token averages for the Self-GC group during the reported six-day window.

The study does **not** establish a pruning-matched improvement; actual sidecar retrieval or byte-exact reconstruction; preservation for alternate plausible futures; downstream task, artifact, safety, or user quality; net tokens, latency, or billed cost including planning and cache disruption; a randomized online treatment effect; cross-harness portability; professional validity; production fitness; or readiness.

## Methodology and system

### Context objects and lifecycle actions

The harness turns each visible user request and following execution span into `conversation:user:k` and each tool result into `function:<tool>:n`. IDs are session-local and monotonic. Assistant turns are deliberately not first-class GC targets because they carry connective text and tool-call envelopes; the harness preserves or normalizes them when adjacent objects change (pp. 3–4).

The abstraction is stronger than raw message truncation:

- **fold** moves an exact payload to a sidecar and leaves a visible recovery pointer;
- **mask** preserves structural boundaries while eliding repetitive middle content; and
- **prune** removes allegedly obsolete content without a recovery guarantee.

A side-channel planner receives a forked indexed prefix and proposes actions over IDs. The harness resolves targets, removes latest/cut-turn edits, normalizes overlaps, projects the candidate locally, estimates savings, delays acceptance until a safe turn boundary, repairs parent lineage, persists folded payloads, and normalizes provider messages (pp. 3–4; Appendix pp. 10–13).

This is a useful division of labor: semantic future-value judgment remains fallible and model-mediated, while target validity, last-turn protection, sidecar persistence, and commit atomicity can be deterministic. The paper even reports that planners attempted to touch the protected cut turn in 25/330, 15/330, and 12/328 parsed plans, demonstrating that the harness guard is active rather than decorative (p. 7).

But the implementation's object ontology is narrower than the abstract. The abstract says user turns, tool spans, and **skill state** become indexed objects; the detailed data model defines only user-turn and tool-span IDs, and online coverage combines `context-gc` with `skill-gc` without a separate skill-state schema, treatment description, or result breakdown (pp. 1, 3–5, 13). Files, claims, obligations, evidence atoms, artifact versions, and permissions are content inside broad spans rather than independently governed objects. An exact folded payload may preserve bytes while its constituent authority, valid time, contradictions, and live obligations remain untyped.

### Recovery and cache-aware commit

Fold reminders are control-plane metadata attached to user messages, not assistant-authored summaries. This is a sensible attempt to keep routes visible without encouraging imitation of internal tags. The paper also proposes:

```text
CommitBenefit ≈ N_future(C − C′) − L_cache_break − L_GC
```

and says deployment regression made immediate commit positive-value above roughly 30% expected pruning; otherwise plans can wait for cache expiry or a task boundary (p. 4).

Neither mechanism is empirically validated at its stated claim level. The study reports no sidecar read API, access-control semantics, encryption or retention policy, collision test, stale-pointer test, partial-write recovery, deleted-sidecar behavior, recovery latency, byte comparison, binary artifact reconstruction, or model-triggered retrieval success. A pointer's presence is **routing availability**, not discovery, successful recovery, correct interpretation, or behavioral use.

The cache equation is a design heuristic rather than a measured cost model. `N_future`, cache-break loss, GC latency/cost, and the cited regression are unspecified; the 30% threshold has no sample, fit, uncertainty, traffic stratum, or sensitivity analysis. The paper excludes side-channel overhead from the online token metric and supplies no cache-hit, billed-token, latency, retry, or dollar ledger (pp. 4–5, 8).

### Offline suites and selection

Table 1 reduces 15,141 raw trace rows to 9,075 compaction-triggered traces, 332 Production Suite sessions, and a 33-session Hard Set. The Hard Set is selected from the highest sustained tool-pressure cases and intentionally overweights browser, shell, and web-fetch workflows. Representative anonymized requests include vendor comparison, spreadsheet repair, and scheduled-task diagnosis (pp. 4–5).

This supplies plausible production pressure but not an auditable sampling frame. The paper does not define:

- how rows map to sessions/accounts/tasks or why 9,075 triggered traces become 332 sessions;
- inclusion, exclusion, de-duplication, failure, language, length, or privacy/redaction rules;
- whether the Hard Set is a subset of the 332 and whether it influenced prompt/threshold development;
- numbers by account, workflow, task family, tool, context length, cut point, or lifecycle action;
- whether one or multiple cut points contribute to each binary session outcome; or
- the selection dates, model/harness versions, production agent, or natural missingness.

The 33-session Hard Set is therefore a selected stress slice, not an independent generalization sample. The 332 sessions are likely clustered by accounts, workflows, and shared tooling, while Wilson intervals treat the reported binary session labels as independent Bernoulli observations. The paper reports no planner repeats, judge repeats, account/task-clustered uncertainty, or run count; its own checklist acknowledges that runs and randomness controls are unspecified (p. 15).

### No-impact observer and evidence view

For each candidate, GPT-5.5 sees the retained prefix, structured GC plan, detailed removed/folded patches, and the **real future turns after the cut point**. It checks whether exact URLs, paths, row values, task IDs, editable bodies, source evidence, goals, and continuation readiness remain visible or recoverable. The evaluated agent sees only the retained view; removed diffs are judge-only. Wilson intervals summarize the binary judgment (pp. 5, 10–11).

This is better than generic summary similarity. It uses the realized future to identify concrete dependencies and gives the observer both sides of the transformation. Yet it is a **retrospective future-conditioned adequacy judgment**, not a continuation experiment:

1. It rewards sufficiency for one observed future and can approve removal of evidence needed by an alternate legitimate request, audit, repair path, or changed instruction.
2. The judge never runs the future agent, follows a pointer, reloads a sidecar, verifies a byte-exact body, performs a tool action, or inspects resulting artifact/environment state.
3. Seeing the removed diff and candidate plan can reveal the intended action and create method/verbosity bias; the tested agent has a strictly weaker evidence view.
4. `visible or recoverable` collapses active availability, route discoverability, storage existence, successful retrieval, proposition preservation, and downstream use.
5. One proprietary future model family, prompt, threshold, and sampled output define the label. There is no human/expert calibration, deterministic anchor set, blindness to method identity, repeated-label reliability, alternate judge panel, or invalid/uncertain disposition analysis.
6. The future itself may restate missing content. The paper does not separate dependence on retained prefix from dependence recovered naturally through future user/tool turns.

The 20-case A/B calibration is too small to repair these limits. On single-prompt disagreements, the A/B judge prefers Self-GC in 11, ties seven, and prefers oldest-turn in two; calibrated estimates become 92.77% versus 87.46% (p. 6). There is no sampling rule for the disagreement set, order randomization, label blinding, repeated judging, human adjudication, or uncertainty propagated from calibration.

### Baselines and unequal operating points

The four replayed baselines are oldest-turn folding, greedy tool pruning, tool mask-plus-prune, and a chronological/tool hybrid. All share cut points, token accounting, latest-turn retention, and the GPT-5.5 observer (pp. 5–6).

On the Hard Set, Self-GC has 28/33 implied passes (84.85%) at 43.95% pruning; baselines have 18–23/33 passes at 61.90–69.87% pruning. On the Production Suite, Self-GC configurations imply 303–314/332 passes at 31.04–33.98% pruning; baselines imply roughly 258–290/332 at 40.19–47.76% pruning. These integer counts reproduce the displayed percentages up to rounding.

The comparison shows that Self-GC occupies a more conservative region. It does **not** identify whether object-level planning dominates at the same compression target. Every Self-GC row prunes materially less than every baseline row. There is no threshold sweep, budget-matched baseline, random-retention control, `fold-only` control, planner-without-harness control, harness-without-planner control, sidecar ablation, or Pareto confidence region. A policy that retains more context should usually receive more no-impact labels. The paper's claim that Self-GC improves the trade-off is plausible from the plotted points, but not demonstrated as frontier dominance.

Planner-backbone similarity is also descriptive. All three are evaluated through the same prompt examples, harness, selected sessions, observer, and one threshold. Rates above 90% under that observer do not establish portability across harnesses, traffic, agent models, object schemas, or futures.

### Failure taxonomy and case evidence

The appendix's six categories are useful: evidence-detail loss, locator/handle loss, behavioral-contract loss, verbatim-source loss, live-state loss, and recovery-routing loss (pp. 12–14). Two narrative cases describe a table-header correction and a task-specific contract/database seed. They correctly show why chronology and message type are poor proxies for future value.

But the taxonomy and cases have no coding protocol, case inventory, frequency table, independent labels, agreement, traces, or causal replay. They are design examples, not measured failure prevalence or evidence that Self-GC repaired a downstream outcome. The prompt's few-shot examples may also encode these same categories, making the audit partly a test of rubric-aligned planning rather than independent construct coverage.

### Online account split

Accounts with email initials lexicographically at or after `o` receive Self-GC; earlier initials are controls. Figure 5 reports lower average main-agent input tokens from 08:00–22:00 on 25–30 May 2026, usually 10–15% and near 20% at peaks; the final window includes volatile month-end batch traffic (pp. 5, 7–8).

Account-level assignment is better than per-session alternation for avoiding treatment spillover, and the authors appropriately call it operational monitoring rather than a fully randomized quality experiment. Still, initials can correlate with language, geography, organization, account age, identity provider, or traffic mix. The paper gives no account/session/request counts, group balance, pre-period, covariate balance, eligibility/coverage rate, baseline input distribution, task mix, concurrent releases, attrition, invalids, quality outcome, confidence interval, or regression specification. It combines interactive `context-gc` and long-lived `skill-gc` and reports only covered aggregate traffic.

The metric excludes planner input/output, cache disruption, storage, recovery, latency, retries, and billed cost. Lower main-agent prompt surface can coexist with higher total tokens or poorer work. Thus the online result is an observed group difference in one resource measure—not a causal token-saving estimate, quality-preserving intervention, net-cost reduction, production utility result, or deployment-readiness test.

## Evidence and claim boundaries

### Supported by the paper

1. Self-GC specifies a coherent indexed-object plan–rehearse–commit architecture with typed lifecycle actions and deterministic latest-turn/target checks.
2. Fold separates exact payload storage from a compact active-view route, a useful capability absent from free-form summary replacement.
3. The planner sometimes proposes protected latest-turn edits, showing why deterministic harness enforcement is necessary.
4. Under one future-aware GPT-5.5 observer, Self-GC rows receive more no-impact labels while retaining more context than the four reported heuristic rows.
5. The manuscript's implied binary counts are internally consistent with 33- and 332-session denominators.
6. The private sessions include plausible evidence, locator, editable-artifact, correction, and live-state dependency patterns.
7. Aggregate main-agent input tokens differ between the deterministic account groups during the reported six-day window.

### Partially supported

- **Better efficiency/preservation trade-off:** point estimates are directionally favorable, but no pruning-matched frontier or uncertainty over paired differences is supplied.
- **Planner robustness:** three backbones behave similarly under one prompt/harness/judge/suite, not across independent implementations or traffic.
- **Recoverability:** the architecture stores exact folded payloads and routes, but no retrieval or reconstruction is executed or scored.
- **Future-dependency preservation:** one realized-future model observer finds fewer apparent losses; alternate futures, agent use, artifacts, and consequences are untested.
- **Production token reduction:** an operational group difference exists, but assignment validity, total resource accounting, and quality preservation are absent.
- **Harness portability:** the interface is conceptually small, but only one private implementation is evidenced.

### Not supported

- semantic, proposition, decision, or artifact equivalence after lifecycle edits;
- byte-exact or binary recovery success, route discoverability, or recovery latency;
- preservation for alternate legitimate future requests, audits, repairs, or handoffs;
- downstream task success, professional artifact quality, stakeholder consequence, or safety;
- causal attribution of observer gains to object indexing, planning, sidecars, rehearsal, or commit policy individually;
- Pareto dominance at equal pruning or equal total cost;
- net tokens, latency, dollars, cache benefit, or billed-cost savings;
- a randomized online quality-preserving treatment effect;
- broad model, harness, domain, workload, or user transport;
- professional validity, production fitness, or readiness.

## Unique insight

Self-GC's durable contribution is to separate **object lifecycle control** from **textual summarization**. That makes runtime mutations addressable, reversible where promised, and inspectable. The paper's own evidence reveals the necessary next distinction:

> **Retention, storage recoverability, routing recoverability, semantic recoverability, behavioral reuse, artifact/state integrity, and utility are different claims.**

A benchmark should therefore treat every context mutation as a transaction over named dependents:

```text
object identity + authority + valid time + content hash
→ transition request (fold / mask / prune)
→ planner identity, evidence view, and rationale
→ deterministic rehearsal and rejected-action ledger
→ committed active-view hash + sidecar hash + lineage repair
→ cache/storage/resource receipt
→ sampled future family, not only realized future
→ route discovery + retrieval attempt + reconstruction check
→ free continuation + artifact/state consequence
→ separate fidelity, sufficiency, quality, safety, and cost estimands
```

This goes beyond ACON's compressed-text event while remaining more modest than a memory-capability claim. It also exposes why `no-impact` is not one binary fact: the answer depends on which future, observer, recovery affordance, authority state, and consequence are in scope.

## Comparison with adjacent reviewed evidence

- **ACON** shows that end-task reward can coexist with date, modality, entity, and answer corruption, and that compression bundles reset/reformatting effects. Self-GC repairs addressability and exact-payload preservation for folded spans, but its observer still does not verify recovered content or alternate-future fidelity.
- **Plans Don't Persist** shows that deleting source text can leave derived restatements and that broad truncation confounds plan loss with working-state loss. Self-GC provides stronger object and commit semantics, but its broad user/tool objects still need proposition-level obligations and derived-trace information-flow checks.
- **Governance Decay** links constraint removal/restoration to a proposed downstream action. Self-GC's future-aware observer is less behavioral: it judges apparent support without allowing a free continuation. Conversely, Self-GC has a stronger recoverable-object architecture and explicit harness safety boundary.
- **Decision Fidelity under Context Compression** evaluates response distributions under source and compressed views and warns that preservation is evaluator-relative. Self-GC observes an earlier rung—future-conditioned sufficiency—without an independent correctness or consequence warrant.
- **Workspace-Bench** separates artifact availability, relevance, provenance, observed use, and causal-use claims. Self-GC sidecars similarly establish potential availability only; pointer presence cannot stand in for discovery, access, correct interpretation, or use.
- **Persistent-memory/lifecycle reviews** distinguish store state, retrieval evidence, model exposure, adoption, and held-out action benefit. Self-GC should inherit the same ladder rather than calling a stored fold `recoverable` at all levels.

## Limitations

1. The private data, code, prompts as executable artifacts, planner outputs, judge rows, sidecars, traces, and online protocol are unreleased.
2. The source package contains only manuscript materials and figures; no result replay is possible.
3. The 15,141→9,075→332 selection flow is under-specified.
4. The Hard Set is selected for high tool pressure and may overlap the Production Suite or development process.
5. Account, workflow, task-family, cut-point, and action-type distributions are absent.
6. Broad user/tool spans are not claim-, obligation-, artifact-, authority-, or permission-level objects.
7. Skill state is claimed in the abstract but not defined in the detailed object model or separately evaluated.
8. Assistant and derived traces are not first-class targets, limiting proposition-level information-flow accounting.
9. Fold existence is not tested through discovery, retrieval, byte equality, interpretation, or downstream use.
10. Prune deliberately has no recovery guarantee, yet the system lacks severity- or authority-based fail-closed eligibility evidence.
11. Sidecar access control, integrity, expiry, deletion, collision, stale routing, and failure semantics are unspecified.
12. Safe boundary and lineage repair are described but not stress-tested under crashes, retries, concurrent edits, or partial commits.
13. Cache-benefit variables and deployment regression are not reported.
14. The 30% threshold has no development sweep, sensitivity, or transport evidence.
15. Self-GC and baselines operate at materially different pruning rates.
16. No budget-matched or Pareto-sweep comparison isolates policy quality.
17. No component ablation isolates indexing, prompt, planner, sidecar, rehearsal, lineage, or commit effects.
18. One proprietary GPT-5.5 observer defines the primary outcome.
19. The observer sees removed content and the plan, unlike the evaluated agent.
20. No human calibration, blinding, repeated labels, judge panel, or deterministic anchor suite is supplied.
21. `visible or recoverable` collapses several distinct states and capabilities.
22. The metric conditions on one realized future and ignores alternate legitimate continuations.
23. Future turns can themselves reintroduce missing information; dependence on retained context is not isolated.
24. Wilson intervals ignore likely account/workflow/session clustering and planner/judge stochasticity.
25. The 20-disagreement A/B calibration is small and selection/order details are absent.
26. Failure categories and cases lack coding protocol, frequencies, agreement, or causal replay.
27. Planner-backbone comparisons share all other treatment and observer components.
28. The online email-initial split is deterministic rather than demonstrated as-if random.
29. Online counts, balance, pre-period, covariates, traffic composition, quality, invalids, and uncertainty are absent.
30. Online metrics exclude planner calls, cache effects, storage, recovery, latency, and billed cost.
31. `context-gc` and `skill-gc` are pooled without treatment-specific denominators or outcomes.
32. Six days, including volatile month-end traffic, do not establish stable utility or transport.
33. No downstream artifact, environment-state, user satisfaction, professional-quality, safety, or consequence measure is reported.

## Reproducibility and operational realism

**Conceptual reproducibility is moderate.** The paper gives the object IDs, lifecycle semantics, planner and judge contracts, output schemas, rehearsal/commit pseudocode, primary thresholds, model roles, formulas, aggregate tables, and a failure taxonomy. The explicit reproducibility checklist is unusually candid about what is absent.

**Result reproducibility is poor.** All sessions and online data are private; no sanitized package, code, prompt files, result rows, judge outputs, sidecars, configuration hashes, endpoint snapshots, seeds, hardware, or statistics scripts are released. Future/private model aliases and a proprietary harness prevent exact reconstruction. The source package audit confirms that these are not extraction omissions.

**Operational realism is promising but unvalidated.** The source workload plausibly includes browser evidence, shell output, spreadsheets, files, correction loops, handles, and handoffs. Object IDs, sidecars, safe commits, and cache concerns are genuine production mechanisms. But realism of pressure is not evidence of quality preservation. The offline trial does not run the agent after mutation; the online study observes only aggregate main-agent prompt tokens; and no artifact, state, user, billing, latency, or recovery outcome closes the loop.

## Transfer to skill-bench

### Retain

1. **Indexed lifecycle objects.** Context transformations should target stable IDs rather than fuzzy message text.
2. **Typed fold/mask/prune semantics.** Exact recoverable storage, structural elision, and irreversible removal must remain distinct.
3. **Plan–rehearse–commit separation.** Let models propose semantic edits while deterministic harness checks enforce target validity, protected regions, atomicity, and persistence.
4. **Rejected-action evidence.** Preserve attempted invalid/protected edits; they diagnose planner risk and prove whether guards matter.
5. **Full raw transcript outside the active view.** Derived context must never overwrite authoritative audit evidence.
6. **Recovery routing as an explicit object.** Keep the sidecar locator and compact semantic trigger separate from the stored payload.
7. **Future-conditioned evaluation.** Real future turns can identify dependencies missed by generic similarity, provided this is labeled retrospective sufficiency rather than complete validity.
8. **Resource-aware commit identity.** Context policy, cache state, planner calls, and commit timing are configured-system components.

### Repair

1. **Atomize authority-bearing dependents.** Link claims, locators, obligations, artifacts, versions, corrections, and permissions inside broad spans to lifecycle eligibility and downstream checks.
2. **Split recoverability.** Record storage existence, route visibility, discovery, authorization, retrieval attempt, byte/structure reconstruction, semantic interpretation, and behavioral use separately.
3. **Use alternate-future families.** Test the realized continuation plus audit, revision, correction, handoff, rollback, and legitimate alternative-action probes.
4. **Execute continuations.** Pair future-aware judging with frozen-prefix free continuations and artifact/environment receipts; observer adequacy cannot substitute for use.
5. **Match operating points.** Sweep thresholds and compare policies at equal pruning, visible-token budget, and total resource cost with paired task/account-clustered uncertainty.
6. **Factor components.** Compare raw spans, indexed-only, planner-only, sidecar-only/fold-only, rehearsal/guard ablations, and full Self-GC.
7. **Make irreversible prune fail closed.** Require evidence that no live authority, unresolved contradiction, required literal, alternate-future dependency, or protected artifact depends on the object.
8. **Audit derived traces.** Summaries, assistant rationales, tool outputs, memory, and skill files can restate removed propositions; condition identity needs an information-flow ledger.
9. **Validate sidecar lifecycle.** Test stale pointers, deletion, access denial, corruption, crash/partial commit, concurrency, expiry, supersession, and rollback.
10. **Measure total economics.** Include planner and judge calls where relevant, cached/uncached tokens, storage, retrieval, latency, retries, failure recovery, dollars, and human review.
11. **Validate online assignment.** Predeclare eligibility and outcomes, report account/task balance and pre-periods, cluster by account, and include quality/noninferiority plus invalid-run outcomes.
12. **Bound every claim.** Keep object retention, proposition fidelity, decision sufficiency, behavioral adoption, artifact integrity, professional quality, safety, cost, and production utility separate.

## Concrete repository actions

1. **No new queue task.** The existing context-compression conformance slice, configured-component realization, evidence-view, workspace, trace, task-health, metric, reliability, and validity machinery already provide homes for these requirements. A Self-GC-specific schema would duplicate machinery and narrow the project.
2. In the next real longitudinal/workspace pilot that uses context reduction, calibrate one existing slice with: a claim-bearing artifact and live obligation; exact fold plus sidecar; mask and irreversible prune variants; stale/corrupt/unauthorized sidecars; realized and alternate futures; route discovery and byte/structural reconstruction; free continuation; artifact-state checks; and total cost receipts.
3. Predeclare a threshold sweep with pruning-matched policies and separate outcomes for storage recoverability, routing recoverability, proposition fidelity, next-action sufficiency, alternate-future sufficiency, behavioral reuse, artifact integrity, quality, and total cost.
4. Treat the paper's 84.85%, 91.27–94.58%, and 10–15% figures as unreplayed configured manuscript evidence—not calibration targets or production-effect estimates—until a sanitized versioned release supplies sessions, outputs, observer records, recovery traces, online denominators, and analysis code.

## Bottom line

Self-GC contributes a genuinely useful systems abstraction: active context is not a disposable suffix but a set of addressable objects whose lifecycle should be proposed semantically and committed under deterministic runtime controls. Stable IDs, recoverable folds, protected boundaries, rejected-action logs, lineage repair, and cache-aware commits are all stronger design ingredients than post hoc prose summary.

Its evaluation does not yet validate the strongest nouns in that design. The primary outcome is one future-aware model's judgment that a more conservative retained view still appears to support one realized continuation; no sidecar is retrieved, no continuation is executed, no artifact is checked, and no equal-pruning frontier is estimated. The online split then measures only main-agent prompt tokens under an under-specified deterministic account partition. `skill-bench` should retain the object-transaction machinery while enforcing a stricter claim ladder: **stored is not routed; routed is not recovered; recovered is not understood; understood is not used; used is not correct; and lower visible context is not lower total cost or preserved professional utility.**
