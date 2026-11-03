# Lesson 8 — Evidence Units & Multi-Resolution Representation

**Status:** Investigations 1–2 and domain-transfer review recorded as completed; Investigation 3 proposed and still open  
**Central question:** What evidence units and representation structure can support multilingual detection without destroying information needed by later measurements?

## 1. Starting point from Lesson 7

Lesson 7 established a requirement, not an implementation design:

> Preserve enough original content, position, boundary information, local evidence and uncertainty to answer the question the system is meant to answer.

Lesson 8 examined what that requirement implies for evidence units and representation architecture.

## 2. Investigation 1 — What makes a unit of text an appropriate unit of evidence?

### Question

What makes a unit of text an appropriate unit of evidence for multilingual detection?

### Candidate units considered

- Code point.
- Character or grapheme cluster.
- Subword or token.
- Word.
- Phrase.
- Sentence.
- Script run.
- Fixed-size window.
- Inferred language span.
- Whole document.

### Finding

There is no universally correct evidence unit. The appropriate unit depends on the question being asked and the evidence needed to answer it.

A useful unit must be assessed against at least four considerations:

1. **Locality:** Does the unit identify where its evidence came from?
2. **Context:** Does it retain enough surrounding material to interpret the evidence?
3. **Boundary integrity:** Can its relationship to source boundaries and segmentation decisions be checked?
4. **Question fit:** Is the unit suitable for the particular measurement or classification question?

### Three things that must not be collapsed

```text
SOURCE UNIT
    ↓
where the source is divided or referenced

MEASUREMENT UNIT
    ↓
which region/features are measured

EVIDENCE RECORD
    ↓
what was measured, where, by which method,
with which candidates and uncertainty
```

The physical or logical source unit is not the same thing as the region used for a measurement, and neither is identical to the full evidence record.

### Technical qualification

In JavaScript, `Array.from(text)` iterates code points rather than UTF-16 code units. It does not, by itself, segment grapheme clusters. Therefore, “character” must be defined precisely in an implementation discussion.

### Principle

> Choose the smallest unit that preserves enough discriminating evidence for the question, while retaining the source boundaries and context needed to verify what that evidence means.

## 3. Investigation 2 — Can one evidence unit satisfy every requirement?

### Question

Can one evidence unit satisfy all requirements of multilingual detection, or does useful evidence representation require multiple levels?

The investigation compared four broad models:

- **A — Single unit:** One fixed unit is used for all evidence and measurements.
- **B — Nested units:** Smaller units are grouped into larger units.
- **C — Source plus independent measurements:** Preserve one source representation and measure different regions or resolutions from it.
- **D — Adaptive evidence:** Select measurement regions or resolutions according to the available evidence and the question.

The examination used test situations including monolingual text, separate-language sentences, intra-sentence code-switching, shared-script multilingual text and very short inputs.

### Central finding

The evidence does not establish one universally correct unit or one mandatory segmentation hierarchy. It supports the need to preserve enough information for multiple resolutions of analysis when the task requires them.

### Key distinction

```text
one preserved source representation
              ↓
     multiple measurements
              ↓
    evidence at different scales
```

The source and its coordinate/boundary information can remain stable while downstream measurements inspect different ranges, windows or spans.

### Storage versus measurement

The investigation did not establish that the system must store multiple independent copies of the original text. A sufficiently rich source representation could, in principle, support multiple measurements, provided it preserves the content, order, coordinates, boundary information and context required by those measurements.

Derived representations or indexes may still be added for access speed, efficient measurement or other computational constraints. Their use is an implementation decision, not a conclusion that multiple original-source copies are conceptually necessary.

### Principle

> Preserve one sufficiently rich, coordinate-bearing source representation so that later measurements at different resolutions remain possible; add derived representations only when measurement, access or computational constraints justify them.

## 4. Domain-transfer review — biological sequence analogy

The user noticed a possible structural resemblance between multi-resolution text evidence and biological information systems, particularly the relationship between DNA and RNA.

### What the analogy contributed

At a high level, the analogy prompted a useful question:

> Can one ordered source carry information that supports several different levels of analysis or operation?

The transferable abstraction was:

```text
ordered source sequence
        ↓
local patterns / regions
        ↓
larger patterns and context
        ↓
question-specific interpretation
```

This helped separate the idea of a preserved source from the different operations that can inspect it.

### What the analogy does not establish

