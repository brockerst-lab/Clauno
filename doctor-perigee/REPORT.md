# Come a Little Closer, Moon (The Ballad of Doctor Perigee) — production report

**Final Suno upload (private):** https://suno.com/song/c5d57cbd-dedc-4929-a494-e739ea8a3c50
**Selected source take:** https://suno.com/song/878f89df-da5a-4f6f-9866-0d3e23cf1adb (v6-wild, Round 1)
**Local files:** `audio/Come a Little Closer, Moon (Master).wav` (24-bit/48 kHz), `… (Master).mp3` (320 kbps), `audio/source_878f89df.wav` (untouched download, not in git), `art/cover.png` (3000×3000)

## The collab brief
"Cartoon Villain's Sad Song" by @eight8eight; 600 credits; closes in about 13 days.

| Requirement | How the song meets it |
|---|---|
| New song: the Saturday-morning villain's sincere, heartbreaking ballad | A piano-and-strings ballad in his own voice |
| Original villain, named, with a named scheme | **Doctor Perigee** (Leonard). His scheme, the **Lunar Magnet**, pulls the moon toward Earth every Saturday at eight |
| Played straight, with at most one evil laugh | The single laugh is in the bridge: practised in a mirror "because a villain's supposed to have one" |
| Clean English, no real artists | No profanity. No artist names in the lyrics or the style prompt |
| Most sympathy wins | The scheme turns out to be love. His dying mother hung a paper moon over his bed and said "look up, I'll be watching". He ends the song switching the magnet off himself |
| Public + tag @eight8eight | **For you to do** on suno.com. The Suno tools can't change visibility, and I can't post to the collab |

The OP's specific request is the brief text itself; you confirmed this by pasting it.

**Research:**
- **The OP's taste:** @eight8eight's public profile lists industrial, lo-fi, nu metal, trap and cinematic. Their "Generations" album and their winning collab entry "One More Winter" are built on concrete objects, so the lyrics lean on those: the paper moon on fishing line, the lunchbox, the attic, Harbor Street.
- **Rival entries:** @barewolf (19 wins) took the loneliness/time-freeze angle, and @frank_dettmer took the 80s power ballad. This entry avoids both.

## Lyrics (final)
See the Suno song page or the generation prompt below. They're unchanged from the approved draft apart from one chorus line ("I just can't reach her from this place").

## Generation (2 of 8 authorised requests; 20 credits; no Max Mode)
**Style prompt:** Sincere 1970s piano ballad that slowly builds into lush strings, 72 BPM, minor-to-major heartbreak; warm grand piano, brushed drums entering in the second verse, swelling string section, a lone theremin answering the vocal hook like a distant moon, soft glockenspiel accents; warm weathered male baritone, close-mic and tender in the verses, cracking with grief on the final chorus; quiet spoken bridge with a single broken laugh; heartbreaking, nostalgic, intimate, restrained cinematic; solo piano intro, theremin-only fading outro

**Exclude:** comedy, novelty, parody, cartoon voice, 80s power ballad, rock guitar solo, EDM, trap, autotune, children's choir

**Settings:** male vocals, style influence 0.7, weirdness 0.4.

