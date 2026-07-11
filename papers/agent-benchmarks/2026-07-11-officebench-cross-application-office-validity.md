# OfficeBench: cross-application execution is not yet professional-work validity

**Source type:** Deep review of the complete immutable arXiv v1 paper and an official acquisition-time repository snapshot  
**Paper:** Zilong Wang et al., *OfficeBench: Benchmarking Language Agents across Multiple Applications for Office Automation* (arXiv:2407.19056v1, 26 July 2024)  
**Immutable paper:** https://arxiv.org/abs/2407.19056v1  
**Local PDF:** `data/papers/pdfs/2407.19056v1-officebench.pdf` (SHA-256 `f5162305716ce6b67326b52150884bdc2d28aaec2553c13938630b4b00fff020`, 16 pages)  
**Local text:** `data/papers/text/2407.19056v1-officebench.txt` (SHA-256 `f8f2f6308bba3942bbaf46b4877dbd29c8d86231cb7be345c82ea098c83d389b`)  
**Official release:** https://github.com/zlwang-cs/OfficeBench  
**Pinned archive:** `data/sources/releases/2407.19056v1-officebench/OfficeBench-b978b808667c32b52ce19a67ce1def1de9ae02b7.tar.gz` (SHA-256 `f78637e82b5a68ab700a35e6aa6277b183550b53ea043e4b530c30016e36999e`)  
**Release provenance:** `data/sources/releases/2407.19056v1-officebench/provenance.json`

> **Timing boundary.** The archived untagged commit `b978b808667c32b52ce19a67ce1def1de9ae02b7` is dated 31 March 2026, well after arXiv v1. It is inspectable official release evidence, not proof of manuscript-time byte identity. Claims below explicitly distinguish the paper from this later snapshot.

## Review judgment

OfficeBench's durable contribution is not proof that agents can do office knowledge work. It is an early, inspectable demonstration that one task can require **stateful transformations across typed office stores**—documents, spreadsheets, calendars, and email—and that final-state predicates can admit more than one action path. This is a useful repair to document-QA benchmarks.

Its central validity limitation is equally important: “number of applications” bundles more actions, longer paths, format conversions, task-family differences, and more output obligations. The reported three-application collapse therefore does not isolate application switching or professional workflow complexity. More fundamentally, many released checks establish only file presence or keyword occurrence. They usually do not establish preservation of unrelated state, artifact usability, recipient correctness, formatting quality, safe side effects, or professional judgment. OfficeBench supports a bounded claim about task-specific predicates in a synthetic API-mediated filesystem—not real-office readiness.

## One-sentence contribution

OfficeBench makes cross-store office state executable and inspectable, but its synthetic task sampling and often narrow final-state checks support task-predicate completion claims rather than professional-work validity.

## Why this matters

It is a useful historical anchor for separating the genuine advance—consequential transitions among typed artifacts and communication stores—from unsupported inferences based on application count, file existence, or programmatic pass rates.

## Contribution details

### Research question

The paper asks whether LLM agents can execute office tasks that exceed extraction/QA by combining information and operations across applications (pp. 1–3). It contributes:

1. a Dockerized transition system with nine named applications and 23 operations;
2. 300 synthetic tasks split into 93 one-app, 95 two-app, and 112 three-app items;
3. per-task conjunctions of exact, containment, file-state, spreadsheet-cell, and calendar-overlap checks;
4. eight model baselines, a two-student human comparison, and a restricted-action-space ablation.

The key methodological advance over document-only evaluation is **cross-store consequential state**: reading one representation can determine mutations in another. The benchmark also preserves the full output testbed for post-hoc checking (paper §3.3, p. 5), which is stronger than scoring only a final textual answer.

## Methodology and system

### Environment and interaction

The paper formulates the current selected application as state and application-specific operations as transitions (§3, pp. 3–5). Agents see full textual action/observation history, select one JSON action per turn, and terminate by submission, five repeated operations, or a stated 50-step limit (pp. 4–5). The environment exposes Word, Excel, PDF, Calendar, Email, OCR, ChatGPT, Shell, and System operations. Inputs live in `/testbed/data`, email accounts in `/emails`, and calendars in `/calendar` (p. 5).

The release confirms a Docker-mediated API environment rather than GUI office applications. `utils/env.py` copies each task testbed and app code into a container, captures the resulting `/testbed`, and records environment and LLM histories. The shell action executes arbitrary commands in the container. The Dockerfile installs LibreOffice and utilities but does not pin its Ubuntu base or package versions and copies an API key into the image. No network-denial policy is evident. Thus the environment is operationally inspectable but mutable and broader than the intended office-action construct.

There is also paper/release configuration drift. The paper states a 50-step ceiling (p. 5); acquisition-time `agent_interact.py` defaults to 20. The release permits a caller override but does not identify the exact manuscript commands/configuration. It stores no paper-result trajectories in the archived tree sufficient to replay Table 2.

