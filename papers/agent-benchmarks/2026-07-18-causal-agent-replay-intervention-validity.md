# Paper Review: Causal Agent Replay intervention validity

- **Paper:** <https://arxiv.org/abs/2606.08275v1>
- **Title:** *Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures*
- **Author:** Jaineet Shah
- **Date read:** 2026-07-18
- **Version read:** immutable arXiv v1, submitted 6 June 2026
- **Local PDF:** `data/papers/pdfs/2606.08275v1-causal-agent-replay.pdf` (5 pages; SHA-256 `477f92f0ebe56eff5ec4e795e974ab797d651e606dc707eae64f5153d2bf6085`)
- **Local text:** `data/papers/text/2606.08275v1-causal-agent-replay.txt` (SHA-256 `f7d36e977002205dd51bc3b7e39e9da44563043cd39dabe9a72c625e8bb0020a`)
- **TeX source:** `data/papers/source/2606.08275v1-source.tar` (SHA-256 `28c9e83bf6ed56942aa1154b9fcb923e9b73845a5cc08e3757e5e9b468998870`)
- **Official release inspected:** <https://github.com/jaineet17/causal-agent-replay/tree/db90fa28b97164c35e7c524e4597b8cbdb3035af>
- **Archived release:** `data/sources/releases/2606.08275v1-causal-agent-replay/jaineet17-causal-agent-replay-db90fa2.zip` (SHA-256 `c981e0a3b6d645be25bbddc780dfda6dcbe931a9d8e0efefeb364c9b44ea16f6`)
- **Release provenance:** `data/sources/releases/2606.08275v1-causal-agent-replay/provenance.json`
- **Timing boundary:** release commit `db90fa28b97164c35e7c524e4597b8cbdb3035af` is dated 9 July 2026, more than a month after v1. Its paper source has a new Who&When section absent from immutable v1. It is an author-linked post-v1 implementation, not proved paper-time code.
- **Tags:** counterfactual-replay, causal-attribution, interventions, stochastic-policy, point-of-commitment, Shapley, trace-diagnosis, repair-validity

## One-sentence contribution

CAR turns trace diagnosis into an executable intervention experiment—hold a factual prefix or coalition of actions, resample the remainder under a supplied policy and environment, score repeated continuations, and report contrastive or Shapley effects—but immutable v1 validates only two tiny mocked SCMs, while the release's replay semantics do not preserve exogenous/environment state or intervention support and its confidence procedure can declare a one-sample rescue certain; the warranted result is therefore a configured suffix-replay effect, not an identified natural cause, minimal repair, or operational debugging benefit.

## Why this matters for skill-bench

`skill-bench` already distinguishes the surface where failure appears from the earliest supported cause. CAR supplies the missing experimental instinct: **a diagnosis should survive an intervention**, not merely resemble an annotated span or a plausible explanation. This directly complements the DRIFT/TELBench review, which showed that claim/support-shaped localization can agree with adjudicated harmful spans without proving repair.

The reusable chain is:

```text
factual event/state
→ declared intervention target and replacement mechanism
→ preserved versus resampled variables
→ replay-valid branch
→ repeated outcome and uncertainty
→ bounded intervention effect
→ interaction allocation
→ candidate diagnosis
→ minimal/natural repair test
→ collateral and recurrence test
→ operational utility claim
```

CAR executes the middle of this chain. It does **not** make the joins on either side automatic. A factual action can be observed without being causal. A suffix replay can show that another sampled continuation avoids the outcome without identifying the earliest cause. A forced action can flip the outcome while being impossible under the counterfactual context. A scalar evaluator can improve while a collateral obligation worsens. A synthetic planted locus can validate code paths without establishing that production environments can be replayed.

This review advances charter objectives A–C through narrow, cross-domain diagnostic machinery. Customer support and multi-agent logs are examples, not scope commitments. Useful completion is a claim boundary and executable falsification of replay assumptions—not another causal-attribution subsystem.

## Research question and licensed claim boundary

The paper asks whether one can identify which step in a failed LLM-agent trajectory caused the outcome by representing the run as a structural causal model, intervening on an action or context, rerunning the suffix under a stochastic policy, and measuring the resulting outcome distribution (Sections 1–4, pp. 1–3).

### What immutable v1 supports

