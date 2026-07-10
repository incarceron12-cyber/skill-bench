# skill-bench Project Charter

> **Canonical master file.** This document defines what `skill-bench` is trying to achieve and is the final reference for resolving scope, priority, and drift. `README.md` explains the repository; `.hermes.md` governs autonomous work; detailed docs and schemas implement this charter.

## 1. Founding intent

Build an ambitious, compounding research and engineering program for creating highly useful benchmarks of **realistic knowledge work performed by AI agents**.

The project should investigate, rather than prematurely assume, how domain knowledge and tacit expertise can be transferred into benchmark tasks, source packs, artifacts, rubrics, graders, and diagnostic evaluation systems. It should combine broad exploration with repeated consolidation, progressively turning research into a coherent and executable benchmark program.

The project is deliberately **not scoped to one profession, workflow, artifact type, or use case**. Individual pilots may be narrow enough to build and validate, but they are experiments for learning general principles—not declarations that the benchmark is only about startups, consulting, finance, spreadsheets, or any other single vertical.

## 2. North star

> Create a credible, diagnostically rich benchmark program that reveals whether AI agents can perform consequential knowledge work requiring messy context, domain expertise, judgment, tool use, and professional artifact production—and explains why they succeed or fail.

The benchmark should ultimately help researchers, builders, organizations, and sponsors answer:

- What forms of knowledge work can current agent systems perform reliably?
- Which expert procedures, concepts, cues, and judgment rules can be transferred to agents?
- Which parts of domain expertise resist codification or remain difficult even when guidance is supplied?
- Are improvements caused by genuine capability transfer, better scaffolding, evaluator cues, or benchmark leakage?
- Where did a failure originate: task design, evidence retrieval, reasoning, state tracking, tool use, artifact construction, verification, judgment, grader, or environment?
- What should improve next in the agent system, the skill or guidance package, the benchmark instrument, or the surrounding workflow?

## 3. Core project objectives

### A. Understand the frontier

Continuously discover and deeply study:

- knowledge-work and long-horizon agent benchmarks;
- artifact, workflow, and trace evaluation;
- domain-expertise elicitation and transfer;
- production agent systems and evaluation practices;
- psychometrics, validity, calibration, leakage, and benchmark operation;
- human evaluation, expert judgment, and incentive design;
- adaptive, learning, and self-improving agent systems when relevant to the benchmark or research process.

Paper reviews must be based on actually acquired and read full text whenever called deep reviews. They should emphasize unique insight, methodology, evidence, limitations, reproducibility, and concrete relevance—not merely restate abstracts.

### B. Develop a general theory and methodology of expertise-to-evaluation

Investigate how expert knowledge becomes a benchmark without reducing expertise to a checklist. The methodology should cover:

- eliciting tacit cues, strategies, thresholds, and expert/novice contrasts;
- identifying hidden requirements and professionally legitimate traps;
- constructing realistic source packs with ambiguity and contradiction;
- specifying expected artifacts and consequential workflow states;
- separating public task requirements from private but fair consequences;
- building deterministic, model-based, and human grading layers;
- validating that tasks measure meaningful knowledge work rather than benchmark-specific compliance.

### C. Build substantial executable infrastructure

Convert research into working artifacts:

- data contracts and schemas;
- source and provenance systems;
- task-authoring packages;
- benchmark bundles;
- validators and tests;
- graders and rubric interfaces;
- trace and causal-diagnosis formats;
- trial, response-matrix, and calibration infrastructure;
- pilot tasks and evaluation suites;
- contributor and expert-participation workflows.

The repository should become more executable and empirically grounded over time, not merely accumulate prose.

### D. Explore broadly, then reconsolidate

The project intentionally alternates between two modes:

1. **Expansion:** search outside the current framing, collect diverse approaches, discover gaps, and generate alternative benchmark concepts.
2. **Consolidation:** compare evidence, merge duplicates, resolve contradictions, revise canonical documents, build artifacts, and prune ideas that do not serve the north star.

Expansion without consolidation creates noise. Consolidation without expansion creates premature lock-in. Both are permanent parts of the project.

