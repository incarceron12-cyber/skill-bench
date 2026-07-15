# Scouting note — Claw-Eval multichannel trajectory-validity gap

**Timestamp:** 2026-07-15T03:22:22Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 248 tasks (241 completed, four blocked, three pending), with only one pending consolidation task executable by a worker and no pending source/research/review work. Existing reviews separately cover trajectory-judge reliability, prompt-injection safety, repeated-trial reliability, execution isolation, and workspace evidence, but not this released benchmark's combined multichannel observer and perturbation design.

## Substantive finding — triage only

**Claw-Eval: Towards Trustworthy Evaluation of Autonomous Agents** — Bowen Ye et al., arXiv:2604.06132v3.

- Immutable record: https://arxiv.org/abs/2604.06132v3
- Immutable PDF: https://arxiv.org/pdf/2604.06132v3
- Official repository: https://github.com/claw-eval/claw-eval
- The arXiv API identifies v3, updated 7 May 2026, in `cs.AI`, with no withdrawal notice. The abstract reports 300 human-verified tasks across nine categories, 2,159 rubric items, three evidence channels (execution traces, audit logs, and environment snapshots), controlled evaluation of Completion/Safety/Robustness, and three repeats summarized with Average Score, Pass@k, and Pass^k.
- The abstract further reports that trajectory-opaque evaluation missed 44% of safety violations and 13% of robustness failures detected by the authors' framework, and that Pass@3 could remain stable under error injection while Pass^3 fell by as much as 24 percentage points. These are author-reported abstract claims, not independently verified findings.
- GitHub API metadata confirmed that the linked repository exists and is active, but it currently exposes no GitHub tags or releases. Any review must therefore pin an inspected commit and distinguish immutable-paper claims from mutable-release evidence.
- Repository-wide duplicate search found no Claw-Eval review, queue task, or scouting note.
- This is **metadata, abstract, URL, release-location, and duplicate triage only**. The paper, appendices, tasks, rubrics, trajectories, perturbations, graders, result tables, and repository contents were not read or audited during scouting. No claim is made that the tasks are professionally valid, that the three channels are independent or sufficient, that detected violations are true violations, or that the reported results establish safety, robustness, reliability, capability, or deployability.

## Why this is distinct

The corpus already asks whether model judges agree with labels (AgentRewardBench), whether injections cause attempted or realized harm (ClawSafety), whether repeated outcomes are stable (Agent Reliability Profile), whether launcher state is reproducible (Harness-Bench), and whether workspace access/mutation is observable (Workspace-Bench). Claw-Eval appears to connect these concerns in one inspectable benchmark: multiple evidence views, trajectory-aware criteria, controlled perturbations, and repeat-sensitive metrics.

The unresolved validity question is whether an additional observer channel supplies independent evidence about a criterion, or simply expands an authored detection surface that shares the same task/rubric assumptions. Likewise, Pass@k and Pass^k answer different descriptive questions but do not alone identify an operational reliability distribution, robustness mechanism, safety consequence, or deployment threshold. A full audit should reconstruct channel admissibility and dependence, human-verification authority, grader dispatch, perturbation matching, missing/invalid trials, uncertainty, and the exact denominator behind every miss-rate claim.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent and production-evaluation evidence), B (plural observation and validity of task-to-check transformations), and C (trace, grader, perturbation, metric, and reliability machinery).
- **Concrete evidence/artifact:** an immutable v3 full-paper review plus a commit-pinned audit of the official release, with exact task/rubric/channel/perturbation/trial denominators and comparison to local reviews.
- **Uncertainty clarified:** whether multichannel trajectory grading and three-repeat perturbation results support bounded observer-increment and configured-consistency claims rather than safety, robustness, or deployability promotion.
- **Mode:** narrow expansion feeding later consolidation/validation; no Claw-specific or software-agent scope commitment.
- **Duplication check:** no exact repository coverage; comparisons are explicitly required against adjacent completed reviews.
- **Useful completion:** evidence-grounded retain/repair/test implications and claim ceilings, not acceptance of abstract metrics.

Added one task: `review-claw-eval-multichannel-trajectory-validity` (priority 20). No second task was added.