1. It specifies a compact trajectory vocabulary—decision state, action, observation, and scalar outcome—and five intervention types (Section 2, p. 2).
2. It correctly insists that stochastic replay yields an outcome distribution rather than one counterfactual path, and that uncertainty should be reported (Sections 2–4, pp. 2–3).
3. It identifies a genuine localization confound: resampling an early step rerolls every later stochastic decision, so an irrelevant early step can inherit the effect of a later pivotal step (Section 4, p. 3).
4. It supplies two complementary estimands: prefix-held suffix resampling for a latest-rescue “point of commitment,” and coalition-based Shapley allocation for interactions (Section 4, p. 3).
5. On the author's three-step mocked policies, the released code reproduces the paper's planted pivotal-step result and two-step interaction values. My exact release run produced Shapley values `0.4391`, `0.4479`, and `0.0224`, with efficiency sum `0.909375`; v1 reports rounded `0.44`, `0.45`, approximately zero, and `0.909` versus analytic `0.91` (Section 5, pp. 3–4).
6. The post-v1 release is substantial and executable: all 77 tests passed under its locked Python 3.12 environment.

### What immutable v1 does not support

It does not establish that an agent trace is a causally sufficient state; that recorded messages preserve provider, hidden service, memory, scheduler, tool, or environment exogenous variables; that live tool state is reset between branches; that forced factual actions remain supported under changed contexts; that the latest significant rescue is the unique, earliest, necessary, or sufficient cause; that Shapley credit is causal blame; that one scalar outcome captures collateral effects; that confidence intervals have advertised coverage; that synthetic effects transfer to organic failures; or that diagnosis-guided repairs improve repeated knowledge work, human debugging, cost, safety, professional validity, production fitness, or readiness.

Immutable v1 contains no real-agent benchmark table, repeated hosted/local-model fidelity experiment, natural-failure validation, expert comparison, repair study, human study, or cost measurement. Figure 1 is a mocked support-agent demonstration (Sections 5 and 7, pp. 3–5). The later repository contains a Who&When study narrative, but those results are absent from v1 and the archive contains no raw benchmark-result JSONL or table-reconstruction artifact.

## Methodology and system

### Trajectory and “SCM” representation

The paper writes a trajectory as

`τ = [s0, (a1,o1), …, (an,on), y]`,

where each decision state includes system prompt, tool schemas, and full message history; the action is sampled from policy `π`; the environment returns an observation; and user-supplied `Y(τ)` produces a score in `[0,1]` (Section 2, p. 2).

This is a useful transition-system schema. It is not yet a complete SCM specification. V1 does not enumerate exogenous variables, structural equations, a causal graph, consistency assumptions, interference boundaries, or a unit-level counterfactual coupling. Provider randomness, tool state, clock, network, service versions, external data, concurrent actors, hidden memory, caches, permissions, scheduler decisions, evaluator randomness, and branch history are not represented as variables with preservation policies. Calling the trace an SCM therefore states an intended causal reading more strongly than the recorded object justifies.

The release's `State` records system prompt, tool schemas, model, provider, sampling dictionary, and messages (`src/car/schemas/trajectory.py:48-84`). This supports request reconstruction for narrow single-agent tool loops. It does not capture endpoint revision, serving policy, model weights, tokenizer, hidden reasoning state, provider-side routing/batching, tool implementation/version, environment snapshot, clock, credentials, filesystem/database state, network responses, side-effect receipts, other actors, or outcome-function identity. `request_digest()` hashes only the declared JSON request fields; equal hashes imply equal recorded requests, not equal action distributions or worlds.

### Five intervention operators

The paper defines (Section 2, p. 2):

- `do_resample(k)`: redraw action `a_k` from the same policy;
- `do_action(k)`: force an action;
- `do_observation(k)`: replace a tool result while holding the factual action;
- `do_context(k)`: edit message history;
- `do_policy(k)`: swap the model from that step onward.

The release implements these as typed discriminated models and reduces each to a choice of context, action, observation, and policy passed to `run_forward` (`src/car/replay/intervene.py:61-170`). That is a clean engineering interface.

The operators answer different questions and should not share an undifferentiated “causal effect” label:

- resampling estimates sensitivity to the supplied policy distribution;
- forcing an action estimates one authored substitution;
- replacing an observation estimates sensitivity to an authored environment value;
- editing context estimates a prompt/history treatment;
- changing policy estimates a component-treatment effect.

Only the first is used for the paper's point-of-commitment locator. None independently proves naturalness, support, minimality, feasibility, authority, or safety of the intervention.

