# EvalAgent: evaluation skills improve first-run artifact generation, not evaluator validity

**Source type:** Deep review of the complete immutable arXiv v2 primary source, including all appendices, plus the pinned official repository release.  
**Source:** Zhou et al., *An Empirical Study of Automating Agent Evaluation*, arXiv:2605.11378v2 (11 June 2026), 42 pages.  
**Local PDF:** `data/papers/pdfs/2605.11378v2-an-empirical-study-of-automating-agent-evaluation.pdf` (SHA-256 `86a73716dbe8b2ac9192b65a8f76d279f6a3cfd5df05d1aba736b8ca6f1fd7e5`). **Local text:** complete extraction `data/papers/text/2605.11378v2-an-empirical-study-of-automating-agent-evaluation.txt` (SHA-256 `24ec21f7cabefd653dc05f86e1aaa6904fccf72cabd4f5c476d040fa151f516b`).  
**Official release inspected:** `https://github.com/awslabs/Agent-EvalKit`, pinned official commit `472fbc6501ba3f7a36e88140de63d1f6574f5efa` (10 March 2026), archived at `data/sources/releases/2605.11378v2-agent-evalkit/awslabs-Agent-EvalKit-472fbc6.zip`; provenance and scope audit at `data/sources/releases/2605.11378v2-agent-evalkit/provenance.json`. The commit predates both paper versions but is not proven to be the exact experimental snapshot.

## Bottom line

EvalAgent tests a useful and narrower hypothesis than its language sometimes suggests: **evaluation-specific procedures, templates, code recipes, and current API documentation can make a coding agent produce smaller and more frequently executable evaluation programs.** In a 20-agent, two-requirement benchmark, the package raises first-run execution-plus-non-vacuity (`Eval@1`) from 30% for the matched plan-then-code baseline to 65% with Sonnet 4.5, while an agentic comparative judge and three engineers strongly prefer its artifacts (paper pp. 8–12, 31–32).

That is evidence for **evaluation-engineering scaffolding**, not evidence that the generated metrics measure the intended construct. `Eval@1` checks execution and manually classified obvious vacuity, while the preference rubric rewards relevance, concision, code quality, and plan consistency. Neither test establishes criterion truth, sensitivity/specificity against planted agent failures, score agreement with an independently authored evaluator, calibration, or decision validity. The system often replaces brittle keyword checks with LLM judges, but semantic-looking judge code is not automatically a valid measurement instrument.

For skill-bench, the unique transferable result is therefore a separation: **generation acceptance must have an executable-conformance gate and an independent measurement-validity gate.** Existing benchmark-bundle, task-health, metric, validity-argument, and observer-evidence contracts already provide the homes; no new schema is warranted.

## One-sentence contribution

Evaluation-specific procedures, templates, trace/code recipes, and current API documentation improve first-run evaluator engineering, but the experiment does not establish that the resulting metrics are valid measures.

## Research question

The paper asks whether frontier coding assistants can automate the end-to-end construction of agent evaluation: deciding what to measure, instrumenting an agent, collecting traces, implementing metrics, and reporting findings. It contributes:

1. **EvalAgent**, a six-stage workflow guided by progressively disclosed “evaluation skills”: procedural instructions, templates/code patterns, and dynamically retrieved API documentation (pp. 3–4; Appendix A, pp. 20–21).
2. **AgentEvalBench**, 20 agents across nine frameworks and fourteen stated domains, each with five scenarios and generic/specific evaluation requests (pp. 6–7; Appendix B).
3. **A comparative meta-evaluator**, using a coding agent to inspect multi-file plans, code, and traces along five weighted dimensions (pp. 5–6; Appendix C).
4. **Eval@1**, a first-run acceptance outcome requiring generated evaluation code to execute and avoid three obvious invalid patterns: constant/all-zero output, mock/hardcoded rather than real artifacts, and predictions reused as gold (p. 6).

The paper is strongest when it treats evaluator construction as artifact production rather than a single judge prompt. It is weakest when it calls comparative artifact preference “comparative validity” (p. 4): preference among two generated implementations does not supply an external validity criterion.

## System and encoded knowledge

The pipeline is plan → test cases → instrumentation → trace collection/processing → evaluation code → report (Figure 1, p. 3; Appendix A). Skills constrain plans to roughly 1–3 essential metrics, prescribe minimal implementations, provide OTEL extraction and DeepEval patterns, and require Context7 lookup before using mutable APIs (pp. 3–4, 28–30). Generated code combines deterministic trace checks and LLM-based assessments.

