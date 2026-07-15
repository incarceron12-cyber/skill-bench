# Evidence-acquisition episode contract v0.1

`evidence-acquisition-episode.schema.json` and
`scripts/validate_evidence_acquisition.py` implement a compact, cross-domain
record for knowledge work in which decision-relevant evidence is latent and must
be requested or supplied under a controlled condition.

```text
latent evidence atom
  → request intent
    → parser interpretation
      → access transition
        → adoption / rejection / ignored evidence
          → stopping decision
            → terminal action or artifact consequence
```

The general hypothesis is that inquiry selection can be distinguished from
interpretation only when parser behavior, access, costs, delay, risk, feedback,
stopping, and endpoint consequence are separate observations. This is building
and validation under charter objectives B and C. It reuses task, check, grader,
task-health, metric, and validity identifiers rather than introducing parallel
versions of those operating-layer objects.

## Enforced boundaries

1. **Latent state is typed.** Every evidence atom records source/locator,
   authority and validity time, availability, decision value, cost, delay, risk,
   redundancy, dependencies, contradictions, and frozen synthetic-minimal-set
   membership.
2. **Intent is not parser output.** Raw request, candidate intent and requested
   scope remain distinct from parser identity, mapping, confidence and evidence
   locator. `matched`, `ambiguous`, `unmatched`, and `parser_error` are parser
   states—not release states.
3. **Parsing is not access.** Access separately records `released`, `delayed`,
   `denied`, `ambiguous`, or `failed`, with request/evidence identity, observer,
   transformation, reason, and content locator only when content was released.
4. **Access is not adoption.** Adoption must point to the same released atom and
   include trace evidence of uptake plus a belief and action/artifact change.
   Endpoint quality alone cannot be used to infer uptake.
5. **Stopping is inspectable.** The stop record binds acquired basis,
   considered-but-unacquired atoms, remaining budget, declared loss rule,
   uncertainty, and terminal choice. Active inquiry cannot claim a supplied-set
   stop, and substantive sufficiency/value stops require both acquired and
   unacquired evidence ledgers.
6. **Feedback fails closed.** Evaluator and grader outputs may appear only after
   terminal action. Preterminal environment feedback is allowlisted separately
   as access status, evidence content, or budget state.
7. **Matched conditions preserve identity.** Each scenario has one `active`, one
   `full_information`, and one `expert_minimal` episode against the same frozen
   target and evidence graph. Full information supplies every admissible/delayed
   atom; the synthetic minimal condition supplies exactly marked atoms.
8. **Endpoint consequence remains plural.** The terminal record keeps the action
   or artifact, direct observation locators, decision loss, severe omissions,
   resource cost, and a narrow synthetic claim scope. It does not collapse these
   into request utilization.
9. **Provenance and claim limits are mandatory.** `--check-paths` verifies design
   evidence and reused contract bytes. Internal fixtures cannot license agent or
   professional capability, clinical/compliance validity, causal inquiry
   benefit, safety, production fitness, readiness, representativeness, or
   cross-domain generality.

## Conformance fixtures

`tests/fixtures/valid-evidence-acquisition-episodes.json` contains six zero-call,
builder-authored episodes across two unlike shapes:

- a document-based compliance disposition; and
- a data-analysis decision with delayed metadata.

Each shape has active, full-information, and frozen synthetic-minimal conditions.
Together they exercise release, delay, denial, and ambiguity while preserving
request → parser → access → adoption → stop → consequence links. “Expert minimal”
is only the condition name inherited from the proposed experimental contrast;
no expert selected or approved these atoms.

`tests/fixtures/invalid-evidence-acquisition-mutations.json` prospectively names
four planted failures and exact mutation paths: parser/release conflation,
preterminal evaluator feedback, a supplied-condition stop in active inquiry, and
endpoint-only adoption. Tests replay every mutation against the positive fixture
and require rejection for the declared reason. Additional mutations check
missing released content, incomplete full-information supply, cross-atom uptake,
and provenance drift.

This demonstrates exact validator behavior on synthetic records. It does not
show that the fields are sufficient for real compliance, analysis, clinical, or
other professional inquiry; that requires independent domain authoring, real
trials, matched repetitions, metric specifications, and bounded validity
arguments.

## Design provenance

| Contract choice | Primary evidence and limitation |
|---|---|
| Separate intent, parser interpretation, release and adoption | `papers/agent-benchmarks/2026-07-15-oncorounds-information-seeking-validity.md`, “Parser as an intervention” and “Unique insight.” The reviewed parser has no reported validation set, so it motivates separation rather than validating this schema. |
| Value/cost/delay/risk and stopping ledger | Same review, “Three rounds and active requests,” “Unique insight,” and “Repair” items 11–14. OncoRounds uses free requests and therefore does not empirically calibrate these fields. |
| Active/full/minimal matched conditions | Same review, matched-interventions table and cross-domain pilot design. The paper did not run these contrasts; they are a project design proposal. |
| Feedback firewall | Same review, “The evaluator feedback leak” and Repair item 9. Release inspection shows judge labels entered later-round candidate context; it does not estimate the feedback effect. |
| Endpoint consequence rather than utilization objective | Same review, “Unique insight” and Transfer items 14–15. Clinical outcome and safety validity are absent. |
| Reused operating identifiers | Charter configured-system, evidence-traceability and plural-measurement principles; executable homes are `benchmark-bundle`, `task-health`, `metric-monitoring`, and `validity-argument` schemas. |

## Validate

```bash
python scripts/validate_evidence_acquisition.py --check-paths \
  tests/fixtures/valid-evidence-acquisition-episodes.json
python -m unittest tests.test_validate_evidence_acquisition -v
```
