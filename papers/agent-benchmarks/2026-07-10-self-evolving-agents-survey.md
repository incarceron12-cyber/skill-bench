# Paper Review: A Survey of Self-Evolving Agents — What, When, How, and Where to Evolve

- **Paper:** https://arxiv.org/abs/2507.21046v4
- **Authors:** Huan-ang Gao et al.
- **Date read:** 2026-07-10
- **Venue / source:** Transactions on Machine Learning Research, January 2026
- **Version read:** immutable arXiv v4, 16 January 2026
- **Local PDF:** `data/papers/pdfs/2507.21046v4-a-survey-of-self-evolving-agents-what-when-how.pdf` (77 pages; SHA-256 `0b39df03feea2f4d8ac41e35a9247889978a53cb1e7b7d3eafaae76ad97b5602`)
- **Local text:** `data/papers/text/2507.21046v4-a-survey-of-self-evolving-agents-what-when-how.txt`
- **Companion repository:** https://github.com/CharlesQ9/Self-Evolving-Agents
- **Tags:** self-evolution, continual-evaluation, longitudinal-benchmarks, retention, cost, safety-drift, state-versioning

## One-sentence contribution

The survey organizes self-evolving agents by **what** changes (model, context, tools, architecture), **when** it changes (within or between tasks), **how** feedback drives change (reward, demonstration, or population methods), and **where** it is deployed, then makes its most actionable contribution by specifying short- and long-horizon evaluation protocols that treat the evolving system's state, learning trajectory, costs, retention, and safety drift as first-class evidence rather than collapsing them into a final pass rate.

## Why this matters for skill-bench

`skill-bench` aims to evaluate expert knowledge work and to compound what it learns. That creates two distinct objects that can evolve: the **evaluated agent** (memory, skills, tools, workflow) and the **benchmark program** (task specifications, source packs, rubrics, lessons). The survey provides a useful coordinate system for the former and a warning for both: once state persists, an evaluation is no longer a bag of independent trials. It is an intervention on a versioned learner moving through an ordered task stream.

The paper's strongest design implication is therefore not “support agent memory.” It is: **define the evolving state and its allowed transitions before interpreting improvement**. For each transition, a benchmark must know what component changed, what triggered it, what feedback was visible, what budget was consumed, what previous capability regressed, and whether the change can be replayed or rolled back. Sections 2.1, 7.1, and 7.2.4 jointly imply this contract, although the survey never formalizes it as an executable schema.

This also sharpens the project's distinction between compounding research and benchmark contamination. An agent that learns a transferable evidence-checking procedure has adapted; an agent that remembers a private answer or verifier outcome has leaked. Both may raise later success rates. The paper calls for full state persistence and replayable evolution logs but does not define information-flow boundaries. `skill-bench` must.

## Research question

The survey asks four descriptive questions: which agent components can evolve, at what temporal stage, through which learning mechanisms, and in which domains. It then asks the more consequential evaluation question: how should systems whose policies, contexts, tools, or architectures change across interactions be assessed for adaptivity, retention, generalization, efficiency, safety, and autonomy?

Its operational definition requires updates to be experience-dependent, persistent and policy-changing, and supported by autonomous exploration or self-initiated learning (Section 2.1, pp. 6–7). That is a valuable boundary because it excludes generic synthetic-data pipelines and transient instruction following. However, the survey subsequently relaxes the boundary to include “proto-evolution,” and some categorized methods reset weights or only revise within the current task. The taxonomy is thus best treated as a design vocabulary, not a cleanly applied inclusion rule.

## Methodology

### Survey and formalization

The paper is a broad narrative synthesis covering methods through 2025. It introduces:

1. a POMDP environment and an agent system `Π = (Γ, {ψᵢ}, {Cᵢ}, {Wᵢ})`, where `Γ` is topology, `ψ` model, `C` context, and `W` tools;
2. an evolution operator `f(Π, τ, r) = Π′` conditioned on trajectory and feedback;
3. a cumulative-utility objective over an ordered task sequence; and
4. an operational definition based on experience dependence, persistent policy effect, and agent initiative (Section 2.1, pp. 5–7).

The manuscript does **not** report a systematic-review protocol: no database/search strings, screening dates, inclusion/exclusion flow, duplicate handling, coder process, extraction form, inter-rater reliability, or quality appraisal. The companion repository is cited, but the paper itself does not establish that its catalog is exhaustive or reproducibly selected. Consequently, method counts and coverage statements should be read as expert-curated synthesis, not systematic evidence in the PRISMA sense.

### Taxonomy