This package encodes several genuine evaluator-engineering practices:

- inspect actual behavior before defining metrics;
- make each metric distinct and tied to a stated objective;
- keep the artifact graph small;
- inspect the actual trace schema before writing extraction logic;
- reuse one trace-processing layer rather than duplicating parsing per metric;
- execute the evaluator on real traces and reject vacuous outputs;
- bind implementation to the plan and produce evidence-bearing reports.

But the package contains little **application-domain expertise**. Under a generic request, the coding agent infers criteria from target code and five observed scenarios. The skill says how to build an evaluation, not what medically correct entity extraction, safe network operation, or professionally sound financial analysis means. This distinction matters: the intervention transfers evaluation workflow knowledge while leaving construct definition largely to the model and observed sample.

The paper also bundles three different treatments—procedural rules, static recipes/templates, and live documentation. The B4 comparison removes all three together; only Context7 receives a separate ablation. It does not identify whether procedural reasoning, copied implementation patterns, format regularization, or current dependency syntax drives the remaining gain.

## Methodology and system

### Benchmark and treatment design

The benchmark has 20 target agents, each crossed with generic and specific requirements, producing 40 cases per evaluator backbone. Complexity tiers are based on LOC, tools, trace length, memory, and multi-agent status, but the paper does not report a sampling frame, inclusion process, licensing, representativeness target, or independently validated domain requirements (pp. 6–7). Five scenarios per agent are authored, but scenario-generation and approval evidence are not described beyond examples.

The main design crosses Haiku 4.5/Sonnet 4.5 evaluator backbones with five methods (p. 8): single-turn code generation; agent over source only; one-stage agent over source and traces; two-stage plan/code agent; and EvalAgent. Agentic methods share Claude Code v2.1.92, file/shell/web tools, and a 50-tool-call ceiling. All consume pre-collected traces for the plan/code comparison, reducing target-agent run variance.

This is not a clean single-factor skill trial. B1 differs in agency and context delivery; B2 lacks traces; B3 removes planning; B4 is the closest comparison but lacks templates, recipes, constraints, and dynamic docs simultaneously. EvalAgent also integrates DeepEval and Context7 in a more prescribed way. Consequently, “skills matter” is supported at package level, not for a general class of evaluation knowledge.

## Evidence and results

### Outcomes

Against B4 with Sonnet, EvalAgent has 90% overall win-or-tie under the Opus meta-evaluator and improves `Eval@1` from 30% (12/40) to 65% (26/40) (Table 5, pp. 8–9). It uses fewer tokens and less generation time than B4, though paper time excludes network/API delay; total cost is about $4.03 per EvalAgent case across plan and code stages for Sonnet’s generic/specific means (Appendix F, pp. 32–33). The study does not report confidence intervals or paired significance tests for the 40-case success differences, despite repeated measurements on the same agents.

The metric-count intervention is informative but limited: at requested counts 1/3/5, EvalAgent’s Sonnet `Eval@1` is 60/55/65%, versus B3’s 55/50/30% and B4’s 50/55/40% (Table 9, p. 11). This suggests recipe reuse avoids compounded parser/API failures. It does not show that five metrics are more informative than one, and the prompt-imposed count may generate unnecessary criteria.

Context7 has the largest reported ablation: Sonnet `Eval@1` rises from 20% without it to 65% with it (Table 10, p. 11). This is compelling evidence that dependency/API state is part of configured evaluator identity. It is not evidence that dynamic retrieval improves metric validity; it mainly repairs model identifiers and class signatures. Even with current docs, 11/14 Sonnet failures remain framework-related (p. 13).

### Human and model meta-evaluation

Three engineers with at least three years’ ML/AI experience, no prior project involvement, two hours of training, five practice cases, and calibration independently compare EvalAgent to B4 on all 40 cases. They see source, traces, plans, and code, spend a reported mean 68 minutes per case, and prefer EvalAgent in 79.5% of judgments with 10.5% ties; overall Fleiss’ κ is 0.923 (pp. 7, 31–32).

This is unusually explicit annotation reporting, but the unit behind “79.5%” is ambiguous in prose: the study has 120 case-level annotator decisions and 600 dimension-level annotator judgments, while Table 3 presents percentages without raw human counts. Majority-vote overall disagreement occurs in 8/40 cases (20%) even though aggregate κ is high. Annotators compare only EvalAgent against B4—the pair whose obvious code-size and dead-code differences align strongly with the rubric—so validation does not cover all baseline pairings or absolute quality.

