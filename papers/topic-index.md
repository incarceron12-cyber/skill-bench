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
| [OccuBench](agent-benchmarks/2026-07-15-occubench-language-simulator-validity.md) | When does an LLM-generated tool environment support a synthetic transition-system claim rather than occupational fitness or real-environment robustness? | language simulators, occupational labels, fault injection, verifier coupling |
| [$OneMillion-Bench](agent-benchmarks/2026-07-14-onemillion-professional-value-validity.md) | When does expert-authored rubric performance support a professional-work claim, and why is wage-cost attached to passing items not economic value delivered? | economic claims, rubrics, source authority, search |
| [Efficient Benchmarking of AI Agents](agent-benchmarks/2026-07-09-efficient-benchmarking-ai-agents.md) | When can a reduced panel preserve useful comparisons, and what coverage is lost? | task selection, cost, rank fidelity |
| [Agent Psychometrics](agent-benchmarks/2026-07-09-agent-psychometrics.md) | How should task difficulty and configured-system ability be modeled? | calibration, IRT, response matrices |
| [Benchmark Ceiling](agent-benchmarks/2026-07-10-benchmark-ceiling-expert-labor-scarcity.md) | What expert-labor and renewal constraints are hypothesized, and how strong is their evidence? | economics, expert scarcity, lifecycle |
| [Benchmark-to-risk expert elicitation](agent-benchmarks/2026-07-12-benchmark-to-risk-expert-elicitation.md) | What evidence is required between a configured-system benchmark observation and a consequential workflow or stakeholder decision claim? | consequence validity, structured judgment, disagreement, decision loss |
| [OfficeEval](agent-benchmarks/2026-07-12-officeeval-standardized-exam-validity.md) | When does adapting an external standardized exam preserve lineage but require a new validity and threshold-transport argument? | external instruments, native artifacts, criterion dependence |
| [Nubank production evaluation](agent-benchmarks/2026-07-14-nubank-offline-online-production-validity.md) | When does an adaptively selected offline-to-online association support prospective production-validity claims rather than retrospective co-movement among treatment bundles? | production evaluation, A/B testing, metric funnels, selection, configured systems |

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
| [AFTER](agent-benchmarks/2026-07-13-after-procedural-memory-transfer-validity.md) | When does trace-refined procedural memory transfer across tasks, work contexts, and solvers rather than overfit shared lineage or feedback? | evolution, transfer edges, configured systems, missingness |
| [SLBench](agent-benchmarks/2026-07-13-slbench-skill-relation-validity.md) | When does a generated executable case validly test a dependency among procedural clauses, and where can source, extraction, projection, observer, or consequence errors enter? | skill relations, task generation, grader validity, root cause |
| [SOP-Bench](agent-benchmarks/2026-07-14-sop-bench-procedure-task-validity.md) | When does a generated procedure/data/tool/oracle package measure procedural fidelity rather than closed-world endpoint recovery? | human–AI authoring, SOP projection, tool traces, oracle validity, release drift |
| [Data Therapist](agent-benchmarks/2026-07-11-data-therapist-tacit-knowledge-elicitation.md) | How can tacit analytic knowledge be elicited and represented without laundering model hypotheses into expertise? | elicitation, data work, provenance |
| [Laboratory workflow twins](agent-benchmarks/2026-07-13-laboratory-workflow-expert-elicitation.md) | When do role-gated workflow claims and masking relations support task/check projections, and why is graph query success not substantive or operational validity? | claim authority, mandatory nulls, observability, root/surface, consent |
| [Industrial expertise codification](agent-benchmarks/2026-07-11-industrial-expertise-codification-agent.md) | When does a codified-knowledge package effect support expertise-transfer or expert-equivalence claims? | industrial case, rule representation, co-design, validity |
| [ArtisanCAD](agent-benchmarks/2026-07-12-artisancad-expert-procedural-transfer-validity.md) | When does a macro-derived procedural IR demonstrate expert transfer, native-artifact editability, or production readiness? | CAD, procedural IR, dependency integrity, claim validity |
| [SimInstruct](agent-benchmarks/2026-07-11-siminstruct-simulated-novice-elicitation.md) | What can simulated novice interactions reveal, and where is real expert/novice evidence still needed? | cognitive elicitation, simulation |
| [TREC Legal participatory benchmark design](agent-benchmarks/2026-07-14-trec-legal-participatory-benchmark-design.md) | When does expert participation change benchmark authority and measurement, and which representation, causal, cost, and simulation claims remain unsupported? | co-design, decision rights, adjudication, metric validity |
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
| [DeskCraft](agent-benchmarks/2026-07-14-deskcraft-interactive-workflow-validity.md) | When does a phased desktop interaction protocol measure endpoint conformance rather than proactive clarification, human collaboration, or professional acceptance? | desktop agents, simulators, triggers, adoption, burden, native artifacts |
| [SaaS-Bench](agent-benchmarks/2026-07-11-saas-bench-stateful-workflow-validity.md) | What does cross-application persistent-state evaluation add, and what simulator/checkpoint limits remain? | SaaS, checkpoints, workflow |
| [AutomationBench](agent-benchmarks/2026-07-15-automationbench-workflow-projection-validity.md) | When do executable multi-app state, hidden evidence, strict assertions, and deterministic reset support synthetic workflow conformance rather than production-automation validity? | SaaS APIs, synthetic state, transition transport, observer coverage, strict scoring |
| [MBABench](agent-benchmarks/2026-07-11-mbabench-spreadsheet-artifact-validity.md) | How should spreadsheet correctness, formulas, structure, finance judgment, and presentation be separated? | spreadsheets, finance, artifacts |
| [KWBench](agent-benchmarks/2026-07-11-kwbench-unprompted-problem-recognition.md) | How can a benchmark measure recognition of latent work rather than only compliance with explicit instructions? | initiative, problem recognition, judgment |
| [EnterpriseClawBench](agent-benchmarks/2026-07-11-enterpriseclawbench-session-derived-validity.md) | What can session-derived enterprise tasks support, and how do provenance and sampling constrain inference? | enterprise, sessions, ecological validity |
| [AlphaEval](agent-benchmarks/2026-07-11-alphaeval-production-grounded-validity.md) | When do production-sourced requirements survive task, grader, score, and value transformations? | production requirements, projection validity, criterion drift |
| [Delegate52](agent-benchmarks/2026-07-11-delegate52-delegated-artifact-integrity.md) | How should delegated work preserve source boundaries, artifact integrity, and responsibility? | delegation, provenance, handoff |
| [AgentCoop](agent-benchmarks/2026-07-11-agentcoop-typed-handoffs-localized-repair.md) | How can multi-agent handoffs and localized repair be represented without hiding upstream failures? | collaboration, handoff, recovery |
| [AARRI](agent-benchmarks/2026-07-11-aarri-research-judgment-lifecycle.md) | How should research judgment, action, abstention, escalation, and artifact consequences be evaluated? | research, judgment, non-completion |
| [OSWorld 2.0](agent-benchmarks/2026-07-11-osworld2-long-horizon-workflow-validity.md) | Do long, evolving desktop workflows repair short-task validity, and which professional/reliability claims remain unsupported? | computer use, checkpoints, dynamic state, safety |
| [OfficeBench](agent-benchmarks/2026-07-11-officebench-cross-application-office-validity.md) | When do cross-application labels and selected final-state predicates support typed state-transition claims rather than professional office-work validity? | office workflows, state deltas, artifact evidence, collateral effects |
| [WorkArena L1](agent-benchmarks/2026-07-12-workarena-l1-knowledge-work-validity.md) | What do parameterized enterprise-UI tasks and native-state predicates establish, and where do work sampling, collateral-state, professional-use, and reset claims exceed the evidence? | browser agents, ServiceNow, state validators, task projection |
| [WorkArena++](agent-benchmarks/2026-07-11-workarena-plus-compositional-validity.md) | What does executable workflow composition establish, and when do dependency, polling, reset, and provenance gaps block planning or realism claims? | composition, state validators, reset, construct validity |
| [HippoCamp](agent-benchmarks/2026-07-11-hippocamp-personal-context-validity.md) | When do composite contextual files support retrieval and answer claims, and where do authorization, adoption, consequence, privacy, and affected-party validity remain unmeasured? | personal context, multimodal retrieval, authority, consequence |
| [SovereignPA-Bench](agent-benchmarks/2026-07-13-sovereignpa-consent-mediation-validity.md) | When do current intent, memory, platform pressure, evidence, consent, and burden support representative action rather than agreement with an author-defined prompt-policy score? | authority, consent, platform mediation, information flow, burden |
| [UnderSpecBench](agent-benchmarks/2026-07-13-underspecbench-action-boundary-validity.md) | When does an underspecified request justify inspection, clarification, refusal/escalation, or action rather than agreement with a fixed private oracle? | authorization, action boundary, side effects, observer coverage |
| [MapSatisfyBench](agent-benchmarks/2026-07-15-mapsatisfybench-behavior-grounded-hidden-requirements.md) | When can behavior nominate a fair hidden factor, and why do prediction, current applicability, authority, causal consequence, and user acceptance require separate evidence? | behavior chains, hidden requirements, personalization, clarification, satisfaction validity |
| [Ambig-DS](agent-benchmarks/2026-07-13-ambig-ds-task-framing-validity.md) | When does an executable artifact hide an unsupported target or objective commitment, and what does idealized clarification actually identify? | task framing, ambiguity, clarification, artifact validity |
| [Synthetic Computers at Scale](agent-benchmarks/2026-07-13-synthetic-computers-workspace-validity.md) | When does persona-conditioned workspace generation provide a useful stress substrate, and why do scale and internal consistency not establish occupational or professional validity? | synthetic environments, file graphs, long horizon, simulated collaboration |
| [OccuBench](agent-benchmarks/2026-07-15-occubench-language-simulator-validity.md) | Which state, transition, observation, fault, grader, and transport evidence is required when a language model replaces a professional environment? | simulated tools, state authority, matched faults, conformance |
| [LongMedBench](agent-benchmarks/2026-07-14-longmedbench-longitudinal-clinical-validity.md) | When does a long record actually make a later decision history-dependent, and why is agreement with the recorded next event not clinical appropriateness? | longitudinal necessity, temporal state, retrospective oracle, clustered outcomes |
| [DORA](agent-benchmarks/2026-07-14-dora-disaster-response-consequence-validity.md) | When do real historical evidence, GT-derived endpoints, and one executable analytical witness support only an offline package claim rather than safe operational action or consequence? | geospatial tools, authority, alternative paths, decision-calibrated tolerances, consequence validity |
| [SciAgentArena](agent-benchmarks/2026-07-14-sciagentarena-scientific-work-validity.md) | When do executable scientific stages and step-wise/pipeline contrasts support bounded workflow claims rather than real-world science, novelty, autonomy, or research impact? | scientific workflows, dependency lineage, validity checks, configured systems, release drift |
| [AstaBench](agent-benchmarks/2026-07-14-astabench-scientific-suite-aggregation-validity.md) | When does a broad, cost-aware scientific suite support a portfolio comparison, and why do common interfaces and macro-averaging not create one validated research-assistance scale? | scientific suite, portfolio estimand, aggregation policy, tool confounding, cost boundary, gated release |

