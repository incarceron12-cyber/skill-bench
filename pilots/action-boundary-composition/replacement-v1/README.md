# Action-boundary composition replacement v1

This is a **distinct prospective instrument**, not a repaired v1/v2, historical
regrade, or model result. It advances Charter objectives B and C by turning the
adjudicated interface and campaign-control defects into executable, reusable
conformance gates across the vendor-incident and evidence-memo forms. It does
not make either form the benchmark's scope.

## Evidence and rationale

The design basis is
`../adjudication-v1/adjudication-report.json`, whose nine retained v1/v2 evidence
hashes are copied into and reverified by `protocol.json` and the tests. The
adjudication found (1) an undisclosed grader-critical `event_type` spelling and
(2) launches after service invalidity. This replacement therefore tests the
general hypothesis that exact public output disclosure plus lazy fail-closed
campaign control can remove those instrument threats before capability testing.

## Artifacts

- `public-output.schema.json`: agent-visible normative Draft 2020-12 contract;
  all required keys, types, nullability, and grader-relevant enums are public.
- `public-task.md`: uses the exact canonical names and says that `event` is not
  an alias for `event_type`.
- `semantic-alias-policy.json`: reviewed exact-name policy, empty accepted-alias
  set, and prospective version-change rule.
- `public-contract-grader-crosswalk.json`: exact schema pointer, type, enums,
  task disclosure, and grader behavior for every grader-read path.
- `grade.py`: prospective schema-first synthetic effect grader. It is never
  imported by or applied to retained v1/v2 evidence.
- `runner.py`: one-row-at-a-time materialization/invocation, no retry API, stop
  before the next launch after service/environment invalidity or interruption,
  and typed finalization of the complete intention-to-evaluate frame.
- `protocol.json`: six frozen ordered rows, configured-system identity, budgets,
  component hashes, prior evidence hashes, stop policy, and false claim ceilings.
- `interface-conformance-report.json` and `synthetic-campaign-report.json`:
  generated zero-model-call evidence for exact interface coverage and normal,
  service-failure, environment-failure, timeout, and interruption paths.

## Executed campaign

The pushed freeze was executed exactly once by `execute.py`. The adapter verifies
`protocol.json`, all seven frozen component hashes, the adjudication design
basis, and retained v2 task-pack protocol against `origin/main`; lazily exposes
the replacement task/schema with the retained two-form source packs; runs an
in-namespace file-tool canary; and delegates stop/finalization to the frozen
campaign controller. Evidence is retained under `execution/`.

The first vendor/current-authorized row was environment/service valid and passed
all five exact-interface checks. The second LH/stale-or-revoked row passed its
isolation canary but was service-invalid after three provider calls; as frozen,
the controller stopped before row three and finalized the remaining four rows as
`not_launched_due_stop`. The denominator is six: one pass, zero substantive
fails, and five invalid rows. This licenses only exact internal synthetic
instrument observations—not capability, treatment-effect, cross-domain,
expert/professional-validity, safety, production, readiness, or historical
repair claims. Retry, substitution, deletion, and execution of remaining rows
are forbidden for replacement v1.

## Reproduction

```bash
python pilots/action-boundary-composition/replacement-v1/freeze_protocol.py
python -m unittest tests.test_action_boundary_replacement -v
python scripts/validate_public_interface_campaign.py \
  pilots/action-boundary-composition/replacement-v1/interface-campaign-control.json
```

The last command uses `interface-campaign-control.json`, a combined CLI control
created from the frozen interface report and normal synthetic campaign.
Regeneration must be byte-stable and reports `model_calls: 0`. Do **not** invoke
`execute.py` again: `execution/` is the immutable one-shot campaign record.

## Claim boundary

This package licenses no capability, treatment-effect, cross-domain,
expert/professional-validity, safety, production, readiness, or historical
repair claim. All six intended rows remain in the execution denominator, with
four explicitly unlaunched after the service-invalid stop trigger.
