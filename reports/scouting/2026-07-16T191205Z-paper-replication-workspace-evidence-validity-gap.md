# Scouting note — Paper-replication workspace-evidence validity gap

**Timestamp:** 2026-07-16T19:12:05Z  
**Evidence status:** arXiv API metadata/abstract, endpoint checks, web discovery, GitHub repository metadata, commit identity/history, recursive tree inventory, and pinned README triage only. The paper, skills, case-study workspaces, analysis, and reported results were **not** deeply read or audited in this scouting run.

## Substantive candidate

**Coding-agents can replicate scientific machine learning papers** — Atharva Hans and Ilias Bilionis, arXiv:2607.02134v2.

- Immutable record: https://arxiv.org/abs/2607.02134v2
- Immutable PDF: https://arxiv.org/pdf/2607.02134v2
- Immutable HTML: https://arxiv.org/html/2607.02134v2
- Official release: https://github.com/PredictiveScienceLab/paper-replication-paper
- The arXiv API reports v1 submission on 2 July 2026 and v2 update on 10 July 2026; the abstract contains no withdrawal notice. Record, PDF, HTML, repository, repository API, and README endpoints returned HTTP 200.
- Repository `main` was verified at `e030a7b5dc625acb7cfc1b9b5630161b7a4a1ed2` by `git ls-remote` and the GitHub API. GitHub identifies a non-fork Apache-2.0 release bundle created 16 June 2026, initially committed 1 July, and last committed 5 July. The pinned README identifies released Codex and Claude Code skills, twelve agent-generated case-study workspaces, analysis scripts, derived artifacts, and manuscript figures.
- The complete GitHub recursive-tree response was not truncated and exposed 8,652 entries. Triage confirmed target configs, run records/indexes, provenance records, status files, reports/artifacts, alignment digests, extracted target/coverage/effort/metric tables, canonical-fidelity and drift outputs, Bayesian draws/diagnostics, and plotting scripts. Existence is not evidence that these objects are correct, complete, mutually consistent, or paper-matched.
- The abstract reports twelve independent runs over four scientific machine-learning papers, 12/12 completion-gate passage, and report coverage for 158 recorded targets. It also reports variation among completed runs in target decomposition, numerical fidelity, elapsed time, replaced intermediate executions, and evidence-acceptance rules. These are author claims awaiting full-paper and release verification.

## Why this is a narrow, useful gap

The corpus already deeply reviews PaperBench, SciAgentArena, LH-Bench, ResearchClawBench, and generated/adaptive rubric systems. Exact title, arXiv-ID, and official-repository searches found no review or queue task for this source. This candidate is adjacent but nonduplicate because it releases a procedural Skill and full repeated workspaces whose own completion contracts can be compared with source-paper claims, numerical fidelity, execution replacement, report coverage, and acceptance-rule variation.

The focused validity chain is:

`source paper/material version → selected computational claim and authority → agent-authored target decomposition → method/code reconstruction → execution and replacement lineage → generated evidence/provenance → acceptance rule and threshold → report locator/coverage → completion gate → independent source-claim/numerical replication → cross-paper/run/solver skill-transfer claim`.

A workspace can satisfy its internal target and report-coverage contract while omitting a source claim, choosing a permissive acceptance rule, retaining only a favorable replacement execution, or reproducing the structure but not the paper's numerical result. Conversely, legitimate replication may use a different decomposition or acceptance rationale. The source is therefore useful for separating internal conformance, evidence lineage, scientific replication, reliability, and skill-transfer claims rather than treating a completion gate as one latent success variable.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic scientific-work evaluation), B (expert/scientific claim-to-target-to-evidence transfer), and C (workspace, artifact, provenance, validator, and repeated-trial machinery).
- **Concrete evidence/artifact:** immutable-v2 full-text review plus commit-pinned release audit, released-analysis replay, and bounded zero-model-call mutations of target, acceptance, provenance, execution-lineage, and completion boundaries.
- **Uncertainty clarified:** whether the workflow establishes workspace contract conformance, report coverage, numerical source-claim replication, or reusable procedural transfer—and how run-specific target/acceptance construction changes those claims.
- **Mode:** narrow expansion feeding validation and consolidation; not generic coding-agent news or a scientific-ML scope commitment.
- **Duplication and scope check:** adjacent reviews cover long-horizon replication, scientific workflow suites, and skill-grounded evaluation, but not this released repeated chain from source claims through agent-authored targets and acceptance rules to completion. The reusable result is cross-domain machinery for evidence-bearing professional artifacts.
- **Useful completion:** reconstruct inputs, configured systems, target and threshold authority, execution/replacement history, evidence/provenance, validators, reports, exclusions, repeats, uncertainty, time/cost, and paper-release correspondence; replay released analysis; test omission/splitting, permissive-rule, stale/replaced-run, missing-provenance, report-only-coverage, and numerical-fidelity boundaries; preserve separate claim ceilings for conformance, coverage, replication, scientific validity, procedural transfer, reliability, professional capability, and readiness.

Added one review task: `review-paper-replication-workspace-evidence-validity` (priority 3), subordinate to the current build, consolidation, and human prerequisite. No second task was added. No claim is made that the full paper or release was read, that the twelve workspaces independently replicate their source papers, that all targets are complete or authoritative, that the analysis reproduces, or that the Skill establishes general efficacy, reliability, scientific validity, professional capability, or readiness.
