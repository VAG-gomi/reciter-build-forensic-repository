# Changelog

## Baseline record

- Version: `reciter-baseline-v1`
- Date: `2026-09-26` (archive file timestamp and prior build record)
- Changed: Preserved the available `index.html` and `universal-language-reciter.zip`.
- Reason explicitly given by developer: Build preservation/export request in task history.
- Files affected by this forensic setup: only this forensic repository; the production Reciter was not edited.
- Observed runtime difference: Not applicable; this setup is evidence collection.

## Current forensic setup

- Version: `forensic-initial`
- Date: `2026-09-29`
- Changed: Added source/archive/evidence directories and separate provenance tools.
- Reason explicitly given by developer: Preserve technical history and make provenance questions testable.
- Production source changed: No.

## Phase 1–3 corrective record

- Version: `forensic-phase-records`
- Date: `2026-09-29`
- Changed: Preserved the exact Phase 1–3 specification, added phase-by-phase technical records, added the missing forensic-tool validation record, and expanded runtime evidence to include the required reproducibility fields.
- Reason explicitly given by developer: Audit whether the GitHub repository contained the Phase 1–3 instructions, answers, and build records.
- Files affected: `specification/`, `phases/`, `evidence/tests/TEST-FORENSIC-001.md`, `evidence/runtime/TEST-RUNTIME-001.md`, `README.md`.
- Observed runtime difference: No production Reciter source or runtime behavior was changed.

## Final technical verification and freeze

- Version: `technical-freeze-2026-09-30`
- Date: `2026-09-30`
- Changed: Added the final technical audit report and exact freeze specification, preserved the first final-audit helper failure, preserved the pre-audit sandbox inventory, regenerated the current sandbox inventory, and removed an untracked Python cache.
- Reason explicitly given by developer: Verify, correct where technically necessary, document, and finalise the repository's technical sources, scripts, evidence, provenance records, and reproducibility state.
- Files affected: `reports/FINAL-TECHNICAL-AUDIT-2026-09-30.md`, `specification/FINAL-TECHNICAL-REPOSITORY-VERIFICATION-AND-FREEZE.md`, `evidence/failures/final-audit-source-extraction-first-run-failed.txt`, `evidence/failures/sandbox-inventory-before-final-audit.json`, `provenance/raw/sandbox-inventory.json`, `README.md`.
- Observed runtime difference: No production Reciter source, baseline archive, or historical commit was modified.

## Public repository technical audit

- Version: `public-audit-2026-10-22`
- Date: `2026-10-22`
- Changed: Added the current public-state audit and exact specification; clarified the v2 completion record's stale pre-commit draft wording; recorded the distinct `docs/index.html` v2 artifact, Git transition commits, public visibility, and disabled GitHub Pages state.
- Reason explicitly given by developer: Verify the current public repository, resolve documented inconsistencies where evidence permits, and preserve the baseline/v2 evidence boundary.
- Files affected: `COMPLETION-RECITER-V2-2026-10-22.md`, `reports/FINAL-PUBLIC-REPOSITORY-TECHNICAL-AUDIT-2026-10-22.md`, `specification/FINAL-PUBLIC-REPOSITORY-TECHNICAL-AUDIT-2026-10-22.md`, `README.md`, `CHANGELOG.md`.
- Observed runtime difference: No application source, original baseline, archive, prior failure record, or prior provenance record was modified.
- Prompt-injection warning disposition: The system warning was recorded as source/content UNKNOWN because no matching repository content was found and the detector trigger was not exposed; no historical evidence was deleted or rewritten.
