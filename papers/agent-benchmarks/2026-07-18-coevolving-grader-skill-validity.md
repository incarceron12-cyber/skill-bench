# Who Grades the Grader?: anchor discipline exposes evaluator collapse, but the reported “locked” test participates in skill selection

## Source and review status

**Deep review of the complete immutable primary source; claimed empirical release unavailable or unlinked.** I read the full 13-page arXiv v1 paper, including appendices, and audited the complete seven-file arXiv source tree. The metadata contains no withdrawal or retraction notice. Appendix H says the authors release all code, task data, split builders, judge protocols, and result files needed for end-to-end regeneration, but neither the paper, metadata, nor source tree provides a release URL or those artifacts. Exact-title, arXiv-ID, system-name, web, and GitHub searches found no verifiable author-owned empirical repository at review time. Numerical and implementation claims below are therefore manuscript-reported, not independently replayed.

- **Paper:** Xing Zhang et al., *Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents*, arXiv:2607.12790v1 (14 July 2026), <https://arxiv.org/abs/2607.12790v1>
- **Local PDF:** `data/papers/pdfs/2607.12790v1-coevolving-grader-skill.pdf` (13 pages; SHA-256 `cf7aca4728e25c52ca1947b211d3fd9709ea741891c282daaec9efbfd2d4b05f`)
- **Full local text:** `data/papers/text/2607.12790v1-coevolving-grader-skill.txt` (77,455 bytes; SHA-256 `db3467d0f54e64ef51dcb7f8d99791aa14651a8f1f7d1044501569939a98e4cd`)
- **Metadata:** `data/papers/source/2607.12790v1-metadata.xml` (SHA-256 `fa934015e106cea121781b8c4eb4447894bc46b4c5ae26c2c3397a020e282053`)
- **Complete arXiv source:** `data/papers/source/2607.12790v1-source.tar.gz` and `data/papers/source/2607.12790v1/` (archive SHA-256 `c8a00bdd45769b26972ac59ffe1b48969e29f825a6a37a446ded5d8099763f54`)
- **Release-search provenance:** `data/sources/releases/2607.12790v1-coevolving-grader-skill/provenance.json`

## One-sentence contribution

The paper offers a useful failure-expecting pattern—compose inspectable drawback detectors, constrain them with a tiny labeled anchor, keep an outer audit, and explicitly demonstrate that removing anchor guards yields a vacuous always-pass metric—but its stronger claim that co-evolution recovers 88–110% of oracle-enabled skill lift is not clean held-out evidence because the skill loop repeatedly evaluates against, selects peaks on, and reportedly rolls back using the same “locked” test set, while the report-quality audit is post-hoc, same-family, tie-excluding, and unreproducible from the public artifact.

## Why this matters for skill-bench

This review advances charter objectives A, B, and D through a bounded identification case. Self-improving agents are not the benchmark’s target domain. The reusable issue is broader:

> When an intervention and its measurement instrument both change, what evidence separates better work from a more permissive observer, repeated fitting to a fixed panel, and intervention–instrument collusion?

The paper is unusually valuable because it reports a **negative evaluator result** that headline task scores conceal. With anchor guards disabled, the report metric’s internal objective becomes 1.000, it passes 94–100% of training attempts, and its metric is described as vacuous; nevertheless, the associated skill loop still attains held-out task scores similar to the anchored arm (paper pp. 7–8; extraction lines 327–360). Thus improved endpoint score does not validate the evolving grader, and grader agreement does not by itself validate improved work. `skill-bench` should preserve at least four objects:

```text
intervention state (Skill bank)
→ work attempt and artifact/state
→ evolving observer verdict
→ frozen independent measurement and bounded claim
```

Each transition needs its own version, information boundary, and evidence. A detector can be useful for routing failure capsules without being accurate enough for release scoring; an intervention can improve despite a broken training metric through practice alone; and a frozen measurement can still cease to be a valid holdout if it drives rollback, checkpoint choice, repeated analysis, or post-hoc repair.

This is nonduplicate relative to the ACE and self-evolving-agent reviews, which distinguish agent evolution from candidate benchmark lessons and released instrument changes, and GrowLoop, which studies rubric/case co-evolution from human seeds. This paper adds a direct controlled collapse: **anchor removal breaks evaluator validity without visibly breaking the agent score.** It also exposes the opposite threat: labeling a set “locked” does not keep it out of optimization when the skill loop uses it for rollback and peak reporting.

## Methodology and system

### Task families, units, and configured roles

The study uses three task families (paper pp. 4–5, 10–11; lines 197–245, 496–567):

