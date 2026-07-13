# Paper Review: GroundEval — Deterministic Evidence-Path Checks Need a Valid Contract Before They Can Replace a Judge

- **Paper:** https://arxiv.org/abs/2606.22737v2
- **Author:** Jeffrey Flynt
- **Date read:** 2026-07-14
- **Source:** complete immutable arXiv v2, updated 2 July 2026
- **Local PDF:** `data/papers/pdfs/2606.22737v2-groundeval.pdf` (17 pages; SHA-256 `0403ce0cee9c4628501f5a5c763e454b78b04eba62ab333dabab4b31ba14c9e9`)
- **Local text:** `data/papers/text/2606.22737v2-groundeval.txt` (SHA-256 `f8b05c0372859f4a2a0b1d7c10847e617061cef02ca5360f5a56f119a1ebbe80`)
- **Official release inspected:** https://github.com/tenurehq/groundeval, annotated tag `groundeval-preprint-v1`, commit `bb772dc857b66b7b23a4973399dd4ab1bddddac0`, tree `3ca01b86c834278052e460f35d07a7bc68b29340`
- **Local release:** `data/sources/releases/2606.22737v2-groundeval/tenurehq-groundeval-bb772dc.zip` (SHA-256 `d25ce0d330c3b2e5a59cdcdb8881c9631f3308dd29b903c8e3d3f814e6cd87e5`); provenance: `data/sources/releases/2606.22737v2-groundeval/provenance.json`
- **Version boundary:** the author-owned commit is one day after arXiv v1; its annotated tag predates v2. It is credible preprint-corresponding evidence, not proven byte-identical v2 manuscript-time code.
- **Tags:** deterministic-grading, evidence-path, access-control, temporal-validity, verified-absence, causal-contracts, trace-observability

## One-sentence contribution

GroundEval contributes a useful three-part deterministic contract for checking whether observable agent behavior stays within actor/time permissions, retrieves configured evidence, and searches before claiming absence; but the paper's experiment validates neither the contract's truth nor its completeness, the released implementation materially diverges from the paper's scoring equation and governance metric, and its “Counterfactual” track recognizes author-declared links rather than identifying causal effects.

## Why this matters for skill-bench

Knowledge-work artifacts can be correct for an invalid reason. An analyst can quote a future filing, a support agent can use a record outside the assigned role, or a researcher can claim that no evidence exists after checking one repository. Final-answer grading loses these distinctions. GroundEval therefore advances charter objectives A, B, and C through a cross-domain measurement question:

> Which observable evidence-path constraints are necessary for a defensible answer, and what evidence establishes that the configured path contract is itself fair, complete, and operationally enforced?

The paper usefully makes three obligations explicit: **entitlement** (Perspective), **configured mechanism evidence** (Counterfactual), and **search sufficiency for a negative claim** (Silence). These can sharpen `skill-bench` source packs, trace records, private checks, and validity arguments.

The title overstates the result. Deterministic checks replace model judgment only for predicates already reduced to trustworthy state and complete observers. They cannot determine source authority, professional relevance, causal truth, search-universe completeness, alternative-path equivalence, artifact quality, or decision consequences merely because the scorer returns the same number twice. The right architecture is plural: deterministic checks for typed state predicates, model or human observers for semantic/artifact predicates, and a validity argument limiting the resulting claim.

## Research question and claim boundary

The paper asks whether agent evaluation can deterministically distinguish a plausible or correct answer from one reached through an impermissible, temporally invalid, insufficiently searched, or causally unsupported evidence path (Sections 1 and 3–6, pp. 1–9).

The strongest defensible claim is:

> Given a fixed GroundEval contract, recorded runtime trace, released scorer version, and compatible adapter, the implementation deterministically computes selected exact-match, artifact-overlap, attempted-access, temporal, and configured-search-space observations for three synthetic task types.

The evidence does **not** establish that:

- the configured event log, access policy, search universe, causal link, or expected artifact set is substantively correct or complete;
- one authored evidence route is necessary when another source or procedure could validly support the answer;
- an attempted blocked fetch is equivalent to information leakage or harm;
- a declared event join establishes a causal mechanism or counterfactual effect;
- the three failure classes are common in agents, professional work, or production;
- GroundEval is more accurate than a model judge given the **same** state contract and evidence view;
- the reported aggregates, worked examples, and judge outputs are independently reproducible from the release;
- deterministic scoring establishes evaluator validity, professional capability, safety, production fitness, or readiness.

## Methodology and system

### Contract and authoring topology

The proposed pipeline observes one native agent run, drafts a contract from visible tools/returns, structurally validates it, and asks a human to correct it before reuse (Section 3.1, pp. 5–6). The contract combines an event log, artifact corpus, role/access policy, track specifications, expected answer schema, and adapter-captured trace. The scorer evaluates a state constraint rather than one exact action sequence.

This is a promising separation: the agent may choose a route, while the contract states admissible evidence boundaries and required consequences. Yet Observe Mode is not an independent oracle. It is outcome-informed authoring: one realized run determines which tools and paths enter the draft. The paper reports no reviewer count, qualifications, protocol, corrections, agreement, time, or held-out contract audit. Its own limitation section admits that unexercised preconditions and subsystems can be omitted (p. 14). Structural validation can show that a link or search space is nonempty; it cannot show that it is authoritative, exhaustive, professionally necessary, or alternative-complete.

The release makes this boundary sharper. `src/groundeval/config_schema.py:58-82` validates only known top-level keys and warns about empty tracks; it explicitly does not validate nested semantics. `src/groundeval/question_gen.py:97-243` treats the user's `CausalLinkSpec` as domain knowledge. `README.md:67-73` reduces the author input to event log, corpus, and roughly fifty lines of YAML, while `README.md:96` and `158-162` recommend asking an LLM to generate synthetic events and artifacts. This is convenient instrument construction, not evidence that generated state is a faithful domain model.

### Perspective: actor-time visibility

Perspective asks whether an actor could have known a fact by an `as_of_time`, given role/subsystem access and a visibility cone (Section 5.1, pp. 7–8). Question generation labels cases positive, permission-negative, or temporal-negative. The released runtime hides future fetches and flags blocked operations (`core.py:494-757`); the scorer combines attempted actor, subsystem, and horizon violations, evidence overlap, and dead-end recovery (`scorers.py:41-138`).

The construct is useful but narrower than “could have known.” In the released generator, the label is principally a projection of timestamp plus subsystem policy (`question_gen.py:644-793`). It does not model delegation, record-level grants, revocation, purpose limitation, confidentiality exceptions, oral knowledge, copied evidence, or whether a role actually observed a record. `EventLogPolicy` first uses participation/broadcast, then grants visibility to any remaining artifact in an accessible subsystem (`adapters.py:278-315`), so its name suggests a finer actor-event boundary than its fallback enforces.

The runtime also mixes **attempt** and **exposure**. A typed search against a blocked subsystem returns nothing, but an untyped search can return metadata—including `summary` and `description`—for inaccessible records while merely flagging a violation (`core.py:606-680`, `697-757`). Search passes `as_of` into the corpus, so future results are removed before `_record`; ordinary search therefore cannot record which future hits were suppressed. An explicit fetch of an already-known future ID can record a horizon attempt. These are different signals: policy probe, result exposure, content access, adoption, and downstream effect.

### Counterfactual: declared-link recognition, not causal identification

Counterfactual scans for the first later effect event matching an author-declared cause type, effect type, time gap, and join keys (`question_gen.py:97-206`). Its answer score assigns exact credit to `outcome_changed`, mechanism label/alias, cause and effect event IDs, direction, evidence IDs, and actors; a score of `0.80` is called correct (`scorers.py:153-337`). Trajectory credit depends on retrieving configured cause/effect artifacts and naming the internal mechanism label (`scorers.py:214-281`).

