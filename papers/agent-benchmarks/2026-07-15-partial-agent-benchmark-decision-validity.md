# Partial agent-benchmark replay preserves a declared completed-record decision—not benchmark validity

## Source and review status

**Deep review of the complete immutable arXiv v1 HTML/full text, the official author-repository PDF, and a commit-pinned official reproducibility release.** I read the full nine-page paper and inspected the complete 643-file release at commit `1117405cfecdee730e01071d859d3c3383f22711`. I executed the public summary/conversion/paired-test path on a fresh Linux extraction and independently checked the release manifest.

- **Paper:** Wei-Jung Huang, *How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks*, arXiv:2607.12338v1, https://arxiv.org/abs/2607.12338v1
- **Version read:** immutable v1, submitted 14 July 2026; metadata contains no withdrawal/retraction notice
- **Date read:** 2026-07-15
- **Official arXiv HTML:** `data/papers/source/2607.12338v1/2607.12338v1.html` (SHA-256 `3a3f7e4734de7560e94de201e3a1cfc3a25b9a50c15337a9188fc02088f7321c`)
- **Local PDF:** `data/papers/pdfs/2607.12338v1-how-many-tasks-enough.pdf` (nine pages; SHA-256 `fddf147dbe940d7669b80be087582cc0d2f84d34fa0984e3feb23ab8682d9288`)
- **Local text:** `data/papers/text/2607.12338v1-how-many-tasks-enough.txt` (SHA-256 `aad0461a2847458a6d172746d79fc624461f089dd131a42e17ab3ee72dd3da56`)
- **PDF provenance caveat:** both canonical arXiv PDF routes returned HTTP 404 during acquisition. The preserved PDF is `paper/main.pdf` from the official pinned repository. Its title and content match the arXiv HTML, but it is not claimed byte-identical to an unavailable arXiv PDF.
- **Official release:** https://github.com/WilliamWJHuang/How-Many-Tasks-Are-Enough-for-Agent-Benchmark-Decisions/tree/1117405cfecdee730e01071d859d3c3383f22711
- **Release archive/provenance:** `data/sources/releases/2607.12338v1-partial-agent-benchmark/WilliamWJHuang-How-Many-Tasks-1117405.zip`; `data/sources/releases/2607.12338v1-partial-agent-benchmark/provenance.json`
- **Executed audit:** `data/sources/releases/2607.12338v1-partial-agent-benchmark/REVIEW_REPLAY_AUDIT.md`
- **Timing boundary:** the pinned commit predates v1 publication by about one hour. It is strong release correspondence evidence, but exact identity with every arXiv rendering input is not assumed.
- **Tags:** benchmark efficiency, partial evaluation, pairwise decisions, deferral, task coverage, replay, reproducibility

## One-sentence contribution

The paper supplies a useful decision-centered alternative to score compression: a partial task budget is “enough” only when a predeclared policy reproduces a fixed completed record's thresholded pairwise decisions within conditional error, group-coverage, and deferral limits—but the result is a retrospective replay property of selected complete cases, not prospective stopping validity, rank fidelity, diagnostic coverage, reliability, professional capability, or readiness.

## Why this matters for skill-bench

This review advances charter objectives A and C through a narrow benchmark-operation question: expensive artifact-heavy trials make reduced runs attractive, but “run 25% of tasks” is not an interpretable claim. The paper forces the evaluator to identify:

```text
completed task-level record
+ ordered configured-system comparison
+ decision threshold
+ task-selection/order policy
+ group-coverage rule
+ partial-decision rule
+ false-accept / false-reject limits
+ unresolved-comparison limit
→ smallest tested budget satisfying that declared replay contract
```

That is stronger than selecting a panel because it correlates with the full score or preserves a leaderboard rank. It also creates a strict claim ceiling. A reduced run may preserve a procurement-style pairwise decision while omitting rare safety failures, root-cause slices, artifact classes, or professional obligations. Conversely, a diagnostically rich panel may be valuable while being insufficient for a narrow thresholded comparison.

