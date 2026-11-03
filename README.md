# Reciter Build Forensic Repository

This repository is a technical record of the Universal Language Reciter build. It separates source, runtime evidence, failures, implementation details, and later provenance investigations.

## Phase records

- `specification/RECITER-BUILD-FORENSIC-SPECIFICATION.md` preserves the exact Phase 1–3 instruction attachment.
- `phases/PHASE-1-BUILD-FORENSIC-RECORD.md` records the Phase 1 build/source/runtime work.
- `phases/PHASE-2-BUILD-PROVENANCE-RECORD.md` records the Phase 2 provenance investigation.
- `phases/PHASE-3-FORENSIC-TOOLSET-RECORD.md` records the Phase 3 toolset and outputs.
- `history/RECITER-BUILD-HISTORY-INTERROGATION.md` records the build and source history account.
- `history/MANUS-REPOSITORY-CREATION-FORENSIC-INTERROGATION.md` records how this Git/GitHub repository was created.
- `specification/MANUS-REPOSITORY-CREATION-FORENSIC-INTERROGATION.md` preserves that interrogation specification.
- `reports/FINAL-TECHNICAL-AUDIT-2026-09-30.md` records the final technical verification and freeze status.
- `specification/FINAL-TECHNICAL-REPOSITORY-VERIFICATION-AND-FREEZE.md` preserves the exact final-freeze specification.
- `reports/FINAL-PUBLIC-REPOSITORY-TECHNICAL-AUDIT-2026-10-22.md` records the current public-state audit and baseline/v2 clarification.
- `specification/FINAL-PUBLIC-REPOSITORY-TECHNICAL-AUDIT-2026-10-22.md` preserves the exact public-repository audit specification.

## Evidence boundary

- `source/` preserves the current source as observed.
- `archive/` preserves the available baseline ZIP and its extracted source.
- `evidence/runtime/` contains executed runtime records.
- `evidence/tests/` contains forensic-tool reproducibility checks.
- `evidence/failures/` contains failed or corrected investigative attempts.
- `evidence/implementation/` contains source and environment records.
- `tools/provenance/` contains separate investigation utilities. They are not Reciter production code.
- `provenance/raw/` contains machine-readable tool output.
- `provenance/reports/` contains summaries of those outputs.

The repository's Phase 1 specification assigns lesson conclusions to the separate investigation layer. The documentation branch proposed for this recovery carries a clearly labelled reference copy for discovery; it does not convert lesson prose into technical evidence or alter the frozen implementation record.

## Investigation lesson reference copy

The consolidated Universal Language Reciter lessons 1–8 are organised under [`investigation-lessons/`](investigation-lessons/README.md). These documents are an editorial learning record, not verbatim transcripts and not a substitute for source/runtime evidence.

- [Lesson index and editorial provenance](investigation-lessons/README.md)
- [Lesson 1 — Input → Interpretation → Output](investigation-lessons/lesson-01.md)
- [Lesson 2 — Keyboard → IME → Input System](investigation-lessons/lesson-02.md)
- [Lesson 3 — Script ≠ Language](investigation-lessons/lesson-03.md)
- [Lesson 4 — Tokenisation](investigation-lessons/lesson-04.md)
- [Lesson 5 — Tokens → Measurement](investigation-lessons/lesson-05.md)
- [Lesson 6 — Measurement → Ranking → Decision](investigation-lessons/lesson-06.md)
- [Lesson 7 — Evidence Quality & Representation Adequacy](investigation-lessons/lesson-07.md)
- [Lesson 8 — Evidence Units & Multi-Resolution Representation](investigation-lessons/lesson-08.md)

**Preservation boundary:** Lesson 7's fixture-encoding and score discrepancy remains `UNKNOWN / UNRECONCILED`. Lesson 8 Investigation 3 remains proposed and open. No lesson authorises a source redesign or implementation change.

Unknown provenance is retained as `UNKNOWN`; a textual component name is not treated as execution evidence.
