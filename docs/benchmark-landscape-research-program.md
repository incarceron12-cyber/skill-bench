# Benchmark Landscape Research Program

## Purpose

Study how benchmark design has evolved from widely used standardized evaluations to newer, more realistic, inspectable, and validity-aware agent benchmarks. The objective is not to collect names. It is to identify:

1. **strengths to preserve** in `skill-bench`;
2. **limitations and failure modes to improve**;
3. **new design responses** and whether they actually solve the older problem;
4. **claims that each benchmark can and cannot support**;
5. **reusable machinery** for broad knowledge-work evaluation.

This program advances charter objectives A, B, and D. It remains cross-domain and does not make any benchmark family the scope of `skill-bench`.

## Comparative method

For each benchmark family, reviews should reconstruct an evolution chain:

```text
established design → demonstrated/admitted limitation
  → newer design response → evidence the response works
  → remaining limitation → implication or experiment for skill-bench
```

### Required comparison fields

| Field | Question |
|---|---|
| Construct and intended use | What capability or decision is the benchmark supposed to support? |
| Unit of work | Question, episode, repository issue, browser task, workspace, artifact package, professional handoff, or longitudinal stream? |
| Inputs and outputs | What context, tools, state, and artifacts are available and produced? |
| Environment | Static dataset, executable sandbox, live web, desktop, SaaS workspace, or persistent organization? |
| Scoring | Exact match, tests, state checks, rubric criteria, judge model, expert comparison, or mixed evidence? |
| Adoption evidence | In what sense is it widely used: citations, model reports, leaderboards, ecosystem tooling, or practitioner use? |
| Strengths to retain | What made it useful, scalable, discriminative, reproducible, or interpretable? |
| Limitations to repair | What validity, realism, contamination, grader, coverage, cost, reliability, or maintenance failure occurs? |
| Newer response | Which newer benchmark explicitly or implicitly addresses the limitation? |
| Response evidence | Is the claimed improvement empirically demonstrated, merely designed, or only asserted? |
| Release audit | Are tasks, environments, graders, traces, results, versions, and dependencies inspectable and reproducible? |
| Skill-bench transfer | What should be adopted, modified, rejected, tested, or encoded? |

## Family portfolio

The portfolio should stay balanced. Depth is allocated by relevance and unresolved design leverage rather than popularity alone.

