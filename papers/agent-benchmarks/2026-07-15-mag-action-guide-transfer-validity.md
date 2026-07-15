# MAG: same-trajectory guide overlap is not yet reusable procedural transfer

## Source and evidence status

**Deep review of the complete immutable primary source.** I read the full 25-page arXiv v2 paper, including all appendices, and checked the extraction against the local PDF identity.

- **Paper:** Chengguang Gan, Hanjun Wei, Yunhao Liang, Zhixi Cai, Qinghao Zhang, and Shiwen Ni, *MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation*
- **Immutable version:** https://arxiv.org/abs/2607.10079v2 (updated 14 July 2026)
- **Date read:** 2026-07-15 UTC
- **Local PDF:** `data/papers/pdfs/2607.10079v2-mag.pdf` (25 pages; SHA-256 `cb2e0437e09dcaf96ffb255659d0474343b5a8fd06503a1f2296f992a198646f`)
- **Local text:** `data/papers/text/2607.10079v2-mag.txt` (SHA-256 `38405263cfec6b34d1fd3733e86f58c2f11cae7f33588b1a07f7f918a4442271`)
- **Metadata:** `data/papers/source/2607.10079v2-metadata.xml`
- **Release status at review time:** the paper repeatedly says the corpus, harness, checkpoints, and metric implementation are released, but v2 contains no project/code/data URL. The arXiv HTML external links contain only model cards, Qwen weights, funders, and arXiv infrastructure; exact-title and arXiv-ID web searches and GitHub repository API searches returned no author-owned MAG release. No code, data, screenshots, guides, tasks, trajectories, checkpoints, evaluator, or results were therefore inspected or executed. The empirical evidence below is manuscript-reported.
- **Tags:** action-guide coupling, instructional artifacts, recipient utility, web agents, trajectory projection, guide metrics, grounding, release inspectability

> **Timing boundary.** “No release” means no verifiable paper-associated release was linked or locatable on 2026-07-15 UTC. It does not mean that the authors cannot publish one later. A later artifact would need its own commit/revision and paper-correspondence audit.

## One-sentence contribution

MAG creates a useful compound task in which one screenshot-driven agent both acts in a self-hosted WebArena environment and emits a user-facing instruction at every step, but its successful-path-derived references, research-team review, single-reference n-gram scoring, success-gated aggregate, and absent recipient execution study identify **same-trajectory instructional narration** far more directly than correct, complete, maintainable, or transferable procedural guidance.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, and C through a cross-domain question that existing execution, Skill, and handoff reviews do not fully answer:

> When can an executed work trace be transformed into a procedural artifact that an independent future actor can use under a changed but legitimate work state?

The question is not web-specific. The output might be a laboratory runbook, financial-model operating note, incident-response playbook, research protocol, onboarding walkthrough, review checklist, or successor instruction. In every case, an actor can complete the source task while producing an incomplete or misleading guide; conversely, a useful guide may describe a valid route different from one reference trajectory.

MAG’s strongest design move is to require an instruction **at the action boundary**, while the page state and target are still available. That creates proposition-level provenance opportunities that post-hoc summarization loses. Its evidence does not close the recipient side. The benchmark evaluates whether guide text resembles one guide generated from one successful path—not whether a separate person or agent, without privileged action IDs or trajectory state, can use it to reproduce the goal, recover from divergence, or survive interface drift.

This is narrow expansion, not a commitment to web automation or Digital Adoption Platforms. The general hypothesis is that execution can generate reusable procedural knowledge. Useful completion requires independent evidence at each source→artifact→recipient link.

## Research question and defensible claim boundary

The paper asks whether multimodal web agents can jointly complete multi-step tasks and write one short user-facing instruction per step, whether Set-of-Mark versus coordinate action grounding changes performance, and whether successful GPT-5.5 trajectories can restore reinforcement-learning signal for a 9B model (Sections 1, 3–6, pp. 1–8).

The strongest defensible empirical claim is:

