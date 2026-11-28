# Music for every season, mood and moment

> "It's snowing outside, the lights are on, and I'm in the mood for Christmas music. I don't want to put together another playlist."

Imagine switching the musical mood of a player with just a few clicks or taps in Material Skin.

This is not a new way of organizing music: Lyrion already supports virtual libraries, including assigning them to individual players, and the original Bliss Mixer can use those libraries for music selection. What the extensions improve is the everyday experience. Once your libraries and settings are ready, Bliss Mixer Lab connects Material's library picker to the player's library, so choosing a different musical world becomes a simple part of listening rather than a separate trip to player settings.

<figure class="guide-figure" markdown="1">
![Four illustrative virtual libraries: Christmas, Summer surf rock, Sunday Jazz, and Dinner and Lounge.](assets/images/listening-moods.svg)
<figcaption>Create your own collections around the music you enjoy. These are examples of virtual libraries, not automatic mood or season detection.</figcaption>
</figure>

A virtual library is a named view of part of your existing collection. Your files stay where they are, and a song can appear in more than one view. [Virtual Library Creator](https://github.com/AF-1/lms-virtuallibrarycreator), by AF-1, makes it convenient to create and maintain these views in a browser.

| Listening moment | Example library |
| --- | --- |
| The first snow, a cup of tea and Christmas lights | Christmas |
| The sun is out, the windows are open | Summer / Surf Rock |
| Coffee and a slow Sunday morning | Sunday Jazz |
| Friends are coming over for dinner | Dinner & Lounge |
| Time for an energetic workout | Workout Rock |

## Set up your musical world

A browsing library in Material Skin and the library assigned to a player are two distinct choices. Lab's optional synchronization brings them together. With both directions enabled, participating Material clients follow the library of their currently selected player, including when you switch between rooms.

<figure class="guide-figure" markdown="1">
![Virtual Library Creator supplies collections; Material's picker sets the selected player's library, which restricts new Lab DSTM candidates and determines the default library for new Better Call Bliss tracks.](assets/images/player-library-sync.svg)
<figcaption>The change belongs to the selected player, not just the current browser. Reverse synchronization is a separate option; other controllers require their own support.</figcaption>
</figure>

**What you need:** Bliss Mixer with completed analysis, Material Skin, Bliss Mixer Lab and at least one virtual library. Virtual Library Creator is recommended but not necessary if your libraries already exist.

1. Create a library such as **Christmas** in **Extras → Virtual Library Creator**, with appropriate genre, tag or other selection criteria. Enable it and let Lyrion create the view.
2. In Material Skin, disable its own **Adjust player library** option to avoid conflicts.
3. Open Bliss Mixer Lab settings. Under **Material player-library synchronization**, enable **Change the player's library when selecting a library in Material**.
4. Optionally enable **Make Material follow the selected player's library** for the reverse direction. Save the settings and reload each Material client.
5. Select the desired player, then choose your virtual library using the Material library picker.
6. Start a suitable song and select **Bliss (Lab)** as the DSTM provider. Subsequent new tracks are selected from the player's assigned library.

!!! tip "Switch moods while listening"
    If the genres of the songs already in your queue don't fit the newly selected library, Lab may initially find no suitable additions. **Relax seed genre restriction after a player library change** lets it retry once without that restriction. The new library and all other filters still apply; normal genre filtering resumes after a successful mix. Your existing queue is not cleared.

## It's Christmas — let the festive music play

Bliss Mixer has a Christmas exclusion that you may want to keep active for everyday listening, while allowing festive music in a dedicated library.

In Bliss Mixer Lab settings, under **Allow Christmas tracks in selected virtual libraries**, check the Christmas library if the normal exclusion would otherwise block those tracks.

<figure class="guide-figure" markdown="1">
![Normal library: the Christmas exclusion remains in force. Selected Christmas library: the exception permits eligible Christmas tracks in Lab DSTM.](assets/images/christmas-exception.svg)
<figcaption>The exception applies only to Bliss (Lab) DSTM and the checked libraries. It does not switch off the exclusion globally or for Better Call Bliss, and other filters remain active.</figcaption>
</figure>

This is a manual, library-specific preference, not a calendar-based switch. Make sure your collection contains enough suitable analyzed tracks.

## Try it with playlists and different rooms

Better Call Bliss also understands virtual libraries for new additions. The editor's initial **Candidate library** follows the active Material library when available, then the active player's assigned library. You can select a different candidate library explicitly. For route actions, the library context restricts newly added tracks; existing source tracks and explicitly chosen destinations are distinct from these additions.

Choose Summer for one room and Jazz for another independent player. Changing libraries does not automatically clear already queued music or force all controllers to reflect the change. Switch back to the full library when you want unrestricted selection.

### Let your music follow you

Moving from the living room to the kitchen? Material already lets you copy, move or swap player queues. With Lab's optional **Carry player libraries with queues copied, moved or swapped in Material** setting, the library can follow the queue too. The destination adopts the source library when copying or moving; when swapping, both libraries follow their queues. The source player's library stays unchanged after a move.

Enable the option in Lab settings, keep Material's **Adjust player library** disabled and reload your Material clients. Your Christmas session can then continue in another room with the same library for subsequent selections. Queue transfers have been tested against independent players through the integration; verification in the Material UI and with synchronized players is still outstanding.

!!! note "The library is a boundary, not a guarantee"
    Bliss acoustic suitability, repeat constraints and other configured filters still apply. If the mix runs out of eligible songs, reconsider the size or rules of the virtual library.

Thanks to the Lyrion community for virtual libraries and player settings, AF-1 for Virtual Library Creator, and Craig Drummond for Bliss Mixer and Material Skin. The Lab builds on these existing capabilities, adding convenient synchronization, library-aware queue transfers, transition recovery and the scoped Christmas exception. Use Bliss Mixer Lab 0.11.2 or later for the current synchronization labels, queue transfers and genre-restriction retry.

## Keep exploring

[Keep the music playing](keep-the-music-playing.md) · [Extend a playlist for your mood](extend-your-playlists.md) · [Personalize your mixes](personalize-your-mixes.md)
