# Scouting note — broad expert-task and living-benchmark validity gap

**Timestamp:** 2026-07-10T22:08:13Z  
**Scope:** Narrow search against charter objectives A/B/C/F after confirming no pending source/research/review work and two legitimately blocked builds. This run targeted broad expert-contributed executable task construction and living-benchmark governance rather than repeating general knowledge-work benchmark discovery.

## Substantive finding (triage only)

**Agents' Last Exam (ALE)**

- Immutable arXiv record: https://arxiv.org/abs/2606.05405v1
- Immutable PDF: https://arxiv.org/pdf/2606.05405v1
- Paper-linked official repository: https://github.com/rdi-berkeley/agents-last-exam
- Repository HEAD observed during scouting: `186691830cd6906a405cb997b39bc5f5ca82e2a4`
- Official project/documentation: https://agents-last-exam.org/docs
- arXiv and official search records describe a long-horizon benchmark of economically valuable, real-world tasks developed with 250+ industry experts, organized across 13 industry clusters and 55 subdomains, with a continuously growing corpus and a public subset.
- The verified official Git repository describes an open `ale_run` framework that provisions sandboxes, runs agents, grades outcomes, and includes roughly 150 public tasks plus reference harness integrations. `git ls-remote` independently verified the repository and observed HEAD above.
- This is **metadata, abstract, documentation-snippet, and release-location triage only**. The full paper, tasks, graders, runner, and repository were not read during scouting. Counts differ across mutable official snippets (1,000+, 1,500+, and approximately 150 public tasks), making immutable-paper versus release-time denominators an explicit review requirement rather than a fact to reconcile here.

## Why this is distinct

The corpus already covers broad expert-authored occupational deliverables (GDPval), expert procedures (LH-Bench), deployable stateful workflows (SaaS-Bench/Workflow-GYM), and session-derived tasks (EnterpriseClawBench). ALE appears to combine several of these at larger occupational breadth with executable verification, tiered difficulty, a public runner, and an explicitly living task pool. The nonduplicate issue is whether that combination preserves expert authority, fair and path-flexible verifiability, configured-system comparability, coverage denominators, and stable score meaning as tasks and public exposure change.

The reusable question is not whether skill-bench should adopt ALE's taxonomy or become a leaderboard. It is how a broad expert-contribution program can turn diverse professional workflows into reproducible, verifiable agent tasks while bounding occupational/economic claims and maintaining version, leakage, and renewal records.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent evaluation), B (expert knowledge into tasks and verifiers), C (executable tasks/graders/runners), and F (large-scale expert participation).
- **Evidence/artifact sought:** immutable-v1 full-paper review, pinned official-release audit, and three end-to-end public task traces from different industry clusters.
- **Uncertainty clarified:** expert recruitment and authority; task realism and alternative valid paths; verifier necessity/sufficiency; public/private coverage; environment validity; difficulty tiers; suite-to-occupation inference; and living-benchmark version/leakage governance.
- **Mode/balance:** one narrow expansion task at priority 67. Existing blocked tasks retain their real prerequisites.
- **Duplication/scope:** repository search found no local index entry, review, queue task, or scouting note for `2606.05405` or Agents' Last Exam. GDPval is the nearest comparison but lacks this exact executable/living-pool combination. ALE is a methodological case, not a domain or taxonomy commitment.
- **Useful completion:** separate paper claims from release evidence; reconcile all task/coverage denominators by version; inspect the runner and graders; trace three diverse tasks; bound economic and occupational claims; and map only nonduplicate requirements into existing contracts.

Added `review-agents-last-exam-expert-task-validity` (priority 67). No second task was added.
