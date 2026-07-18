# Independent freeze review: pre-task procedure transfer v7

**Decision:** **PASS THE FREEZE GATE FOR A SEPARATE, BOUNDED V7 EXECUTION TASK.**

**Evidence status.** This is a commit-bound, zero-call validation review of commit `0b7f9306ec6c3a18d4f5bba98af3eabd2ea7f200`, which exactly matched `origin/main` at audit time. It is not a paper review and not configured-agent evidence. I read the complete v7 instrument, its v6 parent and retained failed reports, the v4 normative internal corpora, source-applicability lineage, builder, oracle, checker, preflight, canary runner, tests, tasks, private endpoints, assignments, and manifests. I did not use the builder preflight as the independent decision rule. I recomputed every frozen hash and size, hard-coded the four expected endpoints from source/input inspection, parsed oracle dependencies with Python AST, wrote a separate seven-test audit, reran source-targeted and checker-language mutations, reran both zero-call canary arms, and reran preflight. No model, provider, executor, repair, or retry attempt occurred.

- Machine decision: [`reports/validation/2026-07-18-pretask-procedure-v7-independent-freeze-audit.json`](../../reports/validation/2026-07-18-pretask-procedure-v7-independent-freeze-audit.json)
- Independent audit: [`tests/test_pretask_procedure_transfer_v7_independent_audit.py`](../../tests/test_pretask_procedure_transfer_v7_independent_audit.py)
- Instrument: [`pilots/pretask-procedure-transfer-v7/`](../../pilots/pretask-procedure-transfer-v7/)
- Narrow authority record: [`source-applicability.json`](../../pilots/pretask-procedure-transfer-v7/source-applicability.json)
- Normative internal sources: v4 [`epsilon`](../../pilots/pretask-procedure-transfer-v4/families/epsilon/corpus.json) and [`zeta`](../../pilots/pretask-procedure-transfer-v4/families/zeta/corpus.json)
- Preserved failed parent evidence: v6 [`canary-report.json`](../../pilots/pretask-procedure-transfer-v6/canary-report.json) and [`preflight-report.json`](../../pilots/pretask-procedure-transfer-v6/preflight-report.json)

## Contribution and research question

This audit tests a general benchmark-lifecycle question: **after an independent review blocks a frozen instrument and its prospective successor itself fails mechanically, can a new version preserve the failures as evidence while repairing only the failed edges strongly enough to license a later empirical run?**

It advances charter objectives B and C through validation. The concrete artifacts are a commit-bound machine decision and an independent mutation suite. The uncertainty is whether v7 has current source applicability, byte-complete ancestry, semantically independent endpoints, a closed checker language, and a real output-capable isolation envelope—not whether the synthetic procedures transfer or are professionally useful. The custody and journal families remain deliberately unlike mechanism probes; passing them does not narrow `skill-bench` to either domain.

## Methodology

The review used seven distinct evidence paths:

1. **Commit and byte identity.** Confirm `HEAD == origin/main == 0b7f930...`; recompute SHA-256 and byte size for all 22 v7 components and 33 external bindings.
2. **Failed-parent preservation.** Verify the external-binding inventory contains every v6 frozen component plus the exact failed v6 manifest, canary report, and preflight report. This checks that v7 did not rewrite lifecycle evidence.
3. **Applicability rather than mere provenance.** Recompute the v6 parent-authority hash, both v4 corpus hashes, and all eight proposition statement hashes. Check that the record says builder-authored internal calibration only, `v7 only`, and does not edit v4 authority.
4. **Independent fixture endpoints.** Write literal expected structures for `k4n7`, `p9c2`, `t6v1`, and `w3d8` from source/input inspection; compare those literals separately with frozen private semantics and `oracle.py` output after normalizing only declared non-scored reason prose.
5. **Source-targeted mutations.** Exercise epsilon's inclusive 24-hour boundary and authority precedence; exercise zeta ancestor rollback, unmatched close, duplicate sequence, and ancestor commit.
6. **Checker-language mutations.** Show declared reason/order alternatives pass while condition/treatment/uncontracted fields, duplicate JSON keys, `NaN`, and nested `true`/`false`/`0`/`1.0`/`null`/object substitutions fail.
7. **Execution-envelope reproduction.** Rerun no-package and reference-package bubblewrap probes and then the full path-checking preflight. Both probes had `/trial` cwd, only arm-allowed inputs, writable unique outputs, no repository/private visibility, no outside write, and identical sandbox signatures apart from staged input content.

## Evidence and result

### Exact freeze and ancestry pass

All 55 bound files (22 components plus 33 external bindings) matched their declared bytes and SHA-256 values. V6's entire frozen component inventory is included in v7's bindings, as are v6's exact failed manifest, failed canary, and failed preflight. Rerunning v7 canaries and preflight did not change their committed report bytes.

This matters because prospective repair is credible only if failure history remains inspectable. V7 does not convert v6's failure into a retroactive success; it creates a new instrument with a new identity.

### Authority and semantic closure pass—narrowly

The v7 applicability record correctly distinguishes two facts that v5 conflated:

- the immutable proposition statements still say `v4 only`; and
- a separate, hash-bound v7 record authorizes unchanged interpretations for **synthetic v7 internal calibration only**.