> Under the authors’ unreleased harness, self-hosted WebArena snapshots, inherited OpAgent-solvable task subset, action parser, WebArena checkers, semantic-answer judge, one successful-path-derived guide reference, and fixed aggregate policy, the reported single greedy sweeps show low configured-system task success and model-specific grounding differences; one SoM 9B training run improves paired test success from 6.9% to 13.2%, while reference-overlap guide scores also increase.

The evidence does **not** establish that:

- predicted guides are factually faithful to the action actually executed or to the resulting state;
- a guide is complete enough for a first-time independent recipient to reproduce the task;
- guide generation causes better execution, because prior guide text is also the agent’s only textual state memory;
- a completed source trajectory has been faithfully codified rather than narrated in a reference-like style;
- reference overlap measures semantic correctness, alternative-path validity, recovery support, accessibility, or professional usability;
- the success-gated guide score is a validated user-value or deployment metric;
- the 82% reference-guide “usefulness” result comes from first-time users executing tasks;
- successful GPT-5.5 trajectories are expert demonstrations or tacit domain expertise;
- the reported SoM gain transfers to unseen sites, substantially unseen templates, other recipients, other action interfaces, or later UI versions;
- one-seed results establish reliability, expected cost, maintenance savings, professional validity, production fitness, or readiness.

## Methodology and system

### Task and environment

An episode contains a natural-language intent, an initial page state on one of six WebArena sites, and an inherited functional checker. At each step, the model sees a 1440×900 screenshot with numbered marks plus a textual candidate menu and its own prior guide sentences. It jointly emits a private `think`, one of seven actions, grounding/payload fields, and a one-sentence `guide_text`. Episodes end on `finish` or after 25 steps (Section 3.1, pp. 3–4; Appendix C–D, pp. 13–16).

The paper calls this “live evaluation,” but the sites are **self-hosted WebArena sandboxes populated with synthetic content**, not mutable public production services (Ethics Statement, p. 9; Appendix A, p. 11). Runtime state is interactive, and containers are reset, accounts re-registered, and logins verified. That is meaningful environment machinery. It supports a bounded synthetic web-state claim, not production-site realism, real DAP deployment, user-data handling, or external organizational consequence.

The source population is outcome-conditioned twice:

1. OpAgent supplies successful coordinate demonstrations for 581 of WebArena’s 812 tasks.
2. Capture/filtering leaves 563 fully annotated tasks: 396 train and 167 test.

The benchmark split is nevertheless stated over all 581 as 407 train/174 test. Success is reported over 174 test tasks; guide metrics are reported over 171 tasks with references; annotated-corpus tables contain 167 test tasks (Sections 3.2–3.3, pp. 4–5; Appendix A, p. 11). The paper explains that three captures failed entirely, but does not reconcile the additional four referenced test tasks with the 167 fully annotated test-task corpus. These are different denominators and should have an explicit membership/disposition ledger.

Because source inclusion requires a prior agent success, MAG does not sample WebArena, DAP authoring demand, or knowledge work. It samples a strong prior agent’s demonstrated-solvable subset. The authors appropriately state that its scores are not comparable with WebArena leaderboards (Section 3.2, p. 4).

### Gold trajectory and guide construction

Recorded coordinate demonstrations are replayed on the sites. Screenshots and Set-of-Mark candidates are captured; GPT-5.5 receives the task, screenshot, action, and prior guides and drafts a rationale and instruction. Rule filters reject replay mismatches, malformed guides, unsupported verbs, and unmapped targets. Three research-team annotators then inspect and edit guides in a purpose-built interface (Section 3.2, pp. 4–5; Appendix B, pp. 12–13).

This pipeline has useful lineage: a guide is attached to a specific task, page image, target action, and prefix. But its authority and transformation evidence are weak:

- all trajectories were selected because they already passed the source evaluator;
- action correctness is only spot-checked during guide review;
- the paper does not say whether all three annotators independently rated each guide or divided the workload;
- annotator qualifications, guideline, independent labels, edit counts, disagreement, adjudication, and criterion-level decisions are absent;
- all annotators are paper authors/research-team members, not intended users, DAP maintainers, or domain professionals;
- guides were reviewed against 1280×720 captures, then released-corpus pages were recaptured at 1440×900 and actions realigned;
- no post-recapture human equivalence review is reported.

