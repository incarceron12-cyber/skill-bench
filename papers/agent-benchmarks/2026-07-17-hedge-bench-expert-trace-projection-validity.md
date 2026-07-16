# Hedge-Bench: expert incidents are valuable, but released checks score a model-authored projection with another model

**Paper:** Eric Cho, Shawn Huang, Alice Lu, and Andy Lyu, *Hedge-Bench: Benchmarking Agents on Hard, Realistic Tasks Pertaining to Financial Reasoning*, arXiv:2606.03918v1 (2 June 2026), <https://arxiv.org/abs/2606.03918v1>.

## Review and evidence status

**Deep review of the complete immutable primary source and complete official release.** I read the full 12-page local PDF/text and statically audited every released environment in the official sole-root-commit snapshot. I did not call the paid Gemini judge or execute released workloads.

- PDF: `data/papers/pdfs/2606.03918v1-hedge-bench.pdf` (12 pages; SHA-256 `b19483100ea43b664fe6de9f0f566148c19cb378016e12d1de050773b00453aa`).
- Full local text: `data/papers/text/2606.03918v1-hedge-bench.txt` (SHA-256 `c81f197b7f23f036b30fbe47cd7282eb33b4274971b8dd01e7cd44e8a41beaa5`).
- Official release: <https://github.com/Trata-Inc/trata-hedge-bench>, archived at commit `0a3c08a1e19bb62212fa4e7e30b53e9d77d46665` (29 May 2026), four days before arXiv v1.
- Complete archive: `data/sources/releases/2606.03918v1-hedge-bench/Trata-Inc-trata-hedge-bench-0a3c08a.zip` (SHA-256 `60bce3f73b3f2fe0178e7354b35291ebf71262e8179790b98b7992fb49743`; 4,861 files; 102 environments).
- Acquisition and timing manifest: `data/sources/releases/2606.03918v1-hedge-bench/provenance.json`.

The snapshot has no `LICENSE`/`COPYING` file and GitHub detected no license. No reuse right is inferred. It contains tasks, source packs, rubrics, and grader code, but no analyst transcripts, example solutions, retained benchmark trajectories, judge outputs, scores, costs, or analysis scripts.

## Why this matters to `skill-bench`

This review advances charter objectives A and B by testing a central general hypothesis: can consequential expert work be projected from authentic incidents into fair, inspectable checks without mistaking one normalized expert path—or a judge's semantic resemblance to it—for the construct? Finance is a bounded case. The reusable object is the incident-to-instrument transformation, not a finance-only benchmark.

## One-sentence contribution

Hedge-Bench contributes an unusually promising source of authentic paired-practitioner discussions and turns 102 open-ended analyses over point-in-time document packs into theme/action-move rubrics, but the released instrument omits the source transcripts and human transformation lineage, exposes rubric-derived theme labels, and computes scores through three uncalibrated Gemini judgments; its strongest supportable claim is therefore configured semantic agreement with a model-authored rubric projection, not deterministic reproduction of verified expert reasoning or occupational capability.

## Research question and intended construct

The paper asks whether agents can perform the open-ended reasoning of senior financial analysts: identify load-bearing questions, choose analyses, reconcile opposing evidence, and form an investment view rather than retrieve a discrete answer (§§1–2, pp. 1–3). Its intended construct is explicitly process-like: closeness between an agent's analytical moves and actions taken by domain experts in the same information environment (p. 1).

The source mechanism is distinctive. Trata records anonymous telephone discussions between two currently employed investment professionals who both know a public company. The authors say these conversations are part of actual research workflows, include collaborative and adversarial discussion, and are perpetually licensed to Trata (§3, p. 3). They report a nine-month corpus of 5,112 candidate tasks/20,448 subtasks and select 102 after internal difficulty assessment and review by two independent humans (§3.2, p. 4).

That mechanism can preserve forms of tacit expertise that answer-key benchmarks erase: what question to ask, what contradiction matters, what comparison changes a view, and how evidence becomes a position. But the paper alternates among four non-equivalent labels—actual on-the-job task, conversation-derived topic, expert action, and verified reasoning step. The release makes only the final projected rubric observable. It does not permit a reader to determine whether each public task was itself performed occupational work, whether every move appeared in the conversation, or how disagreement and omissions were transformed.

