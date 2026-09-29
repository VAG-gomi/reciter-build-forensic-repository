# Phase 3 — Reciter Provenance Investigation Toolset Record

## Tool location

The separate forensic tool is:

```text
tools/provenance/forensic.py
```

It is not imported by or used as Reciter production code.

## Tool-to-output mapping

| Phase 3 requirement | Implemented capability | Output |
|---|---|---|
| Component trace | Whole-name scan for Laya, MAF, LHE, CFHM; records file, line, reference type, context | `provenance/raw/component-trace.json` |
| Source provenance scanner | Compares current source with preserved baseline and conservative frozen-source matches | `provenance/raw/source-provenance.json` |
| Dependency/import auditor | Inspects manifests and external URLs; does not treat text mentions as dependencies | `provenance/raw/dependency-audit.json` |
| Internal tool discovery | Scans project files for scripts/configuration and reports use as UNKNOWN when unestablished | `provenance/raw/internal-tools.json` |
| Runtime trace | Node VM harness executes detector functions and records outputs | `provenance/raw/runtime-trace.json` |
| Build trace | Records that no build command or manifest was specified in the inspected single-file project | `provenance/raw/build-trace.json` |
| Sandbox artefact inventory | Categorizes relevant source, configuration, scripts, archives, and documentation | `provenance/raw/sandbox-inventory.json` |
| Baseline difference | Compares baseline and current project file sets and hashes | `provenance/raw/baseline-diff.json` |
| Provenance graph | Emits evidence-status edges between baseline, sandbox source, frozen repositories, components, and runtime | `provenance/provenance-map.json` |
| Named-component answer | Produces per-component direct-execution, source, sandbox, runtime, and provenance fields | `provenance/raw/named-components.json` |

## EXECUTED

The tool was run against the available build. Raw results are preserved under `provenance/raw/`.

## OBSERVED

- Baseline difference: no added, removed, or modified files between the preserved extracted baseline and current one-file project.
- Runtime trace status: `EXECUTED` using the Node VM harness.
- Browser speech synthesis: not exercised by this tool.
- Named component direct execution: not established.

## FAILED

- The initial runtime harness and initial substring component scanner failures are preserved under `evidence/failures/`.

## NO SELF-CERTIFICATION

The tool reports traces and uncertainty. It does not certify that a component was used merely because a name appears, that similar source was copied, or that an internal script was created by Manus.
