# Papers

This directory contains the evidence-backed review corpus for `skill-bench`.

## Start here

- **[`topic-index.md`](topic-index.md):** thematic organization of every deep review.
- **[`../docs/research-synthesis-index.md`](../docs/research-synthesis-index.md):** grouped cross-paper insights and relevance tiers.
- **[`../docs/benchmark-landscape-research-program.md`](../docs/benchmark-landscape-research-program.md):** program for comparing established benchmark families with newer attempts to improve them.
- **[`../docs/state-of-the-art-map.md`](../docs/state-of-the-art-map.md):** compact external benchmark-family comparison.
- **[`../data/papers/index.json`](../data/papers/index.json):** machine-readable acquisition, extraction, provenance, and review status.

Reviews currently remain under [`agent-benchmarks/`](agent-benchmarks/) to preserve stable links. The topic index supplies organization without forcing papers that span several themes into misleading mutually exclusive folders.

## Review philosophy

A useful review is not an abstract summary. It should answer:

1. What is the paper's unique insight?
2. What exactly did the authors build or measure?
3. What methodology can transfer into `skill-bench`?
4. What strengths should be preserved?
5. What limitations, validity threats, or failure modes should be improved?
6. Which newer benchmark designs attempt to address those limitations, and is there evidence they succeed?
7. What new question should Samuel think about?
8. What concrete repository or benchmark change follows?

Never call a review deep unless the full paper or equivalent primary source was actually acquired and read. Preserve paper-time versus post-paper release boundaries and record source paths, hashes, and limitations.

## Organization policy

- Use one primary collection and multiple secondary tags in `topic-index.md`.
- Keep triage-only discoveries in scouting reports or the machine index.
- Add a deep review only when it contributes a distinct method, contradiction, limitation, or design implication.
- Update grouped synthesis only when the source changes a conclusion or relevance tier.
- Do not move existing review files casually; many schemas, reports, provenance records, and canonical documents link to them.
