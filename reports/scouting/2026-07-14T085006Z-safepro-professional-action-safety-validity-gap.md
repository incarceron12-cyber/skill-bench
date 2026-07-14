# Scouting note — professional action-safety validity gap

**Timestamp:** 2026-07-14T08:50:06Z  
**Scope:** Narrow expansion against charter objectives A/B/D. Queue inspection found 213 tasks: 208 completed, three blocked, one pending consolidation, and one pending human decision; no source/research/review task remained. A prior DeskCraft scout explicitly deferred SafePro pending a distinctness check, so this run followed that identified gap rather than repeating a broad search.

## Substantive finding (triage only)

**SafePro: Evaluating the Safety of Professional-Level AI Agents**

- Immutable arXiv record: https://arxiv.org/abs/2601.06663v2
- Immutable PDF: https://arxiv.org/pdf/2601.06663v2
- Project page: https://safeprobench.github.io/safepro/
- Current official repository: https://github.com/UCSB-AI/SafePro
- Current public dataset: https://huggingface.co/datasets/kzhou35/SafePro
- The immutable arXiv page identifies Kaiwen Zhou, Shreedhar Jangam, Ashwin Nagarajan, Tejas Polu, Suhas Oruganti, Chengzhi Liu, Ching-Chen Kuo, Yuting Zheng, Sravana Narayanaraju, and Xin Eric Wang as authors. Submission history records v1 on 10 January 2026 and v2 on 13 January 2026 in `cs.AI`; the abstract contains no withdrawal notice.
- The abstract frames SafePro as safety-alignment evaluation for high-complexity professional tasks across multiple domains, with iterative task creation/review and mitigation experiments. The current project page reports 275 tasks across nine sectors and 51 occupations, run through CodeAct in OpenHands with web, file, and code tools under a fixed turn budget and summarized by an `Unsafe Rate`. These are discovery leads only: the immutable paper, release, task bytes, prompts, trajectories, judges, denominators, and correspondence were not fully audited.
- Structural inspection of immutable v2 HTML—not a full reading—confirmed sections on harmful-task creation, quality control, safety evaluation, metrics, a claimed safety knowledge–alignment gap, prompts, classifier mitigation, guardrails, limitations, dataset examples, and judge/safeguard prompts. Full review must determine whether safety is a prompt property, an attempted action, a realized state change, an artifact claim, or a model-judge label; whether useful refusal and safe completion are distinguished; and whether professional framing changes the construct beyond domain-themed harmful requests.
- Current release existence was verified, not audited. The project page links the release. GitHub redirects the historical `eric-ai-lab/SafePro` location to `UCSB-AI/SafePro`; acquisition-time HEAD/default branch `kaiwen` is `1239d48c0adc64d799b16d50dedb9772b191d253`. GitHub reports creation on 13 January 2026, latest push on 15 April 2026, and no recognized SPDX license. The public ungated Hugging Face dataset reports revision `e7b408a74ba33d0c445af9bc6aaaa212126683a9`, last modified 14 January 2026, with two listed files. Paper-time correspondence, repository history, data completeness, task licenses, and empirical replay remain unverified.
- Distinctness from existing work is bounded but real. ClawSafety studies ordinary-source prompt injection and separates exposure, adoption, attempted action, realized harm, severity, recovery, and benign utility. UnderSpecBench and the principal-authority slice distinguish authorization, information sufficiency, clarification/escalation, action, and consequence. SafePro instead claims broad professional harmful-task coverage and compares prompt, classifier, and guardrail mitigations in one released agent harness. Auditing it can test whether sector/occupation breadth and judge-assigned unsafe rates support a professional action-safety claim or only a configured harmful-instruction response claim.
- The project page appears to report models and results that may postdate immutable v2, making version identity a first-order issue rather than a reason to treat the current page as paper evidence. Full review must freeze paper, repository, dataset, model/configuration, judge, and result versions separately.
- Repository-wide searches for `SafePro`, `2601.06663`, and `review-safepro` found only the earlier deferred mention and no review or queue task.
- This is **metadata/abstract, section-structure, URL, release-existence, and duplicate triage only**. The PDF, appendices, code, data rows, professional source materials, task-authoring records, agent traces, judge calls, mitigations, and result tables were not fully read or audited. No claim is made that SafePro samples professional work, validates occupational hazards, measures realized harm, establishes safer agent behavior, or supports professional validity, capability, production fitness, safety, or readiness.

## Benchmark implication to test

Professional action-safety needs a typed chain rather than one unsafe-rate label: `work/hazard sampling frame → expert/source authority → public mandate and prohibited consequence → task transformation → configured agent/tools/environment → harmful-content exposure → interpretation and authorization judgment → clarification/refusal/safe alternative → attempted tool action → realized state/artifact delta → affected party and severity/reversibility → recovery and useful-task outcome → observer evidence → licensed claim`. Full review should test occupation/sector clustering; task realism versus domain theming; benign matched controls; refusal calibration and over-refusal; alternative safe paths; actual versus narrated tool actions; judge evidence views, dependence, and reliability; invalid environments; repeated trials and uncertainty; mitigation treatment identity; and whether classifier/guardrail gains preserve usefulness or merely suppress completion.

Transfer should reuse existing action-safety, authority, participation, configured-system, trace, artifact/state, metric, task-health, root/surface, and validity machinery. It should compare directly with ClawSafety and UnderSpecBench without creating a SafePro-specific schema or narrowing the benchmark to safety alone.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier professional-agent and safety benchmark research), B (authority/action/consequence validity), and D (comparative consolidation).
- **Evidence/artifact sought:** immutable full-v2 review plus pinned repository/dataset audit reconstructing task/hazard/expert lineage, configurations, action and state observations, judges, mitigations, results, uncertainty, and release correspondence.
- **Uncertainty clarified:** whether SafePro supports a bounded configured-agent harmful-task judgment claim or stronger professional action-safety and mitigation claims.
- **Mode/balance:** one low-priority review task restores a minimal research backlog while leaving the pending interaction consolidation and human decision ahead of it.
- **Duplication/scope:** follows a previously identified deferred candidate and tests a distinct professional-hazard/mitigation claim against ClawSafety and authority/action work; the nine sectors are an instrument frame, not a scope commitment.
- **Useful completion:** verify every sampling frame, role, observer, denominator, and version; separate harmful instruction, unsafe judgment, attempt, realized consequence, severity, recovery, refusal quality, and benign utility; preserve strict occupational, professional-validity, capability, production, safety, and readiness ceilings.

Added `review-safepro-professional-action-safety-validity` (priority 24). No second task was added.
