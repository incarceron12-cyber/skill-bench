# Released procedure-package cross-instrument validation

## Scope and decision filter

This validation advances charter objectives **B** (expertise-to-evaluation methodology) and **C** (executable infrastructure). It tests whether the builder-authored procedure-package v0.1 contract can consume two intact, mechanically selected released instruments with different generators and work structures. It is validation—not an SOP, aviation, procurement, or ERP scope commitment.

Useful completion means immutable source bytes and roles are mapped without filling release gaps from review prose, the unchanged v0.1 validator is replayed first, failures are classified, and outcomes fail closed. No expert approval, professional correctness, agent capability, safety, production-fitness, or deployment-readiness claim is made.

## Frozen selection and provenance

`selection-freeze.json` was written before adaptation/replay. Its bytewise rule selected exactly:

- **SOP-Bench:** GitHub commit `2fdce4c57e6b02b725d5437ec079c142cffd8e07`, `aircraft_inspection`, first physical CSV row `a_00127`; CC-BY-NC-4.0. The release is more than three months after immutable arXiv v2 and is not treated as paper-time byte identity.
- **Anchor ERP-Bench:** commit `ceba3880af555129b5278e056a0c20f2fb5a0ba9`, task `2000_easy_01_buy_only_baseline`; CC0-1.0. The release is one day after immutable arXiv v1 and is not assumed manuscript-time byte identity.

Selected package files were copied byte-for-byte from the pinned ZIPs under `source/`. The adapters record each file hash; the adapter validator verifies both ZIP and extracted-file hashes. Licenses are preserved beside each extracted package.

## Unchanged v0.1 replay

The existing `scripts/validate_procedure_package.py` was run unchanged against both adapters before adapter-specific validation. Raw reports are preserved as:

- `reports/raw-v0.1-sop-bench.txt`
- `reports/raw-v0.1-anchor.txt`

Both were structurally rejected because v0.1 is not actually format-agnostic at its outer boundary: it requires the builder calibration shape (`table_contract`, finite `tools`, independent `oracle`, at least five specially named planted trials, and multiple accepted paths). This is classified as **non-applicability**, not as a source-package failure and not “fixed” by inventing released traces. The original validator was left unchanged because weakening those calibration invariants would hide absent evidence rather than demonstrate a valid cross-instrument abstraction.

## Role and observation results

| Instrument | Public input | Hidden evidence | Tool result | Scored endpoint | Audit metadata | Prohibited oracle |
|---|---|---|---|---|---|---|
| SOP-Bench Aircraft Inspection | observed: metadata input columns + first row | unavailable as a separately typed role | observed in `tools.py` | observed in metadata output columns | unavailable item-level | observed: expected CSV outputs, also returned by tools |
| Anchor task 2000 | observed: `instruction.md` | observed: scenario projected into Odoo | unavailable without running Odoo/trajectory | observed in terminal-state checker | observed in `task.toml` | observed: plan, solver, checker |

Unavailable runtime, endpoint, final-artifact, procedure-event, or accepted-alternative evidence remains explicitly unavailable. SOP-Bench's released `tools.py` could not be executed in the repository verification environment because its undeclared-at-project-level runtime dependency `pandas` is absent; no local shim or expected CSV value was substituted. Anchor's Odoo environment was not built: doing so would exceed this bounded static adapter slice and still would not supply a released agent terminal-state snapshot or trace.

## Findings and outcomes

### SOP-Bench Aircraft Inspection — **REJECT**

- **Source-package defect:** all seven tools return scored endpoint columns directly.
- **Source-package defect:** multi-argument tools validate argument presence but select rows using only `aircraft_id`; other required arguments do not affect lookup.
- **Mapping insufficiency:** no separate hidden-evidence or item-level audit role.
- **Non-applicability/evidence gap:** no released selected final artifact or clause-covered procedure trace.

### Anchor task 2000 — **REJECT**

- **Source-package defect for operational use:** the intact public package co-distributes prohibited oracle artifacts (`optimal_plan.json`, solver, and checker) without an encoded scored-run access boundary.
- **Mapping insufficiency:** no selected released runtime, terminal-state, or trajectory observation.
- **Non-applicability:** v0.1 assumes tabular rows, finite mock tools, and planted trace cases, whereas Anchor exposes a stateful ERP and terminal-state verifier.

The adapter format itself validates in both cases. `reports/*.adapter.report.json` preserves machine-readable classifications. “Reject” means the intact released package cannot receive a procedure-conformance pass under the current evidence and access contract; it is not a claim that the benchmark, task, procedure, or oracle is professionally wrong.

## Executable artifacts

- `scripts/validate_released_procedure_adapters.py`: verifies frozen selection, archive and file hashes, exact role coverage, typed observation availability, finding classes, fail-closed outcomes, and claim ceilings.
- `tests/test_released_procedure_adapters.py`: six tests cover both outcomes, unavailable dependency honesty, hash mutation, missing role mapping, claim promotion, and outcome promotion.
- The original v0.1 schema/validator was not changed.

Run:

```bash
python scripts/validate_released_procedure_adapters.py \
  --report-dir pilots/procedure-package-released-validation/reports \
  pilots/procedure-package-released-validation/sop-bench-aircraft-inspection.adapter.json \
  pilots/procedure-package-released-validation/anchor-2000.adapter.json
python -m unittest tests.test_released_procedure_adapters -v
```

## Design implication

The validation falsifies the broad “format-agnostic adapter” description at v0.1's outer boundary while preserving the useful internal calibration checks. A future general contract should separate (1) package inventory/role/access conformance, (2) environment adapter and deterministic replay, and (3) observed trial procedure/endpoint conformance. It must support typed `unavailable`/`partial` evidence and stateful terminal-state environments without relaxing answer-bearing oracle, final-artifact, or claim-ceiling safeguards. This report does not queue that larger redesign: the present slice provides the concrete failure evidence needed to scope it without guessing.
