# Reciter Build History Interrogation

Date of this record: `2026-09-30`

This report is a forensic account of what is available from the working history, the current project, preserved runtime records, and Git history. It distinguishes remembered workflow events from project evidence. It does not infer hidden mechanisms.

## Evidence boundary

The available record contains the original single-file source, the first available ZIP archive, later forensic records, command/tool results preserved in the conversation history, and the Git history of the forensic repository. It does not contain a complete operating-system audit, every prior terminal transcript, browser instrumentation, or hidden model/tool internals.

Where an action cannot be established, this report says `UNKNOWN`.

---

## 1. First model/build

### RECEIVED

**OBSERVED from the available working record:** I received a written specification for the Universal Language Reciter. The specification required a single-file web application with a detector, confidence display, speech controls, language profiles, and browser speech behavior.

**UNKNOWN:** The complete contents of the directory before the initial file write are not preserved in the current Git repository. Therefore I cannot establish a complete list of every file that existed before construction.

### CREATED

**OBSERVED:** The initial Reciter source was created as:

```text
/home/ubuntu/universal-language-reciter/index.html
```

That file contains HTML, CSS, and JavaScript in one file. The current preserved source is:

```text
source/index.html
```

### MODIFIED

**OBSERVED:** During the initial Reciter construction, the available working record shows one `write` operation creating `index.html`. A complete edit-by-edit history of that first file is not available.

**OBSERVED:** During the later forensic work, the production Reciter file was not modified. The preserved source hash is:

```text
795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27
```

### COPIED

**OBSERVED:** After the initial build, the source was copied into an archive workflow and packaged as:

```text
/home/ubuntu/universal-language-reciter.zip
```

The archive contains `index.html`. The forensic repository contains an extracted copy and the ZIP copy.

**UNKNOWN:** Whether any code was copied from an external source during the initial creation cannot be established from the surviving Reciter project history.

### ADAPTED

**UNKNOWN:** The current files do not establish whether any initial implementation section was adapted from another source. The conservative frozen-repository comparison found no exact normalized whole-file match, but that does not prove that no partial adaptation occurred.

### DELETED

**UNKNOWN:** No complete deletion history for the initial application workspace is available. No deletion of the preserved production source is recorded.

### LEFT UNCHANGED

**OBSERVED:** The baseline source and the current preserved source are byte-identical. The forensic work left the production source unchanged.

### EXECUTED

The available working history records these initial-build and immediate follow-up operations:

1. Deterministic Python checks against the generated HTML and its self-contained structure.
2. Node.js execution of detector definitions to inspect raw scores and edge cases.
3. A local HTTP server using Python's `http.server` to confirm the file was readable over HTTP.
4. ZIP packaging and `unzip` validation of the first archive.

A later preserved runtime record also executed the detector functions through a Node VM harness. That record is `evidence/runtime/TEST-RUNTIME-001.md`.

### OBSERVED RESULTS

The preserved runtime record shows, for the controlled inputs, the Unicode stage, n-gram stage, and final result. For example, for the Spanish sentence, the n-gram stage returned Spanish with confidence `47`, while the final result returned English with confidence `35` and method `fallback`. The exact outputs are preserved rather than paraphrased.

### UNKNOWN

The original browser speech-synthesis result, actual device voice list, and complete first-build terminal log are not available in the current record.

---

## 2. Frozen repository material

### What was actually done

**OBSERVED:** Frozen repositories were cloned into the temporary Sandbox location:

```text
/tmp/frozen-projects/
```

They were then inspected read-only for the separate score/threshold and architectural comparison research. The available history shows repository cloning, file inventory, targeted reads, and searches. It does not show files from those repositories being copied into the Reciter production project.

### Relevant frozen families and observed commit identifiers

