# Scouting note — WildClawBench harness-transport validity gap

**Timestamp:** 2026-07-16T16:40:29Z  
**Evidence status:** arXiv metadata/abstract, endpoint, repository metadata/root-inventory, commit-history, and pinned-README triage only. The paper, tasks, images, graders, traces, and results were **not** deeply read or audited in this scouting run.

## Substantive candidate

**WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation** — Shuangrui Ding et al., arXiv:2605.10912v1.

- Immutable record: https://arxiv.org/abs/2605.10912v1
- Immutable PDF: https://arxiv.org/pdf/2605.10912v1
- Immutable HTML: https://arxiv.org/html/2605.10912v1
- Official repository: https://github.com/InternLM/WildClawBench
- Official dataset: https://huggingface.co/datasets/internlm/WildClawBench
- Record, PDF, HTML, repository, and dataset endpoints returned HTTP 200. The arXiv page reports submission on 11 May 2026 and contains no withdrawal/retraction notice.
- Repository `main` HEAD was verified by `git ls-remote` at `6f78ad8d4bc17e73e7d84de246dd2caa0b9c82c4`; GitHub identifies a non-fork, active MIT-licensed repository. Its pinned root exposes tasks, skills, evaluation and runner code, scripts, a technical report, and configuration.
- The abstract reports 60 human-authored bilingual multimodal tasks, isolated Docker execution, hybrid rule/state/model grading, 19 model backends, and up to an 18-point score shift from changing harness. These are author claims awaiting full-paper and release verification.
- The pinned README advertises a same-task comparison across OpenClaw, Claude Code, Codex CLI, and Hermes Agent. It also exposes concrete comparability risks: four separately versioned Docker images; differing model-name/provider adapter conventions; an OpenClaw-only custom-endpoint path; OpenRouter references hardcoded in some task prompts and graders; external YouTube/model-weight preparation and authenticated downloads; and mutable task ground truth, including a 14 July commit explicitly fixing one search task's ground truth. Same task IDs and grading code therefore do not by themselves establish an equal model, provider, interface, tool, budget, environment, or benchmark-version treatment.

## Why this is a narrow, useful gap

The corpus already covers configured-system identity, Harness-Bench execution isolation, Claw-Eval multichannel observation, ProcGrep harness confounding, and several mixed model×harness leaderboards. Repository-wide exact-title/ID search found no WildClawBench review or queue task. Unlike those adjacent sources, this release claims a direct four-harness comparison over one nominal task suite and publishes harness-specific runtime packages. It can therefore support a focused audit of the missing transport chain:

`task/source/grader version → harness-specific image and adapter → model/provider realization → visible tools, skills, prompts, permissions, budgets, and termination → valid execution and observer views → paired task-level outcome/resource vector → harness effect or configured-package difference → transport claim`.

A full audit should determine whether the four cells share an intervention-compatible task population and provider realization, whether task-level paired outputs and invalid/service-failure records are released, whether score differences survive task clustering and repeated-run uncertainty, and whether later ground-truth repairs invalidate or split the reported comparison. The benchmark's varied tasks are a cross-domain stress substrate, not a proposal to narrow `skill-bench` to CLI assistants.

## Charter decision filter and queue action

- **Objectives advanced:** A (production/native-runtime benchmark evidence) and C (configured-system, execution, observation, metric, and lifecycle instrumentation).
- **Concrete evidence/artifact:** immutable-v1 full-text review plus commit-pinned GitHub/Hugging Face release audit and a paper↔release/harness-cell conformance record.
- **Uncertainty clarified:** whether the reported contrast identifies a harness/scaffold effect, a broader configured-package difference, or version/provider/task-population confounding.
- **Mode:** narrow expansion feeding validation and consolidation; not another generic benchmark search.
- **Duplication check:** existing reviews establish the general harness-confounding risk but do not audit a released four-harness nominally matched matrix.
- **Useful completion:** reconstruct each cell's model/provider, image, prompt, tools/skills, permissions, budgets, retry/termination, task eligibility, observer, invalidity, resource, and version identity; verify task-level pairing and uncertainty; preserve supported configured-package findings while rejecting unsupported model-capability, harness-causal, reproducibility, professional-validity, safety, production, or readiness claims.

Added one review task: `review-wildclawbench-harness-transport-validity` (priority 84). No second task was added. No claim is made that the full paper or release was read, that all tasks or images are reproducible, that the reported score shifts are causal harness effects, or that WildClawBench establishes general agent capability, professional validity, operational safety, production fitness, or readiness.