- **What evolves:** model policy/experience; context through memory and prompt optimization; tools through creation, mastery, and selection; architecture at node, single-agent, workflow, or multi-agent level (Section 3, pp. 9–15).
- **When:** intra-test evolution couples feedback and updating to the current task; inter-test evolution consolidates completed-task experience for future tasks. Either can use context updates, supervised fine-tuning, or reinforcement learning (Section 4, pp. 16–18).
- **How:** reward-based methods use textual, internal, external, or implicit signals; imitation methods use self-, cross-agent, or hybrid demonstrations; population methods use selection, mutation, competition, and self-play. Cross-cutting axes include online/offline data collection, on/off-policy data, and outcome/process/hybrid reward granularity (Section 5, pp. 19–30).
- **Where:** general-domain evolution through memory, curriculum, and model-agent co-evolution versus specialized coding, GUI, finance, medicine, education, and other domains (Section 6, pp. 31–34).

These dimensions are useful prompts but not fully orthogonal. “Population-based” describes a search organization, while “reward” and “demonstration” describe supervision; population fitness is itself reward. “Architecture” appears under what, while single/multi-agent organization appears under how. “Where” mixes deployment domains with mechanisms under the general-domain branch. The paper recognizes cross-cutting dimensions, but its headline tree can still encourage mutually exclusive labels where multi-label records are needed.

### Evaluation framework

The survey separates five goals (Section 7.1, pp. 35–39):

- **adaptivity:** success-by-iteration, learning curves, adaptation speed;
- **retention:** forgetting (FGT) and backward transfer (BWT);
- **generalization:** held-out task/distribution performance over time;
- **efficiency:** tokens, time, steps, tool calls, memory growth, human oversight, tool productivity, and cost-per-gain;
- **safety:** safety/harm scores, completion under policy, violation risk, refusal, and leakage.

It then distinguishes static snapshots, short-horizon adaptation, and long-horizon lifelong assessment. Table 10 specifies no cross-task persistence for short-horizon tests, but full model/prompt/memory/tool persistence for long-horizon streams; per-task, stage, and cumulative evolution budgets; versioned data and OOD clusters; replayable trajectories and checkpoints; retention probes; decision logs; safety-drift probes; human-intervention accounting; and learning/forgetting matrices (pp. 44–45).

This is a protocol proposal and literature mapping, not an empirical validation study. The EvoAgent worked example shows how incompletely current systems report the proposed fields; it does not test whether the protocol yields reliable rankings or diagnoses.

## Evidence and findings

1. **Static evaluation dominates.** Table 7 catalogs many agent benchmarks, but only a small subset has short- or long-horizon scope; the paper observes that episodic reset makes accumulation and degradation literally unmeasurable (Sections 7.1.2 and 7.2.1, pp. 36–42).
2. **Retention is especially underserved.** The survey highlights dynamic-memory consistency, replay/context overflow, and insufficient repeats, and states that most benchmarks reset state between tasks (pp. 36–37). FGT and BWT provide a useful starting language, but assume task-indexed performance can be re-probed comparably.
3. **Efficiency reporting omits the evolution process.** Table 5 separates tokens, interaction steps, wall-clock time, tools, memory growth, and human oversight, then defines cost-per-gain. Existing papers rarely isolate reflection, replay, architecture search, or memory-update costs and usually impose no realistic hard budgets (pp. 37–38).
4. **Safety is measured episodically rather than as drift.** Existing safety tests expose tool robustness and coordination failures but do not trace whether repeated updates create, spread, or amplify unsafe behavior (pp. 38–39).
5. **Self-directedness is a treatment variable.** The paper recommends reporting who selected tasks/strategies, where feedback came from, and how often humans intervened, because otherwise performance gains may reflect external curriculum engineering rather than autonomous evolution (Section 7.1.6, p. 39).
6. **Longitudinal protocol coverage is poor even in a favorable example.** EvoAgent persists a world model and experience pool, caps subtasks, and reports success/exploration efficiency and wall time. It does not publish replayable iteration logs/checkpoints, FGT/BWT, cost-per-gain, token/memory drift, or long-run safety drift (Table 10, pp. 44–45).
7. **Fair comparison is currently infeasible.** Prompt formats, rollout budgets, tools, environments, model variants, control loops, and reporting differ. The authors appropriately present Table 11 as illustrative rather than causal (Section 7.3.2, pp. 46–47).

The numeric improvements quoted for WebRL, SEAgent, and other methods are secondary reports from cited papers, not results generated or independently reanalyzed by this survey. They indicate possible effect sizes but do not validate the taxonomy.

## Unique insight