Every corpus and statement hash recomputed. The parent record is the exact v6 applicability file, and the Z-P3 interpretation explicitly defines rollback order as innermost still-open descendant outward, then target. This repairs source applicability without pretending the original v4 authority changed.

The four literal endpoints matched both private records and the separately implemented oracle. AST inspection found only `__future__`, `argparse`, `json`, `pathlib`, and `typing` dependencies in `oracle.py`; there is no parsed static or literal dynamic dependency on the builder, checker, or preflight. Unlike v6's substring scan, comments and docstrings cannot create a false coupling result.

Source mutations also behaved as the propositions require:

- an exactly 24-hour broken signed scan remains controlling and quarantines;
- at 25 hours it expires, allowing a fresh intact unsigned note to control and release;
- rolling back ancestor `A` with open child `B` is valid and records `B`, then `A`;
- unmatched closure, duplicate sequence, and ancestor commit with an open child are invalid.

### Checker language passes the tested completeness and soundness boundary

For every task, non-empty reason paraphrases pass. Epsilon decision and observation ordering variants pass as publicly declared. The checker rejects `condition_id`, `treatment_metadata`, and `uncontracted_payload` at the top level; nested epsilon additions also fail. Strict parsing rejects duplicate keys and non-finite numbers. Recursive comparison distinguishes booleans from integers and integer-form from decimal-form numbers, so the concrete v5 false accept—`true` for expected `1`—is closed.

This does not prove exhaustive parser security. It does establish that the checker accepts representative members of the declared equivalence class and rejects the exact condition-leakage, object-closure, and JSON-type defects that previously blocked execution.

### Repaired canary and preflight pass

Both fresh canary arms passed. Staging `inputs/outputs` before read-only-binding `/trial` allows the output overlay that v6 lacked. In each arm:

- cwd was `/trial`;
- observed files exactly matched the arm allowlist;
- `/home/sam/skill-bench` and `/trial/private.json` were absent;
- writing `/trial/outputs/canary.txt` succeeded;
- writing `/trial/escape.txt` failed;
- model, provider, and executor counts remained zero.

The equal-envelope comparison passed, and the subsequent path-checking preflight reported no errors across all nine gates. The independent suite returned seven tests, zero failures, and zero errors.

## Unique insight

The result sharpens the earlier four-part freeze rule into a **prospective-repair chain**:

`retained failed bytes → new version identity → current narrow authority → independent semantic witness → checker language closure → output-capable equal envelope → separate empirical execution`

No link inherits from the previous one. Preserving a failed parent does not repair it; a current authority record does not prove semantics; endpoint agreement does not close the accepted language; an isolated read-only task root does not prove the declared output path is writable; and a passing zero-call envelope does not establish full agent behavior. V6 is useful evidence precisely because it passed semantics while failing the final mechanical edge. V7 passes that edge without erasing the distinction.

The reusable benchmark implication is that **failed pre-execution freezes should become immutable regression fixtures for successor freezes**. A successor should bind not only the prior manifest but the prior failed observations, then demonstrate that its change is prospective and edge-local. This prevents a common operational anti-pattern: silently repairing the artifact that documented the failure and thereby destroying evidence about lifecycle quality.

## Limitations and operational realism

- Authority is builder-authored internal calibration only. There is no domain expert, professional standard, or external source behind these rules.
- Four task forms across two synthetic families are useful for conformance contrast but cannot establish domain coverage or representativeness.
- AST dependency inspection rules out direct static and literal dynamic imports; it cannot prove independent authorship, hidden common design assumptions, or all runtime dependency tricks.
- The canary executes a small Python probe under the declared bubblewrap command. It does not exercise the full Hermes/model/provider/file-tool stack, timeout behavior, trace capture, or 32-row scheduler.
- Equal command signatures establish outer-envelope parity, not equal cognitive information. Treatment materials intentionally differ, and later reporting must preserve package bytes and retrieval exposure.
- The source-targeted/checker mutations are representative, not an exhaustive JSON grammar, parser differential, state-machine model check, or adversarial sandbox audit.
- No configured-agent run occurred. The result licenses only a separate bounded execution attempt; it says nothing about capability, transfer, treatment effect, reliability, utility, cost efficiency, professional validity, production fitness, or readiness.

## Benchmark relevance and next actions

1. **Treat exact commit `0b7f930...` as having passed the independent freeze gate.** Do not mutate v7 in place.
2. **Create one separate v7 execution task.** It should adapt the existing isolated launcher prospectively and run the frozen 32 rows only after confirming the audited commit remains in `origin/main`, all hashes still match, both canaries pass, provider-included cost remains USD 0.00, and attempts are still zero.
3. **Use one attempt, no feedback, and no retry per frozen row.** Retain every attempted, invalid, skipped, service-failed, and environment-failed denominator rather than repairing or rerunning.
4. **Preserve claim ceilings.** Even a complete matrix can initially support only bounded internal treatment observations under these synthetic rules. All seven current claims remain false until distinct evidence and validity arguments license any upgrade.
5. **Stop on drift or service/cost failure.** Do not convert this freeze PASS into permission to bypass later execution-validity gates.

One non-duplicate build task is implied: execute the exact v7 matrix under the frozen envelope. No schema or consolidation task is needed; the main result is an exercised lifecycle gate, not a new subsystem.
