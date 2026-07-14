# Scouting note — repeated agent-evaluation reliability gap

**Timestamp:** 2026-07-14T18:58:41Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 220 tasks: 215 completed, four blocked, and one pending human decision; no source/research/review task remained. The newest empirical build is blocked before model calls because its prospectively frozen repeated-task protocol cannot be pushed. Existing reviews cover repeated operational profiles and trajectory confidence, but not a primary measurement study of within-task versus between-task variance or repeat-budget convergence.

## Substantive finding (triage only)

**Stochasticity in Agentic Evaluations: Quantifying Inconsistency with Intraclass Correlation**

- Immutable arXiv record: https://arxiv.org/abs/2512.06710v1
- Immutable PDF: https://arxiv.org/pdf/2512.06710v1
- Immutable HTML: https://arxiv.org/html/2512.06710v1
- OpenReview record: https://openreview.net/forum?id=CzQ2UGInm5
- Paper-declared implementation: https://github.com/youdotcom-oss/stochastic-agent-evals
- The arXiv API identifies Zairah Mustahsan, Abel Lim, Megna Anand, Saahil Jain, and Bryan McCann; v1 was submitted 7 December 2025 in `cs.AI`, with no later arXiv version or withdrawal notice. The versioned abstract/PDF, OpenReview record, repository, and GitHub API URLs returned HTTP 200 during this run.
- The **v1 abstract** proposes intraclass correlation coefficient (ICC) to decompose observed evaluation variance into between-query difficulty and within-query agent inconsistency. It reports repeated GAIA and FRAMES experiments, model-dependent ICC ranges of 0.304–0.774 and 0.4955–0.7118 respectively, convergence at 8–16 trials for structured tasks and at least 32 for complex reasoning, and an Evaluation Card extension. These are author-reported abstract claims, not independently verified findings.
- This is directly relevant to the blocked repeated cross-pilot matrix, but it is not a turnkey sample-size rule. Full review must establish the exact ICC form, unit and random-effects assumptions, outcome types, repeat balance, task/model hierarchy, missing and service-failure handling, confidence intervals, convergence target, stopping rule, and whether binary or bounded agent scores make a Gaussian variance decomposition misleading. Dataset/configuration-specific stabilization cannot be promoted into a universal repeat budget without transport evidence.
- The official repository is a non-fork MIT project created 14 October 2025. Its current `main` is commit `50bd2cec421320e51a042498a4fb7e8482a70fb5` dated 17 December 2025—after arXiv v1—and GitHub reports no tags or releases. It must therefore be audited as a post-v1 implementation rather than assumed to be the exact paper-time artifact.
- Repository-wide duplicate search found no record for arXiv `2512.06710`, the title, OpenReview ID, or official repository. This differs from Agent Reliability Profile’s plural operational outcome profile and Agentic Confidence Calibration’s prediction of one trial: ICC estimates repeat consistency across sampled outcomes and tasks.
- This is **metadata, abstract, URL, release-location, and duplicate triage only**. The paper, appendices, experiment records, task IDs, configurations, repeated outputs, statistical code, tables, and Evaluation Card implementation were not fully read or audited. No claim is made that ICC is correctly specified, results reproduce, the reported repeat counts transfer, or the method establishes capability, professional validity, production reliability, safety, or readiness.

## Benchmark implication to test

Repeated evaluation needs a typed hierarchy: `task source/family → immutable task form → configured system/provider/time → declared attempt and service validity → grader and outcome/severity observation → within-form repeat distribution → between-form/family variation → estimator assumptions and uncertainty → repeat-budget decision → bounded reliability claim`. Test-retest consistency, probability of useful success, grader reliability, calibration, and operational decision utility are separate estimands.

A full review should test ICC specification and identifiability for binary/ordinal outcomes; task, family, model, and infrastructure clustering; unequal/missing repeats; correlated failures; outcome-conditioned admission; service invalids; provider drift; convergence metric and tolerance; bootstrap or model-based uncertainty; sensitivity to difficulty mixture; and whether an accuracy increase with unchanged or lower ICC can still be valuable under an explicit loss function. Existing configured-system, task-health, metric, reliability, and validity machinery should host any transfer; no ICC-specific schema follows from triage.

## Charter decision filter and queue action

- **Objectives advanced:** A (agent-evaluation measurement frontier), B (measurement-to-reliability claim validity), and C (evidence for executable repeated-trial design).
- **Evidence/artifact sought:** immutable-v1 and pinned post-v1 release audit, including at least one recomputed released result if artifacts permit.
- **Uncertainty clarified:** whether ICC and the reported convergence analysis validly guide future repeated multi-form knowledge-work trials or only describe selected GAIA/FRAMES configurations.
- **Mode/balance:** one review task restores a minimal research backlog and directly informs a current empirical bottleneck; no broad search or parallel bundle was added.
- **Duplication/scope:** complements operational reliability and trajectory-confidence work; GAIA/FRAMES are measurement cases, not a benchmark-scope commitment.
- **Useful completion:** separate consistency, success probability, grader reliability, calibration, and decision utility; preserve hierarchy, invalid/missing outcomes, estimator assumptions, uncertainty, and strict claim ceilings.

Added `review-stochastic-agent-eval-icc-validity` (priority 31). No second task was added.

## Operational note

The required initial `git pull --ff-only` could not authenticate to the HTTPS GitHub remote (`could not read Username`). Local `main` is 17 commits ahead of the recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