This prevents a specific error—accepting temporal adjacency without a shared identifier—but a shared ticket/account ID is not causal evidence. The config authors assert `outcome_changed`; the system performs no intervention, matched control, structural causal estimation, necessity test, or competing-mechanism adjudication. Every causal link in the five substantive released domain configs generated in the local audit had `outcome_changed: true`; the seed-42 audit produced 23 links and zero negative links. The track therefore largely tests recovery of an authored relation and exact internal labels.

The obligation may also be hidden. The public question omits artifact IDs and the internal `link_type`; the expected schema says only that `causal_mechanism` is a string (`core.py:810-852`). Exact scorer credit nevertheless requires the private config label or declared alias and private event IDs. Unless these values are validly recoverable from accessible artifacts, low scores may reflect answer-key opacity rather than causal failure. Exposing them would create the opposite problem: evaluator-cue leakage. GroundEval needs a public-basis and evidence-locator audit for every exact field.

### Silence: configured coverage, not proof of global absence

Silence identifies a trigger without a matching response within an authored window and join policy, then builds an expected search-space list (`question_gen.py:246-400`). The scorer calculates the fraction of expected artifact IDs returned or cited (`scorers.py:340-405`). This is the paper's most useful design correction: a negative answer should carry a search-basis record rather than receive binary credit from the answer alone.

But “verified absence” is too strong. Absence is verified only relative to event-log completeness, response ontology, time window, join policy, corpus synchronization, and search-space construction. The release adds every trigger artifact; selector query hits; up to five arbitrary `list_ids` entries from each named subsystem; or, without selectors, up to twenty entries (`question_gen.py:353-400`). Coverage rewards retrieving those IDs, not issuing a semantically complete query or demonstrating repository/index completeness. A failed but correctly scoped search receives no coverage; a direct fetch of all predeclared IDs can receive full coverage without proving the search system had no omitted records.

Positive Silence cases have another asymmetry: their expected set is the response artifacts plus the first ten corpus IDs (`question_gen.py:1235-1267`). That arbitrary corpus-order dependency can penalize a direct successful lookup for not retrieving irrelevant records. The score formula also collapses to `0.8 × coverage + 0.2 × horizon_d`; the separately named “premature penalty” is algebraically the same coverage term (`scorers.py:375-393`). It is not an independent observation that the agent claimed absence before finishing search.

### Scoring, aggregation, and diagnostics

The paper gives answer/trajectory weights of `0.40/0.60`, `0.50/0.50`, and `0.30/0.70` for Perspective, Counterfactual, and Silence (Table 2, p. 9). Those match `_TRACK_WEIGHTS` in `scorers.py:17-23`. It then defines:

`S_adj = w_a S_answer + w_t S_traj (1-v)^2`

and says `v` aggregates actor-gate, subsystem, and horizon violations across calls (Section 6.3, pp. 9–10).

The released implementation does something materially different. `_violation_adjusted` multiplies the **entire combined score** by `(1-v)^2` (`scorers.py:36-38`), and `aggregate` computes `v` from `actor_gate_violations` only (`scorers.py:452-518`). `_run_one` stores only actor-gate count and search coverage in result metadata, omitting subsystem and horizon counts (`run.py:488-507`). Using the paper's Perspective aggregates (`answer=.214`, `trajectory=.637`, `v=.124`) gives `0.3789` under Equation 1 but `0.3590` under release code; Table 6 reports `0.359`. Thus the table agrees with the release's whole-score multiplier, not the published equation, while the stated three-violation metric is not implementable from released result records.

The quadratic penalty and thresholds are uncalibrated policy choices. A violation rate uses tool calls as denominator, making score sensitive to harmless extra calls and allowing dilution by many compliant calls. It does not weight exposure, sensitivity, intent, effect, or severity. The paper labels a model “accurate-but-unsafe” (p. 10), but attempted access in a synthetic runtime is not a validated safety outcome.

