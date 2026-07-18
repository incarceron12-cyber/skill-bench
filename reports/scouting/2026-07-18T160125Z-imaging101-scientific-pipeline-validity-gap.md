# Scouting note — Imaging-101 scientific-pipeline validity gap

- **Timestamp:** 2026-07-18T16:01:25Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, official project/release surface verification, targeted primary-source searches, and exact repository duplicate searches only. The PDF/source body, 57 tasks, 6,022 release files, fixtures, tests, model outputs, figures, result tables, or expert-review records were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Imaging-101: Benchmarking LLM Coding Agents on Scientific Computational Imaging** — Siyi Chen, Jiahe Ying, Yixuan Jia, Yuxuan Gu, Enze Ye, Weimin Bai, Zhijun Zeng, Shaochi Ren, Binhong Gao, Yubing Li, Tianhan Zhang, and He Sun; arXiv:2607.10789v1.

- Immutable record/PDF/source: https://arxiv.org/abs/2607.10789v1 · https://arxiv.org/pdf/2607.10789v1 · https://export.arxiv.org/e-print/2607.10789v1
- Official project page: https://starpacker.github.io/agent-imaging-website/
- Public dataset: https://huggingface.co/datasets/starpacker52/imaging-101/tree/a9de559b54849a25988a8a0d8a5e869063a5a7a3
- Advertised implementation URL: https://github.com/HeSunPU/imaging-101
- The arXiv API identifies an immutable 12 July 2026 `cs.AI` submission; its summary contains no withdrawal or retraction notice. Record, PDF, and source endpoints returned HTTP 200 in this check, with 42,963 HTML bytes, 6,428,208 PDF bytes, and 7,145,137 source bytes.
- The abstract presents 57 expert-verified tasks across astronomy, biology, chemistry/material science, earth science, medicine, and physics. Each is said to originate in a peer-reviewed paper and be canonicalized into preprocessing, forward-physics, inverse-solver, and visualization stages. Planning, function-level unit-test, and end-to-end reconstruction tracks are reported across seven frontier models. Algorithm choice, physical conventions, and pipeline integration are named failure areas. These are author-stated claims awaiting full-paper verification.
- The project page and ungated Hugging Face dataset returned HTTP 200. The Hugging Face API reported revision `a9de559b54849a25988a8a0d8a5e869063a5a7a3`, 6,022 files, and visible task/result artifacts including numerical fixtures, evaluator scripts, ground truth, generated solver code, outputs, metrics, and visualizations. File completeness, licenses, paper-time correspondence, expert dispositions, oracle independence, and table reconstruction remain unaudited.
- The dataset card advertises `github.com/HeSunPU/imaging-101`, but both the page and `git ls-remote` returned repository-not-found/HTTP 404 on 18 July 2026. This is a time-bounded release observation, not proof that implementation never existed or will remain unavailable.
- Exact title, arXiv-ID, computational-imaging, forward-physics, and inverse-solver searches found no local review, queue task, or scouting note. LQCDMaster, SciAgentArena, Opti-Agent-Bench, ResearchClawBench, PaperBench, and paper-reproduction work are adjacent, but none audits this paper-source → canonical physical pipeline → stage fixture → integrated reconstruction chain.

## Why this is a narrow, useful gap

The reusable chain is:

`peer-reviewed scientific source and data → authorized task projection → expert-reviewed four-stage dependency graph → planning target → function fixture/oracle → generated stage implementation → integrated reconstruction → native numerical/visual artifact → independent physical/scientific check → expert acceptance → downstream research utility`.

This chain directly advances charter objectives A, B, and C. Imaging-101 could supply a cross-domain executable test of paper-grounded expert procedure and stagewise diagnosis. But source faithfulness, agreement with one canonical implementation, numerical equivalence, physical correctness, scientific usefulness, expert acceptance, and expertise transfer are different constructs. Array equality or a favorable image metric can reject legitimate coordinate, phase, scale, solver, or representation equivalents; conversely, compensating stage errors can produce a plausible final image while violating the intended physics.

A full review should reconstruct task candidate/admission and six-domain denominators; source/data provenance and rights; expert qualifications, independence, canonicalization, approval, disagreement, and rejection; stage dependency and integration semantics; planning-label authority; fixture generation and leakage; tolerances, units, shapes, coordinate/phase/sign conventions, stochasticity, and accepted equivalence classes; end-to-end metrics and visual evidence; model/harness/resource identity; retries, selection, invalidity, clustering, uncertainty, and cost; release completeness; and paper/result reconstruction. Scientific imaging is a bounded mechanism portfolio, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic scientific-agent and evaluation frontier), B (expertise-to-executable-instrument transformation), and C (stage, artifact, grader, and release machinery).
- **Concrete evidence:** immutable-v1 full-paper review plus pinned project/dataset audit and representative executable reconstruction where feasible.
- **Uncertainty clarified:** whether stagewise pipeline evaluation localizes domain-procedure and integration failures, or mainly measures conformance to one canonical numerical implementation and representation.
- **Mode:** narrow expansion. Before this addition the queue held one autonomous build and one human-decision task, with no research/review/source backlog; broad searching was unnecessary.
- **Duplication/scope check:** exact and mechanism searches were negative; adjacent scientific-work sources cover different projection and execution chains. Reuse existing source, projection, procedural-skill, artifact, trace, execution-validity, task-health, metric, and validity machinery; add no imaging-specific subsystem absent evidence.
- **Useful completion:** source-locate and test every source→pipeline→fixture→implementation→artifact→score edge, quantify valid-alternative and convention sensitivity, rebuild reported rows where feasible, and preserve strict scientific-correctness, transfer, reliability, utility, and readiness claim ceilings.

Added one task: `review-imaging101-scientific-pipeline-validity` (review, priority 52). No second source was queued.
