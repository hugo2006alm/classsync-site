# ClassSync website

Static marketing + documentation site for ClassSync. It intentionally uses plain HTML/CSS/JS so it can be hosted for free on GitHub Pages, Cloudflare Pages or any static host without a build step.

## Structure

- `index.html` — product homepage
- `docs/index.html` — documentation hub
- `docs/setup/index.html` — first-run setup and credential guide
- `docs/self-host/index.html` — Cloudflare Worker + D1 relay setup
- `assets/styles.css` — design system matching the Flutter app
- `assets/screenshots/README.md` — exact screenshot capture list
- `.github/workflows/pages.yml` — GitHub Pages deployment

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

## GitHub Pages

1. In **Settings → Pages**, choose **GitHub Actions** as the source if GitHub does not select it automatically.
2. Push to `main`. The included workflow publishes the site.

## Screenshots

The documentation uses safe placeholders until real screenshots are available. See `assets/screenshots/README.md` for the exact captures needed and redact every API key, recovery code, webhook secret, account identifier and personal detail before committing an image.
