# Lesson 5 — Tokens → Measurement

**Status:** Established from source inspection and the recorded implementation  
**Central question:** What does the current Reciter actually measure from its input?

## 1. The implementation became the object of study

The investigation moved from general input concepts to the original Reciter implementation. The central feature-extraction operation in the preserved baseline is:

```javascript
text.toLowerCase().replace(/[^a-z]/g, '')
```

This transforms the input before bigram measurement.

## 2. What the expression does

- Converts the text to lowercase.
- Retains only the ASCII lowercase letters `a` through `z`.
- Removes every other character from the string used for this measurement.

It does not preserve all Unicode letters. It also removes spaces, punctuation, digits, line breaks and letters outside the ASCII `a–z` range.

## 3. Simple examples

### Example A

Input:

```text
hello!
```

Cleaned representation:

```text
hello
```

Bigrams:

```text
he  el  ll  lo
```

Each bigram occurs once. With four total bigrams, each has a normalised frequency of `0.25`.

### Example B

Input:

```text
café
```

Cleaned representation:

```text
caf
```

Bigrams:

```text
ca  af
```

The `é` does not contribute to this feature representation.

## 4. What is measured

The extractor builds a frequency vector of adjacent two-letter sequences. A count is divided by the total number of bigrams, producing relative frequencies.

For a cleaned string with length `n`, the number of overlapping bigram positions is `n - 1`, provided `n` is at least two.

```text
cleaned sequence
      ↓
adjacent character pairs
      ↓
frequency counts
      ↓
normalised bigram vector
```

## 5. Cosine similarity

The Reciter compares the observed bigram vector with stored language-profile vectors using cosine similarity:

```text
similarity(A, B) = (A · B) / (||A|| × ||B||)
```

In this operation:

- the dot product rewards overlap between observed and profile features;
- absent profile bigrams contribute nothing to the dot product;
- vector magnitudes affect the normalisation;
- the result measures alignment between two vectors.

The resulting value is a similarity measurement. It is not automatically a probability, a calibrated confidence or a verified language truth.

## 6. The information-loss principle

> What is excluded from the representation cannot contribute to that measurement.

This is a statement about the measurement input. It does not mean the original textarea value has necessarily been deleted from the application. The original text may remain available elsewhere, while the feature extractor receives a reduced representation.

## 7. Evidence classification

**OBSERVED in source:** The extractor lowercases text and removes every character outside `[a-z]` before generating bigrams.

**DERIVED:** Accented letters outside the accepted range, Arabic letters, spaces, punctuation and line breaks do not contribute directly to the resulting bigram vector.

**INFERRED:** A measurement based only on this vector cannot distinguish information that was removed before the vector was built.

**NOT ESTABLISHED:** That this feature representation is sufficient for all supported languages, or that the language profiles produce reliable real-world accuracy.

## 8. Principle

The feature extractor defines the alphabet and sequence that the measurement stage can observe. Measurement quality is constrained by that representation.

**Next question:** Does the highest measured score automatically become the final language decision?

## 9. Technical source

The implementation is preserved in the technical repository at [`source/index.html`](https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/source/index.html). The source hash and baseline status are recorded in the public technical audit.
