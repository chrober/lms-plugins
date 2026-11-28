# User guide development

All thirteen planned articles of the [editorial concept](WIKI_CONCEPT.md) now have a first complete content draft, navigation and conceptual graphics. They are reviewable, but not approved for publication until the live UI and visual review is complete.

## Preview locally

With Python 3.12 installed:

```powershell
py -3.12 -m venv .venv-docs
.\.venv-docs\Scripts\python.exe -m pip install -r requirements-docs.txt
.\.venv-docs\Scripts\python.exe -m mkdocs serve
```

Open http://127.0.0.1:8000/. For other platforms, use the equivalent Python virtual-environment interpreter. To validate:

```powershell
.\.venv-docs\Scripts\python.exe -m mkdocs build --strict
.\.venv-docs\Scripts\python.exe scripts/validate-guide.py
```

## Preview without installing MkDocs

Download the **user-guide-preview** artifact from a successful **Validate user guide** Actions run, extract it, open a terminal in the extracted folder, and run:

```powershell
py -m http.server 8000
```

Open http://localhost:8000/. Serve the files rather than opening the HTML directly so navigation and search can load their assets correctly.

## Review checklist

- Read all thirteen pages on desktop and a narrow mobile viewport; review navigation, search and both themes.
- Confirm the actual workflow and wording against the plugin versions installed on a Lyrion 9.1 test server.
- Review each custom SVG for clear labels and appropriate simplification. No graphs are measured optimization results.
- Capture actual screenshots for the first release: Better Call Bliss Extras editor (source/strategy), read-only preview showing reorder and bridging; Library Signals settings and host enablement, the Bliss (Lab) DSTM selector; the duration controls and queue outputs; the three Material route actions; the virtual-library creator, library picker, the four-mode synchronization selector and separate queue-transfer option in Lab 0.11.4 or later, the Material conflict notice if applicable, and Christmas exception; the preference survey and learned matrix controls; Last.fm source, offline preparation and coverage settings. Capture at a readable scale, anonymize player names, local addresses and private library content when necessary, and give each image useful alt text.
- The reviewed upstream READMEs did not provide these specific UI captures. They are outstanding, not simulated. The conceptual SVGs are included now; add genuine screenshots before approving the relevant practical sections for publication.
- Review the Home page links and all eight added scenario/reference pages, including seasonal player libraries, offline/private use, musical routes and preference learning.

## Publish after review

1. Merge an approved documentation PR into main.
2. In this repository only, choose **Settings → Pages → Build and deployment → Source → GitHub Actions**.
3. On the default branch, manually dispatch **Publish user guide** with confirmation enabled.
4. Check the deployment URL, navigation, search and asset paths at the project URL. The first deployment is manual; subsequent automatic publishing can be considered separately.

The existing plugin feed, validation workflow and other Pages projects are independent. Do not enable a custom domain or alter another site's configuration for this guide.

## Editorial and visual revision

The guide now has 14 articles, including a separate seasonal listening page. The home page leads with listening scenarios. The desktop illustrations remain local SVGs; three have narrow-screen versions selected at up to 600px. Full-size links open the original illustration in a new tab. Dark mode deliberately retains the readable light illustration palettes with a subtle outline rather than inverting semantic colors. Check home headings, seasonal navigation, full-size links, mobile artwork, and theme switching in the browser before publication. Genuine plugin screenshots remain outstanding.

- Visual review: compare the seasonal, rediscovery and portable icon artwork against the approved warm, flowing icon style. Verify the same motifs on mobile and desktop, the repeated Christmas motif, and unchanged semantic colors in sequence diagrams. The generated reference artwork has been translated into editable SVG shapes rather than embedded as a raster image.
