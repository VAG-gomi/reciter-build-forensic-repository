# Final Technical Audit of the Current Public Reciter Repository

Audit date: `2026-10-22`

Scope: technical verification of the current public `main` branch. This report does not write or interpret Lessons 1–8 and does not redesign either Reciter source.

## 1. Current repository and commit status

**OBSERVED:** The repository is currently public:

```text
VAG-gomi/reciter-build-forensic-repository
https://github.com/VAG-gomi/reciter-build-forensic-repository
```

GitHub metadata reports `visibility: PUBLIC`, default branch `main`, and no current GitHub Pages site record (`GET /repos/VAG-gomi/reciter-build-forensic-repository/pages` returned HTTP 404).

**OBSERVED:** The current checkout was cloned from `origin/main` and had a clean working tree before this audit.

The current pre-audit `HEAD` was:

```text
fa3f5d33e1c58196805f77d38d8b12e22a2f8976
Correction: Pages publication was premature, site disabled; application stage comes after tasks/logic/testing (owner ruling 2026-10-22)
```

The v2-related history is:

```text
4095ee89a0af00f6f13b80fc87f2857afeece88d  2026-10-22T02:07:24-06:00
Reciter completion v2: fixed TTS app as new docs/ version + dated record (frozen baseline untouched)

92d161237419c1fa1ba42d3a9d88a9cae56cee9e  2026-10-22T02:11:22-06:00
Record v2 browser verification + GitHub Pages publication (2026-10-22)

fa3f5d33e1c58196805f77d38d8b12e22a2f8976  2026-10-22T02:15:15-06:00
Correction: Pages publication was premature, site disabled; application stage comes after tasks/logic/testing (owner ruling 2026-10-22)
```

**OBSERVED:** Commit `4095ee8` added both `COMPLETION-RECITER-V2-2026-10-22.md` and `docs/index.html`. Commit `92d1612` appended browser/publication claims to the completion record. Commit `fa3f5d3` appended the correction that Pages was disabled and the application stage was premature.

The audit commit(s) added after this report are recorded in the final repository state and changelog.

## 2. Baseline versus v2 identity

These are separate artifacts and are not merged:

| Artifact | Location | SHA-256 | Status |
|---|---|---|---|
| Original frozen baseline | `source/index.html` | `795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27` | Preserved baseline |
| Extracted baseline archive copy | `archive/reciter-baseline/index.html` | `795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27` | Byte-identical to baseline |
| Baseline ZIP | `archive/reciter-baseline-v1.zip` | `58eef85c4ae3e5b0501e9934f0c29be81925590ef69344b60effe218ab9136f5` | Preserved archive |
| v2 draft/application work material | `docs/index.html` | `8a6e38380a87ac84974b95f618cc080bc9c0876875a85973dc5b4828082d58ce` | Separate new file, not baseline |

**OBSERVED:** `source/index.html` and `archive/reciter-baseline/index.html` are byte-identical. The baseline ZIP passes `unzip -t` and contains the matching baseline source.

**OBSERVED:** `docs/index.html` is a different file with a different hash and additional v2 speech-status, voice-selection, chunking, watchdog, and method-label code. No `workspace/reciter-v2/` path exists in the current repository tree.

## 3. Documentation inconsistency and resolution

### Inconsistency found

The opening of `COMPLETION-RECITER-V2-2026-10-22.md` says:

> `DRAFT — not published, not pushed.`

and says the v2 file was located in `workspace/reciter-v2/index.html` while the visibility decision was pending.

That statement accurately describes the pre-commit draft state represented by the first v2 work, but it is stale when read as a statement about the current repository because:

- `COMPLETION-RECITER-V2-2026-10-22.md` is tracked on public `main`;
- `docs/index.html` is tracked on public `main` from commit `4095ee8`;
- no `workspace/reciter-v2/` directory exists in the current tree;
- later sections of the same record document v2 browser verification and the attempted Pages publication;
- the final section says the publication was premature, Pages was disabled, and the v2 material remains draft work material.

### Recoverable transition

