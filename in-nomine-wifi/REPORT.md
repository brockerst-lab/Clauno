# In Nomine Wi-Fi — production report

**Final Suno upload (private):** https://suno.com/song/b3dacf27-b83e-451d-858b-ecad369b3703
**Selected source take:** https://suno.com/song/c1f9974d-3432-4fac-a6e8-c6b3fdd9b2a9 (v6, Round 1)
**Local files:** `audio/In Nomine Wi-Fi (Master).wav` (24-bit/48 kHz), `audio/In Nomine Wi-Fi (Master).mp3` (320 kbps), `art/cover.png` (3000×3000). The source WAV is kept locally only.

## Brief
"Triple-Genre Collision #15 — In Nomine Wi-Fi" by @monelo777.
- **Title:** must be exactly "In Nomine Wi-Fi", and the exact phrase must be in the lyrics.
- **Fusion:** Gregorian chant × illbient × downtempo as one sound, all three audible, no separate sections.
- **Vocal:** Gregorian chant must be the lead vocal style, never just a background choir.

## Research: what the judge rewards
From the winning prompts in "Triple genre collision winners", including #14 "Nobody Lives Upstairs" by @eight8eight, which beat our entry:
- **Exact numbers:** a precise BPM and key.
- **A persistent glue element:** one element running "from first bar to last".
- **Exact vocal placement.**
- **Sound effects tied to the story.**
- **Exclusions written into the style itself,** mirroring the brief's rules (e.g. "‑separate interlude").
- **Concrete details in the lyrics,** with the title phrase anchoring a short chorus.

## Rubric (100 = perfect finished song)
| # | Dimension | Weight | Draft v1 | Draft v2 | Finished (with audio evidence) |
|---|---|---|---|---|---|
| 1 | Brief compliance | 10 | 9.5 | 9.5 | **10**: title exact; phrase intelligible |
| 2 | Gregorian chant as lead | 20 | 13 | 17 | **18**: listener says "solo, low-register cantor with modal, melismatic plainchant phrasing… the chant itself leads"; supporting choir-like layers appear |
| 3 | Three-genre fusion, all at once | 20 | 14 | 17 | **18**: illbient 9/10, downtempo 8/10, chant 9/10, all at once |
| 4 | Concept and lyric craft | 15 | 12 | 13 | **12**: most punchlines intelligible, but "Password Dei" is garbled and the final "Amen" unconfirmed |
| 5 | Signature hook / sonic identity | 10 | 7 | 9 | **8**: modem handshake audible at 1:22–1:33 (once, not recurring); "In Nomine Wi-Fi" hook is clear |
| 6 | Arrangement and arc | 10 | 6 | 8 | **9**: the beat drops out in the bridge and returns as designed |
| 7 | Production and mix | 10 | 6 | 7 | **8**: "no major mud or buried lead"; possible slight level change around the spoken bridge |
| 8 | Atmosphere and impact | 5 | 4 | 4 | **4** (assumed: the listener can't judge humour) |
| | **Total** | | **≈72** | **≈85** | **≈87** |

The finished scores combine Suno's listening-agent answers with my own measurements. Nothing was heard by a person.

## Generation (2 of 8 requests; 20 credits; no Max Mode)
**Style:** Gregorian chant illbient downtempo fusion, 76 BPM, D Dorian; solo male cantor sings Latin plainchant as the lead vocal from first bar to last, monophonic, on a reciting tone with long melismas, upfront and intelligible with a short stone-chapel reverb, schola answers only on responses; dark illbient bed: deep dub sub-bass, dub echo throws on the cantor's final syllables, turntable scratches, night-city field recordings, dark drone, dial-up modem bursts; dusty slow broken breakbeat and detuned Rhodes, steady throughout; hypnotic, solemn, nocturnal, one cohesive sound

**Exclude:** background choir, pop vocals, chillout, lounge, EDM, separate interlude, fast tempo

**Settings:** male vocals, style influence 0.7, weirdness 0.45.

Listening-agent scores per take:

| Take | Model | Chant lead | Illbient | Downtempo | Chant | All at once | Bridge drop-out | Overall | Notes |
|---|---|---|---|---|---|---|---|---|---|
| [fd45e0be](https://suno.com/song/fd45e0be-14ec-4c1d-bf9e-d06750f15210) | v6 | ✔ | 8 | 8 | 9 | ✔ | ✔ | 8 | Bright effects compete with the vocal; beat re-entry is loud |
| **[c1f9974d](https://suno.com/song/c1f9974d-3432-4fac-a6e8-c6b3fdd9b2a9)** | **v6** | ✔ | **9** | 8 | 9 | ✔ | ✔ | **9** | No major mix issues |
| [68e587ba](https://suno.com/song/68e587ba-af64-454d-9e83-c34835323002) | v6-wild | ✔ | 7 | 8 | 8 | ✔ | ✔ | 8 | Dub and scratch elements are weaker; heavy reverb |
| [6c6dad76](https://suno.com/song/6c6dad76-584b-4416-963c-e8f60d9baa53) | v6-wild | ✔ (choir in refrains) | 8 | 8 | 9 | ✔ | ✔ | 8 | Expands into a choir in the refrains, a risk for the lead-chant rule |

**Why I stopped after Round 1:** every take met the brief, and c1f9974d scored highest with no major gap.

**Model difference:** both v6 takes led with a solo cantor more consistently. The v6-wild takes thickened into a choir or relied on heavier reverb.

## Mastering
| | Source | Master |
|---|---|---|
| Format | WAV PCM16, 48 kHz | WAV PCM24, 48 kHz (+ MP3 320 kbps) |
| Duration | 231.56 s | 231.56 s |
| Integrated loudness | −14.5 LUFS | −14.0 LUFS |
| True peak | −3.59 dBTP | −3.03 dBTP |
| Loudness range | 5.3 LU | 5.3 LU |
| Crest factor | 12.1 dB | 12.2 dB |
| L/R correlation | 0.805 | 0.803 |
| Clipped samples | 0 | 0 |

**Processing:** a 16 Hz zero-phase subsonic high-pass plus +0.53 dB of gain.
- **Why 16 Hz rather than the usual 20 Hz:** the dub sub-bass puts real energy at 25–40 Hz (−8.1 dB relative to the whole mix), so a lower cutoff keeps it intact. Below 25 Hz there's only −34 dB.
- **No EQ, compression or limiting.**
- **Change check:** after matching levels, the master differs from the source by only −33.7 dB of residual.

## Suno upload checks
- ✔ Upload completed, status `complete`.
- ✔ Title is "In Nomine Wi-Fi".
- ✔ Duration is 231.56 s, matching the master.
- ✔ It's in your library and private.
- ✔ Lyrics are replaced with the clean approved text. Suno's transcription had "panth with vobiscum", "Mather's letter" and "Resurrectsit".
- ✘ Cover art isn't attached; the tools can't set it. Upload `art/cover.png` from the song's edit menu.

## To submit (you)
1. Listen to the upload.
2. Attach the cover.
3. Set it to public.
4. Submit it to Collision #15, with this comment:

> In Nomine Wi-Fi — a solo cantor sings the evening office to a blinking router. Latin plainchant leads from first bar to last over a dub-heavy illbient bed (modem handshakes, scratches, night-city noise) and a slow downtempo break. "Dominus bandwidth vobiscum / Et cum signal tuo." Turn it off and on again — Resurrexit.

## Credits
- Generation: 20 used.
- Downloads: 1 used.
- No purchases, publishing or submissions.
