# Scouting note — SOP-to-task expertise-transfer validity gap

**Timestamp:** 2026-07-14T00:18:03Z
**Scope:** Narrow expansion against charter objectives A/B. Queue inspection found 198 tasks: 193 completed, two blocked, and three pending build/consolidation tasks, with no pending source/research/review work. The reviewed corpus covers procedural Skills, typed clause relations, industrial expertise codification, professional state, and production-requirement projection, but not a released cross-domain benchmark that transforms expert-authored SOPs into generated tools, data, executable tasks, and ground-truth outputs.

## Substantive finding (triage only)

**SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents**

- Immutable latest arXiv record: https://arxiv.org/abs/2506.08119v2
- Immutable PDF: https://arxiv.org/pdf/2506.08119v2
- Author-owned release: https://github.com/amazon-science/SOP-Bench
- Author-linked dataset: https://huggingface.co/datasets/amazon/sop-bench
- The arXiv API identifies 24 authors, v1 submission on 9 June 2025, and v2 update on 23 February 2026 in `cs.AI`; the abstract contains no withdrawal notice and labels the paper “Under review.”
- The abstract claims 2,000+ tasks across 12 business domains. It describes a human-AI workflow in which experts authored SOPs, AI generated tools/APIs/datasets, and humans validated the resulting artifacts. This is unusually direct evidence for the project’s central SOP/skill → environment → task → oracle transformation question, but all authority, qualification, validation, and lineage details require full verification.
- Structural inspection of immutable v2 HTML—not a full reading—confirmed sections on the human-AI workflow, human authoring and validation, SOP descriptions, evaluation methodology, results/ablations, generation prompts, agent prompts, examples, and a detailed patient-intake package.
- The current author-owned GitHub HEAD `2fdce4c57e6b02b725d5437ec079c142cffd8e07` was verified with `git ls-remote`; GitHub dates that commit to 6 June 2026, more than three months after v2, so it must not be treated as the paper-time implementation. Its recursive tree exposes 381 files, including per-domain `sop.txt`, mock `tools.py`, `toolspecs.json`, metadata, and test sets with/without outputs, plus harness and tests. The README advertises detailed leaderboard results as “coming soon,” despite reporting selected aggregate findings.
- The public Hugging Face dataset API verified `amazon/sop-bench` at revision `92633eae202fbf66cceb374c6ad55da41ca693b6`, last modified 26 May 2026, with 313 listed artifacts. Release correspondence, task/domain count drift, and whether paper-result rows/traces are present remain unaudited.
- Repository-wide title, arXiv-ID, and exact-name searches found no duplicate review or queue task. LH-Bench and SLBench address procedural guidance and clause relations; industrial codification and AlphaEval address expertise/production projection; Workflow-GYM addresses professional state. None audits this released multi-domain SOP-to-executable-task pipeline.
- This is **metadata/abstract, section-structure, URL, and release-existence triage only**. The PDF, source, appendices, SOPs, code, datasets, tests, traces, and results were not fully read or audited. No claim is made that the package preserves tacit expertise, represents real occupational work, validates its ground truths, supports alternative legitimate paths, or establishes cross-domain capability, safety, production fitness, or readiness.

## Benchmark implication to test

SOP-based task construction needs an explicit transformation ledger: `expert identity/authority → source SOP/version → clause and exception representation → AI-generated environment/data/tool artifacts → human validation/adjudication → task/oracle projection → agent-visible procedure → observed calls/state/artifact → score and claim`. Formal procedures can make decision logic executable while omitting the tacit cues, workarounds, exceptions, authority boundaries, and consequence judgments that distinguish professional expertise from closed-world compliance. Full review should test whether task generation preserves relation semantics and legitimate alternatives, whether the same people or generated cues shape intervention and oracle, whether synthetic test rows support domain claims, and whether paper/release drift changes the instrument.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent and expertise-transfer research) and B (general expertise-to-evaluation methodology).
- **Evidence/artifact sought:** immutable full-v2 review plus pinned GitHub/Hugging Face release audit reconstructing expert/AI authorship, approval, task/oracle lineage, counts, scoring, results, and paper-release correspondence.
- **Uncertainty clarified:** whether SOP-Bench operationalizes reusable expert-procedure transfer or primarily evaluates compliance with AI-generated closed-world programs.
- **Mode/balance:** one narrow expansion task restores a minimal review backlog while leaving the three existing build/consolidation tasks at higher priority.
- **Duplication/scope:** complements, rather than repeats, procedural-skill, clause-relation, production-projection, and professional-workflow reviews; 12 released domains are a comparative instrument, not a commitment to SOP execution as the benchmark’s scope.
- **Useful completion:** verify artifact lineage, all denominators/results, relation and alternative-path coverage, human validation, cross-domain dependence, release timing, and licenses; map only nonduplicate findings to existing contracts and preserve strict validity ceilings.

Added `review-sop-bench-procedure-to-task-validity` (priority 32). No second task was added.
