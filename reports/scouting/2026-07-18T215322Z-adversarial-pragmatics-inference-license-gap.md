# Scouting note — pragmatic-label inference-license validity gap

- **Timestamp:** 2026-07-18T21:53:22Z
- **Evidence status:** arXiv metadata/abstract, immutable endpoint checks, web release discovery, and exact local duplicate searches only. The PDF, HTML/source body, benchmark items, validator, pilot records, prompts, labels, or analyses were **not** deeply read, downloaded into the repository, executed, or audited during scouting.

## Substantive candidate — triage only

**Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity** — Brett Reynolds; arXiv:2607.01153v2 (revised 2026-07-15).

- Immutable record/PDF/HTML/source: https://arxiv.org/abs/2607.01153v2 · https://arxiv.org/pdf/2607.01153v2 · https://arxiv.org/html/2607.01153v2 · https://export.arxiv.org/e-print/2607.01153v2
- At scouting time all four endpoints returned HTTP 200; observed response sizes were 42,845, 318,366, 143,465, and 2,807,285 bytes respectively.
- The abstract describes a seven-phenomenon controlled taxonomy spanning instruction conflict, embedded commands, quotation, scope ambiguity, deixis, indirect speech acts, and multi-turn agent transcripts; an 18-item seed benchmark; a 54-row local seed pilot; validator-enforced metadata; and an evaluation protocol separating task success, policy compliance, safety risk, refusal outcome, and evaluator confidence. It frames labels as condition-bounded “inference licenses” whose projection should be tested across paraphrase, wrapper, model, and judge conditions. These are author-stated abstract claims awaiting full-paper verification.
- The abstract reports that a rubric-aided judge graded its own outputs with expected-behaviour fields visible yet missed safety-relevant minority classes. This is a candidate observer-coupling and evidence-view result, not evidence of general judge unreliability.
- No official code/data repository was found in the arXiv record or exact-title web search during this run. A reviewer should inspect the complete paper/source and retry release discovery rather than infer permanent absence.
- Exact title, ID, and distinctive-phrase searches found no local review or queue task. Existing Ambig-DS, UnderSpecBench, AgentRewardBench, ComplexConstraints, ScopeJudge, and Context-to-Execution Integrity reviews address adjacent ambiguity, authority, rater, rubric, gating, and action-integrity boundaries, but not label projection across controlled pragmatic transformations.

## Why this is a narrow, useful gap

The reusable chain is:

`public utterance and context → candidate interpretations → authority/scope resolution → action and policy applicability → task outcome → safety-relevant consequence → observer evidence view → typed label plus confidence/disagreement → projection test under paraphrase/wrapper/model/judge changes`.

This directly tests charter principles around public basis/private consequence, plural measurement, alternative valid paths, configured-rater identity, and expert disagreement. A binary outcome can hide whether a failure arose from task capability, instruction conflict, ambiguous policy, scaffold behavior, refusal policy, or observer instability. Conversely, a fine-grained label taxonomy is not validated merely because it is linguistically plausible or schema-checked.

The main validity risks are the small author-created seed, unclear expert identity and independence, self-judging, visible expected-behaviour fields, sparse minority classes, condition dependence, and any gap between validator conformance and substantive label correctness. The source should therefore be reviewed as a methodological probe, not treated as a realistic knowledge-work benchmark or safety assurance instrument.

## Charter decision filter and queue action

- **Objectives advanced:** A (benchmark validity, human evaluation, and safety evaluation), B (fair interpretation-to-requirement/check projection), and E (clear distinction among competing label and claim meanings).
- **Concrete evidence:** immutable-v2 full-paper review, preserved PDF/text provenance, release-presence audit, and reconstruction of item/condition/label/judge denominators.
- **Uncertainty clarified:** whether pragmatic categories and typed outcome labels provide stable diagnostic measurement, and what evidence is needed before one interpretation becomes a scored obligation or safety claim.
- **Mode:** narrow expansion/human learning. Two higher-priority consolidation tasks remain pending; one lower-priority review restores a small research buffer without repeating broad searches.
- **Duplication/scope check:** exact searches were negative and adjacent reviews are explicit comparators. Linguistics/safety is a bounded measurement-method case, not a benchmark-domain commitment.
- **Useful completion:** distinguish taxonomy plausibility, annotation consistency, configured-judge behavior, label projection, realistic-task validity, and safety consequence; preserve all claim ceilings and map only nonduplicative implications into existing contracts.

Added one task: `review-adversarial-pragmatics-inference-license-validity` (review, priority 44). No second task was queued. Experience Memory Graph (arXiv:2607.13884v1) was triaged but deferred because its failed/successful-trajectory graph matching and retrieved correction guidance substantially overlap the freshly reviewed AgentTether, AFTER, Compliance Trap, and memory/recovery corpus.
