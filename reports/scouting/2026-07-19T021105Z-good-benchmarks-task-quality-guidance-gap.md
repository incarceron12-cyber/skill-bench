# Scouting note — practitioner task-quality guidance gap

- **Timestamp:** 2026-07-19T02:11:05Z
- **Evidence status:** arXiv abstract metadata, immutable endpoint checks, arXiv-HTML outbound-link inventory, web search, and exact local duplicate searches only. The PDF/source body, examples, references, or cited evidence were **not** deeply read, downloaded into the repository, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Good Benchmarks** — Ivan Bercovich; arXiv:2607.12217v1 (submitted 2026-07-13).

- Immutable record/PDF/HTML/source: https://arxiv.org/abs/2607.12217v1 · https://arxiv.org/pdf/2607.12217v1 · https://arxiv.org/html/2607.12217v1 · https://export.arxiv.org/e-print/2607.12217v1
- At scouting time all four endpoints returned HTTP 200, with observed response sizes of 37,648, 214,506, 58,664, and 10,061 bytes; the source endpoint resolved to `/src/2607.12217v1`.
- The metadata abstract argues that good tasks are correct, solvable, verifiable, well-specified, and hard for interesting reasons; that strong tasks describe practitioner-recognizable problems in practitioner language; and that tests should verify outcomes rather than prescribed approaches. These are author-stated claims awaiting complete critical review, not validated design rules.
- The immutable HTML exposes no paper-specific code, data, task set, or audit release. Its only substantive external evidence link visible in the outbound-link inventory is a METR reward-hacking post; the author's personal site hosts a related rendering at https://ivanbercovich.com/2026/good-benchmarks, which is not independent corroboration.
- Exact arXiv-ID, title, characteristic abstract phrases, task-quality conjunctions, queue, review, and scouting searches found no paper-specific duplicate. ECBD, Validity-Centered AI Evaluation, Terminal-Bench, adversarial verifier hardening, task-health, artifact-admissibility, and public-basis work are required comparators and make a critical nonduplication audit more useful than accepting the essay as a new checklist.

## Why this is a narrow, useful gap

The reusable chain is:

`practitioner-recognized work demand → source/task projection → public specification and solvability witness → construct-relevant difficulty → admissible solution set → outcome evidence view → verifier necessity/sufficiency and anti-reward-hacking tests → independent review → task-health disposition → bounded benchmark claim`.

This directly advances charter objectives A, B, D, and E. The source is unusually direct about benchmark authoring quality and appears to distill experience from building terminal-agent benchmarks. The useful question is not whether its maxims sound right, but whether they add operational distinctions, evidence, or failure tests beyond the repository's existing validity machinery.

The claim ceiling is important. Practitioner experience is valuable primary testimony but not independent empirical validation; a realistic-sounding task need not represent a work population; solvability by one reference path does not establish alternative admissibility; deterministic verification can reward the wrong outcome; outcome-only tests can omit required process, safety, or provenance obligations; and fewer curated tasks do not automatically support broad, reliable, or decision-valid benchmark claims.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark-design evidence), B (expertise-to-task and task-to-verifier method), D (critical comparison with accumulated machinery), and E (clear evidence/claim distinction).
- **Concrete evidence:** immutable-v1 critical full-text review with source locators and a recommendation-by-recommendation retain/repair/reject comparison against existing contracts and reviewed evidence.
- **Uncertainty clarified:** whether the essay contributes a nonduplicative operational authoring/review gate or primarily compresses already represented principles, and which claims rest on examples, citations, or practitioner testimony.
- **Mode:** narrow expansion/human learning. Queue inspection found one pending prospective build, two ordered consolidations, one human decision, and no review item; one low-priority review restores a small research buffer without repeating broad searches.
- **Duplication/scope check:** exact paper-specific searches were negative; adjacent work is explicitly required as comparison. Terminal/coding experience is evidence for a general task-quality hypothesis, not a benchmark-domain commitment.
- **Useful completion:** preserve acquisition provenance; distinguish testimony, examples, citations, and evidence; test recommendations against counterexamples and current executable contracts; add no schema or checklist unless a demonstrated obligation is absent.

Added one task: `review-good-benchmarks-task-quality-guidance` (review, priority 38). No second task was queued.
