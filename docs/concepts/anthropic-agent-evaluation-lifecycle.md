# Agent evaluation as a maintained evidence system

## Source and review status

- **Primary source:** Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, and Jiri De Jonghe, “Demystifying evals for AI agents,” Anthropic Engineering, published 2026-01-09: <https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>
- **Full local source:** `data/sources/anthropic-demystifying-evals-for-ai-agents.md`
- **Provenance:** `data/sources/anthropic-demystifying-evals-for-ai-agents.provenance.json`
- **Local extraction SHA-256:** `4587dc2e359fa9fa84ddef6d7508f634ef1805e90dc1fe3eff635b11cf04c2e7`
- **Read and verified:** 2026-07-10. The complete 441-line official article extraction was read. A fresh fetch of the canonical page contained the title and the article's reference-solution, trial-isolation, and `pass^k` claims. Its raw HTML had the same recorded byte count but a different hash from the retained provenance hash, so the local extraction—not the mutable live page—is the reviewed evidence object.
- **Evidence type:** official production-method post, not a controlled study or benchmark paper.

## Charter fit and useful completion

This note advances charter objectives A–C: understand production evaluation practice, convert it into reusable benchmark-design knowledge, and identify missing executable contracts. It is **consolidation** of a production source into a lifecycle model, not a proposal to narrow `skill-bench` to Anthropic products or any one agent family. The uncertainty it clarifies is whether the current task/trial/grader/trace schema is enough to operate a trustworthy benchmark over time. Useful completion means identifying source-supported lifecycle controls that the current static bundle cannot represent, while refusing claims the source does not evidence.

## Contribution and research question

The post's explicit question is practical: how should product teams construct, run, debug, and maintain automated evaluations for multi-turn agents? Its contribution is a production vocabulary and an eight-step operating roadmap spanning task collection, task specification, grader design, environment isolation, transcript inspection, saturation monitoring, and ownership (source lines 25–44, 257–327).

For `skill-bench`, the important contribution is not the already-familiar task/trial/grader/trace decomposition. It is the less explicit proposition that an evaluation is a **maintained evidence system**. A task begins as a requirement or observed failure, is made executable and solvable, accumulates repeated trial and adjudication evidence, may change function from capability probe to regression guard, and must eventually be revised, retired, or replaced as agents and usage distributions change. The current benchmark bundle captures an instrument and its trials, but not this task-level evidence history.

## Methodology and system described

The article synthesizes lessons from Anthropic's internal evaluations, customer collaborations, and named product examples. It does not report a sampling frame, study protocol, comparison group, or underlying datasets. Its system model has these parts:

1. **Executable units.** A task has inputs and success criteria; a trial is one stochastic attempt; graders contain assertions/checks; the transcript records the interaction; the outcome is final environment state; evaluation and agent harnesses are separate; a suite groups tasks around a capability (lines 35–44).
2. **Plural grading.** Code-, model-, and human-based graders inspect either outcomes or transcripts. Deterministic checks are preferred where possible; model judges cover open-ended dimensions but require human calibration; humans remain the reference for expert judgment (lines 70–131, 287–299).
3. **Domain-specific observability.** Coding emphasizes tests and state; conversational agents combine interaction quality, end state, and simulated users; research agents combine groundedness, coverage, authority, and synthesis; computer-use agents require sandboxed execution and backend/artifact state (lines 141–241).
4. **Repeated trials.** `pass@k` represents whether at least one of multiple attempts succeeds, while `pass^k` represents consistent success across all attempts; the metric should follow the operational requirement (lines 243–255).
5. **Task authoring and health.** Start with 20–50 requirements or real failures; require expert-agreeable verdicts, an agent-passable specification, a passing reference solution, and positive/negative cases for trigger behavior (lines 261–279).
6. **Execution integrity.** Reset each trial to a clean environment and avoid shared state or shared resource constraints that make failures correlated or leak prior work (lines 281–285).
7. **Adjudication and maintenance.** Inspect transcripts to distinguish agent failures from task, grader, or harness defects; monitor saturation; keep explicit ownership; combine offline evals with production monitoring, A/B tests, user feedback, and human studies (lines 301–415).

## Evidence actually offered

The evidence is experience-based and heterogeneous:

- Claude Code reportedly progressed from dogfooding to narrow and then broader behavior evals; Descript reportedly moved from manual grading to calibrated LLM grading and split quality from regression suites; Bolt reportedly built static-analysis, browser-agent, and LLM-judge evaluation within three months (lines 50–64).
- The post cites concrete benchmark incidents where grader/task/harness defects allegedly changed results materially: CORE-Bench from 42% to 95% after corrections and a less constrained scaffold, and METR tasks whose stated threshold did not match the graded threshold (lines 295–297).
- Anthropic reports an internal leakage mode where an agent inspected git history left by prior trials, illustrating why state reset is part of validity rather than mere infrastructure hygiene (lines 283–285).
- Product examples support multidimensional grading patterns, but the YAML fragments are explicitly theoretical illustrations rather than released task artifacts or validation results (lines 149–183, 191–225).