The transferable conclusion is therefore: **a reduced suite must be versioned against the decision it is meant to preserve. “Benchmark efficiency” is not one construct.**

## Research question and defensible claim boundary

The paper asks: given completed task-level outcomes, an improvement threshold, a group-coverage rule, a maximum unresolved rate, a task order, and a partial decision policy, what is the smallest tested task budget at which partial evidence matches the completed benchmark's pairwise decision often enough? (Sections 1 and 3, pp. 1–4.)

The strongest defensible claim is:

> For the selected complete public records and sampled reveal orders, the paper's coverage-aware bootstrap policy at its declared targets reaches different first-sufficient tested fractions across AppWorld, tau-bench, SWE-bench Verified, and SWE-bench Lite; task fraction alone cannot identify whether the partial policy preserved the fixed full-record pairwise decision.

The evidence does **not** establish:

- unbiased prediction of outcomes on new tasks or future benchmark forms;
- a prospectively valid sequential stopping rule or time-uniform error guarantee;
- preservation of full-suite scores, leaderboard ranks, diagnostic profiles, rare-critical coverage, or configured-system reliability;
- validity of the completed benchmark decision used as replay “truth”;
- independence of the two orientations of each system pair;
- transport from coding/app/tool-use binary outcomes to artifact-heavy, rubric-valued knowledge work;
- professional capability, comparative utility, deployment fitness, economic value, safety, or readiness.

## Methodology and system

### Replay unit and full-record target

For each task shared by tested system A and comparison system B, the paper defines paired binary difference `D_i = Y_i,A - Y_i,B`. The full-record paired improvement is the mean over the pair's overlapping task set. For threshold `δ`, the full decision is positive iff `Δ_full > δ`; equality is negative (Section 3, p. 3).

This is an **ordered one-sided question**. A-versus-B and B-versus-A are both counted, although they reuse the same outcomes. Table 1 reports:

| Source | Ordered pairs (unordered) | Task units | Positive full decisions at 0/5/10 pp |
|---|---:|---:|---:|
| SWE-bench Lite | 552 (276) | median overlap 300 | 275 / 199 / 154 |
| SWE-bench Verified | 156 (78) | median overlap 496 | 77 / 60 / 54 |
| AppWorld | 306 (153) | 585 task keys | 153 / 128 / 108 |
| tau-bench | 12 (6) | 278 domain-task items | 6 / 5 / 2 |

The systems are public leaderboard entries—model, prompt, tools, scaffold, retries, and other components—not base models (Section 1, p. 1). That configured-system framing is appropriate.

But the full record is treated as the reference label, not independently validated truth. A benchmark defect, invalid run, noncomparable environment, missing outcome, or bad grader can be reproduced perfectly by the partial policy. Decision preservation and decision validity remain separate.

### Partial policy and three outputs

At budget fraction `b`, the policy reveals `ceil(bN)` tasks from a precomputed order and returns positive, negative, or unresolved. The main rule uses a nonparametric bootstrap of the observed paired differences. It concludes positive when the observed mean is above `δ` and at most fraction `a` of bootstrap means lie at or below `δ`; negative is symmetric; otherwise it defers. The main `a` is 0.05, with 0.02 and 0.10 sensitivity (Section 3, pp. 4–5).

The bootstrap is a decision heuristic over the observed fixed subset. The paper correctly says its tail fraction is not a population guarantee. Reveal orders are sampled from the already completed record; this is replay, not online experimentation.

### Coverage rule

For group `g`, size `n_g`, total tasks `N`, and observed count `k_b`, the primary required count is:

`r_g(b) = max(1, min(n_g, floor(k_b n_g / N)))`.

Groups are repository for SWE-bench, split-by-difficulty for AppWorld, and domain for tau-bench. A slack sensitivity subtracts one from the proportional floor while still requiring every group (Section 3, pp. 3–4).

