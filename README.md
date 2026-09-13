# ClassSync website

Static marketing + documentation site for ClassSync. It intentionally uses plain HTML/CSS/JS so it can be hosted for free on GitHub Pages, Cloudflare Pages or any static host without a build step.

Primary URL: `https://classsync.hugoalmeida.tech/`

Fallback GitHub Pages URL: `https://hugo2006alm.github.io/classsync-site/`

## Structure

- `index.html` — product homepage
- `docs/index.html` — documentation hub
- `docs/setup/index.html` — first-run setup and credential guide
- `docs/self-host/index.html` — Cloudflare Worker + D1 relay setup
- `assets/styles.css` — design system matching the Flutter app
- `assets/screenshots/README.md` — exact screenshot capture list
- `CNAME` — GitHub Pages custom domain (`classsync.hugoalmeida.tech`)
- `.nojekyll` — publish the static files directly without a Jekyll build
- `.github/workflows/pages.yml` — optional GitHub Actions deployment path

## Design

The site mirrors the Flutter theme:

- Fraunces headings
- Manrope body text
- paper `#F6F1E7`
- teal `#24534F`
- coral `#C85E42`
- large rounded cards and controls
- matching dark mode through `prefers-color-scheme`

Fonts are loaded from Google Fonts; no font binaries are committed.

## Local preview

Any static server works, for example:

```bash
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Custom domain

GitHub Pages is configured to serve the site at `classsync.hugoalmeida.tech` through the repository `CNAME` file. DNS should expose a `CNAME` record named `classsync` pointing to `hugo2006alm.github.io`.

The site keeps its internal links relative, so changing the custom domain later does not require rewriting navigation or documentation links.

## GitHub Pages without Actions

When Actions minutes are unavailable, use branch deployment. In the repository, open **Settings → Pages** and set:

- **Source:** `Deploy from a branch`
- **Branch:** `main`
- **Folder:** `/ (root)`

Then save. The repository contains `.nojekyll`, so the HTML/CSS/JS files can be served directly without a Jekyll build or custom Actions execution.

## GitHub Pages with Actions

The repository also keeps `.github/workflows/pages.yml`. When you want to use the workflow again, switch **Settings → Pages → Source** back to **GitHub Actions**. The workflow deploys the repository root on pushes to `main` and can also be dispatched manually.

## Screenshots

The documentation uses safe placeholders until real screenshots are available. See `assets/screenshots/README.md` for the exact captures needed and redact every API key, recovery code, webhook secret, account identifier and personal detail before committing an image.