The paper's deepest contribution is the shift from evaluating **outputs** to evaluating **state transitions**. A static benchmark asks whether configuration `Π₀` solves task `T`. A self-evolution benchmark must estimate the behavior of an update policy `f` over an ordered stream: `Πⱼ₊₁ = f(Πⱼ, τⱼ, rⱼ)`. Final success confounds at least five properties: initial ability, task order, feedback authority, update quality, and accumulated cost. The natural atomic record is therefore an **evolution event**, not merely a trial.

That event needs two orthogonal identities which the paper leaves implicit:

- **configured-system identity:** hashes/versions of model, prompt, memory, tools, topology, harness, feedback policy, and permissions before and after the event;
- **information exposure:** exactly which public instructions, runtime observations, demonstrations, private checks, reference artifacts, human guidance, and other agents' trajectories were available to the updater.

Without both, “retention” and “transfer” can be false friends. If later tasks resemble earlier private checks, apparent forward transfer may be answer memorization. If a tool or rubric changes at the same time as memory, improvement cannot be attributed to learning. If the benchmark itself evolves while the agent evolves, task difficulty and agent ability are jointly endogenous.

A second insight follows from the what/when/how taxonomy: these should be **multi-label causal coordinates**, not a folder hierarchy. One evolution event can update a prompt and tool documentation, occur between tasks, use external process feedback plus a population search, and target finance. Encoding it as one “method family” destroys the interactions that determine failure. `skill-bench` should represent changed components, trigger timing, data policy, optimizer, feedback channels, and domain independently.

A third insight is that persistence must be selective. Table 10 says long-horizon assessment assumes full persistence, which is useful for exposing real accumulation, but operational systems also require scoped deletion, rollback, user separation, and safety quarantine. A benchmark should test a declared persistence policy, not assume that retaining everything is desirable. Correct forgetting after revocation is a capability; indiscriminate retention is a privacy failure.

## Transferable design patterns

### 1. Evolution-event ledger

For every permitted update, record:

- event ID, parent and child configured-system hashes;
- changed loci: model, prompt, memory, tool/code, topology, evaluator, or environment;
- trigger: failure, success, uncertainty threshold, scheduled consolidation, human request, or autonomous exploration;
- timing: within-task, between-attempt, between-task, or between-stage;
- feedback channel, authority, visibility, and evidence locators;
- optimizer/update mechanism and random seed;
- stage and cumulative resource use;
- validation decision, approver, rollback pointer, and downstream dependencies.

This operationalizes `f(Π, τ, r)` and makes mixed-component updates auditable.

### 2. Separate four estimands

Report separately:

1. **initial competence** before any stream exposure;
2. **adaptation gain** on future held-out tasks;
3. **retention/regression** on scheduled old-task probes;
4. **policy compliance and cost drift** across the stream.

A single final average hides all four. Learning-curve area should not substitute for regression and safety checks.

### 3. Design the task stream as part of the benchmark

Version and publish (or securely commit to) task order, semantic clusters, stage boundaries, non-stationarity, OOD groups, reset points, and evolution budgets. Run multiple orders or deliberately adversarial orders. Keep private-check evidence out of agent-visible updates and track near-duplicate transfer separately from cluster-OOD transfer.

### 4. Use component-intervention ablations

Because “what evolves” is multi-dimensional, compare matched conditions such as no persistence, memory-only, skill/tool-only, and full evolution while pinning model, harness, tasks, and feedback. For mixed updates, preserve event-level attribution rather than claiming a monolithic self-improvement effect.

### 5. Treat forgetting and rollback as tested functions

Include revocation events, stale-policy changes, poisoned memories, contradictory expert guidance, and tool vulnerabilities. Test whether the system can identify affected state, stop its use, roll back, delete scoped data, and retain unrelated competencies.

## Limitations and validity threats