This blocks a glaring failure—concluding from only one repository or domain—but it is not construct coverage. Public metadata groups need not track hidden requirements, failure modes, artifact types, safety-critical checks, expert traps, or consequence severity. Proportional count also treats every member within a group as exchangeable and every group as requiring at least one item irrespective of decision relevance or consequence.

AppWorld's difficulty strata are themselves outcome-derived in the release: scripts estimate per-item pass rate across the same public system pool and quantile-bin difficulty before forming split×difficulty groups. That is acceptable for retrospective replay, but a live deployment needs a frozen historical/calibration population and a drift policy.

### Sufficiency rule and exact denominators

A tested budget is sufficient only when all four empirical rates pass:

- conditional false accept ≤ 0.05 among negative full decisions;
- conditional false reject ≤ 0.05 among positive full decisions;
- coverage failure ≤ 0.05 over all replay cases;
- unresolved rate ≤ 0.25 over all replay cases.

Unresolved cases stay in the full-decision-class denominators but count as neither wrong nor correct final conclusions (Section 3, p. 4). Thus error cannot look artificially low solely by removing deferrals from its denominator; the separate 25% unresolved ceiling addresses usefulness.

Under the main replay counts, the effective reveal-order denominators at each threshold/budget are:

- SWE-bench Lite: 552×500 = 276,000 replay cases; at 0 pp, 137,500 positive-class and 138,500 negative-class cases;
- SWE-bench Verified: 156×500 = 78,000; at 0 pp, 38,500 positive and 39,500 negative;
- AppWorld: 306×500 = 153,000; at 0 pp, 76,500 in each class;
- tau-bench: 12×2,000 = 24,000; at 0 pp, 12,000 in each class.

These large row counts are Monte Carlo replays of very few configured-system pairs, not independent empirical trials. For tau-bench especially, the inferential support is six unordered system pairs, despite 24,000 replay rows. The release does provide pair-cluster bootstrap intervals and an orientation collapse, but the minimum-sufficient-budget decision itself is a point-threshold crossing on a finite grid; it does not require confidence that the true replay rate lies below each target.

### Task order and selection

The main policy builds random stratified reveal orders before observing current partial effects. Comparators include uniform forced, stratified forced, tested-system cheap-first, bootstrap without coverage, paired-normal, exact McNemar at 0 pp, Serfling, and a diagnostic Neyman allocation using completed-record within-group variances (Sections 3–5, pp. 4–8).

The task order is not adaptive to current outcomes. The Neyman result is explicitly oracle-like because it uses full-record variances; a live implementation needs pilot or historical estimates. Cheap-first sorts on tested-system cost, making orientation part of both the decision and allocation treatment. Cost is available only for the small tau-bench grid.

### Missing, invalid, and selected records

The analysis is complete-case by construction:

- SWE-bench entries are retained when they report at least 95% of a split, then each system pair is evaluated on its inner-join overlap. Consequently `N`, repository mix, and the “full benchmark” can vary by pair.
- AppWorld uses all 36 public split bundles for 18 systems, but the release distributes a compact derived task table rather than raw bundles.
- tau-bench excludes banking-knowledge trajectories because retrieval configurations differ, chooses four entries, inner-joins shared domain/task keys, and uses a declared missing-infrastructure-reward imputation with sensitivity tables.

This is a defensible public replay sample, not a benchmark-wide missingness model. It lacks typed attempted/valid/invalid/missing/retried outcomes and no inclusion-probability or selection analysis supports generalization from the selected systems. Pair-specific overlap also means two A/B comparisons may target different task sets while appearing under one benchmark name.

## Evidence and results

### Main first-sufficient fractions

At `a=0.05`, error target 5%, coverage target 5%, unresolved target 25%, and the 5-percentage-point budget grid, the release tables reproduce the paper's main values:

| Source | 0 pp | 5 pp | 10 pp |
|---|---:|---:|---:|
| AppWorld | 15% | 15% | 15% |
| tau-bench | 25% | 30% | 35% |
| SWE-bench Verified | 90% | 90% | 90% |
| SWE-bench Lite | not found by 95% | 55% | 35% |

