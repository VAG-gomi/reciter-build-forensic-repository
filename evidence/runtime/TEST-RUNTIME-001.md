# Runtime Evidence — Node VM Trace

Status: `EXECUTED`
Execution method: `Node VM harness`
Source: `/home/ubuntu/reciter-build-forensic/source/index.html`

## Inputs and outputs

### Input
```text
hola
```

**Unicode stage:** `{"confidence": 100, "languageCode": null, "script": "latin"}`

**N-gram stage:** `{"confidence": 40, "languageCode": "en-US", "languageName": "English"}`

**Final result:** `{"confidence": 35, "languageCode": "en-US", "languageName": "English", "method": "fallback"}`

### Input
```text
Esta es una oración mucho más larga que contiene varios patrones del español.
```

**Unicode stage:** `{"confidence": 98, "languageCode": null, "script": "latin"}`

**N-gram stage:** `{"confidence": 47, "languageCode": "es-ES", "languageName": "Spanish"}`

**Final result:** `{"confidence": 35, "languageCode": "en-US", "languageName": "English", "method": "fallback"}`

### Input
```text
Hello my friend.\nمرحبا يا صديقي.\nBonjour mon ami.
```

**Unicode stage:** `{"confidence": 67, "languageCode": null, "script": "latin"}`

**N-gram stage:** `{"confidence": 22, "languageCode": "en-US", "languageName": "English"}`

**Final result:** `{"confidence": 35, "languageCode": "en-US", "languageName": "English", "method": "fallback"}`

### Input
```text

```

**Unicode stage:** `{"confidence": 0, "languageCode": null, "script": null}`

**N-gram stage:** `{"confidence": 40, "languageCode": "en-US", "languageName": "English"}`

**Final result:** `{"confidence": 0, "languageCode": "en-US", "languageName": "English", "method": "none"}`

