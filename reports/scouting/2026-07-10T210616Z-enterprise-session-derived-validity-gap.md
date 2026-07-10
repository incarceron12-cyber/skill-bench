# Scouting note — session-derived workplace benchmark validity gap

**Timestamp:** 2026-07-10T21:06:16Z  
**Scope:** Narrow search against charter objectives A/B/C after confirming one consolidation task pending, no pending source/research/review work, and two appropriately blocked builds. This run targeted an uncovered provenance boundary—turning real workplace sessions into reproducible benchmark tasks—rather than repeating broad benchmark discovery.

## Substantive finding (triage only)

**EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions**

- Immutable arXiv record: https://arxiv.org/abs/2606.23654v1
- Immutable PDF: https://arxiv.org/pdf/2606.23654v1
- Paper-linked official repository: https://github.com/FrontisAI/EnterpriseClawBench
- Repository HEAD observed during scouting: `68507699d1a61700f4281f1f34dcadb20f2de06d`
- arXiv API metadata identifies version 1 in `cs.CL`, submitted and last updated 2026-06-22. The abstract describes 852 reproducible tasks derived from a proprietary archive of real workplace sessions, with recovered fixtures, rewritten prompts, role classes, skill subclasses, hard rules, and semantic rubrics.
- The abstract explicitly says the benchmark data are not released because sessions contain internal enterprise content; the reusable claim is therefore the construction and evaluation protocol. It also calls for harness–model reporting alongside artifact delivery, visual quality, cost, runtime, and skill-transfer behavior.
- The paper itself links the GitHub repository. GitHub API and `git ls-remote` verified the public repository and main-branch HEAD; indexed repository paths include `construction`, `evaluation`, `sandbox`, `raw_session_example`, `docs`, and `example_runs`.
- This is **metadata/abstract and release-location triage only**. The full paper and repository were not read during scouting. Source-session sampling, consent and privacy controls, transformation fidelity, task exclusions, rubric construction, evaluation details, uncertainty, and workplace-capability claims require full review.

## Why this is distinct

The local corpus covers expert-authored occupational tasks, synthetic workspaces, stateful workflows, generated task projections, and artifact-centered grading. It does not directly examine the reverse-engineering of benchmark tasks from observed production sessions. That pathway offers stronger ecological grounding but introduces a distinct validity chain: session selection → privacy filtering → problem and context recovery → prompt rewriting → fixture reconstruction → rule/rubric extraction → reproducible sandbox. Each transformation can remove tacit context, import hindsight, expose answer-bearing traces, or turn one historical path into the only accepted solution.

The reusable question is not whether skill-bench should become an enterprise benchmark. It is whether naturally occurring work traces can provide evidence for task content and hidden requirements while preserving provenance, contributor rights, alternative valid procedures, and auditable construct fidelity when the original data cannot be released.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic knowledge-work and production evaluation frontier), B (expert/workflow evidence into tasks and rubrics), and C (provenance, projection, artifact, workspace, and validity machinery).
- **Evidence/artifact sought:** immutable-v1 full-paper review, pinned official-release audit, two public-safe end-to-end example traces, and a crosswalk to existing contracts.
- **Uncertainty clarified:** whether session-derived tasks preserve the original construct; how privacy transformations and unreleased evidence limit external audit; whether historical paths become over-restrictive rules; and what one deployment can support about broader workplace capability.
- **Mode/balance:** one narrow expansion task at priority 68. The queue retains one higher-priority consolidation path; blocked tasks remain blocked for real prerequisites.
- **Duplication/scope:** no local index entry, review, queue item, or scouting note matched `2606.23654`, `EnterpriseClawBench`, or session-derived benchmark construction. Workspace-Bench and GDPval address related realism but not this source-to-task transformation chain. Enterprise work is a methodological case, not a scope commitment.
- **Useful completion:** separate paper claims from inspectable release evidence; reconstruct and audit the entire transformation and evaluation pipeline; trace at least two released examples; preserve the proprietary-evidence boundary; map only nonduplicate implications into existing machinery.

Added `review-enterpriseclawbench-session-derived-validity` (priority 68). No second task was added.
