# Scouting note — cross-domain procedural-skill ablation gap

**Timestamp:** 2026-07-10T06:09:35Z

**Scope:** Narrow gap check around the active LH pilot's no-skill/public-skill ablation. The queue was healthy (eight pending tasks), so this run did not repeat broad benchmark searches and added only the closest missing methodological review.

## Substantive finding (triage only)

**SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks** — Li et al., arXiv:2602.12670v4.

- Immutable record: https://arxiv.org/abs/2602.12670v4
- Immutable PDF already local: `data/papers/pdfs/2602.12670v4-skillsbench-benchmarking-how-well-agent-skills-wor.pdf`
- Extracted text already local: `data/papers/text/2602.12670v4-skillsbench-benchmarking-how-well-agent-skills-wor.txt`
- Official release: https://github.com/benchflow-ai/skillsbench (reachable during this run; remote HEAD `44cdda48f6e8c4d381f4f5075c0f4a051ba69e98`)
- The local arXiv metadata/abstract reports a current inventory of 87 tasks across eight domains, matched no-Skills and curated-Skills conditions for 18 model-harness configurations, deterministic verifiers, and configuration-level gains that vary substantially.
- This was **metadata/abstract and URL triage only**. The paper and repository were not read during scouting; all design details and efficacy claims require full immutable-v4 and pinned-release inspection.

## Why this fills a distinct current gap

The repository has already reviewed LH-Bench's skill-grounded rubric pattern and implemented a four-condition intervention/instrument contract, but it has not deeply reviewed the closest cross-domain matched evaluation of procedural skills. SkillsBench can test whether the LH pilot records enough information to distinguish intervention efficacy from task–skill–verifier co-design, harness interactions, criterion leakage, and binary-verifier limits. Its breadth is evidence for a general skill-transfer hypothesis, not a reason to narrow the benchmark to the SkillsBench task inventory.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier evidence), B (expertise-to-evaluation methodology), and C (validation of executable ablation contracts).
- **Evidence/artifact sought:** a full-paper plus pinned-release review and a nonduplicative mapping to the active pilot, validity argument, and task-health contracts.
- **Uncertainty clarified:** what matched evidence actually supports claims that procedural skills transfer capability across domains and configured systems.
- **Mode:** targeted expansion supporting an immediate validation gate; lower priority than ACTA and the genuine LH pilot runs.
- **Duplication/scope check:** distinct from the completed LH-Bench review because it centers paired intervention efficacy across many tasks/configurations rather than skill-grounded subjective judging.
- **Useful completion:** reconstruct the experimental matrix and uncertainty, inspect released tasks/skills/verifiers, identify confounds, and specify only changes that materially improve the existing ablation.

Added one task: `review-skillsbench-paired-skill-efficacy` (priority 91).
