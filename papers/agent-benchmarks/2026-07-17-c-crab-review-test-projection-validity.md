# c-CRAB: executable consequences improve review evaluation, but the score is a selected repair-and-test chain

## Bottom line

c-CRAB makes a valuable correction to code-review evaluation. Instead of asking a model judge whether a candidate comment resembles a historical comment, it converts real pull-request review comments into tests that fail before the merged change and pass afterward, runs a coding agent on each historical comment, retains comments that the agent can resolve, then asks whether a review tool's findings induce a patch that passes those tests. This is far closer to a consequential check than text overlap. The official release is unusually inspectable: it preserves the stage funnel, generated tests, coding-agent resolution results, baseline review outputs, raw test results, and the implementation needed to reproduce the reported final rates from released bytes.

The resulting construct is nevertheless narrower than “code-review quality” or true-positive rate in the usual detection sense. A c-CRAB success is:

`historical review comment selected as actionable → GPT-5.2 test projection succeeds → Claude Sonnet 4.6 can repair from the historical comment → candidate review batch leads Claude Sonnet 4.6 to a patch satisfying that projected test`.

The candidate comment is not matched to the human issue, the candidate tool is not itself required to produce a fix, and false-positive findings are not scored. One candidate finding can trigger a patch that passes several human-comment tests; irrelevant or harmful findings can coexist with a passing patch. Conversely, a correct but differently framed finding can fail because the repair agent or generated test prefers the merged implementation. The 234 final comments are also selected on solvability by the same coding-agent model used in evaluation, so they are a post-treatment subset favorable to one particular mediator.

The strongest paper claim is therefore that four configured review-tool → Claude-Sonnet-repair packages have materially different **projected-test pass rates on 234 selected historical review comments**: Claude Code 75/234 (32.1%), Devin 58/234 (24.8%), PR-Agent 54/234 (23.1%), and Codex 47/234 (20.1%). The release audit reproduces those exact numerators and rates. It does not establish recall, precision, false-positive burden, human usefulness, professional acceptance, model-only review ability, or production readiness.

## Source and reading record

### Complete primary paper read

- Yuntong Zhang et al., *Code Review Agent Benchmark*.
- Immutable record: <https://arxiv.org/abs/2603.23448v3>; PDF: <https://arxiv.org/pdf/2603.23448v3>.
- Version read: immutable arXiv v3, updated 7 April 2026; the API metadata contains no withdrawal or retraction notice.
- Local PDF: `data/papers/pdfs/2603.23448v3-c-crab.pdf` (11 pages; 1,016,395 bytes; SHA-256 `7317d231fd9a84584666098d0c9810c2380fa27a10a590d96801c28fc00fbe15`).
- Local full text: `data/papers/text/2603.23448v3-c-crab.txt` (SHA-256 `46d689038c140451c63ca853a9839d20bb613488df81e857a992667d201686cd`).
- Date read: 17 July 2026. The complete paper was read through benchmark construction, filtering, test generation, agent resolution, evaluation, results, manual analyses, threats to validity, and data availability.

### Official release audited

