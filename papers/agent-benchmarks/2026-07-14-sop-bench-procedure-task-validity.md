# SOP-Bench exposes a useful procedure package, but its released score mostly tests closed-world oracle recovery—not validated procedural fidelity

**Source.** Subhrangshu Nandi et al., *SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents*, arXiv:2506.08119v2 (23 February 2026), <https://arxiv.org/abs/2506.08119v2>.

**Full text read.** Immutable 27-page v2 PDF: `data/papers/pdfs/2506.08119v2-sop-bench.pdf` (SHA-256 `697bfdf8860a9b7dc17a81b599d2571d3e68225238fd72cb193dbf8a921824e3`). Complete local layout-preserving extraction: `data/papers/text/2506.08119v2-sop-bench.txt` (SHA-256 `dcfc39236fac8b65aed307b614e9ff8fbb0a13231d41d5a22d7765a8ba5bc03d`). The full arXiv source archive is preserved at `data/papers/source/2506.08119v2-source.tar.gz` (SHA-256 `73c4b12177e382d4bf3439c166cd2ec722ef04e82b8bf7e44259ef460f304ff6`). The paper, generation and agent prompts, examples, and appendices were read. Date read: 2026-07-14.

**Release audit.** The author-owned GitHub release was archived at commit `2fdce4c57e6b02b725d5437ec079c142cffd8e07` (6 June 2026), and the author-linked Hugging Face dataset at revision `92633eae202fbf66cceb374c6ad55da41ca693b6` (26 May 2026). Local archives, hashes, inventories, timing boundaries, and cross-surface correspondence are recorded in `data/sources/releases/2506.08119v2-sop-bench/provenance.json`. Both snapshots postdate immutable v2 by more than three months and are evidence about the public instrument, not proof of paper-time byte identity.

## Bottom line

SOP-Bench contributes an unusually inspectable **procedure package**: a natural-language SOP, structured task rows, mock tools, tool specifications, expected endpoint fields, two agent loops, and an evaluator. This is materially more useful for skill-bench than a task prompt plus answer key. Its human–AI construction order—expert task context and draft procedure; AI-assisted schema and refinement; AI-generated data, APIs, and tool code; human review—is also directly relevant to converting expertise into executable evaluations.

But the evidence does not validate the paper's stronger procedure-to-task story. The paper says experts validated every generated datapoint, API, and tool implementation, yet identifies neither the experts and their qualifications per domain nor the review instrument, independent labels, rejection/revision records, disagreements, adjudication, or item-level lineage. The released packages contain no source-authority, reviewer, approval, version, or transformation records. “Human-validated” is therefore an asserted process property, not an auditable task-level warrant.

More importantly, the released metric does not observe SOP compliance. It marks success when parsed endpoint value(s) match CSV fields. It neither specifies a required/accepted procedure graph nor checks ordering, mandatory calls, skipped gates, fallback triggers, audit artifacts, side effects, or alternative valid paths. In multi-output cases it deliberately parses expected fields from the reasoning trace's tool results, so direct retrieval of oracle fields can count even if the agent never emits the required final structured artifact. “Tool Accuracy” in the implementation is only the fraction of calls that returned without an exception, not whether the right tool, arguments, order, or use of evidence was correct.

The mock environments range from useful decompositions to answer-bearing lookups. Dangerous Goods returns four precomputed component scores and leaves the SOP's imputation, sum, and classification rule to the agent. Aircraft Inspection's seven tools, by contrast, each read and return one of the seven scored ground-truth output columns from `test_set_with_outputs.csv`; the all-fields score can therefore collapse to collecting oracle fields. Content Flagging is worse for the paper's reproducibility claim: two supposedly stable mock calculations call unseeded `random.random()`, even though the expected final decision is fixed. Procedure difficulty, tool orchestration, information retrieval, and endpoint formatting are consequently mixed in domain-specific proportions under one TSR.

The defensible claim is bounded: **the paper reports endpoint agreement for configured FC/ReAct agents on thirteen synthetic closed-world SOP configurations, and the later release provides a closely related, partially runnable instrument.** It does not establish faithful execution of expert procedure, preservation of tacit expertise, realistic industrial work, calibrated cross-domain capability, safety, or deployment readiness.

## Why this matters: charter relevance and research question

This is narrow expansion serving charter objectives A and B: understand an important realistic-agent benchmark and extract reusable expertise-to-evaluation machinery without narrowing skill-bench to SOP automation.

The paper's question is whether model/agent combinations can execute complex industrial SOPs through tools, and how architecture, model, domain, tool-registry size, and procedural complexity affect endpoint success. The stricter validity question is:

> When a human-framed and AI-refined SOP, synthetic row, mock tool set, output oracle, parser, and endpoint metric are generated as one package, what evidence shows that a successful task means the procedure was followed rather than that an answer-bearing closed-world interface was navigated?

That distinction matters across domains. A correct final disposition can coexist with a bypassed approval, skipped cross-check, invalid evidence source, untriggered fallback, missing audit record, or unsafe side effect. Conversely, a valid alternative workflow can fail a single canonical endpoint/parser contract.

## One-sentence contribution

The paper supplies three connected artifacts:

1. a human–AI workflow for turning procedural descriptions into schemas, synthetic data, APIs, executable tools, and expected outputs;
2. a synthetic evaluation suite reported as 2,411 tasks over thirteen SOP configurations spanning twelve domains (the two referral-abuse variants are one controlled family); and
3. FC and ReAct harnesses with ECR, conditional TSR, TSR, traces, and latency.

The strongest design contribution is the **co-generated executable bundle**. The procedure is not treated as prose alone: data schemas constrain terms; tools define information access; test rows instantiate decision paths; and expected outputs make trials repeatable. This is the right level at which to test projection drift.

## Unique insight for skill-bench

SOP-Bench makes visible that expert-to-benchmark conversion is a **coupled projection problem**:

`source authority → task context → procedure text → schema → row → tool contracts/code → observable events/artifacts → oracle → parser → score claim`.

Internal consistency across that chain is useful but not sufficient. If one generator and review process co-designs the SOP, rows, tools, and oracle, the package can be self-consistent while misrepresenting professional practice. If tools return oracle fields, package consistency can make the task easier without preserving procedural reasoning. If only endpoints are scored, procedural language can decorate an outcome-classification benchmark without becoming the measured construct.

Skill-bench should therefore preserve a **procedure-projection ledger**, with independent approval and tests at each edge, rather than a single `expert_authored` or `human_validated` flag.

## Methodology and system

### 1. Human–AI construction workflow

The paper reports that domain experts supply an initial business-task SOP and task context. Claude 3.5 Sonnet v2 then helps generate the dataset schema, refines the SOP against that schema, generates synthetic datasets, creates API/tool specifications, and generates executable tool code. Humans reportedly review domain standards, schema completeness, logical consistency, every datapoint, edge-case coverage, API/schema alignment, and code by execution (Sections 3.1–3.2 and the generative-AI appendix).

This ordering has merit. Schema-first generation can make implicit categories explicit; executable tools expose interface defects; and synthetic rows can cover positive, negative, edge, and failure paths. The paper also includes generation prompts and a detailed patient-intake example, which makes the conceptual process more reproducible than prose-only claims.

However, the validation method is not specified at the level needed to evaluate validity:

- no expert roster, qualifications, years of experience, domain-to-expert assignment, independence, or conflicts;
- no distinction between SOP author, artifact generator, verifier, and final approver;
- no per-item validation forms, acceptance criteria, confidence, comments, rejected rows, revisions, or adjudication;
- no inter-reviewer agreement or blinded re-derivation of expected outcomes;
- no audit of whether AI refinement changed the human draft's requirements;
- no sampled comparison to real cases, production distributions, artifacts, or operators; and
- no evidence that “edge cases” have realistic prevalence or consequence.

Three experts independently rate SOP complexity, but those averaged 1–10 judgments validate neither procedure correctness nor task/oracle fidelity. The paper gives one pair of public patient-registration SOP links as motivation for SOP diversity; it does not provide source-to-released-SOP lineage for the benchmark's industrial procedures.

### 2. Task and environment realization

Each public configuration generally contains `sop.txt`, `tools.py`, `toolspecs.json`, `metadata.json`, and a `test_set_with_outputs.csv`; most also include a blinded/output-removed file. The loader passes only `input_columns` to the agent, keeps one or more `output_columns` as the expected result, and makes a domain-specific manager available through the tools.

The row often stores three different kinds of data together:

1. public task inputs;
2. hidden/precomputed values returned by tools; and
3. scored final output fields.

That is a practical mock-server representation, but it needs explicit field roles and leakage checks. The release metadata are uneven: `content_flagging`, `order_fulfillment`, and `warehouse_package_inspection` omit `input_columns`; other domains declare very narrow public inputs while many row columns are reachable through tools. The fallback loader puts the whole row into task inputs when input columns are absent, including the expected-output column, creating a potential direct oracle-exposure path for those configurations.

Representative realizations show that “one benchmark” contains different constructs:

- **Dangerous Goods:** four tools return precomputed SDS, handling, transportation, and disposal scores. The agent must apply missing-score handling, sum the scores, and map the total to one of five classes. This can test tool collection plus a visible decision rule, though it does not test extraction from the source documents because scores are already computed.
- **Referral Abuse v1/v2:** tools return account and traffic attributes plus enforcement guidelines. The agent applies SOP thresholds to choose an action. The controlled easy/hard pair is a promising design, although the variants change many procedural dimensions at once and released lineage does not identify matched cases or isolate each added dependency.
- **Aircraft Inspection:** seven tools select a row by `aircraft_id` and directly return the seven fields that the evaluator scores (`aircraft_ready`, mechanical/electrical results, incident/mismatch/cross-check responses). Some arguments are checked only for non-emptiness and then ignored in lookup. This mostly tests whether the agent calls enough answer-bearing tools and reproduces their outputs.
- **Patient Intake:** six output fields are also returned directly by corresponding mock functions. The final all-fields endpoint can conflate comprehensive retrieval with procedural judgment.
- **Content Flagging:** the procedure requires several computed scores and a final weighted decision. Yet bot probability and device consistency use unseeded random values. A fixed CSV final label is not a stable consequence of repeated tool execution.

The release's 14 data directories also include `order_fulfillment`, which is absent from the paper's Table 3 and main results. This is a later extension, not evidence for the paper's reported 13 configurations.

### 3. Ground truth and scoring

The evaluator calls an agent with the SOP, public task fields, and tools. It parses either the final answer or—when multiple fields are expected—the entire reasoning trace. It then compares parsed values to the held-out CSV output(s). All expected fields must match for a multi-field task.

This endpoint oracle is deterministic when tool outputs and parsing are deterministic, easy to compute, and useful for regression. But it cannot support the paper's outcome language without sharper boundaries:

- **No procedural conformance contract.** The release contains no required steps, ordering edges, pre/postconditions, fallback/exception triggers, accepted alternative paths, or per-step evidence requirements.
- **No trajectory correctness.** A correct endpoint passes despite irrelevant calls, skipped non-endpoint obligations, invalid reasoning, or copied answer-bearing tool output. A wrong endpoint fails even if all observable procedural actions were sound but a formatting/parser issue intervened.
- **Trace-to-oracle shortcut.** For multi-output tasks, the evaluator extracts expected field names from tool results in the reasoning trace before inspecting final output. Where tools return scored outputs directly, merely obtaining those tool results can satisfy the oracle without producing the SOP's required final document.
- **Permissive string equivalence.** Single-field comparison lowercases values, normalizes hyphens/underscores, and accepts either string containing the other. This can make semantically distinct actions equivalent (for example, `account closure` is contained in `permanent account closure`) and can accept negated/explanatory strings containing the expected label.
- **Null equivalence.** `none`, `null`, `na`, `n/a`, `nan`, `unknown`, and empty string are treated as equal. The released Aircraft Inspection expected outputs contain 23 empty field values across 112 rows, so an `unknown` output can agree with an absent oracle value.
- **Tool “accuracy” is execution success.** The metric counts a call as correct when its `success` flag is true; the manager sets that flag when code returns without exception. It does not compare tool choice, arguments, call necessity, sequence, or output use against an expert trace.

Thus TSR is **parsed endpoint agreement under a domain-specific mock package**. ECR is whether execution avoided runtime failure (including endpoint mismatches as completed). C-TSR is endpoint accuracy conditional on that operational definition. The identity `TSR = ECR × C-TSR` is bookkeeping, not additional validation.

### 4. Empirical evaluation

The paper evaluates FC and ReAct agents with eleven named frontier models. FC uses native function calling for compatible models and up to ten iterations; ReAct uses a custom loop with up to fifteen iterations and requires at least one tool call. Temperature is 0.5 and output limit 8,000 tokens. The main comparison reports per-SOP ECR, TSR, and latency; appendices list model/agent results. Ablations compare 26 versus 6 tools for Video Annotation and easy versus hard Referral Abuse procedures.

The paper's findings are useful as descriptive configured-system observations:

- architecture rankings reverse by domain;
- newer model versions do not monotonically improve a fixed agent loop;
- adding twenty distractor tools coincides with a 16.2-point TSR decrease in one Video Annotation condition; and
- the harder referral procedure raises latency while preserving high endpoint success for one model.

But inference is limited:

- no run-level results, traces, prompts as rendered per run, exact provider snapshots, dates, seeds, retry records, or cost records are released;
- no repetitions are reported despite temperature 0.5 and at least one nondeterministic tool implementation;
- displayed “standard errors” summarize variation across heterogeneous SOPs, not repeated-trial uncertainty for a configured system;
- model and agent are partly nested (FC only for compatible Claude models), so broad architecture comparisons are not controlled across the same backbone set;
- domain averages macro-average different task counts, output cardinalities, answer-bearing interfaces, and procedural demands;
- the registry-bloat ablation is one SOP/model/agent comparison and may also depend on prompt ordering; and
- easy/hard referral variants add steps, decisions, history, and enforcement levels together, so they do not identify a single complexity cause.

These results support “architecture choice is task-package dependent” more strongly than claims about domain generalization or real industrial workflows.

## Release and reproducibility audit

### Paper–release count mismatch

The paper's Table 3 reports 2,411 tasks over 13 configurations. At pinned GitHub commit `2fdce4c`, the 13 paper-listed `test_set_with_outputs.csv` files contain 2,124 rows; including the post-paper `order_fulfillment` directory yields 2,154. Per-domain differences are substantial: paper/release counts include Content Flagging 226/168, Customer Service 208/156, Dangerous Goods 327/274, Email Intent 122/186, Know Your Business 122/90, and Video Annotation 168/125. Output-removed files do not resolve this cleanly: in some domains they are subsets, while in others they appear to be blinded copies of the same population.

The later public data can support new evaluations, but not exact reproduction of paper denominators or tables. The release includes no paper result CSVs, traces, or immutable paper-time dataset manifest.

### Divergent official surfaces

Across the pinned GitHub and Hugging Face data trees, 305 of 311 common paths are byte-identical. Six differ, and GitHub has one additional metadata file. Critically, the Hugging Face `email_intent` SOP and CSVs contain unresolved Git conflict markers (`<<<<<<< Updated upstream`), causing ordinary CSV parsing to produce a one-column malformed dataset. The two official surfaces therefore cannot be treated as interchangeable. The GitHub snapshot is the more runnable acquisition-time instrument, but neither proves paper-time correspondence.

### Executability and test coverage

A clean temporary environment required manually installing runtime packages because the release's `pyproject.toml` declares no project dependencies. With dependencies present and `AWS_REGION=us-west-2` set to avoid host/dotenv configuration overriding the asserted default, the release's test suite returned **9 passed**. Without controlling that variable, two default-configuration tests failed because repository configuration loaded `us-east-1` from the environment.

The passing suite covers configuration and a mock base agent only. It contains no benchmark-loading, schema/row consistency, tool contract, oracle re-derivation, parser adversarial, deterministic replay, paper-count, cross-surface, or end-to-end evaluation tests. Nine passing unit tests therefore do not validate the released benchmark data or scorer.

### License and operational realism

The code/data release is CC BY-NC 4.0. That enables research inspection but restricts commercial reuse, relevant for a benchmark positioned toward industrial deployment decisions.

Operationally, the mocks are cheap and stable in many domains, avoid credentials and live-service failures, and make controlled regression possible. They do not reproduce latency, permission boundaries, partial outages, stale records, concurrent updates, human escalation, irreversible effects, audit/compliance review, or affected-party consequences. Some outputs include current timestamps/UUIDs and Content Flagging is stochastic. The paper itself acknowledges deterministic mock tools and simplified SOPs; the public implementation shows that even this simplified environment needs determinism and conformance validation.

## What the evidence supports

1. A human–AI pipeline can produce an inspectable bundle of SOP prose, synthetic records, tool interfaces/code, endpoint labels, and an evaluation harness across many domains.
2. The paper reports substantial endpoint-accuracy variation across named model/agent packages and SOP configurations.
3. Procedure/package characteristics matter: tool-set size, output cardinality, answer-bearing tool design, context length, and branching can alter measured performance.
4. A schema-first, executable-artifact workflow is a promising benchmark-authoring scaffold.
5. The post-v2 GitHub release is sufficiently complete to audit many projection and scoring choices and to run its narrow nine-test suite.

## What it does not support

- verified expert authorship or approval at the task/field/procedure level;
- faithful preservation of tacit domain expertise;
- correctness of all generated SOPs, rows, tools, or expected outputs;
- procedural compliance, step accuracy, or correct tool orchestration as distinct from endpoint agreement;
- representative industrial tasks, case distributions, APIs, operating conditions, or consequences;
- exact reproduction of the paper's 2,411-task experiments from the public release;
- stable configured-system rates under stochastic model/tool execution;
- cross-domain general agent capability;
- professional equivalence, safety, production fitness, economic value, or deployment readiness.

## Limitations of this review