The paper says diagnostics pair tool activity with turn-level narration (abstract and Figure 1). Released `AgentTrajectory` contains tool calls, citations, final answer, counts, tokens, and latency, but no narration/message field (`core.py:85-103`). `results_*.json` stores only `EvalResult` summaries, not the trajectory (`run.py:297-357`). The README mentions optional agent messages, but no result artifact or schema preserves them. Narration is appropriately excluded from credit, yet the claimed inspectable diagnostic surface is absent from the paper-corresponding snapshot.

## Evidence and results interpretation

### Reported experiment

The paper evaluates one DeepSeek-V4-Pro configuration at temperature zero over a synthetic OrgForge enterprise scenario: 22,530 events, 60 days, nine subsystems, 72 actors/eight roles, 25 causal-link types, 19 silence-pair types, and 96 questions—30 Perspective, 27 Counterfactual, and 39 Silence (Section 7, pp. 10–11). It compares gated tool mode with question-only zero-shot answer scores. There are no repeated trials, alternate agents, human labels, contract reviewers, uncertainty intervals, clustered estimands, invalid/missing-run ledger, cost results, or held-out domain transfer.

The reported aggregate answer/trajectory scores are respectively `.214/.637`, `.063/.357`, and `.359/.421` for Perspective, Counterfactual, and Silence (Table 5, p. 13). Table 6 reports an overall combined `.369` and adjusted `.350`. A zero-shot Counterfactual answer score of `.220` and gated `.063` is evidence that the configured tool condition did not improve this exact-field score; it is not evidence that tool use revealed causal reasoning.

### Three worked cases

The paper narrates one failure per track (Sections 8.1–8.3, pp. 11–13):

1. a Silence answer misses `CONF-PROD-002`, while prose-only Kimi-K2.6 and ChatGPT-5.5 judges score the answer `.90` and `.85`;
2. a Perspective answer crosses the configured `hr_ops`/Zoom boundary seven times;
3. a Counterfactual answer misses a configured downstream Slack artifact and internal coordination mechanism.

These examples illustrate why a state contract can reveal information unavailable in prose. They do **not** compare evaluator validity. The judges receive only question and prose, while GroundEval receives private ground truth, access policy, expected artifact set, and trace. Any observer deprived of decisive evidence must abstain or guess. A fair comparison would give human and model observers the same trace/contract, separately test each predicate, and compare against independently adjudicated labels. The experiment instead demonstrates evidence-view insufficiency “by construction.”

### Release audit and executable evidence

The archived release contains 176 files: nine source modules, six test modules, six example domains (five substantive plus `tiny`), 202 example events, 127 JSON artifacts, configs, documentation, and packaging files. It contains none of the paper's 22,530-event corpus, 96 generated questions, three worked traces, judge prompts/outputs, run-level results, invalidity ledger, or aggregate-analysis artifacts. Searches found none of the headline IDs or scores. Every headline empirical value therefore remains manuscript-only.

The local release test suite passed: **82 tests in 0.15 seconds**. This supports internal behavior of selected functions, not paper-result reproduction or contract validity. A seed-42 local generation audit over the five substantive examples produced:

| Domain | Events | Artifacts | Causal links | Absence / confirmed | Generated questions (P/C/S) |
|---|---:|---:|---:|---:|---:|
| cybersecurity | 42 | 25 | 4 | 3 / 12 | 40 / 4 / 15 |
| enterprise-support | 44 | 34 | 10 | 4 / 7 | 22 / 7 / 10 |
| finance | 37 | 23 | 3 | 5 / 5 | 37 / 3 / 10 |
| healthcare | 40 | 22 | 5 | 7 / 4 | 34 / 5 / 11 |
| legal | 35 | 21 | 11 | 6 / 5 | 34 / 6 / 11 |

This shows the code can index and generate compact synthetic examples. It does not reproduce the paper. It also exposes an implementation issue: `_build_perspective_for_actor` computes four pivot events but the target-event loop is outside the pivot loop (`question_gen.py:632-730`), so only the last sampled pivot contributes. The documented per-actor cap can also be exceeded; cybersecurity generated 40 Perspective questions despite five actors and a nominal cap of five per actor. No test checks these invariants.

### Supported, partial, and unsupported claims