The SoM projection itself drops 1,019 of 4,768 element steps (21.4%) because they map to no candidate. An anchor audit flags 3.9% of SoM click targets as suspect, especially under overlay menus. The SoM and coordinate views therefore do not differ only in action grounding: they can contain different step sequences and guide completeness (Appendix A–B, pp. 11–13).

The paper’s own 50-task audit finds seven references useless and two ambiguous. It attributes most failures to dropped SoM terminal controls. That is not a superficial wording issue: a guide that stops before submission can be locally fluent and globally unusable.

### The “82% useful” evidence is an author judgment, not recipient execution

Appendix B says **one author** rated 50 randomly sampled test references as useful, ambiguous, or useless, where “useful” meant that a first-time user *could* complete the task by following the guide alone. The result is 41/50 useful (82%; Wilson 95% interval 69.2–90.2%), two ambiguous, and seven useless (p. 13).

No first-time user followed a guide. There is no participant count, execution log, completion rate, time, error, clarification, recovery, comparison condition, or independent rater. Thus the main text’s phrase that 82% “let a first time user complete the task” (p. 4) overstates the protocol. The evidence is a single author’s prospective usefulness rating of gold references.

Even this audit concerns the **reference layer**, not model-generated candidate guides. It provides no calibration between BLEU/ROUGE, GGS, and recipient success.

### Action and guide output contract

The output parser extracts one JSON object with five keys. The guide must be a direct user-facing sentence and must omit mark IDs, coordinates, DOM details, and selectors. OFCR checks parseability, action-field validity, and regex-defined leakage. A malformed step consumes budget but executes nothing (Section 3.3 and 4.1, p. 5; Appendix C–D, pp. 13–16).

This is a valuable separation between machine action coordinates and human-visible language. OFCR is still contract conformance, not guide correctness. The reported absence of leaked IDs/coordinates says the tested systems followed a narrow surface rule; it does not show that the visible target is uniquely identified, that the instruction matches the executed action, or that a recipient can locate it.

The guide history is the **only textual state carried across steps** (Section 3.1, p. 3). This makes the design operationally interesting but causally entangled:

```text
emitted guide
→ next-step model memory
→ later action choice and success
→ later guide context
```

A guide is simultaneously a candidate user artifact and internal scaffold. The study has no action-only history control, private-state control, independently supplied guide-history control, or corrupted-guide intervention. It therefore cannot attribute execution differences to joint generation, explainability, memory quality, or guide utility separately.

### Task-success observer

Most tasks use inherited WebArena functional checkers over final URL, page content, program queries, state, and returned answer. Twenty-nine of 174 test tasks use a fixed GPT-5.5 semantic-answer judge that sees only the answer and reference (Section 3.3, pp. 4–5; Appendix D, pp. 15–17).

The authors rerun all 435 saved semantic verdicts—29 tasks × 15 runs—with Gemini and Claude judges. Gemini agrees with GPT-5.5 on 94.9%; Claude is more lenient and agrees at 79.1% with GPT-5.5 and 82.8% with Gemini. No interpreted ordering changes (Appendix F, p. 17). This is useful observer-sensitivity evidence, but not human correctness calibration. It also covers only semantic-answer tasks, not the inherited functional checkers, guide references, or guide metrics.

A successful endpoint verifies selected encoded state/answer consequences. It does not verify that every action was legitimate, that the guide described the realized path, that collateral state was preserved, or that an independent recipient can follow the procedure.

### Guide metrics and aggregation

For each task, all predicted guide sentences are concatenated in step order and compared with the concatenated single gold guide using equal-weight BLEU-1, BLEU-2, ROUGE-1, and ROUGE-L. `G` is their mean. `GGS = S × (0.4 + 0.6G)` sets every failed trajectory to zero and maps every successful trajectory into `[0.4, 1]`. `SR − GGS` is called “guide tax” (Section 3.3, p. 5; Appendix D, pp. 15–16).

