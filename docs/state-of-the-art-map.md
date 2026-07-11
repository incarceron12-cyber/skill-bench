# State-of-the-Art Map

This file tracks benchmark families relevant to `skill-bench`. For grouped conclusions and explicit source-relevance tiers, start with [`research-synthesis-index.md`](research-synthesis-index.md).

| Benchmark / Area | What it tests | Inputs | Outputs | Scoring | Why it matters for us | Open questions |
|---|---|---|---|---|---|---|
| AA-Briefcase / Lite | Private multi-project artifact benchmark; public demonstrative due-diligence week | Private thousands of files/91 tasks; Lite 147 files across 67 sources | PDF/LaTeX, XLSX, PPTX, MP4/SRT | Binary accuracy/critical-insight checks + pairwise analytical/presentation Elo | Strong source→check traceability, contradiction/supersession cases, artifact diversity | Private scored suite is unauditable; tasks reset independently, so “multi-week” is not longitudinal agent work; artifact-only judges cannot verify source entailment/use |
| GDPval / GDPval-AA | Broad occupational artifact-production slice | Multimodal case/task material | Professional work deliverables | Occupation-matched pairwise comparison against one human witness | Demonstrates expert task acquisition and occupational-frame breadth | How should frame, content, suite assembly, and inference populations be separated? |
| APEX-Agents-AA | Professional services tasks | Realistic app/workflow dependencies | Task completions | Rubric-based local file grading | Strong adjacent model for professional service workflows | What is reproducible publicly? |
| GAIA / BrowseComp | Generalist tool use and persistent live-web fact finding | Web, files, multimodal inputs | Short answers | Exact/semantic answer correctness | Historical anchors for tool composition and adversarial search depth | Live-web equivalence, source authority/use, search-time leakage, and professional research quality remain unmeasured |
| WebArena / BrowserGym | Stateful browser navigation plus a shared execution/experiment substrate over heterogeneous web families | Self-hosted or live websites; rich screenshot/DOM/AXTree/chat observations; benchmark-specific backends and datasets | Website state changes, synthetic task rewards, or final answers depending on family | One scalar interface over materially different native/wrapped evaluators (for example MiniWoB page reward, WebArena state/answer checks, AssistantBench answer matching, and later WebArena Verified component checks) | Retains alternative valid paths while reducing runner/adapter friction and exposing configured-system breadth | Full v2 paper and post-paper release audit shows transport interoperability, not native/adapted or cross-family measurement equivalence; independently pin upstream dataset/evaluator/backend/adapter, retain transformations/dropped semantics and retry/invalid/reset ledgers, report family scores, and require native-versus-adapted differential tests before preservation claims |
| ToolBench / API-Bank / τ-bench | Tool retrieval, invocation, planning, policy, user interaction, and transaction state | Implemented APIs, databases, policies, simulated users | Calls, responses, database deltas | Call equivalence, response overlap, final state, repeated `pass^k` | Evolution from call syntax to stateful policy/user reliability | Gold-chain bias, synthetic APIs/users, omitted consequences, task defects, and simulator validity |
| OSWorld / OSWorld 2.0 / AndroidWorld | Computer/mobile agents | Desktop VMs or parameterized Android environment | Completed GUI workflows and state | Task-specific execution/state success | Real applications, alternative paths, reset lifecycle, and equivalent-form stress | Environment health, omitted harms, version drift, expensive maintenance; OSWorld 2.0 now has a release-audited full review, while its checkpoint dependence, dynamic-state generation, single-run evidence, safety coverage, and professional-validity limits remain |
| TheAgentCompany / OdysseyBench / OfficeBench / WorkArena++ | Workplace-shaped, history-conditioned, cross-application, and composed workflows | Self-hosted company services and LLM coworkers; office files/dialogue histories; or seeded ServiceNow state | Files, messages, records, and cross-application state transitions | Authored checkpoints or task predicates; WorkArena++ composes setup/oracle/validators with sequential or global semantics | Separates integrated substrate, requirement lineage, action execution, and composition as useful but non-substitutable repairs | Full-paper/later-release audits support strong substrate machinery (TheAgentCompany), inspectable synthetic evidence-to-state lineage (OdysseyBench), and reusable composition (WorkArena++), not occupational sampling, persistent memory, coworker authority, complete consequences, isolated planning, or readiness. Require service/reset identity; availability→access→authority→adoption evidence; intended/collateral deltas; evaluator-dispatch and observer-sufficiency conformance; alternate paths; and bounded claims. OfficeBench remains an audit gap |
| HippoCamp | Multimodal file retrieval and open-ended QA over three contributor-composite personal profiles | 2,000+ files / 42.4 GB; 581 questions with authored support sets and locators | Answers and reported support files; no file mutation or action | Answer-only GPT-4o judge plus overlap with one annotated file set | Makes availability, representation access, entity/time/scope interpretation, and answer acceptance separable | Full v1 paper and one-day-post-v1 release audit support a contextual-QA instrument, not faithful personalization, task-time authorization, privacy safety, causal evidence adoption, consequential computer action, user validation, or readiness; corpus/results/audits were unavailable and alternate support sets are not adjudicated |
| MBABench | End-to-end finance spreadsheet artifacts | Competition/training cases and starting workbooks | Native professional spreadsheets | Static Accuracy/Formula/Format judgments against one reference | Corrects final-cell evaluation by exposing formulas, structure, and formatting | How should counterfactual recalculation, rendered charts, task delta, and alternative valid models be tested? |
| AIDABench | Document analysis agents | Heterogeneous documents | Analysis outputs | End-to-end pipeline checks | Useful for document-heavy source pools | How to evaluate evidence use? |
| SaaS-Bench | Real deployable SaaS workflows | 23 open-source SaaS systems, multimodal inputs, persistent app state | Cross-application task completion | Weighted verification checkpoints + resolved score | Strong model for professional workflow realism and partial-credit state checks | Can we borrow checkpoint scoring without inheriting heavy environment maintenance? |
| LH-Bench | Subjective enterprise long-horizon work | Real Figma files, course data rooms, expert-authored `SKILL.md` procedures | Front-end implementations, programmatic content artifacts | Skill-grounded rubrics, artifact contracts, human pairwise preferences | Shows expert procedural knowledge can be the bridge between execution guidance and evaluation criteria | How should skill-bench separate public skills from private verifier/rubric contracts to avoid leakage? |
| AlphaEval / industrial expertise codification | Production-demand projection and codified-rule package efficacy | Private partner requirements/files; or proprietary simulation data, expert rules, manuals, and examples | Professional task packages and agent artifacts; or visualization scripts/plots | Heterogeneous automated rubric/check aggregates; or mixed-rater ordinal artifact judgments | Together expose the full demand→elicitation→codification→projection→configured-intervention→measurement chain | Full reviews support prospective demand/co-design and bounded package effects only. Seven purposive partners with private AlphaEval tasks/results, nonfactorial packages, and score×wage arithmetic do not establish occupational coverage, scaffold causality, readiness, or value. Five selected Siemens cases, two experts, task–rule–criterion overlap, no component ablations, and no rater reliability do not establish tacit transfer, expert equivalence, or cross-domain generalization |
| Workflow-GYM | Professional GUI workflows | Configured VMs with domain-specific professional software | Final GUI state / produced artifacts | Deterministic final-state or artifact success criteria | Reinforces that long-horizon professional work fails through stage omission, objective drift, and software-specific knowledge gaps | Which professional GUI tasks can be approximated with lighter open-source or file-based environments? |
| STRACE / trajectory diagnosis | Long-horizon agent failure optimization | Execution traces and dependency graphs | Root-cause module updates / diagnostic slices | Success-rate lift after localized optimization | Suggests benchmark logs should support causal failure slicing, not just final scoring | What minimal trace schema lets us diagnose planner vs retrieval vs artifact failures? |
| Efficient Benchmarking / Agent Psychometrics | Low-cost, calibrated agent evaluation | Per-task response matrices, task artifacts, model/scaffold metadata | Reduced task panels, predicted difficulty, component ability estimates | Rank fidelity, AUC-ROC, IRT-style difficulty/ability models | Shows that benchmark operation needs psychometric infrastructure: pass-rate histories, mid-difficulty panels, and scaffold-aware reporting | Can artifact-heavy knowledge-work rubrics be reduced at the rubric-check level without losing diagnostic coverage? |
| ClawsBench | Productivity agents + safety | Simulated workspace services | API actions / task completion | State-based task success and safety | Important for productivity-agent risks | How to include safety and prompt injection? |
| SWE-bench / Terminal-Bench | Coding / terminal tasks | Repos or terminal envs | Patches / terminal outcomes | Tests | Shows value of executable scoring | What analogs exist for decks/spreadsheets/memos? |
| LiveBench | Rotating broad LLM capability forms under limited public exposure | Recent competitions/articles/datasets plus procedural variants; temporary private slice | Short answers, code, tables, constrained text | Exact/regex/symbolic/executable/task-specific checks | Makes source age, exposure role, form renewal, grader revision, rerun cost, and leaderboard version explicit | Difficulty-conditioned renewal changes the estimand; timestamp is not exposure proof; equivalent-form linkage and grader reliability remain weak |
| MMLU → MMLU-Pro | Broad academic/professional exam knowledge → harder, reasoning-weighted multiple choice | Public static questions; 57 subjects → 14 domains and ten choices | One selected option, optionally with CoT | Exact-match macro/domain accuracy | Preserves a cheap common interface; MMLU-Pro demonstrates renewed headroom and lower tested prompt sensitivity | Difficulty/model-assisted filtering changes the population; subject breadth is not work sampling; hardness and CoT gain do not establish professional reasoning validity |
| HumanEval → LiveCodeBench | Standalone function synthesis → rotating contest problems and generation/repair/execution/output scenarios | Docstrings/tests → timestamped contest statements, programs, inputs, and execution feedback | Python functions/programs or predicted outputs | Hidden tests, exact outputs, pass@k | Functional tests admit alternative implementations; timestamped renewal and plural scenarios expose failures hidden by generation-only scores | Tests observe only encoded consequences; pass@k is budget-conditioned; cutoff dates do not prove non-exposure; rotating difficulty/source mix breaks naive trends |
| PaperBench / PresentBench | Research replication / presentations | Papers, specs | Artifacts | Task-specific / judge scoring | Adjacent artifact-generation benchmarks | How mature are methods? |

