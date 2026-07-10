# State-of-the-Art Map

This file tracks benchmark families relevant to `skill-bench`. For grouped conclusions and explicit source-relevance tiers, start with [`research-synthesis-index.md`](research-synthesis-index.md).

| Benchmark / Area | What it tests | Inputs | Outputs | Scoring | Why it matters for us | Open questions |
|---|---|---|---|---|---|---|
| AA-Briefcase | Long-horizon knowledge work | Emails, Slack, docs, transcripts, spreadsheets, data exports | Spreadsheets, decks, memos, PDFs, mockups, videos | Binary rubrics + pairwise analytical/presentation Elo | Closest inspiration; shows artifact-centered benchmark design | How to build an open/lower-budget version without losing realism? |
| AA-Briefcase-Lite | Public due-diligence example | 147 files across 67 sources | LaTeX/PDF, XLSX, PPTX, MP4/SRT | 63 checks: accuracy, critical insight, analytical quality, presentation | Concrete schema to study and adapt | How much of the structure can be generalized? |
| GDPval / GDPval-AA | Economically valuable professional tasks | Case/task material | Work deliverables | Pairwise comparison / expert anchoring | Demonstrates labor-market relevance framing | What task taxonomy did they use? |
| APEX-Agents-AA | Professional services tasks | Realistic app/workflow dependencies | Task completions | Rubric-based local file grading | Strong adjacent model for professional service workflows | What is reproducible publicly? |
| OSWorld / OSWorld 2.0 | Computer-use agents | Desktop environment | Completed GUI workflows | Task success | Long-horizon GUI realism | How to combine GUI tasks with knowledge-work artifacts? |
| OdysseyBench / OfficeBench | Office application workflows | Word/Excel/PDF/email/calendar | Office workflow completion | Programmatic / task-specific evaluation | Directly relevant to office knowledge work | How robust are evaluation functions? |
| WorkstreamBench / MBABench | End-to-end spreadsheet finance tasks | Finance context and spreadsheet data | Professional spreadsheets | Spreadsheet / finance-specific checks | Useful for artifact testing and spreadsheet grading | Can we make an open finance-lite scenario? |
| AIDABench | Document analysis agents | Heterogeneous documents | Analysis outputs | End-to-end pipeline checks | Useful for document-heavy source pools | How to evaluate evidence use? |
| SaaS-Bench | Real deployable SaaS workflows | 23 open-source SaaS systems, multimodal inputs, persistent app state | Cross-application task completion | Weighted verification checkpoints + resolved score | Strong model for professional workflow realism and partial-credit state checks | Can we borrow checkpoint scoring without inheriting heavy environment maintenance? |
| LH-Bench | Subjective enterprise long-horizon work | Real Figma files, course data rooms, expert-authored `SKILL.md` procedures | Front-end implementations, programmatic content artifacts | Skill-grounded rubrics, artifact contracts, human pairwise preferences | Shows expert procedural knowledge can be the bridge between execution guidance and evaluation criteria | How should skill-bench separate public skills from private verifier/rubric contracts to avoid leakage? |
| Workflow-GYM | Professional GUI workflows | Configured VMs with domain-specific professional software | Final GUI state / produced artifacts | Deterministic final-state or artifact success criteria | Reinforces that long-horizon professional work fails through stage omission, objective drift, and software-specific knowledge gaps | Which professional GUI tasks can be approximated with lighter open-source or file-based environments? |
| STRACE / trajectory diagnosis | Long-horizon agent failure optimization | Execution traces and dependency graphs | Root-cause module updates / diagnostic slices | Success-rate lift after localized optimization | Suggests benchmark logs should support causal failure slicing, not just final scoring | What minimal trace schema lets us diagnose planner vs retrieval vs artifact failures? |
| Efficient Benchmarking / Agent Psychometrics | Low-cost, calibrated agent evaluation | Per-task response matrices, task artifacts, model/scaffold metadata | Reduced task panels, predicted difficulty, component ability estimates | Rank fidelity, AUC-ROC, IRT-style difficulty/ability models | Shows that benchmark operation needs psychometric infrastructure: pass-rate histories, mid-difficulty panels, and scaffold-aware reporting | Can artifact-heavy knowledge-work rubrics be reduced at the rubric-check level without losing diagnostic coverage? |
| ClawsBench | Productivity agents + safety | Simulated workspace services | API actions / task completion | State-based task success and safety | Important for productivity-agent risks | How to include safety and prompt injection? |
| SWE-bench / Terminal-Bench | Coding / terminal tasks | Repos or terminal envs | Patches / terminal outcomes | Tests | Shows value of executable scoring | What analogs exist for decks/spreadsheets/memos? |
| PaperBench / PresentBench | Research replication / presentations | Papers, specs | Artifacts | Task-specific / judge scoring | Adjacent artifact-generation benchmarks | How mature are methods? |

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