These examples are useful failure reports, not effect estimates. The source gives no task-level data, grader-human agreement values, confidence intervals, cost curves, false-positive rates, or before/after product outcomes. Named customer practice is not independently auditable from this article.

## Unique insight: a task's role is an evidence-backed state, not permanent metadata

The post distinguishes capability suites, which should initially have headroom, from regression suites, which should be near-perfect, and says successful capability tasks can “graduate” into regression tests (lines 133–139). Combined with failure-derived task creation, reference-solution validation, transcript adjudication, and saturation monitoring, this implies a lifecycle:

```text
observed requirement/failure
  -> candidate task
  -> specification/reference validation
  -> active capability probe
  -> adjudicated and calibrated task
  -> regression guard, retained diagnostic, revised task, or retirement
```

A task does not become a regression guard merely because agents score highly. Graduation is a change in **intended use and evidentiary burden**: the task must be stable enough that a new failure is more likely a regression than task noise, yet still relevant enough that preserving it matters. Conversely, a saturated capability item may retain value as a regression or critical diagnostic even when it contributes no frontier discrimination.

This sharpens the repository's existing task-bank/panel split. “Capability,” “regression,” “critical diagnostic,” and “calibration-only” should be typed operational roles attached to an instrument version, with evidence and transition records. They should not be inferred from current pass rate or collapsed into one suite label.

## Important tensions with current benchmark principles

### 1. Clear grading basis does not require exact private-check disclosure

The article says everything a grader checks should be clear from the task description (lines 271–275). Taken literally, that would eliminate held-out consequences and invite criterion gaming. The defensible transfer is narrower: every check needs a disclosed **public basis**, while exact test cases, weights, perturbations, or implementation may remain private. This agrees with the charter's public-basis/private-consequence invariant. The Terminal-Bench filepath example is an undisclosed obligation, not a legitimate hidden consequence.

### 2. Outcome-first grading does not make all process evidence illegitimate

The article warns that exact tool-call sequence checks punish valid creative solutions and recommends grading products rather than paths (lines 287–293). That is sound for incidental implementation choices. It does not justify discarding process checks where ordering is itself consequential—authorization before action, source verification before causal claims, or reconciliation before recommendation. `skill-bench` should distinguish:

- **incidental path conformance**, which should not be graded;
- **expert-grounded workflow invariants**, which may be graded when linked to outcomes or safety; and
- **trace evidence used only for diagnosis**, which should not alter task success.

### 3. Reference solutions are smoke tests, not validity proofs

A known output that passes all graders establishes at least one executable route and can expose configuration errors (lines 271–275). It does not establish that the prompt is unambiguous, graders accept plural valid procedures, the task represents real work, or an agent had a fair opportunity. Reference validation therefore needs a typed claim such as `witness_pass`, not a generic `validated=true`.

### 4. Repeated-trial metrics need an independence audit

The article correctly notes stochastic outcomes, but its illustrative `pass^k = p^k` extrapolation assumes exchangeable independent trials with stable success probability (lines 243–255). The same article documents shared-state and resource failures that violate this assumption (lines 283–285). A benchmark should report empirical all-success/any-success rates over declared replicate groups, record seeds and environment identities, and avoid extrapolating to larger `k` unless dependence and stationarity are defensible.

### 5. Expert agreement is necessary but not sufficient

“Two experts independently reach the same verdict” is a useful authoring test (lines 271–273), but no agreement statistic, expert qualification rule, reconciliation protocol, or validity criterion is supplied. Experts can agree on a construct-irrelevant task. Agreement must remain separate from content, construct, ecological, and consequential validity.

## Limitations and threats to transfer

1. **No systematic evidence method.** The authors do not state how organizations, incidents, or successful practices were sampled. Negative or failed implementations may be missing.
2. **No quantitative support for key thresholds.** The 20–50-task starting point and claim that large early effects make small samples sufficient are heuristics without power analysis, variance estimates, or conditions of validity (lines 261–265).
3. **Mutable and partly secondary evidence.** Several dramatic examples link to social posts or changing benchmark pages rather than immutable incident reports. The official article itself has an upstream update timestamp and a mutable canonical page.
4. **Calibration is under-specified.** “Closely calibrated” LLM judges are recommended, but the post gives no sampling plan, target agreement, subgroup analysis, drift trigger, uncertainty representation, or adjudication protocol (lines 293–295).
5. **Product success and benchmark validity are conflated at points.** Fast iteration and fewer regressions may justify internal tests without establishing that scores support broad capability or professional-readiness claims.
6. **Outcome loopholes remain unresolved.** The flight-policy example shows a creative solution that is better for a user but fails the written eval (lines 31–33). The post recommends transcript reading, but provides no durable adjudication or task-amendment contract that preserves comparability after correcting the evaluator.
7. **Security advice is non-operational.** “Resistant to bypasses or hacks” is a goal, not a threat model, attack protocol, or evidence standard (line 299).
8. **Human evidence is costly but not costed.** Human studies and SME calibration are recommended without reporting hours, rates, reviewer burden, or scalable sampling rules.
9. **Reasoning capture is treated too casually.** The transcript definition includes “reasoning” (line 40), but configured systems may not expose faithful hidden reasoning. Observable messages, actions, tool results, state, artifacts, and declared reasoning summaries should be recorded without claiming latent-thought fidelity.