These are **first tested grid points**, not identified continuous minima. A reported 15% means the policy passed at 15% and did not pass at earlier tested points; it does not show that 14.9% fails or that the value is stable under another item sample, system population, threshold, or grouping.

SWE-bench Lite illustrates why deferral is separate: at 0 pp, error and coverage pass at 25%, but 55.92% remain unresolved; even at 95%, 27.25% remain unresolved. Verified leaves 93.64% unresolved at 25% and first falls to 24.22% at 90% (Section 5, pp. 6–7).

AppWorld's 15% result is not a universal “easy benchmark” fact. The same paper reports split-difficulty stratified forced evaluation requiring 50%, while uniform forced has 99.96% coverage failure at 25%. The 15% figure belongs to the joint selection-and-decision policy.

The tau-bench cost check usefully falsifies “cheap means sufficient”: tested-system cheap-first uses 11.51% of cost at a 25% task budget but has 100% domain-coverage failure and wrong decisions among only 12 ordered comparisons (Section 5, p. 7). The failure is vivid, but too small to estimate a general cost-coverage law.

### Sensitivity evidence

The paper varies bootstrap tail cutoff, replicate count, paired decision rule, orientation, grouping floor, threshold, and allocation. Important movements include:

- AppWorld 0 pp moves from 25% (`a=.02`) to 15% (`.05`) to 10% (`.10`).
- SWE-bench Lite 0 pp becomes sufficient at 75% on the coarse grid under one-task slack coverage, but remains unfound by 95% under the primary floor at `a=.05`.
- exact McNemar moves Verified 0 pp from 90% to 95% and tau-bench from 25% to 35%.
- keeping one orientation per unordered pair can produce almost one-sided classes—SWE-bench Lite has 275 positive and one negative at 0 pp—making one conditional error rate effectively unsupported.

The public execution reproduced the paired-test table and these headline decision-rule differences. This supports the paper's central qualitative claim that the task fraction is inseparable from the policy specification.

It also exposes a tuning issue: the release's sensitivity summarizer uses `policy_alpha` simultaneously as the bootstrap-tail cutoff and the replay-level conditional error target. The manuscript distinguishes `a` from `α`, even though both are 0.05 in the primary analysis. Sensitivity rows therefore change both the decision policy and the acceptance criterion; they do not isolate cutoff sensitivity. Primary results are unaffected because both are predeclared at 0.05, but interpretation of the `a` sweep should remain bounded.

## Release audit and reproducibility

### What executed

On a fresh extraction, all 15 Python scripts compiled after installing the three unpinned requirements (`pandas`, `numpy`, `matplotlib`) into an isolated temporary environment. The following public paths executed successfully:

- tau-bench ordered-grid summary: 24 truth rows, 30 aggregate rows, 10 sufficient rows;
- tau-bench reward sensitivity: 72 truth rows, 24 flip rows;
- SWE-bench conversion: 55,697 task rows, 218 submissions, 32,196 pair rows;
- AppWorld feasibility: 18 systems, 10,530 rows, 585 keys, 306 ordered pairs;
- public robustness summaries;
- paired-test diagnostics for all 1,026 directed comparisons.

The package includes the fine-grid main-policy pair tables used for the headline result, but the default quick path summarizes those derived tables rather than recomputing the 500/2,000-order fine sweep. The full raw replay is not self-contained: raw AppWorld bundles and tau-bench trajectories are omitted, and the PowerShell wrapper expects Windows-style execution. Included compact tables are enough to audit and regenerate many summaries but not to verify every raw-input transformation from the archived package alone.

### Manifest defect

