# Scouting note — CutVerse temporal creative-artifact validity gap

**Timestamp:** 2026-07-15T04:16:48Z  
**Scope:** Narrow expansion against charter objectives A/B/C. At intake the queue had 249 tasks: 242 completed, four blocked, two pending human decisions, and one pending consolidation; no source/research/review task remained. Existing reviews cover professional GUI state, desktop interaction, multimodal artifact observation, artifact transitions, and trajectory evidence, but not dense time-based creative artifacts whose requirements span cross-application actions, synchronization, and rendered output.

## Substantive finding — triage only

**CutVerse: A Compositional GUI Agents Benchmark for Media Post-Production Editing** — Haobo Hu, Xiangwu Guo, Zhiheng Chen, Difei Gao, Haotian Liu, Libiao Jin, and Qi Mao, arXiv:2605.19484v1.

- Immutable record: https://arxiv.org/abs/2605.19484v1
- Immutable PDF: https://arxiv.org/pdf/2605.19484v1
- Official repository: https://github.com/CUC-MIPG/CutVerse
- arXiv API metadata identifies immutable v1, submitted 19 May 2026 in `cs.CV` with secondary `cs.AI`, `cs.GR`, and `cs.HC`; its summary contains no withdrawal notice.
- The abstract reports 186 complex long-horizon tasks grounded in expert demonstrations across seven professional applications, including Premiere Pro and Photoshop. It describes dense multimodal interfaces, tightly coupled interaction sequences, and a parser that converts screen recordings and low-level interaction logs into structured compositional GUI trajectories. It reports 36.0% task success and attributes remaining difficulty to long-horizon reliability and domain-specific planning. These are author-reported abstract claims, not independently verified findings.
- GitHub API verification found the official repository live and unarchived. Its mutable `main` head was `8b40dc18e1385bf6a9710cd999b22e4c51d602c8` (commit timestamp 8 June 2026), with 328 tree entries. A `Preview` tag/release was published 21 May 2026 but had no attached release assets. The tree exposes implementation material, but scouting did not inspect or execute repository files; a review must pin exact bytes and distinguish paper-time, Preview, and later-main evidence.
- Repository-wide duplicate search found no CutVerse title, arXiv ID, review, or queue task. The only nearby creative-quality observations occur in DeskCraft and general professional-work reviews.
- This is **metadata, abstract, URL, repository-metadata/tree, release-location, and duplicate triage only**. The paper body, appendices, expert demonstrations, tasks, source media, parser, trajectories, environments, artifacts, graders, model runs, result tables, and repository implementation were not read or audited. No claim is made that the tasks sample professional work, that structured trajectories preserve expert procedure, that action-sequence agreement permits only legitimate paths, that task success reflects temporal/cross-modal output quality, or that the benchmark establishes creative competence, professional acceptance, reliability, capability, or readiness.

## Why this is distinct

Time-based creative work stresses a reusable evaluation boundary that static document and final-state tasks only partly expose. The same rendered output can arise through different legitimate edit graphs; an apparently correct action sequence can produce an invalid, flattened, destructive, mistimed, or non-editable project; a structurally valid project can still fail synchronization, perceptual coherence, or stakeholder intent. Screen-recording and interaction-log parsing also introduces a transformation layer between expert demonstration and benchmark trajectory that may omit semantic operations or overprivilege one witness path.

A full audit should therefore separate `expert demonstration provenance → parser transformation → compositional action/dependency representation → observed execution → editable project state → rendered temporal/cross-modal output → plural creative/professional acceptance`. It should test whether the benchmark observes requested deltas and preservation constraints, accepts alternative paths, validates application/environment state, and reports repeats and invalids—rather than promoting trajectory conformance or one task-success scalar into creative-work capability.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic knowledge-work benchmarks), B (expert-demonstration-to-task/check transformation validity), and C (trajectory, temporal artifact, and observer machinery).
- **Concrete evidence/artifact:** immutable-v1 full-paper review plus commit-pinned official-release audit, including at least one representative task/parser/grader/result path if released.
- **Uncertainty clarified:** whether compositional trajectories and benchmark observers measure temporal/cross-modal artifact correctness and preservation, or primarily one demonstrated action path and selected endpoint predicates.
- **Mode:** narrow expansion feeding later consolidation/validation; media post-production is a bounded stress case for reusable artifact machinery, not a project scope commitment.
- **Duplication check:** no exact coverage; required comparisons with DeskCraft, Workflow-GYM, OSWorld 2.0, SciVisAgentBench, Delegate52/artifact-transition, and trajectory-observer work prevent isolated benchmark collecting.
- **Useful completion:** evidence-grounded retain/repair/test implications and strict claim ceilings across demonstration provenance, conformance, artifact quality, professional acceptance, reliability, capability, and readiness.

Added one task: `review-cutverse-temporal-creative-artifact-validity` (priority 19). No second task was added.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). The pre-existing untracked arXiv source trees and AgentFootprint release ZIP were not modified.
