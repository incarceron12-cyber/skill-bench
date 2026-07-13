# Paper and Release Review: Ambig-DS — Executable Is Not Well-Framed

- **Paper:** https://arxiv.org/abs/2605.09698v1
- **Authors:** Josefa Lia Stoisser, Marc Boubnovski Martell, Sidsel Boldsen, Kaspar Märtens, and Robert Kitchen
- **Date read:** 2026-07-13
- **Source:** complete immutable arXiv v1, submitted 2026-05-10
- **Tags:** task-framing, ambiguity, clarification, abstention, hidden-requirements, data-science-agents, artifact-validity
- **Local PDF:** `data/papers/pdfs/2605.09698v1-ambig-ds.pdf` (32 pages; SHA-256 `e259e54bc9b8f115967c86a9c6cad71735f90f2ae9a00899be8fa7b7d348ce11`)
- **Local text:** `data/papers/text/2605.09698v1-ambig-ds.txt` (SHA-256 `9f3414425ec700e96d957e02f95bf6f63c5f010bad800cae344e51bb3947bdf4`)
- **Official releases:** complete Ambig-DS-T revision `9e567c66ac8bfec31d3b2b720bbd2c122abf82e4` and Ambig-DS-M revision `3187b0f5e9d1f5329914e5669bb2cc19592663d1`, archived under `data/sources/releases/2605.09698v1-ambig-ds/`; provenance: `data/sources/releases/2605.09698v1-ambig-ds/provenance.json`
- **Timing boundary:** both inspected dataset revisions are about four days before v1 and are plausible manuscript-time evidence, but the paper pins no revision; exact experiment-package identity is unproven.

## One-sentence contribution

Ambig-DS creates paired fully specified and deliberately underdetermined predictive-modeling tasks, showing that five code agents often produce valid-looking artifacts after silently selecting an unsupported target or metric and that perfect, scoped clarification can repair much of the score loss—but its protocol identifies behavior under synthetic one-bit ambiguity, not natural stakeholder ambiguity or professional task-framing competence.

## Why this matters for skill-bench

This advances charter objectives A, B, and C by supplying a controlled method for a central knowledge-work failure: **an artifact may be executable, internally coherent, and accepted by a grader while answering the wrong question**. The paper makes task framing—not just task execution—an explicit construct, and its paired intervention is stronger causal evidence than an unpaired collection of vague tasks.

This is a data-science case testing a cross-domain hypothesis, not a proposal to narrow `skill-bench` to ML competitions. Useful transfer is a decision-boundary design: identify which missing commitment changes consequential action, prove that multiple framings remain publicly admissible, distinguish asking from abstaining and unilateral assumption, and score the clarification burden separately from downstream execution.

## Research question and claim ladder

The defensible question is:

> When one consequential framing variable is removed from an otherwise executable benchmark package, do fixed agent configurations recognize the underdetermination, seek clarification, and use a truthful answer?

The stronger implied chain is:

```text
paired prompt/data edit
→ multiple professionally plausible framings
→ degradation is caused only by ambiguity
→ agent detects the ambiguity
→ agent asks the right authority
→ answer resolves the real decision
→ repaired benchmark score
→ natural stakeholder collaboration
→ professional task-framing competence
```

Ambig-DS gives evidence for selected early links. It verifies alternatives with a checklist, keeps the source evaluator fixed, and compares matched task conditions. It does not validate professional plausibility with independent practitioners, isolate every changed cue in the target suite, provide a clarification channel in the no-Ask condition, or test noisy, conflicting, unavailable, strategically motivated, or unauthorized stakeholders.

## Methodology and system

### 1. Construct and paired conditions

An agent receives a prompt–data observation and must choose a supervised-learning framing. The paper focuses on two variables: prediction target `T` and evaluation objective `M` (pp. 3–4). The inherited source framing is a **scoring convention**, not the unique semantic truth of the ambiguous observation. Desired behavior is therefore not to guess that private convention but to recognize that more than one framing remains and ask before committing.

Each retained source task yields:

- **Full:** the original target or metric is explicit;
- **Ambig.:** that framing information is removed, with no clarification channel;
- **Ask:** the ambiguous package plus one pre-modeling question of at most 50 words to a restricted oracle.