### Task construction and coverage

Annotators brainstormed tasks for application pairs, then expanded two-app tasks with a relevant third application (§4.1, pp. 5–6). Documents and records were generated with ChatGPT and random generators rather than sampled from observed work (§4.2, p. 6). The release contains all 300 JSON task records across 167 task directories, matching the paper's 93/95/112 split. An audit found:

- 290 records use date `2020-05-01`, seven use `2024-05-01`, and three use `2022-11-01`;
- 193 identify Alice, 104 Bob, and three Jack;
- 297 label the weekday Friday, including the seven 2024 dates (1 May 2024 was not Friday); only the three 2022 records say Tuesday.

These are not merely cosmetic defects when relative-time phrases and calendars are part of the construct. The suite has neither a professional task-sampling frame nor evidence that app-count strata represent increasing versions of the same construct. Three-app tasks are authored extensions, not matched counterfactuals.

### Evaluation

The paper describes exact, fuzzy, and execution-based methods (§4.3, p. 6; Appendix D, p. 14). The later release makes the actual semantics inspectable: each item passes only if every configured predicate returns true, so the reported task score is binary—not partial credit. Across 300 records, the audit counted 601 predicate invocations:

| Predicate | Invocations |
|---|---:|
| containment | 279 |
| file exists | 233 |
| spreadsheet-cell value | 37 |
| negative containment | 19 |
| spreadsheet exact match | 18 |
| calendar no-overlap | 6 |
| diff contains text | 6 |
| file absent | 2 |
| spreadsheet-cell comparator | 1 |

There are 155 one-check tasks; 54 tasks use only file-existence/nonexistence predicates. `evaluate_contain` lowercases extracted text and accepts substring presence anywhere. `evaluate_file_exist` checks only path existence. Spreadsheet “exact match” compares cell values on the active sheet, not formatting, formulas-as-calculation, charts, workbook structure, or downstream usability. Conversely, strict cell/reference equality can reject legitimate alternative layouts. Calendar overlap is checked only where explicitly configured. No general invariant prevents deletion or corruption of unrelated files, emails, or events.

This yields an important distinction: **alternative action paths are generally allowed, but alternative professionally valid artifacts are inconsistently allowed**. Outcome predicates avoid trajectory imitation, yet their evidence views are often too weak. A generated JPEG can pass on existence alone; a report can pass with required keywords despite contradiction or unusable structure; an email check can ignore attachments, recipient policy, or collateral messages unless a task author happened to encode them.

The evaluator uses Python `eval` both to dispatch configured function names and, for the comparator, to execute a lambda from task JSON. This is acceptable only for trusted benchmark packages and should not be generalized to contributed packs without code isolation and signed/allowlisted graders.

## Evidence and results

Table 2 reports one pass/fail result per task for each configured model: GPT-4o reaches 47.00% overall (64.52/60.00/21.43% for one/two/three apps); the human figure is 93.33% (96/96/88%) (p. 7). The paper says two computer-science graduate students performed the tasks, but does not state assignment, repetition, adjudication, timing, tool familiarity, or uncertainty. It reports no confidence intervals and no repeated stochastic trials.

The app-switch ablation compares a restricted current-app action space with listing all operations. GPT-4o changes from 44.33% to 47.00%; Llama 3 from 25.57% to 27.33% (Table 3, p. 7). Token means exclude stagnation and overflow failures (footnote 3, p. 8), making them outcome-conditioned cost summaries. No paired uncertainty or run replication is reported. Because the treatment changes both prompt length and action availability, it tests the configured interface package, not application switching alone.

The error analysis gives three illustrative trajectories—redundant repetition, nonexistent actions, and failure to convert a PDF before editing (p. 8). It provides no coded sample, frequencies, independent raters, or root-cause protocol. The paper's attribution of lower multi-app scores to cross-application planning is therefore plausible diagnosis, not identified causal evidence.

## Unique insight

OfficeBench reveals that **application identity is a weak proxy; typed state transitions are the stronger reusable unit**. A workflow is not difficult because it names three apps. It is difficult because information must cross representation boundaries while preserving authority and invariants: PDF→text extraction, spreadsheet→decision, decision→calendar mutation, calendar→recipient communication. This reframing travels across domains and avoids reducing skill-bench to office automation.

The benchmark also exposes a two-sided grading problem:

- checking only final state appropriately avoids requiring one canonical procedure;
- but a narrow final-state view cannot detect collateral damage, invalid provenance, unsafe communication, or an artifact that is technically present but unusable.

The repair is not mandatory trajectory matching. It is a **state-delta contract**: required mutations, permitted mutations, forbidden collateral changes, preserved invariants, authoritative representations, and handoff-usability checks, plus selective trace evidence for provenance and diagnosis.

## Limitations and validity threats