The cross-family evolution analysis and retain/repair/test decisions are in
[`concepts/professional-benchmark-evolution-matrix.md`](concepts/professional-benchmark-evolution-matrix.md).
Its central conclusion is that newer professional-work benchmarks repair
different links—occupational frame, source pack, environment, workflow,
artifact/state delta, grader, and lifecycle—but none yet closes the full chain
from professional demand to a licensed readiness claim.

The interactive-family evolution analysis is in
[`concepts/web-tool-computer-benchmark-evolution.md`](concepts/web-tool-computer-benchmark-evolution.md).
Its central conclusion is that interactivity migrates rather than removes the
oracle: syntheticity moves from a reference answer into authored site/database
state, user simulators, task initializers, and selected success predicates.

The grading/validity/lifecycle evolution analysis is in
[`concepts/grading-validity-lifecycle-evolution.md`](concepts/grading-validity-lifecycle-evolution.md).
Its central conclusion is that exact, executable, state, artifact, rubric,
expert, psychometric, validity, and lifecycle systems repair different links;
no observer family dominates, and form or grader renewal is itself a
measurement intervention requiring immutable identity and bridge evidence.

The reasoning/coding evolution analysis is in
[`concepts/reasoning-coding-benchmark-evolution.md`](concepts/reasoning-coding-benchmark-evolution.md).
It shows that adoption often follows a low-friction common interface, while
successor hardness, freshness, executable grading, and larger execution units
repair different links. Difficulty filtering and rolling forms change the task
population; executable checks relocate rather than eliminate the oracle.

## How to use this landscape

This table is an external benchmark-family index, not the project's canonical
schema. The consolidated internal taxonomy lives in
[`benchmark-design-taxonomy.md`](benchmark-design-taxonomy.md), which separates:

1. the expertise-to-task authoring lifecycle;
2. the trial measurement stack;
3. intervention, instrument, and configured-system identity; and
4. task-bank calibration and compounding operation.

New sources should be added above only when they contribute a distinct benchmark
pattern or materially change the evidence for one already listed. Repeated
primitive lists, scoring-layer definitions, and operating rules should update
the canonical taxonomy instead of accumulating in this landscape file. Source-
specific methodology, limitations, and disagreements remain in paper reviews.
