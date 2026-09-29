# Implementation Evidence

Source: `source/index.html`

Observed implementation regions:

- `detectUnicode()` iterates `Array.from(text)` and classifies code points.
- `extractBigrams()` applies `text.toLowerCase().replace(/[^a-z]/g, '')`.
- `cosineSimilarity()` compares the derived bigram vector with profile vectors.
- `detectNgram()` retains one best profile and scales its score to a rounded percentage.
- `detectLanguage()` applies the Unicode rule, n-gram threshold, or English fallback.
- `speakText()` creates one `SpeechSynthesisUtterance` from the supplied text and language code.

These are implementation observations. They are not claims about accuracy or multilingual capability.