`sha256sum -c MANIFEST.sha256` yielded **58 OK and 584 FAILED** on the official GitHub commit ZIP before replay scripts ran. Binary figures largely matched; many text artifacts did not. A CRLF transformation exactly recovered the manifest hash for the inspected AppWorld task table, but not for every sampled text file, so line endings explain part—not all—of the mismatch. The manifest is therefore not a valid integrity check over the GitHub archive as distributed. This does not negate the recomputed summaries, but it weakens byte-level release assurance and should be repaired with hashes generated from the published commit bytes plus a manifest self-check in CI.

### Reproducibility assessment

- **High** for inspecting the decision rule, included task-level/derived tables, pair tables, fixed seeds, and paper correspondence.
- **Moderate** for regenerating public summary and paired-test outputs from included derived records.
- **Low-to-moderate** for end-to-end reconstruction from upstream raw releases because large raw inputs are omitted, dependencies are unpinned, the primary wrapper is PowerShell-specific, and the manifest fails on most files.
- **Absent** for prospective stopping guarantees, new-form transport, or professional knowledge-work validity, none of which the release claims.

## Unique insight: efficiency is claim-indexed

Read against [Efficient Benchmarking](2026-07-09-efficient-benchmarking-ai-agents.md) and [Agent Psychometrics](2026-07-09-agent-psychometrics.md), this paper identifies a third reduced-evaluation target:

| Reduced-evaluation target | Required evidence | What it can preserve | What it may discard |
|---|---|---|---|
| Rank panel | held-out systems and pair/rank fidelity | ordering of systems under a specified population | exact scores, diagnostics, rare obligations |
| Psychometric/adaptive panel | response matrix, item model, task/system features, calibrated novelty handling | information about latent ability or predicted task response | unsupported model fit, novel interactions, causal difficulty |
| Decision-preserving partial run | fixed completed record, threshold, selection policy, coverage, conditional errors, deferral | one declared completed-record pairwise decision | ranks, scores, future forms, diagnostic and professional validity |

These are not interchangeable. A task can be uninformative for global ranking yet decisive near a procurement threshold. A rare safety task can be essential for release gating while reducing average rank efficiency. A psychometrically informative criterion can still be inadmissible if its grader lacks an authoritative artifact view.

For skill-bench, the reduced-run object should therefore be keyed to a **claim/use record**, not merely a suite version. The same task bank may legitimately expose different panels for triage, pairwise selection, regression detection, diagnostic localization, or safety gating, each with separate validity evidence.

## Limitations and validity threats

1. **Retrospective target leakage:** task outcomes, task groups, eligible systems, and full decisions are all known before replay. Neyman allocation explicitly uses full-record variance. This estimates replay compressibility, not a live policy's operating guarantee.
2. **Reference-label circularity:** the full benchmark decision is treated as truth. Full-run grader or environment defects are preserved rather than detected.
3. **Pair/population dependence:** two orientations reuse identical outcomes; many pairs reuse the same systems and tasks; reveal orders are Monte Carlo repeats, not new agent trials. Point-rate denominators greatly exceed independent system-pair support.
4. **Threshold fragility:** at 0 pp, one task can flip direction. Positive thresholds change class balance and the estimand itself, not merely tolerance around one stable truth.
5. **Grid-defined minimum:** first passing fractions are minima only over the tested grid and can cross a hard target due to simulation noise.
6. **No simultaneous/selection correction:** many budgets, thresholds, cutoffs, policies, groupings, and sources are inspected. The final minimum is selected from repeated point estimates without a confidence-bound or held-out policy-selection gate.
7. **Coverage proxy weakness:** repository, difficulty bin, and domain are available metadata, not validated construct partitions or consequence weights.
8. **Complete-case and overlap selection:** near-complete systems and inner-joined tasks define changing pair-specific populations; invalid and missing outcomes are not a typed estimand component.
9. **Small tau support:** six unordered pairs cannot support broad cost-ordering or threshold claims despite thousands of replay permutations.
10. **Binary-outcome dependence:** knowledge-work rubrics have ordinal/continuous criteria, dependencies, gates, alternative valid solutions, and observer abstentions; mean paired binary difference does not directly transport.
11. **No repeated configured-system trials:** task stochasticity, service failure, harness variance, and per-task reliability are frozen into one public record.
12. **Release integrity gap:** most manifest entries fail against the official archive; dependencies are not pinned; raw AppWorld/tau inputs are omitted.

