# Reciter completion — v2 draft record (2026-10-22)

**Status: DRAFT — not published, not pushed.** This record
and the v2 file were prepared while the repository-visibility
decision (make `VAG-gomi/reciter-build-forensic-repository`
public?) is pending with the owner. Nothing in the frozen
baseline was modified; no commit or push was made.

## Baseline (untouched)

- Frozen baseline: `source/index.html` (88 lines),
  SHA-256 `795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27`,
  frozen 2026-09-30. Archive `archive/reciter-baseline-v1.zip`
  unchanged. No file under `source/`, `archive/`,
  `evidence/`, `provenance/`, `reports/`, `specification/`,
  `phases/`, or `history/` was touched.

## v2 draft location (workspace only, for now)

- `workspace/reciter-v2/index.html` — single self-contained
  HTML file, derived from the baseline bytes.

## Changes in v2 (each tied to the approved fix list)

1. **Visible speech status line.** A `#speech-status` line
   under SPEAK shows errors and warnings to the user.
   `onerror` now writes "Speech error: …" there (baseline
   only logged to console). If `speechSynthesis` is
   absent, SPEAK stays disabled with "Speech is not
   supported in this browser." If no voices enumerate
   after the retry window, the status says so.
2. **Device-default voice option, always present.**
   The selector now always offers "Device default (uses
   detected language)". When no voice matches the
   detected language, the device default is used with
   the *detected* language tag, and a warning is shown
   ("No voice for this language on this device…").
   Baseline silently fell back to an unrelated voice and
   overwrote the language tag with that voice's language.
3. **Long-text chunking.** Text is split into sentence
   pieces (max ~180 chars, word-boundary splits for
   over-long sentences) and spoken as a queue; STOP
   cancels the whole queue. Baseline sent one utterance
   for any length.
4. **Method label corrected.** `detectLanguage` returns
   method `bigram-cosine` where baseline said
   `neural-ngram`. The classifier is bigram cosine
   similarity, not neural.

## Deliberately unchanged

- Language profiles, detection thresholds (95% / 60% /
  fallback 35%), Unicode script ranges, UI layout,
  Google Fonts reference, rate slider range.

## Checks run on v2 (2026-10-22, Node VM harness)

- `node --check` on the extracted script: PASS.
- Detection (unchanged logic, confirmed):
  - Bengali "আমি বাংলায় কথা বলছি" → bn-BD, 100%,
    unicode-rule.
  - Arabic sample → ar-SA, 100%, unicode-rule.
  - Short English sentence → English, 35%, fallback
    (bigram cosine below 60%).
  - Short Spanish sentence → English, 35%, fallback
    (same cause: short Latin-script samples often fall
    below the 60% bigram threshold).
- Chunking: 2250-char text → 50 chunks, max 44 chars,
  rejoined text byte-identical to input (modulo
  whitespace normalization).

## Observed baseline limitation (NOT fixed in v2 — out of scope)

Short Latin-script inputs frequently fall back to
English at 35% confidence because bigram cosine scores
stay under the 60% bar. This is baseline detector
behavior, unchanged in v2. Improving it (more profiles,
better short-text handling) is a separate proposal, not
part of this completion.

## v1 browser verification (completed 2026-10-22, read-only)