- Author-declared repository: <https://github.com/c-CRAB-Benchmark/dataset>.
- Pinned commit: [`856dfa3102b8996d168c4f195217b7603e1d1bc6`](https://github.com/c-CRAB-Benchmark/dataset/commit/856dfa3102b8996d168c4f195217b7603e1d1bc6), dated 27 March 2026—after arXiv v1 and before v3. Exact snapshot identity with every v3 result is not independently certified.
- Local archive: `data/sources/releases/2603.23448v3-c-crab/c-CRAB-Benchmark-dataset-856dfa3.zip` (38,181,564 bytes; SHA-256 `4eda3cc68edfe14492bc30fb17b1475e3499b9c9e9033edff1b0795c97b8cd05`; 415 files; ZIP integrity passed).
- Provenance: `data/sources/releases/2603.23448v3-c-crab/provenance.json`; pinned commit metadata: `commit.json`.
- The archive has no detected repository license; reuse rights are not inferred.

The audit parsed the complete released JSONL funnel and every `result.json` in the compressed test-generation, agent-resolution, review, and four tool-evaluation archives. It inspected the filtering, test-generation, repair-agent, test-running, baseline, and Docker runtime implementations. No mutable commercial model was called and no untrusted repository workload was executed. This is a release/data/implementation audit, not an independent rerun of generation or repair.

## One-sentence contribution

c-CRAB replaces text-match review scoring with a released human-comment → fail/pass test → repair-agent intervention chain, but conditions its final population on generator and repair-agent success and then scores only whether a candidate review batch enables that same repair agent to satisfy implementation-sensitive projected tests, without measuring finding attribution or false-positive cost.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through expansion and validation of a distinct expertise-to-evaluation transformation. It does not imply that `skill-bench` should narrow to software engineering. c-CRAB is a compact, inspectable instance of a cross-domain pattern:

`expert intervention → executable consequence projection → intermediary agent action → downstream check`.

The uncertainty clarified is when such a chain measures the quality of the candidate knowledge-work artifact and when it instead measures a configured mediation package over a selected subset. The concrete evidence is stronger than prose alone: immutable paper bytes, a pinned release, stage-wise membership, generated tests, raw candidate outputs, per-comment outcomes, and executable filtering logic. Useful completion is a claim-bounded account of source authority, projection validity, mediator conditioning, denominators, alternative-valid outcomes, and missing cost—not another code-review-specific schema.

## Research question and warranted claim

The paper asks whether code-review agents can be evaluated by whether their feedback causes a coding agent to make changes that satisfy executable tests derived from real human review comments, rather than by lexical or model-judge similarity (Sections 1–3, pp. 1–5).

The released evidence warrants the following statements:

1. The pipeline starts from the SWE-CARE test split: 671 pull-request instances, 1,313 reference review comments, and 90 repositories in the released stage-zero file.
2. An LLM quality filter retains 410 instances and 595 comments; Docker availability does not further reduce that released stage.
3. Test generation retains 339 instances and 485 comments in the released stage-three dataset.
4. Claude Sonnet 4.6 resolves 234 comments across 184 instances and 67 repositories; these become the final benchmark comments.
5. Filtering the raw tool-evaluation archives to those 234 resolved comments exactly reproduces Table 1: Claude Code 75, Devin 58, PR-Agent 54, and Codex 47 passing projected tests.
6. The released test-generation corpus and raw execution records make the benchmark's transformation substantially more inspectable than judge-only review benchmarks.

The evidence does **not** establish that every source comment is expert, correct, current, representative, or professionally important; that generated tests completely express comment intent; that passing the merged implementation is the only valid response; that candidate findings correspond to the human findings; that tools have the reported precision or recall; that extra findings are harmless; that model ordering transports across repair agents, model versions, prompts, repositories, or operational review workflows; or that scores predict defect prevention, maintainer acceptance, review latency, or production outcomes.

## Methodology and released funnel

### Source population and human-comment authority

c-CRAB inherits pull requests and review comments from SWE-CARE. The paper treats human review as the desired reference behavior and uses the merged change as evidence that the comment was addressed. This is stronger provenance than model-authored bug descriptions: the comment occurred in a real repository review and has an associated code transition.

But “human” is not equivalent to “expert-approved ground truth.” The paper/release do not provide a task-level authority ledger covering reviewer role, maintainer status, repository familiarity, whether the comment was blocking, author acknowledgement, explicit resolution decision, disagreement, later reversal, or whether the merge implemented the requested remedy for that comment rather than a correlated change. Repository participation is useful ecological provenance; it is not automatic substantive authority.

The source population is also already selected. It includes public GitHub pull requests available through SWE-CARE and excludes private review, abandoned changes, comments without recoverable commits, and workflows outside Python/JavaScript/TypeScript. The released stage zero has 90 repositories, but no probability sampling frame for code review is defined. Results describe this constructed public-PR population, not code review generally.

### LLM comment filtering

GPT-5.2 classifies comments as HIGH, MEDIUM, or LOW based on actionability and technical specificity. The authors manually label 100 comments, iteratively tune the prompt until a target agreement threshold is reached, and report 84% agreement between the final filter and the manual labels (Section 3.1, pp. 3–4). In production, HIGH and MEDIUM are kept; the release implementation defaults unparseable output to HIGH.

This stage removes 718/1,313 source comments (54.7%) and 261/671 PR instances (38.9%). The exclusion is construct-changing, not merely cleanup: politeness, design discussion, questions, architectural concern, and context-dependent feedback are less likely to become executable local tests. The retained benchmark therefore targets test-projectable actionable feedback, not all useful review work.

The reported 84% is raw agreement on the same 100 cases used to tune the prompt. The paper gives no initial-versus-final agreement, class prevalence, confusion matrix, independent held-out set, inter-author reliability, adjudication policy, or error severity. Prompt iteration against the evaluation labels makes 84% a development-set fit, not held-out filter validity. The fallback-to-HIGH policy additionally converts evaluator invalidity into inclusion.

### Review comment to fail/pass test

For each retained comment, GPT-5.2 receives the review comment plus before/after repository context and generates a test. The test is accepted if it fails on the pre-change commit and passes on the merged commit (Section 3.2, p. 4). The paper reports 485 retained comments after this stage; the release reproduces 339 instances and 485 comments.

This transformation has two important strengths:

1. it binds an evaluative statement to executable evidence rather than wording similarity; and
2. it checks directionality across a real code transition, rejecting tests that already pass before or still fail after.

Yet fail→pass is **transition consistency**, not semantic completeness. The generator sees both the pre-change and merged states, so it can project a visible implementation delta into a test without correctly recovering the reviewer's underlying requirement. A test can overfit exact strings, APIs, exception forms, or structural choices in the merged patch. It can also miss collateral regressions and broader intent. The released generation artifacts label successful tests by language/comment type but do not provide independent expert acceptance, alternative-fix trials, mutation sensitivity, or a requirement-atom coverage matrix.

The archive contains 908 generation-result entries across 397 instances, of which 774 are marked successful. The released funnel later contains only 485 comments. The archive does not include one table-building manifest that explains every intermediate membership transition from all successful generation records to stage three. Stage-wise JSONL files make final membership inspectable, but the exact generation-attempt → accepted-stage lineage remains less explicit than the headline counts suggest.

### Repair-agent solvability filter

Claude Sonnet 4.6 receives each historical comment and attempts to modify the pre-change repository. A comment remains only if its generated test passes after that patch (Section 3.3, p. 4). The released archive contains 339 repair results and 483 per-comment resolution records, with 234 marked resolved. The stage-three JSONL contains 485 comments, leaving two comments without a corresponding per-comment resolution record in the compressed results; the release provides no explicit typed reason for that discrepancy.

The resulting stage four contains 184 instances and 234 comments. Thus 251/485 stage-three comments (51.8%) and 155/339 instances (45.7%) are removed by the mediator-solvability gate. This is a major estimand change. The benchmark no longer asks about all test-projectable human comments; it asks about comments that one run of one commercial coding-agent configuration could resolve.

That gate has a legitimate operational motive: if the evaluation repair agent cannot act on the human comment, candidate review tools should not be blamed for its downstream failure. But conditioning on mediator success creates post-treatment selection and model affinity. It favors issue types, wording, repositories, and tests that Claude Sonnet 4.6 can handle. The same model family/configuration then mediates candidate review outputs. A tool whose feedback is especially compatible with that mediator can score well even if another engineer or coding agent would prefer different feedback; a useful comment outside Claude's repair envelope never enters the benchmark.

A stronger design would preserve all 485 comments, report mediator-validity separately, and evaluate multiple independently configured repair agents or human patches. At minimum, selection probability and score should be stratified by source-comment type, repository, and mediator outcome rather than treating the 234 as an unqualified benchmark population.

### Candidate review evaluation

Each review tool receives the historical PR diff and problem statement but is instructed not to inspect existing review comments. The released runner supports Claude Code, Codex CLI, Devin, PR-Agent, and CodeRabbit. The reported table covers four tools. Their findings are passed as a batch to Claude Sonnet 4.6, which edits the repository; the generated tests are then run (Section 3.4, pp. 4–5).

This measures an intervention chain rather than direct finding equivalence:

`candidate review output R → repair-agent policy M(R, repository) → patch Δ → projected test T(Δ)`.

No step attributes a passing test to a particular candidate finding. The repair agent can infer an issue from the diff, combine findings, ignore bad findings, or repair multiple historical issues from one broad comment. Conversely, parse loss or unhelpful formatting can block an otherwise valid finding. Score therefore bundles review content, parser behavior, prompt, repair-agent reasoning, repository tools, generated-test validity, and execution environment.

The tool treatments are also not fully normalized. Claude Code uses the mutable `sonnet` alias with `--dangerously-skip-permissions`; Codex uses the CLI's default model through `--full-auto`; Devin uses a hosted API session; and PR-Agent uses its own local provider/configuration. The paper does not pin CLI/package versions, exact endpoint snapshots for every reviewer, decoding seeds, network policy, tool budgets, or equivalent affordances. These are configured products, not clean model-only comparisons.

### Metric semantics

The paper calls its principal metric true positive rate (TPR): the fraction of human-derived tests that pass after the candidate review output is applied through the coding agent. For this experiment the denominator and computation are clear, but “TPR” is potentially misleading.

There is no candidate-finding ↔ human-finding detection match, no count of candidate positives, and no false-positive label. The metric is better named **selected projected-test pass rate**:

`number of selected human-comment tests passed after mediated repair / 234 selected human-comment tests`.

It answers whether a review batch contains enough usable signal for the configured repair agent to satisfy each selected projected check. It does not estimate conventional recall because the evaluator can pass without identifying the same issue explicitly, and it does not estimate precision because extra findings are unpenalized.

The paper's manual usefulness study samples six pull requests from one repository and judges individual comments useful at 88–91% for the four tools (Section 4.2, pp. 6–7). This tiny purposive sample is suggestive only. It lacks reviewer count/qualification, independent assignment, agreement, blinding, sampling probabilities, confidence intervals, severity weighting, and a link from comment-level usefulness to the 234 projected tests. It cannot repair the missing false-positive denominator at suite scale.

## Evidence and result reconstruction

The released artifacts support exact reconstruction of the reported final table by:

1. taking the 184 agent-resolution instances containing 234 `resolved=true` human comments;
2. matching those comments by instance ID and exact comment text to each raw tool-evaluation archive;
3. treating the 20 missing Codex instance outputs and six missing PR-Agent instance outputs as failures, as the released filtering script does; and
4. counting `test_passed=true`.

| Configured review package | Raw result instances | Missing selected instances scored as failure | Passing selected tests | Denominator | Released-audit rate | Paper rate |
|---|---:|---:|---:|---:|---:|---:|
| Claude Code → Sonnet 4.6 repair | 184 | 0 | 75 | 234 | 32.05% | 32.1% |
| Devin → Sonnet 4.6 repair | 184 | 0 | 58 | 234 | 24.79% | 24.8% |
| PR-Agent → Sonnet 4.6 repair | 178 | 6 | 54 | 234 | 23.08% | 23.1% |
| Codex → Sonnet 4.6 repair | 164 | 20 | 47 | 234 | 20.09% | 20.1% |

This is an important reproducibility strength. Missing outputs do not silently disappear from the final denominator, and the raw archives allow the reported numerators to be checked without rerunning commercial endpoints.

However, the paper provides only point estimates. It reports no paired uncertainty, repository-clustered interval, task-type stratification with uncertainty, repeated review/repair runs, rank probability, or sensitivity to the repair agent. The 234 comments are nested in 184 PRs and 67 repositories and share generation and mediation models, so a binomial independent-item interpretation is optimistic. Differences of 4–7 percentage points among the lower three systems are not supported as stable rankings.

The paper/release also contain small internal inconsistencies worth preserving rather than silently repairing:

- Section 3.2 says 481 review comments pass test verification, whereas Figure 2, Table 4, the README, and released stage three show 485.
- Section 3.3 says the final benchmark spans 56 repositories, whereas the abstract, Table 4, README, and released stage four show 67.
- The released filter script's live assertions use 184 instances and 234 comments, but comments and final status messages still refer to stale 149-instance/189-comment counts.
- Stage three has 485 comments while the compressed repair archive has 483 per-comment records, with no typed missingness ledger.

These do not invalidate the final 234-denominator table; they show why executable membership manifests and typed attrition records are necessary.

## Unique insight: consequence projection creates a mediated instrument, not direct artifact measurement

c-CRAB's distinctive lesson is that moving from semantic similarity to execution does not eliminate evaluator mediation—it relocates it.

A direct code-review construct might ask whether the reviewer identifies a consequential defect, communicates it accurately and actionably, avoids harmful false alarms, and supports an acceptable resolution. c-CRAB observes only the final event in this chain:

`authorized source issue H`
`→ generated executable projection T(H, before, merged-after)`
`→ solvability under selected mediator M(H)`
`→ candidate review batch R`
`→ mediator patch M(R)`
`→ T(M(R)) passes`.

Every arrow can change the construct:

- **source-authority error:** the historical comment may be mistaken, superseded, optional, or weakly tied to the merge;
- **projection error:** the test may encode one implementation rather than the underlying concern;
- **selection error:** the issue survives only if GPT-5.2 can test it and Claude Sonnet 4.6 can fix it;
- **mediation error:** the candidate finding may be ignored, misparsed, or supplemented by the repair agent's own inference;
- **attribution error:** one finding may satisfy several tests, and a pass need not identify which finding caused the repair;
- **cost omission:** extra false or harmful findings do not reduce score;
- **observer error:** the generated test may pass despite collateral damage or fail a legitimate alternative.

The reusable implication for `skill-bench` is a **mediated-evaluator claim ceiling**: when a candidate artifact is scored through another agent's downstream action, the result is a property of the full candidate–mediator–environment–observer package unless causal uptake and attribution are separately observed. Executability strengthens the evidence view but does not by itself identify expert-intent fidelity, candidate-artifact correctness, or professional utility.

A second insight is that **curation by successful mediation is collider-like selection**. Final cases are jointly selected by source wording, generator projectability, repository executability, test behavior, and repair-agent ability. Comparing candidate reviewers only on that subset can be operationally useful, but it cannot be promoted to performance on the original human-review population without reporting excluded cases and transport evidence.

A third insight is that **false-positive cost is not optional in intervention benchmarks**. A repair agent can ignore extra findings in a clean sandbox; a human reviewer in production pays attention, verification, delay, trust, and risk costs. A candidate could improve c-CRAB's projected-test pass rate by emitting broad speculative feedback. Without candidate-positive denominators, collateral-change checks, and review-burden measurement, the benchmark rewards sufficient signal but does not establish review quality.

## Reproducibility and operational realism

**Paper inspectability: good.** The 11-page paper defines the conceptual pipeline, models used in curation/repair, final metric, baseline results, categories, manual analysis, and threats. Some exact prompts/configurations are delegated to the repository.

**Release inspectability: strong.** The pinned archive preserves the stage-zero through stage-four datasets; successful and failed test-generation results; generated test files; repair-agent patches and outputs; raw baseline reviews; raw per-tool test outcomes; and the scripts that filter to the final 234. The final table is reproducible from released bytes without paid calls.

**Exact generative reproducibility: weak.** GPT-5.2 and Claude Sonnet 4.6 are commercial endpoints; reviewer CLIs and defaults are mutable; prompts evolved during filtering; and package/model versions, decoding randomness, seeds, endpoint dates, and complete environment image digests are not frozen. Re-running generation or repair would be a new experiment.

**Execution isolation: partial.** Repository workloads run in Docker images, but `DockerContainerSession.start()` adds no explicit `--network none`, CPU/memory/PID limits, read-only root filesystem, capability drops, or no-new-privileges policy. Baseline review agents run with materially different access paths; Claude is invoked with skipped permissions and Codex with full auto. The release does not preserve a complete per-trial network/filesystem/credential exposure record. Public repositories reduce confidentiality concerns but do not eliminate untrusted-code and supply-chain risk.

**Operational realism: moderate for defect-remediation consequence, low for the review lifecycle.** Real PR diffs, historical comments, full repositories, build environments, and executable checks are meaningful. But each case is historical and bounded; the reviewer cannot ask authors questions, participate in discussion, update after replies, prioritize under time, distinguish blocking from optional feedback, or own merge consequences. The repair agent—not the candidate reviewer or a human author—implements the response. There is no latency, cost, attention, trust, acceptance, post-merge defect, or rollback outcome.

## Limitations and validity threats

### Source and content validity

1. Public SWE-CARE PRs are not a defined probability sample of code review.
2. Private, abandoned, non-merged, non-GitHub, and non-supported-language review is absent.
3. Reviewer role, expertise, repository familiarity, decision authority, and comment acceptance are not task-level fields.
4. A merged code change does not prove that each associated comment was correct or causally responsible.
5. The filter removes discussion, questions, and non-testable design feedback, narrowing the construct to executable actionable comments.
6. The 100-comment filter set is used for prompt development and evaluation; 84% agreement is not held-out validity.
7. Raw agreement lacks class balance, chance correction, confusion matrix, disagreement rationale, and severity.
8. Unparseable filter output defaults to HIGH, conflating invalid measurement with inclusion.
9. Repository and PR clustering reduce effective sample size.
10. Public benchmark tests and historical patches create contamination and answer-recovery risk for future systems.

### Projection and oracle validity

11. GPT-5.2 sees before and merged-after code, allowing outcome-informed test projection.
12. Fail-before/pass-after establishes consistency with one transition, not complete review intent.
13. Generated tests may encode exact merged implementation choices.
14. Legitimate alternative fixes are not tested systematically.
15. No independent expert acceptance, mutation score, requirement coverage, or adversarial oracle suite is reported.
16. Structural/style checks can pass while preserving the underlying risk, or fail semantically equivalent code.
17. Collateral behavior and regressions beyond the generated test are not part of the primary decision.
18. The 774 successful generation records do not have a single explicit lineage manifest to the 485 stage-three comments.
19. Stage-three/repair-archive count differs by two comments without typed missingness.

### Selection and mediation validity

20. Half of test-verified comments are removed because one Claude Sonnet 4.6 run cannot resolve them.
21. The final population is selected on the same model configuration later used as evaluator mediator.
22. One repair agent cannot establish general actionability for humans or other agents.
23. Single-run mediator failure mixes stochastic failure with intrinsic unsolvability.
24. The score bundles candidate reviewer, output parser, repair prompt/model/tools, repository state, test, and runtime.
25. Candidate finding ↔ human issue ↔ patch attribution is unobserved.
26. The repair agent can infer defects independently from the diff or combine findings.
27. One finding can satisfy multiple human-comment tests.
28. Candidate findings that are correct but incompatible with the selected mediator can be penalized.
29. No no-review control quantifies repair-agent self-discovery from the diff and prompt alone.
30. No human-repair or multi-mediator sensitivity establishes ranking transport.

### Metric and inference validity

31. “TPR” is not conventional recall because candidate findings are not matched to reference positives.
32. There is no suite-scale false-positive denominator, precision, burden, or harm score.
33. Extra speculative findings can be ignored by the mediator without penalty.
34. Passing tests do not prove the candidate explicitly recognized or explained the issue.
35. The six-PR usefulness sample is too small and underspecified to validate false-positive quality.
36. Reported rates have no paired or repository-clustered uncertainty.
37. One run per configured package provides no repeat reliability.
38. Lower-system rank differences may be unstable.
39. Missing Codex/PR-Agent runs are correctly failed in the final reconstruction, but failure types are not reported in the headline table.
40. Paper count contradictions (481/485 and 56/67) weaken manual provenance even though release counts resolve final membership.

### Treatment, reproducibility, safety, and consequence validity

41. Reviewer tools have different hosting, prompts, permissions, parsers, and affordances.
42. Claude's `sonnet` alias, Codex defaults, PR-Agent dependencies, and hosted Devin behavior are not immutable identities.
43. No complete endpoint/date/version/seed ledger supports exact regeneration.
44. Docker images are named but not bound in the paper to immutable content digests for every trial.
45. Containers lack explicit network denial and resource/capability hardening in the inspected runtime wrapper.
46. Commercial endpoint cost, wall time, repair cost, test cost, and failure-retry burden are absent.
47. No independent reproduction reruns the model-mediated pipeline.
48. Repository code has no detected license, limiting clear reuse.
49. No author/maintainer accepts candidate comments or patches in a live review.
50. No evidence links score to defect prevention, review efficiency, trust, merge quality, rollback, or professional readiness.

## Transferable design patterns

### Retain

1. **Project expert feedback into executable consequence checks.** This is much stronger than text similarity when the projection and claim boundary are explicit.
2. **Require directional evidence.** Fail-before/pass-after rejects checks that do not distinguish the relevant transition.
3. **Preserve the full attrition funnel.** Stage counts reveal how much the construct narrows at each transformation.
4. **Release raw per-case outputs and table inputs.** c-CRAB's final reported numerators can be independently reconstructed.
5. **Fail missing attempts into the declared denominator.** The released filtering path avoids silent denominator shrinkage for missing tool outputs.
6. **Separate curation from final hidden evaluation information.** Candidate review tools are instructed not to inspect historical review comments.

### Repair

1. **Represent every projection edge.** Preserve source-comment authority, exact before/after bytes, generator/version/prompt, generated check, requirement atoms, excluded intent, alternative-valid outcomes, and independent approval.
2. **Keep pre- and post-selection estimands.** Report results over all source comments, quality-filtered comments, test-projectable comments, and mediator-valid comments; never let the final selected subset stand for the source population.
3. **Use plural mediators and a no-review control.** Estimate how much the repair agent fixes from the diff alone, and whether candidate-tool ordering changes across agents/humans.
4. **Observe causal uptake.** Bind each candidate finding to repair-agent references, patch hunks, affected checks, and ignored/contradicted guidance; do not infer use from endpoint success.
5. **Score false-positive and collateral cost.** Preserve candidate finding count, severity, verification burden, harmful edits, unaffected-test regressions, and human triage/acceptance.
6. **Falsify the oracle.** Test semantically equivalent fixes, alternative APIs/structures, mutants that preserve superficial merged features, and patches that pass the projected test while retaining the root issue.
7. **Type missingness and invalidity.** Separate generator parse failure, unavailable image, test timeout, repair-agent failure, candidate parse failure, safety refusal, and substantive test failure.
8. **Bind configured-system identity.** Pin endpoint/date, exact model, prompt hash, CLI/package lock, image digest, permissions, network, resources, retries, and parser version.
9. **Report clustered uncertainty and repeated reliability.** Preserve PR/repository families and repeat candidate and mediator runs before ranking close systems.
10. **Calibrate consequence claims separately.** Maintainer acceptance, defect prevention, attention cost, latency, and production outcomes need independent studies.

## Concrete changes for skill-bench

1. **Do not create a c-CRAB-specific schema.** Reuse the existing projection manifest, artifact/evidence views, configured-system identity, execution validity, metric, and claim-validity machinery.
2. **Add one cross-domain mediated-evaluator adversarial slice when projection conformance is next consolidated.** It should include: a candidate artifact whose downstream agent succeeds without using it; one finding satisfying multiple projected checks; a correct alternative rejected by an implementation-specific oracle; a broad false-positive artifact that passes all positive checks; and mediator-dependent rank reversal. Require source→projection→uptake→action→check lineage and preserve pre/post-selection denominators.
3. **Name mediated metrics literally.** Prefer `selected_projected_check_pass_rate` plus a treatment vector over TPR/recall unless reference matching and candidate-positive labels exist.
4. **Make false-positive cost a non-compensatory companion.** Positive consequence coverage must not erase harmful unsupported claims, collateral state changes, reviewer burden, or mandatory safety/compliance failure.
5. **Use c-CRAB as a Tier A design case for execution-backed feedback projection and a Tier B release case.** Its released raw results are exemplary; its empirical claim remains a configured selected-chain comparison, not professional review validity.

One bounded validation task is warranted because existing projection machinery covers requirement→check alignment but does not yet exercise the distinctive candidate→mediator→action attribution failure and post-mediator selection in one adversarial package. The task should consolidate with current contracts rather than add a new subsystem.

## Claim boundary

c-CRAB v3 and the pinned official release establish that a public pipeline can transform selected real human review comments into fail-before/pass-after executable tests, filter them through one coding agent, and reproducibly compare four configured review-tool → Claude-Sonnet-repair packages on 234 retained projected checks. They provide strong release inspectability and exact final-table reconstruction. They do **not** establish conventional review true-positive rate, precision, comprehensive review quality, expert-equivalent feedback, direct candidate-finding attribution, model-only ability, population-wide code-review performance, operational efficiency, professional acceptance, defect prevention, or production readiness.
