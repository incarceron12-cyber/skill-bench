# Independent freeze review: pre-task procedure transfer v5

**Decision:** **BLOCK EXECUTION** of `build-execute-v5-endpoint-matrix`.

**Evidence status.** This is a commit-bound, zero-call validation review of commit `6195ab494213b3e86f2e46d88472f7b7e23aeb40`, not a paper review. I read the complete v5 instrument, the frozen v4 source corpora and bindings, the v4 post-hoc defect audit, and the builder preflight. I did not treat the builder's derivation or preflight as an independent oracle. I recomputed all manifest hashes, independently derived the four endpoints from public inputs and source propositions, and executed a separate ten-test mutation suite. No v5 frozen instrument byte was edited and no model, provider, executor, repair, or retry attempt was made.

- Machine report: [`reports/validation/2026-07-18-pretask-procedure-v5-independent-freeze-audit.json`](../../reports/validation/2026-07-18-pretask-procedure-v5-independent-freeze-audit.json)
- Independent tests and literal oracles: [`tests/test_pretask_procedure_transfer_v5_independent_audit.py`](../../tests/test_pretask_procedure_transfer_v5_independent_audit.py)
- Instrument: [`pilots/pretask-procedure-transfer-v5/`](../../pilots/pretask-procedure-transfer-v5/)
- Normative source rules: v4 [`epsilon`](../../pilots/pretask-procedure-transfer-v4/families/epsilon/corpus.json) and [`zeta`](../../pilots/pretask-procedure-transfer-v4/families/zeta/corpus.json)
- Parent defect diagnosis: [`posthoc-endpoint-audit.json`](../../pilots/pretask-procedure-transfer-v4/posthoc-endpoint-audit.json)

## Contribution and research question

The review tests a narrow but general benchmark-lifecycle question: **does a repaired, frozen endpoint instrument have enough independent evidence to authorize costly trials, or does agreement among co-produced tasks, private answers, deriver, checker, and preflight conceal common-mode defects?**

This advances charter objectives B and C as validation. Its concrete artifacts are an independent oracle/mutation suite and a fail-closed release decision. It clarifies the boundary between (1) correct endpoints for the four current fixtures, (2) a checker that enforces the declared artifact contract, (3) a deriver that conforms to its normative source, and (4) a source that is actually applicable to the new instrument version. The two synthetic families remain mechanism probes; they do not narrow the benchmark to custody or transaction journals.

## Methodology

The audit used five deliberately separate evidence paths:

1. **Byte and lifecycle reconstruction.** Recompute SHA-256 and byte sizes for every v5 component and all six external bindings; compare v5's 32 assignment cells and order with v4; inspect protocol-, manifest-, task-, and row-level attempts; inspect all claim ceilings and prohibited execution artifacts.
2. **Independent endpoint derivation.** Implement literal epsilon and zeta interpreters in the audit test without importing `prepare_freeze.expected`, `derive_expected`, `preflight.validate`, or checker expectations. Compare only after normalizing the explicitly unscored reason text.
3. **Public-basis review.** Trace every checked field to `public.md`, `input.json`, and the exact source proposition, then inspect source authority scope and valid time rather than equating hash binding with applicability.
4. **Checker soundness and completeness mutations.** Exercise paraphrases, reversed observation order, alternate JSON key order/whitespace, inclusive/expired threshold boundaries, arithmetic contradictions, omissions, wrong identifiers, wrong types, cross-family substitution, extra fields, condition tokens, and JSON scalar-type collisions.
5. **Derivation common-mode probe.** Construct an ancestor-rollback case directly from Z-P3's language and compare a literal independent result with the builder deriver. This tests the source-to-deriver edge rather than merely comparing two consumers of the same implementation.

## Evidence and findings

### What passed

- Every component and external-binding hash and byte count recomputed exactly.
- V5 preserves all 32 v4 `(schedule_index, task_id, family_id, condition_id)` cells and order; row attempts are zero.
- Protocol attempts are all zero, execution remains unauthorized, and transfer, capability, utility, expert provenance, professional validity, production fitness, and readiness remain false.
- The four frozen endpoint semantics are correct under the independent literal oracles:
  - `k4n7`: release; blue evidence is age 20, satisfying `<= 24`.
  - `p9c2`: release under signed-scan precedence and freshness.
  - `t6v1`: valid, final state `{"x": 1}`, committed `A`, rolled back `B`.
  - `w3d8`: invalid with no certified final state because `D` remains open.
- The checker accepts reason paraphrases, key-order/whitespace changes, and observation-order changes as declared; it rejects the tested omissions, wrong identifiers, wrong top-level boolean type, arithmetic/consequence flips, and cross-family artifacts.
- The independent epsilon boundary probe releases at exactly 24 hours and quarantines at 25.

These are meaningful successes. They show that v5 repaired v4's known arithmetic endpoint and hidden-literal/reason-wording failures for the current fixtures. They do **not** authorize execution because four independent gates fail.

### Fatal finding 1: the normative source excludes v5

Both frozen corpora declare `authority_scope.valid_time` as “pretask procedure transfer v4 internal calibration only”; every proposition says `valid_time: "v4 only"`. V5's protocol binds and reuses those exact files as its normative source. A hash proves byte identity, not authority beyond declared scope. V5 therefore has no applicable source basis for its private consequences as currently versioned.

This is not cured by saying that v5 changes only the endpoint. The point of a valid-time field is to force an explicit authority decision when a rule crosses a version boundary. The repair needs a versioned v5 applicability record or an explicit authority amendment that preserves the proposition content while extending its declared use. Editing the frozen v4 source in place would destroy the evidence boundary.