## Methodology and system reconstruction

### From conversation to task

The paper's pipeline is:

```text
paired analyst conversation in an actual research setting
→ transcript and discussed diligence/questions
→ single-pass language-model generation of themes, moves, and metadata
→ check that a move is derivable from the source folder
→ two-reviewer task quality assessment
→ public instruction + closed source pack + private rubric
→ agent answer
→ three Gemini judge calls
→ move/theme coverage and 0–4 score
```

The authors expressly disclose the weakest projection edge in §6 (p. 10): one language-model pass generates themes, moves, rejects rule-violating moves, and emits metadata; the verification step checks derivability from `/app/data/`, **not fidelity to the analyst transcript**. They propose transcript-span grounding, per-step generation, human validation of every move, and cross-model disagreement review for v2. This limitation directly contradicts broad readings of “verified expert steps.” A source-supported model-generated move can be plausible without being an observed expert move; conversely, a real expert move may rely on tacit or proprietary context absent from the public pack.

The released task metadata names only `Trata` as author. It contains no contributor IDs/pseudonyms, analyst role or experience, conversation/session ID, transcript span, spontaneous/probed/inferred status, reviewer identity, disagreement, correction, transformation model/prompt/version, acceptance rationale, or criterion-level authority record. The perpetual-license statement establishes a claimed IP relationship, not participant comprehension, consent scope, withdrawal boundary, occupational representativeness, or continued approval after model transformation.

### Released population and dependency structure

Static parsing of all 102 environments found:

- 21 ticker/company source packs, each reused across 3–7 tasks;
- 20 task dates from 15 August 2025 through 22 May 2026;
- exactly 21 unique source-pack hashes, with 21–55 files per pack (median 38.5) and roughly 0.5–5.7 MB per pack (median 2.6 MB);
- 102 unique instructions and 102 unique rubrics;
- 16 tasks with three themes, 66 with four, and 20 with five;
- 1,289 total required moves, about 3.13 per theme; and
- no mismatch between public theme titles and private rubric theme titles.

This reconciles the release count with the paper's 102 environments, but exposes the effective structure: 102 tasks are not 102 independent companies, source contexts, or practitioner sessions. They are clusters of related questions over 21 identical document packs. The paper says a “standard” task has three or four themes and each theme four or five moves (§3.1, p. 4), whereas the release has 20 five-theme tasks and averages only 3.13 moves per theme. The code's threshold still handles these, but the prose is not a release-accurate description.

The paper reports six topic categories. Every released `task.toml` instead has only `category = "finance"`; no released manifest maps tasks to the paper's Valuation/Growth/M&A/Competitive Positioning/Operational Strategy/Risk labels. Figure/table membership and category aggregates therefore cannot be reconstructed from the snapshot.

### Source packs and public task

Each environment supplies a Docker image containing filings, earnings calls, financial statements, company profiles, press releases, and sometimes prices, ownership, presentations, or S-1 material. Filename checks found no dated filename later than its environment cutoff and no empty source file. That is useful release conformance, not full point-in-time verification: `company_profiles.json` has no obvious as-of field, many files do not preserve retrieval URL/license/authority metadata in a uniform manifest, and this audit did not independently replay every datum against its origin.

All tasks for a ticker reuse an identical pack. This controls context across that conversation's projected topics but creates cluster dependence and can reveal neighboring rubric concepts when the suite is public. The instruction exposes the exact rubric theme titles and mandates clear position, strongest counter-evidence, reconciliation, ambiguity, and inline file citations. This is a fair disclosed procedure, but performance partly measures response to author-provided decomposition. It does not isolate whether an agent independently discovered the load-bearing questions, despite that being part of the motivating construct.

The paper and README say each environment contains an “example solution.” No example/reference-solution file exists in the release; `tests/ground_truth.txt` is a rubric, not a worked solution. No transcript is present. Reproduction can inspect the projected instrument but cannot audit it against either endpoint claimed to generate it.

### Rubric and aggregation

