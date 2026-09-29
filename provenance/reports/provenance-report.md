# Reciter Provenance Report

## A. Established facts

- The current project contains one source file: `universal-language-reciter/index.html`.
- The available ZIP and extracted source are byte-identical at the recorded hashes.
- A Node VM harness executed the detector functions on controlled inputs.
- The project has no package manifest or declared build script in the inspected tree.
- No direct import or API invocation of Laya, MAF, LHE, or CFHM was found in the project scan.
- The initial component scan produced a false positive by matching `Laya` inside `Malayalam`; that result is preserved under `evidence/failures/`.

## B. Strongly supported relationships

- `archive/reciter-baseline/index.html` and `source/index.html` are byte-identical.
- The Reciter runtime trace is connected to the preserved source through the Node VM harness.

## C. Unresolved questions

- Whether Laya or any other named component was used directly, indirectly, or only mentioned outside the surviving project tree.
- Whether any source was copied or adapted from frozen repositories beyond the conservative exact-match scan.
- Whether any hidden or prior build tooling existed outside the available project tree.
- Whether browser speech synthesis executed successfully; the Node harness does not provide a browser speech engine.

## D. Missing evidence

- Original build terminal/session logs if they exist outside the available history.
- Browser runtime trace with actual `speechSynthesis` and voice enumeration.
- Version-control history for the standalone Reciter source; no Git metadata exists in the project.
- Any external API/tool logs that would establish direct component execution.

## E. Tool inventory

- `tools/provenance/forensic.py` — read-only component trace, source comparison, dependency audit, internal-tool scan, runtime trace, build trace, artifact inventory, baseline diff, named-component report, and provenance map.

## Named components

| Component | Direct execution evidence | Status |
|---|---|---|
| Laya | NO | UNRESOLVED |
| MAF | NO | UNRESOLVED |
| LHE | NO | UNRESOLVED |
| CFHM | NO | UNRESOLVED |
| Frozen repository sections | NO | PARTIALLY_ESTABLISHED |

## Baseline difference

Added files: `[]`

Removed files: `[]`

Modified files: `[]`

## Evidence boundary

The report records what was found in the available sandbox and project tree. It does not claim that absent traces prove a component was never used.