### E. Develop Samuel's understanding and thinking

Updates should not only report activity. They should:

- explain important concepts clearly;
- distinguish evidence from project hypotheses;
- surface uncertainties and competing design choices;
- show how new work changes the benchmark thesis;
- pose useful strategic questions;
- help Samuel develop an increasingly sophisticated view of benchmark design, domain expertise, and agent evaluation.

### F. Make expert participation feasible under limited resources

Research and test creative ways to obtain useful expertise for free or near-zero cost, including:

- attribution and visible authorship;
- reciprocal tools and structured outputs experts can reuse;
- scoped micro-contributions;
- challenge or review formats;
- access to benchmark findings;
- sponsor-funded domain packs or bounties;
- community reputation and governance;
- public-good and professional-development incentives.

The project should remain open to sponsorship and partnerships without making them prerequisites for early progress.

## 4. What the benchmark is—and is not

### It is about

- realistic, multi-step knowledge work;
- domain-grounded judgment;
- messy and conflicting evidence;
- professional artifacts and inspectable states;
- configured agent systems, not isolated base models;
- multiple forms of validity and scoring;
- causal and operational diagnosis;
- expertise transfer as a central research axis;
- a portfolio or family of task domains when that improves construct coverage.

### It is not inherently about

- one specific professional use case;
- startup operating reviews or any other single pilot;
- computer-use skill alone;
- final-answer accuracy alone;
- a leaderboard without diagnostic value;
- producing paper summaries as an end in itself;
- improving Hermes for its own sake;
- maximizing commits, cron runs, source counts, or activity metrics.

A narrow pilot is justified only when it tests a general hypothesis, produces reusable benchmark machinery, or reveals what must differ across domains.

## 5. Role of the compounding/self-improvement system

The autonomous research system is **instrumental infrastructure**, not the project’s object of worship and not necessarily the benchmark’s subject.

Its purpose is to accelerate the charter by:

- discovering and reading useful sources;
- preserving evidence and provenance;
- challenging prior assumptions;
- expanding the design space;
- converting insights into benchmark artifacts;
- testing and validating those artifacts;
- consolidating knowledge into clear canonical documents;
- identifying decisions requiring Samuel.

A self-improvement change is valuable only if there is evidence that it improves one or more of:

- research quality;
- source coverage or depth;
- synthesis and conceptual clarity;
- benchmark validity or diagnostic power;
- executable benchmark infrastructure;
- pilot quality and diversity;
- expert contribution feasibility;
- Samuel's understanding and decision quality.

The system must not drift into generic agent-framework development, generic AI news collection, or self-modification disconnected from building the knowledge-work benchmark.

## 6. Benchmark design principles

The exact methodology should evolve with evidence, but the following principles currently anchor the work:

1. **Configured-system evaluation:** record model, scaffold, tools, memory, skills, environment, graders, and feedback policy independently.
2. **Evidence traceability:** preserve the chain from expert/source claim through task design and grading to trial outcome and diagnosis.
3. **Artifact-centered realism:** evaluate real work products such as spreadsheets, memos, decks, notebooks, tickets, models, and operational states.
4. **Plural measurement:** keep correctness, process, artifact quality, judgment, safety, efficiency, preference, readiness, and diagnosis separate until aggregation is validated.
5. **Public basis, private consequence:** hidden checks may test fair consequences of disclosed professional requirements but must not introduce surprise obligations.
6. **Intervention/instrument separation:** distinguish procedural guidance or skills from rubrics and graders so evaluator-cue compliance is not mistaken for expertise transfer.
7. **Root/surface separation:** distinguish where failure appeared from the earliest supported cause.
8. **Expert and empirical validation:** benchmark claims require more than internal coherence; they need expert review, calibration, trials, and evidence of construct validity.
9. **Cross-domain learning without forced uniformity:** seek reusable primitives while preserving legitimate differences among domains.
10. **Cost-aware usefulness:** measure quality relative to time, cost, infrastructure, and human-review burden.

These are working principles, not immutable dogma. Changes should be evidence-backed and recorded.

## 7. Current strategic program

