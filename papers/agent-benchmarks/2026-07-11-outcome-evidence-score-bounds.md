# Can Agent Benchmarks Support Their Scores? — outcome evidence, partial identification, and claim boundaries

**Source URL:** https://arxiv.org/abs/2605.10448v1  
**Citation:** Shanshan Gao and Liyi Zhou, *Can Agent Benchmarks Support Their Scores? Evidence-Supported Bounds for Interactive-Agent Evaluation*, arXiv:2605.10448v1 (11 May 2026), 20 pages.  
**Local PDF read in full:** `data/papers/pdfs/2605.10448v1-outcome-evidence-score-bounds.pdf` (SHA-256 `52640fdfc5a6f15490c99007b6adb80642c38104a7dbda32fc0645e010afa260`).  
**Local full-text extraction read:** `data/papers/text/2605.10448v1-outcome-evidence-score-bounds.txt` (SHA-256 `c5ea4e79ea9b6245bfe3c72d00898cabd9cb065a7f1d6d2753a52d647f2aaea5`).  
**Official release inspected:** acquisition-time commit `470805fc8cb4ec3103d4bc18b7816e11f5bc678f` (19 May 2026), eight days after immutable v1. Provenance and targeted files are under `data/sources/releases/2605.10448v1-evidence-bounds/`. The 6.5 GB release could not be mirrored completely; the recursive GitHub tree was truncated, so release findings below are limited to the README, manifest, schemas, prompts, checklist locks, guardrails, and layout verifier fetched by immutable commit. This is not evidence of exact manuscript-time code identity or a full result replay.

## Bottom line

The paper's distinctive contribution is not another verifier. It makes **outcome decidability a property of each completed record**, separate from the native evaluator's label, and then refuses to turn missing evidence into agent success, agent failure, or dropped data. A pre-locked, source-grounded checklist asks what retained artifacts would decide the benchmark's own claim; each record receives Evidence Pass, Evidence Fail, or Unknown; and the fixed completed-record denominator yields a partial-identification interval `[P/N, (P+U)/N]` (Sections 2–3, pp. 3–5). This is directly useful to skill-bench: a score should carry an evidence-support envelope, not merely a grader verdict.

The empirical audit is unusually concrete. Across 1,282 record slots (1,582 episodes because AgentDojo has paired arms), the authors find three materially different regimes: wide uncertainty from missing authoritative state (AndroidWorld, AgentDojo), narrow bounds but native evaluator conflicts (τ³-bench), and mostly decisive/native-aligned records (AppWorld), with MiniWoB showing that decidability still does not establish construct adequacy (Tables 1–3, pp. 5–8). But the study does **not** validate a universal evidence ontology, estimate population capability, establish statistical model rankings, or demonstrate reproducibility from the full release. Its strongest claims are conditional and sample-bound.

## One-sentence contribution

The paper adds a locked outcome-evidence checklist and Pass/Fail/Unknown reporting layer that turns missing evidence into explicit partial-identification bounds rather than silently coercing or dropping uncertain records.

## Research question

The research question is: **When an interactive benchmark prints a binary result and aggregates it into a success rate, do its stored artifacts actually decide the outcome claim represented by that result?** The paper separates:

1. **native label** — what the released evaluator says;
2. **identification** — whether retained evidence decides the native claim;
3. **alignment/conflict** — whether task, target construction, evaluator, oracle, and reward encode the same claim;
4. **stronger measurement** — additional process, collateral-effect, identity, privacy, or completeness requirements not licensed by the native claim.

## Unique insight

That separation is the paper's unique insight. A plausible action trace is not necessarily evidence of persistent state; a decisive trace may contradict the evaluator; and a perfectly decisive native result may measure a weaker construct than users infer (Sections 2, 5–6, pp. 3, 6–9). The method contracts a claim rather than silently strengthening it.

## Methodology and system

### Claim reconstruction and locked checklist

For each case unit, an LLM-assisted drafter reads the user goal, task/policy, evaluator or oracle, and schemas. It records the native binary claim, official source, decisive artifacts, success/failure/Unknown rules, and any stronger conditions. Humans source-check fields against a hierarchy: evaluator semantics first, task text/policy second, schema constraints third; annotator intuition cannot enter native bounds (Section 2, pp. 3–4). Checklists are locked before outcome scoring and cannot adapt to observed model results (Section 4, pp. 5–6).