Gating is directionally sensible: fluent narration attached to failed work should not receive deployment credit. It does not validate the guide. The instrument has major construct problems:

1. **One path is treated as the text target.** A successful alternative route is penalized by design, even if its guide is better for users.
2. **Concatenation erases state alignment.** The metric does not establish which instruction belongs to which observed page, target, action, or resulting state.
3. **N-gram overlap is not procedural correctness.** It cannot validate target identity, preconditions, postconditions, omitted steps, prohibited actions, recovery branches, or recipient comprehension.
4. **The gate inherits endpoint-observer limits.** A selected final-state pass does not certify intermediate instructions.
5. **The 0.4 floor is an authored product policy.** A successful trajectory with an unusable guide still receives at least 0.4; no stakeholder loss or acceptance study supports that compensation rule.
6. **“Guide tax” mixes phenomena.** It includes wording variation, path divergence, trajectory-length mismatch, reference defects, tokenization, and actual guide error.
7. **Metric denominators conflict.** Section 3.3 and Table 1 say guide-bearing metrics average over 171 referenced test tasks, while Appendix D says GGS averages over all 174. No released scorer resolves the discrepancy.

Teacher-forced GACS adds action agreement, guide-head-verb matching, token-F1 target anchors, and heuristic referent sufficiency. This can localize projection defects, but it is evaluated against the same path and target strings. “Deterministic” means reproducible under an implementation, not independently valid or “dependency free”: target strings, verb lexicon, anchor extraction, F1 thresholds, tie rule, coordinate tolerance, and gold path are authored dependencies (Appendix D, pp. 15–16).

### Training design and “expert” trajectories

Stage 1 fully finetunes Qwen3.5-9B separately for SoM and coordinate outputs on 3,308 and 4,018 gold steps from 396 annotated train tasks. It raises output-format correctness from 19%/14% to roughly 97% but does not improve task success reliably (Section 4.2, p. 6).

Stage 2 pre-rolls GPT-5.5 twice on 407 training tasks, caches only evaluator-passing trajectories, and adds up to two cached rows to groups of six policy rollouts. The two teacher passes solve 112 and 122 tasks, 139 in union and 95 in both. Binary task success is the only RL reward; guides receive no direct RL reward. One ten-round run is conducted per grounding scheme (Sections 4.3–5, pp. 6–8; Appendix E, p. 16).

Calling these rows “expert trajectories” describes reward status, not expertise. GPT-5.5 is a frontier model under the same benchmark prompt and checker. No human expert authored the trajectory, no domain expertise was elicited, and no independent user accepted its guide.

The SoM result is supported better than many one-run benchmark claims: paired task comparison gives +6.3 success points from SFT to round 10 (17 gains, six losses; task bootstrap 95% CI +1.1 to +11.5), while coordinate change is +0.6 points (CI −3.4 to +4.6). The difference between grounding-mode gains still crosses zero (CI −0.6 to +12.1), which the authors appropriately avoid calling proven (Section 6 and Appendix F, pp. 8, 17).

The six-sample analysis also shows pass@6 rising from 14.4% to 21.3% (21 tasks only GRPO, nine only SFT; CI +1.2 to +13.2). This argues against a **pure probability-concentration account on the same task form**. It does not establish “new capability” in the stronger transfer sense: 159/174 test intents share templates with training, the unseen-template slice has only 15 tasks, and the tuned model gains no count over SFT there (Appendix F–G, pp. 16–18).

The plain-GRPO comparison is explicitly documentary rather than controlled. Ten prior configurations vary rewards, curricula, penalties, KL, duration, fresh training batches, and judge routing; one used an inflated stub judge. They do not form a fixed-test ablation against the selected expert-augmented run (Appendix H, p. 18).

### Results and uncertainty