Each rubric has theme prose, lettered required moves, and broad source locators. Most locators are directories such as `earnings_call/` or `sec_filings/10-k/`; some name aggregate JSON files. They do not provide exact file/span/table locators, transcript spans, authority, applicable time, accepted alternatives, or dependencies among moves.

For a theme with `n` moves, coverage requires `max(1, min(n-1, 3))` valid hits. Thus a three-move theme requires two and a four-or-more-move theme requires three. A move that the coverage judge marks hit but supported by a claim the grounding judge flags becomes tainted and is removed. Off-rubric analysis is not penalized, but it also cannot earn coverage; the paper's example of a novel model insight required post-hoc human recognition and remains invisible to score (§5.5, p. 9).

A trial receives 4 only for all themes plus one synthesis sentence, 3 for all themes without synthesis, 2 for at least two themes, 1 for one, and 0 otherwise (§4.3, pp. 6–7). This produces severe information loss: with five themes, both two-theme and four-theme answers score 2. Pass@1 is the probability of a perfect 4. The public theme decomposition, flexible within-theme slack, all-theme top gate, and one-sentence synthesis gate are policy choices, not empirically calibrated consequences of professional quality or financial loss.

### The released grader is semantic, not deterministic

All 102 tasks contain the same three prompts and shell wrapper. There are two `grade.py` hashes: 93 tasks use one version; nine tasks use a variant that additionally accepts a one-element list containing a dictionary. Both compile. Each trial requires at least three calls to `gemini-3.1-pro-preview` at temperature zero, with up to two attempts per call:

1. **grounding:** load only files whose relative path or basename literally appears in the answer, then ask Gemini to extract and verify factual claims;
2. **coverage:** show Gemini the answer, complete private rubric, and flagged claims, then ask for move hits/misses/taints; and
3. **synthesis:** show Gemini the answer and rubric, then ask for a synthesis quotation.

Coverage and synthesis run concurrently after grounding. The prompts request JSON and the API requests `application/json`, but no response schema is supplied. Outputs are repaired by stripping fences/trailing commas and applying permissive JSON parsing. Judge identity is a mutable preview endpoint, with no dated revision/hash.

The abstract's “deterministic grading against verified expert steps” is therefore untenable as an implementation description. Arithmetic after judge output is deterministic; factual verification, concept equivalence, taint linkage, and synthesis detection—the decisive observations—are model judgments. Temperature zero does not establish repeatability, calibration, or independence. The same model family is also one evaluated agent, creating possible self-preference or style interaction that is not tested.

Failure semantics are also mixed. An exception writes zero and is re-raised; the shell forces exit 0 after ensuring a reward exists. A coverage parse failure yields no themes and hence zero. A synthesis parse failure prevents score 4. But a grounding parse failure defaults to **no hallucinations and an empty flagged list**, silently making the factuality check permissive. The paper says unparsable judge output zeros the entire run (§6, p. 10), which is not true for grounding-stage parse failure. Missing answers are replaced by placeholder text for retention before grading. These are instrument outcomes, not agent reasoning failures, and should not enter capability scores without separate invalid-run handling.

## Evidence and what it supports

The experiment nominally crosses 102 environments, eight model configurations, and eight attempts: `102 × 8 × 8 = 6,528` trials (§4, p. 4). The eight systems are four Claude versions, two Gemini versions, and two GPT versions, all through Terminus 2. The paper does not report exact harness commit, model endpoint snapshots, prompts beyond tasks, decoding, tool policy, token/time budgets, retry policy, or per-model invalid counts in a complete table.

The paper reports Claude Sonnet 4.6 highest at dense mean 1.92/4 and pass@1 above 15%; Opus 4.7 is 1.84, GPT-5.5 and Gemini 3.5 Flash 1.68, and GPT-5.4 Mini 0.75 (§5.1, p. 7). Theme and valid-move coverage are also reported. The “below 16%” statement is a perfect-rubric rate under this configured observer, not percentage of real financial tasks resolved.

