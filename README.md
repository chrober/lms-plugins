# chrober's LMS Plugin Repository

Add this URL as an additional repository in Lyrion Music Server:

`https://raw.githubusercontent.com/chrober/lms-plugins/main/repo.xml`

## Plugins

- [Better Call Bliss](https://github.com/chrober/lms-better-call-bliss) — a
  playlist optimizer that previews reordered, extended, or seed-grown saved
  playlists and player queues using Bliss analysis, repeat constraints, and
  optional Last.fm evidence. It requires the original Bliss Mixer and can use a
  learned matrix supplied by Bliss Mixer Extensions when available.
- [Bliss Mixer Extensions](https://github.com/chrober/lms-blissmixer-ext) —
  experimental and early-access extensions for Bliss Mixer. It installs beside
  the original plugin, contributes the separate **Bliss (Ext)** “Don't Stop the
  Music” provider, and owns its experimental mixer, preference-learning survey,
  learner, and learned matrix.

## Requirements

[Craig Drummond's original Bliss Mixer](https://github.com/CDrummond/lms-blissmixer)
is the required owner of library analysis and `bliss.db`; it is not distributed
by this repository. Bliss Mixer Extensions currently requires Bliss Mixer 0.10.0
or newer and Lyrion Music Server 9.0 or newer. Better Call Bliss treats Bliss
Mixer Extensions and its learned matrix as optional.

## Publishing

The Better Call Bliss and Bliss Mixer Extensions release workflows update
`repo.xml` only after installable GitHub Release packages and checksums exist.
The feed references immutable release assets rather than local builds, workflow
artifacts, or scaffold ZIPs. Platform-specific entries are published for Linux,
macOS, and Windows as appropriate.
