# Final Technical Repository Verification and Freeze

Audit date: `2026-09-30`

Scope: technical verification only. No Lesson 1–8 conclusions are written here, and no research interpretation is added.

## A. Repository status

**OBSERVED:** The repository is internally coherent for the available evidence baseline. It has one Git branch, `main`, tracking one remote, `origin`, at `https://github.com/VAG-gomi/reciter-build-forensic-repository.git`. The working tree was clean before this audit.

**OBSERVED:** The repository contains source, baseline/archive, runtime evidence, tests, failures, implementation records, provenance JSON, provenance reports, phase records, history records, specifications, and the forensic tool.

**OBSERVED:** No `lesson-*.md` files, `lessons/` directory, or `examinations/` directory is present. This preserves the requested technical/research separation.

**OBSERVED:** No likely secret token, private-key block, or API-key pattern was found in the tracked text scan. Git author metadata contains the configured public noreply email `manus@users.noreply.github.com`; this is metadata, not a credential.

**ISSUES FOUND AND HANDLED:**

1. An untracked `tools/provenance/__pycache__/` cache existed in the Sandbox. It was removed and is excluded by `.gitignore`; it was never tracked.
2. The regenerated sandbox inventory changed because the repository had gained later phase/history files and the final-audit failure record. The previous committed inventory was preserved as `evidence/failures/sandbox-inventory-before-final-audit.json`, and the regenerated current inventory is retained as `provenance/raw/sandbox-inventory.json`.
3. The first final-audit JavaScript extraction helper used an incorrectly escaped regex and failed. That audit-helper failure is preserved at `evidence/failures/final-audit-source-extraction-first-run-failed.txt`. The corrected check succeeded.
4. Several evidence records intentionally contain absolute historical Sandbox paths such as `/home/ubuntu/...` and `/tmp/frozen-projects`. These are provenance references, not broken repository links; they are non-portable outside the original environment and are recorded as a limitation.
5. `provenance/provenance-map.json` and `provenance/raw/provenance-map.json` are intentionally duplicated roles: one canonical top-level map and one raw tool output. They are not treated as independent evidence.

## B. Source status

**OBSERVED:** The preserved Reciter baseline source is:

```text
source/index.html
```

The extracted archive copy is:

```text
archive/reciter-baseline/index.html
```

The original archive is:

```text
archive/reciter-baseline-v1.zip
```

**OBSERVED:** `source/index.html` and `archive/reciter-baseline/index.html` are byte-identical.

**OBSERVED:** Source SHA-256:

```text
795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27
```

**OBSERVED:** Baseline ZIP SHA-256:

```text
58eef85c4ae3e5b0501e9934f0c29be81925590ef69344b60effe218ab9136f5
```

**EXECUTED:** The JavaScript body extracted from the preserved source passed `node --check`.

**EXECUTED:** A Chromium headless load produced a DOM containing the expected Reciter title. Chromium emitted one environment DBus warning about unavailable UPower; no source syntax failure was recorded.

**IMPLEMENTATION EVIDENCE:** The source contains Unicode script detection, ASCII-letter bigram extraction, language profile literals, cosine similarity, n-gram winner selection, confidence/fallback handling, Web Speech API routing, textarea input handling, speed handling, and speak-button handling.

**NOT VERIFIED:** Full HTML validity by a standards validator was not performed because `tidy` was unavailable. Browser speech synthesis, actual voice enumeration, and pronunciation were not verified.

**DEFECT RECORDING RULE:** No source redesign or algorithm correction was made. Any limitations remain in the preserved baseline and are documented as observations or unverified behavior.

## C. Tool status

| Tool | Purpose | Inputs | Outputs | Dependencies | Execution status | Known limitations | Source |
|---|---|---|---|---|---|---|---|
| `forensic.py` | Generate provenance, inventory, baseline, runtime, and build records | Reciter project, preserved source/archive, available frozen checkouts | JSON files under `provenance/raw/` and provenance map | Python standard library; Node.js for embedded runtime harness | **REPRODUCED**; corrected run returned runtime `EXECUTED` | Uses fixed Sandbox paths; absence of evidence is not proof of absence | `tools/provenance/forensic.py` |
| Embedded Node VM harness | Execute existing Reciter JavaScript functions without browser speech | Preserved `source/index.html`; four controlled inputs | `provenance/raw/runtime-trace.json` | Node.js VM module; minimal mocked DOM | **REPRODUCED** | Does not test actual browser UI or speech synthesis | Embedded in `forensic.py` |
| Static source checks | Verify source structure and implementation regions | `source/index.html` | Terminal check results | Python, Node.js | **REPRODUCED** | Not a full HTML standards validation | Audit command, not repository production code |
| Chromium headless load | Check practical browser parsing/DOM load | `file://source/index.html` | Dumped DOM and stderr | Chromium | **PARTIALLY REPRODUCED** | No speech/voice test; environment DBus warning | Audit command, not repository production code |
| Git/ZIP/hash checks | Verify repository and baseline integrity | Git tree, source, archive | Status, hashes, ZIP test output | Git, unzip, sha256sum | **REPRODUCED** | Only available local/remote state is observable | Audit commands |

The temporary Node runner and temporary extracted source used by the embedded harness are intentionally deleted after execution. Their existence and execution are preserved by the runtime JSON, the forensic tool source, and the failure records.

## D. Evidence status

### IMPLEMENTATION EVIDENCE

The source file itself establishes the functions, literal language profiles, source cleaning expression, cosine computation, fallback branch, TTS calls, and event handlers. `evidence/implementation/IMPLEMENTATION-001.md` records these locations and distinctions.

### EXPERIMENTAL/RUNTIME EVIDENCE