Eight attempts per environment reveal within-task stochasticity, and macro-averaging environments avoids allowing tasks with more valid trials to dominate. But the 95% interval is computed from the standard deviation of 102 per-environment pass rates divided by `sqrt(102)` (§4.3, p. 6). It treats environments as the sampling units despite 3–7 tasks sharing each of only 21 source packs/company incidents. It also excludes run-to-run uncertainty by design. A cluster bootstrap over incident/source-pack lineage, paired model contrasts, and explicit invalid-run uncertainty would be materially wider and better aligned with the sampling process.

No retained result rows or trajectories are released, so these claims cannot be recomputed. There is no judge agreement study against blinded analysts, repeat-judge stability, alternative-judge comparison, false-positive/false-negative set, criterion-level adjudication, or evidence that perfect rubric coverage predicts expert preference, decision quality, P&L, risk detection, time saved, or deployment success. The post-hoc observation that human evaluators found some off-rubric model insights useful is qualitative and lacks sampling, protocol, ratings, or denominators.

The reported hallucination rates (for example 88.7% for Sonnet and 36.6% for GPT-5.5) are “any judge-flagged claim” trial rates, not calibrated factual-error probabilities. The claim that GPT-5.5 is “most deployable” (§5.4, p. 9) is unsupported: no deployment threshold, severity weighting, utility function, human oversight burden, decision outcome, latency/cost ledger, or safety evaluation is supplied.

The evidence supports this bounded claim:

> In the authors' unreleased 6,528-trial result set, under Terminus 2 and a mutable Gemini preview grader that semantically compares answers to 102 released model-authored rubrics over 21 released company source packs, no tested configured system received a perfect projected-rubric score on 16% or more of reported attempts.

Even that claim cannot be independently replayed from the release because trajectories, judge records, results, configured-system receipts, and costs are absent.

## Unique insight: an authentic trace does not confer authority on every projection of it

Hedge-Bench's best idea is to start from a consequential expert incident rather than invent a plausible task backward from a convenient answer. Its central failure reveals a more general rule:

> Authority does not automatically propagate from an authentic expert conversation through transcript selection, model normalization, source-grounding checks, public theme disclosure, semantic judge decisions, and score aggregation.

The necessary lineage is:

```text
occupational incident and participant authority
→ consented transcript with context and disagreement
→ transcript claims/actions with exact spans
→ requirement atoms and accepted alternatives
→ public instruction/source affordances
→ private criteria with fair public basis
→ realized agent evidence view and artifact
→ grader observation with calibrated error
→ metric with clustered sampling uncertainty
→ bounded validity claim and intended use
```

Hedge-Bench has potentially strong evidence at the first node and inspectable artifacts in the middle, but omits the transcript bridge and empirical grader/claim bridges. Source derivability answers “could this move be argued from the pack?” It does not answer “did the experts make it?”, “is it professionally necessary?”, “are alternatives valid?”, or “can this judge detect it reliably?” This is exactly why `skill-bench` must keep contributor authority, projection conformance, grader reliability, and validity arguments as separate records.

## Limitations and validity threats

### Expertise and projection validity

1. **Transcript fidelity is not checked.** The authors explicitly say the v1 verifier tests source-pack derivability, not whether a move appears in the expert transcript (p. 10).
2. **The rubric is a single-pass model projection.** Themes, moves, rejection, and metadata share one generation call; transformation errors and correlated omissions are not independently observable.
3. **No transcript or span lineage is released.** External reviewers cannot distinguish expert-spoken, analyst-inferred, model-inferred, or reviewer-added moves.
4. **Contributor authority is under-specified.** Employment at an established firm does not establish role, seniority, strategy, sector knowledge, performance, conflicts, or representativeness.
5. **Pair agreement is asserted, not measured.** “Largely agreed” on load-bearing questions has no sampling frame, coding protocol, disagreement counts, inter-rater statistic, or retained adjudication.
6. **Perpetual licensing is not participation validation.** Consent scope, compensation/reciprocal value, anonymity risks, permitted benchmark/model uses, withdrawal, and reconsent after transformation are absent.
7. **Selection may be outcome-conditioned.** The paper says selection used internal difficulty and two-reviewer quality assessments, then immediately describes heterogeneous frontier-model pass rates. It does not state whether model outcomes influenced admission or were held out.
8. **Occupational scope is narrow.** Twenty-one public-company packs cannot establish representation of hedge-fund work across strategies, asset classes, time horizons, regions, operations, portfolio construction, trading, risk, and compliance.