Run against the public mirror of the baseline file
after the owner confirmed making the repo public.
Page loaded (after the mirror's interstitial), title
and all controls rendered.

- Detection: Bengali "আমি বাংলায় কথা বলছি" →
  Bengali, bn-BD, 100%, unicode-rule, green dot
  (exactly as expected). English sample → English,
  en-US, 35%, fallback, red dot. Spanish sample →
  English, en-US, 35%, fallback, red dot (misdetected;
  same short-Latin-text limitation recorded above).
  Long text (~2000 chars) → English, 35%, fallback.
- Voices: ZERO named voices in this browser
  environment. The selector showed only "Device
  default" — no Bengali voice, no Arabic voice, no
  "Other voices" group.
- Speaking: every SPEAK click (English, Bengali,
  Spanish, long text incl. 30-second observation)
  silently did nothing — button stayed SPEAK, no
  audio, no page-visible error. Consistent with the
  browser environment exposing no usable speech
  engine; the app defect this proves is the silence
  (no error shown), not that speech is broken on
  every device.
- Bounds: pronunciation/audio quality NOT checked
  (no audio played); developer-console log NOT
  available through the browser tooling (page-visible
  errors only); a device with real TTS voices still
  needs a human-ear test.

## v2 change added after v1 verification (same day)

5. **Watchdog (8 seconds).** If an utterance neither
   starts nor errors within 8 seconds, v2 reports
   "Speech did not start — this device may have no
   speech voices" and resets, instead of sitting on
   STOP forever. Cancellation errors (`canceled` /
   `interrupted`, e.g. from STOP) are treated as
   silent stops, not failures. This covers the case
   the v1 test could not distinguish: a speech engine
   present but dead, where v2 without a watchdog
   would have stuck on STOP.

## Still outstanding

- Browser re-verification of v2 (same matrix, plus:
  SPEAK disabled with a reason when speech is
  unsupported; Device-default option present from
  the start; no-matching-voice warning for Bengali;
  watchdog behavior). For this, v2 is landed in the
  repo at `docs/index.html` (new file; baseline
  untouched) so the mirror can serve it — Pages NOT
  yet enabled; that is the publication step and comes
  only after v2 re-verification passes.
- Publication: `docs/index.html` + GitHub Pages (main
  branch, /docs), after v2 re-verification. The frozen
  baseline stays byte-identical throughout.

## AI approach (unchanged sequence)

TTS completion first; only then the joint AI steps
(J1 recitation-schedule world, J2 reciter features as
observations, J3 listener world) from
`CONNECTION-MAP-reciter-TBM.md`. None authorized yet.

## v2 browser verification (completed 2026-10-22, read-only)

Run against the public mirror of `docs/index.html`.

- Status line: CONFIRMED present. Initial warning
  "No voices found on this device — speech may be
  unavailable." Every SPEAK attempt then showed
  "Speech error: synthesis-failed" visibly. The app
  no longer fails silently — this was the core fix
  and it is verified.
- Device-default option: CONFIRMED present from the
  start. Voice enumeration: 1 option only (Device
  default); no Bengali, no Arabic voice in this
  browser environment.
- Language-specific no-matching-voice warning: NOT
  TRIGGERED, correctly — with zero voices present,
  the generic "No voices found" warning is the right
  message; the language-specific branch only fires
  when voices exist but none match. That branch still
  needs a voices-present-but-no-match environment.
- SPEAK behavior: button never stuck on STOP;
  every attempt errored immediately (synthesis-failed).
  Watchdog: NOT TRIGGERED, correctly — no utterance
  hung without starting or erroring, so there was
  nothing for the watchdog to catch. The watchdog path
  itself remains unverified (needs a hanging engine).
- Chunk queue: NOT VERIFIABLE here — speech never
  started, so no chunk could play.
- Detection unchanged from v1: Bengali bn-BD 100%
  unicode-rule; English fallback 35%; Spanish
  misdetected as English fallback 35% (known
  short-Latin-text limitation, out of scope).
- Bounds (unchanged): pronunciation unverified;
  console log unavailable through browser tooling;
  voiced-device test still needed.

## Publication (2026-10-22)

- GitHub Pages enabled: source main branch, /docs
  folder, HTTPS enforced, site public.
- Live URL: https://vag-gomi.github.io/reciter-build-forensic-repository/
- Verified after build: pages status `built`,
  live URL HTTP 200, served content contains v2
  markers (speech-status, Device default,
  bigram-cosine).
- Frozen baseline untouched throughout
  (source/index.html SHA-256 unchanged).

## Still needs a voiced device (user's ear)

- Pronunciation correctness per language.
- Chunk-queue behavior on long text with real speech.
- Watchdog behavior on a hanging engine.
- Language-specific warning (voices present, no
  Bengali voice).
Once the voiced-device test passes, the TTS-first
sequence is complete and the AI approach (J1/J2/J3)
can be ruled on.