### Prefix-held suffix replay

For contrastive attribution, the implementation holds factual actions `[0,k)` and resamples `k` onward (`src/car/attribute/contrastive.py:71-131`; `src/car/attribute/sampling.py:28-64`). The factual observed outcome is scored once. For each step, `K` child trajectories are rerun and the effect is `P_bad(intervened) - P_bad(observed)`.

This is best interpreted as:

> Conditional on this recorded factual prefix, this supplied policy/environment/evaluator realization, and this branch-generation procedure, how often does rerunning from index `k` avoid the selected bad label?

It is not a unit-level counterfactual for “the same run with only step `k` changed,” because every downstream stochastic action and live observation can change. V1 explicitly acknowledges the total-effect-through-continuation issue and leaves common random numbers for future work (Section 7, p. 5). More fundamentally, common random numbers would reduce variance only if the two branches expose meaningfully coupled exogenous variables; divergent prompts, tool calls, and episode lengths make that coupling a substantive design choice.

### Point-of-commitment rule

The paper chooses the latest step whose effect interval excludes zero—the last index where rerunning can still rescue the outcome (Section 4, p. 3). The code operationalizes “rescue” as a negative bootstrap effect with a zero-excluding interval and takes the last such index (`src/car/attribute/contrastive.py:111-116`).

This rule repairs one specific early-step magnitude confound in monotone commitment-like traces. It is not a general causal-localization theorem. It can fail when:

- a late recovery/override action can still rescue an earlier cause;
- a later independent defect also affects the outcome;
- an outcome requires several jointly bad actions;
- step boundaries change across branches;
- resampling a final answer changes the score despite an earlier state defect;
- tool/environment drift creates a late rescue;
- evaluator drift creates a late rescue;
- multiple tested intervals produce a late false positive;
- an early irreversible state mutation is followed by a later compensating action;
- the “latest” rescue is a feasible mitigation but not a cause.

The paper's “point of commitment” is therefore an intervention-policy label: latest index at which this configured rerun procedure still yields detectable rescue. It may be useful for repair even when it is not the earliest root, and useless when the available late rescue is unnatural or damaging.

### Coalition and Shapley attribution

CAR defines a coalition `S` as factual step indices held at their recorded actions; all other indices are resampled. Its value is `v(S)=P(bad | held=S)`, and Monte Carlo permutation sampling allocates average marginal changes, paired with reverse permutations (`src/car/attribute/shapley.py:69-249`).

The interaction motivation is sound: independent single-step effects can double-count or miss jointly sufficient conditions. But the released coalition game has three load-bearing semantics:

1. **Players are factual indices, not stable decisions.** Counterfactual trajectories can terminate early, grow longer, or contain different semantic actions at the same index.
2. **A held action is forced under whatever context the resampled predecessors create.** `coalition_forward` explicitly holds factual `a_k` even when context differs (`src/car/replay/forward.py:118-128`). This may create an impossible or policy-zero action.
3. **Observations are not held with actions.** Even `held=all` re-executes tools in the live environment (`src/car/replay/forward.py:146-159`). The code comment says all-held reproduces the factual trajectory, but that is true only for stationary deterministic/mock environments.

Accordingly, the Shapley values fairly allocate the value of this **index/action-forcing game**. They do not automatically allocate causal responsibility in the natural agent process. Shapley symmetry and efficiency are properties of the chosen value function; they cannot validate the game's support, state sufficiency, outcome authority, or moral/operational blame semantics.

### Outcome functions

The package supports deterministic rule outcomes and LLM judges. The paper appropriately prefers rules and flags judge noise (Section 7, p. 5; `src/car/outcome/functions.py:1-13`).

The interface nevertheless compresses a trajectory to one label and one `[0,1]` score. It does not natively require separate primary quality, safety, side effect, authority, cost, latency, artifact integrity, and collateral-change outcomes. A substitution that avoids `bad_label` while creating a different harm is counted as a rescue unless `Y` captures it. Repair utility therefore requires a vector of noncompensatory outcomes and explicit loss/acceptance policy, not one outcome shift.

## Evidence and result interpretation

### Pivotal-step fixture

The factual mocked support run is `lookup_order → issue_refund → final`. At step 1, a seeded policy samples the bad refund with probability `0.3` and escalation otherwise. The outcome is bad iff `issue_refund` appears (`tests/synthetic_scms.py:40-76`). Resampling at or before step 1 can remove the refund; resampling the final step cannot. With 80 samples, the released test selects step 1 (`tests/test_attribution.py:53-68`).