The inspected release schema operationalizes this distinction. `case_checklist.schema.json` requires `user_goal`, `benchmark_success`, `checked_by`, decisive artifact questions, and explicit success/fail/undecided rules, with source pointers or rationale; stronger conditions occupy a separate object. External `locks/cases.jsonl` hashes case packets, checklists, prompts, and schemas rather than cluttering the semantic checklist (`source_code/README.md`, lines 5–19 and 106–119). This is a useful semantic/operational separation.

### Evidence adjudication

A read-only LLM-assisted scorer applies each locked checklist to stored traces, calls, evaluator I/O, messages, and available post-state. The released `evidence_score.schema.json` requires a native `S/F/U` verdict, reason, and pointers; stronger conditions separately permit `NA/S/F/U` and criterion-level supported/contradicted/undecided statuses. Native labels are explicitly barred as decisive evidence by the release pipeline (`source_code/README.md`, lines 130–169). Humans review disagreements, Unknowns, stronger downgrades, and sampled triggers; scorer/checklist errors are corrected before aggregation, while benchmark-facing conflicts remain findings (Section 3, p. 4; Appendix D, pp. 15–16).

### Estimand and denominator

For an agent-domain cell, `N=P+F+U`. The all-record supported performance set is:

`Perf ∈ [P/N, (P+U)/N]`, with width `U/N`.

This is a worst-case partial-identification interval, not a confidence interval. `P/(P+F)` is only a decidable-record diagnostic because dropping Unknowns can create agent-dependent post-selection. Only infrastructure or pre-run failures leave the denominator; timeouts, malformed answers, tool misuse, and post-start aborts remain failures when evidence supports the native failure (Section 3, pp. 4–5; Section 4, p. 6). Model ordering is supported only where one interval's lower endpoint exceeds the other's upper endpoint; this is an identification rule, not a significance test (Section 3, p. 5).

## Evidence and observed failure modes

The study freezes random case samples before inspecting outcomes: 100 cases × three models for AgentDojo, AppWorld, τ³-bench retail, and MiniWoB; 41 AndroidWorld cases × two models under a USD 250 benchmark cap. Models are GPT-5.4, Claude Opus 4.7, and DeepSeek V4 Pro, run once per case/model at temperature zero with a 4,096-token output cap, 120-second timeout, and two retries. Ten cases per benchmark receive one GPT-5.4 rerun as a stability probe, not an uncertainty interval (Section 4, pp. 5–6).

Central results (Table 2, pp. 6–7):

- **AndroidWorld:** 13/28/41 P/F/U over 82 records; bound `[15.9%, 65.9%]`; 50% Unknown; two target-set conflicts. Missing evaluator-time app/database/media/filesystem/content-provider state dominates.
- **τ³-bench retail:** 212/87/1 over 300; `[70.7%, 71.0%]`; 24 conflicts despite narrow bounds. Required subchecks can be omitted from scalar reward, attempted actions accepted as completion, and DB/action criteria can disagree.
- **AppWorld:** 220/80/0; `[73.3%, 73.3%]`; no native conflicts after audit. Twelve initially flagged successes were the paper's own scorer/checklist errors about supervisor bookkeeping, illustrating why correction lineage matters.
- **AgentDojo:** 191/59/50; `[63.7%, 80.3%]`; 16.7% Unknown; four conflicts. Paired utility/security claims often lack arm-indexed final state, side-effect receipts, or non-effect evidence.
- **MiniWoB:** 118/182/0; `[39.3%, 39.3%]`; two conflicts. Retained DOM contradicts success in `find-greatest`, while copy/paste and scrolling cases expose stronger construct shortcuts rather than native evidence failures.