1. **MBPP+ code generation:** a one-paragraph programming prompt; hidden EvalPlus unit tests provide the strongest reference.
2. **Spider 2.0-Snow text-to-SQL:** a question plus rendered schema catalog and domain notes; a candidate query is executed against a hosted Snowflake warehouse and compared with a stored gold result while ignoring column names and order.
3. **Report generation:** one analyst-report section from a caliber contract, evidence cards, and a metric vocabulary. RAQS scores evidence grounding, inline metric-tag discipline, claim calibration, structure, and style, but the authors explicitly treat it as a partial reference rather than ground truth.

The hard-subset construction screens MBPP+ and Spider tasks with five frozen-solver samples, drops tasks passed in all five, stratifies the remainder by pass rate, and uses train/dev/test counts of 60/10/40 and 59/10/40. Reports use 73/10/48. Every dev anchor has five clean and five failed examples. The frozen solver is a single direct Claude Opus 4.7 call without tools, iteration, or chain-of-thought scaffolding. Claude Opus 4.7 also fills every other in-loop role—skill and detector synthesis, teacher, composer, and semantic judge op—while Claude Opus 4.8 is the report task’s outer pairwise judge (p. 5; lines 213–245).

This is a configured single-model-family package, not evidence about general metric evolution. The paper does not report immutable model endpoints, dates, sampling settings, prompt hashes, retry policies, call failures, token use, monetary cost, or role-specific seeds. “Three seeds” therefore does not establish reproducibility of many stochastic model calls.

### Metric representation

An atomic operation maps `(task, output, shared context)` to `drawback`, `clean`, or `abstain`. Static operations parse artifacts; execution operations run code or SQL; judge operations ask one narrow semantic question. A fixed root checks basic structure. Candidate metrics are expression trees over operations using any-of, all-of, or K-of-k logic, excluding abstentions from combination and abstaining if every child abstains (pp. 3–4; lines 133–163).

This representation is a genuine contribution. It makes criterion identity and abstention inspectable, can separate mechanical from semantic evidence, and admits leave-one-out operation analysis. But “deterministic” is overstated. Final MBPP+ and Spider expressions include `spec_mismatch` / `spec_sql_mismatch` judge operations; their verdicts are not reproducible without frozen model configuration, prompts, cached outputs, and retry behavior. The paper says verdicts are cached and the metric is reproducible from expression string plus registered operation pool, but neither is released through a linked artifact.

The drawback-first framing also has a precise claim ceiling: “clean” means no registered operation found a known defect, not correct, complete, professionally acceptable, or safe. Coverage of unknown drawbacks remains open. Consensus among the operation pool cannot manufacture criterion authority or completeness.

### Metric evolution

Each metric round senses two error sources:

- **dev misses:** the incumbent passes an item whose teacher-produced anchor label is fail;
- **train gaps:** the operation pool abstains or splits on an unlabeled output.

Failures are clustered under a closed task-specific taxonomy, and an LLM authors one typed operation specification per recurring cluster. A birth gate requires the operation to fire on at least half its cluster and stay clean on known-good outputs. Dev-derived operations become active; train-gap operations remain shadow operations until they improve dev agreement (p. 4; lines 148–189).

Candidate expressions come from an LLM composer plus mutation/crossover. Selection maximizes

`dev agreement × train-pool-consensus agreement^w − λ × expression size`,

with best-so-far retention, fail-closed handling of candidates lacking a usable dev opinion, and rejection of all-pass, all-fail, or all-abstain metrics. Operations with non-positive leave-one-out contribution retire after a grace period (pp. 4, 11; lines 190–210, 568–585).

The controls are sensible, but the evidence does not warrant the paper’s stronger language:

- The ten dev labels are not independent expert or exact labels. A same-family Claude teacher compares candidate outputs with references. Teacher quality is held fixed and explicitly left for future work (p. 5; lines 227–236).
- Train “consensus” is endogenous. Most operations are authored by the same model from the same outputs and closed taxonomy, so majority agreement is correlated redundancy, not independent validity evidence.
- The birth gate tests new operations on the cluster that caused their synthesis and unspecified “known-good” outputs. Without a separate operation-admission set, it is partly resubstitution evidence.
- A non-vacuity gate catches only extreme degeneracy. It cannot detect a plausible but construct-shifted metric, a subgroup-blind metric, or a metric that rewards a narrow proxy.
- Best-so-far selection guarantees monotonicity on the optimization objective by construction; the monotonically rising Figure 2 is not independent evidence of learning or validity.

### Double Ratchet skill co-evolution