**Cross-family synthesis:** [Professional knowledge-work benchmark evolution](../docs/concepts/professional-benchmark-evolution-matrix.md) compares the fully reviewed/release-audited professional families plus the official AA-Briefcase-Lite release. It records retain/repair/test decisions. OfficeBench supplies bounded cross-store transition and selected final-state-predicate evidence; AutomationBench adds broad executable synthetic multi-app state, strict guards, and tool-surface interventions; TheAgentCompany, OdysseyBench, WorkArena L1, and WorkArena++ add integrated substrate, evidence-to-action, atomic native-state, and composition evidence. None licenses occupational, production-transition, persistent-memory, collaboration, planning, professional-validity, or readiness claims.

**Framing-and-authority synthesis:** Read [Ambig-DS](agent-benchmarks/2026-07-13-ambig-ds-task-framing-validity.md) with [UnderSpecBench](agent-benchmarks/2026-07-13-underspecbench-action-boundary-validity.md) and [KWBench](agent-benchmarks/2026-07-11-kwbench-unprompted-problem-recognition.md). Together they separate latent-problem recognition, public admissible-framing sets, resolvable uncertainty, authority-dependent clarification, private intent, action, and consequence. Preserve paired intervention hashes and stage-separated recognition, disclosure, question, routing, uptake, action, and artifact/state observations. Ambig-DS's synthetic Kaggle-derived edits and ideal oracle, UnderSpecBench's fixed private oracle and unavailable release, and KWBench's cold final-artifact gate support diagnostic patterns—not natural ambiguity prevalence, realistic stakeholder authority, professional escalation, or readiness.