This separation is conceptually valuable. `Full → Ambig.` probes sensitivity to information removal; `Ambig. → Ask` probes whether perfect delivery of the missing bit is sufficient for recovery. But Ask also changes the prompt, workflow, stopping rule, interaction availability, and agent expectation—not only information content.

### 2. Target ambiguity: coordinated prompt and data intervention

Ambig-DS-Target starts from 74 DSBench tasks and retains 51 with a clean target and valid transformation (33 classification, 18 regression; pp. 4, 14–15). It:

1. renames the true target to `val_1` or `val_2` (31/20 split);
2. adds the other as a synthetic candidate with an exactly matched marginal;
3. anonymizes feature names;
4. removes target-identifying prompt and sample-submission cues;
5. keeps the source evaluator and intended answer mapping private.

The decoy is rank-mapped from low-correlation features and receives calibrated label noise. Twenty-nine of 51 tasks meet a 0.02 true/decoy CV-score gap, 40 meet 0.05, and 44 meet 0.10; seven remain above 0.10 and the maximum reported gap is about 0.30 (pp. 4, 15–17). Simple marginal, CV, and LLM selectors have Wilson intervals including chance, although a prompt-aware LLM reaches 62.7% and naturalistic domain reasoning 56.9% (Table 7, p. 16). Thus the intended target is difficult, not proven impossible, to infer from residual cues.

This is not a single-variable text intervention. It bundles target-cue deletion, feature-name anonymization, a synthetic target, generic submission headers, and changed data semantics. The paired score difference identifies the **whole ambiguity construction package**, not separately target omission, anonymization, or decoy competition.

### 3. Objective ambiguity: prompt-only metric removal

Ambig-DS-Objective screens 75 MLE-bench competitions and retains 61 under a 50 GB harness limit and decision-relevance checks (pp. 4, 14). Data, target, submission columns, and evaluator remain unchanged; explicit metric name, direction, formula, and related cues are removed. The 61 released manifests span 19 lower-is-better and 42 higher-is-better tasks, including ranking, probability, hard-label, regression, segmentation, string, and custom metrics.

This intervention is cleaner than Target because the package files are nominally fixed. Yet “metric-only” removal can alter more than optimization: it may obscure required output value type, thresholding, clipping, top-K structure, scored columns, or submission semantics (pp. 4–5). These are deliberately treated as one framing variable, but `M` is actually a bundle of criterion, direction, representation, and aggregation decisions.

### 4. Construction and ambiguity verification

Claude Opus 4.7 generates prompt edits. Candidates pass a four-item checklist (pp. 4–5, 28–31):

1. at least two plausible alternatives;
2. ambiguity survives the whole prompt/data package;
3. resolution changes a consequential solver choice;
4. unrelated task information is preserved.

Humans review final labels; Claude, GPT, and Gemini verifiers are reported to agree with final decisions at roughly 71–89% by criterion and 80–85% on retain/reject (Table 8, p. 17). This is evidence that checklist judgments are not wholly Claude-idiosyncratic, but agreement with a human-reviewed outcome is not independent professional validation. The paper does not report reviewer count, domain qualifications, independent labels, adjudication, or human agreement. “Plausible” is operationalized by authors and model judges rather than practitioners deciding whether each alternative would be legitimate in context.

### 5. Clarification oracle and ask policy

Before modeling, the agent may inspect headers, rows, shapes, dtypes, and sample submission, then asks one self-contained question or writes `NONE`; it must stop until answered (pp. 5, 25–27). Claude Haiku 4.6 receives the private manifest and answers only target or metric/submission questions. It refuses modeling advice, test information, construction details, and unrelated requests. A GPT-5.4 oracle swap on Claude-agent cells changes Target recovery from +0.20 to +0.18 and leaves Objective at +0.03 (p. 17).

The authors correctly call this a causal probe, not stakeholder simulation. It provides an always-available, truthful authority that already knows the benchmark's private convention and has no cost, delay, uncertainty, disagreement, consent, or organizational constraint. One-shot interaction may understate multi-turn recovery, while perfect authority overstates real recovery.

Two ask policies test calibration (pp. 8, 23–24): permissive says the agent may ask; conservative says ask only if unresolved and warns that unnecessary clarification is penalized. The paper reports no model/policy pair calibrated across both axes. But its `CalibScore` is a harmonic combination of ask recall and non-ask specificity with no empirically justified loss ratio. In professional work, needless interruption and silent wrong commitment can have radically unequal costs; policy selection requires decision loss, urgency, reversibility, and authority availability—not a generic symmetric score.

