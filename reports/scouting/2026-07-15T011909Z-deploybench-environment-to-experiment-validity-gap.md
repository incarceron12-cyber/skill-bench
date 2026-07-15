# Scouting note — environment-to-experiment validity in research-artifact deployment

**Timestamp:** 2026-07-15T01:19:09Z  
**Scope:** Narrow expansion against charter objectives A/B/C. At intake the queue had 241 tasks: 233 completed, four blocked, four pending, with no source/research/review task. Existing reviews cover research replication, scientific workflows, executable artifacts, harness isolation, task health, and completion/abstention, but not fresh-machine deployment as a separately graded prerequisite to substantive research work.

## Substantive finding (triage only)

**DeployBench: Benchmarking LLM Agents for Research Artifact Deployment**

- Immutable record: https://arxiv.org/abs/2606.05238v1
- Immutable PDF: https://arxiv.org/pdf/2606.05238v1
- Official repository: https://github.com/pentium3/DeployBench
- The arXiv API identifies Yuanli Wang et al.; primary category `cs.SE`; submitted 3 June 2026 with no later version. Its metadata summary contains no withdrawal notice. The versioned abstract, PDF, and official repository URLs returned HTTP 200.
- The **v1 abstract** describes 51 research-artifact deployment tasks spanning AI/ML, computer systems, and scientific computing. Each starts from a fresh-machine setup problem and is checked by a hidden pipeline that runs a paper-designated experiment. The abstract reports OpenHands evaluations of four models, pass rates from 7.8% to 51.0%, and 97 agent-terminated self-stops among 154 failures, attributed to pre-finish checks targeting something weaker or different from the task. These are author-reported abstract claims, not independently verified findings.
- The official repository README exposes a concrete audit surface: `papers.csv`; per-task `task.json`; oracle `setup_reference.sh`; `verify.sh`; and `task_parser.py`. It types tasks by domain, manual difficulty, time budget, pre-2020 status, GPU, main language, QEMU use, external artifacts, and whether the oracle applies a compatibility patch. GitHub API metadata reports `master` at commit `be8f68a328fe6dcda137d46adb05f330d546d394` (30 June 2026), with no machine-resolved license. This is current metadata and README triage, not a version-matched release audit.
- The distinctive validity question is the boundary between **environment construction and research reproduction**. A verifier can establish that one selected experiment ran and emitted expected artifacts without establishing faithful deployment of the paper, independent reproduction, scientific correctness, or downstream research usability. Conversely, a failure can originate in task projection, legacy compatibility, external infrastructure, verifier/parser coverage, agent completion judgment, or substantive setup competence.
- This is metadata, abstract, URL, official-README, repository-metadata, and duplicate triage only. The paper body, appendices, release files, 51 task packages, source repositories, oracle scripts, compatibility patches, verifiers, parsers, runs, logs, results, and statistics were not read or audited. No claim is made that the benchmark is representative, its hidden checks are valid, the release reproduces v1, its failure taxonomy is correct, or any system has general research capability or deployment readiness.

## Benchmark implication to test

Research-artifact deployment needs a typed chain: `paper/version and designated claim → source repository/commit → task projection and fresh-machine contract → dependency/toolchain/hardware/external-artifact state → authorized compatibility transformation → agent observations/actions → agent-declared completion and pre-finish evidence → independently executed experiment → artifact/log observation → parser/verifier decision → downstream reproducibility or usability evidence → bounded claim`. Environment invalidity, task invalidity, completion-judgment mismatch, verifier blind spots, and substantive deployment failure need separate labels and denominators.

A full audit should reconstruct at least one released task end to end and test whether the designated experiment is sufficient for the paper-level target; whether oracle compatibility changes preserve semantics; whether source, task, and verifier versions are pinned; whether hidden checks admit legitimate alternatives and reject superficial outputs; how GPU/QEMU/external services, timeouts, resets, invalid trials, and self-stops are handled; and whether task/repository clustering, repeats, costs, and release drift support the reported comparisons. Compare with PaperBench, SciAgentArena, Harness-Bench, task-health, artifact-observation, and completion/abstention machinery.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent benchmark research), B (paper→environment→experiment→claim validity), and C (task-health, execution, artifact-observer, and diagnosis machinery).
- **Evidence/artifact sought:** immutable-v1 deep review, pinned release audit, and one source→setup→experiment→verdict reconstruction.
- **Uncertainty clarified:** what hidden experiment execution establishes, and whether self-stops diagnose completion judgment rather than environment, task, or verifier defects.
- **Mode/balance:** one low-priority review restores a minimal research backlog behind two pending consolidations and human/operational blockers; no broad search bundle was added.
- **Duplication/scope:** repository search found no DeployBench/2606.05238 entry. Adjacent reviews cover replication and scientific execution, not fresh-machine deployment plus legacy compatibility. The three technical domains test reusable validity machinery and do not narrow `skill-bench` to software engineering.
- **Useful completion:** preserve paper/source/task/environment/transformation/verifier identities, invalids, alternatives, clustering, repeats, cost, release drift, and claim ceilings; reuse existing contracts unless a concrete executable gap remains.

Added one task: `review-deploybench-research-artifact-deployment-validity` (priority 12).

`τ`-Knowledge was not queued: its retrieval-plus-state-change contribution overlaps the mature tool/user-simulator, policy, evidence-adoption, and state-observer streams more directly than DeployBench fills the environment-to-experiment boundary.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 68 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