1. **No reproducible literature-search method.** The paper claims the first systematic and comprehensive review but reports no search strategy, screening flow, eligibility rules, coding protocol, or assessor agreement. Coverage and categorization cannot be independently audited from the manuscript.
2. **The operational definition is inconsistently applied.** Persistence is an inclusion criterion (p. 7), yet intra-task methods that reset weights or only modify the current context are included (Section 4.1). The “proto- to strong-evolution” relaxation preserves breadth at the cost of category validity.
3. **The taxonomy is not orthogonal.** Supervision source, optimization algorithm, population structure, update locus, and architecture recur across branches. A method can belong to multiple supposedly sibling categories, making counts and comparisons ambiguous.
4. **The objective omits constraints.** Equation 3 maximizes cumulative task utility, while safety, privacy, cost, and human control appear later as metrics. For deployment, these are constraints or co-objectives on each update, not optional post-hoc diagnostics.
5. **Evidence is mostly descriptive and secondary.** The survey does not conduct a meta-analysis, controlled re-evaluation, or quality-weighted synthesis. Performance numbers from heterogeneous papers are not comparable, as the authors acknowledge in Section 7.3.2.
6. **Proposed metrics are under-specified.** Cost-per-gain needs a cost normalization and baseline; “safety drift” needs probe scheduling and uncertainty; self-directedness is reduced to three disclosure fields rather than a validated scale; aggregate cost can conceal catastrophic tail events.
7. **FGT/BWT assumptions may fail in agent streams.** Re-running old interactive tasks can change environments or leak answers, and a later system may solve a task differently while still preserving the relevant skill. Retention probes need equivalent forms and artifact/process-level checks.
8. **Full persistence is not always desirable.** Table 10 does not foreground tenant isolation, data expiry, right-to-delete, benchmark secrecy, or selective rollback. The future-directions section discusses deletion and privacy, but the protocol does not integrate them as state-transition invariants.
9. **Safety recommendations are prescriptive rather than validated.** Table 12 is a sensible checklist, but the survey provides no evidence that the checklist is sufficient, no threat-model coverage analysis, and no evaluation of interactions among safeguards.
10. **Reproducibility conflicts with hidden reasoning.** The protocol asks for “full reasoning and action traces” (p. 45). Modern systems may not expose faithful chain-of-thought, and storing it can create privacy/security risk. Reproducibility should rely on observable actions, inputs, outputs, state deltas, and verifier evidence rather than assuming private reasoning is available or faithful.
11. **Benchmark co-evolution creates an unresolved identification problem.** The paper mentions evolving benchmarks, but does not provide a design that disentangles agent improvement from task-distribution change or benchmark-generator drift.
12. **Operational realism is surveyed, not demonstrated.** Hard budgets, changing policies, irreversible actions, concurrent users, incident response, and human approval are recommended but not instantiated in a benchmark or evaluated empirically.

## Reproducibility and operational realism

The immutable v4 PDF, full 77-page local extraction, formulas, tables, named methods, metric definitions, and companion repository make the conceptual synthesis inspectable. The formal tuple and Table 10 are concrete enough to guide schema work.

Reproducing the **review corpus and labels** is not possible from the paper alone. A replication would need the exact bibliography snapshot, search/export records, screened-out candidates, inclusion decisions, taxonomy codebook, per-paper extraction records, and adjudication history. The GitHub list may aid discovery, but a mutable catalog is not a versioned review protocol.

Operationally, the survey is stronger than most high-level agent surveys because it explicitly includes wall time, tool cost, memory growth, human intervention, checkpoints, rollback, privacy, and safety drift. Yet these remain requirements, not observed evidence. Its recommendation to persist all state and log full reasoning should be narrowed to **minimum sufficient, policy-compliant observability**: externally replayable actions, artifacts, state deltas, component versions, evidence locators, and decisions.

## Concrete changes for skill-bench

1. **Make longitudinal mode explicit in benchmark bundles.** Add a stream/stage specification with state-persistence policy, reset cadence, task-order seed, similarity/OOD clusters, stage and cumulative budgets, probe schedule, and allowed update loci.
2. **Represent each update as an evolution event.** Link before/after component hashes, trigger, feedback provenance, evidence exposure, changed components, costs, validation, and rollback. Reuse the existing typed component hashes and the planned provenance-gated lesson lifecycle rather than creating parallel provenance concepts.
3. **Add leakage-aware transfer metrics.** Distinguish same-instance retry, near-neighbor transfer, held-out cluster transfer, and true cross-domain transfer. Reject gains derived from private-check or reference-answer exposure.
4. **Add retention and selective-forgetting probes.** Use equivalent-form tasks where exact replay would leak answers; include revocation, contradiction, stale-rule, and poisoned-memory cases, plus unaffected-skill controls.
5. **Track cost and safety as trajectories.** Store stage-wise token/tool/time/memory/human costs, completion-under-policy, violations, leakage, and rollback events—not only cumulative totals.
6. **Require matched persistence ablations before claiming compounding improvement.** At minimum compare reset, memory/lesson-only, and full permitted evolution under identical task streams and feedback policies.
7. **Do not require hidden chain-of-thought.** Require replayable observable traces and typed state deltas; treat private reasoning as unavailable and potentially unfaithful.

## Action items for repository

- [x] Read and preserve the complete immutable arXiv v4 PDF and full 77-page local text.
- [x] Map the what/when/how/where taxonomy, evaluation goals, longitudinal protocols, safety controls, and validity threats to benchmark primitives with page evidence.
- [ ] Extend the benchmark bundle with a longitudinal stream/evolution-event protocol, multi-order retention probes, cost/safety drift, and leakage-aware transfer metrics.
- [ ] Instantiate that protocol only after the first static evidence-traceable pilot exposes which state transitions and probes are practical.
