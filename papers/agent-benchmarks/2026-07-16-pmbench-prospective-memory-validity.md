# PM-Bench: a strong timing-and-monitoring stress test whose “ongoing activity” is not an evaluated task

**Source:** Genglin Liu and Saadia Gabriel, *PM-Bench: Evaluating Prospective Memory in LLM Agents*, arXiv:2607.12385v1 (14 July 2026), 22 pages; https://arxiv.org/abs/2607.12385v1.
**Immutable paper:** `data/papers/pdfs/2607.12385v1-pm-bench.pdf` (SHA-256 `ca391936e787ee6597e0ef4bb078913b54cd5ef4151e673f6bb928db39ad67a1`).
**Full extraction read:** `data/papers/text/2607.12385v1-pm-bench.txt` (SHA-256 `f50b0f2561ea55d474d8823f1dc0ba3771476355a2799016f1b75f72aa1c95ae`).
**Official release inspected:** commit `e1093c470c8981daf522d4ef047a7c3a71e077d7`, approximately 12 minutes before v1 publication.
**Release provenance:** `data/sources/releases/2607.12385v1-pmbench/provenance.json`.
**Pinned release root:** `data/sources/releases/2607.12385v1-pmbench/repository/PMBench-e1093c470c8981daf522d4ef047a7c3a71e077d7/`.

## Review status and charter fit

This is a **deep full-paper and release review**. I read the complete immutable v1 local PDF and complete local text extraction, then inspected the pinned 172-file official snapshot: deterministic week generator and scenario, runtime/scorer, eight configuration paths, 64 released primary trajectories, prompt/ledger/debug records, aggregate report builder, and human-play UI. I executed canonical scenario validation and regenerated the released comparison report successfully. I also regenerated the default week in memory and audited all 64 primary JSONL files; every file contained one metadata record plus 80 decisions.

The review advances charter objectives A–C by testing a general question: how should delayed obligations, monitoring choices, updates, and temporal execution be separated from concurrent work quality? It is expansion into reusable timing/monitoring machinery, not a proposal to narrow skill-bench to personal reminders or memory agents.

## One-sentence contribution

PM-Bench releases an unusually inspectable, executable stress test of delayed action selection under hidden cues, updates, lures, and monitoring choices, but it measures obligation tracking and menu selection—not the dual-task prospective-memory construct or professional work quality—because its nominal ongoing activity has no correctness, cost, consequence, or score.

## Why this matters

Delayed requirements are common across knowledge work: a professional may need to revisit evidence when a state changes, apply a later correction, preserve a deadline while producing an artifact, or suppress an obsolete instruction. PM-Bench supplies unusually clear machinery for the obligation side of that problem. Its missing concurrent-work outcome also identifies the precise repair skill-bench needs before delayed-action reliability can support a claim about useful agentic knowledge work.

## Contribution and research question

The paper asks whether LLM agents can remember **to act later**, at the right time or cue, rather than merely recall past information. Its 7-day synthetic week combines time- and event-based obligations, cross-day tasks, cancellation/rescheduling/override updates, dependencies, recurring medication-like actions, hidden state channels, anonymous action handles, and lures (paper §§2–3, pp. 3–7).

This decomposition is valuable. PM-Bench does not reduce prospective memory to final recall: the agent must encode an instruction, retain it while 80 steps advance, decide when to query clock or state channels, respond to an exact cue, suppress premature/canceled/lure actions, and follow the latest task state. The release makes these mechanisms explicit rather than burying them in one dialogue score.

The distinctive unit is a **virtual step with two outputs**: one required `A/B/C` choice to advance the vignette and an optional set of task handles. Ground truth marks which handles are due at that step. Replay then computes set precision/recall/F1 plus timing, update, dependency, false-alarm, commission, monitoring, and slice diagnostics.

## Methodology and released system

### Scenario construction

