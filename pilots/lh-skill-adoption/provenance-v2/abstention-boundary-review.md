# Independent builder-authored abstention-boundary review

**Reviewer independence:** a separate builder-authored review artifact, not an expert review, blinded adjudication, or evidence of professional validity. The review tests the frozen corpus against the public v2 contract.

## Boundary findings

- Valid abstentions are narrow: prospective date, threshold/sample size, and the prospective portion of a mixed sourced/prospective line. Citation, source-row fidelity, matrix crosswalk, and unmarked sourced-number checks remain active.
- Parentheses and ranges intentionally fail rather than being silently broadened. This makes the public parser boundary exact and prospective.
- Unsupported, uncited, and wrong-row numbers fail in the planted corpus.
- **Planted over-broad abstention:** `Agreement was {{PROSPECTIVE:0.60}}.` passes the lexical grader even though 0.60 is source-reported. The corpus records `semantic_marker_misuse_not_machine_detected`. Therefore marker honesty requires an independent semantic check; it must not be represented as machine-verified provenance.
- The grader also cannot establish entailment, causal appropriateness, alternative valid attribution, or professional decision quality.

Decision: accept v2 only as a lexical conformance instrument with the unresolved semantic-marker limitation explicit. Do not use its pass as Skill-effect, capability, expert-validity, or release-readiness evidence. A future trial would require a separately specified semantic review; no new agent call is part of this build.
