# Scouting note — HealthAdminBench workflow-projection gap

**Timestamp:** 2026-07-16T16:05:14Z

**Evidence status:** metadata/abstract and release-endpoint triage only; the paper and repository have **not** been deeply read in this scouting run.

## Substantive candidate

**HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks** — Suhana Bedi et al., arXiv:2604.09937v1.

- Immutable record: https://arxiv.org/abs/2604.09937v1
- Immutable PDF (HTTP 200, `application/pdf`): https://arxiv.org/pdf/2604.09937v1
- Official release (HTTP 200): https://github.com/som-shahlab/health-admin-bench
- Release HEAD verified with `git ls-remote`: `e71a8f4d6923037805b7f51fbbf608d12ea56cf5` on `main`; GitHub reports Apache-2.0.
- arXiv API metadata: submitted/updated 2026-04-10; no withdrawal notice in the summary.

The abstract reports four GUI environments (EHR, two payer portals, fax), 135 expert-defined tasks across prior authorization, appeals/denials, and DME processing, and 1,698 fine-grained evaluation points. It also reports a marked difference between best end-to-end task success (36.3%) and best subtask success (82.8%). These figures are author claims awaiting full-paper and release verification.

## Why this is a narrow, useful gap

The corpus covers GUI/state benchmarks, synthetic healthcare workflows, expert-authored tasks, and reliability separately, but repository-wide search found no `HealthAdminBench`, `2604.09937`, or official-release entry. This source directly exposes a missing cross-domain transformation chain:

`observed professional workflow → expert-defined task → GUI state/action path → dependent subtask checks → end-to-end outcome`

A full audit can test whether shadowing and expert involvement leave inspectable requirement/authority lineage, whether fine-grained checks represent necessary workflow dependencies rather than a compensatory checklist, and whether the subtask/task gap diagnoses compounding failure or merely reflects aggregation. Healthcare administration is a bounded high-stakes stress case for reusable projection, observer, dependency, reset, privacy, and claim-validity machinery—not a proposed benchmark scope.

## Queue action

Added one review task: `review-healthadminbench-workflow-projection-validity` (priority 86). It requires immutable full-text acquisition, a pinned release audit, paper↔release conformance, and strict claim ceilings for occupational capability, safety, reliability, economic value, production fitness, and readiness.
