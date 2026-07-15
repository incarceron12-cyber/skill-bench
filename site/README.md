# Skill Bench Research Observatory

Astro + Starlight presentation layer for the canonical `skill-bench` repository.

The website is deliberately **read-only and deterministic**. Research remains canonical in the repository root; `scripts/build_site_content.py` creates a sanitized site projection at build time.

## What it presents

- project charter and anti-drift boundaries;
- grouped research insights and relevance tiers;
- benchmark-family landscape and methodology;
- every evidence-backed paper review;
- thematic paper navigation plus a visible unclassified-review backlog;
- current queue priorities and blockers;
- the compounding-system and improvement ledger.

## Local development

From `site/`:

```bash
npm install
npm run dev
```

Open <http://localhost:4321>.

The `dev` and `build` commands run the content projection first, so changes to canonical Markdown or `data/work_queue.json` appear without copying content manually.

## Validation and production build

```bash
npm run check
npm run build
```

The static output is written to `site/dist/`. Pagefind search is built automatically.

The current build pipeline validates Astro types and content before generating static pages. Repository-level verification should also run:

```bash
python -m py_compile scripts/*.py
python scripts/check_review_quality.py papers --allow-empty
python scripts/queue.py validate
```

## Content architecture

| Website area | Canonical source |
|---|---|
| Dashboard | Generated summary of canonical sources |
| Charter | `PROJECT_CHARTER.md` |
| Key insights | `docs/research-synthesis-index.md` |
| Benchmark landscape | `docs/state-of-the-art-map.md` |
| Research program | `docs/benchmark-landscape-research-program.md` |
| Methodology | `docs/benchmark-design-taxonomy.md` |
| Papers | `papers/topic-index.md` and `papers/agent-benchmarks/*.md` |
| Next steps | `data/work_queue.json` |
| Operations | `docs/compounding-system.md` and `docs/self-improvement-ledger.md` |

Generated Markdown under `site/src/content/docs/` is ignored by Git. Do not edit it directly; edit the canonical source and rebuild.

## Reverse-proxy deployment

The recommended production pattern is a static release directory behind Caddy:

```text
Git checkout → npm ci → npm run build → validated release directory → Caddy HTTPS
```

An example is provided in [`Caddyfile.example`](Caddyfile.example). A release can be installed atomically:

```bash
release="/srv/skill-bench-site/releases/$(date -u +%Y%m%dT%H%M%SZ)"
sudo mkdir -p "$release"
sudo cp -a dist/. "$release/"
sudo ln -sfn "$release" /srv/skill-bench-site/current
sudo systemctl reload caddy
```

Do not use `astro preview` as the production server. Caddy should serve the static `dist` output directly.

Before making the site public, decide:

1. hostname/domain;
2. public versus private access;
3. VPS/server or managed static hosting;
4. whether Cloudflare Access or Tailscale is required;
5. which repository fields are safe to publish.

The projection intentionally excludes credentials and local paper/source archives. Review queue rationales and next actions before publishing them on a public hostname.

## Continuous private builds

`.github/workflows/site.yml` performs a clean projection, validates canonical sources, runs Astro checks, builds the static site, and uploads a private workflow artifact whenever relevant content reaches `main`.

The repository remains private. The workflow deliberately does **not** attempt GitHub Pages deployment because this account plan does not support Pages from this private repository.

Private hosting options are:

1. **Cloudflare Pages + Access:** managed builds from the private GitHub repository, protected by an identity policy. Best balance of convenience and private browser access.
2. **Caddy + Cloudflare Tunnel/Access:** build on a private server, serve `dist/` with Caddy, and expose it without opening an inbound port.
3. **Tailscale Serve:** serve the static site only inside the tailnet. Simplest and strongest option when access is limited to Samuel's own devices.
4. **Private VPS + Caddy authentication:** conventional reverse-proxy hosting with explicit identity or VPN controls; more operational work.
5. **GitHub Enterprise Cloud private Pages:** native repository-reader access control, but substantially more expensive than the other options.

All options reflect the latest **successfully built/published commit**, not uncommitted local worker state. The Astro configuration accepts `SITE_URL` and `SITE_BASE` so a chosen host can set its final URL without changing canonical research content.
