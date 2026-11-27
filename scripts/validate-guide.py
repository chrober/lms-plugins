"""Check required article visuals and generated local links, without external network access."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "guide"
SITE = ROOT / "site"
REQUIRED = {
    "index": ["listening-worlds.svg"],
    "understanding-bliss": ["bliss-ecosystem.svg", "bliss-first.svg"],
    "getting-started": ["setup-map.svg"],
    "make-your-playlists-flow": ["playlist-reorder.svg", "playlist-bridges.svg"],
    "rediscover-your-music": ["rediscovery-signals.svg", "bliss-first.svg"],
}

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        for attr in ("href", "src"):
            if values.get(attr):
                self.urls.append(values[attr])

def parse(path):
    parser = References()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser

errors = []
for article, images in REQUIRED.items():
    source = GUIDE / (article + ".md")
    if not source.is_file():
        errors.append(f"Missing article: {source}")
        continue
    body = source.read_text(encoding="utf-8")
    for image in images:
        path = GUIDE / "assets" / "images" / image
        if not path.is_file() or image not in body:
            errors.append(f"Missing or unreferenced illustration: {article}: {image}")
            continue
        try:
            root = ET.parse(path).getroot()
            if not root.get("viewBox"):
                errors.append(f"No scalable viewBox: {path}")
            if root.find("{http://www.w3.org/2000/svg}title") is None:
                errors.append(f"No accessible SVG title: {path}")
        except ET.ParseError as exc:
            errors.append(f"Invalid SVG {path}: {exc}")

pages = {path.resolve(): parse(path) for path in SITE.rglob("*.html")}
if not pages:
    errors.append("No generated HTML found; run mkdocs build first.")
for article in REQUIRED:
    page = SITE / ("index.html" if article == "index" else f"{article}/index.html")
    if not page.is_file():
        errors.append(f"Missing generated page: {page}")
for page, refs in pages.items():
    for url in refs.urls:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc:
            continue
        part = unquote(parsed.path)
        if not part:
            target = page
        elif part.startswith("/lms-plugins/"):
            target = SITE / part.removeprefix("/lms-plugins/")
        elif part.startswith("/"):
            target = SITE / part.lstrip("/")
        else:
            target = page.parent / part
        target = target.resolve()
        if target.is_dir():
            target = target / "index.html"
        if not target.is_file():
            errors.append(f"{page.relative_to(SITE)}: broken local URL {url}")
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            # Browser text fragments are not element identifiers.
            if not parsed.fragment.startswith(":~:text="):
                errors.append(f"{page.relative_to(SITE)}: missing anchor {url}")

if errors:
    raise SystemExit("\n".join(sorted(set(errors))))
print(f"Validated {len(pages)} HTML files and required scenario illustrations.")