| Family | Observed checkout(s) | Observed commit(s) | Relationship to Reciter |
|---|---|---|---|
| MAF | `maf-release`, `maf-software`, `maf-evidence-bank`, `maf-spec-m1-evidence` | `bf3625a5de89f054be6aeb46fae44bbf33305381`, `5e6a021d1f81997aa8e824eaf6584471d28546f3`, `a32d68e9629da3b32e8a0c83809013c02a43fd87`, `0c4f49da4bcc56017099479aeaaf206ce34888d2` | Research reference only; no Reciter dependency established |
| LHE | `lhe-release`, `lhe-software`, `lhe-evidence-bank`, `lhe-spec-l2-evidence` | `80f6343ecde29f544f7d685c48a02fbedd8ecc8d`, `ecf3846d64d948b4a53cc8d224d25d10de11d9ed`, `89ed1b61868083127c0cb486b70aec3a09c216e92`, `e9a6c03e07083127c0cb486b70aec3a09c216e92` | Research reference only; no Reciter dependency established |
| CFHM | `cfhm-release`, `cfhm-software`, `cfhm-evidence-bank`, `cfhm-spec-c1-evidence` | `17fd6c6211839e99e40907c41e9c1ff34026fddf`, `497a21057a9b041ce61891f86e5e7638506cbf64`, `660b28d0e169e6a55e130cfa0c92f535407be96`, `bd39df64dd2cbe5feb743095533542d066cc1184` | Research reference only; no Reciter dependency established |
| Other frozen projects | QGRIM, Protocol Singularity, Unified Robust Coder Protocol, GrimChess, Trilogy and others | Recorded in the temporary checkout metadata | Architectural comparison research; no Reciter dependency established |

### COPIED / MODIFIED / REFERENCED

- **Copied into Reciter production source:** `UNKNOWN`; no evidence found.
- **Modified in Reciter production source:** `UNKNOWN`; no evidence found.
- **Merely referenced for research:** `OBSERVED`. The repositories were read as external comparison material.
- **Remained unchanged in their original locations:** `OBSERVED` for the read-only inspection workflow; no write operation against those repositories is recorded.
- **Resulting file/location inside Reciter:** no frozen repository file is present under `source/`, `archive/`, or the production project.

The exact comparison output is preserved in `provenance/raw/source-provenance.json` and `provenance/reports/provenance-report.md`.

---

## 3. Laya AI

### Direct use

**NO direct Laya execution is established by the available record.**

The available working history contains no Laya tool call, Laya API call, Laya MCP call, local Laya runtime, or execution trace. The current Reciter project contains no whole-name `Laya` reference after the scanner was corrected to avoid matching the substring inside `Malayalam`.

### What happened instead

**OBSERVED:** The initial Reciter source was created as a standalone HTML file from the provided implementation specification, then tested with local Python/Node tooling. Later, Laya was discussed as a provenance question and searched as an architectural comparison topic; that is not evidence of Laya execution during the Reciter build.

### Possible answers requested by the specification

| Question | Record |
|---|---|
| Was Laya accessed as an external model/service? | NO surviving execution evidence |
| Was a Laya API used? | NO surviving execution evidence |
| Was an Laya MCP interface used? | NO surviving execution evidence |
| Was a local Laya copy used? | NO surviving project evidence |
| Was code generated by Laya? | UNKNOWN; no generation attribution or trace is preserved |
| Which files resulted from Laya? | UNKNOWN; no resulting file is attributable to Laya |
| Can an execution trace be identified? | NO |

The correct provenance label is therefore **UNRESOLVED / UNKNOWN**, not a claim that every possible historical use is disproven.

---

## 4. MAF

| Question | Factual record |
|---|---|
| Directly used? | NO direct MAF execution is present in the available Reciter build record. |
| Installed? | UNKNOWN; no package metadata or installation log for MAF is present. |
| Accessed through an API? | NO surviving API evidence in the Reciter project. |
| Represented by copied/adapted code? | UNKNOWN; no exact source match or attribution establishes this. |
| Only mentioned in instructions/research? | OBSERVED for the later provenance/research activity. |
| Internal replacement/wrapper created? | NO MAF-specific wrapper is present in the Reciter project; a general forensic Python tool was created later, but it does not implement MAF. |
| Final classification | UNRESOLVED; direct use is not established. |

MAF repository files were cloned and read for comparison research. They were not recorded as Reciter runtime dependencies.

---

## 5. LHE

| Relationship | Factual record |
|---|---|
| Direct use | NO direct LHE execution evidence in the Reciter record. |
| Indirect use | UNKNOWN; no indirect adapter or dependency is present. |
| Copied implementation | UNKNOWN; no exact normalized whole-file match established. |
| Adapted implementation | UNKNOWN. |
| Reference only | OBSERVED for the later research comparing verdict/threshold mechanisms. |
| Internal replacement | No LHE-specific replacement is present in the Reciter source. |
| Final classification | UNRESOLVED; direct use is not established. |

---

## 6. CFHM

