# Phase 1 — Build Forensic Record

## Role boundary

This is a technical record of the build as available in the Sandbox. It is not a lesson or interpretation document.

## OBSERVED

- The available Reciter project contains one production source file: `/home/ubuntu/universal-language-reciter/index.html`.
- The available build archive is `/home/ubuntu/universal-language-reciter.zip`.
- The archive contains one file, `index.html`.
- The extracted archive and current production source are byte-identical.
- The preserved source SHA-256 is recorded in `evidence/implementation/SHA256SUMS.txt`.
- The standalone production project has no Git metadata.

## IMPLEMENTED

- Preserved the source at `source/index.html`.
- Preserved the first available archive at `archive/reciter-baseline-v1.zip`.
- Preserved the extracted baseline at `archive/reciter-baseline/index.html`.
- Recorded source and environment metadata under `evidence/implementation/`.
- Recorded the implementation details used by the detector in `evidence/implementation/IMPLEMENTATION-001.md`.
- Recorded the factual build history in `CHANGELOG.md`.

## EXECUTED

- A Node VM trace executed the detector functions against controlled inputs.
- The readable runtime record is `evidence/runtime/TEST-RUNTIME-001.md`.
- The machine-readable result is `provenance/raw/runtime-trace.json`.

## FAILED

- The first runtime harness attempt failed because of an invalid regular-expression literal. The raw failure is preserved at `evidence/failures/runtime-trace-first-run-failed.json`.
- This failure belongs to the forensic harness, not to a changed Reciter production source.

## UNKNOWN

- Original build logs outside the available Sandbox are unavailable.
- Browser speech-synthesis execution was not captured by the Node trace.
- The absence of Git metadata means a source commit history for the standalone Reciter cannot be reconstructed from this project alone.

## Historical rule

Later interpretation must not rewrite the source or original runtime record. Any limitation discovered later is recorded as a later finding, not inserted into the baseline history.
