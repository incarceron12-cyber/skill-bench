# Scouting note — deterministic evidence-path validity gap

**Timestamp:** 2026-07-13T22:36:11Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 192 tasks: 188 completed, two blocked, one ready cross-domain validation build, and one pending consolidation task, with no pending source/research/review work. The reviewed corpus already separates evidence availability, access, authority, adoption, artifact acceptance, and consequence, but does not audit GroundEval's proposed deterministic tests for verified absence, actor-time evidence permissions, and causal-mechanism use.

## Substantive finding (triage only)

**GroundEval: A Deterministic Replacement for LLM-as-Judge in Stateful Agent Evaluation**

- Immutable arXiv record: https://arxiv.org/abs/2606.22737v2
- Immutable PDF: https://arxiv.org/pdf/2606.22737v2
- Immutable HTML: https://arxiv.org/html/2606.22737v2
- Author-linked repository: https://github.com/tenurehq/groundeval
- The arXiv API identifies Jeffrey Flynt as sole author; v1 was submitted 22 June 2026 and v2 updated 2 July 2026. The API record contains no withdrawal notice.
- The abstract proposes a judge-free framework that scores both final answer and recorded trajectory against grounded, time-bounded, access-controlled evidence. Its three tracks target distinct failure claims: **Silence** (did the agent check before asserting absence?), **Perspective** (did it use only evidence available to the actor at the relevant time?), and **Counterfactual** (did it use the specified causal mechanism rather than a plausible surface association?).
- The abstract reports a case in which two frontier LLM judges scored a plausible response at least 0.85 while GroundEval assigned zero because the required artifact had never been retrieved. That is a discovery lead only: sample construction, judge prompts, denominators, trial independence, threshold choice, and whether the deterministic oracle actually captures justified evidence use require full verification.
- Structural inspection of the immutable HTML—not a full reading—confirmed sections for the core evaluation contract, formal properties, three tracks, leakage/shortcut controls, dual and violation-adjusted scoring, subjects, dataset, baselines, per-track and aggregate results, authoring gradient, integration surface, and limitations.
- The immutable HTML links the author-owned repository directly. `git ls-remote` verified current HEAD `0b2dc4940435394f20267c943ec460addb09f412` and annotated tag `groundeval-preprint-v1` resolving to commit `bb772dc857b66b7b23a4973399dd4ab1bddddac0`. Release timing and correspondence to arXiv v2 remain unaudited.
- Repository-wide title, ID, and signature-phrase searches found no duplicate. ClawArena and evidence-state machinery handle temporal authority and supersession; Workspace-Bench separates file availability, access, and claimed use; BigFinanceBench and RuVerBench expose evidence-view limitations; LongMedBench exposes retrospective-oracle laundering. None currently audits this three-track deterministic instrument or its claim to distinguish a correct answer from a valid evidence path.
- This is **metadata/abstract, URL, section-structure, and repository-existence triage only**. The PDF, appendices, code, configuration, generated questions, traces, judges, and results were not fully read or audited. No claim is made that GroundEval replaces model or human judgment generally, proves causal reasoning, validates professional work, detects common failures, or supports capability, safety, production, or readiness conclusions.

## Benchmark implication to test

A useful evaluator may need typed path obligations that cannot be recovered from a final artifact alone: an absence claim needs a declared search universe and completeness witness; an actor-time claim needs valid-time, availability, permission, and principal identity; and a mechanism claim needs independently authorized causal structure plus observations capable of discriminating it from plausible alternatives. Full review should test whether GroundEval's deterministic rules truly observe those obligations or merely encode one authored route, and whether narration is treated as evidence, corroboration, or an untrusted claim. Any transfer should reuse existing evidence-state, provenance-observation, artifact-view, trace, authority, alternative-path, root/surface, metric, and validity machinery rather than create a GroundEval-specific subsystem.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier stateful-agent evaluation), B (evidence-path-to-claim warrants), and C (deterministic graders and trace diagnostics).
- **Evidence/artifact sought:** immutable full-v2 review plus pinned author-owned release audit reconstructing question generation, oracle authoring, domain configuration, trace/narration contract, scoring, leakage controls, subjects, denominators, baselines, uncertainty, and paper/release correspondence.
- **Uncertainty clarified:** whether the three tracks distinguish evidence-path validity from answer plausibility without imposing one hidden route, laundering a retrospective oracle, trusting narration, or overstating sparse case studies.
- **Mode/balance:** one narrow expansion task restores a minimal review backlog while leaving the ready build and consolidation tasks higher priority.
- **Duplication/scope:** complements existing evidence-state and grader-validity work; the reusable construct is evidence-path admissibility across knowledge-work domains, not a memory-product or safety-only scope commitment.
- **Useful completion:** verify all reported samples, configurations, scores, and comparisons; inspect complete release artifacts and mutation/shortcut coverage; map each obligation to existing contracts; preserve deterministic-instrument, causal, prevalence, professional-validity, capability, safety, production, and readiness ceilings.

Added `review-groundeval-evidence-path-validity` (priority 38). No second task was added.