| Relationship | Factual record |
|---|---|
| Direct use | NO direct CFHM execution evidence in the Reciter record. |
| Indirect use | UNKNOWN; no adapter or dependency is present. |
| Copied implementation | UNKNOWN; no exact normalized whole-file match established. |
| Adapted implementation | UNKNOWN. |
| Reference only | OBSERVED for the later research comparing stability gates and decision boundaries. |
| Internal replacement | No CFHM-specific replacement is present in the Reciter source. |
| Final classification | UNRESOLVED; direct use is not established. |

---

## 7. Manus Sandbox activity

### OBSERVED

The available record establishes that the Sandbox was used to:

- create and preserve the initial HTML file;
- run Python and Node checks;
- run a local HTTP server;
- package and inspect the Reciter ZIP;
- clone and inspect frozen repositories in `/tmp/frozen-projects`;
- create the forensic repository and its records;
- create and execute `tools/provenance/forensic.py`;
- generate JSON provenance outputs and Markdown reports;
- initialize a Git repository and push it to GitHub.

### Component-by-component status

| Activity | Status | Evidence |
|---|---|---|
| Copied frozen repository files into Reciter source | NO surviving evidence |
| Cloned frozen repositories | OBSERVED | `/tmp/frozen-projects` checkouts and Git metadata |
| Created local versions of Laya/MAF/LHE/CFHM | NO surviving evidence |
| Modified frozen implementations | NO surviving evidence in the inspected workflow |
| Created wrappers/adapters for named components | NO named-component wrapper found |
| Created MCP server/client for Reciter | NO surviving evidence |
| Created helper scripts | OBSERVED | forensic Python tool and temporary Node harness |
| Created test harnesses | OBSERVED | Node VM harness and deterministic checks |
| Generated configuration | OBSERVED for forensic repository metadata such as Git and `.gitignore`; no Reciter dependency configuration was generated |
| Created temporary implementation files | OBSERVED | temporary runtime runner/source files created and removed by the forensic tool |
| Converted external implementations into Reciter local implementations | UNKNOWN; no evidence establishes this |

---

## 8. Internal tools

### Tool: `forensic.py`

- **Location:** `tools/provenance/forensic.py`
- **When/why created:** During the forensic repository setup, to investigate provenance and produce reproducible evidence records.
- **What it does:** Component trace, source comparison, dependency audit, internal-tool scan, runtime trace, build trace, artifact inventory, baseline diff, named-component report, and provenance map generation.
- **What it connects to:** Local filesystem, preserved source, `/tmp/frozen-projects` when available, and Node.js for the runtime harness. It does not connect to Laya, MAF, LHE, or CFHM.
- **Actually executed:** YES. Its raw outputs are under `provenance/raw/`.
- **Evidence:** `evidence/tests/TEST-FORENSIC-001.md`, `provenance/raw/*.json`.
- **Still present:** YES.

### Temporary Node runtime harness

- **Location:** Generated temporarily inside `tools/provenance/` by `forensic.py`; `.runtime_runner.js` and `.runtime_source.html` are removed in the tool's `finally` block.
- **When/why created:** To execute the existing JavaScript detector functions without modifying the production HTML.
- **Actually executed:** YES.
- **Still present:** NO as a generated temporary file; the harness source is embedded in `forensic.py`.
- **Connection:** Node VM to the preserved HTML script; no external model or named component.

### Other tools

The available record also shows use of standard existing utilities such as Python, Node.js, Git, GitHub CLI, ZIP tools, and the local HTTP server. They were execution/investigation utilities, not Reciter production components.

**UNKNOWN:** Whether any hidden internal tool outside the available history was used cannot be established.

---

## 9. Response to named-tool instructions

When instructions named Laya, MAF, LHE, or CFHM, the available workflow record shows two separate activities:

1. During the later research phase, the names triggered repository lookup, source reading, and architectural/provenance comparison.
2. During the Reciter build itself, the surviving implementation is a standalone HTML/CSS/JavaScript file. No named-system API, MCP, model connector, or runtime dependency appears in that project.

The available record does **not** expose the model's private internal reasoning or hidden routing mechanism. Therefore I cannot establish whether the names affected hidden model-side reasoning beyond the observable repository lookup and research actions.

Established observable mechanisms are:

- repository lookup and cloning for frozen-project research;
- local source writing for the Reciter file;
- local Node/Python execution for testing;
- later creation of a separate provenance tool.

There is no established evidence of direct named-system invocation, copied implementation, simulation, or mock for the Reciter application.

