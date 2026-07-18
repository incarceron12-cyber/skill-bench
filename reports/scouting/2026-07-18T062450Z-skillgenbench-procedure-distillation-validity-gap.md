# Scouting note — corpus-to-skill distillation validity gap

**Scouted:** 2026-07-18 06:24 UTC  
**Evidence status:** abstract/release triage only; the full paper was **not** read in this scouting run.

## High-value primary source

**SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents** — Zhou et al., arXiv:2605.18693v1.

- Immutable paper record: https://arxiv.org/abs/2605.18693v1
- Immutable PDF: https://arxiv.org/pdf/2605.18693v1
- Official release: https://github.com/QuantaAlpha/SkillGenBench
- Release reachability check: `git ls-remote` resolved `HEAD` to `5a8bd61d8191e34fa1bbbffbff7f70db1d2a027d` at scouting time.

The arXiv API reports v1 submitted 2026-05-18 in `cs.AI`. Its abstract frames a missing measurement layer: a generator receives raw repository or document corpora, emits standardized skill artifacts, and a fixed harness executes them on downstream tasks. It distinguishes task-conditioned generation from task-agnostic reusable-library generation and claims pinned environments, deterministic execution checks, and diagnostic signals. The official repository search result describes 187 tasks across code-repository and document source types.

## Why this is not another generic Skills paper

The reviewed corpus already covers provided-skill effects, online memory/skill value, trace-derived procedural memory, and expert-authored Skill packages. An exact repository and queue search found no review or task for `2605.18693` or `SkillGenBench`. This source isolates the transformation that is most central to charter objective B:

`raw source corpus → generated procedural artifact → fixed executor → downstream task/check consequence`.

That design can clarify whether an apparent gain is attributable to procedural distillation rather than raw-context exposure, task leakage, executor compatibility, skill length/retrieval, or benchmark-specific optimization. The two generation regimes also provide a direct test of reuse claims: seeing the target task before authoring and distilling a library before downstream tasks are known license different conclusions.

## Required validity audit

A full-text and pinned-release review should reconstruct:

1. corpus, task, and split identities for repository, code-document, and domain-document families;
2. the exact generated `SKILL.md` contract and any executable/supporting files;
3. information available in task-conditioned versus task-agnostic generation;
4. executor/harness identity, task exposure, deterministic checks, auxiliary judges, repeats, invalids, costs, and denominators;
5. representative corpus→skill→execution→check lineage;
6. adverse controls for raw context, irrelevant/placebo skills, source/task overlap, executor sensitivity, and size/retrieval budget;
7. paper/release consistency, license, frozen environments, result reconstruction, and contamination boundaries.

The warranted output is a bounded generation-pipeline validity assessment—not a claim that automated Skills contain expert knowledge, transfer across domains, improve professional work, or reduce expert burden.

## Queue action

Added one pending review task: `review-skillgenbench-procedure-distillation-validity` (priority 95). Useful completion is an immutable full-paper review and pinned-release audit that traces the complete transformation chain and states regime-specific claim ceilings.