`sim/week_builder_v9.py` deterministically constructs one week from default seed 42, rejecting candidates until schema, diversity, and perfect-play solvability checks pass. The canonical `data/synthetic_week_v9.json` has 7 days, 80 steps, 83 task records, 67 lures, 7 cross-day obligations, and 11 updates (6 reschedules, 3 overrides, 2 cancellations). The paper's scored denominator is 81 non-canceled obligations: 26 time-based and 55 event-based (paper pp. 4–6, 13–15).

The generator assigns seven day archetypes, irregular times, shuffled handles, varied cue families, and narrative templates. `generate_week_v9.py` attaches exact per-step ground truth and refuses an unsolvable week. I regenerated the default scenario and confirmed the same structural statistics; after applying the release's ground-truth attachment wrapper, generation is deterministic. The written scenario itself does not retain the seed, attempt number, generator hash, or generation statistics, so provenance depends on external code/command records.

Tasks are synthetic and authored from libraries, not sampled from observed prospective-memory incidents, consenting users, occupational workflows, or expert elicitation. Medical, administrative, household, logistics, academic, and social labels increase surface breadth, but do not establish representativeness, severity, or domain realism.

### Observation, action, and monitoring contract

At each step the agent receives a short vignette, three arbitrary continuation options, and an action menu containing active tasks plus deterministic sampled lures. Clock and other channels—calendar, email, shipment, appointment portal, and similar state—may be hidden until queried. Tasks can become active at day start or a later step; updates alter runtime state; dependencies gate execution. Correct execution hides a completed item, while canceled tasks remain visible so selecting them is observable.

The runtime cleanly separates due-state calculation (`compute_due_now`) from completion and grading. Event actions selected one step late and time actions selected within 60 virtual minutes can be diagnosed as late completions, while exact-step set-F1 still treats them as false positives/misses. Premature selection does not complete an item, so an agent can incur a false alarm and later receive a hit. This is a defensible diagnostic design, but lateness windows are author-set conventions without empirical or consequence calibration.

The release also exposes a meaningful monitoring treatment. Plain agents decide whether to query; automatic heartbeat variants receive periodic evaluator-generated nudges; hierarchical agents union subagent queries; vote variants replay the same hierarchical traces. Importantly, a heartbeat is not merely a neutral clock interrupt: `pending_proactive_channels_for_heartbeat` derives a list from the oracle runtime state of active, incomplete, uncanceled tasks, and the prompt can name channels worth checking. Task-reminder mode can reveal upcoming action text and urgency. These are privileged scaffolds and should be described as different evidence interventions, not merely memory aids.

### Models, configurations, and released runs

The paper crosses eight backbones with eight configurations: baseline, todo ledger, optional heartbeat, automatic 60- and 30-minute heartbeat, hierarchical union-query, and majority/unanimity replay ablations, for 64 scored trajectories (paper §3.3, pp. 7–9). Models span GPT-5.4, GPT-5.3-Codex, Llama-3.3-70B, two Mistral models, and Qwen3 8B/14B/32B.

The pinned release contains all 64 primary logs. Static audit found every log has 80 action rows plus one metadata record and identifies model, backend, timestamps, duration, and mode. However, metadata records no model revision, prompt hash, scenario hash, temperature/config hash, token usage, API cost, retry count, provider routing identity, hardware identity, or random seed. OpenRouter calls use temperature 0 and can retry structured output before falling back to unconstrained JSON. Hierarchical logs retain subagent failures and coordinator recoveries; replay vote logs reuse one union-query run and therefore are not independent executions.

### Scoring

The primary metric micro-aggregates task-handle decisions over due sets:

`Set-F1 = 2TP / (2TP + FP + FN)`.

This appropriately penalizes both omission and indiscriminate action dumping. The report also gives macro day F1, total false positives and queries, event/time hit rates, cross-day/update subsets, late and error categories, and monitoring-required slices (paper pp. 8–12). Perfect-play validation ensures each due action appears in the menu and all non-canceled tasks can be completed exactly on time.

Yet the score treats all obligations equally: taking medication, sending an email, cleaning a mug, and collecting a package have no severity, reversibility, deadline-width, stakeholder, or cost distinction. Queries have counts but no time/token/attention price in the objective. `A/B/C` choices are logged but not graded. The benchmark therefore optimizes exact obligation selection under equal-weight synthetic loss, not expected operational utility.