The Opus meta-evaluator matches the human majority’s weighted overall winner in 39/40 cases, yet only 150/200 dimensions (75%); Plan Quality is 50% and Plan-Code Alignment 60% (Table 20, p. 32). The 97.5% headline is therefore dominated by weighted aggregation and a strong treatment difference, not uniformly reliable criterion judgments. Three Opus runs have only 76.3% unanimous outcome agreement and 84.2% mean pairwise agreement (pp. 34–35). The claimed random baseline of 33.3% for three-way agreement is incorrect under three equiprobable independent labels: all-three agreement is 1/9. More importantly, label prevalence—not a uniform baseline—is the relevant comparator.

## Reproducibility and operational realism

The official repository was inspected at commit `472fbc6`; it contains 47 tracked files: slash-command procedures, plan/report templates, OTEL processing, DeepEval reference patterns, and one QA example. Python syntax compilation passes for the example and trace scripts. The release is useful for inspecting the intervention:

- `commands/plan.md` encodes source/trace inspection, user-priority rules, minimal metrics, real-agent focus, and a flat artifact structure.
- `commands/eval.md` requires loading processed traces, implementing extraction and metrics, running the evaluator, and consulting Context7.
- the QA `metrics.py` demonstrates a DeepEval/LiteLLM wrapper and trace extraction.

However, the inspected example is not a clean executable witness: `create_test_case_from_trace` prints extracted values and calls `exit()` before constructing a test case (`examples/qa_agent_evaluation/eval/metrics.py`, lines 102–127). Syntax-valid release code is therefore not evidence of end-to-end behavior. The repository has no visible benchmark corpus, experimental baseline outputs, human annotations, meta-evaluator outputs, `Eval@1` labels, or paper result tables; searches for `AgentEvalBench`, `Eval@1`, `Fleiss`, and representative benchmark agent names return no files. The empirical claims cannot be independently replayed from this snapshot. There is also no pinned lockfile or immutable Context7 response corpus, so the intervention’s dynamic API knowledge is intrinsically time-dependent.

The repository’s README appropriately says the generated pipeline should be reviewed and customized (lines 132–140), a materially narrower operational claim than the paper’s framing of complete automated evaluation.

## Limitations and validity threats

1. **Conformance is mistaken for measurement quality.** `Eval@1` rejects grossly empty/mock/self-referential evaluations, but a runnable LLM judge with plausible criteria can still be systematically wrong. No planted-error suite measures sensitivity, specificity, invariance, or calibration.
2. **The criterion is co-designed with the treatment.** The meta-rubric explicitly rewards fewer metrics, shorter code, plan adherence, and LLM-judge use—the package’s intended outputs. Those are maintainability properties, not independent evidence that scores track agent quality.
3. **No reference evaluator or outcome intervention.** Generated metrics are not compared with expert-authored criteria on target trajectories, nor tested on controlled pairs where a known defect changes and irrelevant properties remain fixed.
4. **Domain authority is absent.** Three ML engineers validate evaluation artifacts, not the domain truth of criteria across medicine, finance, networking, travel, and fourteen claimed domains.
5. **Weak scenario evidence.** Five scenarios per agent are too few to support coverage, and the paper provides no independent scenario authoring/adjudication or held-out test of metric generalization.
6. **Package-level confounding.** Procedures, templates, code snippets, dynamic docs, and likely formatting/length constraints move together. The B4 contrast cannot attribute gains to “domain expertise” rather than recipes or dependency repair.
7. **Outcome-conditioned diagnostics.** Failure categories are reported for EvalAgent failures only and manually interpreted; coding a single async fix to estimate 87.5% `Eval@1` is a post-hoc counterfactual, not a rerun.
8. **Dependence and uncertainty are ignored.** Cases share target agents, traces, model, framework, libraries, and generated-code patterns. Reported proportions lack paired/clustered intervals, and “three independent runs” apply to the judge, not evaluator generation.
9. **Dynamic resources impede replay.** Context7 content, web search, library versions, model endpoints, and service behavior are not preserved per trial.
10. **Configured-system scope is narrow.** Both generator backbones and both meta-judges are Claude-family models; observed performance does not establish cross-provider or cross-harness transfer.
11. **Reporting overreaches traces.** The report template asks for root causes, file-line locators, expected gains, and status labels. A trace association does not establish causal root cause or expected improvement without intervention evidence.
12. **Release incompleteness.** The official snapshot exposes intervention ingredients but not the benchmark and result evidence required to reproduce the paper.

## Unique insight relative to adjacent work