---

## 10. Source provenance by major Reciter component

| Component | Origin/current location | Copied? | Modified? | Generated/adapted? | Record |
|---|---|---|---|---|---|
| HTML UI | Initial standalone file; `source/index.html` | UNKNOWN | Production source unchanged during forensic work | Created in initial file-write operation; exact upstream origin UNKNOWN | Current source proves the markup exists, not its authorship |
| CSS | Inline in `source/index.html` | UNKNOWN | Production source unchanged during forensic work | Created/assembled in initial file-write operation; exact origin UNKNOWN | No external CSS package is declared |
| Unicode detection | `detectUnicode()` in `source/index.html` | UNKNOWN | Unchanged in preserved baseline | Adaptation/copy status UNKNOWN | Implementation is directly observable |
| N-gram extraction | `extractBigrams()` in `source/index.html` | UNKNOWN | Unchanged in preserved baseline | Adaptation/copy status UNKNOWN | Uses ASCII-letter cleaning and bigrams |
| Language profiles | `LANGUAGE_PROFILES` in `source/index.html` | UNKNOWN | Unchanged in preserved baseline | Adaptation/copy status UNKNOWN | Literal profile data is present in source |
| Cosine scoring | `cosineSimilarity()` in `source/index.html` | UNKNOWN | Unchanged in preserved baseline | Adaptation/copy status UNKNOWN | Implementation is directly observable |
| TTS | `speakText()` and browser speech synthesis calls | UNKNOWN | Unchanged in preserved baseline | Adaptation/copy status UNKNOWN | No external TTS adapter is present |
| Model/API adapter | None found in Reciter source | NO surviving implementation | N/A | N/A | No model/API adapter is established |
| Tool interface | Browser DOM/event listeners in `source/index.html` | UNKNOWN | Unchanged in preserved baseline | Adaptation/copy status UNKNOWN | No MCP interface is present |
| Sandbox integration | None in production source | NO surviving implementation | N/A | N/A | Sandbox was used externally for building/testing, not as a source dependency |

---

## 11. Runtime operations actually performed

### Operation A — Initial deterministic checks

- **Input:** Generated Reciter HTML and extracted JavaScript.
- **Build/version:** Initial available Reciter build.
- **Method:** Python scripts inspecting HTML structure and Node.js scripts executing detector definitions.
- **Actual output:** Syntax and behavior checks were run; exact full terminal transcript is not preserved in the current repository.
- **Errors:** Not established for every initial check.
- **Warnings:** UNKNOWN.
- **Relevant files:** `/home/ubuntu/universal-language-reciter/index.html`.

### Operation B — Local HTTP readability check

- **Input:** `index.html`.
- **Build/version:** Initial available Reciter build.
- **Method:** `python3 -m http.server 4173 --bind 127.0.0.1`.
- **Actual output:** The prior record states that the file was verified over a local HTTP server and was readable.
- **Errors:** None recorded in the available summary.
- **Warnings:** This did not establish browser UI or speech behavior.
- **Relevant files:** `index.html`.

### Operation C — ZIP packaging

- **Input:** `index.html`.
- **Build/version:** Baseline archive.
- **Method:** ZIP creation followed by `unzip -l`, extraction, hash comparison, and `cmp`.
- **Actual output:** Archive contained one `index.html`; extracted source matched the source byte-for-byte.
- **Errors:** None in the preserved packaging result.
- **Warnings:** None recorded.
- **Relevant files:** `universal-language-reciter.zip`.

### Operation D — Node VM runtime trace

- **Input:** `hola`; a Spanish sentence; a three-line English/Arabic/French input; empty string.
- **Build/version:** `reciter-baseline-v1` / preserved `source/index.html`.
- **Method:** Node VM harness from `tools/provenance/forensic.py`.
- **Actual output:** Preserved in `evidence/runtime/TEST-RUNTIME-001.md` and `provenance/raw/runtime-trace.json`.
- **Errors:** The corrected trace emitted no error. An earlier harness failure is preserved separately.
- **Warnings:** No browser speech engine was present.
- **Relevant files/functions:** `source/index.html`; `detectUnicode()`, `extractBigrams()`, `cosineSimilarity()`, `detectNgram()`, `detectLanguage()`.

### Operation E — Frozen repository research