- It does not make human language equivalent to DNA.
- It does not imply that DNA literally stores human languages.
- It does not prove that Reciter requires a biological architecture.
- It does not prove that one source representation is sufficient for every computational task.
- It does not prove that every useful measurement must be nested or non-overlapping.

DNA/RNA was used as a conceptual prompt at the level of information representation and different operations on an ordered biological sequence. It is not a literal engineering specification for Reciter and is not experimental evidence about language detection.

Biological sequences also contain variation, noise, redundancy and context dependence. The analogy should not be simplified into a claim that biological information has a perfect or uniformly regular rhythm.

## 5. Domain-transfer review — recorded outcome

A 60-question review was used to test the transfer of the representation principles across the biological analogy and the Reciter evidence problem.

The preserved outcome was:

- No universally correct evidence unit was established.
- Locality, context, boundary information, candidate alternatives, provenance and uncertainty remain important.
- The analogy supports multi-resolution interpretation over one ordered source, but does not prove a literal biological-to-language architecture.
- There is no evidence that multiple independent stored copies are necessary.
- One sufficiently rich source representation could in principle support multiple measurements if content, order, coordinates, boundaries and script observations remain recoverable.
- Derived indexes may be justified for efficiency, but that is separate from the conceptual requirement to preserve information.
- No earlier lesson conclusion was overturned; Lesson 7's representation requirement was clarified.

The complete verbatim user answers to all 60 questions are not reproduced in this file. This section records the consolidated outcome available in the session history, not a transcript of every answer.

## 6. Clarification to Lesson 7

Lesson 7 established that multilingual evidence needs to remain available at the structural level of the question. Lesson 8 clarifies that this does **not** require storing multiple independent copies or committing to one fixed segmentation hierarchy.

A precise clarification is:

> Preserve a sufficiently rich, coordinate-bearing source representation so that later measurements at different resolutions remain possible; add derived representations only when measurement, access or computational constraints justify them.

This is a clarification of the representation requirement, not a replacement of the Lesson 7 conclusion.

## 7. Evidence classification

### ESTABLISHED within the investigation

- No universal evidence unit was identified.
- The appropriate unit depends on the question and discriminating evidence required.
- Source unit, measurement unit and evidence record are distinct concepts.
- Multiple measurement resolutions may be needed for multilingual analysis.
- The available reasoning does not require multiple independent copies of the original source.
- Preserving coordinates and the relationship to the source is important when measurements operate at different resolutions.

### INFERRED

- A coordinate-bearing source representation is a suitable conceptual foundation for multiple later measurements.
- Different measurements may refer to overlapping or differently sized regions of the same source.

### HYPOTHESIS / NOT YET TESTED

- An adaptive measurement strategy may be useful.
- Overlapping evidence windows may preserve useful context better than a single mutually exclusive segmentation.
- A future evidence architecture may combine source coordinates, local measurements and derived indexes.

### UNKNOWN

- The best measurement-window sizes.
- The minimum reliable span length for each language or script.
- Whether overlapping measurements improve accuracy or merely add cost.
- How to reconcile evidence from different resolutions.
- Which boundaries should be explicit, inferred or both.
- What data structure best balances preservation, access and computation.

## 8. Investigation 3 — Proposed next question, not yet answered

> **Can one preserved source representation support multiple overlapping evidence measurements at different resolutions without losing their relationship to the original source?**

This question follows directly from the Lesson 8 findings. It is preserved as the next investigation, not written as a conclusion.

Potential test cases include:

- two language spans that overlap at a transition;
- a short ambiguous region whose interpretation changes when more context is included;
- a measurement window that crosses a sentence or line boundary;
- overlapping windows that produce conflicting candidates;
- a source where one language appears inside a word or phrase from another language.

These are proposed probes. They are not recorded experiment results.

## 9. Final Lesson 8 principle

> Preserve the source once in a sufficiently rich, coordinate-bearing form; permit multiple question-specific measurements over it; preserve the provenance and uncertainty of each measurement; add derived structures only when there is a demonstrated reason.

## 10. Status boundary

**Completed:** Investigation 1, Investigation 2, and the domain-transfer review as summarised above.  
**Clarified:** Lesson 7's representation requirement.  
**Not completed:** Investigation 3 on overlapping multi-resolution measurements.  
**Not authorised by this lesson:** A Reciter source redesign, implementation change or selection of a final segmentation algorithm.