This validates that the implementation recovers a locus designed to match its rule. It does not test context dependence, observation-mediated decisions, hidden state, branch-specific step identities, stateful tools, competing causes, nonmonotone recovery, off-support actions, evaluator error, or natural failure.

### Two-step interaction fixture

The second fixture has factual `bad_a → bad_b → final`; the outcome is bad iff both tool calls occur. Each bad action is independently sampled with probability `q=0.3` (`tests/synthetic_scms.py:79-101`). The analytic all-held versus none-held value is `1-q²=0.91`. My run under the released test settings exactly reconstructed the reported rounded values:

| Step | Released local value | 95% normal CI |
|---|---:|---:|
| 0 | 0.4391 | [0.4154, 0.4627] |
| 1 | 0.4479 | [0.4259, 0.4700] |
| 2 | 0.0224 | [-0.0001, 0.0449] |
| sum | 0.909375 | — |

This is credible code-path evidence for one stationary independent Bernoulli game. The final step's finite-sample value is not exactly zero, as the paper's `≈0` correctly indicates. The test tolerances are wide (`±0.15` per interacting step and `±0.2` on efficiency), and there is only one interaction form. No alternative causal graph, correlated noise, mediator, OR/redundant cause, suppressor, varying horizon, support violation, or stateful environment is tested.

### Confidence intervals

The paper says every effect is reported with confidence intervals and mentions Wilson intervals for proportions, bootstrap intervals for differences, and normal intervals for Shapley marginals (Sections 3–4, pp. 2–3). The release does implement all three.

The interval used to select the contrastive locus is the percentile bootstrap difference against a one-observation factual baseline, not the Wilson interval. At boundary samples it is severely overconfident. My direct audit passed a single factual bad observation and one rescued rollout to `prob_label_effect`; the release returned:

```text
point=-1.0, 95% CI=[-1.0,-1.0], n_baseline=1, n_intervened=1
```

Thus `K=1` can declare a rescue statistically significant with a zero-width interval. Resampling one observed Bernoulli value reproduces the same value in every bootstrap draw; this is an artifact of the nonparametric percentile bootstrap, not evidence of certainty. The package separately knows the Wilson interval is wide for all-success small samples (`tests/test_effects.py:110-119`) but does not use that uncertainty for locus selection.

Other inferential limits include:

- no simultaneous/multiplicity correction across trajectory steps;
- adaptive comparisons if users inspect and rerun selected interventions;
- no uncertainty for environment/provider/evaluator versions or task sampling;
- possible dependence from sharing one mutable policy and environment across rollouts;
- normal Shapley intervals with zero width when only one marginal is available;
- no efficiency-sum interval;
- no failed/invalid branch contribution policy beyond raising;
- no stopping-rule-adjusted coverage.

The intervals quantify Monte Carlo variation only under the release's branch generator, and in the smallest cases not reliably even that.

## Release audit and executable adversarial checks

### What the release provides

The archived post-v1 repository contains 90 tracked files: typed schemas, native recording, storage, five intervention operators, deterministic and forward replay, contrastive/Shapley estimators, budget counters, HTML reports, LangGraph/OpenAI Agents/CrewAI adapters, Who&When surrogate tooling, research notes, examples, and 77 tests. `uv sync --extra dev && uv run pytest -q` completed successfully under Python 3.12.13: **77 passed**, with 65 dependency deprecation warnings.

This is meaningful implementation evidence. The release is far more than a paper stub, and the core code is small enough to inspect.

### Paper/release correspondence

The exact TeX in the immutable v1 source differs from `paper/main.tex` at the release commit. The later file adds an entire Who&When evaluation section, headline `20.7%` step-exact accuracy, `121/126` completion, `120/121` factual-failure reproduction, and later analysis. These claims were not in the version read.

The archive contains five example Who&When JSON files and scripts, but no full raw result JSONL, no 121-row attribution output, no exact model/runtime receipts, and no table-builder input sufficient to reconstruct those numbers. `RESEARCH/phase_6_benchmark.md` describes a week of intermittent local compute and post-hoc rule comparisons, but prose is not a retained result ledger. This review therefore treats Who&When as **post-v1 release narrative**, not immutable-paper evidence or independently reproduced evaluation.

### Environment state is not replayed or reset

