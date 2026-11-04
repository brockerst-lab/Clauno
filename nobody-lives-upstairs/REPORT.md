# Nobody Lives Upstairs — production report

**Final Suno upload (private):** https://suno.com/song/4a284cc8-71c4-4944-8ae7-aacc550a1bbc
**Selected source take:** https://suno.com/song/409783bc-9000-426f-bfc0-4b5a24f121ca (v6-wild, Round 3)
**Local files:** `audio/Nobody Lives Upstairs (Master).wav` (24-bit/48 kHz), `audio/Nobody Lives Upstairs (Master).mp3` (320 kbps), `audio/source_409783bc.wav` (untouched download), `art/cover.png` (3000×3000)

## The collab brief
"Triple-Genre Collision #14" by @monelo777 makes these requirements:
- The title must be "Nobody Lives Upstairs", and that phrase must appear in the lyrics. ✔ It appears 5 times.
- Slowcore × Grunge × Dungeon Synth must be fused into one sound, with all three recognisable and not split into sections. ✔ This is the design goal; see the evidence below.
- The emptiness should feel alive: intimate, raw, eerily otherworldly.
- **The listing says "1 specific request", which I could not read.** The collab page is behind Suno's login, so I don't know what it says. Check it before submitting.

## Research
- **Public research:** the OP's playlist "Triple genre collision winners" has 14 songs, with style prompts and lyrics visible. The winning prompts are long and concrete. They describe vocal delivery ("roomy and unprocessed", "hushed close-mic"), an arc from intro to bridge to outro, and the mechanism that locks genres together ("66 BPM half-time doom crawl with four-on-the-floor disco kick"). Two winners came from the same entrant, 【BareW✪LF】.
- **Fusion background:** I found no documented slowcore × dungeon synth or grunge × dungeon synth releases. The dungeon synth crossovers on record are mostly with black metal and synthwave.
- **Blocked by login:** Suno search, style pages, the collab page and the other entries.

## Generation (6 of 8 authorised requests; 60 credits; Max Mode not used)
Every take used male vocals and weirdness 0.45.

