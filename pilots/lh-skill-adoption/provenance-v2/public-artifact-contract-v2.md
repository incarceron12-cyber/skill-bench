# Public artifact contract: evidence provenance v2.1.0

**Status:** prospective internal calibration contract; it does not alter or rescore any historical trial.

For every sourced material number, use an exact square-bracket citation on the same memo line: `[E01]` or `[E01, E02]`. Parenthetical citations such as `(E01)`, citation ranges such as `[E01-E03]`, and bare IDs are **not accepted**. Every cited ID must also appear in the evidence matrix. Matrix rows must preserve the source row's `authority`, `scope`, and `caveat` exactly.

A number chosen by the analyst for the proposed program—rather than reported by a source—must be wrapped exactly as `{{PROSPECTIVE:<text containing the number>}}`, for example `{{PROSPECTIVE:minimum 30 paired runs}}` or `{{PROSPECTIVE:review date 2026-09-01}}`. The provenance-value check abstains only for numbers inside that marker. A mixed line may say: `The source reports 7 runs [E07]; require {{PROSPECTIVE:30 paired runs}}.` The citation still supports only the sourced value.

Do not use the marker for source-reported measurements, source scope, evidence IDs, citations, or claims about past/current facts. Empty, nonnumeric, nested, or malformed markers fail. The deterministic grader can verify syntax, source-row fidelity, numeric linkage, and matrix crosswalks; it cannot determine whether a marker is semantically honest, whether cited text is entailed, or whether the recommendation is professionally sound. Those limits require independent review.

Numeric linkage preserves explicit relations. Symbolic and natural-language equivalents are canonicalized (`>=4`/`at least 4`, `>4`/`more than 4`, `<=4`/`at most 4`, and `<4`/`less than 4`); `%` and `percent` are equivalent; and explicit ranges are compared as ranges. A bare `4` is **not** accepted for a sourced `>=4`, because dropping the comparator changes the claim. This lexical rule does not infer semantic equivalence beyond the listed forms.

Design provenance: `pilots/lh-skill-adoption/ablation/provenance-failure-diagnosis.md`, especially the observed hidden syntax and prospective-value boundary. This contract is reusable provenance machinery instantiated in LH; it is not evidence that this domain or contract is professionally valid.