| Model | Take | Duration | BPM | Key | Tagger evidence |
|---|---|---|---|---|---|
| v6 | [dbb1692a](https://suno.com/song/dbb1692a-8fc1-46a5-bc05-0402b59a061c) | 4:04 | 67.5 | C min | piano 0.76, masculine 0.72; "blues" |
| v6 | [a63de7b0](https://suno.com/song/a63de7b0-a542-4148-9da0-93e7549aef3a) | 4:03 | 66.8 | C min | keyboard 0.71, piano 0.69; "techno" (odd; possibly reading the theremin or synth) |
| v6-wild | [37bd4ac9](https://suno.com/song/37bd4ac9-b489-414b-b275-4b7eeb1517bc) | 4:51 | 71.9 | B♭ maj | piano 0.70, masculine 0.71; all lyrics aligned |
| v6-wild | **[878f89df](https://suno.com/song/878f89df-da5a-4f6f-9866-0d3e23cf1adb) ← selected** | 3:50 | 69.8 | E♭ maj | **piano 0.78, masculine 0.75**, A/B/C/D section development; all lyrics aligned |

**Why I stopped after Round 1:**
- All four takes hit the core brief: a male-vocal piano ballad at 67–72 BPM.
- Both v6-wild takes I checked sang every line in order.
- No major gap showed in the evidence, and another blind round would only add takes I can't tell apart by ear.

**Model difference:**
- v6 landed in C minor, darker.
- v6-wild landed in major keys, closer to the "minor-to-major" brief, with a more developed structure.

## Why 878f89df
- **Strongest readings:** the strongest piano (0.78) and male vocal (0.75) of the four.
- **Structure:** the clearest development, with distinct intro, verse, chorus and bridge/final sections.
- **Lyrics:** every line is present in order.
- **Length:** 3:50, against 4:51 for the 72-BPM alternative.
- **Instrumentation:** Suno's description of the upload names "piano, strings, and percussion", which confirms the string section.

## Unverified (no listening was possible)
- **The evil laugh:** the lyric aligner skips non-word vocals. Between "supposed to have one" (160.7 s) and "Mother…" (168.2 s) there's a 7.5 s passage about 12 dB quieter than the song, with weak, intermittent, partly periodic bursts. It could be a soft, broken laugh or sparse piano. **Listen at 2:41–2:48 before submitting.** If the laugh is missing or sounds comic, use 37bd4ac9 instead, or ask me to try a targeted extend/cover of that section.
- **Theremin and glockenspiel:** not confirmed by any tag or description.
- **Vocal performance:** whether the voice actually cracks with grief is unverified, and that matters most for "most sympathy".

## Mastering
| | Source | Master |
|---|---|---|
| Format | WAV PCM16, 48 kHz, stereo | WAV PCM24, 48 kHz (+ MP3 320 kbps) |
| Duration | 229.88 s | 229.88 s |
| Integrated loudness | −17.16 LUFS | −16.00 LUFS |
| True peak | −2.75 dBTP | −1.50 dBTP |
| Loudness range (approx.) | 8.8 LU | 8.8 LU |
| Crest factor | 16.8 dB | 17.0 dB |
| L/R correlation | 0.882 | 0.882 |
| Clipped samples | 0 | 0 |

**Processing:** a 20 Hz subsonic high-pass (only −39.9 dB of energy below 25 Hz) plus +1.16 dB of gain. There's no EQ, compression or limiting.
- **Why −16 LUFS:** it's a common target for dynamic ballads, and it keeps the quiet bridge quiet and the true peak under −1 dBTP without a limiter.
- **Why not −14 LUFS:** that would need about 1.5 dB of limiting on a song whose emotional arc depends on dynamics.

## Artwork
`art/cover.png` is 3000×3000 and drawn in code: a folded paper crescent moon hangs on fishing line in a dark attic, while a red horseshoe magnet below points up at it, with field lines reaching for the moon. There's no text. **It isn't attached to Suno:** the Suno tools can't set cover art. Upload it from the song's edit menu.

## Suno upload checks
- ✔ Upload completed, status `complete`.
- ✔ Title is correct.
- ✔ Duration is 229.88 s, matching the master.
- ✔ It's in your library and private.
- ✔ Lyrics are replaced with the approved text, the laugh shown as "(Ha... ha ha... ha...)".
- ✘ Cover art isn't attached.
- ? Playback wasn't tested by ear.
- ? Community Collab eligibility wasn't checked; this needs your login.

## To submit (you)
1. Listen, especially the bridge laugh at 2:41–2:48.
2. Attach `art/cover.png`.
3. Set the song to **Public**.
4. Submit to the collab and tag **@eight8eight**, with this comment:

> Doctor Perigee — the Lunar Magnet. Every Saturday at eight he tried to pull the moon down, and every week the town thought he wanted a flood. He just wanted it close enough to see her face: his mother hung a paper moon over his bed and told him to look up when she was gone. One laugh, practised in a mirror, because a villain's supposed to have one. @eight8eight

## Credits
- Generation: 20 used (217 → 197).
- Downloads: 1 used (41 → 40).
- No purchases, deletions, publishing or submissions.
