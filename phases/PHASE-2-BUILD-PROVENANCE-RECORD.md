# Phase 2 — Build Provenance and Sandbox Forensics Record

## Scope

This phase investigates whether the available Reciter build contains traceable relationships to Laya, MAF, LHE, CFHM, frozen repositories, adapters, wrappers, dependencies, or internal tools.

## OBSERVED

- The current project tree was scanned for named component references.
- The current project contains no package manifest, lockfile, import statement, or declared build script.
- No whole-name reference to `Laya`, `MAF`, `LHE`, or `CFHM` was found in the current project after correcting a substring false positive.
- Frozen repository checkouts are available under `/tmp/frozen-projects` in the investigation environment.
- No exact normalized whole-file match between the Reciter source and scanned frozen-repository files was established by the conservative source scanner.

## Component classification

| Component | Direct execution evidence | Local copy in Reciter project | Adapted code | Wrapper/API evidence | Provenance | Status |
|---|---|---|---|---|---|---|
| Laya | NO surviving evidence | NO | UNKNOWN | NO surviving evidence | UNKNOWN | UNRESOLVED |
| MAF | NO surviving evidence | NO | UNKNOWN | NO surviving evidence | UNKNOWN | UNRESOLVED |
| LHE | NO surviving evidence | NO | UNKNOWN | NO surviving evidence | UNKNOWN | UNRESOLVED |
| CFHM | NO surviving evidence | NO | UNKNOWN | NO surviving evidence | UNKNOWN | UNRESOLVED |
| Frozen repository sections | NO direct execution evidence | NO exact whole-file match established | UNKNOWN | UNKNOWN | PARTIALLY SUPPORTED as available comparison material | PARTIALLY ESTABLISHED |

## IMPLEMENTED

- Component trace and named-component report: `provenance/raw/component-trace.json` and `provenance/raw/named-components.json`.
- Source provenance comparison: `provenance/raw/source-provenance.json`.
- Dependency/import audit: `provenance/raw/dependency-audit.json`.
- Sandbox artefact inventory: `provenance/raw/sandbox-inventory.json`.
- Human-readable synthesis: `provenance/reports/provenance-report.md`.
- Machine-readable graph: `provenance/provenance-map.json`.

## FAILED

- The first component scanner matched `Laya` inside `Malayalam`. This was a false positive caused by substring matching. The original output is preserved at `evidence/failures/component-trace-first-run-false-positive.json`.
- The scanner was corrected to require whole component names and rerun. The corrected result contains no Laya match.

## UNKNOWN

A missing reference in the surviving project tree does not establish that a component was never used elsewhere. Resolving that question would require original build logs, external API/tool logs, or other surviving provenance evidence.
