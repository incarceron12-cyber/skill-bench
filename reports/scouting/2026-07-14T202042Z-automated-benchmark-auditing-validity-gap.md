# Scouting note — automated benchmark-auditing validity gap

**Timestamp:** 2026-07-14T20:20:42Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 224 tasks: 218 completed, four blocked, and two pending human decisions; no source/research/review task remained. Existing work covers task health, environment validity, tool-evaluator disagreement, verifier hardening, and benchmark lifecycle, but no local review or queue task evaluates automated cross-benchmark defect auditing and the validity of score/rank changes after defect-based filtering.

## Substantive finding (triage only)

**Automated Benchmark Auditing for AI Agents and Large Language Models**

- Immutable record selected for review: https://arxiv.org/abs/2605.26079v2
- Immutable PDF: https://arxiv.org/pdf/2605.26079v2
- Immutable HTML: https://arxiv.org/html/2605.26079v2
- Official repository: https://github.com/IsThatYou/auto-bench-audit
- The arXiv API identifies Junlin Wang, Federico Bianchi, Shang Zhu, Fan Nie, Yongchan Kwon, Bhuwan Dhingra, and James Zou; v1 was submitted 25 May 2026 and v2 on 26 May 2026 in `cs.CL`. The summary contains no withdrawal notice, and the versioned abstract, PDF, and HTML returned HTTP 200.
- The **v2 abstract** introduces Auto Benchmark Audit (ABA), an agentic task-level auditor for hidden environment dependencies, specification gaps, and limited grading logic. It reports auditing 168 benchmarks across nine domains, issues in more than 25.7% of evaluated tasks, expert and upstream-PR corroboration, and score increases of 9.9% and 9.6% after filtering flagged SWE-bench Verified and Terminal-Bench 2 tasks. These are author-reported abstract claims, not independently verified findings.
- The abstract's wording makes several denominators and estimands ambiguous at triage: 168 is described as benchmarks while the issue rate is over evaluated tasks; “critical,” “precision,” and “validated” require exact definitions; and score changes after removing flagged items can reflect altered difficulty/composition rather than corrected capability measurement. Full review must reconstruct sampling, issue units, severity, human review, false-negative coverage, filter policy, paired model/task matrices, uncertainty, and rank sensitivity.
- The official GitHub repository is a non-fork project created 25 May 2026 with no API-reported license, tags, or releases. Current `main` resolves to commit `f74341939a0dbb7a67fe1643609214f4e546df87` dated 27 May 2026, after arXiv v2. It must be audited as a post-v2 artifact unless paper-time identity can be recovered; no repository files or annotations were inspected during scouting.
- Repository-wide duplicate search found no arXiv `2605.26079` record. The closest completed review audits tool-calling evaluator disagreement on selected BFCL tasks; adversarial-verifier work asks whether graders accept hacks. ABA instead claims a general pre-measurement audit pipeline across task specifications, environments, ground truths, and grading logic, then studies score sensitivity.
- This is **metadata, abstract, URL, release-location, and duplicate triage only**. The full paper, appendices, prompts, issue records, benchmark/task sampling, code, expert-review protocol, upstream PRs, score matrices, and cost evidence were not read or audited. No claim is made that ABA findings are correct, complete, representative, causally validated, or suitable as automatic task-admission decisions.

## Benchmark implication to test

Benchmark maintenance needs a typed defect lifecycle: `immutable task/form/environment/grader identity → audit configured system and admissible evidence view → candidate issue/category/severity → independent human or upstream corroboration plus disagreement → false-positive/false-negative evidence → quarantine/repair/retain decision → versioned revalidation → score/rank sensitivity under common-task and changed-composition estimands → bounded claim update`. Auditor output is evidence for review, not ground truth; removing flagged tasks can silently change the construct, difficulty distribution, and population.

A full review should test whether ABA separates task ambiguity from legitimate alternative paths, environment failure from solver failure, incorrect truth from incomplete check coverage, and auditor uncertainty from confirmed defects. It should preserve task-level paired outcomes before and after correction, distinguish filtering from repair, inspect expert qualifications/blinding/overlap/adjudication, and report whether upstream acceptance validates the issue or only a code change. Existing task-health, validity, metric, projection, and lifecycle machinery should host any transfer; no ABA-specific schema follows from triage.

## Charter decision filter and queue action

- **Objectives advanced:** A (benchmark-operation frontier), B (task-defect-to-score-claim validity), and C (evidence for executable task-health and lifecycle checks).
- **Evidence/artifact sought:** immutable-v2 deep review, exact post-v2 release audit, and at least one recomputed issue or score-sensitivity result if released artifacts permit.
- **Uncertainty clarified:** when an automated audit finding justifies quarantine, repair, or historical-score qualification, and when defect filtering merely changes benchmark composition.
- **Mode/balance:** one low-priority review task restores a minimal research backlog while blocked empirical work awaits Git authentication; no broad search or parallel source bundle was added.
- **Duplication/scope:** complements tool-evaluator and verifier audits; coding/terminal suites are measurement cases, not a permanent benchmark scope.
- **Useful completion:** preserve benchmark/task sampling, issue denominators and severity, auditor identity/evidence views, expert review and missed-defect limits, corroboration, remediation states, score/rank estimands, release drift, cost, and strict claim ceilings.

Added `review-auto-benchmark-audit-task-defect-validity` (priority 22). No second task was added.

## Operational note

The required initial `git pull --ff-only` could not authenticate to the HTTPS GitHub remote (`could not read Username`). Local `main` was 26 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