- **Input:** MAF, LHE, CFHM, and other frozen repository checkouts.
- **Build/version:** Recorded repository commits listed in the Phase 2 record.
- **Method:** GitHub CLI repository inventory, shallow clones, file inventory, targeted reads, and searches.
- **Actual output:** Research notes and provenance classifications; no Reciter source modification.
- **Errors:** Some repository listing output required clean-session retries; no evidence indicates source corruption.
- **Warnings:** Research comparison is not build dependency evidence.
- **Relevant files:** `/tmp/frozen-projects/*`; final comparisons in `provenance/`.

### Operation F — Forensic tool execution

- **Input:** Current project, preserved baseline, and available Sandbox artifacts.
- **Build/version:** `forensic-initial`.
- **Method:** `python3 tools/provenance/forensic.py`.
- **Actual output:** JSON records under `provenance/raw/`.
- **Errors:** Initial runtime-harness regex failure and initial component-scan false positive are preserved under `evidence/failures/`.
- **Warnings:** No browser speech execution.
- **Relevant file:** `tools/provenance/forensic.py`.

---

## 12. What I did not do

### DEFINITELY DID NOT / strongly established from available evidence

- I did not modify the preserved production source during the forensic repository work.
- I did not add Python code to the Reciter production application.
- I did not add Laya, MAF, LHE, or CFHM imports, APIs, MCP calls, or runtime dependencies to the current Reciter project.
- I did not create a named-component MCP server or named-component wrapper in the Reciter project.
- I did not put frozen repository files into `source/` or the baseline archive.
- I did not replace the original source with a later redesign.

### UNKNOWN rather than NO

- Whether code in the initial Reciter source was partially copied or adapted from an unobserved source.
- Whether an unrecorded external model or tool was used before the available history began.
- Whether hidden internal model routing occurred outside observable tool calls.
- Whether any external build service was used outside the available Sandbox and preserved history.

---

## 13. Memory versus project evidence

### A. What I remember doing / what the available working history records

I remember the observable workflow: create the standalone HTML Reciter from the specification; run local Python/Node checks; package and verify the ZIP; later clone and inspect frozen repositories for separate research; create a separate Python forensic tool; preserve failures; create the forensic Git repository; and push it to a private GitHub repository.

### B. What the current project proves

The project proves that the preserved Reciter is one HTML file containing the detector, profiles, UI, and speech code. It proves the baseline/source hash equality, the preserved runtime outputs, the existence and execution of the forensic Python tool, the preserved failures, and the Git commits that contain the forensic records.

### C. What I cannot establish

I cannot establish the complete initial workspace contents, the full initial edit history, the origin of each algorithm/profile/UI fragment, hidden model-side routing, or whether any unrecorded external service influenced the first file.

---

## 14. Contradictions

### MEMORY / working-history account

The available working history shows the Reciter was created as a standalone HTML file and tested locally. Later research involved frozen repositories and named systems.

### PROJECT EVIDENCE

The current Reciter source contains no direct named-system imports or API calls. The frozen repositories are not present inside the Reciter source or archive. The forensic tool is separate from the production application.

### CONFLICT

`NO` for the observable records available here.

### Limitation

This is not proof that no earlier unrecorded action occurred. Any unrecorded history remains `UNKNOWN` rather than silently resolved.

---

## 15. Final account

### DEFINITELY DID

- Created/preserved the standalone `index.html` Reciter implementation in the available Sandbox workflow.
- Ran local Python and Node checks against the source.
- Started a local HTTP server to check file readability.
- Packaged and hash-compared the baseline ZIP.
- Cloned and read frozen repositories for later research comparison.
- Created the separate Python provenance tool and Node VM harness.
- Preserved runtime outputs and failures.
- Created and pushed the private forensic GitHub repository.

### DEFINITELY DID NOT

- Modify the production Reciter source during the forensic repository work.
- Add Python to the production Reciter application.
- Establish or add direct Laya, MAF, LHE, or CFHM runtime integration to the current project.
- Put frozen repository source into the preserved Reciter source or baseline archive.

### UNKNOWN / UNRESOLVED

- Whether Laya, MAF, LHE, or CFHM was used before the available history or through hidden mechanisms.
- Whether any initial source section was copied or adapted from an unobserved source.
- The complete initial workspace and edit-by-edit construction history.
- Any browser speech-synthesis result from the initial build.
- Any external build or model service activity not captured in the available records.

The exact new interrogation specification is preserved separately at `specification/RECITER-BUILD-HISTORY-INTERROGATION.md`.