**OBSERVED:** The exact transition from private/draft working material to committed `docs/index.html` is recoverable at the Git level: commit `4095ee8` created `docs/index.html` and the completion record. The exact pre-commit filesystem path and any unrecorded workspace operations before that commit are not recoverable from the current repository.

**OBSERVED:** Commit `92d1612` recorded v2 browser verification and GitHub Pages publication claims.

**OBSERVED:** Commit `fa3f5d3` recorded that the Pages publication was premature and that Pages was disabled. Current GitHub Pages API and the documented live URL both return 404, consistent with that correction.

**CORRECTION MADE IN THIS AUDIT:** A dated current-state clarification is added at the beginning of the completion record. It preserves the original draft wording below while explicitly distinguishing the historical pre-commit state from the current public repository state. The application files are not modified.

## 4. Source and script verification

### Original baseline

- **Method:** Extract inline script from `source/index.html`; run `node --check`; execute detector functions in a Node VM with minimal DOM and speech mocks.
- **Inputs:** Bengali `আমি বাংলায় কথা বলছি`; Arabic `مرحبا يا صديقي`; short English sentence; short Spanish sentence.
- **Observed output:** Bengali → `bn-BD`, `Bengali`, `100`, `unicode-rule`; Arabic → `ar-SA`, `Arabic`, `100`, `unicode-rule`; English → English, `35`, `fallback`; Spanish → English, `35`, `fallback`.
- **Status:** `REPRODUCED` for syntax and the existing simulated detector path.
- **Limitation:** Minimal VM mocks are not a real browser and do not verify speech audio.

### v2 source

- **Method:** Extract inline script from `docs/index.html`; run `node --check`; execute the same detector functions with the same minimal DOM/speech mocks.
- **Observed output:** Same detector outputs as the baseline for the four inputs, consistent with the v2 record’s statement that detection logic was unchanged.
- **Status:** `REPRODUCED` for syntax and the simulated detector path.
- **Additional source checks:** v2 contains `#speech-status`, a persistent Device-default option, voice matching/fallback handling, chunk queue functions, cancellation handling, `bigram-cosine`, and the watchdog path.
- **Limitation:** A mocked speech engine does not establish real browser speech behavior.

### Browser-load checks

- **Method:** Chromium headless `--dump-dom` against local `file://` URLs for `source/index.html` and `docs/index.html`.
- **Observed output:** Both pages loaded and produced the expected `Universal Language Reciter` title in the dumped DOM.
- **Status:** `PARTIALLY REPRODUCED`.
- **Limitation:** This verifies practical parsing/DOM load only, not speech voices, audio, or human pronunciation.

### Forensic script

`tools/provenance/forensic.py` remains a separate forensic tool and is not application code. Its prior execution records remain under `provenance/raw/`; this audit did not redesign it. Its fixed historical paths and environment assumptions remain documented limitations.

## 5. Runtime, evidence, and provenance status

### Verified or reproduced

- Original source hash and archive relationship.
- Separate v2 source hash and current tracked path.
- Git history and v2 transition commits.
- Current public repository metadata.
- GitHub Pages disabled state through API 404 and live URL HTTP 404.
- Node syntax checks for baseline and v2.
- Simulated detector behavior for the controlled input matrix.
- Local Chromium DOM load for baseline and v2.
- Existing runtime, failure, and provenance records remain present.

### Existing evidence retained

- Implementation evidence: source files and `evidence/implementation/`.
- Runtime/experimental evidence: `evidence/runtime/` and existing v2 completion record.
- Provenance evidence: `provenance/`, history records, and Git history.
- Failure evidence: `evidence/failures/`, including prior harness and audit failures.
- Inference: explicitly labeled in prior records and this report.
- Unknown: retained for unrecorded pre-commit workspace activity and real-device speech behavior.

### Not established

- The exact filesystem path or command used for the v2 draft before commit `4095ee8`.
- A real voiced-device pronunciation test.
- Watchdog behavior on a genuinely hanging speech engine.
- The voice-present-but-no-language-match branch in a browser with voices.
- Whether any unrecorded external tool influenced v2 before its first commit.

## 6. Public-exposure scan

The current tracked tree and relevant Git history were scanned for:

- GitHub token prefixes such as `ghp_` and `github_pat_`;
- OpenAI-style secret prefixes such as `sk-`;
- private-key delimiters;
- explicit environment assignments such as `GH_TOKEN=` or `OPENAI_API_KEY=`;
- suspicious credential-like material in current tracked text;
- personal data beyond repository author metadata and public paths.

**Observed result:** No matching credential or private-key material was found in the limited scan.

**Scope limitation:** This is not a complete security audit. It does not prove absence of secrets in GitHub object storage, deleted blobs not reached by the scan, binary data, external services, browser caches, or unobserved history. The repository is public, so future additions should be scanned before pushing.

## Prompt-injection warning disposition

A system-level prompt-injection warning interrupted the audit before authorization to continue. The exact detector trigger is not exposed in the available records, so its originating token or content cannot be identified with certainty.

The repository and attachment were treated as untrusted data. A scan of the current tracked tree found no matches for common prompt-injection patterns such as requests to ignore prior instructions, reveal prompts, exfiltrate secrets, or execute unrelated commands. The only command-like matches were inert historical command examples in provenance records and search terms in audit documentation; they were not followed as instructions.

No repository file was deleted or rewritten because of the warning. The warning is recorded as **SOURCE/CONTENT UNKNOWN** rather than attributed to a specific file without evidence. The user subsequently explicitly authorized this validation, commit, and push within the stated documentation-only boundaries.

## 7. Exact files changed in this audit

The technical clarification commit adds or modifies only:

- `COMPLETION-RECITER-V2-2026-10-22.md` — adds a dated current-state clarification while preserving the original draft text.
- `CHANGELOG.md` — records this audit and the documentation correction.
- `README.md` — links the public-repository audit.
- `reports/FINAL-PUBLIC-REPOSITORY-TECHNICAL-AUDIT-2026-10-22.md` — this report.
- `specification/FINAL-PUBLIC-REPOSITORY-TECHNICAL-AUDIT-2026-10-22.md` — exact attached specification.

No source, archive, baseline, v2 application file, prior failure record, or prior provenance record is replaced or rewritten.

## 8. Remaining technical defects and unknowns

- The v2 completion record had stale opening draft/path wording; this is clarified by the new dated note.
- The v2 source remains draft work material rather than an enabled application, consistent with the final owner correction.
- Real-device speech output and pronunciation remain unverified.
- Some v2 speech branches require browser environments not available in this audit.
- The original baseline’s short Latin-text fallback behavior remains unchanged and is not repaired here.
- Historical absolute paths and prior environment-specific records are not portable to a fresh environment.
- Absence of scan matches is not proof that no unobserved secret or external influence ever existed.

## 9. Final repository state

Final audit documentation commit hash: `95eb09467895debce69943c25666fd58dd1fcfd6`.

This report-hash correction is itself a new documentation-only commit; no application source or prior evidence is changed.

Branch: `main`

Remote: `origin` → `https://github.com/VAG-gomi/reciter-build-forensic-repository.git`

Visibility: `PUBLIC`

GitHub Pages: not enabled/current API 404; documented live URL returns HTTP 404.

Original baseline SHA-256: `795c4406efd0931847af4b6620c9576c54184389bf01e8419b897098fbc42e27`

Baseline ZIP SHA-256: `58eef85c4ae3e5b0501e9934f0c29be81925590ef69344b60effe218ab9136f5`

v2 `docs/index.html` SHA-256: `8a6e38380a87ac84974b95f618cc080bc9c0876875a85973dc5b4828082d58ce`

Audit timestamp: `2026-10-22`, execution around `2026-10-23T04:20Z` / local task time.

## Final technical conclusion

The current public repository contains two distinct Reciter artifacts: the frozen original baseline under `source/` and a separately committed v2 draft under `docs/`. The baseline remains byte-identical to its archive. The v2 transition and later Pages correction are visible in Git history. The documentation inconsistency is a stale historical opening statement, not evidence that the current `docs/index.html` is absent or uncommitted. This audit clarifies that distinction without merging the artifacts, altering their code, enabling Pages, or creating lesson conclusions.