Reported greedy success over 174 test tasks ranges from 1.7% to 37.4%. GPT-5.5 coordinates is best at 37.4%; Gemini shows a large SoM advantage; Claude and GPT-5.5 show small grounding differences. The best trained 9B SoM row reaches 13.2%. The guide-overlap score rises with the successful SoM GRPO row even though guide text is not rewarded directly (Table 1 and Section 6, pp. 8–9).

These results support three bounded observations:

- format conformance can be learned without task competence;
- grounding interface effects are configured-model-specific;
- success and same-reference guide overlap are positively associated in this setup.

They do not show that task competence produces recipient-usable explanation. On round 10, `G` is .369 for successful episodes and .256 for failed episodes; this association can reflect shared task difficulty, closeness to the reference path, trajectory length, guide-as-memory effects, or better local target selection. No recipient outcome is observed.

The authors report task bootstraps for selected paired contrasts and six-sample pass@k, which is welcome. Main API rows and training rows are still single sweeps; training has one seed per grounding scheme; API deterministic settings are unavailable; environment/provider invalidity and retries are not tabulated; task intents are template-clustered; and no site/template-clustered interval is reported. Costs, tokens per completed task, wall time, API spend, annotation time, guide-review burden, and maintenance burden are absent.

## Evidence and claim assessment

### Strongly supported by the manuscript

1. A compound action-plus-instruction interface can be precisely specified over screenshot observations.
2. Machine-only action grounding can be kept out of user-facing guide text with a parser/regex contract.
3. The reported source and split denominators reveal substantial outcome-conditioned selection from WebArena.
4. The reported configured systems have low task success under the 25-step compound protocol.
5. Grounding preference varies by model configuration.
6. In one SoM 9B run, expert-augmented training improves paired same-form test success and pass@6 relative to its SFT anchor.
7. Gold SoM projection drops many coordinate steps and can produce incomplete guide paths.

### Partially supported

- **Action-grounded guide annotation:** every retained guide is tied to a successful source action and reviewed, but review independence, action correctness, edit lineage, post-recapture validity, and recipient authority are incomplete.
- **Reference-guide usefulness:** one author’s stratified 50-task judgment suggests many gold guides look usable, but no user execution validates that inference.
- **Guide/success coupling:** overlap is higher on successful episodes, but shared difficulty, reference-path proximity, length, and guide-memory effects are not isolated.
- **Training-induced guide improvement:** corpus overlap metrics rise without direct guide reward, but no independent semantic or recipient measure confirms improved guide quality.
- **Live environment:** runtime execution and reset are real within self-hosted replicas; production websites, external users, and operational consequences are not.

### Unsupported

- first-time-user completion from model-generated guides;
- faithful codification of tacit expertise;
- independent procedural transfer;
- correctness/completeness under alternative paths;
- maintenance under interface or content drift;
- deployment-ready DAP overlays;
- labor or cost reduction;
- professional usability, capability, reliability, safety, production fitness, or readiness.

## Unique insight

> **A guide is a versioned recipient-facing projection of a trajectory, not a by-product certified by the trajectory’s success.**

The transferable claim ladder is:

```text
source task / public requirements / environment version
→ executed action and observed pre/post state
→ selected guide proposition and source-event locator
→ proposition truth, scope, ordering, and omission status
→ assembled procedure with alternate paths and recovery branches
→ recipient-visible environment and evidence entitlement
→ recipient interpretation, target localization, and justified action
→ independent completion, preservation, errors, burden, and cost
→ transport across task/interface/version changes
→ maintenance detection and repair
→ professional acceptance and downstream consequence
```

MAG directly observes the first two links, drafts the third, and applies a limited author review around local clarity. Its n-gram metrics compare textual projections without validating the remaining links.

This ladder produces five durable distinctions for `skill-bench`:

1. **Source success vs proposition truth.** A passing endpoint does not make every narrated step correct, necessary, safe, or complete.
2. **Local action grounding vs procedural completeness.** A sentence can identify the right current button while omitting submission, verification, exception handling, or a later dependency.
3. **Text resemblance vs recipient utility.** Reference overlap is an authoring-conformance signal; independent execution, correction burden, and consequence are recipient outcomes.
4. **Episode memory vs reusable procedure.** MAG feeds prior guides back to the producer. A recipient receives an external artifact under a possibly different state. Those are different interventions.
5. **Current usability vs maintainability.** Even a successful frozen-version guide can become stale when labels, permissions, workflows, or interfaces change. Detecting and repairing drift is a separate lifecycle claim.

### Comparison with adjacent reviewed evidence

- **LH-Bench:** LH-Bench starts from an expert procedure and maps it to trace/artifact evidence; MAG starts from a successful trace and projects user instructions. Together they expose opposite transformation directions. Neither direction inherits validity: shared task/rubric authorship can cue compliance, while successful action can launder one path into a “guide.” Independent public guidance, private consequence checks, and recipient outcomes remain necessary.
- **AFTER:** AFTER separates source-context gain, equivalent-form reuse, changed-context transport, and cross-model consumption. MAG evaluates same-task, same-environment reference resemblance. Its 15 unseen intent-template tasks do not test guide consumption. A MAG guide would need typed source→recipient transfer edges across held-out tasks, roles, interfaces, and versions before procedural-transfer language is warranted.
- **DeskCraft:** DeskCraft separates authored interaction opportunity from participant receipt, adoption, endpoint effect, and burden. MAG needs the analogous recipient chain. Displaying an instruction next to an element is an opportunity; it is not evidence that the user understood, followed, benefited from, or accepted it.
- **Handoff Debt:** Handoff Debt freezes work state and varies successor-visible context, measuring takeover-side effort and endpoint outcomes. MAG should borrow that matched recipient design: freeze a target state, vary no guide/reference guide/model guide/corrupted guide, and include generation plus verification cost. A guide is episode-general procedure rather than an episode-specific handoff, but both are recipient-relative artifacts.
- **AgentRewardBench:** success checkers and model judges are observers with predicate-specific errors and evidence views. MAG adds a guide observer whose decisive evidence is only one text reference. Recipient execution and proposition-grounded human review should be separate immutable observations, not assumed from BLEU/ROUGE.
- **Artifact-admissibility and trace machinery:** existing `skill-bench` records can bind guide clauses to source events, page/artifact states, public requirements, observer views, and downstream trials. No web- or DAP-specific schema is justified.

## Limitations and validity threats