**Strongly supported:** fixed code produces deterministic outputs for a fixed trace/contract; exact state predicates can expose failures hidden from final-answer-only views; the release provides reusable config/index/scoring machinery and passing unit tests; answer and path observations should remain separate.

**Partially supported:** the three tracks are useful authoring patterns, but their substantive validity depends on external authority/completeness evidence; the examples show plausible failure signatures, but not prevalence; the release corresponds to the preprint, but not provably to v2 or the reported experiment.

**Not supported:** general replacement of LLM-as-judge; validated causal reasoning; global verified absence; safety measurement; common failure prevalence; professional validity; capability; production fitness; readiness.

## Unique insight

GroundEval's deepest transferable contribution is not “judge-free evaluation.” It is the recognition that an answer may need a **proof-carrying evidence-path claim**. But deterministic execution sits late in a longer validity chain:

```text
public requirement / affected-party authority
→ authoritative state sources and valid-time policy
→ claim-specific admissible evidence universe
→ alternative-complete path or sparse necessary checkpoints
→ adapter observation and information-flow stages
→ deterministic predicate observations
→ semantic / professional observations where needed
→ aggregation and loss policy
→ bounded claim and decision
```

Four distinctions are essential:

1. **Contract determinism vs contract validity.** Repeating the same authored rule perfectly does not show that the rule represents the profession, stakeholder, source universe, or causal mechanism.
2. **Access attempt vs information effect.** Search, result exposure, page/content access, model visibility, citation/adoption, action, and consequence are separate stages. A blocked call can be a valuable canary without being a leak or harm.
3. **Witness path vs necessary path.** A known artifact set can prove one sufficient route. Penalizing every other route requires evidence that the set is complete or that sparse process checkpoints are genuinely part of the construct.
4. **Configured dependency vs causality.** A join key supports entity linkage; a counterfactual effect requires intervention or a warranted causal model. Exact mechanism-label recovery is not causal reasoning.

This extends, rather than replaces, existing project evidence:

- **ClawArena** types source authority, valid time, contradiction, supersession, and belief change; GroundEval adds actor-time gates and negative-claim search obligations, but its state authority is less contested.
- **Workspace-Bench** distinguishes availability, authored relevance, observed access, and causal use, and warns that dependency graphs are hypotheses. GroundEval observes access attempts but similarly risks canonical-path scoring.
- **LongMedBench** shows that a retrospective event is not automatically a valid decision oracle. GroundEval's event log likewise needs authority and decision-time necessity evidence.
- **BigFinanceBench** shows that narrated derivation checkpoints are not audited workflow evidence. GroundEval improves machine observability but can still encode hidden exact labels and one authored route.
- **RuVerBench/AgentRewardBench** show that evidence view and observer configuration define judge agreement. GroundEval's asymmetric prose-only comparison is therefore an evidence-view ablation, not a judge-accuracy contest.
- Existing provenance-observation and alternative-path conformance machinery already supplies homes for source/observation separation, insufficiency outcomes, and equivalent paths; a new GroundEval-specific subsystem would duplicate them.

## Limitations and validity threats

