# State-of-the-Art Map

This file tracks benchmark families relevant to `skill-bench`.

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
| ClawsBench | Productivity agents + safety | Simulated workspace services | API actions / task completion | State-based task success and safety | Important for productivity-agent risks | How to include safety and prompt injection? |
| SWE-bench / Terminal-Bench | Coding / terminal tasks | Repos or terminal envs | Patches / terminal outcomes | Tests | Shows value of executable scoring | What analogs exist for decks/spreadsheets/memos? |
| PaperBench / PresentBench | Research replication / presentations | Papers, specs | Artifacts | Task-specific / judge scoring | Adjacent artifact-generation benchmarks | How mature are methods? |

## Emerging taxonomy

### Task horizon

- Single-turn Q&A
- Short tool-use task
- Multi-step workflow
- Multi-day / multi-week scenario
- Persistent institutional context

### Evaluation target

- Answer correctness
- Tool-call correctness
- Environment state change
- Artifact correctness
- Analytical quality
- Presentation quality
- Safety / policy compliance
- Cost/time efficiency

### Domain knowledge conversion primitives

- Hidden requirement
- Contradictory evidence
- Expert caveat
- Decision threshold
- Artifact convention
- Regulatory/compliance constraint
- Stakeholder preference
- Data quality issue
- “Looks good but wrong” trap
