# Scouting note — matched trigger / causal-chain validity gap

- **Timestamp:** 2026-07-18T05:01:09Z
- **Evidence status:** arXiv API metadata/abstract, immutable URL checks, exact repository duplicate searches, and a pinned GitHub API tree/README inspection only. The PDF body, paper source, dataset rows, manual labels, evaluation code, logs, LFS objects, or result records were **not** deeply read, downloaded, reproduced, or audited during scouting.

## Substantive candidate — triage only

**AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration** — Arastoo Zibaeirad, Marco Vieira, and Thomas Zimmermann; arXiv:2607.12058v1.

- Immutable record/PDF: https://arxiv.org/abs/2607.12058v1 · https://arxiv.org/pdf/2607.12058v1
- Pinned artifact: https://github.com/Erroristotle/AutoTrace/tree/af1f3345928a5652dfbfa615ac0407c39e459143
- The arXiv API reports v1 submitted and last updated 13 July 2026 in `cs.SE`, `cs.AI`, and `cs.CR`; its abstract contains no withdrawal or retraction notice. The immutable record, PDF, and repository URLs returned HTTP 200.
- The abstract defines trigger localization as identifying the statement that turns vulnerable state into an unsafe operation. It describes LLM-directed layerwise exploration over a code property graph with deterministic evidence-admissibility gates, reports 75.0% VulnHit and 80.8% FuncHit on InterPVD, and introduces SinkTrace-Bench: 1,542 balanced vulnerable/safe source-to-sink samples from matched vulnerable/patched program states, reportedly verifier-confirmed and audited against expert annotations. These are author-stated abstract claims awaiting full-paper and release verification.
- GitHub API inspection pinned the sole visible latest commit `af1f3345928a5652dfbfa615ac0407c39e459143` (3 July 2026). Its 28,417-entry recursive tree was complete according to the API and exposes a 58.6 MB `dataset/train.jsonl`, manual-evaluation JSONL/Markdown, RQ evaluation scripts, five named model result files, score/report files, extensive per-CVE prompts/traces/results, and Git-LFS pointer-sized graph binaries. The sparse README says the repository contains evaluation, dataset, logs, and results; GitHub reports no declared license. This is release-surface triage, not an audit of content or reproducibility.
- Exact ID/title/signature-phrase searches found no local review, task, or scouting note. Existing reviews cover root/surface attribution, injected-fault localization, evidence-backed traces, paired repair, alternative paths, and evaluator validity, but none audits patch-conditioned trigger localization or this matched source-to-sink construction.

## Why this is a narrow, useful gap

The reusable chain is:

`versioned vulnerable state + fixing commit → patch interpretation and critical-variable hypothesis → interprocedural exploration decisions → graph evidence and coverage → candidate unsafe operation → deterministic admissibility/verifier disposition → matched patched-state counterfactual → expert adjudication → localization/classification score → downstream repair, test, or diagnosis use`.

This could sharpen `skill-bench`'s root/surface principle. A structured witness can make a hypothesized causal path inspectable, while a matched repaired artifact can falsify superficial final-state similarity. But neither automatically proves the earliest cause, necessity, sufficiency, uniqueness, or downstream diagnostic utility. The useful object is a typed audit of where agent judgment ends, where deterministic graph rules begin, what each observer can see, and which causal claim each matched pair actually supports.

The release surface also raises high-value validity questions: patch conditioning may leak the answer or select only patch-expressible causes; vulnerable and safe rows from one CVE are dependent; project/CVE duplicates can cross splits; one code-property-graph ontology can jointly generate evidence and verify it; graph construction failures may silently remove difficult cases; an expert audit sample may not validate all generated chains; multiple legitimate triggers may make one target incomplete; and pointer-sized LFS objects, absent licensing, mutable dependencies, and unreconciled invalid/retry records can limit reproduction. Classification accuracy on matched slices is not equivalent to full-repository localization, exploitability judgment, repair quality, professional security work, or readiness.

This is a cross-domain causal-diagnosis mechanism case, not a proposal to narrow `skill-bench` to software security.

## Charter decision filter and queue action

- **Objectives advanced:** A (agent evaluation, diagnostic benchmarks, and validity), B (evidence-bearing causal and root/surface chains), and D/E (cross-source consolidation and decision-relevant learning).
- **Concrete evidence:** immutable-v1 full-paper/source review plus pinned-release audit of construction, annotations, graph/admissibility rules, result accounting, and reproducibility, with page/file/commit locators.
- **Uncertainty clarified:** whether matched artifact deltas and deterministic graph witnesses identify a causal trigger or mainly encode patch-correlated syntax, graph reachability, and verifier conventions.
- **Mode:** narrow expansion. Before this addition the autonomous source/research/review backlog was empty; one bounded audit restores evidence flow without restarting broad searches.
- **Duplication/scope check:** adjacent work covers attribution components but not this construction or release. Existing trace, root-cause, alternative-path, configured-system, metric, task-health, and validity machinery should host implications; add no security-specific schema or pilot absent stronger evidence.
- **Useful completion:** reproduce or decisively bound the reported tables and 1,542-row construction where artifacts permit; preserve pair/project/CVE dependence, exclusions, retries, version identity, observer limits, and alternative triggers; separate graph conformance, trigger localization, vulnerability classification, causal correctness, downstream utility, professional validity, and readiness.

Added one task: `review-autotrace-trigger-causal-chain-validity` (review, priority 58). No second source was queued.
