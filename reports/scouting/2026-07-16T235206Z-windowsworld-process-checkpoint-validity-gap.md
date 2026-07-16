# Scouting note — WindowsWorld process-checkpoint validity gap

- **Timestamp:** 2026-07-16T23:52:06Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv-HTML outbound-link inspection, ACL Anthology endpoint verification, official repository metadata/current README triage, Git ref/API checks, and local corpus/queue duplicate searches only. The PDF/ACL paper body, `benchmark.json`, task-generation evidence, checkpoint definitions, evaluator implementation, environment/reset code, and reported trials were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments** — Jinchao Li, Yunxin Li, Chenrui Zhao, Zhenran Xu, Baotian Hu, and Min Zhang, arXiv:2604.27776v1; Findings of ACL 2026.

- Immutable record: https://arxiv.org/abs/2604.27776v1
- Immutable PDF: https://arxiv.org/pdf/2604.27776v1
- ACL Anthology record: https://aclanthology.org/2026.findings-acl.750/
- Official release: https://github.com/HITsz-TMG/WindowsWorld
- The arXiv API reports one version submitted 30 April 2026 in `cs.HC`/`cs.AI`, with no withdrawal notice in the abstract. Versioned abstract, PDF, and HTML endpoints and the ACL Anthology record returned HTTP 200.
- The abstract describes 181 simulated Windows tasks steered by 16 occupation labels, four difficulty levels, intermediate inspection, human refinement, 17 applications, an average five subgoals, and 78% multi-application tasks. It reports success below 21%, early stalling on tasks involving at least three applications, and step counts above human limits. These are author claims awaiting full-paper and release verification.
- The paper HTML links the non-fork official repository. `git ls-remote` and the GitHub API resolved current `main`/HEAD to `fbccd464f94fec9e284e139f97bf96d0b192f580`, committed 11 May 2026 after arXiv v1. The Apache-2.0 repository root exposes `benchmark.json`, desktop-environment, monitor, agent, runner, result-display, installation, and requirements artifacts. README triage claims 181 tasks, 77.9% multi-app tasks, and 4.97 intermediate checkpoints per task, and states that substantial evaluation machinery derives from OSWorld. Package completeness, exact paper correspondence, reset correctness, observer validity, and result reproducibility were not established in scouting.

## Why this is a narrow, useful gap

The reviewed corpus already covers OSWorld 2.0, OfficeBench, Workflow-GYM, WorkArena L1/++, AutomationBench, and HealthAdminBench. Exact title/ID searches found WindowsWorld only as a citation in the acquired OSWorld 2.0 paper, with no review, queue task, or prior scouting note. Its distinct question is whether intermediate state checkpoints across applications improve process diagnosis without silently imposing one authored route:

`source requirement and occupation frame → generated/refined task → ordered or partially ordered subgoals → cross-application state transitions → intermediate checkpoint observations → terminal and collateral state → process/endpoint score → professional-work claim`.

Checkpoint credit can reveal where a run stopped, but it need not establish that every checkpoint is necessary, independent, correctly ordered, or semantically sufficient. A valid alternative route can fail path-shaped checks; an upstream miss can mask descendants; preserved intermediate state can be reversed before completion; app count can be confounded with horizon, difficulty, information load, and step budget; and a simulated Windows VM plus occupation label does not establish professional demand, acceptance, reliability, or readiness. Windows GUI work is a bounded substrate for a general workflow-observability question, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic benchmark frontier) and B (expertise/workflow-to-evaluation methodology).
- **Concrete evidence:** immutable-v1/ACL full-paper review plus exact-commit audit of the public task/check/environment package and zero-call static invariants where feasible.
- **Uncertainty clarified:** whether process checkpoints represent meaningful, alternative-aware workflow progress; whether cross-app comparisons isolate coordination; and what occupation/professional claims the source, human-review, environment, and observer evidence licenses.
- **Mode:** narrow expansion feeding comparative validation. Before addition the queue had one pending consolidation, one human prerequisite, no pending review/research/source task, and three blocked builds.
- **Duplication/scope check:** nearest reviews cover endpoint state, composed workflows, checkpointing, and dependency masking, but none audits this exact 181-task WindowsWorld release or its progress-centric scoring. No GUI-, Windows-, or occupation-specific subsystem is proposed.
- **Useful completion:** reconcile paper/release units and denominators; inspect task generation and human authority; reconstruct checkpoint dependencies, weighting, terminal rechecks, alternative routes, collateral-state coverage, environment failures, step budgets, missingness, and run aggregation; compare the claimed repair against nearby benchmark families; and preserve bounded claim ceilings.

Added one task: `review-windowsworld-process-checkpoint-validity` (priority 8). No full-paper, implementation-correctness, professional-validity, planning, reliability, safety, or readiness claim was made during scouting.
