# Reciter Build Forensic Repository

This repository is a technical record of the Universal Language Reciter build. It separates source, runtime evidence, failures, implementation details, and later provenance investigations.

## Evidence boundary

- `source/` preserves the current source as observed.
- `archive/` preserves the available baseline ZIP and its extracted source.
- `evidence/runtime/` contains executed runtime records.
- `evidence/implementation/` contains source and environment records.
- `tools/provenance/` contains separate investigation utilities. They are not Reciter production code.
- `provenance/raw/` contains machine-readable tool output.
- `provenance/reports/` contains summaries of those outputs.

Unknown provenance is retained as `UNKNOWN`; a textual component name is not treated as execution evidence.