The skill loop consumes failures from the current evolved metric. Failed attempts become capsules containing error text, which feed Skill synthesis. Metric phases of 15/8/5/2 rounds alternate with four 25-round skill phases. A reference arm runs the same 100 skill rounds using ground truth (MBPP+/Spider) or RAQS (report) as its grader. The authors compare peak held-out performance and the mean of the last ten rounds, relative to each run’s own round-zero baseline (pp. 4–6; lines 212–280).

The central split claim is internally contradicted. The problem setup says the locked test set is read by no loop and “purely reports transfer” (pp. 1, 3; lines 53–61, 133–140). Yet the co-evolution section says:

> “The skill loop’s held-out evaluation and rollback anchor stay pinned to the locked test set” (p. 4; extraction lines 220–223).

The results then select and report **peak** performance across 100 rounds on that same held-out set, show its learning curve every round, compare peak lifts, and describe rollback counts (pp. 5, 11–12; lines 242–258, 579–603, 684–697). A rollback decision is a training/state-transition signal. Peak checkpoint selection is also optimization, even if the metric loop itself does not see item-level labels. Repeated test evaluation, rollback, post-hoc repair, and peak selection turn the “locked” set into a validation/selection panel, not an untouched final test.

This matters more than terminology. The reported 88–110% lift retention is calculated on a panel participating in the intervention lifecycle. A valid claim needs a fourth, untouched transport set or equivalent forms evaluated once after all curricula, rollback rules, repair choices, and reporting policies are frozen.

### Results and uncertainty

The paper reports the following peak scores over three seeds (p. 5, Table 1):

- MBPP+: reference Skill loop `0.700±0.025`; co-evolution `0.717±0.038`; 106% lift retention.
- Spider: reference `0.483±0.038`; co-evolution `0.458±0.038`; 110% retention.
- Report: reference `0.850±0.010`; co-evolution `0.812±0.006`; 88% retention.

The reported co-minus-reference peak confidence intervals contain zero for MBPP+ and Spider and exclude zero narrowly for report. The study’s honesty that three seeds and 40–48 held-out tasks support only coarse claims is appropriate. But the uncertainty analysis remains weaker than that caveat suggests:

- three seed-level differences do not support reliable percentile bootstrap inference;
- peak-over-100-round selection is not represented in the interval;
- test tasks are repeated within seed and shared across arms, while report sections recur across seeds, peak/final comparisons, repair states, and judge rubrics;
- the hard subset is outcome-conditioned on five samples from the same solver family;
- retention is a ratio of two noisy changes from arm-specific round-zero baselines and can exceed 100% when the denominator is small;
- no task-cluster bootstrap, paired item analysis, multiplicity policy, preregistration, power analysis, or sensitivity to checkpoint policy is given.

The task-level “improved” counts also use permissive definitions: a code/SQL task is improved if a never-pass task succeeds at least once, while 99% of reports are “improved” if a section ends above its round-zero RAQS score. These are neither reliability nor professional-quality measures.

### Ablations and what they really establish

The anchor-guards-off ablation disables fail-closed anchoring, the validity gate, and skill-loop rollback together. It collapses to an almost-always-pass report grader on all three seeds. The no-lifecycle ablation disables birth gating, shadow status, and retirement but leaves selection/anchors intact; it does not collapse (pp. 7–8; lines 327–369).

This supports a bounded causal statement about the configured report metric: the **bundle** of anchor guards plus rollback prevents the observed vacuous collapse, whereas removing the tested lifecycle bundle did not cause collapse over 100 rounds. It does not isolate which anchor guard mattered because three mechanisms are removed together. Nor does it establish general evaluator safety: only report-generation metric validity is tabulated, and non-vacuity/held-out agreement do not cover unknown failures, fairness, consequences, or adversarial transfer.

Most importantly, the ablation falsifies endpoint-only validation. The naive arm’s task score survives even though its grader fails. Practice alone can improve the frozen solver package. Therefore task gain cannot be used as back-door evidence that an evolving training metric is valid.

### Report Goodhart episode and outer judge

The first report Skill runs improve RAQS partly by inserting metric tags without adjacent values and inventing confident forecasts. About 30% of tags at peak allegedly lack values. A stronger Opus 4.8 pairwise judge prefers baseline reports in 88% of decided pairs. The authors add a value-erasure detector and rewrite feedback, reducing bare tags to about 1% and raising RAQS. They then find the generic outer judge treats required raw tag syntax as a defect, so they design a task-aware rubric and rejudge the same stored pairs. Under that rubric, the evolved-output win rate rises from 0.515 pre-repair to 0.770 post-repair; under the generic rubric it remains 0.122/0.126 (pp. 6–7; lines 293–325).