`run_forward` and `coalition_forward` call a supplied live `Environment` object for observations. `coalition_distribution` shares that same object across all nominally independent children and does not clone, snapshot, reset, seed, or transact it (`src/car/attribute/sampling.py:49-64`).

I supplied a deterministic counter environment whose result increments on every call. Three “independent” branches returned labels `['1','2','3']`, with final environment count `3`. The differences came entirely from branch order and shared world mutation. The method would interpret them as outcome-distribution variation unless the evaluator or caller detects the invalid environment.

This is not a corner case for knowledge work. Files, databases, tickets, SaaS records, clocks, rate limits, caches, search indexes, network services, and human inboxes are stateful. CAR's paper honestly puts real side-effecting tools out of scope (Section 7, p. 5), but the post-v1 README says adapters re-execute “your tools live.” Without per-branch snapshots, transactional rollback, read-only simulation, immutable recorded responses, or a validated environment model, live replay is not intervention evidence.

### Coalition actions can be off support

I built a policy that resamples step 0 to `good_a` and, under that observation, would always choose `good_b` at step 1. Holding only factual step 1 nonetheless produced:

```text
['good_a', 'bad_b', 'final']
```

The release forced factual `bad_b` under a context in which the supplied policy would never select it. No support score, applicability predicate, action precondition, tool-argument validity check, or naturalness disposition is recorded. Such a branch can still be useful as a surgical intervention, but its estimand is an authored off-policy patch—not natural replay or individual causal responsibility.

### Evaluator drift can manufacture a locus

I supplied a stateful outcome function that labels only its first call bad and all later calls good. The policy and environment were otherwise deterministic and unchanged. With one sample per step, CAR reported every step as a certain rescue and selected the last step as the causal locus:

```text
step effects: (-1,[-1,-1]), (-1,[-1,-1]), (-1,[-1,-1]); locus=2
```

The package does not bind evaluator hash/version/state, repeat a factual control interleaved with branches, or run sham/no-op controls by default. An LLM judge, mutable external checker, time-dependent source, or stateful grader can therefore be mistaken for an agent-step effect.

### No-op behavior is correct but insufficient

With a deterministic scripted policy, stationary mocked environment, and deterministic outcome, resampling every step produced zero effects and no locus. This is a useful null-path check. It does not expose the environment/evaluator drift cases above because the released synthetic suite fixes both by construction.

### Missing replay-validity gates

The package has a deterministic reconstruction report for message-state self-consistency and action-match rates (`src/car/replay/deterministic.py`). Contrastive and Shapley attribution do not require that report to pass, attach it to results, or gate claims on it. Nor do results retain:

- complete configured-system hashes;
- environment snapshot/reset receipts;
- branch-level exogenous/seed identity;
- tool implementation/version and side-effect policy;
- action-support or precondition evidence;
- outcome-function hash/repeat reliability;
- invalid branch counts and reasons;
- factual/sham interleaved controls;
- changed-versus-preserved variable manifests;
- branch artifacts, state deltas, or collateral outcomes;
- alternative repair set and minimality checks.

The result models retain aggregate effects, sample counts, confidence, and locus/values. That is enough for a demo, not for an auditable causal claim.

## Unique insight

CAR's most important contribution is not that rerunning an agent “proves” a cause. It is that **diagnostic labels should be treated as claims with intervention-specific warrants**.

A trace can support several non-equivalent statements:

1. **Observed event:** action or state appeared in the factual trace.
2. **Outcome-associated event:** the event covaries with failure across observations.
3. **Configured resampling sensitivity:** rerunning a suffix at this index changes the outcome distribution.
4. **Supported substitution effect:** a declared, feasible replacement changes the outcome under a replay-valid world.
5. **Pivotal step under a declared policy:** latest/earliest step satisfying a specified rescue rule.
6. **Interaction credit:** Shapley or another rule allocates one declared coalition game's value.
7. **Earliest sufficient cause:** no earlier supported alternative explains the outcome under the admissible intervention class.
8. **Minimal natural repair:** the smallest feasible in-support change reliably repairs equivalent cases.
9. **Operationally useful diagnosis:** using the diagnosis improves repair, recurrence, collateral quality, review burden, and cost.
10. **Professional or production validity:** target-domain authority and field evidence license consequential use.

CAR directly implements evidence toward rungs 3–6. Its synthetic fixtures validate those calculations under authored worlds. It does not establish rungs 7–10.

