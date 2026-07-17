# Scouting note — LQCDMaster expert-skill and executable-science validity gap

- **Timestamp:** 2026-07-17T22:51:19Z
- **Evidence status:** arXiv API metadata/abstract, arXiv HTML link triage, GitHub repository metadata, and recursive-tree triage only. The paper body, appendices, Skills, benchmark tasks, expert implementations, trajectories, numerical outputs, timing records, or claimed scientific case studies were **not** deeply read, downloaded, recomputed, or executed during scouting.

## Substantive candidate — triage only

**LQCDMaster: Agentic Scientific Computing for Lattice Quantum Chromodynamics Research** — arXiv:2607.15001v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.15001v1 · https://arxiv.org/pdf/2607.15001v1 · https://arxiv.org/html/2607.15001v1
- Official repository linked by the arXiv HTML: https://github.com/sjtu-sai-agents/LQCD_Master at inspected commit [`e4a443e08d5904371fc280ce93c00ff84df21893`](https://github.com/sjtu-sai-agents/LQCD_Master/commit/e4a443e08d5904371fc280ce93c00ff84df21893), committed 16 July 2026.
- The arXiv API identifies a v1 submitted and last updated 16 July 2026. Its summary contains no withdrawal or retraction notice.
- The abstract describes a tool-augmented, skill-guided system that turns natural-language lattice-QCD requests into PyQUDA measurement code, job-submission artifacts, logs, and numerical outputs. It attributes algebraically fragile operations partly to a deterministic Wick-contraction tool and claims evaluation on 70 tasks: 63 exact reproductions of expert implementations at machine precision, three further convention mismatches, hours-to-minutes implementation-time reduction, and novel exploratory computations. These are author-stated abstract claims awaiting full-paper and artifact verification.
- GitHub API inspection found a public, unarchived, non-fork repository with no declared license, 9,074 recursive-tree objects, and a large empirical surface: 175 `benchmark/` objects, 22 `skills/` objects, and 8,759 `experiments/` objects. Visible paths include natural-language tasks, expert/reference benchmark scripts and outputs, five Skill directories, prompts, plans, trajectories, generated code, scheduler logs, numerical outputs, and model-specific experiment directories. This establishes unusually inspectable release material, not paper/release conformance, expert authority, successful recomputation, or scientific validity.
- Exact ID/title/mechanism searches found no local review, queue task, or scouting note. BrainPilot and ReasFlow cover adjacent domain scaffolds and scientific agents, while Opti-Agent-Bench and scientific-workspace reviews cover executable cross-artifact chains; none directly audits expert Skill → deterministic algebra tool → generated HPC workflow → expert numerical equivalence → convention-sensitive result claims.

## Why this is a narrow, useful gap

The relevant chain is:

`research request and domain authority → expert Skill source/review/version → Skill eligibility/loading/adoption → deterministic algebra-tool scope → generated code/job artifacts → environment and execution provenance → numerical output → expert-reference identity and tolerance → convention identity or admissible equivalence → scientific interpretation → novelty/utility/time claim`.

This source is unusually direct for the charter because the benchmark unit is an executable professional-scientific artifact chain rather than a final answer, and the reported failures include convention mismatches that may be either substantive errors or legitimate alternate formulations. Machine-precision agreement can validate one pinned implementation/output relation while still leaving task sampling, expert authority, hidden shared code, environmental reproducibility, alternative-path admissibility, physical correctness, time accounting, novelty, and downstream scientific judgment unresolved. A release audit can test whether the unusually rich repository closes those links or merely makes author-selected runs inspectable.

Lattice QCD is a bounded stress case for reusable expertise-transfer, executable-artifact, environment, alternative-path, and validity machinery—not a proposal to narrow `skill-bench` to physics or scientific computing.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier domain-agent and scientific benchmark evidence), B (expertise-to-Skill and convention-sensitive evaluation), and C (executable artifact/state, trace, environment, and release records).
- **Concrete evidence:** immutable-v1 full-paper review plus a pinned audit of Skills, expert/reference tasks, generated workflows, execution records, numerical comparisons, convention-mismatch adjudication, timing evidence, and scientific case-study artifacts.
- **Uncertainty clarified:** when expert-guided workflow reproduction supports configured conformance, expertise transfer, implementation correctness, scientific validity, labor savings, novelty, or readiness; and how legitimate convention alternatives should be represented without weakening fail-closed grading.
- **Mode:** narrow expansion. The queue has three pending tasks but no autonomous review/source/build task; one review restores a small evidence path without restarting broad search.
- **Duplication/scope check:** adjacent reviews cover separate links, not this exact released end-to-end numerical workflow and expert-equivalence claim. Reuse existing contracts; add no physics-specific schema or pilot.
- **Useful completion:** page/path-grounded reconstruction of Skill authority and realization, deterministic-tool boundary, task/reference provenance, environment and trial denominators, exact comparison procedure, convention mismatches and alternative paths, released-result conformance, time/cost accounting, novelty evidence, and bounded retain/repair/test implications.

Added one task: `review-lqcdmaster-expert-skill-executable-science-validity` (review, priority 59). No other candidate was queued.
