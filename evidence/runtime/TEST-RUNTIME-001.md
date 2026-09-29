# TEST-RUNTIME-001 — Reciter Detector Runtime Trace

Test ID: `TEST-RUNTIME-001`

Date: `2026-09-29`

Build/version: `reciter-baseline-v1` / preserved `source/index.html`

Input set: four controlled text inputs listed below

Execution method: Node.js VM harness invoking the extracted functions from the preserved HTML source

Expected behaviour: not previously specified

Relevant source file: `source/index.html`

Relevant functions: `detectUnicode()`, `extractBigrams()`, `cosineSimilarity()`, `detectNgram()`, `detectLanguage()`

## Actual outputs

### Input 1

```text
hola
```

Observed Unicode stage:

```json
{"confidence":100,"languageCode":null,"script":"latin"}
```

Observed n-gram stage:

```json
{"confidence":40,"languageCode":"en-US","languageName":"English"}
```

Observed final result:

```json
{"confidence":35,"languageCode":"en-US","languageName":"English","method":"fallback"}
```

### Input 2

```text
Esta es una oración mucho más larga que contiene varios patrones del español.
```

Observed Unicode stage:

```json
{"confidence":98,"languageCode":null,"script":"latin"}
```

Observed n-gram stage:

```json
{"confidence":47,"languageCode":"es-ES","languageName":"Spanish"}
```

Observed final result:

```json
{"confidence":35,"languageCode":"en-US","languageName":"English","method":"fallback"}
```

### Input 3

```text
Hello my friend.
مرحبا يا صديقي.
Bonjour mon ami.
```

Observed Unicode stage:

```json
{"confidence":67,"languageCode":null,"script":"latin"}
```

Observed n-gram stage:

```json
{"confidence":22,"languageCode":"en-US","languageName":"English"}
```

Observed final result:

```json
{"confidence":35,"languageCode":"en-US","languageName":"English","method":"fallback"}
```

### Input 4

```text
[empty string]
```

Observed Unicode stage:

```json
{"confidence":0,"languageCode":null,"script":null}
```

Observed n-gram stage:

```json
{"confidence":40,"languageCode":"en-US","languageName":"English"}
```

Observed final result:

```json
{"confidence":0,"languageCode":"en-US","languageName":"English","method":"none"}
```

## Errors

No error was emitted by the corrected Node VM runtime trace.

## Warnings and limitations

- The Node VM harness supplied a minimal DOM environment and no browser speech engine.
- Web Speech API execution, voice enumeration, and actual browser UI interaction were not tested by this record.
- The result records are observations of this implementation and are not claims of language-detection accuracy.

## Exit/status

`EXECUTED` for the detector trace.
