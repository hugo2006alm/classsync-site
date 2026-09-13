# Screenshot checklist

The site deliberately ships with styled placeholders instead of copied third-party screenshots.
Add these images when they can be captured from real accounts with every credential and personal identifier blurred or replaced:

- `fireflies-api-key.webp` — Fireflies Settings → Developer settings, API key area.
- `gemini-api-key.webp` — Google AI Studio API Keys page, showing the Create API key action.
- `notion-token.webp` — Notion Settings → Connections / Developer Mode, internal connection token flow.
- `notion-page-connection.webp` — copied ClassSync Template page → Connections, with the ClassSync connection visible.
- `fireflies-webhook-v2.webp` — Fireflies Webhooks V2 configuration, using fake webhook URL and secret.

Optional self-hosting screenshots:

- `cloudflare-d1.webp` — D1 database overview after creation.
- `cloudflare-worker-secrets.webp` — Worker secret names only, with values hidden.

After adding images, replace each `.screenshot-slot` block in `docs/setup/index.html` (and optionally `docs/self-host/index.html`) with a normal `<figure><img ...></figure>`.