1. One synthetic corpus, one tested model configuration, one temperature, and one attempt per question do not estimate general agent behavior.
2. The corpus comes from the author's OrgForge system; no independent domain source or professional validation is reported.
3. No author/reviewer protocol, qualifications, correction log, agreement, time, or contract acceptance criteria are reported.
4. Observe Mode drafts from realized behavior and can omit unexercised requirements; review is an unmeasured rescue step.
5. Structural nonemptiness does not validate authority, completeness, fairness, necessity, or alternative paths.
6. Access policy is a simplified role/subsystem projection; real purpose, record, project, revocation, delegation, and affected-party rules are absent.
7. Runtime search can expose metadata for inaccessible records while only flagging it; attempt, exposure, adoption, and consequence are collapsed.
8. Horizon violations are not observable for ordinary searches whose corpus adapter filters future hits before trace recording.
9. Perspective's “could know” label is broader than actual observation and narrower than real organizational knowledge.
10. Counterfactual labels are authored assertions; event joins and temporal order do not identify causal effects.
11. Released examples contain no negative `outcome_changed` causal links in the local audit.
12. Exact private mechanism/event-ID scoring risks hidden-obligation failure or evaluator-cue leakage.
13. Silence proves absence only within an assumed complete event ontology/window/join/corpus.
14. Expected search spaces are outcome-informed artifact lists and arbitrary list prefixes, not validated search-universe completeness.
15. Positive Silence cases include the first ten corpus IDs, making scores depend on irrelevant corpus order.
16. “Premature penalty” duplicates coverage algebraically and does not observe answer timing.
17. Fixed answer/trajectory weights, `.80` causal threshold, `.50/.70` diagnostic cutoffs, quadratic compliance exponent, and tier thresholds are uncalibrated.
18. Tool-call denominators allow governance rates to change with harmless extra calls and ignore severity/effect.
19. The paper's Equation 1 and released/table implementation disagree about which score components receive the compliance multiplier.
20. The stated violation rate includes three types, while release aggregation records only actor-gate violations.
21. Structured diagnostics with turn narration are not preserved in released trajectory/result schemas.
22. The perspective generator's pivot indentation and cap behavior contradict documented sampling logic.
23. No repeated-run uncertainty, question/case clustering, confidence intervals, or missing/invalid ledger is reported.
24. Zero-shot and gated conditions differ in tools, context, step budget, and opportunity for format/tool failures; answer gaps are not attributable only to corpus access as claimed on p. 10.
25. Prose-only judges and GroundEval receive unequal decisive evidence, so their scores do not estimate relative evaluator accuracy.
26. “Common rather than exceptional” is unsupported by 96 selected synthetic questions and three anecdotes.
27. The release lacks the empirical corpus, questions, traces, judge outputs, and results, blocking aggregate verification.
28. The author-owned tag predates v2; paper/release discrepancies cannot be assigned confidently to a bug, later manuscript change, or unreleased implementation.
29. No license is declared in the pinned archive, limiting straightforward reuse despite source availability.
30. No evidence supports professional validity, capability, safety, production fitness, or readiness.

## Reproducibility and operational realism

Reproducibility is **good for selected scorer/generator mechanics, poor for the paper experiment, and unvalidated for substantive contracts**. The immutable paper specifies track formulas, corpus scale, question counts, one model, and aggregate tables. The complete pinned code snapshot is compact and testable; all 82 tests passed locally. Five substantive example domains can generate questions from event/config/artifact bundles.

Exact reproduction is blocked by absent paper corpus, generated question set, reviewed contracts, model endpoint/version record, prompts and raw responses, trajectories, judge prompts/outputs, retry/invalid records, result JSON, seeds, usage/cost, and analysis code. The version boundary matters because the paper's equation, table, and release disagree, and the release does not retain the claimed narration diagnostics.

Operational realism is low to moderate. Role-scoped tools, time boundaries, event/artifact joins, multi-repository absence checks, and observable retrieval are realistic structural ingredients. The supplied domains are small handcrafted/LLM-generatable JSON worlds, not production ACLs, mutable search indices, partial observability, concurrent work, legal purposes, source-system failures, or professionally validated causal models. The paper-scale corpus is synthetic and unavailable. “Start synthetic, graduate to production” is a roadmap, not transfer evidence.

## Transfer to skill-bench

### Preserve

1. **Dual observation:** keep answer/artifact consequence separate from evidence-path admissibility.
2. **Actor-time policy:** bind each source observation to actor/role, purpose, valid interval, subsystem, and policy version.
3. **Negative-claim basis:** require a search-universe and completeness claim before crediting “none found.”
4. **Observable external traces:** grade tool requests, returned evidence, citations, and state changes rather than private chain of thought.
5. **Fail-closed diagnostics:** return `unsupported`, `insufficient_evidence`, `policy_attempt`, and `observer_invalid` instead of forcing every case into right/wrong.
6. **Reusable state predicates:** deterministic checks are valuable regression gates after instrument qualification.

