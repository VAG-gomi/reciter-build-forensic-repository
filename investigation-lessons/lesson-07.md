# Lesson 7 — Evidence Quality & Representation Adequacy

**Status:** Four investigations recorded; representation requirements established with a technical-record caveat  
**Central question:** What makes evidence strong enough for the question the system must answer, and what information must its representation preserve?

## 1. Investigation 1 — Can a high score still be weak evidence?

A high similarity score does not automatically mean that the evidence is strong.

Illustrative comparison used in the lesson:

```text
A: short input   → candidate similarity 0.91
B: longer input  → candidate similarity 0.72
```

The short input has the larger score. The longer input may provide more characters, patterns, feature coverage and opportunities to discriminate between candidates. However, length alone does not prove stronger evidence either.

**Principle:**

> Score magnitude and evidence strength are different properties.

Evidence quality must consider more than the top score, including the amount and coverage of usable evidence and whether the result is stable.

## 2. Investigation 2 — Can a strong score fail to discriminate?

A candidate can have a high score while very similar alternatives score almost as highly.

Illustrative example:

```text
Spanish = 0.72
French  = 0.71
Italian = 0.70
English = 0.31
```

The top-two margin is:

```text
0.72 - 0.71 = 0.01
```

The leading candidate ranks first, but the margin shows weak separation from the runner-up.

Useful evidence therefore includes:

```text
top score
+
runner-up score
+
top-two margin
```

**Principle:**

> A high absolute score does not guarantee strong discrimination.

The values above are an explanatory example, not a runtime record.

## 3. Investigation 3 — Where does evidence disappear?

The lesson examined the multilingual input:

```text
Hello my friend.
مرحبا يا صديقي.
Bonjour mon ami.
```

### Stage 1 — Raw input

The original input is available to the application at the start of processing.

### Stage 2 — Unicode observation

The baseline's `detectUnicode()` counts code points by configured ranges and returns a dominant-script summary. A single dominant-script result does not preserve a full map of where each script occurs or distinguish English from French when both use Latin script.

### Stage 3 — N-gram preprocessing

The baseline's extractor is:

```javascript
text.toLowerCase().replace(/[^a-z]/g, '')
```

This removes Arabic letters, spaces, punctuation and line breaks from the string passed to the n-gram measurement. The surviving ASCII letters are combined into one sequence. Consequently, letters from originally separate portions can become adjacent in the reduced sequence.

For the intended line-separated input, the simplified source-level result would be:

```text
hellomyfriendbonjourmonami
```

This is a derivation from the preprocessing rule, not a claim that every stored runtime fixture was encoded exactly as shown.

### Stage 4 — Bigram representation

The implementation creates one global bigram-frequency vector. That vector no longer carries the removed Arabic letters, original word boundaries, source line boundaries or a location map for local language spans.

### Stage 5 — Ranking and final decision

The implementation retains the highest-scoring language profile. If the best n-gram score does not meet the acceptance threshold, `detectLanguage()` returns the fixed English fallback rather than an accepted language classification.

The runtime record for the mixed-script example reports:

```text
Unicode:  confidence 67, no language code, script latin
N-gram:   confidence 22, candidate en-US
Final:    confidence 35, en-US, method fallback
```

These values are reported as the contents of `evidence/runtime/TEST-RUNTIME-001.md`, not as proof that the example represents a general multilingual accuracy test.

### Important forensic caveat: fixture encoding and score discrepancy

The technical repository contains both a human-readable runtime record and a raw JSON runtime trace. In the human-readable record, the third input is displayed as three lines. In the raw JSON file, the input field is encoded with `\\n` sequences. As stored, that representation may indicate literal backslash-plus-`n` characters rather than actual newline characters. The available records do not fully reconcile this difference.

The earlier session-history summary also records a more detailed score vector, including an English similarity of approximately `0.2313`, while the runtime record reports an n-gram confidence of `22`. Under the source's `Math.round(bestScore * 100)` conversion, a value of `0.2313` would round to `23`, not `22`. These figures are therefore not treated as one reconciled runtime result in this edition.

**Disposition:** The exact fixture encoding and exact score vector remain **UNKNOWN / UNRECONCILED**. The source-level information-loss finding does not depend on selecting one of those disputed numbers: the preprocessing expression itself removes the characters and boundaries described above.

### Information-loss principle

> A measurement cannot recover information that its input representation no longer contains.

Qualification: the original raw text may still exist elsewhere in application memory. The narrower claim is that a downstream stage cannot use information that has been removed from the representation supplied to that stage.

## 4. Investigation 4 — What must an evidence representation preserve?

If multilingual detection is required, the representation must preserve enough information to answer:

```text
What languages may be present?
Where do they occur?
How much usable evidence supports each candidate?
How strong are competing candidates?
How stable or reliable is the result?
What remains uncertain?
```

A minimum conceptual evidence representation therefore needs:

```text
original content / lossless access
+
position / offsets
+
boundary information and provenance
+
script evidence
+
local candidate language evidence
+
local measurements
+
ranking and competing candidates
+
score margins
+
feature coverage
+
stability information where claimed
+
acceptance / decision-grade status
+
uncertainty / fallback state
+
provenance
+
TTS routing metadata where required
```

This is a representation requirement, not an implementation specification. It does not dictate a particular database, data structure, segmentation algorithm or model.

## 5. Source boundaries are not language boundaries

A source boundary is directly present in the input, such as a newline, punctuation mark or known document boundary.

A language boundary is a classification claim, such as:

```text
English → Arabic
```

That boundary may be inferred from evidence. A newline is not automatically a language boundary, and a language change does not have to coincide with a newline.

Preserve the observed source boundary and record any inferred language boundary separately.

## 6. Strictly necessary versus conditional information

| Information | General language detection | Multilingual detection | Multilingual TTS |
|---|---|---|---|
| Original content or lossless access | Yes | Yes | Yes |
| Script observations | Useful | Yes | Yes |
| One global score | Sometimes sufficient | Not sufficient by itself | Not sufficient by itself |
| Span offsets | Not always | Required for locating spans | Required for routing spans |
| Boundary provenance | Useful | Required at some level | Required |
| Multiple candidate scores | Useful | Yes | Yes |
| Score margin | Useful | Strongly recommended | Strongly recommended |
| Feature coverage | Useful | Needed for quality assessment | Needed for quality assessment |
| Local measurements | Not always | Yes | Yes |
| Language proportions | Not required unless claimed | Only if proportions are claimed | Useful where relevant |
| Stability | Depends on the claim | Strongly recommended | Strongly recommended |
| Unknown / fallback state | Yes for robust systems | Yes | Yes |
| Voice metadata | No | No | Yes |
| Decision provenance | Useful | Strongly recommended | Strongly recommended |

## 7. Evidence classification

### OBSERVED in the baseline source

- The textarea's text is passed to a whole-input detection function.
- `detectUnicode()` returns a dominant-script summary rather than a position-indexed multilingual map.
- `extractBigrams()` removes every character outside ASCII `a–z`.
- The n-gram stage creates one global bigram vector.
- The detector retains a winning profile and then applies an acceptance threshold or fallback.
- The speech function receives the full text and one language code for a single utterance.

### DERIVED from the source operations

- Arabic characters are not represented in the ASCII bigram vector.
- Original spaces and line breaks are not available as boundaries in that vector.
- A single aggregate vector cannot reconstruct the original positions of the removed characters.
- A single winning label cannot itself describe a document's internal language composition.

### INFERRED

- Multilingual detection needs local evidence and location, not only a whole-input winner.
- A global score is an aggregate summary, not a complete multilingual description.
- The representation must be designed around the question the system is expected to answer.

### HYPOTHESIS

- Hierarchical, nested, local-window or adaptive representations may be useful.
- Segment-level margins and stability measures may improve decision quality.
- Preserved local evidence may support multilingual text-to-speech routing.

### UNKNOWN

- Best segmentation granularity.
- Minimum reliable span length.
- Cross-language score calibration.
- The appropriate stability measure.
- Reliability of browser voice switching across spans.
- Whether language proportions can be accurately estimated from the current profiles.

## 8. Precise attribution of the design limitation

The investigation exposed a representation-level limitation in the original Reciter design/specification for the multilingual requirement.

It did **not** establish that:

- Manus implemented the system incorrectly;
- the current classifier is useless for every whole-input task;
- the entire Reciter architecture is invalid;
- one particular future segmentation architecture has already been proven correct.

The narrower finding is:

```text
current representation
       ↓
can support some whole-input similarity experiments
       ↓
but does not preserve enough structure for multilingual localisation
```

## 9. Major lesson principle

> **Preserve the evidence at the same structural level as the question the system must answer.**

A global vector may be adequate for the question “Which profile best matches this whole input?” It is not adequate by itself for “Which languages occur, where do they occur, and how should each portion be spoken?”

## 10. Technical references

- [Frozen baseline source](https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/source/index.html)
- [Recorded runtime trace](https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/evidence/runtime/TEST-RUNTIME-001.md)
- [Raw runtime trace JSON](https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/provenance/raw/runtime-trace.json)
- [Final public technical audit](https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/reports/FINAL-PUBLIC-REPOSITORY-TECHNICAL-AUDIT-2026-10-22.md)

## 11. Next question

How should the evidence be represented so that one preserved source can support more than one level of analysis without losing the relationship between a measurement and its original location?