This audit read the full immutable paper/source and inspected both pinned public releases. It did not spend on provider APIs or attempt to reproduce the paper's 11-model matrix. The public snapshots postdate v2; implementation findings therefore characterize those snapshots and identify correspondence gaps, not necessarily undisclosed paper-time code. The row/tool audit is broad and includes exact counts, metadata, scoring code, all random/time calls, and representative domain implementations, but it is not an independent domain-expert re-annotation of 2,000+ synthetic cases.

## Transfer to skill-bench

### Retain

1. **Bundle procedures with executable interfaces.** A useful task package should include source/procedure, public inputs, hidden evidence, tools, output/artifact contract, and runnable checks.
2. **Use schema before generation.** Explicit types, decision categories, compliance gates, and expected artifacts can constrain generation and expose missing requirements.
3. **Build controlled variants.** Matched easy/hard or minimal/bloated forms can test specific hypotheses when all other dimensions and rows are held fixed.
4. **Report execution separately from substantive correctness.** Environment/runtime failure should not be silently merged with task failure.
5. **Preserve domain-level results.** Aggregate scores can hide architecture reversals and instrument differences.

### Repair

1. **Add a procedure-projection ledger.** For each task, record source authority/version, exact clauses, human/AI transformations, schema fields, row generator/version, tool semantics, expected events/artifacts, oracle derivation, reviewers, decisions, revisions, and approval scope.
2. **Separate field roles.** Mark every row field as public input, hidden evidence, tool output, scored endpoint, audit-only metadata, or prohibited oracle. Validate that public inputs and tool responses cannot expose prohibited outputs except where explicitly intended.
3. **Compile a conformance contract.** Represent mandatory/optional steps, preconditions, ordering, dependencies, fallback/exception triggers, side effects, audit artifacts, and accepted alternative paths. Score criterion-level observations before applying an endpoint policy.
4. **Independently derive oracles.** Do not let the same generated row be both mock database and unverified answer key. Recompute expected outcomes with a reference implementation, cross-review sampled cases, mutation-test thresholds, and preserve disagreements.
5. **Freeze determinism.** Seed or remove randomness, freeze time/UUID providers, test repeated replay, and distinguish intended environmental stochasticity from defects.
6. **Use typed comparators.** Enumerated actions require exact canonical equality; booleans, numbers, dates, sets, and documents need type-specific checks. Never use unrestricted substring matching for consequential labels.
7. **Score tool behavior honestly.** Distinguish call execution, tool selection, argument validity, evidence returned, evidence adopted, ordering, and required-call coverage. Runtime success is not tool accuracy.
8. **Keep final artifact and trace evidence separate.** Tool-returned oracle fields can be evidence, but they should not silently substitute for a required final report or decision artifact.
9. **Version paper and release forms.** Publish task IDs, manifests, counts, rendered prompts, snapshots, traces/results, exclusions, and migration notes so later extensions do not overwrite the evaluated instrument.
10. **Test benchmark integrity.** Add end-to-end data loading for every domain, conflict-marker checks, metadata/CSV contract checks, tool determinism, oracle re-derivation, parser adversarial cases, and paper-count reconciliation.

### Test before adopting broadly

Run a small cross-domain pilot where two qualified reviewers independently map source clauses to procedure relations, expected evidence, accepted paths, and endpoint artifacts. Compare three scores on repeated trials:

1. endpoint only;
2. procedure-conformance only; and
3. joint procedure-plus-endpoint success.

Include answer-bearing-tool and evidence-bearing-tool variants, deterministic replay, relation mutations, valid-alternative traces, wrong-order traces, skipped-gate traces, and endpoint-correct/procedure-wrong counterexamples. The key empirical question is how often endpoint TSR changes the ranking or diagnosis relative to the joint contract.

## Concrete repository actions

1. Build a reusable **procedure-package conformance validator** that checks field-role leakage, metadata/CSV/tool contracts, deterministic replay, typed oracle comparators, and procedure/event coverage. This generalizes beyond SOP-Bench to any generated skill/task/environment package.
2. Integrate the procedure-projection ledger into existing expertise-transfer and validity machinery rather than creating an SOP-specific benchmark schema.

## Verdict

**High methodological relevance; moderate inspectability; low demonstrated procedure-to-task validity.** SOP-Bench should influence skill-bench's authoring architecture because it operationalizes the whole procedure/data/tool/oracle bundle. It should not supply a validity shortcut. Its public instrument demonstrates exactly why endpoint correctness, executable tools, and asserted expert review must remain separate from evidence that procedural expertise survived projection and was actually followed.