1. The claimed corpus, harness, checkpoints, metric code, prompts-as-files, trajectories, and results were not linked or locatable at review time.
2. No paper-time release commit or revision can be identified, so exact reproduction and paper/release correspondence are absent.
3. The task frame is 581 successful OpAgent demonstrations out of 812 WebArena tasks, not a representative sample of WebArena, DAP work, or knowledge work.
4. Selection is outcome-conditioned on one prior agent and checker package.
5. The reported 174 test, 171 reference-guide, and 167 fully annotated test denominators are not fully reconciled.
6. “Live” refers to interactive self-hosted sandbox replicas, not production services.
7. Six sites and mostly shared train/test intent templates limit task and interface transport.
8. Only 15 test tasks have unseen intent templates; trained gains do not exceed the SFT count there.
9. All guide references derive from one successful trajectory; accepted alternative paths and guide sets are not represented.
10. Coordinate-to-SoM projection drops 21.4% of element steps, changing trajectory and guide completeness.
11. A 3.9% suspect-target audit indicates mapping defects concentrated in overlays.
12. Eleven annotated test demonstrations exceed the 25-step budget, so the witness path is not executable under the evaluation budget for those tasks.
13. The guide-review capture resolution differs from the released/evaluation resolution, with no reported post-recapture human validation.
14. Three research-team annotators are not independent intended users or domain authorities.
15. It is unclear whether all three independently label each guide or share the corpus.
16. Annotation guideline, initial labels, edits, disagreements, agreement, adjudication, qualifications, and time/cost are absent.
17. Action correctness is only spot-checked during guide review.
18. The 82% usefulness check is one author’s prospective rating, not first-time-user execution.
19. The usefulness sample validates references only, not model outputs or automatic metrics.
20. No human recipient, DAP maintainer, professional, accessibility reviewer, or downstream stakeholder is observed.
21. Guide text is also the producer’s only textual state memory, confounding guide generation, state tracking, and action success.
22. No action-only, private-memory, supplied-history, omitted-guide, or corrupted-guide control separates the coupling.
23. OFCR validates format and narrow regex leakage, not semantic target grounding or usability.
24. BLEU/ROUGE over concatenated guides cannot verify step/state alignment, target truth, ordering, omissions, alternatives, recovery, or user comprehension.
25. A single reference penalizes valid alternative paths and lexical realizations.
26. GGS’s 0.4 success floor and linear compensation have no user-acceptance or loss-model basis.
27. “Guide tax” mixes path, length, tokenization, reference, metric, and substantive-guide error.
28. The Appendix D GGS denominator conflicts with Section 3.3/Table 1.
29. Teacher-forced GACS inherits the gold path, target strings, anchor extractor, lexicon, thresholds, and candidate mapping.
30. WebArena functional checkers are inherited rather than release-audited or falsified in MAG.
31. The 29-task semantic judge has model-judge agreement evidence but no human correctness calibration.
32. Endpoint success does not establish legitimate actions, preserved collateral state, intermediate-guide truth, or recipient utility.
33. “Expert trajectories” are successful GPT-5.5 benchmark runs, not human/domain-expert demonstrations.
34. The training treatment mixes successful off-policy rows, task scheduling, group-size change, and one selected recipe.
35. Ten plain-GRPO runs are heterogeneous documentary attempts, not a controlled fixed-test ablation.
36. One seed per grounding scheme does not establish training reliability.
37. Main rows are single greedy sweeps; API settings are fixed but not deterministic or fully identified.
38. The SoM-versus-coordinate training-gain contrast interval crosses zero.
39. Pass@6 rejects pure same-form sharpening but does not establish equivalent-form or changed-context capability transfer.
40. Environment/provider invalids, retries, timeouts, missing rows, and account/reset failures are not reported as denominators.
41. Task bootstraps ignore site/template and source-lineage clustering.
42. Annotation, training, inference, guide-review, maintenance, wall-time, token, hardware, API, and user-burden costs are absent.
43. No interface/version drift or guide-update study supports maintainability claims.
44. No evidence supports professional validity, labor savings, deployment utility, production fitness, or readiness.

## Reproducibility and operational realism

**Protocol inspectability: moderate to strong.** The immutable paper gives the output contract, prompts, action vocabulary, viewport, step budget, parser behavior, reset protocol, training hyperparameters, equations, selected task-level paired counts, bootstrap intervals, pass@k setup, corpus/action statistics, and qualitative examples. Another team could build a related instrument.

**Exact reproducibility: absent at review time.** Despite repeated release claims, no author-owned project was linked or located. Reproduction needs immutable task membership and dispositions; screenshot/action/guide records; source demonstrations and mapping audit; annotator labels/edits; prompts and parser; WebArena/OpAgent/harness commits; container and account fixtures; checker/judge versions; checkpoints; raw completions; all attempts/invalids; result tables; and analysis code. Mutable API model labels and live runtime dependencies would still need dated endpoint/configuration records.

**Operational realism: moderate for controlled interactive state, low for recipient and production claims.** Self-hosted services, screenshot observations, long dependent action chains, container resets, authentication checks, and functional endpoint predicates are valuable. But the sites use synthetic content; tasks are prior-agent-solvable; the guide is not consumed by another actor; there are no permissions changes, concurrent users, accessibility needs, organization-specific conventions, exceptions, support escalation, deployment, telemetry, recipient uptake, or UI-maintenance cycle. MAG is an action-plus-narration benchmark, not a demonstrated DAP production workflow.

## Transfer to `skill-bench`

### Retain