The failure taxonomy is operational rather than merely descriptive. Unknown reasons identify missing authoritative post-state, paired-arm comparability, durable side-effect receipts, or non-effect evidence (Tables 4–5, pp. 12–13). Conflicts identify ignored required subchecks, wrong-state/action proxies, inconsistent internal criteria, target-set construction errors, or omitted task requirements (Tables 6–7, pp. 13–14). The τ³ task 50 case is particularly strong: retained output says the required transfer action failed while aggregate reward remains 1.0 because its reward basis excludes that action check (Appendix C.1, pp. 13–14).

The two-researcher audit corrected 48 of 126 reviewed flagged records (8/6 AndroidWorld, 53/10 τ³, 15/12 AppWorld, 14/0 AgentDojo, 36/20 MiniWoB; reviewed/corrected), but the paper does not report independent pre-adjudication agreement or per-reviewer labels (Table 9, p. 16). These correction rates are evidence that the audit layer catches mistakes, but also that provisional LLM/checklist judgments are not a trustworthy unattended grader.

## Reproducibility and operational realism

### What is inspectable

The paper identifies frozen samples, denominator policy, model settings, source hierarchy, checklist lock timing, common ledger fields, prompt/schema hashes, and audit triggers. The official release exposes the semantic schemas, deterministic guardrails, 441 checklist locks, scorer prompts, package scripts, and release checks. The schema cleanly separates native and stronger claims and requires artifact pointers. The README states that an offline smoke test and packaged-case rescoring are available.

### What is not established

The acquisition-time repository commit postdates arXiv v1 by eight days. The repository itself states that `evaluation_artifacts/` is about 6.5 GB. A bounded archive acquisition exceeded 667 MB and timed out; the GitHub recursive tree is truncated at 27,447 entries and more than 967 MB of visible blobs. Thus this review inspected targeted implementation contracts but did not replay aggregate tables or verify every record ledger. The public release may be substantial, but release size, untagged timing, and GitHub-tree truncation materially raise archival and independent-reproduction burden.

More importantly, the paper gives no independent double-scoring reliability statistic, no blind allocation protocol, no adjudicator-disagreement rate, and no validation of checklist completeness against an external domain authority. “Two researchers cross-validate” is process evidence, not measured reliability. Since the same authors design the checklist method, choose source interpretations, adjudicate flags, and report benchmark conflicts, interpretation bias remains possible.

## Limitations and validity threats

1. **Conditional bounds are not capability intervals.** `[P/N,(P+U)/N]` bounds the fraction of sampled completed records compatible with stored evidence under the locked checklist. It excludes sampling uncertainty, repeated-run variability, model-version uncertainty, grader error, and benchmark-to-domain generalization (Sections 3–4, pp. 4–6).
2. **Native semantics can be underspecified.** Following evaluator semantics first may faithfully audit a weak proxy while underweighting the user-facing task. The stronger layer exposes this but does not resolve which interpretation benchmark users should privilege (Sections 2 and 6, pp. 3, 8–9).
3. **Checklist construction is itself a measurement intervention.** Locking prevents outcome-conditioned edits, but LLM drafting plus author adjudication can still omit decisive evidence, encode source-hierarchy choices, or over-/under-classify stronger requirements. The high correction count demonstrates material fallibility.
4. **No measured scorer/reviewer reliability.** The paper reports reviewed and corrected totals, not independent agreement, uncertainty over labels, or sensitivity of aggregate bounds to alternative valid checklists.
5. **One execution per primary case/model.** Temperature zero does not eliminate service, environment, or agent stochasticity. Ten reruns per benchmark cannot estimate model-cell reliability and are not analyzed as such.
6. **Sample-limited and heterogeneous selection.** Four 100-case samples and one cost-censored 41-case sample support audits of those samples, not benchmark-wide defect prevalence. AndroidWorld uses fewer models and is excluded from leaderboard analysis.
7. **Conflict discovery is trigger-dependent.** Human review focuses on disagreements, Unknowns, stronger downgrades, and sampled checks. Unless the sampled-trigger rate and false-negative audit are fully reported, conflicts among apparently aligned records may be missed.
8. **Ranking rule lacks statistical inference.** Non-overlapping worst-case evidence bounds support direction conditional on the sample, but do not establish population ranking; overlapping bounds mean unresolved, not equal (Table 3, p. 8).
9. **Negative claims require closure assumptions.** “Nothing happened” needs a complete authoritative state or signed diff. The taxonomy names this correctly, but real knowledge-work environments often lack a closed world; evidence sufficiency must state coverage and authority, not just retain another log.
10. **Operational cost is understated by API spend.** The reported paid-call upper bound (USD 370.91) excludes two-researcher checklist and adjudication labor, benchmark setup, artifact storage, and the cost of handling a multi-gigabyte release (Section 6, p. 9).