### Repair

1. **Version the whole contract transaction.** Hash task, public requirement, state sources, ACL/time policy, adapter, tool responses, trace, scorer, weights, aggregation, and validity record.
2. **Represent the information-flow ladder.** Distinguish request → result exposure → content access → model visibility → citation/adoption → action → consequence; do not call attempted access a leak or safety failure without later stages.
3. **Type search completeness.** Record universe owner, source/index coverage, snapshot time, query/operator semantics, pagination, truncation, inaccessible/missing systems, and residual uncertainty. A negative answer should be “not found within U under Q at T,” not globally absent.
4. **Admit alternative paths.** Store sufficient evidence sets or sparse necessary checkpoints with authority and equivalence status. Mutate omitted valid paths and irrelevant retrieved artifacts to measure scorer soundness/completeness.
5. **Rename configured causal checks.** Use `declared_dependency_recognition` unless intervention, causal-model warrants, rival mechanisms, and qualified adjudication support a counterfactual claim.
6. **Separate contract derivation from scoring.** Freeze contracts before candidate trials; blind reviewers to candidate outcomes; preserve reviewer changes; validate on held-out planted cases.
7. **Calibrate aggregation.** Keep each violation type/severity visible; do not multiply a scalar until loss/decision evidence justifies it. Report exact denominators and clustered uncertainty.
8. **Use equal evidence views for evaluator comparison.** Compare deterministic, model, and human observations predicate by predicate against independent labels; use prose-only judges only as an explicit insufficient-view control.
9. **Preserve full immutable trajectories.** Store requests, filtered/unfiltered result identities where policy permits, gate decisions, adapter errors, final answer, and optional narration as non-credit diagnostic evidence.
10. **Maintain strict claim ceilings.** A passing conformance fixture licenses exact observer behavior on that fixture, not causality, absence completeness, safety, professional quality, or readiness.

## Concrete repository actions

1. **Do not add a GroundEval-specific schema or grader.** Existing benchmark-bundle traces, information-flow stages, provenance-observation derivation, alternative-path checks, artifact admissibility, task health, metrics, and validity arguments already cover the required objects.
2. **Add one consolidation task** to integrate the verified-absence and actor-time evidence-path boundary into `docs/benchmark-design-taxonomy.md` and `docs/research-synthesis-index.md`: contract authority/completeness before deterministic scoring; request/exposure/access/adoption/effect stages; configured dependency versus causality; search-universe semantics; equal-evidence observer comparison; and the paper/release scoring discrepancy.
3. **If a future pilot needs negative claims**, add a small cross-domain conformance slice to an existing pilot rather than a new subsystem: complete and incomplete search universes, valid alternate source, inaccessible source, empty result, truncated pagination, direct known-ID retrieval, and stale index. Freeze observer inputs before expected labels and preserve insufficiency separately from contradiction.

## Action items

- [x] Read the complete immutable v2 PDF/text through references.
- [x] Inspect the complete 176-file author-owned preprint snapshot with explicit v1/v2 timing boundary.
- [x] Run the release test suite: 82 tests passed.
- [x] Audit all core data models, adapters, generators, runtime gates, scorers, aggregation, configs, examples, and tests.
- [x] Reconstruct Perspective, Counterfactual, Silence, dual scoring, compliance adjustment, and reported experiment.
- [x] Search for every headline artifact ID, trace, score, and result artifact; none is present in the release.
- [x] Generate seed-42 structural audits for all five substantive released example domains.
- [x] Identify equation/table/code disagreement, omitted violation types, missing narration records, Perspective sampling/cap defects, untyped-search exposure, search-universe limitations, and declared-link causal overclaim.
- [x] Compare nonduplicatively with ClawArena, Workspace-Bench, LongMedBench, BigFinanceBench, RuVerBench/AgentRewardBench, and existing provenance/alternative-path machinery.
- [ ] Consolidate the bounded evidence-path contract into canonical synthesis; no new GroundEval-specific subsystem is justified.