LH-Bench and SkillsBench test whether procedural skills improve task performance. ResearchRubrics studies expert construction of detailed criteria. AgentRewardBench calibrates judges against trajectory labels. Anthropic’s production guidance separates task and grader health. Anchor compiles one specification into task/environment/oracle/check projections.

EvalAgent adds a different object: **the evaluator-construction workspace itself**—plan, trace adapter, metric code, dependency state, execution result, and report—generated as a linked artifact graph. Its strongest finding is that this graph has two independent failure axes:

- **engineering validity:** does the adapter observe the intended trace fields, does code execute in the pinned environment, and are outputs non-vacuous?
- **measurement validity:** do criteria and scores respond to the intended agent behavior rather than superficial correlates, judge preference, or extraction accidents?

The paper improves the first axis and mostly evaluates the first plus maintainability. It leaves the second axis open. This distinction prevents skill-bench from treating “generated grader passes tests” as “grader is fit to support a capability claim.”

## Relevance

This work directly tests whether evaluator-construction expertise can be packaged for an agent, but its evidence requires skill-bench to keep artifact-generation success separate from measurement claims.

## Transfer to skill-bench

### Retain

- Treat evaluation generation as a staged, inspectable artifact graph with immutable links among requirement, observed traces, plan, criterion, adapter, grader code, environment, outputs, and report.
- Keep trace parsing shared and separately tested; distinguish missing observation from substantive agent failure.
- Pin evaluator dependencies and dynamic documentation snapshots as configured-system components.
- Require first-run execution and explicit rejection of constant, mock, hardcoded, prediction-as-gold, missing-view, and empty-extraction outputs.
- Measure implementation burden (generation time, human debugging time, token/API cost, files/LOC, and maintenance) separately from metric quality.
- Preserve plan-code alignment as a diagnostic, not as proof of validity.

### Repair

A generated evaluator should progress through a claim ladder:

1. **syntax/import conformance**;
2. **execution in a pinned environment**;
3. **observation conformance** on planted trace fields, missingness, and alternate valid representations;
4. **non-vacuity/discrimination** on positive/negative and metamorphic cases;
5. **criterion equivalence** against an independently authored evaluator or expert adjudication;
6. **reliability/calibration** across judge versions, repeats, task clusters, and relevant slices;
7. **bounded validity argument** for the specific score interpretation and use.

Passing a lower rung must not imply a higher one. Existing artifact-view admissibility and observer-evidence checks cover observation; task-health can hold contrast sets and defects; metric-monitoring specifies estimands and dependence; validity arguments bound claims. The missing work is empirical use of those contracts on generated evaluators, not another schema.

### Falsifiable benchmark experiment

On at least two structurally different knowledge-work pilots, have an expert or source-grounded author define criteria and plant paired trajectory/artifact mutations: intended failure, irrelevant formatting change, missing evidence view, alternative valid path, and adversarial superficial cue. Generate evaluators under no-guidance, procedure-only, recipe-only, dynamic-doc-only, and full-package conditions with model/harness held constant. Score separately:

- first-run environment conformance;
- trace-field extraction precision/recall;
- planted-defect sensitivity and invariance specificity;
- agreement with independent criteria/adjudication;
- debugging and review time/cost;
- cross-task reuse on held-out agents without co-designed criteria.

This would identify whether skills transfer evaluator judgment, merely stabilize implementation, or overfit the benchmark’s own acceptance style.

## Concrete changes

1. **Do not add a schema task.** Map generated evaluators into the existing benchmark-bundle component hashes, observer/admissibility evidence, task-health contrast sets, metric specifications, and validity arguments.
2. **When the next grader slice is built, add a generated-evaluator treatment arm** only if it includes independently authored planted failures and held-out task reuse. The useful outcome is a conformance-versus-validity matrix, not another successful code-generation demo.
3. **Require dynamic-resource provenance** in any evaluator-generation trial: exact documentation queries/responses, retrieval time, library lock, model/provider/harness, trace schema, and generated artifact hashes.
4. **Keep report claims typed.** “Observed association,” “suspected cause,” “confirmed by intervention,” and “expected gain” must not collapse into one root-cause recommendation.

## Claim boundary

The study supports: in this 20-agent, Claude-family, pre-collected-trace setup, the full EvalAgent package produces more concise, more preferred, and more frequently first-run executable/non-obviously-vacuous evaluator artifacts than the tested prompts, especially the matched unstructured plan/code baseline.

It does **not** establish: accurate domain evaluation, equivalence to expert-authored graders, calibrated metrics, causal root-cause reports, cross-domain evaluator transfer, production readiness, or general automation of benchmark validity.
