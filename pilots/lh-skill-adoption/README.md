# Pilot: advise on adopting skill-grounded scoring

**Status:** non-releasable internal calibration pilot; the evidence-link and two private claim-boundary checks are executable, but no domain expert has approved the procedures, task, or rubric.

## Scenario

Act as a benchmark program analyst advising a program lead whether to adopt skill-grounded scoring now, reject it, or run a controlled pilot. Produce a spreadsheet-compatible evidence matrix and decision memo from the supplied evidence pack. The critical incident is that the evidence contains both attractive aggregate agreement results and weak individual human/automated concordance, plus a promising but seven-run execution ablation.

This scenario tests evidence reconciliation and decision calibration, not recall of LH-Bench. The task must be answerable from supplied files with network denied.

## Files

- `source-pack/decision-evidence.csv`: row-level decision evidence derived from the deep local LH-Bench review.
- `source-pack/manifest.json`: source authority, visibility, locators, and derivation.
- `public-skill.md`: public workflow principles and artifact interface.
- `candidate-procedures.json`: two plural candidate routes, explicitly pending expert approval.
- `rubric-skeleton.json`: public requirements and private held-out consequences.
- `expertise-transfer.json`: authoring/evidence graph fixture.
- `benchmark-bundle.json`: executable-contract task skeleton with zero fabricated trials.
- `evidence-chain-audit.json`: hash- and pointer-bound cross-record ECBD audit with explicit unsupported links and suite limits.
- `validation-plan.md`: evidence required to move beyond schema validity.

## Cross-record evidence-chain audit

Run the fail-closed composition check with:

```bash
python scripts/audit_evidence_chain.py --check-paths \
  pilots/lh-skill-adoption/evidence-chain-audit.json
```

The audit connects existing expertise-transfer, benchmark-bundle, execution,
metric, and validity records rather than defining another ECBD schema. Each
adjacent intended-use → construct/criterion → item requirement → response view
→ check → metric → validity-claim edge retains a warrant, support state,
evidence/counterevidence locators, scope, and claim consequence. The checker
recomputes artifact hashes, resolves every JSON Pointer, requires the complete
ordered chain, and rejects claim upgrades across non-supported edges or explicit
blockers.

This first application finds substantive gaps rather than certifying the pilot:
the artifact paths are predeclared but their professional and workflow evidence
sufficiency is unreviewed; the authoritative human check remains interface-only;
the executable 8/8 metric is synthetic grader-regression evidence rather than a
professional criterion; the matched no-skill arm is absent after provider
failure; and one convenience task supplies no suite assembly, precision, or
cross-domain evidence. Expert validity, matched Skill effect, suite validity,
cross-domain generalization, and release readiness therefore remain false. The
audit itself is builder-authored checker calibration, not evidence that ECBD
improves benchmark quality.

## Executable evidence-link slice

Run the deterministic public check against an output pair:

```bash
python scripts/grade_lh_evidence.py \
  --matrix outputs/evidence-matrix.csv \
  --memo outputs/recommendation.md
```

The grader emits `check-result-v0.1`. It checks six deliberately inspectable properties: required columns, evidence-ID resolution, exact source authority, exact source scope, exact caveat preservation, and numeric memo citation linkage. Calibration fixtures live under `calibration/`: one cautious pass plus agreement-overclaim, tiny-ablation-overclaim, and malformed-source failures.

This is intentionally **not** an entailment grader or a substitute for professional judgment. Exact string preservation makes a bounded provenance failure surface executable; contradiction reconciliation, causal appropriateness, decision quality, and alternative valid phrasings remain human-calibrated. The distinction follows the consulting review's separation of source existence, support, authority, scope, and freshness rather than pretending one citation check establishes them all.

The private internal calibrator can also be exercised with:

```bash
python scripts/grade_lh_claims.py \
  --matrix outputs/evidence-matrix.csv \
  --memo outputs/recommendation.md
```