### 6. Agents, execution, measurements, and uncertainty

Five proprietary model backbones run in OpenCode with matched tools and environments: Gemini 3 Flash, GPT-5.4 Nano, Claude Haiku 4.5, Gemini 3.1 Pro, and GPT-5.4 (pp. 5–6). Budgets are two hours per Target task and 24 hours per Objective task; oracle time is excluded. Invalid and timeout outcomes score zero and remain in the 51/61 denominators.

The source score is normalized to `[0,1]`: DSBench Relative Performance Gap for Target and performance relative to Kaggle median for Objective (pp. 19–20). Mean matched deltas are accompanied by one-sided Wilcoxon tests and 10,000-replicate paired bootstrap intervals. Pairing and explicit invalid/timeout denominators are strengths. However:

- each model–task–condition appears to have one agent attempt, so trajectory stochasticity is unmeasured;
- ten models/suites × two directional hypotheses produce multiple tests without correction;
- one-sided tests encode the expected direction after designing the treatment to degrade information;
- task bootstrap uncertainty does not cover model API, oracle, judge, task-construction, or source-selection uncertainty;
- normalized score scales differ across source benchmarks and the paper appropriately avoids pooling axes;
- roughly 2,970 compute-hours are reported, but no token/API cost or per-condition resource distribution is provided (p. 14).

## Evidence and results

### Strongly supported within the constructed suites

- Ambiguity lowers mean normalized scores for every tested model within both suites: Target deltas range from −0.10 to −0.29; Objective from −0.04 to −0.09, with reported paired bootstrap intervals excluding zero except the rounded lower endpoint for one Ask interval (Table 1 and Table 12, pp. 6, 22).
- On Target Ambig. runs, 39–63% of frontier-model submissions and 43–59% of smaller-model submissions optimize the alternative candidate while remaining valid artifacts (Table 2, p. 6).
- Objective silent failures combine alternative-objective modeling and degenerate baselines; combined rates range 16–62% under Ambig. (Table 3, p. 7).
- Ask recovery is positive in every reported model/suite cell, reaching +0.20 on Target and +0.09 on Objective (Table 1).
- Perfect information does not erase all execution failure: Ask often remains below Full, and Objective degeneration persists for weaker models (pp. 7–9).
- Trace recognition and answer-facing escalation differ. On Target, some models explicitly notice ambiguity in traces, yet user-overridable final-answer flags never exceed 4%; on Objective, explicit recognition is below 10% and overridable flags are zero (Table 10, p. 18).

## Unique insight

Ambig-DS's most transferable insight is not simply “agents should ask questions.” It is that benchmark authors can construct a **framing counterfactual** while preserving an executable task:

```text
public evidence + requirements
→ set of admissible framings
→ decision-relevant unresolved variable
→ allowed terminal policy {act, ask, abstain, escalate}
→ authority-scoped answer event
→ framing commitment
→ artifact and state consequences
→ bounded score and claim
```

For `skill-bench`, a hidden reference should not silently turn one admissible framing into “correct.” If multiple public interpretations are fair, unilateral action should be assessed by consequence and reversibility, while the benchmark separately measures recognition, disclosure, clarification quality, authority choice, answer uptake, execution, and interruption cost.

The paper also exposes a useful failure distinction:

- **recognition failure:** no sign that ambiguity was noticed;
- **communication failure:** noticed internally but not made overridable;
- **authority-routing failure:** asks the wrong party/topic;
- **commitment failure:** chooses an unsupported framing;
- **abdication:** avoids the decision with a non-substantive artifact;
- **execution failure after resolution:** has the answer but still fails.

A single terminal task score collapses these mechanisms.

## Release audit

The two official Hugging Face repositories are compact and inspectable at the pinned revisions:

- **Ambig-DS-T:** 207 tracked files—51 full prompts, 51 ambiguous prompts, 51 manifests, 51 `eval.py` files, `tasks.csv`, and metadata. Static audit confirms 51 unique tasks, 33/18 classification/regression, 31/20 true-target placement, exact marginal-match flags for all tasks, and no sidecar data. The archive contains no Kaggle data. The README says a deterministic build script is “published separately on GitHub,” but neither the dataset nor paper provides its URL; the released manifests are recipes, not an executable reconstruction pipeline.
- **Ambig-DS-M:** 191 tracked files—61 prompt pairs, 61 single-record verification JSONs, summary, metric manifest, and indexes. Static audit confirms 61 unique slugs, 61 manifests, 61 prompt directories, and 61 passing verification records. Character-level Full/Ambig similarity has median 0.963 (range 0.826–0.993), consistent with mostly bounded edits but not proof of semantic isolation.

A material paper/release boundary remains. The paper reports three-model verification plus human review (pp. 4, 16–17), while every released `_verify` record says `n_judges: 1`, model `anthropic_claude_opus_4_7`; the cross-family decisions and human review lineage are not released. The release README calls this a “panel,” which overstates the archived evidence. Target packages have no analogous released verification records.

Neither release includes the evaluated Kaggle data, complete target transformation builder, OpenCode harness/configuration, clarification oracle implementation, agent trajectories, objective diagnostic judge calls, human corrections, raw scores, result tables, bootstrap inputs, model snapshots, token/cost logs, or exact environment images. MLE-bench evaluators are external; Target evaluators are present but answer data is not. The mechanism can be inspected, but paper results cannot be independently replayed from these archives alone.

## Limitations and validity threats

1. Only target and metric ambiguity are tested; authorization, evidence scope, valid time, external-data rules, safety thresholds, affected parties, and deliverable purpose remain fixed.
2. Axis and source benchmark are perfectly confounded, preventing a target-versus-objective effect comparison.
3. Target intervention bundles prompt edits, feature anonymization, decoy creation, and submission-header changes.
4. Objective “metric” bundles metric identity, direction, value type, ranking/thresholding, quirks, and aggregation.
5. The intended framing is a private scoring convention, not uniquely implied by the ambiguous public package.
6. Professional plausibility of alternatives is not independently established; human reviewer number, qualifications, labels, agreement, and adjudication are absent.
7. Model-assisted generation can shape which ambiguity types enter the benchmark; cross-family verification does not audit generator-selection bias.
8. Seven Target decoys miss the 0.10 CV-parity tier; residual prompt/domain cues may make some targets inferable.
9. The Ambig. condition has no clarification channel, so score loss cannot fully separate non-recognition from recognized-but-forced commitment.
10. Trace/final-answer recognition is model-judged; full label artifacts and independent human reliability are unreleased.
11. Objective failure labels depend on five LLM calls and human correction; κ values show substantial, not perfect, agreement.
12. One attempt per cell does not estimate configured-system reliability or trajectory variance.
13. One-sided tests and many model/suite hypotheses have no multiplicity correction.
14. Task-level bootstrap intervals omit task-construction, model, judge, oracle, and source-selection uncertainty.
15. Invalid and timeout scoring at zero is transparent but mixes framing, infrastructure, and resource failure in aggregate deltas.
16. Ask changes interaction affordance and workflow, not merely the missing information.
17. The oracle is perfectly informed, truthful, scoped, immediate, and always available; it is not ecological participant evidence.
18. Ask time is excluded, and human interruption, delay, coordination, privacy, and authority costs are unmeasured.
19. `CalibScore` embeds an unvalidated symmetric operating objective and hides consequence asymmetry.
20. No open-weight model, repeated attempt, human baseline, novice/expert comparison, or natural ambiguity sample is evaluated.
21. All source tasks are public Kaggle-derived tasks, creating contamination and familiarity risk.
22. The modest, filtered 51/61 samples are diagnostic sets, not prevalence samples of data-science or knowledge work.
23. The release lacks raw experimental results and sufficient exact configuration for result reproduction.
24. The target data and complete builder are unavailable in the release; Kaggle access/rules and external MLE-bench versions add operational drift.
25. CC-BY-NC and competition-specific terms constrain reuse and maintenance.

## Reproducibility and operational realism

Reproducibility is **moderate for inspecting task definitions, weak for rebuilding Target packages, and weak for reproducing reported results**. Both official metadata releases are complete, compact, revision-pinned, and pre-v1. Target manifests preserve seeds, feature maps, decoy pools, noise parameters, diagnostics, source URLs, and evaluator scripts. Objective packages preserve complete prompt pairs, metric metadata, and one Claude verification result per task.

