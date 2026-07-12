# Paper Review Topic Index

This is the navigation layer for the reviewed corpus. Reviews currently remain in `agent-benchmarks/` so existing citations and provenance paths do not break; organization is by **primary research question** here rather than by moving files into mutually exclusive folders. Many papers span multiple themes, so secondary tags are included.

For grouped conclusions and relevance tiers, use [`../docs/research-synthesis-index.md`](../docs/research-synthesis-index.md). For benchmark-family evolution, use [`../docs/benchmark-landscape-research-program.md`](../docs/benchmark-landscape-research-program.md).

## Status vocabulary

- **Deep review:** full paper/text was acquired and read; source/release evidence is recorded in the review.
- **Release-audited:** official implementation/data artifacts were additionally inspected with timing and provenance limits.
- **Triage:** metadata/abstract-level only; not eligible for deep methodological claims.

The review files below are deep reviews unless their own evidence-status section states otherwise. The machine-readable acquisition and review status lives in [`../data/papers/index.json`](../data/papers/index.json).

## 1. Benchmark validity, constructs, coverage, and claims

| Review | Primary question | Secondary tags |
|---|---|---|
| [ECBD: Evidence-Centered Benchmark Design](agent-benchmarks/2026-07-10-ecbd-evidence-centered-benchmark-design.md) | How should intended use, constructs, tasks, measurements, and score claims be connected by evidence? | validity, assembly, warrants |
| [Validity-Centered AI Evaluation](agent-benchmarks/2026-07-10-validity-centered-ai-evaluation.md) | What validity arguments are required before promoting a score into a capability or readiness claim? | claims, deployment, evidence |
| [Design Report for Knowledge-Work Benchmarks](agent-benchmarks/2026-07-11-design-report-knowledge-work-benchmarks.md) | How should activities, settings, outputs, handoffs, and omitted work bound knowledge-work claims? | work taxonomy, handoffs, coverage |
| [Agents' Last Exam](agent-benchmarks/2026-07-11-agents-last-exam-expert-task-validity.md) | What can expert-authored long-horizon tasks establish, and which selection or verifier limits remain? | expert tasks, horizon, validity |
| [GDPval](agent-benchmarks/2026-07-10-gdpval-occupational-task-validity.md) | How do occupational framing, expert artifacts, suite assembly, and inference population differ? | occupations, artifacts, sampling |
| [Efficient Benchmarking of AI Agents](agent-benchmarks/2026-07-09-efficient-benchmarking-ai-agents.md) | When can a reduced panel preserve useful comparisons, and what coverage is lost? | task selection, cost, rank fidelity |
| [Agent Psychometrics](agent-benchmarks/2026-07-09-agent-psychometrics.md) | How should task difficulty and configured-system ability be modeled? | calibration, IRT, response matrices |
| [Benchmark Ceiling](agent-benchmarks/2026-07-10-benchmark-ceiling-expert-labor-scarcity.md) | What expert-labor and renewal constraints are hypothesized, and how strong is their evidence? | economics, expert scarcity, lifecycle |
| [Benchmark-to-risk expert elicitation](agent-benchmarks/2026-07-12-benchmark-to-risk-expert-elicitation.md) | What evidence is required between a configured-system benchmark observation and a consequential workflow or stakeholder decision claim? | consequence validity, structured judgment, disagreement, decision loss |
| [OfficeEval](agent-benchmarks/2026-07-12-officeeval-standardized-exam-validity.md) | When does adapting an external standardized exam preserve lineage but require a new validity and threshold-transport argument? | external instruments, native artifacts, criterion dependence |

**Benchmark-to-consequence synthesis:** Treat consequence promotion as a linked
chain—observation → bounded capability interpretation → scenario applicability,
access, and use → conditional workflow effect → outcome frequency/severity →
stakeholder threshold/loss. The reviewed cyber pilot makes rival warrants and
information-condition effects visible, but does not validate its probability
ranges, calibrated uplift, cyber risk, expected harm, or decision use. Preserve
packet/order identity, initial and revised rationales, deliberative dependence,
estimand forks, calibration status, aggregation sensitivity, excluded links, and
the next discriminating evidence; use the existing validity, metric, participation,
and elicitation machinery rather than a domain-specific schema.

## 2. Expertise elicitation, transfer, participation, and skills

| Review | Primary question | Secondary tags |
|---|---|---|
| [LH-Bench](agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md) | How can expert procedural skills connect execution guidance to artifact and rubric evaluation? | intervention, artifacts, long horizon |
| [SkillsBench](agent-benchmarks/2026-07-10-skillsbench-paired-skill-efficacy.md) | How should skill/no-skill efficacy be compared without confounding the harness or rubric? | paired trials, uncertainty, intervention |
| [Data Therapist](agent-benchmarks/2026-07-11-data-therapist-tacit-knowledge-elicitation.md) | How can tacit analytic knowledge be elicited and represented without laundering model hypotheses into expertise? | elicitation, data work, provenance |
| [Industrial expertise codification](agent-benchmarks/2026-07-11-industrial-expertise-codification-agent.md) | When does a codified-knowledge package effect support expertise-transfer or expert-equivalence claims? | industrial case, rule representation, co-design, validity |
| [ArtisanCAD](agent-benchmarks/2026-07-12-artisancad-expert-procedural-transfer-validity.md) | When does a macro-derived procedural IR demonstrate expert transfer, native-artifact editability, or production readiness? | CAD, procedural IR, dependency integrity, claim validity |
| [SimInstruct](agent-benchmarks/2026-07-11-siminstruct-simulated-novice-elicitation.md) | What can simulated novice interactions reveal, and where is real expert/novice evidence still needed? | cognitive elicitation, simulation |
| [Consulting Cognitive Traps](agent-benchmarks/2026-07-10-consulting-cognitive-traps.md) | How can naive paths, expert cues, operations, and consequences become fair critical incidents? | hidden requirements, traps, rubrics |
| [Domain-Expert Participation Ethnography](agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md) | How should purpose, authority, transformation, approval, reciprocity, and withdrawal be governed? | participation, consent, incentives |
| [Expert Disagreement in Human Feedback](agent-benchmarks/2026-07-11-expert-disagreement-human-feedback-validity.md) | How should genuine expert disagreement affect labels, adjudication, and benchmark claims? | disagreement, authority, human evaluation |
| [JobBench](agent-benchmarks/2026-07-12-jobbench-delegation-desire-validity.md) | When can worker-reported delegation preference select tasks, and what additional evidence is required for consent, uptake, or worker outcomes? | delegation demand, occupational sampling, consent, outcome validity |
| [HAS-Bench](agent-benchmarks/2026-07-13-hasbench-configurable-human-participation-validity.md) | When does a configurable participant graph measure simulated assistance rather than identified human participation? | authority, user simulation, treatment bundles, burden |

**Demand-to-transfer synthesis:** Read [AlphaEval](agent-benchmarks/2026-07-11-alphaeval-production-grounded-validity.md) with [Industrial expertise codification](agent-benchmarks/2026-07-11-industrial-expertise-codification-agent.md). Together they motivate a bounded chain from production demand through elicitation authority, representation, task projection, configured intervention, and independent measurement to a claim ceiling. Add [JobBench](agent-benchmarks/2026-07-12-jobbench-delegation-desire-validity.md) for the worker-side boundary: historical preference → package fidelity → present consent/retained authority → configured-system measurement → observed uptake → measured outcome. The combined evidence supports demand/co-design provenance, one delegation-selection signal, and selected package effects—not occupational representativeness, tacit transfer, expert equivalence, worker benefit, production readiness, economic value, or cross-domain capability.

**Participation-treatment synthesis:** Read [HAS-Bench](agent-benchmarks/2026-07-13-hasbench-configurable-human-participation-validity.md) with [TheAgentCompany](agent-benchmarks/2026-07-11-theagentcompany-workplace-simulation-validity.md), [AgentCoop](agent-benchmarks/2026-07-11-agentcoop-typed-handoffs-localized-repair.md), and the [Domain-Expert Participation Ethnography](agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md). A social-role label or graph edge does not identify participant realization, authority, semantic uptake, causal repair, or human burden. Preserve the participation-policy vector and authority-event lineage, then measure availability, exercise, uptake, effect, and burden separately. Simulator-only trials license synthetic configured-collaboration claims, not human-participation, expert-substitution, professional-collaboration, or readiness claims.

## 3. Realistic knowledge work, workflows, workspaces, and artifacts

| Review | Primary question | Secondary tags |
|---|---|---|
| [TheAgentCompany](agent-benchmarks/2026-07-11-theagentcompany-workplace-simulation-validity.md) | What does an integrated simulated company establish, and where do workplace substrate, occupational validity, collaboration, consequences, and sampling diverge? | workplace simulation, coworkers, checkpoints, reset |
| [OdysseyBench](agent-benchmarks/2026-07-11-odysseybench-longitudinal-office-memory-validity.md) | When do dialogue-distributed requirements support consequential office action, and why is that not persistent memory or professional validity? | office workflows, history, evidence adoption, evaluator dispatch |
| [Workspace-Bench](agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md) | How should files, dependencies, provenance, observed use, mutations, and workspace integrity be evaluated? | persistent workspace, retrieval, causal use |
| [Workflow-GYM](agent-benchmarks/2026-07-11-workflow-gym-professional-state-validity.md) | How can professional GUI workflows and final state be evaluated without confusing environment faults with capability? | GUI, state, environment validity |
| [SaaS-Bench](agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md) | What does cross-application persistent-state evaluation add, and what simulator/checkpoint limits remain? | SaaS, checkpoints, workflow |
| [MBABench](agent-benchmarks/2026-07-11-mbabench-spreadsheet-artifact-validity.md) | How should spreadsheet correctness, formulas, structure, finance judgment, and presentation be separated? | spreadsheets, finance, artifacts |
| [KWBench](agent-benchmarks/2026-07-11-kwbench-unprompted-problem-recognition.md) | How can a benchmark measure recognition of latent work rather than only compliance with explicit instructions? | initiative, problem recognition, judgment |
| [EnterpriseClawBench](agent-benchmarks/2026-07-11-enterpriseclawbench-session-derived-validity.md) | What can session-derived enterprise tasks support, and how do provenance and sampling constrain inference? | enterprise, sessions, ecological validity |
| [AlphaEval](agent-benchmarks/2026-07-11-alphaeval-production-grounded-validity.md) | When do production-sourced requirements survive task, grader, score, and value transformations? | production requirements, projection validity, criterion drift |
| [Delegate52](agent-benchmarks/2026-07-11-delegate52-delegated-artifact-integrity.md) | How should delegated work preserve source boundaries, artifact integrity, and responsibility? | delegation, provenance, handoff |
| [AgentCoop](agent-benchmarks/2026-07-11-agentcoop-typed-handoffs-localized-repair.md) | How can multi-agent handoffs and localized repair be represented without hiding upstream failures? | collaboration, handoff, recovery |
| [AARRI](agent-benchmarks/2026-07-11-aarri-research-judgment-lifecycle.md) | How should research judgment, action, abstention, escalation, and artifact consequences be evaluated? | research, judgment, non-completion |
| [OSWorld 2.0](agent-benchmarks/2026-07-11-osworld2-long-horizon-workflow-validity.md) | Do long, evolving desktop workflows repair short-task validity, and which professional/reliability claims remain unsupported? | computer use, checkpoints, dynamic state, safety |
| [WorkArena L1](agent-benchmarks/2026-07-12-workarena-l1-knowledge-work-validity.md) | What do parameterized enterprise-UI tasks and native-state predicates establish, and where do work sampling, collateral-state, professional-use, and reset claims exceed the evidence? | browser agents, ServiceNow, state validators, task projection |
| [WorkArena++](agent-benchmarks/2026-07-11-workarena-plus-compositional-validity.md) | What does executable workflow composition establish, and when do dependency, polling, reset, and provenance gaps block planning or realism claims? | composition, state validators, reset, construct validity |
| [HippoCamp](agent-benchmarks/2026-07-11-hippocamp-personal-context-validity.md) | When do composite contextual files support retrieval and answer claims, and where do authorization, adoption, consequence, privacy, and affected-party validity remain unmeasured? | personal context, multimodal retrieval, authority, consequence |

**Cross-family synthesis:** [Professional knowledge-work benchmark evolution](../docs/concepts/professional-benchmark-evolution-matrix.md) compares the fully reviewed/release-audited professional families plus the official AA-Briefcase-Lite release. It records retain/repair/test decisions. OfficeBench remains an evidence gap; TheAgentCompany, OdysseyBench, WorkArena L1, and WorkArena++ now supply bounded substrate, evidence-to-action, atomic native-state, and composition evidence without licensing occupational, persistent-memory, collaboration, planning, professional-validity, or readiness claims.

**Interactive-family synthesis:** [Web, tool-use, and computer-use benchmark evolution](../docs/concepts/web-tool-computer-benchmark-evolution.md) compares full immutable primary sources for GAIA, WebArena, ToolBench, API-Bank, τ-bench, OSWorld, AndroidWorld, and BrowseComp. It traces answer→action→state→policy/user→repeated-outcome measurement and records retain/repair/test decisions. Release-audited reviews now cover [OSWorld 2.0](agent-benchmarks/2026-07-11-osworld2-long-horizon-workflow-validity.md) and [BrowserGym](agent-benchmarks/2026-07-11-browsergym-ecosystem-measurement.md), with their successor and adapter claim limits preserved.

**Reasoning/coding synthesis:** [Reasoning and coding benchmark evolution](../docs/concepts/reasoning-coding-benchmark-evolution.md) compares full primary papers for MMLU, MMLU-Pro, HumanEval, and LiveCodeBench plus pinned current successor releases. It separates low-friction adoption, evidenced headroom/prompt stability, executable equivalence, and rolling freshness from unsupported professional-validity, contamination-free, and longitudinal-trend claims.

## 4. Rubrics, graders, raters, and artifact evidence

| Review | Primary question | Secondary tags |
|---|---|---|
| [ResearchRubrics](agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | How can expert criteria be authored and reviewed, and what dependence, applicability, and threshold problems remain? | rubrics, examples, judging |
| [JADE](agent-benchmarks/2026-07-11-jade-dynamic-professional-grading.md) | How should fixed obligations differ from response-triggered claims and consequences in dynamic grading? | adaptive criteria, applicability, evidence |
| [AgentRewardBench](agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md) | How reliable are judge models under different observer views and trajectory evidence? | judge reliability, trajectories, annotations |
| [Many-Facet Human/AI Rater Effects](agent-benchmarks/2026-07-11-many-facet-human-ai-rater-effects.md) | How should task, system, rater, criterion, and interaction effects be separated? | rater modeling, psychometrics, human-AI |
| [Rubric Modification and Human/Autorater Agreement](agent-benchmarks/2026-07-11-rubric-modification-human-autorater-agreement.md) | When do rubric changes improve agreement, and what construct shifts might they introduce? | rubric evolution, agreement, calibration |
| [SciVisAgentBench](agent-benchmarks/2026-07-10-scivisagentbench-multimodal-artifact-evaluation.md) | Which artifact representations and controls are sufficient for valid multimodal grading? | visualization, renderer, admissibility |

**Cross-family synthesis:** [Grading, validity, and benchmark-lifecycle evolution](../docs/concepts/grading-validity-lifecycle-evolution.md) compares exact/executable checks, state and artifact observers, fixed/dynamic rubrics, human preference and plural judgment, rater/psychometric models, claim-validity systems, reliability profiles, task health, and live forms through explicit retain/repair/test decisions.

## 5. Reliability, traces, recovery, memory, and execution

| Review | Primary question | Secondary tags |
|---|---|---|
| [Agent Reliability Profile](agent-benchmarks/2026-07-11-agent-reliability-profile.md) | How should repeated success, failure severity, recovery, and operational reliability be profiled? | reliability, repetition, operations |
| [STRACE](agent-benchmarks/2026-07-09-strace.md) | How can long-horizon failures be localized to supported upstream causes? | causal diagnosis, traces, repair |
| [Harness-Bench](agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | How should launcher, tool, permission, sandbox, and environment differences be isolated? | harness, reproducibility, system identity |
| [Anchor](agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md) | How can generated tasks keep instructions, environment, witness, and checker projections aligned? | task generation, conformance, drift |
| [ClawArena](agent-benchmarks/2026-07-10-clawarena-evolving-information.md) | How should corrections, retractions, supersession, and consequential updates be represented? | evolving evidence, workspace, state |
| [LongMemEval v2](agent-benchmarks/2026-07-11-longmemeval-v2-environment-experience-memory.md) | How should environment experience, memory access, adoption, retention, and downstream effect differ? | memory, longitudinal evaluation, experience |
| [WorkBench Revisited](agent-benchmarks/2026-07-12-workbench-revisited-longitudinal-lifecycle.md) | How should corrected current forms, frozen anchors, renewed forms, and score bridges coexist? | lifecycle, instrument drift, side-effect denominators |

OdysseyBench is indexed primarily with workplace workflows rather than duplicated
here: it consumes a supplied synthetic history and acts on office state, but does
not test memory accumulated persistently through executed experience.

## 6. Safety, contamination, and integrity

| Review | Primary question | Secondary tags |
|---|---|---|
| [ClawSafety](agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md) | How should prompt-injection placement, exposure, adoption, attempted action, realized harm, severity, recovery, and benign utility differ? | prompt injection, tool safety, utility |
| [Search-Time Contamination](agent-benchmarks/2026-07-10-search-time-contamination.md) | How should source exposure and benchmark contamination be audited without overclaiming causal score inflation? | leakage, live search, role transition |
| [LiveBench](agent-benchmarks/2026-07-11-livebench-contamination-limited-lifecycle.md) | What does rolling recent-source evaluation repair, and when do renewal or grader changes break longitudinal comparability? | contamination, deterministic grading, lifecycle |

Safety and integrity also appear in Workspace-Bench, Delegate52, Harness-Bench, and the artifact-view reviews; they remain in their primary collections to avoid duplicate inventory rows.

## 7. Compounding and adaptive systems

| Review | Primary question | Secondary tags |
|---|---|---|
| [Agentic Context Engineering](agent-benchmarks/2026-07-10-agentic-context-engineering.md) | How can bounded context updates, provenance, contradiction, promotion, and rollback support learning? | context, lessons, rollback |
| [Self-Evolving Agents Survey](agent-benchmarks/2026-07-10-self-evolving-agents-survey.md) | What adaptation mechanisms and evaluation confounds recur across self-evolving systems? | evolution, retention, safety |

These reviews primarily support the research/build system and longitudinal evaluation. They do not redefine the benchmark as a self-improving-agent benchmark.

## Intake and organization rules

1. Every deep review stays linked from exactly one primary collection here.
2. Add secondary tags instead of duplicating or moving a review between multiple folders.
3. Record full-text, release, version, and evidence status inside the review and machine-readable paper index.
4. Add a paper only after it contributes a distinct method, limitation, contradiction, or benchmark implication.
5. Triage-only candidates remain in scouting reports or the machine index until selected for deep review.
6. Update [`../docs/research-synthesis-index.md`](../docs/research-synthesis-index.md) only when the review changes a grouped conclusion or relevance tier.
7. Update [`../docs/state-of-the-art-map.md`](../docs/state-of-the-art-map.md) when it changes the comparison of benchmark families.
8. Preserve stable file paths unless a repository-wide migration updates every link and provenance record.