**Interactive-family synthesis:** [Web, tool-use, and computer-use benchmark evolution](../docs/concepts/web-tool-computer-benchmark-evolution.md) compares full immutable primary sources for GAIA, WebArena, ToolBench, API-Bank, τ-bench, OSWorld, AndroidWorld, and BrowseComp. It traces answer→action→state→policy/user→repeated-outcome measurement and records retain/repair/test decisions. Release-audited reviews now cover [OSWorld 2.0](agent-benchmarks/2026-07-11-osworld2-long-horizon-workflow-validity.md) and [BrowserGym](agent-benchmarks/2026-07-11-browsergym-ecosystem-measurement.md), with their successor and adapter claim limits preserved.

**Reasoning/coding synthesis:** [Reasoning and coding benchmark evolution](../docs/concepts/reasoning-coding-benchmark-evolution.md) compares full primary papers for MMLU, MMLU-Pro, HumanEval, and LiveCodeBench plus pinned current successor releases. It separates low-friction adoption, evidenced headroom/prompt stability, executable equivalence, and rolling freshness from unsupported professional-validity, contamination-free, and longitudinal-trend claims.

## 4. Rubrics, graders, raters, and artifact evidence

| Review | Primary question | Secondary tags |
|---|---|---|
| [ResearchRubrics](agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md) | How can expert criteria be authored and reviewed, and what dependence, applicability, and threshold problems remain? | rubrics, examples, judging |
| [BigFinanceBench](agent-benchmarks/2026-07-14-bigfinancebench-workflow-derivation-validity.md) | When does a stepwise financial rubric observe an audited derivation rather than narrated agreement with one reference decomposition? | source provenance, criterion dependence, traces, judge validity |
| [JADE](agent-benchmarks/2026-07-11-jade-dynamic-professional-grading.md) | How should fixed obligations differ from response-triggered claims and consequences in dynamic grading? | adaptive criteria, applicability, evidence |
| [GroundEval](agent-benchmarks/2026-07-14-groundeval-evidence-path-validity.md) | When does a deterministic evidence-path check establish a valid actor/time, negative-search, or dependency observation rather than repeat an incomplete authored contract? | deterministic grading, access, verified absence, causal claims |
| [AgentRewardBench](agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md) | How reliable are judge models under different observer views and trajectory evidence? | judge reliability, trajectories, annotations |
| [RuVerBench](agent-benchmarks/2026-07-14-ruverbench-criterion-judge-validity.md) | When does criterion-level agreement over long reports and trajectories establish a reliable configured verifier, and which selection, label-policy, evidence-view, batching, and voting limits remain? | rubric verification, long context, annotations, call topology |
| [Adversarial verifier hardening](agent-benchmarks/2026-07-14-adversarial-verifier-hardening-validity.md) | When does adversarial grader repair reduce false accepts without silently narrowing the legitimate solution set? | reward hacking, verifier falsification, alternative paths, benchmark revision |
| [AsymmetryZero](agent-benchmarks/2026-07-14-asymmetryzero-semantic-eval-contracts.md) | When does an executable criterion contract preserve expert judgment, and why are panel agreement, repeated-call reliability, correctness, and decision equivalence separate? | semantic evals, model juries, aggregation, adapter conformance |
| [Auto Benchmark Audit](agent-benchmarks/2026-07-14-auto-benchmark-audit-task-defect-validity.md) | When does an automated, path-grounded finding support candidate-defect triage, and why are auditor-label prevalence, deletion sensitivity, adjudicated defects, and repaired-instrument validity different? | task health, benchmark maintenance, auditor validity, repair lifecycle, release audit |
| [Many-Facet Human/AI Rater Effects](agent-benchmarks/2026-07-11-many-facet-human-ai-rater-effects.md) | How should task, system, rater, criterion, and interaction effects be separated? | rater modeling, psychometrics, human-AI |
| [Rubric Modification and Human/Autorater Agreement](agent-benchmarks/2026-07-11-rubric-modification-human-autorater-agreement.md) | When do rubric changes improve agreement, and what construct shifts might they introduce? | rubric evolution, agreement, calibration |
| [SciVisAgentBench](agent-benchmarks/2026-07-10-scivisagentbench-multimodal-artifact-evaluation.md) | Which artifact representations and controls are sufficient for valid multimodal grading? | visualization, renderer, admissibility |
| [PaperBench](agent-benchmarks/2026-07-15-paperbench-replication-rubric-validity.md) | When do dense hierarchical criteria support partial-progress diagnostics, and why do compensatory scoring and leaf-level judge agreement not establish successful replication? | research replication, rubric dependencies, execution lineage, judge validity, human baseline |

