# Initial Reciter Build Forensic Report

## Baseline preserved

**OBSERVED:** The available `/home/ubuntu/universal-language-reciter.zip` was preserved as `archive/reciter-baseline-v1.zip`. Its extracted `index.html` is byte-identical to the preserved current source. Source SHA-256: `795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27`.

## Source files preserved

**OBSERVED:** `source/index.html` is preserved without modification. The production file `/home/ubuntu/universal-language-reciter/index.html` was not edited by this forensic setup.

## Runtime/test evidence preserved

**EXECUTED:** A Node VM harness executed `detectUnicode`, `extractBigrams`, `cosineSimilarity`, `detectNgram`, and `detectLanguage` against four controlled inputs. Raw JSON is in `provenance/raw/runtime-trace.json`; the readable record is `evidence/runtime/TEST-RUNTIME-001.md`.

**UNVERIFIED:** Browser speech synthesis, voice enumeration, and actual UI interaction were not executed in this sandbox trace.

## Known failures preserved

**FAILED:** The first runtime harness attempt failed because of a malformed regular-expression literal. It is preserved at `evidence/failures/runtime-trace-first-run-failed.json`.

**FAILED:** The first component scanner falsely matched `Laya` inside `Malayalam`. That output is preserved at `evidence/failures/component-trace-first-run-false-positive.json`; the scanner was corrected to require whole component names.

## Current build state

**OBSERVED:** The project contains one HTML source file and no package manifest or declared build script in the inspected tree.

**IMPLEMENTED:** The HTML contains Unicode-script detection, ASCII-letter bigram profiling, cosine similarity, threshold/fallback classification, and one-utterance Web Speech API routing.

## Version/change history

**OBSERVED:** No Git metadata exists in the standalone Reciter project. The available ZIP timestamp and prior task record identify the preserved baseline as the first available build archive. See `CHANGELOG.md`.

## Provenance findings

**OBSERVED:** No direct import/API/function-call evidence for Laya, MAF, LHE, or CFHM was found in the current project scan after whole-name matching.

**UNKNOWN:** Absence of surviving project traces does not establish that a named component was never used elsewhere during the build.

**PARTIALLY SUPPORTED:** Frozen repositories exist under `/tmp/frozen-projects`, but the conservative whole-file source comparison did not establish an unchanged copy of the Reciter source.

## Missing evidence

**UNKNOWN:** Original build logs, browser runtime traces, external API/tool logs, and any version-control history outside the available sandbox were not available for this record.

## Assumptions not verified

No assumption is made that a named component was directly executed, installed, copied, or created by Manus merely because it appeared in an instruction or resembles part of the final implementation.