| Round | Model | Take | Duration | BPM | Key | Tagger evidence |
|---|---|---|---|---|---|---|
| 1 | v6 | [ae5f0da0](https://suno.com/song/ae5f0da0-01d6-48dd-ab0a-ea6fb58a975c) | 3:47 | 62.2 | B♭ maj | grunge 0.62, bass; all lyrics aligned |
| 1 | v6 | [c445cb3b](https://suno.com/song/c445cb3b-7a72-4bb0-9681-8b977fd0a494) | 3:53 | 119.6 (likely double-time) | B♭ maj | alt rock, dark ominous |
| 1 | v6-wild | [1b2b7582](https://suno.com/song/1b2b7582-316b-43ec-8668-6aa01586c217) | 3:30 | 64.6 | F maj | grunge, alt rock, **keyboard 0.64**, piano; all lyrics aligned |
| 1 | v6-wild | [764c5b30](https://suno.com/song/764c5b30-7e3c-4ccf-a7c0-b030e4a303bc) | 3:20 | 65.6 | E♭ maj | grunge 0.62, alt rock |
| 2 | v6 | [b9c3c69d](https://suno.com/song/b9c3c69d-3878-4931-857d-e651bef09858) | 4:00 | 117.2 (likely double-time) | A♭ min | alt rock, grunge |
| 2 | v6 | [c06fa417](https://suno.com/song/c06fa417-b275-44a3-8990-0e8f8411d8af) | 3:57 | 62.9 | B♭ maj | rock, alt rock |
| 2 | v6-wild | [5ce97035](https://suno.com/song/5ce97035-1b21-46c8-88b5-1fe3c1b70c4e) | 3:42 | 63.1 | F min | rock, alt rock |
| 2 | v6-wild | [4dbb85b8](https://suno.com/song/4dbb85b8-da75-4721-a9a1-d5082ced6a76) | 3:42 | 63.6 | F min | rock, alt rock, grunge 0.63 |
| 3 | v6 | [d82e1cfe](https://suno.com/song/d82e1cfe-71e0-4274-aa95-dbb6f06a04a8) | 4:44 | 63.5 | G min | **keyboard 0.76, piano, harpsichord**, rock; male vocal; all lyrics aligned |
| 3 | v6 | [63974a30](https://suno.com/song/63974a30-daf7-4a4a-b7c0-3401a18d9f2f) | 4:53 | 64.9 | G min | keyboard 0.70, ambient, meditation (grunge lost) |
| 3 | v6-wild | [85e6266f](https://suno.com/song/85e6266f-9cfa-4b6e-a3e5-ceb7d4fc896b) | 3:55 | 64.4 | D min | keyboard 0.65, alt rock, "poor recording quality" |
| 3 | v6-wild | **[409783bc](https://suno.com/song/409783bc-9000-426f-bfc0-4b5a24f121ca) ← selected** | 4:24 | 63.8 | G min | **rock 0.85, alt rock 0.70, keyboard 0.64, grunge 0.63, instrumental 0.66**; all lyrics aligned |

What changed between rounds:
- **Round 1 → 2:** "Dungeon synth" moved to the front of the prompt, concrete keyboard names were added (Casio/Roland choir, harpsichord), and style influence went from 0.65 to 0.75. Keys moved to minor in three of the four takes, but keyboards still weren't detected. Strengthening the prompt didn't fix it.
- **Round 2 → 3:** I changed the lever instead of pushing harder. The arrangement got keyboard-led instrumental passages written into the lyrics, with the fuzz kept droning underneath. The prompt re-weighted the mix: keyboards carry the melody throughout, and the fuzz drones beneath and never leads. Keyboards were detected in all four takes, and three were in G minor.
- **Models:** v6 and v6-wild behaved alike on tempo and lyric fidelity. v6-wild gave the only take that kept grunge and keyboards together. v6 produced the strongest keyboard and harpsichord reading but tended to lose the grunge weight, and one v6 take drifted into ambient. Neither model held all three genres reliably. The winning take came down to the draw within a round.
- **Why no Round 4 (Max Mode):** the major gap was the missing dungeon synth layer, and Round 3 fixed it. Under the rules, research and Max Mode weren't justified.

## Why 409783bc
- **Fusion requirement:** it's the only one of the twelve takes tagged with grunge and keyboards together. The slow tempo (63.8 BPM) and minor key support the slowcore side, though Suno's tagger has no slowcore label.
- **Arrangement:** the lyric alignment shows the structure landed as written. There's a 32-second keyboard intro, a keyboard break after chorus 1 (84–100 s), a 30-second harpsichord and keyboard passage before the final chorus (175–205 s), and an outro on "Window, door".
- **Lyrics:** all lines are present in order, with no invented words or repeated sections.
- **Runner-up:** d82e1cfe (v6). It has a stronger keyboard and harpsichord signature but no grunge tag, and it's 20 s longer.
- **Caveat:** I chose from metadata and automated analysis only. MP3 previews cost a download credit, and only one download was authorised, so I didn't listen to any take. Melody, vocal quality and how well the fusion actually lands are unverified.

## Mastering
| | Source | Master |
|---|---|---|
| Format | WAV PCM16, 48 kHz, stereo | WAV PCM24, 48 kHz, stereo (+ MP3 320 kbps) |
| Duration | 264.16 s | 264.16 s (sample-identical length) |
| Integrated loudness | −15.83 LUFS | −14.00 LUFS |
| True peak | −4.46 dBTP | −2.62 dBTP |
| Loudness range (approx.) | 5.2 LU | 5.2 LU |
| Short-term max/min | −13.2 / −29.3 LUFS | −11.3 / −27.5 LUFS |
| Crest factor | 13.1 dB | 13.1 dB |
| L/R correlation, side/mid | 0.631, −6.4 dB | unchanged |
| Clipped samples | 0 | 0 |

**Processing:** a 20 Hz second-order zero-phase high-pass (subsonic safety; there was only −36.5 dB of energy below 25 Hz) plus +1.85 dB of gain. There's no EQ, compression or limiting. The tonal balance is dark and heavy in the 60–120 Hz band, which fits the genre, and I couldn't listen to justify changing it. The true peak stayed under −1 dBTP without a limiter. After matching levels, the master differs from the source by only −34.4 dB of residual, which is the subsonic filter alone.

## Artwork
`art/cover.png` is 3000×3000 and drawn in code: fourteen faint stairs climb into the dark toward one warm lit window. The fourteenth step sits slightly off ("Thirteen / then one more"), and the frame has tape grain and scanline warble, with no text. No image-generation tool was available.

**Not attached to Suno.** The Suno tools can't set cover art, and the web editor needs your login. Upload it in the song's edit menu on suno.com.

## Suno upload checks
- ✔ Upload completed, status `complete`, type `upload`.
- ✔ Title is "Nobody Lives Upstairs".
- ✔ Duration is 264.16 s, matching the master.
- ✔ It's in your library and private.
- ✔ Lyrics are replaced with the exact approved text.
- ✘ Cover art isn't attached (see above).
- ? Playback: Suno reports the clip as complete, but I couldn't play it myself because the page needs your login.
- ? Community Collab eligibility: I couldn't check it. If it doesn't show up as selectable, Suno's Remaster has fixed this for you before (unproven, and it costs credits).

## Submission: not done (needs you)
Community Collab is only reachable when signed in, and Claude in Chrome isn't connected, so I couldn't submit.

To finish:
1. Open the collab and **check the OP's "1 specific request"** against the track.
2. Attach `art/cover.png` to the upload.
3. Submit the uploaded song with this comment:

> Slowcore × grunge × dungeon synth as one sound: a cheap 90s keyboard choir and harpsichord carry a slow modal melody from the first bar to the last, while drop-D fuzz drones underneath at 64 BPM, never taking over. The vocal stays close-mic and hushed until the last chorus cracks. The emptiness is the flat upstairs: footsteps window to door, a lamp that comes on at four, thirteen stairs in the dark — then one more.

## Credits
- Generation: 60 used (277 → 217).
- Downloads: 1 used (42 → 41).
- No purchases, deletions, publishing or submissions.