Yet manifests do not substitute for executable lineage. Target raw data, transformed CSV hashes, builder code, and answer files are absent. Objective data and evaluators require mutable external MLE-bench/Kaggle dependencies. No environment lock, harness, trial manifest, raw trajectory, or result matrix is released. Proprietary 2026 model names and oracle behavior will drift or become unavailable. Reproduction would therefore be a new implementation guided by the paper, not a byte-identical replay.

Operational realism is intentionally low for clarification and mixed for execution. Kaggle-style long-horizon modeling and heterogeneous source metrics exercise real technical work, but tasks start from clean competition packages; ambiguity is author-planted; authority is omniscient; no stakeholder conflict, evolving evidence, organizational consequence, approval chain, or artifact handoff is represented. The design has high value as a diagnostic instrument precisely because it isolates one failure—not because it estimates workplace prevalence.

## Transfer to skill-bench

## Concrete repository actions

### Retain

1. **Paired framing interventions:** preserve a fully specified anchor and minimally altered ambiguous form with an immutable diff and unchanged downstream checker where possible.
2. **Admissible-framing set:** enumerate at least two public-evidence-compatible framings and record why each is plausible.
3. **Decision relevance:** require evidence that resolving the variable changes target, threshold, action, artifact semantics, safety, cost, or stakeholder consequence.
4. **Separate stages:** score recognition, user-visible disclosure, question quality, authority routing, answer uptake, execution, and final consequence separately.
5. **Null outcomes:** retain invalid, timeout, abstain, escalate, wrong-authority, unsupported-assumption, and insufficient-evidence states rather than forcing pass/fail.
6. **Matched denominators and uncertainty:** use task-paired contrasts, preserve invalid runs, report dependence-aware intervals, and repeat stochastic conditions.

### Repair

1. Replace a private “intended” answer with a **public-basis and consequence rule**: if several framings are fair, the grader must not penalize one merely for disagreeing with the author's hidden preference.
2. Make clarification a typed authority event: who can answer, which claims they control, evidence scope, uncertainty, valid time, conflicts, delay, cost, and whether the answer is binding.
3. Cross ambiguity presence/absence with channel available/unavailable and reversible/irreversible action; Ambig-DS confounds recognition with absent affordance.
4. Predeclare decision loss for asking, acting, abstaining, and escalating; do not use an unvalidated generic calibration aggregate.
5. Freeze author/reviewer provenance and independent ambiguity labels; report disagreement rather than laundering model-assisted consensus into expert truth.
6. Verify intervention isolation at prompt, source-pack, artifact-contract, evaluator, and environment layers; hash every projection.

### Falsifiable next validation experiment

Use two existing cross-domain pilot shapes rather than a new data-science subsystem. For each, author one publicly resolvable ambiguity and one irreducible authority-dependent ambiguity, then cross:

- full versus ambiguous public package;
- no channel versus correct authority versus wrong/uncertain authority;
- reversible draft versus consequential state-changing action;
- generic “ask if needed” versus loss-calibrated policy.

Blindly adjudicate public admissibility before trials. Measure ambiguity recognition, answer-facing flagging, question information gain, authority correctness, answer adoption, unsupported assumptions, interruption cost, final artifact/state quality, collateral effects, and repeated-run reliability. A valid design should show that resolvable cases are solved without needless asking, irreducible cases trigger the appropriate authority under calibrated loss, and wrong-authority answers do not gain inherited legitimacy.

No new queue task is added: existing UnderSpecBench/action-boundary, participation/authority, public-basis, validity, task-health, metric, and artifact-state machinery already represents this experiment. The evidence should first be consolidated into those contracts rather than spawning an ambiguity-specific schema.

## Claim ceiling

This paper and release support the claim that, on two controlled Kaggle-derived suites and five specified proprietary-model/OpenCode configurations, removing target or objective information often lowers source-benchmark scores, valid-looking artifacts can encode unsupported framing commitments, and perfect scoped clarification frequently recovers part of the loss. They do **not** support prevalence over data-science or knowledge work, natural ambiguity detection, realistic stakeholder interaction, calibrated professional escalation, expert-level task framing, occupational capability, production fitness, safety, economic value, or deployment readiness.