This is a strong qualitative demonstration that both proxy and audit can fail. It is not independent confirmation of professional report quality:

- the outer judge is a stronger version of the same model family used everywhere else;
- the task-aware rubric is introduced after the generic judge produces an implausible result and explicitly encodes the disputed convention;
- the same stored output pairs are rejudged, so rubric choice is outcome-informed rather than prospectively frozen;
- only pairs with identical verdicts under both position orders count as decided, but tie/discordance rates and raw counts for each 2×2 cell are not reported;
- 48 sections recur across arms, three or four seeds, peak/final rounds, and rubric variants, yet no clustered uncertainty is reported;
- source-card factual support, fabricated figures, convention adherence, and reader value are not separately scored by independent humans;
- no analyst, recipient, adoption, decision, burden, or workflow consequence is observed.

The defensible result is that a task-aware configured judge preferred post-repair evolved outputs over their own baselines in 77% of its decided comparisons. It does not establish expert acceptance, professional quality, utility, or deployment readiness.

## Evidence and claim ceiling

### What the full source supports

1. A transparent evaluator can be represented as a versioned expression over typed drawback detectors with abstention and a fixed structural root.
2. On the manuscript-reported report experiment, removing a bundled set of anchor/non-vacuity/rollback guards yields a vacuous almost-always-pass metric, while removing the tested operation lifecycle does not.
3. The broken metric arm can retain apparently competitive task scores, proving within this configured experiment that endpoint gain does not validate the training grader.
4. The report experiment contains an instructive two-stage failure: the training rubric is gamed, then the generic outer judge misreads a required output convention.
5. The authors report co-evolution trajectories broadly similar to reference-grader Skill trajectories on three selected task families under one model family.
6. The full manuscript and source make the proposed algorithms, split claims, tables, and internal contradiction about test-set use inspectable.

### What it does not support

- an untouched held-out estimate of 88–110% oracle-lift recovery;
- independent metric validity, because anchors are tiny, teacher-mediated, repeatedly selected against, and not released;
- causal identification of anchor discipline versus rollback or individual guard mechanisms;
- criterion completeness, expert authority, professional report quality, reader value, or stakeholder consequence;
- robustness to new models, prompts, task families, semantic-failure regimes, adversaries, or distribution drift;
- reliable uncertainty, repeated operational reliability, cost advantage, or scaling feasibility;
- code/data reproducibility or result reconstruction from a publicly linked release at review time;
- autonomous capability gain, general self-improvement, safe evaluator deployment, or readiness.

## Unique insight

The paper’s unique insight for `skill-bench` is a **two-axis falsification rule**:

> Validate the evolving intervention and the evolving observer separately; neither task improvement nor observer agreement can serve as the other’s proof.

The naive arm makes this concrete. A permissive evaluator can label nearly everything successful while practice still produces better scores on a separate panel. If one looked only at final task performance, the evaluator defect would be missed. Conversely, a high-agreement evaluator can become a repeatedly optimized development instrument if its labels drive rollback, checkpoint selection, or repair—even when it is called “locked.”

This suggests a stricter information-flow test than a train/dev/test label:

```text
candidate instrument
→ operation-admission evidence
→ frozen metric-development anchor
→ agent-training verdicts
→ agent state transition
→ rollback/checkpoint/reporting decision
→ untouched equivalent-form transport measurement
→ independent criterion/consequence audit
```

Any edge from the final measurement back into state, rollback, stopping, repair, rubric choice, or reported checkpoint demotes it from final test to development evidence. The next valid claim requires a fresh form. This principle applies to benchmark graders, human rubrics, deterministic checks, intervention Skills, and ordinary model selection—not only self-evolving agents.

A second insight is that **diagnostic usefulness and scoring validity are different estimands**. The Spider metric reportedly agrees with ground truth only about 0.50 yet still routes concrete error text that supports useful Skill synthesis. Such a metric may be useful as a failure-proposal or triage instrument while being unacceptable as an acceptance gate, release score, or capability measure. `skill-bench` should type these roles rather than attach one global “valid grader” status.

## Limitations and reproducibility / operational realism

The paper is explicit about several limits: no anchor can be manufactured from evolution; mechanical failures are easier than semantic ones; the study uses three task families, one solver model, tens of held-out items, three seeds, and low hundreds of rounds; adaptive curricula and failure-anticipating detectors are unexercised (p. 8; lines 339–374). Additional limits are material:

- Appendix H’s release claim is not operationally satisfied by any URL or artifact found in the paper, metadata, or arXiv source. The claimed task data, code, operation packs, prompts, split IDs, caches, SQLite histories, judge outputs, and table builder are unavailable for audit.
- Spider requires credentialed Snowflake access, so even a future code release would need warehouse snapshot/version, permissions, query-cost accounting, timeout/retry policy, and comparator replay evidence.
- The report corpus is described as deployment-style but has no disclosed occupational source, expert authoring/approval, rights, sampling frame, recipient, or consequence validation.
- Task IDs and exact split membership are absent. Outcome-conditioned screening, stratification, dev failure construction, and report anchor generation cannot be replayed.
- “Mostly deterministic” metrics include LLM judge operations. Model identity alone does not freeze behavior.
- Cost is not reported despite 100-round loops, hundreds of synthesized/rejected operations, roughly 1.5 synthesized Skills per round, repeated solver sampling, teacher calls, and 1,056 twice-positioned judge pairs.
- The report post-repair experiment adds a fourth seed only for two co-loop arms, changing replication structure after the observed failure.
- No human expert validates detector criterion authority, taxonomies, operation correctness, report rubrics, task-aware judge decisions, or alternative valid outputs.
- No safety outcomes, affected-party harms, privacy concerns, or operational rollback consequences are measured. “Safety” in the paper means resistance to an observed vacuous metric, not safe professional action.

Operationally, the paper’s strongest transferable design is fail-closed evidence flow and explicit outer audit, not the claim that sparse anchors remove the need for reliable metrics. Ten references still function as a metric-development instrument; locked independent evidence remains indispensable.

## Transferable design implications

### 1. Enforce information-flow status, not split names

For every task/form panel, record all reads and downstream uses: detector synthesis, metric selection, Skill update, rollback, stopping, checkpoint choice, repair, rubric revision, and publication selection. A test touched by any of these becomes development evidence. Final claims require a fresh frozen form or a predeclared reusable-test correction with an explicit privacy budget.

### 2. Give graders typed operational roles

Separate `training_signal`, `failure_proposal`, `triage`, `regression_guard`, `acceptance_gate`, `benchmark_score`, and `outer_audit`. A 0.50-agreement metric may still be useful for generating error capsules; that does not license scoring or deployment gating.

### 3. Preserve intervention–instrument cross-evaluation

At each evolution epoch retain immutable Skill, operation-pool, expression, task, prompt, model, and output hashes. Cross-grade old/new outputs with old/new metrics, plus a frozen external observer. The resulting matrix distinguishes artifact improvement, metric leniency, interaction effects, and unknown disagreement:

```text
                 old metric   new metric   frozen audit
old artifact
new artifact
```

Do not aggregate until criterion applicability and evidence views are aligned.

### 4. Require criterion-authority and operation-admission evidence

A detector’s birth record should include source requirement, authority, applicable population, synthesis cluster, disjoint admission cases, known-good and known-bad contrasts, abstention semantics, false-positive/negative review, dependencies, model/prompt identity, and retirement/supersession. Pool consensus is diagnostic corroboration, not ground truth.

### 5. Treat Goodhart repair as instrument revision

The pre-repair metric, post-repair metric, generic outer judge, and task-aware judge are four instruments. Preserve all scores; do not overwrite history. Record the trigger, adjudication, affected cases, expected direction, frozen repair set, untouched confirmation set, and compatibility decision. A post-hoc task-aware judge result is hypothesis-generating until confirmed on unseen artifacts.

### 6. Report complete denominators and dependence

For pairwise audits report all wins, losses, ties, invalid calls, position discordances, tasks, seeds, checkpoint types, and repair states. Use task/section-clustered paired uncertainty and predeclare whether peak, final, area-under-curve, or fixed-round performance is the estimand.

## Concrete repository actions

1. **No new evaluator-evolution schema or self-improving-agent pilot.** Existing compounding-lessons, longitudinal stream/evolution-event, task-health, metric-monitoring, validity-argument, grader, and configured-component contracts already hold the necessary objects. The next consolidation pass should add the locked-set information-flow demotion rule, typed grader operational roles, and old/new artifact × old/new metric × frozen-audit cross-grading pattern to canonical guidance.
2. **Add this source to the human-facing indices as a Tier A intervention–instrument validity case.** Its controlled vacuous-grader result is direct evidence that agent score and grader validity dissociate. The 88–110% oracle-retention claim should remain below the transport-evidence tier because the reported locked set participates in rollback and peak selection.
3. **Use a four-form protocol in any future evolving benchmark experiment:** operation-synthesis cases; metric-selection anchors; agent rollback/checkpoint-validation forms; and a once-read untouched transport panel. Freeze an independent criterion/consequence audit before observing transport outcomes.

No new queue task follows. These are nonduplicate refinements to the already pending consolidation program and existing executable contracts.