| Family | Established anchors | Newer directions to prioritize | Strengths to inspect | Common limitations/opportunities |
|---|---|---|---|---|
| Language knowledge and reasoning | MMLU, BIG-bench/BBH, ARC, GSM8K | MMLU-Pro, GPQA, ARC-AGI and contamination-resistant/live variants | Standardization, low-cost administration, broad model coverage, comparability | Static/final-answer units, contamination, saturation, ambiguous items, weak workflow/artifact validity, benchmark-specific training |
| Coding and software engineering | HumanEval, MBPP, APPS | SWE-bench Verified/variants, LiveCodeBench, Terminal-Bench and newer repository/terminal suites | Executable tests, reproducibility, concrete task outcomes, ecosystem adoption | Test incompleteness, issue selection, environment/harness confounds, leakage, patch equivalence, narrow occupational inference |
| Web research and browsing | WebArena, MiniWoB++, GAIA | BrowseComp, BrowserGym ecosystems, deep-research benchmarks, changing-web evaluations | Tool use, retrieval, navigation, multi-step state, source access | Website drift, brittle environments, answer leakage, weak source-quality/entailment checks, live-web non-reproducibility |
| Tool/API and transactional agents | ToolBench, API-Bank, function-calling suites | τ-bench and stateful multi-turn transactional evaluations | Explicit actions, deterministic APIs, state changes, partial checks | Synthetic APIs, shallow objectives, underspecified side effects, simulator validity, missing recovery/safety evidence |
| Computer and mobile use | OSWorld, AndroidWorld | OSWorld 2.0 and more reproducible/diagnostic computer-use suites | End-to-end interface interaction, broad applications, visual grounding | Flakiness, expensive execution, hidden environment faults, task validity, narrow final-state grading, poor root-cause attribution |
| Office/workspace and professional workflows | OfficeBench, WorkArena, spreadsheet benchmarks | Workspace-Bench, Workflow-GYM, SaaS-Bench, MBABench and persistent-workspace designs | Real files/apps, state, dependencies, multi-artifact work, professional conventions | Authored realism versus ecological validity, destructive side effects, provenance, dependency inference, environment maintenance |
| Professional artifacts and economically valuable work | Expert-written professional tasks, GDPval-style evaluations | GDPval, AA-Briefcase/Lite, LH-Bench, Agents' Last Exam and newer occupational/artifact suites | Stakeholder-facing artifacts, economic framing, expert criteria, broad occupations | Sampling and weighting, exposed witnesses/rubrics, pairwise preference versus readiness, expert ceiling, cost, private data |
| Long-horizon research and knowledge work | GAIA and report-generation evaluations | PaperBench, AIDABench, AARRI, deep-research and handoff-centered benchmarks | Synthesis, evidence, iterative work, long outputs, realistic decisions | Open-ended ground truth, citation/authority failures, judge dependence, outcome hindsight, under-observed process, handoff usability |
| Multimodal artifact evaluation | VQA/document benchmarks and presentation checks | SciVisAgentBench, PresentBench and artifact-view-aware evaluation | Visual and structured artifacts, render quality, multiple representations | Renderer/control confounds, lossy views, subjective presentation judgments, missing authoritative representation |
| Safety and adversarial agents | Prompt-injection and tool-safety suites | AgentDojo, ClawSafety and cross-domain action-consequence evaluations | Explicit threats, action consequences, reproducible attacks | Attack-selection bias, ASR without utility/over-refusal, unrealized side effects, weak severity and recovery measurement |
| Human/expert and grader evaluation | Human preference and rubric scoring | ResearchRubrics, AgentRewardBench, JADE, many-facet rater models, disagreement-aware evaluation | Scalable qualitative assessment, inspectable criteria, expert judgment | Rater dependence, applicability, criterion overlap, shared-cue leakage, evidence-view insufficiency, no absolute acceptance threshold |
| Benchmark validity, psychometrics, and lifecycle | Classical test theory and static leaderboards | ECBD, agent psychometrics, task-health, contamination, dynamic assembly and validity-argument approaches | Calibration, comparability, explicit constructs, uncertainty | Rank-only interpretation, population ambiguity, item dependence, saturation, revision drift, unsupported capability claims |

Names in this table are starting anchors, not claims that every item is equally relevant or already deeply reviewed. Discovery must identify official papers, repositories, releases, variants, and evidence of actual adoption before making comparative claims.

## Cross-family questions

Every consolidation should look for conclusions that recur across families:

1. Why do simple, executable, standardized benchmarks become widely used?
2. Which useful properties are lost when realism and horizon increase?
3. Which final-state checks are robust, and which hide process or causal failures?
4. When do rubric or judge systems improve coverage but weaken reproducibility?
5. How do newer suites distinguish model capability from scaffold, tool, harness, environment, and grader?
6. Which benchmark limitations are addressed by design only, and which have evidence of improvement?
7. How does public release change a benchmark from capability evidence into calibration material?
8. What costs and maintenance burdens make a benchmark unusable despite strong validity?
9. What can be standardized across knowledge-work domains, and what must remain domain-specific?
10. Which strengths explain adoption and should be retained even when the construct changes?

## Outputs

The research stream should update:

- [`state-of-the-art-map.md`](state-of-the-art-map.md): family-level comparison;
- [`research-synthesis-index.md`](research-synthesis-index.md): grouped conclusions and relevance tiers;
- [`../papers/topic-index.md`](../papers/topic-index.md): navigable review organization;
- `papers/agent-benchmarks/`: full-text and release-based reviews;
- `data/papers/index.json`: acquisition and provenance status;
- schemas, validators, fixtures, and pilots only when comparative evidence supports a concrete change.

## Quality and stopping rules

- Do not call a benchmark commonly used without recording the evidence and sense of use.
- Do not claim a newer design fixed a limitation without inspecting its method and results.
- Do not deep-review every historical benchmark; use established anchors to explain evolution.
- Prefer current primary papers, official benchmark repositories, task releases, graders, and evaluation artifacts.
- Preserve paper-time versus post-paper release boundaries.
- Stop a family scan when added sources repeat known strengths/limitations without changing a decision.
- Consolidate before expanding a family further.
- Convert comparative insights into explicit retain/repair/test decisions for `skill-bench`.