1. **Joint action/proposition capture:** emit the user-facing proposition while the pre-state, target action, and resulting state can still be linked.
2. **Machine/human grounding separation:** prohibit internal IDs and coordinates in recipient-facing artifacts while preserving them privately for traceability.
3. **Functional outcome gating as one layer:** do not treat fluent guidance attached to failed work as deployable, but keep endpoint and guide measures separate.
4. **Projection-defect audits:** quantify unmapped actions, suspect targets, missing terminal steps, recapture drift, and over-budget witness paths.
5. **Paired task comparisons and pass@k:** retain task-level discordance and repeated sampled outcomes rather than relying only on macro means.

### Repair

1. **Make every guide clause proof-carrying.** Bind clause ID to public requirement, source event/span, pre/post state, intended action/decision, target locator, valid time, authority, and reviewer disposition.
2. **Separate local truth from procedure completeness.** Score action match, state transition, required-step coverage, ordering/dependencies, alternate routes, terminal verification, prohibited side effects, exception/recovery coverage, and unresolved assumptions independently.
3. **Use semantic accepted sets, not one text path.** Permit reviewed alternative procedures and paraphrases; judge clauses against authoritative state and requirement evidence before any reference resemblance diagnostic.
4. **Run matched recipient trials.** Freeze initial state and recipient configuration; compare no guide, gold guide, model guide, and planted omission/stale/wrong-target variants. Measure localization, execution, completion, preservation, errors, clarification, burden, time, and cost.
5. **Separate producer memory from external artifact.** Cross private structured state × emitted guide history so execution gains are not attributed to recipient-facing narration.
6. **Test transfer edges.** Hold the procedure constant across equivalent task forms, different recipients, changed labels/layouts, permission states, and version drift. Record where clauses remain applicable or require repair.
7. **Measure lifecycle cost.** Include guide generation, proposition validation, recipient verification, execution, review, drift detection, updates, failures, and human burden.
8. **Keep plural outcomes primary.** Report source task success, clause validity, procedure completeness, recipient success, correction burden, transport, maintenance, and professional acceptance separately. Any aggregate needs a named decision and loss policy.
9. **Version the full configured system.** Pin task/source trajectory, environment snapshot, candidate renderer, action interface, parser, producer, recipient, guide, grader, feedback, reset, and metric identities.
10. **Use existing contracts.** Guide propositions fit the repository’s evidence/provenance, procedural-skill, artifact-view, trace, handoff-usability, configured-system, metric, task-health, and validity machinery. Do not add a web/DAP-specific subsystem.

## Action items

1. Index MAG as a Tier B enabling source: it contributes a distinct action→instruction projection boundary and concrete mapping failures, but its absent release and recipient evidence prevent Tier A transfer claims.
2. Consolidate the action→guide→recipient→maintenance ladder into the canonical taxonomy when adjacent handoff, procedural-skill, and artifact-admissibility guidance is next revised; avoid a duplicate guide schema.
3. Before building a large study, adapt one existing cross-domain pilot into a small frozen-state recipient falsification: one valid guide, one omitted terminal obligation, one stale target, and one valid alternate route under no-guide/guide conditions. Treat this as instrument validation, not evidence that guides generally help.

## Review checklist

- [x] Read the complete immutable v2 PDF and extraction, including appendices.
- [x] Verified local PDF/text hashes and 25-page identity.
- [x] Repeated official-release searches and documented the absent/unlocated boundary.
- [x] Reconstructed source selection, corpus/split denominators, task interface, observers, metrics, training, uncertainty, and costs.
- [x] Distinguished self-hosted runtime interactivity from production-live websites.
- [x] Distinguished author-rated reference usefulness from recipient execution.
- [x] Distinguished same-reference guide overlap from proposition truth, completeness, recipient utility, transfer, maintenance, and professional consequence.
- [x] Compared nonduplicatively with LH-Bench, AFTER, DeskCraft, Handoff Debt, AgentRewardBench, and existing artifact/trace machinery.
- [x] Proposed reuse through existing contracts rather than a web-specific subsystem.