The program should maintain a balanced portfolio rather than collapse onto one pilot:

1. **Frontier research:** benchmark literature, production systems, expertise elicitation, validity, and incentives.
2. **Canonical synthesis:** the benchmark-design taxonomy and state-of-the-art map.
3. **Executable contracts:** expertise-transfer and benchmark-bundle schemas, validators, fixtures, and tests.
4. **Diverse pilots:** bounded experiments across different knowledge-work structures to test generality and expose domain-specific differences.
5. **Evaluation infrastructure:** graders, traces, response matrices, calibration, reliability, and causal diagnosis.
6. **Expert/community model:** mechanisms for contribution, review, attribution, sponsorship, and governance.
7. **Learning system:** the 24/7 queue-driven expansion, building, consolidation, and briefing loop.

No single workstream should consume the project indefinitely. The queue and briefs should expose imbalance and redirect effort when necessary.

## 8. Success criteria

The project is making substantive progress when it produces evidence such as:

- comprehensive primary-source reviews that materially change design choices;
- a coherent, cited, and evolving theory of knowledge-work benchmark design;
- multiple validated task-authoring packages from meaningfully different domains;
- executable benchmark bundles with provenance, graders, traces, and diagnostic output;
- empirical agent trials, ablations, expert review, and calibration results;
- demonstrated separation of genuine skill transfer from rubric or scaffold effects;
- reusable tooling that lowers the cost of adding new domains;
- credible mechanisms for expert participation;
- clear decision-relevant reports for benchmark users;
- documented process improvements tied to better research or benchmark outcomes.

The project is drifting when it produces mostly:

- uncited summaries or abstract paraphrases;
- disconnected framework code with no benchmark use;
- repeated taxonomy rewrites without tests or pilots;
- many narrow tasks with no general learning;
- one domain treated as the permanent benchmark without an explicit decision;
- self-improvement activity measured only by frequency or commits;
- outputs that do not improve Samuel's understanding or the benchmark's usefulness.

## 9. Decision filter for every task

Before adding or claiming work, answer:

1. Which charter objective does this advance?
2. What concrete evidence or artifact will it produce?
3. What decision, capability, or benchmark-design uncertainty will it clarify?
4. Is this expansion, consolidation, building, validation, or human learning—and is that mode currently under- or over-supplied?
5. Does similar work already exist?
6. Could this narrow the project accidentally? If it is a pilot, what general hypothesis does it test?
7. How will we know whether the work was useful?

If these questions do not yield a credible answer, do not prioritize the task.

## 10. Canonical document hierarchy

When documents disagree, use this order:

1. **`PROJECT_CHARTER.md`** — mission, scope, objectives, and anti-drift boundaries.
2. **`.hermes.md`** — autonomous operating rules for implementing the charter.
3. **`docs/research-agenda.md`** — active research questions and hypotheses.
4. **`docs/benchmark-design-taxonomy.md`** — current canonical technical design model.
5. **`schemas/` and tests** — executable contracts and currently enforced invariants.
6. **`docs/state-of-the-art-map.md` and paper reviews** — evidence base and external landscape.
7. **Reports, inboxes, and queue** — transient or operational state.

Lower-level artifacts may reveal that a higher-level document needs revision, but they do not silently override it.

## 11. How this charter evolves

This is a living master document with two kinds of content:

- **Founding intent and scope boundaries** (§§1–5): change only when Samuel explicitly changes the project’s goals.
- **Working principles, strategic program, and success criteria** (§§6–8): may be proposed for revision when accumulated evidence or implementation experience makes them incomplete or wrong.

For any proposed revision:

1. cite the evidence or project change motivating it;
2. state whether it clarifies, expands, or changes the mission;
3. check for accidental narrowing or metric substitution;
4. record the change in Git history and, when it concerns the autonomous system, the self-improvement ledger;
5. surface material scope changes to Samuel before implementation.

The consolidator should periodically check whether the charter still matches the repository. It may update stale links, status descriptions, or working principles autonomously, but it must not rewrite the founding intent or narrow the benchmark to a single use case without Samuel's explicit approval.