## Evidence and what it supports

Across model-averaged configurations, optional heartbeat has the best reported Set-F1 at 65.1%, followed by ledger at 64.1% and baseline at 62.1%; hierarchical union-query reaches 49.9%, majority vote 38.7%, and unanimity vote 36.0% (paper Table 2). Per-model rankings vary: GPT-5.3-Codex baseline reaches 78.9%, GPT-5.4 optional heartbeat 79.1%, while several Qwen/Mistral configurations are much lower (Table 3).

The most informative pattern is not the leaderboard. Monitoring-heavy systems gather more evidence but act less selectively. Hierarchical union-query issues 1,661 total state queries yet trails single-agent methods; majority replay improves monitoring-sensitive hit rates but generates 655 false positives. Automatic 30-minute heartbeat reaches the strongest hidden-channel hit rate among the automatic schedules (15.8%) but accumulates 489 false positives and only 57.8% aggregate Set-F1 (paper pp. 9–12).

These observations support three bounded claims:

1. current configured systems frequently miss or mistime obligations in this fixed synthetic week;
2. more monitoring or more reminders does not monotonically improve exact-step set selection;
3. scaffold effects interact strongly with model backbone and precision/recall behavior.

They do **not** show that optional heartbeat is generally superior, that model failures are human-like prospective-memory failures, or that one architecture has more prospective-memory capacity. Every headline cell is one run on the same public generated week. The 64 trajectories are crossed configurations, not 64 independent task samples; vote rows are deterministic replays of union traces. No repeated model calls, equivalent weeks, confidence intervals, paired uncertainty, or week/task-family-cluster analysis establishes stability or generalization.

## Unique insight: prospective remembering requires a dual-task consequence, not just an advance token

PM-Bench's most reusable contribution is its explicit **obligation state machine**:

`instruction → activation → update/dependency → cue observability → monitoring/access → due set → selected action → timing/error outcome`.

This is directly transferable to delayed requirements in knowledge work. But the implementation reveals the benchmark's central construct boundary:

> The agent's “ongoing activity” is a compulsory but ungraded A/B/C token. Because option choice has no right answer, state consequence, interference cost, or artifact effect, PM-Bench does not measure whether prospective remembering competes with or preserves concurrent work.

Classic prospective-memory paradigms are dual-task designs: remembering to perform the delayed intention is evaluated alongside performance on an ongoing task. In PM-Bench, all three vignette options merely advance the simulator. An agent can devote unlimited conceptual attention to reminders, query aggressively, select arbitrary `A/B/C`, and suffer no degradation in the nominal work stream. The query count is reported, but queries do not consume a task budget or reduce ongoing-task quality.

For skill-bench, the transferable estimand is therefore not a scalar “prospective memory” score. It is a paired outcome:

1. **delayed-obligation reliability:** correct, timely, update-consistent action under observable cue conditions;
2. **concurrent-work preservation:** quality, safety, latency, and collateral effects on the primary artifact/workflow while monitoring and remembering.

Only their joint frontier can distinguish useful prospective support from a reminder system that overwhelms the work, and only explicit evidence-access/adoption traces can distinguish retention from monitoring or action-control failure.

## Limitations and validity threats

### Construct and task validity

1. **No evaluated ongoing task.** A/B/C choices are semantically inert and unscored, so the central dual-task/interference component of prospective memory is absent.
2. **One synthetic week is the entire test form.** All models see the same 80-step public scenario; there are no held-out or equivalent weeks, difficulty links, refresh stream, or contamination controls.
3. **Surface diversity is not population validity.** Domains and obligations come from authored libraries without incident sampling, user/expert elicitation, frequency weights, or consequence calibration.
4. **Construct components are entangled.** Final action selection jointly depends on instruction comprehension, long-context retention, handle binding, cue detection, query policy, update reconciliation, JSON compliance, and inhibition. No matched interventions identify the earliest failing link.
5. **Monitoring-required labels are authored/runtime-derived.** Hidden-channel slices test this simulator's visibility policy, not a validated latent monitoring capability.
6. **No human comparator or criterion validation.** Psychology literature motivates the design, but humans are not evaluated under the same interface and no expert judges whether tasks, lateness windows, updates, or interference resemble consequential practice.

