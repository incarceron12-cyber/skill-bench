# Scouting note — HCAST human-time and autonomy-validity gap

- **Timestamp:** 2026-07-17T14:20:19Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, exact local duplicate search, and official GitHub README/API-tree triage only. The paper body, task packages, DVC assets, human-baseline records, graders, agent runs, statistical analysis, and reported result rows were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**HCAST: Human-Calibrated Autonomy Software Tasks** — David Rein et al.; arXiv:2503.17354v1.

- Immutable record/PDF: https://arxiv.org/abs/2503.17354v1 · https://arxiv.org/pdf/2503.17354v1
- Official release: https://github.com/METR/hcast-public at inspected commit [`7a3795e7e060389bed9ed0bced7a2576b85185e4`](https://github.com/METR/hcast-public/commit/7a3795e7e060389bed9ed0bced7a2576b85185e4)
- The arXiv API identifies a `cs.AI` v1 submitted 21 March 2025. Its summary contains no withdrawal/retraction notice. The immutable record and PDF returned HTTP 200; the PDF response reports `application/pdf` and 1,442,718 bytes.
- The abstract describes 189 machine-learning-engineering, cybersecurity, software-engineering, and general-reasoning tasks; 563 human baselines totaling more than 1,500 hours; estimated human durations from one minute to more than eight hours; and frontier-agent success falling with estimated human duration. It frames duration as an intuitive way to ask whether an agent can be trusted with work taking a human a given number of hours. These are author-stated abstract claims awaiting full-paper audit.
- The official repository was public, unarchived, and had an untruncated 198-object tree. Its README says it releases source code for only a subset of paper tasks, uses the METR Task Standard and Inspect task bridge, stores some assets through DVC, and requests contamination precautions. The GitHub API reports no machine-readable SPDX license despite a repository `LICENSE` file and README statement of MIT licensing. These are release-triage observations, not a reproducibility audit.
- Exact repository searches for the title, arXiv ID, and distinctive name found citations in other acquired papers but no dedicated review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus already covers agent psychometrics, repeated-trial reliability, configured-system identity, task duration/cost, professional value, consequence promotion, and benchmark decision validity. It does not yet directly audit the influential **human-time calibration chain**:

`task/source population → selected executable task → recruited human and proficiency → matched resource/environment condition → observed attempt and censoring → human-duration distribution → fitted duration/difficulty relation → configured-agent success probability → reliability at a declared horizon → autonomy/trust decision → workflow and societal consequence`.

Human duration may be a useful, legible task covariate, but each promotion requires evidence. A longer human attempt may reflect setup, familiarity, strategy, debugging, task defect, or environment friction rather than a single latent capability difficulty. Human and agent conditions can appear identical while differing in prior knowledge, tools, latency, stopping rules, parallelism, incentives, and invalid-attempt handling. A cross-task success curve does not establish within-task operational reliability, safe unsupervised duration, labor substitution, professional validity, or trustworthiness. The released subset and DVC boundary also matter: a paper-wide result may be only partly inspectable, while public task exposure creates lifecycle and contamination constraints.

HCAST's software-heavy portfolio is a bounded case for reusable duration/calibration methodology, not a proposal to narrow `skill-bench` to software work or to adopt “time horizon” as its master scale.

## Charter decision filter and queue action

- **Objectives advanced:** A (benchmark frontier), B (valid expertise-to-evaluation and claim boundaries), C (task/baseline/trial/grader evidence contracts), and E (clarify what human-time metrics can support).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit of the official release, task-standard/DVC boundary, human baseline design, estimator, success graders, run denominators, and paper/release mismatch.
- **Uncertainty clarified:** whether human completion time supports a bounded difficulty covariate and configured-system comparison, and what additional repetition, clustering, censoring, matched-condition, decision-loss, and consequence evidence is needed before autonomy or trust claims.
- **Mode:** narrow expansion. One consolidation task and one human prerequisite were pending; this review is priority 67 and does not displace them.
- **Duplication/scope check:** adjacent reviews provide comparison machinery but do not audit HCAST or the human-time-to-autonomy inference. No new schema, software-only pilot, or benchmark-wide time scale is proposed during scouting.
- **Useful completion:** section/page- and release-path-grounded methodology, limitations, reproducibility/contamination status, relevance tier, and retain/repair/test implications, while keeping duration, difficulty, success, reliability, autonomy, trust, substitution, professional validity, consequence, and societal impact separate.

Added one task: `review-hcast-human-time-calibrated-autonomy-validity` (review, priority 67). No other candidate was queued.