1. **Construct confounding.** App count covaries with task family, number of obligations, path length, action count, conversions, and source/output formats. No matched task ladder isolates switching.
2. **Synthetic ecological validity.** Tasks were brainstormed and data generated; no observed workplace workflow, domain expert authoring, recipient study, or consequential handoff validates “realistic” or “human productivity” claims.
3. **Weak artifact evidence.** Fifty-four released tasks can pass on file-state existence alone. Keyword checks ignore coherence and provenance; active-sheet cell checks ignore much artifact structure.
4. **Collateral effects undermeasured.** Most tasks do not specify preserved files/events/messages. Destructive side effects are visible in the captured testbed but largely unscored.
5. **No path/process validity.** Full histories are retained, but scoring uses final predicates. The benchmark cannot distinguish retrieval, transformation, decision, mutation, verification, and communication failures without manual reconstruction.
6. **Reliability absent.** Single attempts, no task-clustered uncertainty, no stochastic replication, and an under-described two-student human comparison.
7. **Mutable configuration.** Unpinned base image/dependencies, network-capable shell, changing APIs, no paper commit, 50-versus-20 step discrepancy, and absent result trajectories prevent exact reproduction.
8. **Temporal and metadata defects.** Date/weekday inconsistencies can alter relative-time semantics.
9. **Safety gap.** Email/calendar operations are consequential mutations, but no authorization, recipient-boundary, confirmation, or rollback scoring is reported.
10. **Contamination/adoption limits.** Public tasks and graders enable direct memorization. The paper offers no refresh/private split. The paper motivates influence as an early predecessor, but supplies no adoption evidence; reuse by a successor should be recorded separately rather than treated as validity.

## Reproducibility and operational realism

**Inspectability: moderate.** The official snapshot includes 300 task records, source packs, app adapters, evaluator code, Docker setup, and runner code. It permits static audits of task/check semantics.

**Exact reproducibility: low.** The paper does not pin a commit, package/image digests, provider parameters, seeds, per-trial outputs, or complete costs. The acquired commit is post-paper. External model APIs and the in-environment LLM app are mutable; the Docker base is `ubuntu:latest`; network is not evidently disabled.

**Operational realism: bounded.** Real file formats and persistent stores are manipulated, but through purpose-built textual APIs, mostly synthetic content, broad shell access, and no organizational permissions or human handoff. The system measures an API-mediated office-state sandbox, not GUI competence or professional readiness.

## Transferable benchmark relevance to skill-bench

### Retain

- Tasks that cross typed source and destination stores.
- Full task-scoped output-state capture.
- Per-task deterministic predicates where the predicate's evidence view is sufficient.
- Outcome-based grading that admits alternative procedures.
- Explicit termination and resource ceilings.

### Repair

1. Replace app count with typed transition descriptors: source representation, transformation, decision, destination mutation, recipient/handoff, and preservation obligations.
2. Pair matched tasks that vary one transition while holding requirements, source pack, and output obligations fixed.
3. For every task, declare required, permitted, and forbidden state deltas plus preserved invariants; fail on collateral mutations.
4. Bind each check to an authoritative artifact view and evidence sufficiency. File existence cannot support content or usability claims.
5. Score plural dimensions separately: task correctness, artifact integrity, communication/authorization, side effects, process diagnosis, cost, and handoff usability.
6. Record image/package/tool hashes, network policy, shell policy, step budget, reset evidence, seeds, traces, and retries as configured-system identity.
7. Use repeated trials and task-clustered uncertainty; never infer transition effects from heterogeneous app-count strata.
8. Add expert and recipient validation before licensing “professional” or productivity claims.

These requirements already have homes in the benchmark-bundle, artifact-view admissibility, execution-validity, task-health, metric-monitoring, validity-argument, and handoff-usability work. No new queue task is warranted.

## Concrete changes

1. **Consolidation:** when the workspace-family synthesis next updates, use OfficeBench as a historical anchor for the distinction between cross-application labels and typed state-transition validity; compare with OdysseyBench only after its source/release audit and preserve different environment/evaluator scopes.
2. **Validation:** extend an existing cross-domain handoff/state conformance slice—not a new office pilot—with a planted collateral mutation and a plausible-but-unusable artifact. Require the grader to separate required delta, preserved state, and recipient usability.
3. **Task authoring:** prohibit app count as a standalone difficulty claim; require evidence that a difficulty knob changes one declared transition burden or estimate it as a bundled configured-task contrast.
4. **Release operation:** record public exposure and retire/refresh policy for any openly released task/check pair.

## Claim boundary

OfficeBench v1 provides evidence that selected 2024 model-agent configurations often failed deterministic predicates on 300 synthetic API-mediated office-state tasks, and that performance was lower in the heterogeneous three-app stratum. It does **not** establish general office-work capability, professional artifact quality, safe autonomous operation, human-level comparison, a causal application-switching effect, or deployment readiness.