### Treatment and measurement

7. **Heartbeat is an oracle-derived evidence treatment.** It can reveal which channels correspond to currently pending tasks, and task-reminder mode can reveal action text/urgency; comparison with baseline does not isolate an internal memory mechanism.
8. **Hierarchical and vote methods are package/replay treatments.** They change prompts, agent count, evidence union, action aggregation, latency, and error recovery. Majority/unanimity results are post-hoc views of the same union run, not fresh stochastic trials.
9. **Equal-weight F1 ignores consequence.** False medication, missed deadline, premature administrative action, and harmless lure share one count. Precision/recall is useful diagnosis but not expected harm or utility.
10. **Exact-step ground truth embeds one timing policy.** One-step event lateness and 60-minute time lateness are diagnostics, not empirically validated action windows; irregular step spacing makes those windows non-equivalent.
11. **Query counts are not monitoring cost.** There is no action/token/time budget tradeoff, information acquisition price, concurrent-task decrement, or total compute/cost objective.
12. **Update hit rates can hide update reasoning.** A correct final action does not show whether the agent encoded the update, forgot the predecessor, inferred from the menu, or guessed; no access/adoption/substitution intervention identifies the path.
13. **The menu is both affordance and memory support.** Active action text is repeatedly displayed, which reduces content retention demands while leaving cue/time binding. This is legitimate, but the claim should be “intention timing and selection with refreshed action affordances,” not unaided prospective memory.

### Statistics, reproducibility, and operations

14. **One attempt per configuration/model/week.** No solver repeats, alternative seeds, confidence intervals, paired randomization, or cluster-aware uncertainty support ranking stability.
15. **Strong dependence and partial reuse.** Eight configurations share model/week/task lineage, and three hierarchical scores derive from each model's same union-query trajectory.
16. **Incomplete run identity.** Logs omit exact provider/model revision, scenario/config/prompt hashes, token/cost usage, retry summaries, and environment identity despite including durations and backend labels.
17. **Public fixed-form saturation risk.** Scenario, ground truth, generator, prompts, scorer, and outputs are all public; no private split or lifecycle policy is described.
18. **Operational realism is low by design.** There are no real applications, artifacts, affected parties, permissions, irreversible effects, changing external state, team handoffs, or stakeholder acceptance.
19. **Release licensing is unclear.** The pinned repository has no repository-level license file, limiting reuse clarity.

## Reproducibility and operational realism

**Inspectability is high.** The near-paper commit contains the exact canonical scenario, deterministic generator, runtime, scorer, configuration implementations, released trajectories, report builder, and prompt logs. Canonical validation and report regeneration passed locally. Perfect-play solvability is executable rather than asserted.

**Exact paper-run reproducibility is moderate-low.** Aggregate report generation from released logs is reproducible, but generating the model trajectories anew requires mutable proprietary and hosted endpoints. Missing model/provider revisions, prompt/config/scenario hashes, usage, retry summaries, environment lock, and seeds prevent byte-identical inference reproduction. The deterministic default generator produces the canonical structure, but provenance should be embedded in the scenario rather than inferred from the wrapper.

**Operational realism is intentionally bounded.** PM-Bench is a board-game-like diagnostic simulator. It is useful for controlled cue/update/timing failures, not evidence that an agent can preserve commitments while performing professional work, handle real side effects, or improve stakeholder outcomes.

## Comparison with adjacent reviewed benchmarks