## Why this matters

The method supplies a missing bridge between skill-bench's artifact observations and the aggregate claims made from them: each score must expose whether authoritative evidence supports, contradicts, or cannot decide its outcome before that score enters a metric or validity argument.

## Transfer to skill-bench

### Retain

1. **Record-level evidence state distinct from outcome state.** Preserve native grader output, then separately record `supported`, `contradicted`, or `unknown/insufficient_evidence`, with decisive artifact pointers. This aligns with the existing artifact-view admissibility and evidence-state machinery but sharpens its aggregation consequence.
2. **Fixed denominator and unknown bounds.** For any score family aggregating records, publish `P/F/U`, `[P/N,(P+U)/N]`, Unknown share, exclusion reasons, and a counted-only diagnostic only when clearly labeled conditional on decidability.
3. **Native/stronger claim split.** A private check may test fair consequences of public requirements, but must not silently rewrite the native construct. Keep native score support, professional-quality extensions, safety/collateral constraints, and process claims as separate validity arguments.
4. **Checklist locking and lineage.** Freeze claim text, source hierarchy, decisive artifacts, rules, prompt/schema hashes, and reviewer state before scoring; revisions create a new instrument version rather than rewriting old results.
5. **Unknown reason as repair target.** Type authoritative post-state, paired-view comparability, durable side-effect receipt, and non-effect/coverage gaps separately from substantive agent failures and benchmark conflicts.

### Repair

1. **Represent uncertainty on the audit layer itself.** Store independent reviewer labels, agreement, adjudication transitions, alternative-checklist sensitivity, and sampled false-negative audits. A corrected consensus label should not erase disagreement.
2. **Bind every decisive artifact to authority and coverage.** “Final state” is insufficient: identify object/entity, timestamp, transformation, completeness/closed-world basis, arm, and whether the artifact proves effect or non-effect.
3. **Separate five levels:** native evaluator label; evidence support for that label; benchmark conflict; stronger professional requirement; and the higher-order validity/capability claim. Do not collapse a narrow supported native claim into professional readiness.
4. **Carry two uncertainty axes.** Outcome-evidence bounds and sampling/repetition uncertainty answer different questions. Report both rather than treating bound separation as a leaderboard confidence result.
5. **Make exclusion causality explicit.** Pre-run/infrastructure exclusions require typed evidence that the agent never received a valid task; post-start failures remain in denominator. Environment-validity failures should not become agent failures, but neither should they silently disappear.

## Concrete repository changes

No new schema task is warranted. Existing benchmark-bundle artifact views/check outcomes, metric-monitoring denominator and missingness policy, task-health adjudications, and validity arguments can absorb the requirements. The next consolidation/build pass should test one synthetic aggregate where:

- one record is supported success;
- one is supported failure;
- one native success lacks authoritative post-state;
- one native failure is contradicted by decisive state;
- one run is a proven pre-run environment failure;
- one stronger professional requirement fails while the native claim remains supported.

Acceptance requires preserving all six states without coercion, computing native score and evidence bounds over the correct fixed denominator, excluding only the proven pre-run failure, refusing a directional ranking when intervals overlap, and preventing stronger-condition failure from mutating the native-evidence label. This tests general aggregation behavior across domains without creating another subsystem or narrowing skill-bench to computer use.

## Decision impact

This review strengthens the charter's plural-measurement and validity principles: **a grader result is not yet evidence support, and evidence support is not yet a capability claim**. For skill-bench, useful benchmark reports should expose (a) what outcome was claimed, (b) which authoritative views could decide it, (c) whether those views support, contradict, or fail to decide it, (d) what benchmark/evaluator conflict was observed, and (e) which broader professional interpretations remain excluded. The practical addition is not another point score; it is an evidence-support envelope around every aggregate.