The second insight is that replay validity requires **three coupled identities**:

```text
actor mechanism: policy/configuration + admissible action support
world mechanism: environment state/transition + exogenous event coupling
observer mechanism: outcome/evaluator identity + evidence view + reliability
```

Holding only the model label and message prefix is insufficient. A branch can change because the actor changed, the world drifted, or the observer drifted. Causal attribution is valid only when those channels are either preserved, intentionally intervened, or marked invalid.

The third insight is that **repair and cause are orthogonal orderings**. Earliest cause, latest point of commitment, cheapest intervention, safest mitigation, smallest edit, and best operational repair can be different steps. Benchmarks should score them separately rather than force one “root cause” index.

## Limitations and validity threats

1. Immutable v1 is only five pages and omits many implementation and experimental details.
2. The trajectory tuple is called an SCM without explicit exogenous variables, structural equations, graph, or identification assumptions.
3. Recorded state excludes provider-side and environment-side hidden variables.
4. Equal request digests do not imply equal action distributions.
5. Provider endpoint/model revision and serving configuration are not immutable components of the trace.
6. Tool implementations, versions, credentials, clocks, network state, and external data snapshots are not bound.
7. Real side-effecting tools are explicitly out of paper scope.
8. The post-v1 README nevertheless presents live tool re-execution as an adapter path.
9. Branches share one environment object without required clone/reset/snapshot semantics.
10. Stateful environment drift can create branch variation and interference.
11. Concurrent branches can race on policy or environment state.
12. No branch-level seed or exogenous-noise ledger supports matched coupling.
13. Common random numbers are acknowledged but unimplemented.
14. Recorded-prefix actions are held without revalidating preconditions in changed worlds.
15. Shapley factual actions are forced under divergent contexts without support checks.
16. Factual step indices are not stable semantic players when branches change length or action meaning.
17. All-held Shapley coalitions re-execute observations and need not reproduce the factual trajectory.
18. Early termination means some factual players may never be exercised.
19. `do_context` edits text but has no semantic preservation, authority, or confound audit.
20. `do_observation` can install impossible values without environment constraints.
21. `do_action` can force unsafe, unauthorized, or infeasible actions.
22. `do_policy` changes model identity but may also change formatting, tool protocol, context limits, and sampling support.
23. Contrastive effects are total suffix effects, not isolated direct effects.
24. The point-of-commitment rule assumes a useful latest-rescue structure not guaranteed in nonmonotone workflows.
25. Late mitigation can be mislabeled as cause.
26. Multiple independent or interacting causes can make one latest index misleading.
27. No multiplicity correction covers per-step significance tests.
28. The bootstrap difference interval is degenerate at boundary samples.
29. One rescued rollout can produce a zero-width 95% interval and a “significant” locus.
30. The Wilson interval is calculated by the package but not used for locus selection.
31. A size-one observed baseline is treated as fixed; no uncertainty over factual run selection is represented.
32. Shapley normal intervals can be zero-width with one marginal.
33. Antithetic pairs and shared state complicate independence assumptions.
34. No uncertainty covers task, failure, policy, environment, or evaluator sampling.
35. No simultaneous interval or selection-adjusted inference supports the chosen locus.
36. Judge-based outcomes can drift or share model-family error with the policy.
37. Outcome-function identity/version/hash is absent from attribution results.
38. No interleaved factual or sham control detects evaluator/environment drift.
39. One scalar outcome can hide collateral harms and regressions.
40. No noncompensatory safety/authority/artifact-integrity gates are required.
41. Failed branches raise and abort rather than enter a typed invalid/missingness ledger.
42. The budget counts samples, not tokens, latency, provider spend, tool cost, or human burden.
43. Budget truncation can return partial or empty Shapley estimates without decision-calibrated precision.
44. The pivotal fixture is structurally aligned with the latest-rescue rule.
45. The interaction fixture is one independent Bernoulli AND gate with stationary mocked tools.
46. There are no mediator, confounder, redundant-cause, suppressor, OR-gate, nonmonotone, or context-dependent ground-truth fixtures.
47. Test tolerances are broad relative to the tiny synthetic design.
48. Synthetic SCM recovery validates software behavior under authored assumptions, not assumptions in real traces.
49. Immutable v1 has no organic failure corpus or realistic knowledge-work benchmark.
50. It reports no human attribution comparison, repair study, recurrence reduction, or debugging-time outcome.
51. It reports no hosted-model action-match experiment despite discussing provider nondeterminism.
52. It reports no total runtime, tokens, monetary cost, or cost–precision frontier.
53. The support-agent prompt-injection figure uses mocked reproducible tools.
54. The release commit postdates v1 by more than a month.
55. The release's paper source adds a Who&When evaluation absent from immutable v1.
56. Full Who&When result rows and table-reconstruction records are absent from the archive.
57. The later Who&When rules include post-hoc comparisons and point-estimate fallbacks that differ from v1's headline CI-gated rule.
58. The package's 77 passing tests establish implementation conformance only within tested conditions.
59. No adversarial test in the release detects shared environment state, off-support coalitions, evaluator drift, or one-sample CI certainty.
60. No evidence licenses natural-root, minimal-repair, professional-capability, safety, production, or readiness claims.