**Cross-family synthesis:** [Grading, validity, and benchmark-lifecycle evolution](../docs/concepts/grading-validity-lifecycle-evolution.md) compares exact/executable checks, state and artifact observers, fixed/dynamic rubrics, human preference and plural judgment, rater/psychometric models, claim-validity systems, reliability profiles, task health, and live forms through explicit retain/repair/test decisions.

## 5. Reliability, traces, recovery, memory, and execution

| Review | Primary question | Secondary tags |
|---|---|---|
| [Agent Reliability Profile](agent-benchmarks/2026-07-11-agent-reliability-profile.md) | How should repeated success, failure severity, recovery, and operational reliability be profiled? | reliability, repetition, operations |
| [Stochastic Agent Evaluations](agent-benchmarks/2026-07-14-stochastic-agent-evaluations-icc-validity.md) | When do repeated binary trials support a variance-component reliability claim, and why is variance of finite-trial task means not ICC(1,1) or a transferable repeat budget? | ICC, repeated trials, clustered uncertainty, missingness, configured systems |
| [Agentic Confidence Calibration](agent-benchmarks/2026-07-14-agentic-confidence-calibration-validity.md) | When does trajectory-derived confidence predict one configured trial's success, and what additional transport, decision-loss, and workload evidence is required before using it for review, escalation, or acceptance? | confidence calibration, selective prediction, decision validity, logprobs |
| [STRACE](agent-benchmarks/2026-07-09-strace.md) | How can long-horizon failures be localized to supported upstream causes? | causal diagnosis, traces, repair |
| [Harness-Bench](agent-benchmarks/2026-07-10-harness-bench-execution-isolation.md) | How should launcher, tool, permission, sandbox, and environment differences be isolated? | harness, reproducibility, system identity |
| [Anchor](agent-benchmarks/2026-07-10-anchor-artifact-drift-generation.md) | How can generated tasks keep instructions, environment, witness, and checker projections aligned? | task generation, conformance, drift |
| [ClawArena](agent-benchmarks/2026-07-10-clawarena-evolving-information.md) | How should corrections, retractions, supersession, and consequential updates be represented? | evolving evidence, workspace, state |
| [LongMemEval v2](agent-benchmarks/2026-07-11-longmemeval-v2-environment-experience-memory.md) | How should environment experience, memory access, adoption, retention, and downstream effect differ? | memory, longitudinal evaluation, experience |
| [MemoryArena](agent-benchmarks/2026-07-13-memoryarena-interdependent-experience-action.md) | When do interdependent sessions test memory-conditioned action, and what controls isolate retrieval, state reconstruction, adoption, and consequence? | memory, session dependency, feedback, action consequence |
| [EvoMemBench](agent-benchmarks/2026-07-15-evomembench-memory-scope-content-validity.md) | When does an in-/cross-episode × knowledge/execution taxonomy organize configured memory tests without implying a common self-evolving-memory construct? | memory scope, information flow, treatment parity, release validity |
| [WorkBench Revisited](agent-benchmarks/2026-07-12-workbench-revisited-longitudinal-lifecycle.md) | How should corrected current forms, frozen anchors, renewed forms, and score bridges coexist? | lifecycle, instrument drift, side-effect denominators |
| [UniClawBench](agent-benchmarks/2026-07-13-uniclawbench-proactive-closed-loop-validity.md) | When does role-separated synthetic feedback measure requested-task repair rather than proactivity, natural-user behavior, or non-leaking evaluation? | feedback firewall, repair, simulators, information flow |
| [EdgeBench](agent-benchmarks/2026-07-13-edgebench-within-run-learning-validity.md) | What do day-scale visible-feedback and hidden-snapshot trajectories establish, and how do adaptive search, persistence, best-so-far selection, and censoring bound learning claims? | longitudinal evaluation, feedback budget, persistence, estimands |
| [Signals trajectory triage](agent-benchmarks/2026-07-14-signals-trajectory-triage-sampling-validity.md) | When does signal-enriched trajectory review improve case-finding yield, and why can that queue not estimate prevalence or downstream utility without a probability sentinel and selection ledger? | review sampling, inclusion probabilities, annotation burden, production monitoring |
| [Measuring Agents in Production](agent-benchmarks/2026-07-14-measuring-agents-production-practitioner-evidence.md) | When can selected practitioner reports guide portfolio and authoring choices, and why do reported practice prevalence and deployment conditioning not identify successful or reliable methods? | practitioner survey, human evaluation, bounded autonomy, missingness, operational validity |