It emits separate `contradiction-reconciliation` and `causal-claim-strength` check results. Its independently versioned rubric was derived afresh from the pinned evidence groups and review claims, but this is **not blinded independent human authorship**: the builder had repository access to the shared rubric. Evidence-group membership and regex boundaries correctly classify the planted cases; they do not establish entailment, accept alternative professional reasoning, or advance the failed expert/release gates.

## Matched-condition task-only preflight

Run the reproducible packaging preflight with:

```bash
python scripts/run_lh_ablation_preflight.py
```

This materializes the same cautious builder-authored fixture under all four no-skill/public-skill × independent/shared-rubric conditions, pins task, skill, rubric, tool, harness, and feedback-policy hashes, and executes only graders valid for each rubric boundary. The report is `ablation/preflight-report.json`, validated by `schemas/ablation-preflight.schema.json`. Independent-rubric conditions execute the provenance and internal claim calibrators; shared-rubric conditions execute only the rubric-independent provenance layer and explicitly leave human claim checks unexecuted.

This is a **plumbing preflight, not an agent trial**. All four conditions replay identical authored artifacts, `capability_evidence` is fixed to `false`, and no condition effect may be inferred. Its reusable contribution is a hash-pinned, machine-validated 2×2 run manifest that a later agent harness can populate with genuine matched outputs without confusing fixtures with capability evidence.

## Retained invalid agent attempts

Two sequential no-skill/public-skill model executions and one unattributable
concurrent launch are retained under
`ablation/agent-attempts-20260710/`. Run:

```bash
python scripts/audit_lh_agent_attempts.py
```

The attempts are **not valid trials**. Hermes v0.18.2 was launched from
temporary trial directories with only file tools, but its trace records
`/home/sam/skill-bench` as the effective cwd. Repository-wide searches exposed
private grader/calibration filenames and treatment-adjacent documentation; the
no-skill trace was even shown the pilot README's `public-skill.md` inventory and
professional-trap descriptions. Artifacts also resolved to the shared
`/home/sam/outputs` directory. A first concurrent pair therefore collided, and
the later sequential artifacts required post-hoc relocation.

The audit preserves redacted session traces, usage, exact matched prompts,
outputs, hashes, and grader results while fixing `capability_evidence=false`.
Both sequential outputs pass the unvalidated internal claim-boundary calibrator
and fail the deterministic evidence-link convention; these are useful grader
diagnostics, not a treatment comparison. A future launcher must pass a zero-cost
cwd/input/output canary before another model run and must make repository files
unreachable, not merely instruct the agent to ignore them.

## Difficulty knobs

| Knob | Easier | Harder | Construct guarded |
|---|---|---|---|
| Caveat salience | caveat in same row | caveat only in reviewed source locator | evidence retrieval vs reconciliation |
| Contradiction distance | adjacent agreement/validity rows | separate files/sections | context tracking |
| Distractor quality | explicit “directional” labels | polished adoption summary using E01/E08 only | overclaim resistance |
| Source count | one reviewed source | independent expert notes and production evidence | authority selection |
| Decision stakes | internal pilot | public procurement/release | threshold judgment |
| Missingness | all scopes supplied | unequal run counts/exclusions require qualification | missing-data reasoning |

Do not increase difficulty by hiding a new obligation. Every variant must preserve the public basis and update provenance.

## Professional traps

1. **Agreement-is-validity:** cite κ=0.60 and variance=0.10 as proof that automated scores reflect professional quality, omitting κ=0.06/0.08 and the one-expert threshold evidence.
2. **Tiny-ablation causality:** cite the +0.87 Codex delta or 2/7 no-skill deployments as a stable causal effect while omitting the seven-run scope and harness/integration confounds.

Both are evidence-backed failure signatures from the reviewed source, not arbitrary tricks. The deterministic grader's provenance convention is public; human check boundaries for contradiction and causal judgment remain private held-out consequences of disclosed principles.

## Provenance boundary

The review and underlying immutable PDF/text were actually read by the research worker recorded in the queue. This build consumes that reviewed artifact; it does not claim a new paper review. Spreadsheet columns, memo format, candidate route details, weights, and adoption-threshold wording are **unvalidated design hypotheses** introduced by the benchmark builder. They are release-gated accordingly.