`evidence/runtime/TEST-RUNTIME-001.md` and `provenance/raw/runtime-trace.json` preserve four controlled inputs, intermediate outputs, final outputs, method values, and the Node VM execution method. The corrected runtime trace status is `EXECUTED`.

### PROVENANCE EVIDENCE

`provenance/raw/`, `provenance/provenance-map.json`, the phase records, and the history reports preserve source/archive relationships, named-component scans, frozen-repository comparisons, and repository-creation evidence.

### FAILURE EVIDENCE

The following failures remain preserved:

- `evidence/failures/runtime-trace-first-run-failed.json`
- `evidence/failures/component-trace-first-run-false-positive.json`
- `evidence/failures/final-audit-source-extraction-first-run-failed.txt`
- `evidence/failures/sandbox-inventory-before-final-audit.json`

### INFERENCE

The reports contain explicitly labeled inferences, especially where a command's observed effects imply a mechanism. These are not relabeled as execution facts.

### UNKNOWN

Unknown states remain for browser speech behavior, original unrecorded build history, exact origin of individual source fragments, hidden tool/model activity, and whether named external systems influenced unrecorded steps.

## E. Provenance status

### ESTABLISHED

- The baseline source/archive correspondence and hashes.
- The current forensic repository's visible Git structure and history.
- The existence and execution of the local Python forensic tool.
- The Node VM detector trace and its preserved outputs.
- The absence of direct named-component imports/API calls in the scanned current Reciter project.
- The absence of lesson files in this technical repository.
- The presence of external Google Fonts URLs and the browser Web Speech API as source-level dependencies.

### NOT ESTABLISHED

- Direct execution of Laya, MAF, LHE, or CFHM by the Reciter build.
- Copied or adapted implementation from those frozen projects.
- Any named-component wrapper, adapter, MCP server, or model connector in the Reciter source.
- Full HTML standards validity.
- Actual speech pronunciation or voice availability.

### UNKNOWN

- Whether an unrecorded external model/service influenced the initial source.
- Whether partial source adaptation occurred without surviving provenance.
- Whether hidden Sandbox provisioning or unobserved sessions existed outside the available record.
- Whether the current source performs acceptably for languages or environments not covered by the controlled tests.

## F. Reproducibility status

| Check | Status | Basis or limitation |
|---|---|---|
| Source SHA-256 | **REPRODUCED** | Recomputed and matched the preserved hash |
| Archive integrity | **REPRODUCED** | `unzip -t` succeeded; extracted file matched source |
| Source JavaScript syntax | **REPRODUCED** | `node --check` succeeded on extracted script |
| Forensic Python syntax | **REPRODUCED** | `python3 -m py_compile` completed |
| Forensic tool execution | **REPRODUCED** | Tool regenerated valid JSON outputs |
| Detector runtime trace | **REPRODUCED** | Four inputs; result status `EXECUTED` |
| JSON provenance outputs | **REPRODUCED** | All generated JSON parsed successfully |
| Chromium DOM load | **PARTIALLY REPRODUCED** | Title/DOM observed; one DBus environment warning |
| Browser speech and voices | **NOT REPRODUCED** | No speech/voice assertions were made |
| Full HTML validator | **NOT REPRODUCED** | `tidy` unavailable; no standards-validity claim |
| Git local state | **REPRODUCED** | Branch, history, remote, and clean state inspected |
| GitHub remote state | **REPRODUCED** | Remote metadata and commit list inspected through `gh` |
| Frozen-repository provenance | **PARTIALLY REPRODUCED** | Checkouts and prior raw records available; full original environment is not permanent |

## G. Corrections made

- **NO HISTORICAL SOURCE MODIFICATIONS MADE.** `source/index.html` and the baseline archive were not changed.
- Removed the untracked Python `__pycache__` transient cache from the Sandbox; it was not tracked.
- Preserved the first final-audit helper failure as a new failure record.
- Preserved the prior committed sandbox inventory before accepting the regenerated current inventory.
- Regenerated `provenance/raw/sandbox-inventory.json` so it reflects the repository state at this final audit point.
- Added this dated final audit report and the exact final-audit specification in the corresponding commit.

These are new corrective/audit records. No old commit was amended or rewritten, and no previous failure was deleted.

## H. Remaining technical limitations

- Browser speech synthesis, voice enumeration, and pronunciation remain unverified.
- Full HTML standards validation remains unverified because no `tidy` executable was available.
- The runtime harness uses a minimal Node VM environment and is not equivalent to a full browser.
- External Google Fonts are referenced by URL and were not required for the Node detector trace.
- Historical absolute paths in evidence are tied to the original Sandbox layout and are not portable proof of availability in a fresh environment.
- The exact origin of individual implementation fragments remains unknown where no source history exists.
- Absence of named-component traces is not proof that no unrecorded external use occurred.

## I. Final repository state

The exact final Git commit hash will be the hash of the commit that adds this report and the corresponding audit records; Git computes it after commit creation and it is recorded in the final delivery message and remote Git metadata.

Branch: `main`

Remote: `origin` → `https://github.com/VAG-gomi/reciter-build-forensic-repository.git`

Source hash: `795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27`

Baseline/archive hash: `58eef85c4ae3e5b0501e9934f0c29be81925590ef69344b60effe218ab9136f5`

Forensic tool hash at audit time: recorded in the final delivery metadata after commit.

Final audit timestamp: `2026-09-30` UTC, execution records around `12:00` UTC.

## Freeze statement

The technical repository is now the evidence baseline for future research. Future lesson work must not silently alter the preserved source, baseline, runtime evidence, failure evidence, or provenance records. New research should be added as a dated research-layer record or a new corrective technical record when technically necessary.
