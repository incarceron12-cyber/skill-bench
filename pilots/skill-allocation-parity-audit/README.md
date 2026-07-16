# Skill allocation and resource-parity audit v1

This zero-call diagnostic instantiates the allocation record derived in
`papers/agent-benchmarks/2026-07-16-online-skill-memory-budget-value.md` over two
retained, prospective no-Skill/public-Skill studies. It advances charter
objectives B and C by testing whether existing intervention evidence can support
a resource-allocation contrast without changing either parent package.

## Frozen evidence and rationale

`manifest.json` binds all 14 intended attempts, both parent protocols/reports,
and every retained trial report, usage record, and available grade by path,
byte count, SHA-256, and Git blob identity. The replay verifies those identities,
the frozen schedule, condition, execution order, and configured-system hash.
Every intended attempt remains in the ledger, including four service-invalid
cross-pilot cells; there is no complete-case replacement.

The manifest predeclares exact task/configuration/order/state matching and token,
call, and component-allocation parity tolerances. Aggregate provider usage is
retained but is never allocated to direct acting, Skill delivery/injection,
generation, verification, retrieval, or repair. Public-guide presence records
only presentation, not invocation or adoption. Missing state hashes, per-call
phase labels, tool-call counts, and wall time are represented as
`unavailable`, not estimated.

The retained result is therefore useful negative diagnostic evidence: all 14
allocation rows replay, but **zero exact matched allocation contrasts are
admissible**. The exact prospective capture fields are listed in
`audit-report.json`. This does not erase the parent studies' descriptive rubric
results; it shows that they cannot identify resource-allocation value.

## Replay

```bash
python scripts/audit_skill_allocation_parity.py \
  pilots/skill-allocation-parity-audit/v1/manifest.json \
  --output pilots/skill-allocation-parity-audit/v1/audit-report.json
python -m unittest tests.test_skill_allocation_parity_audit -v
```

`--freeze-manifest` is an explicit authoring operation and is not part of normal
validation. The report makes no Skill-effect, memory-value, capability,
professional-validity, cross-domain, safety, production, or readiness claim.
