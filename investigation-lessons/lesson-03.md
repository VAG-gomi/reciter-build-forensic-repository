# Lesson 3 — Script ≠ Language

**Status:** Established distinction  
**Central question:** Does identifying a writing system establish which language a text is written in?

## 1. The distinction

```text
SCRIPT:
Which writing system or script is represented?

LANGUAGE:
Which language is being expressed?
```

A script is a writing system. A language is the linguistic system expressed through text. One script can be used by multiple languages, so script identification alone does not settle language identification.

## 2. Examples

- Latin script is used by English, French, Spanish, German and many other languages.
- Arabic script is used for Arabic and for other languages that use Arabic-derived writing systems.
- Cyrillic is shared by multiple languages.
- Japanese text can combine several writing systems.

These examples show why a script label is useful evidence but not a complete language decision.

## 3. What Unicode can and cannot establish

Unicode assigns code points and provides character properties. A system can inspect those properties and use them to identify script-related evidence.

A simplified evidence path is:

```text
Unicode code points / character properties
                ↓
       script observations
                ↓
       language candidates
                ↓
       language-specific evidence
                ↓
        classification decision
```

**OBSERVED:** A code point belongs to a particular Unicode range or has a particular Unicode property.

**INFERRED:** The distribution of such code points may support a script candidate.

**NOT ESTABLISHED:** That the script candidate uniquely identifies the language.

Technical qualification: Unicode blocks and simple numeric ranges are not always identical to Unicode's Script property. Common and inherited characters, combining marks and scripts with multiple ranges need careful handling. A range-based detector is a heuristic, not a complete Unicode script-analysis implementation.

## 4. Language evidence beyond script

When multiple languages share a script, the system needs additional evidence. One possible source is recurring character sequences, such as:

- **Bigram:** a sequence of two adjacent characters.
- **Trigram:** a sequence of three adjacent characters.

A detector can compare observed sequence patterns with language profiles. This is language evidence, not proof that any particular text is correctly classified.

## 5. Confidence is not truth

A detector may report a high confidence value because its own rule or measurement strongly favours a candidate. That value does not automatically represent a calibrated probability that the candidate is correct.

```text
system confidence ≠ truth
script evidence    ≠ language proof
```

## 6. Principles

> Observed: Latin script. Not yet established: English.

> System confidence is not the same thing as truth.

## 7. What was established and what remains open

**ESTABLISHED:** Script identification and language identification are different tasks. Unicode evidence can contribute to script identification, while language classification requires further evidence when scripts are shared.

**UNKNOWN:** How much text is needed for reliable language evidence; how to calibrate candidate scores across languages; and how to handle mixed-script or shared-script multilingual input robustly.

**Next question:** Before extracting patterns, what should count as a unit of text?