## Reproducibility and operational realism

**Core synthetic reproducibility is high.** The immutable PDF/text/TeX are preserved; the release is complete and pinned; dependency locking works; all 77 tests pass; and the reported Shapley numbers are exactly reconstructible to rounding. This is strong evidence that the released post-v1 engine implements the stated synthetic coalition calculation.

**Paper-level empirical reproducibility is narrow.** V1 contains only mocked synthetic evidence. There is no retained run matrix beyond tests and the generated demo. The later release manuscript and research note add Who&When results, but exact rows, model receipts, failures, continuations, judgments, and analysis inputs are absent. Those numbers cannot be rebuilt from the archive.

**Operational realism is low for consequential knowledge work.** Message/action/tool-loop instrumentation is relevant, and framework adapters make the mechanism testable. But real knowledge-work environments contain mutable documents, databases, applications, permissions, collaborators, services, clocks, and side effects. CAR currently reuses one live environment without a required snapshot/rollback contract and lacks collateral-state grading. It is best suited to mocked, read-only, simulatable, or transactionally isolated worlds. Production use would additionally require privacy controls, safe intervention authority, cost budgets, evaluator calibration, invalid-branch handling, and evidence that diagnosis improves human or automated repairs.

## Transfer to skill-bench

### Retain

1. **Executed intervention before causal promotion.** A plausible span or dependency edge should remain a hypothesis until a replay, substitution, deletion, or repair test changes an independently observed outcome.
2. **Distributional suffix replay.** One continuation is not evidence; repeated configured branches and uncertainty are necessary.
3. **Separate contrastive and interaction estimands.** Latest-rescue localization and interaction allocation answer different questions.
4. **Mocked planted SCMs as conformance tests.** Every causal diagnostic should first recover known structures under controlled worlds.
5. **Explicit intervention algebra.** Action, observation, context, policy, and resampling interventions should remain typed.
6. **Budget-aware diagnostics.** Expensive interaction analysis should be on demand and precision/decision gated.

### Repair

1. **Replace “SCM” by an executable replay-validity contract unless assumptions are instantiated.** Record endogenous nodes, exogenous variables, structural transitions, preserved/intervened variables, support, consistency, interference, and horizon.
2. **Bind actor/world/observer identity.** Hash policy/scaffold/tools/environment/evaluator and record versions, permissions, clocks, seeds, source snapshots, and evidence views.
3. **Require branch isolation.** Clone or reset environments per branch; preserve initial-state hashes and final-state deltas; reject nonreplayable worlds.
4. **Type intervention admissibility.** Record feasibility, authority, policy support, preconditions, naturalness, semantic scope, and expected collateral dimensions.
5. **Separate factual action from factual transition.** Holding an action must not imply holding its observation; declare which variable pair is fixed and verify all-held reconstruction.
6. **Use valid small-sample uncertainty.** Replace degenerate percentile-bootstrap significance with an exact/Bayesian/binomial procedure suited to the declared estimand, plus simultaneous or hierarchical control across steps.
7. **Add sham and drift controls.** Interleave factual reruns, no-op context edits, equivalent actions, irrelevant observation patches, frozen evaluator repeats, and branch-order permutations.
8. **Score vectors, not one rescue label.** Keep target repair, new errors, safety, authority, artifact/state integrity, cost, latency, and collateral effects separate.
9. **Preserve branch-level records and invalidity.** Store every trajectory, state delta, tool receipt, outcome observation, exception, timeout, retry, and exclusion.
10. **Do not conflate cause and repair.** Report earliest supported cause, latest commitment, minimal change, feasible mitigation, and best operational repair as separate labels/decisions.