OdysseyBench is indexed primarily with workplace workflows rather than duplicated
here: it consumes a supplied synthetic history and acts on office state, but does
does not test memory accumulated persistently through executed experience.

**Action-and-memory synthesis:** Read UnderSpecBench with AARRI for the distinction
among private intent, public authorization, resolvable uncertainty, and calibrated
terminal actions. Read MemoryArena with LongMemEval-V2 for the separate estimands of
evidence delivery and held-out action benefit. Together they require link-level
observation and matched controls; endpoint agreement or success alone supports no
professional, longitudinal-learning, root-cause-memory, or deployment claim.

**Feedback-intervention synthesis:** Read UniClawBench with EdgeBench to separate
ecological support, evaluator-generated intervention, and hidden measurement.
Preserve role/component identity, proposition-level information flow, channel
authority and adaptive-query budget, state-persistence/reset policy, current and
best-so-far outcomes, new errors, cost, run-at-risk denominators, and censoring.
Requested-task repair is not proactivity; cumulative selected quality is not
endpoint quality; and improvement under evaluator feedback estimates a configured
adaptive package rather than unaided capability or a universal learning law.

## 6. Safety, contamination, and integrity

| Review | Primary question | Secondary tags |
|---|---|---|
| [ClawSafety](agent-benchmarks/2026-07-10-clawsafety-cross-domain-injection-validity.md) | How should prompt-injection placement, exposure, adoption, attempted action, realized harm, severity, recovery, and benign utility differ? | prompt injection, tool safety, utility |
| [SafePro](agent-benchmarks/2026-07-14-safepro-professional-action-safety-validity.md) | When does a harmful professional-style instruction plus transcript judge support only configured criterion agreement rather than action safety or realized consequence? | professional safety, observer validity, artifacts, refusal utility |
| [Context-to-Execution Integrity](agent-benchmarks/2026-07-14-context-to-execution-integrity-action-authority.md) | When do protected-field, exact-effect, and invocation authority jointly support mediated-gate conformance rather than end-to-end agent safety? | action authority, capabilities, exact effects, complete mediation |
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