### Fatal finding 2: extra and condition-bearing fields pass

The public task asks for one object “using exactly these public field types,” and v5 describes its checker as typed and structural. The checker, however, validates selected fields without closing either object schema. An otherwise canonical artifact containing:

```json
{
  "condition_id": "reference_procedure",
  "uncontracted_payload": {"answer_hint": "retained"}
}
```

passes for both families; epsilon decision rows also accept arbitrary fields. This fails the requested extra-field and condition-token-leakage gates. Even though the checker does not branch on `condition_id`, allowing treatment identity or answer-bearing payload into a passing result defeats a strict blinded artifact contract and can contaminate retained outputs or downstream observers.

The repair should reject unknown keys at the top level and within every decision row. If extensions are intentionally allowed, the public contract must define an extension namespace and downstream information-flow policy; silent acceptance is not condition blindness.

### Fatal finding 3: Python equality collapses distinct JSON types

For `t6v1`, replacing expected `final_state.x = 1` with `final_state.x = true` still passes because Python considers `True == 1`. JSON defines boolean and number as distinct types. Consequently, line-level `dict` equality does not establish the claimed typed semantic consequence.

This is a concrete checker false accept, not a hypothetical style concern. The checker needs recursive JSON equality that first requires exact type identity (with an explicit policy for integers versus non-integral/floating numbers) and only then compares values and object/array structure. Mutation tests should include `true/1`, `false/0`, `1/1.0` according to the chosen numeric policy, null/object, and nested collisions.

### Fatal finding 4: builder derivation and preflight share a Z-P3 error

Z-P3 states: “Rollback discards the target transaction mutations and all still-open descendants, recording their identifiers in rollback order.” The builder deriver permits rollback only when the target is `stack[-1]`. On a journal with open `A > B` and `rollback A`, the independent literal interpreter validly discards `B` then `A`; the builder declares the journal invalid before applying Z-P3.

The four frozen fixtures do not exercise ancestor rollback, so their endpoints remain independently correct. The defect nevertheless falsifies the broader source-conformance gate and demonstrates the exact common-mode risk this review was meant to detect: `derive_expected.py` imports `prepare_freeze.py`, while `preflight.py` imports the same builder module. Agreement among private answers, “independent” derivation, and preflight is therefore one implementation agreeing with itself.

A fresh version needs a genuinely separate oracle or declarative fixture table plus source-targeted mutations for ancestor rollback, duplicate transaction identifiers, ancestor commit attempts, unmatched closes, repeated keys, and valid alternatives. Critical source semantics should not be validated only by importing their generator.

## Unique insight

The central lesson is that **freeze integrity has four non-inheriting dimensions**:

`byte identity → source applicability → independent semantic derivation → checker language closure`.

V5 passes byte identity and the four fixture endpoints, yet fails applicability and checker closure. This is stronger evidence than either “the builder preflight passes” or “a mutation was rejected.” A manifest can faithfully freeze an out-of-scope source; two derivation entry points can share one faulty implementation; and a condition-blind checker can still admit condition-bearing artifacts. Pre-execution review must therefore test the edges between components, not only each component's self-consistency.

The reusable benchmark implication is a release rule: **a trial instrument is not execution-ready until an independent reviewer can produce both valid alternatives the checker accepts and invalid artifacts the checker rejects under a currently authorized source basis.** Mutation adequacy must include language completeness (false accepts), not only rejection of planted private-answer changes.

## Limitations and reproducibility

- This is an internal synthetic calibration audit, not external evidence about expertise transfer or realistic knowledge work.
- The independent epsilon interpreter resolves valid-time precedence literally from E-P2/E-P3; the four current fixtures do not force a contested expired-high-authority versus fresh-low-authority interpretation.
- “Rollback order” for ancestor rollback is interpreted inner descendant to target (`B`, then `A`) because that is the executable discard order. The source should state the ordering explicitly in the repair. The builder's invalid result still conflicts with Z-P3 regardless of ordering.
- The suite tests representative schema and scalar collisions, not an exhaustive JSON grammar or adversarial parser differential.
- No model call was warranted: the defects are deterministic prerequisites. Therefore this review says nothing about v5 treatment effects, reliability, or model behavior.
- The report is reproducible with:

```bash
python -m unittest tests.test_pretask_procedure_transfer_v5_independent_audit -v
```

The retained run returned 10 tests, zero failures, and zero errors. Passing means the independent positive checks and the documented defect witnesses reproduced; it does **not** mean v5 passed review.

## Benchmark relevance and next actions

1. **Block `build-execute-v5-endpoint-matrix`.** Do not adapt the launcher or execute any row against v5.
2. **Create v6; do not edit frozen v5.** Preserve v5 as evidence of a failed independent gate.
3. Add an explicit, versioned source-applicability record authorized for v6 while retaining the exact proposition lineage to v4.
4. Close object schemas at every level or publicly define constrained extensions; reject condition/treatment fields and uncontracted payloads.
5. Implement strict recursive JSON type/value comparison.
6. Separate generator, oracle, checker, and preflight implementations; add source-proposition mutations, especially Z-P3 ancestor rollback.
7. Repeat a commit-bound independent freeze review before calls. Keep all seven claim ceilings false after any mechanical repair.

No new queue task is added by this review: the blocked execution task already carries the operational dependency, and the blocker reason gives the exact v6 repair path. Adding a duplicate build task would obscure the fail-closed lifecycle rather than improve it.
