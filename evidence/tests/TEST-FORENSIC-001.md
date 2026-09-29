# TEST-FORENSIC-001 — Forensic Repository Validation

Test ID: `TEST-FORENSIC-001`
Date: `2026-09-29`
Build/version: `forensic-initial`
Execution method: shell, Python, JSON parser, Git, ZIP integrity tools
Expected behaviour: not previously specified

## Executed checks

- `python3 -m py_compile tools/provenance/forensic.py`
- Forensic CLI execution against the available project
- JSON parsing of every generated raw result and provenance map
- Byte comparison of preserved source, extracted baseline, and available archive contents
- ZIP integrity test of the packaged forensic repository
- Git working-tree and remote synchronization checks

## Actual output

- Python compilation: completed without an error.
- Raw JSON parsing: completed without an error.
- Source SHA-256 remained `795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27`.
- Baseline/source byte comparison: equal.
- Package ZIP integrity test: passed for the archive produced by the packaging command.
- Git branch state: `main` synchronized with `origin/main` at the initial commit before this corrective record.

## Errors and warnings

- The first runtime harness failure is preserved separately in `evidence/failures/runtime-trace-first-run-failed.json`.
- The first component scanner false positive is preserved separately in `evidence/failures/component-trace-first-run-false-positive.json`.
- Browser speech synthesis was not tested.

## Relevant files and functions

- `source/index.html`
- `tools/provenance/forensic.py`
- `detectUnicode()`
- `extractBigrams()`
- `cosineSimilarity()`
- `detectNgram()`
- `detectLanguage()`
- `speakText()`

## Exit/status

`EXECUTED` for the listed checks. This record does not certify Reciter accuracy or browser speech behaviour.