## Reproducibility and operational realism

The post is operationally realistic where it treats stateful environments, harness constraints, correlated infrastructure failure, grader defects, evolving requirements, and transcript adjudication as normal rather than exceptional. It also explicitly evaluates a model plus scaffold, aligning with configured-system evaluation.

It is not reproducible as a research result: no evaluation suites, complete grader prompts, trial matrices, incident logs, or human labels accompany the article. The theoretical YAML is too incomplete to execute. Thus the post should guide contract design and failure hypotheses, not serve as empirical validation for a `skill-bench` scoring policy.

## Concrete transfer to `skill-bench`

### Preserve existing contracts

The current `benchmark-bundle.schema.json` already captures task/trial/grader/check/trace separation, configured component versions, artifact outcomes, environment-error status, and separate deterministic/model/human grader types. Do not rebuild these.

### Add a task-health and lifecycle layer, after the current pilot execution gate

A separate operating-layer record should reference immutable task and grader hashes rather than expanding every static bundle. Minimum fields:

- `task_version_ref` and `suite_version_ref`;
- `operational_roles[]`: `capability_probe`, `regression_guard`, `critical_diagnostic`, `calibration_only`;
- `origin`: requirement, manual check, production failure, user report, expert incident, or synthetic hypothesis, with provenance and privacy/redaction state;
- `reference_attempts[]`: configured system or human, artifact/trace locator, grader versions, result, and narrow validation claim;
- `contrast_set`: positive/negative paired cases and the trigger or boundary they test;
- `replication_policy`: intended `k`, replicate grouping, seed policy, environment reset/fingerprint, and independence threats;
- `adjudications[]`: original result, validity owner, transcript/evidence locators, accepted alternative or defect type, decision, and affected versions;
- `health_evidence`: pass-rate distribution, invalid-run rate, grader-human disagreement, saturation, production/usage relevance, last reviewed date, and owner;
- `transitions[]`: from/to role or state, rationale, evidence, approver, effective benchmark version, and compatibility/bridge requirement;
- `retirement_or_revision`: reason, replacement, preserved critical coverage, and comparability decision.

### Add semantic invariants

1. A task cannot become a regression guard solely from a high aggregate score; it needs stable repeated-trial evidence, low unresolved invalidity, and an owner-defined consequence of regression.
2. A reference witness can prove executability only for its exact task/grader/environment versions.
3. Any adjudication that changes task, grader, harness, or environment hashes creates a new instrument version; old scores are retained, not rewritten.
4. An `environment_error` or task/grader defect is excluded from capability aggregation by an explicit policy and remains countable in operational reliability.
5. Private checks retain a public-basis link even when exact assertions are hidden.
6. Capability saturation may trigger role transition or revision but must not automatically delete rare safety, compliance, or expert-trap coverage.
7. `pass@k`/all-success reporting names the replicate group and independence assumptions; it does not silently calculate `p^k` from pooled `pass@1`.

## Concrete next actions

1. **Build one non-duplicate operating artifact:** after the static pilot grader continuation, implement the task-health/lifecycle record above with fixtures for (a) a valid capability-to-regression transition, (b) a forbidden transition based only on saturation, and (c) grader-defect adjudication that versions rather than rewrites the instrument.
2. **Use the current LH adoption pilot as the first fixture:** its planted cases can prove witness/reference mechanics and invalid-trial handling without pretending internal fixtures establish expert or production validity.
3. **Do not add a generic “more graders” task:** plural graders, check results, component hashes, and failure ownership already exist. The missing object is longitudinal evidence about the *instrument's operational role and health*.
4. **Future empirical validation:** once real trials exist, compare empirical replicate-group any/all-success rates with independence-based estimates, and sample transcript adjudications to estimate agent-vs-instrument failure proportions. Until then, these remain proposed tests rather than source-established facts.

## Bottom line

Anthropic's post is strongest as an operational failure catalogue and lifecycle argument, not as validation evidence. Its distinctive transfer is that benchmark tasks must carry an auditable history of origin, executability, replication, adjudication, role transitions, saturation, and ownership. `skill-bench` already models what happened in one configured trial; it should next model why a task is still fit for a particular evaluative use—and version that judgment when the evidence changes.
