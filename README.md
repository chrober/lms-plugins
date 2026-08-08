# chrober's LMS Plugin Repository

Add this URL as an additional repository in Lyrion Music Server:

`https://raw.githubusercontent.com/chrober/lms-plugins/main/repo.xml`

## Plugins

- [BlissMixer (Dynamic Weights)](https://github.com/chrober/lms-blissmixer) — a “Don’t Stop The Music” mixer using [Bliss](https://lelele.io/bliss.html) audio analysis with automatic seed-based feature weighting. This fork of [Craig Drummond's BlissMixer](https://github.com/CDrummond/lms-blissmixer) adapts feature importance to what the seed tracks have in common.
- [Better Call Bliss](https://github.com/chrober/lms-better-call-bliss) — a playlist optimizer that previews reordered, extended, or seed-grown saved playlists using Bliss analysis, repeat constraints, and optional Last.fm evidence.

Better Call Bliss entries are added to `repo.xml` by the `lms-better-call-bliss`
release workflow only after an installable GitHub Release package exists. The
feed should reference immutable release assets, never local builds or scaffold
ZIPs.
