# Concept for the LMS Plugins Wiki

**Status:** Proposal for review — 26 November 2026 (expanded with lightweight, portable and private listening and Lyrion Display as an optional companion)

## 1. Purpose and review of existing documentation

Position the Wiki as a **practical, scenario-driven user guide for Lyrion Music Server users**, rather than an extension of the technical documentation in the individual repositories.

The central question:

> What can these plugins do to improve my everyday music-listening experience, and how can I use them to achieve that?

Users should discover capabilities without already knowing which plugin provides them, how Bliss works internally, or what a guidance provider is.

### Existing documentation

| Repository | Existing documentation |
| --- | --- |
| [LMS Plugins](https://github.com/chrober/lms-plugins) | Collection overview, plugin selection, dependencies and installation |
| [Better Call Bliss](https://github.com/chrober/lms-better-call-bliss) | Playlist optimization, bridging, extension, queue manipulation and musical journeys |
| [Bliss Mixer Lab](https://github.com/chrober/lms-blissmixer-lab) | Personalized mixing, DSTM, artist repeat policies, virtual libraries and alternative mixing actions |
| [Library Signals](https://github.com/chrober/lms-guidance-library-signals) | Rediscovery, listening history, play counts and recent library additions |
| [Last.fm Guidance](https://github.com/chrober/lms-guidance-lastfm) | Related tracks and artists, additional mixing guidance and offline listening |

The READMEs, particularly their “What can I do with it?” sections, provide a strong foundation. However, they are naturally organized around individual plugins. A user interested in rediscovering music in a large collection must already understand the relationship between Bliss Mixer Lab and Library Signals to locate the relevant information.

| Existing READMEs | Proposed Wiki |
| --- | --- |
| Plugin-oriented | Listening-scenario-oriented |
| What does this plugin do? | What do I want to achieve? |
| Individual features | Practical outcomes |
| Individual plugin configuration | Combined plugin usage |
| Technical requirements | Guided setup |
| Architecture and implementation | Illustrative everyday examples |

Retain the READMEs largely as they are; the Wiki is a complementary, cross-plugin documentation layer.

Beyond musical features, the Wiki should communicate the benefits of owning and controlling a local music system: modest hardware requirements, portable listening, independence from internet connectivity, and the option to keep music selection and listening history private. These are benefits of the wider Lyrion and Bliss ecosystem, complemented by the plugins in this collection.

[Lyrion Display](https://github.com/chrober/lyrion-display) is a related, independent Android app that complements the listening experience with a dedicated Now Playing display. It belongs in the Wiki as a peripheral topic, not as another plugin in the collection or an additional editorial pillar. Its own README remains the source for installation, compatibility and support.

## 2. Proposed information architecture

Use a hybrid architecture with **usage scenarios as primary navigation** and individual plugin descriptions as secondary reference material. Readers should not need to understand the ecosystem before discovering its benefits.

- **Home** — welcome and discover what is possible.
- **Getting started**
  - Understanding Bliss and its extensions
  - Which plugins do I need?
  - Installation and first steps
- **Make more of your playlists**
  - Make your playlists flow better
  - Smooth transitions without changing the order
  - Turn a short playlist into a long listening session
  - Improve your current player queue
  - Take a musical journey to a song or album
- **Keep the music playing**
  - A different Don't Stop the Music experience
  - Teach Bliss your musical preferences
  - Avoid repetitive mixes
  - Mix within a selected music collection
- **Rediscover your music collection**
  - Rediscover forgotten favorites
  - Give rarely played music a chance
  - Discover your recently added albums
  - Rediscover related artists and songs
- **Combine plugins for a better experience**
  - Personalized playlists and mixes
  - Combining listening history and Last.fm
  - Music discovery without internet access
- **Your music, anywhere, under your control**
  - A lightweight music server on a Raspberry Pi
  - Take your music collection travelling
  - Listen without an internet connection
  - Keep your listening habits private at home
  - Prepare optional Last.fm information for offline use
- **Plugin reference**
  - Better Call Bliss
  - Bliss Mixer Lab
  - Bliss Guidance: Library Signals
  - Bliss Guidance: Last.fm
- **Help and frequently asked questions**
  - Common questions and troubleshooting
- **Related projects** (a small sidebar section)
  - [Lyrion Display](https://github.com/chrober/lyrion-display) — a dedicated Now Playing display for your Lyrion music system

This is the logical structure, not necessarily a one-page-per-entry plan. Closely related scenarios can initially share a page to keep the Wiki manageable.

## 3. Wiki home page

The home page could also serve as a landing page for visitors from the Lyrion community forum. Introduce four musical reasons to explore the collection rather than immediately introducing four plugins, followed by a cross-cutting benefit: local, portable and private listening.

### Proposed home-page copy

> # Get more out of your music collection
>
> Music is more than a collection of albums and tracks. These extensions for Lyrion Music Server help you create better playlists, enjoy more personal mixes and rediscover music you already own.
>
> **Make your playlists flow**
>
> Turn a collection of favorite songs into a coherent listening experience, with smoother transitions and suitable additions.
>
> **Keep the music playing**
>
> Enjoy continuous mixes that reflect your musical preferences, without having to decide what to play next.
>
> **Rediscover the music you own**
>
> Hear forgotten favorites, overlooked albums and recent additions instead of always returning to the same songs.
>
> **Explore musical connections**
>
> Discover relationships between tracks and artists beyond their acoustic similarities.
>
> **Your music, anywhere, under your control**
>
> Run your music server on a small Raspberry Pi, take it with you when travelling, or enjoy music at home without relying on online recommendation services. Your local music collection, Bliss analysis and listening history can stay with you. Even without internet access, you can create mixes, improve playlists and rediscover music you already own.
>
> **See what's playing**
>
> As an optional companion, [Lyrion Display](https://github.com/chrober/lyrion-display) turns a compatible Fire TV, Android TV or Android tablet into a dedicated Now Playing display for your Lyrion system.
>
> **New here?** Start with *Which plugins do I need?*

For the actual Wiki, use genuine plugin screenshots and purpose-built illustrations rather than generic stock photography.

## 4. Explain the Bliss ecosystem in simple language

Dedicate a page to why the plugins are separate and how they interact with CDrummond's original [Bliss Mixer](https://github.com/CDrummond/lms-blissmixer).

```mermaid
flowchart TB
    Bliss["Bliss Mixer<br/>Understands how your music sounds"]
    BCB["Better Call Bliss<br/>Improves playlists and queues"]
    Lab["Bliss Mixer Lab<br/>Personal and customizable mixes"]
    History["Library Signals<br/>Listening history and library additions"]
    LastFM["Last.fm Guidance<br/>Relationships between artists and tracks"]
    Bliss --> BCB
    Bliss --> Lab
    History -. optional guidance .-> BCB
    History -. optional guidance .-> Lab
    LastFM -. optional guidance .-> BCB
    LastFM -. optional guidance .-> Lab
    Lab -. optional learned preferences .-> BCB
```

The guidance connections apply to supported workflows, notably Bliss (Lab) DSTM and Better Call Bliss optimization.

Suggested explanation:

> Bliss Mixer understands how your music sounds.
>
> Better Call Bliss uses this knowledge to improve your playlists and player queues.
>
> Bliss Mixer Lab uses it to explore new ways of creating mixes, including mixes that reflect your personal taste.
>
> Library Signals adds knowledge about your listening habits, while Last.fm Guidance adds knowledge about musical relationships.
>
> You can choose the extensions that suit your listening habits. You don't need to install all of them.

Explain the **Bliss-first principle** in everyday language: additional information helps choose between musically suitable songs rather than replacing acoustic similarity. No discussion of Rust engines, native binaries, databases, scoring algorithms or provider interfaces is needed here.

### Optional companion: the visual listening experience

Lyrion Display is independent of the Bliss ecosystem. It connects to Lyrion Music Server and presents Craig Drummond's existing Material Skin fullscreen Now Playing view. It neither selects music nor controls playback. A conceptual listening-experience diagram may show the music server providing playback to existing Lyrion players and, separately, Now Playing information through Material Skin to Lyrion Display. Do not draw a direct functional dependency from any Bliss extension to the app.

## 5. Usage scenario catalogue

Some scenarios below are explicitly described in the READMEs; others are practical applications of documented features. The original Bliss Mixer and its completed library analysis are assumed throughout.

### Playlists and listening sessions

| Scenario | Benefit | Plugin |
| --- | --- | --- |
| My favorite songs don't flow well together | Reorder tracks for smoother transitions | Better Call Bliss |
| I don't want to change my carefully curated playlist | Add suitable bridging tracks | Better Call Bliss |
| I'm hosting a dinner party | Extend a short playlist to last the entire evening | Better Call Bliss |
| I'm not happy with what's coming up next | Improve upcoming tracks without interrupting the current song | Better Call Bliss |
| I want to hear a particular album next | Create a musical journey to the album | Better Call Bliss |
| I want to take a musical detour | Visit another song or album and return to the original queue | Better Call Bliss |

### Continuous and personalized listening

| Scenario | Benefit | Plugin |
| --- | --- | --- |
| I don't want to constantly choose what plays next | Automatic continuation with Bliss (Lab) | Bliss Mixer Lab |
| Bliss doesn't always understand what I consider similar | Learn personal musical preferences | Bliss Mixer Lab |
| The same artists appear too frequently | More precise artist repeat handling | Bliss Mixer Lab |
| I want a dedicated Christmas music experience | Respect the player's virtual library and optionally suspend Christmas exclusions for that library | Bliss Mixer Lab |
| I have separate collections for different moods | Restrict DSTM mixes to the selected player library | Bliss Mixer Lab |

### Music rediscovery

| Scenario | Benefit | Plugin combination |
| --- | --- | --- |
| I haven't heard some of my favorite songs in years | Prefer long-unheard tracks | Lab + Library Signals |
| My mixes always contain the same familiar songs | Give less-played tracks more opportunities | Lab + Library Signals |
| I recently added several new albums | Give recent additions more attention | Lab + Library Signals |
| I want a mix of my familiar favorites | Favor frequently played tracks | Lab + Library Signals |
| I want an existing playlist to help me rediscover music | Guide playlist additions using listening history | Better Call Bliss + Library Signals |

### Musical relationships and combined experiences

| Scenario | Benefit | Plugin combination |
| --- | --- | --- |
| Acoustic similarity alone isn't enough for me | Include Last.fm musical relationships | Either host + Last.fm |
| I want to rediscover related artists I already own | Favor musically suitable, related artists | Lab + Last.fm |
| I want playlists that reflect my personal taste | Use learned preferences in playlist optimization | Better Call Bliss + Lab |
| I want related but overlooked music | Combine Last.fm relationships and listening history | Either host + both providers |
| I take my music server on holiday | Prepare artist relationships for offline-friendly listening | Either host + Last.fm |

The combined scenarios are particularly valuable because they communicate the benefits of the ecosystem as a whole.

### Lightweight, portable and private listening

| Scenario | Benefit | What makes it possible |
| --- | --- | --- |
| I don't want to keep a large computer running just to listen to music | A compact, low-resource local music server | Lyrion + Bliss Mixer; compatible collection plugins |
| I want to take my music collection on holiday or on a camping trip | Bring the server, local music and prepared analysis with you | Lyrion + Bliss Mixer; optional Better Call Bliss and Lab |
| I have unreliable or no internet access | Keep mixing, optimizing playlists and rediscovering locally available tracks | Local Bliss analysis, local music, optional learned preferences and Library Signals |
| I prefer not to send my listening habits or music queries to online services | Use local music selection and local listening history on an internet-isolated setup | Lyrion + Bliss Mixer; optional Library Signals and Lab; no live online guidance |
| I want some Last.fm knowledge available while travelling | Prepare and reuse locally stored artist relationships | Last.fm Guidance with API Key source; Offline preferred; compatible host |

### Dedicated article: Your music, anywhere, under your control

> “I want a small music server that I can take with me, and I don't want my music experience to depend on having an internet connection.”

This is a distinct user benefit, not merely a technical requirement or another Last.fm feature. It merits a dedicated page, cross-linked from Getting Started, Rediscover Your Music, Explore Musical Connections and the home page.

**A small music server, not a cloud service.** A Raspberry Pi 4 is the author's actual development and test platform and a practical example of the modest hardware on which the collection can run. Avoid universal performance guarantees or quantified resource claims without measurements; library size, initial analysis, optimization workload and storage affect performance.

**Take your music along.** A portable setup could consist of a Raspberry Pi, a power supply, a local music drive or other storage accessible without the internet, and a player/controller on a local network. Illustrate everyday examples such as a holiday apartment, campervan or remote location. A local network can work without an internet connection; internet isolation does not necessarily mean disconnecting the player and server from one another.

**Keep your music knowledge with you.** Once the local library has been prepared, Bliss acoustic analysis, Lyrion play counts and last-played information, library-addition dates and optional learned preferences can remain locally available. The collection's playlist and mixing capabilities can operate on those local resources. Library Signals adds music rediscovery without requiring an external recommendation service.

**Privacy at home.** The same setup can deliberately be isolated from the internet, rather than merely being offline while travelling. Local analysis and locally guided selection do not inherently require sending track or artist queries to a recommendation service. Avoid claiming that every LMS feature, third-party plugin or controller is network-free: online metadata, scrobbling, streaming, updates and Last.fm queries may use the internet depending on configuration. For a firm no-internet guarantee, enforce isolation at the network level and use locally available media. A LAN-only setup is not necessarily a strict physical air gap; explain that distinction without unnecessary networking jargon.

**Optional Last.fm preparation.** Last.fm Guidance can acquire artist relationships while connected, using its API Key source, and retain them locally for later use. Offline preferred can reuse stored artist information and degrade gracefully when the network is unavailable. Track relationships use a separate short-lived cache, so not all track information will necessarily be available offline. Offline preferred is not a strict offline-only setting: it may still make online requests if connectivity is available. For an internet-isolated setup, rely on actual network isolation (or leave Last.fm guidance disabled if no external data is wanted). Be explicit that initial acquisition sends requests to Last.fm; storing the results locally does not undo those earlier requests. Keep the distinction between fully local analysis/history and previously downloaded external knowledge.

**Before you leave home:** install and configure the required plugins, complete the Bliss analysis, ensure the music files are accessible offline, optionally train the preference survey and download Last.fm artist information, and test playback and mixing with internet access disconnected. Updates or downloads can be performed during a separate connected maintenance session if desired.

**Give credit where it belongs.** Local music hosting and local playback are Lyrion capabilities. Local acoustic analysis and the foundation for Bliss-based music selection come from [Bliss Mixer by Craig Drummond](https://github.com/CDrummond/lms-blissmixer) and the underlying Bliss technology. The plugins in this collection build on that foundation: Better Call Bliss adds local playlist and queue transformations; Bliss Mixer Lab adds experimental mixing and optional learned preferences; Library Signals uses locally stored listening information; Last.fm Guidance optionally adds stored external artist relationships. The portability and privacy benefits are shared ecosystem strengths, not inventions of this collection alone.

### Peripheral usage scenarios: Lyrion Display

| Scenario | Benefit |
| --- | --- |
| Bring your music to life on the big screen | See album artwork, artist and track information on a compatible TV while your usual Lyrion player continues playing. |
| Give an old tablet a new purpose | Use a compatible Android tablet as a dedicated Now Playing display beside your stereo. |
| Rediscover music at a glance | When a Library Signals-guided mix brings back a forgotten song, immediately see which artist and album it comes from, where artwork and metadata are available. |
| Your music experience travels with you | Pair a portable Raspberry Pi music server with an Android display on the same reachable local network, even without internet access. |

The app complements these experiences without being required for any of them. It works with ordinary Lyrion playback, regardless of whether Bliss or the collection's plugins are installed.

**Proposed short article insert — More than just listening**

> Rediscovering music is even more enjoyable when you can see what's playing. An album cover, an artist's name or a forgotten song title can bring back memories and encourage you to explore your collection further.
>
> [Lyrion Display](https://github.com/chrober/lyrion-display) turns a compatible Fire TV, Android TV or Android tablet into a dedicated, fullscreen Now Playing display using Material Skin.
>
> It requires no additional server plugin beyond Material Skin, no account and no cloud service. It works alongside your existing Lyrion setup, regardless of which mixing or music discovery plugins you use.
>
> Whether you're listening at home or running a portable music server without internet access, it's another way to make your music collection part of your everyday surroundings.
>
> [Discover Lyrion Display](https://github.com/chrober/lyrion-display)

Keep this insert short and cross-link it from **Rediscover Your Music** and **Your Music, Anywhere, Under Your Control**. Include a subtle home-page link and a **Related projects** sidebar entry. No standalone Wiki article is planned initially.

**Requirements and boundaries:** a compatible Android-based device (Android 5.1 or newer), a reachable Lyrion server with Material Skin enabled, and an existing Lyrion player. Authenticated Lyrion servers are not currently supported. The app is read-only; control playback with your usual Lyrion clients. It does not require Bliss Mixer, any of the four collection plugins or the separate Material Android app. The fullscreen interface and themes are provided by Craig Drummond's Material Skin. Internet-independent use requires local network reachability and locally available media/metadata; it does not imply that the TV or Android operating system itself never contacts online services. Refer to the [app README](https://github.com/chrober/lyrion-display) for device compatibility, installation and detailed limitations.

## 6. Consistent structure for each scenario

Each scenario should have a recognizable editorial structure:

1. **The situation:** A relatable everyday listening experience.
2. **What you can achieve:** The outcome, without technical jargon.
3. **What you need:** Required plugins and optional enhancements.
4. **How to do it:** A short step-by-step guide using actual UI terminology.
5. **What to expect:** The practical result and relevant limitations.
6. **Try this as well:** Related scenarios or useful plugin combinations.

### Example A — Make your playlists flow better

> “I love every song in my playlist, but somehow they don't work particularly well together in their current order.”

Imagine you've created a playlist of 30 favorite songs. Some are quiet and atmospheric, others are energetic and loud. You enjoy all of them, but listening to the playlist sometimes feels like jumping randomly between different moods.

Better Call Bliss can help you find a more natural sequence without removing the songs you selected.

**Illustrative before/after:** the same eight songs in a different order.

| | Track order |
| --- | --- |
| Before | A → B → C → D → E → F → G → H |
| After | E → A → C → H → G → D → B → F |

A possible visual is a before/after bar diagram representing a single musical characteristic, with abrupt changes in the original order and smoother changes in the optimized order. This is a simplified illustration, not an actual optimization result or a claim that Bliss sorts by energy: actual optimization considers multiple acoustic characteristics and configured constraints.

**What you need:** Bliss Mixer and Better Call Bliss. No additional guidance plugins are necessary.

**How to do it**

1. Open **Extras → Better Call Bliss**.
2. Select one of your saved playlists.
3. Choose to optimize the track order without adding tracks.
4. Run a preview and review the suggested sequence.
5. Save the result as a new playlist.

**What happens to my original playlist?** Nothing changes unless you explicitly choose to overwrite it. Save the optimized version separately and compare the two.

**Try this as well:** Smooth transitions without changing the original order, or extend your playlist with additional tracks.

### Example B — Take a musical journey

> “I'm listening to something right now, but I'd love to hear another album without abruptly changing the mood.”

Give the three distinctive **Bliss me there...** actions a dedicated page with visual examples.

```text
Current queue:
[Now] [B] [C] [D] [E]

Bliss me there...
[Now] [+] [+] [Target]

Bliss me there... and back again!
[Now] [+] [Target] [+] [B] [C] [D] [E]

Bliss me there... when we're through!
[Now] [B] [C] [D] [E] [+] [+] [Target]
```

Legend: Now = currently playing; B–E = original upcoming queue; + = illustrative bridging track; Target = selected song or album.

- **Bliss me there...** — Take a route directly to the destination.
- **Bliss me there... and back again!** — Take a detour and return to the original upcoming queue.
- **Bliss me there... when we're through!** — Finish the current queue before heading to the destination.

These shortcuts require Material Skin. Unlike the playlist editor, successful routes are applied automatically after validating the live player queue. If a route fails or the queue changes incompatibly, no changes are made. An album destination includes its local tracks in disc and track order. Diagrams are illustrative.

### Example C — Rediscover the music you already own

> “I have thousands of albums, but sometimes I feel like I'm listening to only a small part of my collection.”

Library Signals can help Bliss give more attention to music you rarely play, haven't heard for a long time or have recently added.

| Approach | Benefit |
| --- | --- |
| Forgotten favorites | Prefer songs you haven't listened to for months or years. |
| Hidden gems | Give songs with low play counts more opportunities to appear. |
| New discoveries | Hear more of the albums you recently added. |

**What you need:** Bliss Mixer, Bliss Mixer Lab and Library Signals.

Enable Library Signals in Bliss Mixer Lab, configure your preferred listening-history signals and select **Bliss (Lab)** as your Don't Stop the Music provider.

Your mixes will continue to be based on acoustic similarity. Library Signals simply helps decide which suitable tracks deserve more attention.

You can also use Library Signals with Better Call Bliss to guide music added to playlists.

**Optional companion:** If you have a dedicated screen beside your stereo or in your living room, [Lyrion Display](https://github.com/chrober/lyrion-display) can show the artist, album and track that you have just rediscovered. It is independent of the mixing and guidance plugins.

## 7. Plugin selection guide

A page titled **Which plugins do I need?** should make dependencies immediately understandable. The interactive prototype in the original discussion is represented here by a static decision table, suitable for GitHub Wiki Markdown.

| What would you like to achieve? | Install in addition to Bliss Mixer |
| --- | --- |
| Improve or extend my playlists and queues | Better Call Bliss |
| Enjoy continuous, automatic mixes | Bliss Mixer Lab |
| Personalize music selection based on my taste | Bliss Mixer Lab; optionally Better Call Bliss for playlists |
| Rediscover music using my listening history | Either host + Library Signals |
| Use Last.fm musical relationships | Either host + Last.fm Guidance |
| Use stored Last.fm artist relationships offline | Either host + Last.fm Guidance (API Key source, offline preferred) |

Combine rows for multiple goals. The original Bliss Mixer is the required foundation for the two hosts; complete its library analysis first. Better Call Bliss and Lab are independent and neither requires the other for basic operation. Providers are optional and must be enabled on the relevant host settings page. For guidance-only goals, suggest Lab for continuous listening and Better Call Bliss for playlist work.

Offline preferred can use stored artist relationships; it is not strict offline-only, and track relationships are not all permanently stored. Last.fm is not a streaming source in this context.

## 8. Visual documentation strategy

Use visuals that explain a feature rather than decorate a page.

| Visual element | Purpose | Priority |
| --- | --- | --- |
| Playlist before/after diagrams | Explain reordering | High |
| Bridging track diagrams | Explain preserving the original order | High |
| Musical route diagrams | Explain the three destination actions | High |
| Plugin relationship diagram | Explain the ecosystem | High |
| Actual Better Call Bliss screenshots | Show how to use the editor | High |
| Actual DSTM selection screenshots | Show where to select Bliss (Lab) | High |
| Guidance settings screenshots | Show how to enable and configure providers | High |
| Preference survey screenshots | Explain personalization | Medium |
| Last.fm offline preparation screenshots | Explain preparation for offline listening | Medium |
| Raspberry Pi and local music setup illustration | Explain portable, internet-independent listening | Medium |
| Local vs optional online data-flow diagram | Explain privacy and where music knowledge resides | High |
| Actual Lyrion Display Now Playing screenshot | Illustrate the optional visual listening experience, using the app repository's existing screenshot | Low (peripheral topic) |

Use Material Skin for most screenshots while explicitly indicating which features require it. Better Call Bliss's editor does not require Material Skin; its destination shortcuts do.

Establish a consistent visual language: original tracks gray, currently playing tracks green, added tracks blue and destination tracks orange. Add text labels so that color is not the only means of conveying meaning.

## 9. Scope of the initial Wiki

Start with approximately **13 content pages**, plus a sidebar and footer.

| Proposed Wiki page | Content |
| --- | --- |
| Home | Introduction and scenario navigation |
| Understanding Bliss | Ecosystem and plugin relationships |
| Getting Started | Plugin selection, requirements and installation |
| Make Your Playlists Flow | Reordering and bridging |
| Extend Your Playlists | Longer listening sessions |
| Improve Your Player Queue | Working with live queues |
| Take a Musical Journey | All three destination shortcuts |
| Keep the Music Playing | DSTM, artist repeat behavior and virtual libraries |
| Personalize Your Mixes | Preference learning and its use in both hosts |
| Rediscover Your Music | All Library Signals scenarios; optional Now Playing display example |
| Explore Musical Connections | Last.fm guidance, combined guidance and offline listening |
| Your Music, Anywhere, Under Your Control | Raspberry Pi, travel, internet-independent listening, local data and privacy; optional Last.fm preparation and local Now Playing display |
| Plugins and FAQ | Plugin references, limitations and troubleshooting |

Use GitHub's custom `_Sidebar.md` and `_Footer.md` for consistent navigation. Add a small **Related projects** sidebar section linking to Lyrion Display; keep it outside the plugin reference. No additional content page is required for this companion app. Split topics into dedicated pages later as content grows, without changing the overall architecture.

## 10. Editorial principles

| Prefer | Avoid where possible |
| --- | --- |
| Songs that sound good together | Acoustically eligible candidate pool |
| Your personal musical preferences | Learned similarity matrix |
| Additional musical knowledge | External scoring signals |
| Songs you haven't heard in a long time | Last-played timestamp weighting |
| Suitable songs between two tracks | Intermediate route candidates |
| Preview your improved playlist | Optimizer job output |
| Stored artist relationships | Persistent SQLite artist graph |

Use technical terms when they correspond to actual UI labels or are needed to configure a feature.

Consistently communicate that:

- The original Bliss Mixer remains available and functional.
- The four extensions are not an all-or-nothing bundle.
- Guidance providers must be explicitly enabled.
- Additional guidance expresses preferences, not guaranteed track selections.
- Audio files are not modified.
- Bliss Mixer Lab is experimental by design.
- Local-first listening and optional online guidance must be clearly distinguished; avoid promising that every plugin or Lyrion feature is inherently offline or private.
- Credit Lyrion, CDrummond's Bliss Mixer and the underlying Bliss technology for their foundational contributions. Describe Raspberry Pi 4 as the author's tested setup, not a universal performance benchmark.
- Present Lyrion Display as an independent, optional Android companion, not an LMS plugin or a Bliss integration. Credit Craig Drummond's Material Skin for the Now Playing interface and themes. Keep app-specific installation and support documentation in its own repository.

Preserve the established compatibility wording: developed and tested with Lyrion 9.1; older versions may work but have not been tested. Link to the plugin READMEs for exact requirements and technical details rather than duplicating them.

## 11. Proposed Wiki implementation and publication

The repository has Wiki enabled and the GitHub connection has normal repository write permissions. Direct Wiki-specific operations are not available through the current connector; the existing Wiki's page inventory could not be verified through it.

GitHub stores Wikis in separate Git repositories. The Wiki remote is:

```text
https://github.com/chrober/lms-plugins.wiki.git
```

Consider maintaining the canonical Wiki source in the main `lms-plugins` repository:

```text
lms-plugins/
├── .github/
│   └── workflows/
│       └── publish-wiki.yml
├── wiki/
│   ├── Home.md
│   ├── _Sidebar.md
│   ├── _Footer.md
│   ├── Getting-Started.md
│   ├── Understanding-Bliss.md
│   ├── Make-Your-Playlists-Flow.md
│   ├── ...
│   └── images/
├── README.md
└── repo.xml
```

```mermaid
flowchart TB
    Source["Markdown documentation<br/>lms-plugins/wiki/"] --> Review["Pull request and review"]
    Review --> Publish["GitHub Actions publishes Wiki"]
    Publish --> Wiki["Public GitHub Wiki<br/>lms-plugins.wiki.git"]
```

Advantages:

- Create and edit source pages through the existing GitHub connection.
- Review documentation changes through normal pull requests.
- Validate internal links and referenced images in CI.
- Publish changes automatically after merging.
- Keep the Wiki source accessible in the normal repository.

**Open implementation questions:** verify authentication and push permissions against the separate Wiki repository before relying on automatic publication. If the Wiki is not initialized, its first page must be created. Check for existing pages before any synchronization; avoid inadvertently overwriting them. The publication workflow is a proposal, not an implemented or tested capability.

GitHub documentation: [About wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis), [Adding or editing wiki pages](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages).

## 12. Recommended direction and rollout

Treat the Wiki less as a conventional software manual and more as a **guide to getting more enjoyment out of a personal music collection**.

The four editorial themes:

- **Musical flow** — make existing playlists and listening sessions more coherent.
- **Personalization** — make music selection reflect individual musical taste.
- **Rediscovery** — get more value out of a collection that may have been accumulated over decades.
- **Musical exploration** — discover interesting connections and journeys within that collection.

These four musical themes can remain the editorial identity of the Wiki regardless of how many plugins are added to the collection in future.

A fifth, cross-cutting theme is **freedom and control — your music, anywhere, under your control**: lightweight hardware, portability, internet independence and privacy through local music selection. It should be visible on the home page and have a dedicated article, not be buried under Last.fm configuration. This dimension describes a shared strength of the Lyrion and Bliss ecosystem and the collection's extensions.

Lyrion Display adds an optional visual dimension to the overall listening experience, particularly rediscovery and portable/local listening. It is a related project, not a sixth pillar. Keep the core Wiki focused on the four collection plugins and the five established themes.

Start by implementing the home page, ecosystem explanation, getting-started guide, custom sidebar and two representative scenario pages: **Make Your Playlists Flow** and **Rediscover Your Music**. Establish the tone, level of detail, visual language and navigation before populating the remaining pages. Include the local-first positioning in the home page and prioritize the dedicated portable/private listening article in the next batch.

This is a concept for review, not the published Wiki. The chat's interactive selector and visual mockups have been translated into Markdown-compatible tables, diagrams and descriptions; final screenshots and illustrations remain to be prepared.
