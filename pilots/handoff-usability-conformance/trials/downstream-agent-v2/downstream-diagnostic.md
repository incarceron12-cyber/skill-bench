# Corrected-path downstream-operation diagnostic

## Frozen comparison

Version 2 changed only the public task's handoff locator from the invalid
`inputs/handoff.json` to the mounted `handoff.json`. It reused the exact two
producer handoffs from `isolated-agent-v3`, operation contracts, deterministic
checks, `gpt-5.6-sol` / `openai-codex`, file-only safe-mode envelope, 900-second
timeout, one attempt, and zero retries. Version 1 remains immutable.

## Observed evidence

Both outer-envelope canaries passed. Producer and consumer SHA-256 values match
for both handoffs, excluded producer/repository probes remained denied, input
inventories were unchanged, both processes returned zero, and both required
operation artifacts and usage records were written. Thus the interface repair
moved both cases from version 1's `not_scored` abstention to substantive grading.

The procurement artifact passed handoff lineage, approval decision, and
observable-action checks, but failed `risk_preserved`: it used an immediate
calendar-control formulation rather than retaining the grader's predeclared
observable `30-day` notice token. The operations artifact passed lineage,
blocking, and failover-confirmation checks, but failed `destination_owner`: it
placed `database on-call` in `requested_confirmation` while retaining `primary
on-call` in the separate `owner` field. Both overall outcomes are `fail` under
the frozen all-checks policy. Replaying the deterministic grader reproduces both
reports.

## Bounded interpretation

Relative to version 1, the corrected public path enabled valid downstream
operation evidence and localized two contract/grader alignment failures rather
than handoff-access failures. This two-case, one-attempt builder-authored slice
does **not** establish human-recipient usability, expert validity, professional
capability, cross-domain generalization, treatment effect, productivity,
downstream impact, or readiness.