- **LongMemEval-V2** isolates experience-to-evidence retrieval but stops before action. PM-Bench adds timed action and monitoring, yet its action is menu selection without a work artifact. Both need evidence access/adoption instrumentation before causal failure labels.
- **MemoryArena** makes earlier sessions consequential to later actions but confounds memory with feedback and domain pipelines. PM-Bench is much more controlled and replayable, but lacks MemoryArena's consequential downstream environment work.
- **OdysseyBench** distributes hidden requirements through dialogue and checks office state, supplying an evidence-to-artifact consequence that PM-Bench lacks. It is less controlled and has narrow/defective graders. Their complementary design is delayed requirement timing plus artifact/state consequences, not either scalar score alone.
- **MemOps** provides explicit expected update/forget/trajectory probes. PM-Bench provides realized timing and suppression outcomes, but neither uniformly records actual internal write, retrieval, access, adoption, or causal use.

## Transfer to skill-bench

### Retain

1. A typed obligation state machine with activation, due condition, update, cancellation, dependency, completion, and lateness.
2. Separate narrative-visible, time-visible, and query-only cue channels.
3. Menus that mix legitimate actions with lures and keep canceled actions observable.
4. Perfect-play solvability checks and deterministic replay of action traces.
5. Separate exact-step TP/FP/FN from late, commission, wrong-content, update, dependency, and monitoring diagnostics.
6. Model-independent trace replay for explicitly labeled aggregation-policy ablations.

### Repair

1. Bind each delayed obligation to a real primary artifact/workflow criterion and preservation invariant. Monitoring or remembering must consume budget or create observable interference.
2. Record `instruction source/authority → encoded obligation → update/supersession → cue availability → query/access → presented evidence → adoption/rejection → attempted action → realized state → criterion consequence`.
3. Cross obligation support (`none / neutral periodic interrupt / channel hint / task reminder / oracle cue`) with matched work tasks; name each as an evidence intervention.
4. Use multiple generated forms with held-out seeds and bridge items. Retain generator version, seed, attempt, scenario hash, template lineage, and ground-truth hash in every bundle.
5. Weight or stratify errors by deadline width, reversibility, authority, stakeholder, consequence severity, and recovery cost; do not replace plural metrics with one utility number.
6. Add matched diagnostic interventions: oracle-retention, oracle-cue-access, cue-substitution, update-removal, irrelevant reminder, and action-control assistance. These separate encoding, monitoring, updating, and selection.
7. Repeat stochastic trials and report task/week/model-clustered uncertainty, invalid/retry rates, latency, tokens, calls, and cost.

### Do not infer

Do not infer general memory ability, human-like prospective memory, professional reliability, concurrent-work competence, expected safety, deployment readiness, or a universally best scaffold from PM-Bench Set-F1. Do not call a query-heavy failure a memory failure without showing whether the obligation was encoded, the cue was available/accessed, the evidence was adopted, and the action policy selected correctly.

## Concrete repository actions

No new queue task is warranted. Existing benchmark-bundle, trace, evidence-chain, longitudinal, metric, task-health, and experience-to-consequence contracts already have nonduplicate homes for PM-Bench's useful requirements. The next selected cross-domain pilot should instantiate one **dual-task prospective obligation slice**:

1. a primary artifact with graded quality/preservation constraints;
2. one delayed hidden-channel requirement, one update/cancellation, and one lure;
3. matched neutral-interrupt, channel-hint, and oracle-reminder conditions;
4. separate obligation, primary-work, query/cost, access/adoption, and collateral-effect outcomes;
5. repeated equivalent forms with scenario and configuration hashes.

This should refine an existing pilot rather than create a PM-Bench-specific schema.

## Claim boundary

PM-Bench v1 provides credible, release-inspectable evidence that selected 2026 model–scaffold packages differ on one deterministic synthetic week of delayed obligation selection, that update/cross-day/hidden-channel slices remain difficult in those runs, and that aggressive monitoring/reminder/aggregation can trade recall for many false actions. Its executable state machine, solvability checks, plural diagnostics, and released traces are strong benchmark machinery.

It does **not** establish general prospective-memory capacity, human comparability, concurrent-task interference, professional reliability, expected operational harm, causal failure origin, stable scaffold rankings, or deployment fitness. For skill-bench, the key repair is to connect PM-Bench-style delayed obligations to consequential primary work and score both sides of the dual task.