## Transfer to skill-bench

### Reuse existing contracts; do not create a new subsystem

The requirements fit existing benchmark-bundle, task-health, metric-monitoring, validity-argument, and response-matrix machinery. No nonduplicate build task is warranted from this review.

A reduced-run specification should bind:

- immutable full-record and configured-system component hashes;
- ordered comparison and whether orientation reuse is included;
- pair-specific eligible task set and overlap/missing/invalid policy;
- public decision use and predeclared threshold/loss basis;
- panel/order policy, seeds, adaptation, and any historical/oracle inputs;
- group construction, authority, version, required counts, and critical/gating strata;
- positive/negative/unresolved semantics;
- conditional error denominators and unresolved/coverage denominators;
- tested budget grid and rule for selecting the first sufficient point;
- clustered uncertainty at task-family, system, and unordered-pair levels;
- distinction among retrospective replay, prospective stopping, and active selection;
- excluded interpretations: score, rank, diagnosis, reliability, professional capability, safety, and readiness unless separately validated;
- expiry triggers when task forms, system population, grader, environment, or difficulty distribution changes.

### Validation design for artifact-heavy knowledge work

Before using reduced runs operationally:

1. freeze one valid full response matrix with repeated configured-system trials and typed invalid/missing outcomes;
2. predeclare at least three separate uses: pairwise threshold decision, rank/portfolio comparison, and diagnostic/safety coverage;
3. derive candidate reduced policies on a calibration subset of systems/forms;
4. validate decisions prospectively on held-out configured systems and equivalent task forms;
5. require non-negotiable inclusion for critical safety/compliance checks rather than relying on proportional coverage;
6. compare whole-task, criterion, dependency-cluster, artifact-type, and failure-signature strata;
7. report effect on expert-review burden, wall time, cost, unresolved workload, and false decision loss—not only task fraction;
8. retain periodic full runs and invalidate the panel on drift, saturation, grader revision, or system-family change.

### Useful completion criterion

The general hypothesis is: **a claim-indexed partial policy can reduce evaluation cost while preserving one predeclared decision and bounded diagnostic/safety obligations on held-out equivalent forms.** Useful completion requires an empirical held-out replay/prospective comparison with repeated trials, clustered uncertainty, typed missingness, and separate claim ladders. This paper supplies the retrospective decision contract and useful failure cases; it does not supply that validation for skill-bench.

## Action items

1. During the next response-matrix consolidation, add an explicit `reduced_evaluation_use`/estimand link distinguishing rank, score, pairwise threshold, regression, diagnostic, and gate-preservation targets. This is a refinement of existing contracts, not a new queue task.
2. When the cross-pilot repeated-task matrix is available, preserve full records first; only then preregister a retrospective partial-decision replay with unordered-pair clustering and criterion/failure-signature coverage. Do not let this analysis replace the planned repeated trials.
3. Treat task-group coverage as an evidence-backed construct map: include artifact type, hidden-requirement family, failure signature, and criticality, with hard inclusion for noncompensatory safety/compliance gates.
4. Require released-package manifest verification against archive bytes before a source can support byte-level reproducibility claims.

## Bottom line

The paper repairs a real reporting error: “we ran 25% of the benchmark” says nothing about which decision that evidence supports. Its threshold + coverage + conditional-error + unresolved contract is a valuable operating primitive, and the release makes the main qualitative result auditable. The same precision sharply limits the claim: the study preserves selected pairwise labels from fixed complete public records. It neither validates those labels nor establishes a prospective stopping rule, rank preservation, diagnostic sufficiency, reliability, or professional capability. Skill-bench should adopt the decision contract, retain stronger construct/critical coverage, and validate reduced policies only after full repeated response matrices exist.