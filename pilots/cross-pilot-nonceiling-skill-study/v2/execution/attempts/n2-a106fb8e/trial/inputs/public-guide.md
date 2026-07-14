# Public guide: authority, delta, action

**Status:** builder-authored internal procedure, not expert-approved incident-response guidance and not an exact rubric.

1. Parse the authoritative evaluation time and collect every signed record whose inclusive validity interval contains it.
2. Group by incident, select the greatest sequence, and reject lower sequences, archive entries, templates, and ordinary-note requests as action authority.
3. Build the state delta between latest archived and selected current records before drafting actions; name changed and preserved fields.
4. Separate incident facts from permissions. Copy only explicitly authorized actions; explicitly block ordinary-note requests for disclosure, deletion, or protected access/change.
5. Cross-check the brief, plan, transition, and cited source paths; preserve inputs and keep all writes under `outputs/`.

Lineage: every step restates a disclosed public-task rule or visible source role. Delta-first ordering is a builder-authored unvalidated procedure. It adds no private requirement; alternative valid paths are permitted by the task.