### Task and rubric validity

9. **Public themes supply the decomposition.** This tests execution against disclosed lines of inquiry more than independent discovery of them.
10. **No exact criterion evidence locators.** Directory-level source labels cannot audit entailment, authority, valid time, or whether a move combines unsupported fragments.
11. **Alternative valid paths are unrepresented.** Off-rubric work avoids penalty but cannot substitute for a missed canonical move or earn positive credit.
12. **Criterion dependence is ignored.** Moves and themes may entail, duplicate, or causally depend on one another, yet thresholding counts them as separate evidence.
13. **Aggregation is uncalibrated.** Theme slack, all-theme gates, score compression, and the synthesis sentence have no demonstrated relation to expert preference, consequence, or decision loss.
14. **The release diverges from the paper.** Twenty tasks have five themes; average moves/theme is about 3.13; no example solution or category manifest is released.
15. **Source-pack provenance is incomplete.** Point-in-time filename conformance is encouraging, but uniform origin URL, retrieval time, license, transformation, authority, and as-of records are absent.
16. **Cross-task exposure is plausible.** Several tasks reuse the same source pack and neighboring conceptual context; a public benchmark can leak task family and rubric vocabulary over repeated use.

### Grader and measurement validity

17. **The grader is not deterministic.** Three semantic Gemini calls determine facts, equivalence, taint, and synthesis; only score arithmetic is deterministic.
18. **No judge calibration.** There is no blinded expert gold set, agreement, repeatability, alternative judge, perturbation, or adversarial test.
19. **Grounding failure can fail open.** An unparsable grounding response becomes “no hallucinations,” contrary to the paper's all-unparsable-zero statement.
20. **Evidence matching is citation-string dependent.** Only files literally named by path or basename are loaded; citation formatting can change the evidence view independently of substantive support.
21. **Taint linkage is another semantic inference.** A flagged claim only removes a move if the coverage judge associates them; no deterministic claim-to-move locator exists.
22. **Preview judge identity is mutable.** `gemini-3.1-pro-preview` has no immutable endpoint/version receipt, compromising longitudinal comparability.
23. **Judge/evaluated-model interaction is untested.** Gemini judges Gemini and non-Gemini prose without a cross-judge matrix or style controls.
24. **Invalid and zero are conflated.** Harness errors, grader crashes, parse defects, missing output, substantive misses, and hallucinations can all surface as zero or exclusion under different paths.
25. **Hallucination severity is absent.** “Any flagged claim” treats one immaterial error and a thesis-destroying fabrication alike.

### Statistics, reproducibility, and operational realism

26. **Environment-level intervals ignore 21-pack clustering.** The effective diversity is closer to 21 company/conversation contexts than 102 independent environments.
27. **Trial uncertainty is omitted from reported intervals.** Eight attempts are averaged, but intervals intentionally represent only nominal task sampling.
28. **No paired contrasts.** Overlapping marginal intervals do not test model differences on shared environments.
29. **Results are not released.** Scores, details, trajectories, invalids, judge outputs, usage, costs, and analysis code cannot be audited.
30. **Configured systems are under-specified.** Harness commit, adapter behavior, model snapshots, prompts, budgets, and failure/retry semantics are incomplete.
31. **Cost is unreported.** At least 19,584 successful judge calls are implied before retries (`6,528 × 3`), in addition to agent inference, but tokens, latency, and spend are absent.
32. **Sandboxing is asserted, not inspectable from results.** The Dockerfile packages data, but the release contains no network policy, canary report, or trial evidence proving agents could not retrieve outside information.
33. **No professional outcome.** A single prose answer and rubric resemblance do not establish an investment decision, portfolio consequence, risk control, compliance, timeliness, or readiness.
34. **No reusable license.** The official snapshot supplies no license, limiting legal reproducibility and downstream benchmark use.

## Transfer to `skill-bench`

### Retain

