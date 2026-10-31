# chrober's Lyrion Music Server Plugins

A collection of plugins for [Lyrion Music Server (LMS)](https://lyrion.org/).

This repository provides an additional plugin feed so you can install and update my plugins through the LMS plugin manager. The plugins are grouped by purpose; each has its own GitHub repository with features, requirements, setup instructions, and technical documentation.

## Plugins

### Bliss & music discovery

Extend CDrummond's [**Bliss Mixer**](https://github.com/CDrummond/lms-blissmixer) with playlist optimization, experimental mixing features, and extra information that can guide music selection.

| Plugin | What does it add? | Role |
| --- | --- | --- |
| **[Better Call Bliss](https://github.com/chrober/lms-better-call-bliss)** | Improve the flow of saved playlists and player queues, add bridging tracks, extend a playlist, or build a musical route to a chosen track or album. Preview the result before applying it. | Playlist and queue optimizer |
| **[Bliss Mixer Lab](https://github.com/chrober/lms-blissmixer-lab)** | Explore experimental Bliss features: learn from your preferences, try a separate **Bliss (Lab)** Don't Stop the Music mode, and fine-tune artist repeat behavior. | Experimental Bliss companion |
| **[Bliss Guidance: Library Signals](https://github.com/chrober/lms-guidance-library-signals)** | Adds listening-history and library-age guidance to Better Call Bliss and Bliss Mixer Lab, so they can favor rarely played songs, tracks not heard for a long time, or recent additions. | Optional guidance provider |
| **[Bliss Guidance: Last.fm](https://github.com/chrober/lms-guidance-lastfm)** | Adds Last.fm similar-track and similar-artist guidance to Better Call Bliss and Bliss Mixer Lab. Artist relationships can also be stored locally for offline-friendly use. | Optional guidance provider |

## Which plugins do I need?

The four plugins are **not** an all-or-nothing bundle.

- **I want to improve a saved playlist or queue:** Start with **Better Call Bliss**.
- **I want to experiment with Don't Stop the Music (DSTM) and personalized mixing:** Try **Bliss Mixer Lab**. DSTM automatically chooses more music when your current queue needs continuing.
- **I want listening history or Last.fm to influence my mixes or playlists:** Install **Library Signals** and/or **Last.fm** as optional guidance providers for **Better Call Bliss** and **Bliss Mixer Lab**. They do not offer standalone music-selection features: they contribute additional guidance only when enabled in either of these host plugins.

For this Bliss-related collection, start with CDrummond's [**Bliss Mixer**](https://github.com/CDrummond/lms-blissmixer), enable it, and complete its library analysis. Better Call Bliss and Bliss Mixer Lab use that analyzed library; neither replaces the original plugin. The guidance providers are separate, optional installations, and must be enabled in a compatible host before they have any effect.

See each plugin's README for its exact requirements, supported options, and setup instructions.

## Installation

1. In Lyrion Music Server, open **Settings > Plugins**.
2. Add the following URL as an **additional plugin repository**:

   ```text
   https://raw.githubusercontent.com/chrober/lms-plugins/main/repo.xml
   ```

3. Apply the change, select the plugin(s) you want to install, and restart LMS when prompted.
4. Follow the individual plugin's README for prerequisites and first-time configuration.

The feed supplies platform-specific packages where required and supports future updates through the LMS plugin manager.

## More information

Each plugin is developed and documented in its own repository. Please use the corresponding repository to find documentation, releases, and an appropriate place to report an issue or suggest an improvement.


Licenses, attributions, and upstream project credits are listed in the individual plugin repositories.