### Test

1. **Ground-truth graph suite:** pivotal mediator, confounded proxy, redundant OR causes, AND interaction, suppressor, delayed effect, reversible commitment, late mitigation, and clean no-op worlds.
2. **Environment conformance:** immutable, stateful-reset, intentionally persistent, nonreplayable, clock-dependent, and concurrent-actor worlds; require branch-order invariance where appropriate.
3. **Support mutations:** force factual actions after changed contexts, invalid tool arguments, impossible observations, early termination, and shifted semantic step identities; ensure unsupported branches abstain rather than become natural causal evidence.
4. **Observer factorial:** deterministic rule, noisy frozen judge, drifting judge, incomplete evidence view, and collateral-harm observer; cross evaluator versions and interleaved factual controls.
5. **Uncertainty calibration:** simulate known Bernoulli effects across `K`, step counts, adaptive stopping, and shared dependence; measure coverage, family-wise false loci, power, and abstention.
6. **Repair ladder on existing pilots:** original, sham, injected, diagnosed correction, alternate correction, dual fault, and overcorrection under repeated seeds and isolated state; measure recurrence and collateral regressions.
7. **Human utility:** matched raw-trace versus diagnosis-assisted review with blinded repair success, time, false leads, confidence calibration, and burden.

## Concrete repository actions

- [x] Read the complete immutable v1 PDF/text and verify it against the TeX source.
- [x] Inspect the complete 90-file author-linked post-v1 release with explicit timing boundaries.
- [x] Run the locked release test suite: 77 passed.
- [x] Reconstruct the pivotal and interaction mechanisms and reproduce the paper's rounded Shapley values.
- [x] Compare immutable v1 TeX with the release manuscript and isolate the later Who&When addition.
- [x] Run adversarial executable checks for one-sample interval degeneracy, shared stateful-environment drift, off-support coalition actions, evaluator drift, and deterministic no-op behavior.
- [x] Separate observed event, configured replay sensitivity, supported substitution, pivotal step, interaction credit, earliest cause, minimal repair, operational utility, and professional/readiness claims.
- [x] Add no queue task. Existing trace/intervention, execution-isolation, artifact/state, invalid-trial, metric, task-health, uncertainty, root/surface, recovery, and validity machinery already houses these requirements. The existing internal intervention-attribution replay is the right empirical home; a CAR-specific schema or another synthetic-only build would duplicate it.

## Bottom line

CAR is a strong executable research prototype and a useful correction to purely observational trace diagnosis. Its five intervention types, repeated suffix replay, latest-rescue rule, and coalition Shapley estimator make causal assumptions testable rather than decorative. The post-v1 package is inspectable, its 77 tests pass, and its headline synthetic interaction values reproduce exactly to rounding.

The causal claim must remain narrower than the branding. The released object is not a complete SCM; it does not preserve or couple exogenous state, reset live environments, check action support, freeze evaluators, protect small-sample interval coverage, or score collateral effects. My adversarial checks showed that branch order in a shared environment changes outcomes, factual actions are forced in impossible counterfactual contexts, evaluator drift alone produces a last-step locus, and one rescued rollout receives a zero-width 95% interval. Immutable v1 validates two mocked authored worlds and nothing resembling consequential professional operation.

`skill-bench` should retain CAR's central discipline—**intervene before promoting a diagnosis**—while naming the actual estimand: a configured counterfactual effect under a declared actor, world, observer, intervention, and replay contract. Promotion to earliest cause or useful repair requires support-aware substitutions, isolated worlds, sham controls, valid uncertainty, alternative repairs, collateral outcomes, repeated equivalent cases, and eventually human/domain evidence. Synthetic recovery is software-conformance evidence, not natural-failure, professional-validity, production-fitness, or readiness evidence.

## Source links

- Immutable abstract: <https://arxiv.org/abs/2606.08275v1>
- Immutable PDF: <https://arxiv.org/pdf/2606.08275v1>
- Immutable source: <https://arxiv.org/e-print/2606.08275v1>
- Official repository: <https://github.com/jaineet17/causal-agent-replay>
- Pinned release: <https://github.com/jaineet17/causal-agent-replay/tree/db90fa28b97164c35e7c524e4597b8cbdb3035af>
- Local provenance: `data/sources/releases/2606.08275v1-causal-agent-replay/provenance.json`
