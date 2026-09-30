"""Check that relative links in static HTML resolve to published files."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for key in ("href", "src"):
            if values.get(key):
                self.urls.append(values[key])


errors = []
pages = sorted(ROOT.rglob("*.html"))
for page in pages:
    links = Links()
    links.feed(page.read_text(encoding="utf-8"))
    for url in links.urls:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        path = unquote(parsed.path)
        target = (ROOT / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
        target = target.resolve()
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"{page.relative_to(ROOT)}: {url}")

if errors:
    raise SystemExit("Missing local links:\n" + "\n".join(errors))
print(f"Checked local links in {len(pages)} HTML files.")
