# Scouting note — second-order validity-audit assurance gap

- **Timestamp:** 2026-07-18T19:28:35Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, targeted primary-source/release searches, and exact repository duplicate searches only. The PDF/HTML/source body, ten-cell study, five failure mechanisms, six-point gate, figures, analysis code, model outputs, or repair history were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Auditing the Audit: Five Failure Modes in Benchmark-Validity Audits** — Yanhang Li, Zhichao Fan, and Zexin Zhuang; arXiv:2607.02586v1; accepted at the TAIGR Workshop at ICML 2026.

- Immutable record/PDF/HTML/source: https://arxiv.org/abs/2607.02586v1 · https://arxiv.org/pdf/2607.02586v1 · https://arxiv.org/html/2607.02586v1 · https://export.arxiv.org/e-print/2607.02586v1
- The arXiv API identifies a 1 July 2026 `cs.AI` submission and describes one two-model/five-benchmark self-audit of perturbation-based construct-validity evidence. The abstract names five pipeline-failure classes and a six-point due-diligence gate under which all ten cells remain non-confirmatory. It explicitly presents the taxonomy as illustrative rather than exhaustive and the gate as a withholding/disclosure protocol rather than a benchmark-validity verdict. These are author-stated claims awaiting full-paper verification.
- At scouting time the immutable record, PDF, HTML, and source endpoints returned HTTP 200 with 42,145, 443,403, 399,506, and 101,630 bytes respectively.
- The arXiv record exposes no code/data link. Exact title, ID, author, and GitHub searches did not establish an author-identified release. Release absence is therefore an unresolved review question, not a finding that no artifact exists.
- Exact title, arXiv-ID, and mechanism searches found no local review, queue task, or scouting note. Existing validity arguments, provenance boundaries, adversarial-verifier checks, release reconstruction, and benchmark-audit work are adjacent, but none directly audits the **audit-to-assurance claim** pipeline itself.

## Why this is a narrow, useful gap

The reusable chain is:

`benchmark/construct claim → immutable benchmark and implementation identity → semantically valid perturbation → complete execution and denominator ledger → correctly oriented comparison → sensitivity/repair audit → disclosure gate → confirmatory, non-confirmatory, or withheld evidence → bounded governance use`.

This directly advances charter objectives A, B, and C. `skill-bench` increasingly relies on external release audits and its own validation reports, so it needs evidence for when those second-order instruments deserve trust. The likely boundary is also important: finding pipeline fragility in one selected safety-benchmark case study does not establish a complete audit taxonomy, benchmark invalidity, or governance readiness.

A full review should reconstruct F1–F5, the ten cells, perturbation semantics, model/benchmark/implementation versions, missingness and denominators, comparison orientation, repair history, sensitivity, and every due-diligence predicate. Where official artifacts permit, it should test source/version substitution, perturbation drift, label/polarity reversal, filtering, stale caches, and seed/comparison sensitivity, then map only nonduplicate consequences to existing provenance, metric, task-health, release, adversarial-grader, and validity machinery.

## Charter decision filter and queue action

- **Objectives advanced:** A (validity and audit frontier), B (claim-to-evidence warrants), and C (reproducible validation and release machinery).
- **Concrete evidence:** immutable-v1 full-paper review plus a timing-aware author-release audit and representative reconstruction/mutations where feasible.
- **Uncertainty clarified:** whether the proposed gate supplies independent assurance checks that improve artifact/workflow benchmark audits, or only a useful withholding vocabulary demonstrated on one co-designed case study.
- **Mode:** narrow expansion, lower priority than the pending v7 consolidation; the review backlog was empty.
- **Duplication/scope check:** exact searches were negative. The safety benchmarks are a bounded mechanism case, not a safety scope commitment.
- **Useful completion:** source-locate every audit→evidence→disclosure edge, verify inspectable cells, establish what the gate can and cannot license, and preserve benchmark-validity, governance, professional-validity, production-fitness, and readiness claim ceilings.

Added one task: `review-auditing-the-audit-validity-evidence` (review, priority 49). No second task was queued. `Rubrics on Trial` (arXiv:2607.15092v1) was triaged but deferred because its query-only synthetic-rubric mechanism overlaps the already deep GrowLoop, co-evolving-rubric, generated-evaluator, and rubric-meta-evaluation coverage more than this second-order assurance gap.
