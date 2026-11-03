# Universal Language Reciter — Investigation Lessons

**Documentation edition:** 1.0  
**Prepared:** 2026-10-30  
**Scope:** Lessons 1–8  
**Purpose:** A structured account of the concepts, investigations, evidence boundaries and conclusions developed during the Reciter learning session.

## Contents

1. [Lesson 1 — Input → Interpretation → Output](lesson-01.md)
2. [Lesson 2 — Keyboard → IME → Input System](lesson-02.md)
3. [Lesson 3 — Script ≠ Language](lesson-03.md)
4. [Lesson 4 — Tokenisation](lesson-04.md)
5. [Lesson 5 — Tokens → Measurement](lesson-05.md)
6. [Lesson 6 — Measurement → Ranking → Decision](lesson-06.md)
7. [Lesson 7 — Evidence Quality & Representation Adequacy](lesson-07.md)
8. [Lesson 8 — Evidence Units & Multi-Resolution Representation](lesson-08.md)

## Editorial and evidence provenance

These files are a **consolidated editorial edition**, not a verbatim transcript of every lesson conversation.

- Lessons 1–7 were compiled from the archived `Universal_Language_Reciter_Lessons_1-7_Session_History.md` session-history document and checked against the technical repository where implementation or runtime claims were involved.
- Lesson 8 was compiled from the preserved Lesson 8 discussion and its investigation conclusions available in the current conversation context. The full verbatim Q1–Q60 exchange is not reproduced here; only its recorded outcome is summarised.
- The investigation's conceptual direction and conclusions are attributed to the user-led learning process. The organisation, explanatory wording and evidence cross-checks in this edition were prepared by ChatGPT. This is not a claim that every sentence is a verbatim statement by the user.
- A lesson's conceptual conclusion is not automatically an implementation fact. Technical claims must be checked against the linked source or runtime record.

## Evidence vocabulary

| Label | Meaning |
|---|---|
| **OBSERVED** | Directly visible in a source, record, output or supplied example. |
| **DERIVED** | A result obtained by applying a stated operation to observed material. |
| **INFERRED** | A conclusion supported by evidence but not stated directly by it. |
| **HYPOTHESIS** | A possibility or proposed design that still needs testing. |
| **UNKNOWN** | The available evidence does not settle the question. |
| **NOT ESTABLISHED** | The available evidence does not justify the proposed claim. |

For implementation tasks, keep these distinctions separate:

```text
implementation evidence
        ≠
executed runtime evidence
        ≠
experimental validation
        ≠
conceptual hypothesis
        ≠
final conclusion
```

## Technical evidence repository

The lessons are intentionally separate from the technical build repository. The technical repository states that it supplies evidence for the lessons but does not contain lesson conclusions.

- Repository: <https://github.com/VAG-gomi/reciter-build-forensic-repository>
- Frozen original source: <https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/source/index.html>
- Runtime trace: <https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/evidence/runtime/TEST-RUNTIME-001.md>
- Raw runtime trace: <https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/provenance/raw/runtime-trace.json>
- Public-state technical audit: <https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/reports/FINAL-PUBLIC-REPOSITORY-TECHNICAL-AUDIT-2026-10-22.md>
- Build-history interrogation: <https://github.com/VAG-gomi/reciter-build-forensic-repository/blob/main/history/RECITER-BUILD-HISTORY-INTERROGATION.md>

## Status of Lesson 8

Investigations 1 and 2 and the domain-transfer review are recorded as completed. Investigation 3 is preserved as the next proposed question, not as a completed finding. See [Lesson 8](lesson-08.md).

## Preservation rule

Do not silently turn an unknown into a negative finding, an inference into an observation, or an untested design proposal into an established architecture. Where records disagree, preserve the disagreement until it is reconciled.