1. Start task authoring from authentic critical incidents and paired-practitioner debate where disagreement itself is informative.
2. Freeze a point-in-time source environment and require claim-level evidence citations.
3. Represent themes and moves separately, preserving which analytical decomposition and evidence relationships matter.
4. Separate factual grounding, criterion coverage, and synthesis rather than ask one judge for a holistic score.
5. Preserve off-rubric observations for adjudication instead of automatically penalizing them.
6. Use repeated attempts and task-macro estimates, while retaining trial-level failure and resource evidence.

### Repair before reuse

1. Give every criterion an authority chain: incident/session, contributor role, transcript span, extraction status, transformation model/prompt/hash, reviewer decision, source locator, and unresolved disagreement.
2. Validate both directions: every private move traces to expert evidence and fair public affordances; every material expert move is either represented or explicitly excluded.
3. Add accepted alternatives, dependencies, contradiction/applicability conditions, and “novel but valid” adjudication rather than canonical-path-only credit.
4. Factor discovery from execution with matched conditions: open topic alone versus disclosed themes, holding source pack, rubric, grader, and agent fixed.
5. Replace broad source directories with exact proposition-level locators and authority/valid-time records.
6. Pin judge model/configuration/prompts/evidence view; require typed `pass/fail/not_applicable/invalid/insufficient_evidence`; fail closed on every parse/service error.
7. Calibrate grounding, move equivalence, taint, and synthesis separately against blinded expert double labels, adjudication, positive/negative contrasts, and repeat/cross-judge tests.
8. Cluster inference by incident/source-pack/contributor lineage and report trial, task, pack, domain, and grader uncertainty separately.
9. Release result rows, redacted traces, judge observations, invalid-run ledger, usage/cost, exact analysis code, category manifest, and legal license.
10. Keep rubric alignment, expert preference, professional artifact quality, economic utility, safety, and deployment readiness as separate claims.

### Do not infer

Do not infer that a perfect Hedge-Bench score reproduces an analyst's reasoning trace; that below-16% means agents can resolve below 16% of real hedge-fund work; that judge-flagged hallucination rates are calibrated factual-error rates; that GPT-5.5 is deployable; or that 102 environments represent 102 independent occupational incidents. Do not call a semantic LLM observer deterministic because its downstream arithmetic is fixed.

## Concrete repository actions

**No new queue task is warranted.** The evidence maps to existing machinery rather than a finance-specific subsystem:

- contributor/session authority and transformation lineage → expertise-transfer and expert-participation contracts;
- transcript/requirement/instruction/source/witness/check equivalence → completed task-projection conformance machinery;
- exact evidence views, typed invalids, and judge calibration → benchmark-bundle grader observations, artifact-view admissibility, and task-health records;
- pack/contributor clustering, missingness, cost, and monitoring → metric specification;
- claim ceilings → validity arguments.

The next relevant pilot should exercise one **incident-to-criterion projection audit** using those records: at least two independently reviewed transcript spans; one model-inferred but source-derivable move that experts reject; one valid alternative path; matched hidden-versus-disclosed theme conditions; blinded double-label judge calibration; and cluster-aware reporting. Useful completion is not a schema-valid record—it is empirical evidence that authentic incident authority survives projection without laundering model inference into expert ground truth.

## Claim boundary

Hedge-Bench supplies a complete, inspectable 102-task instrument over 21 point-in-time company packs and a valuable hypothesis for converting paired practitioner conversations into analytical-move evaluation. Its release verifies that all environments contain instructions, source packs, unique rubrics, and executable semantic grader code.

It does **not** release the transcripts, criterion transformation lineage, example solutions, category map, trial records, judge outputs, analysis code, costs, or a license. The paper itself concedes that v1 rubric verification checks source derivability rather than transcript fidelity. Since uncalibrated Gemini judgments determine grounding, move equivalence, taint, and synthesis—and one parse path fails open—the benchmark does not provide deterministic grading against verified expert steps. It measures configured agreement with a model-authored, source-derivable rubric projection. Expert validity, occupational representativeness, professional capability, production fitness, economic value, safety, and deployment readiness remain unsupported.