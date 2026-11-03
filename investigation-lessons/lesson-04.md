# Lesson 4 — Tokenisation

**Status:** Established conceptual foundation, with technical refinements noted  
**Central question:** What constitutes a meaningful unit of input for a processing system?

## 1. Tokenisation is a design decision

Tokenisation is not merely splitting a string at spaces. It determines which units a later processing stage receives and therefore what that stage can observe.

A broad hierarchy is:

```text
code point
    ↓
character / grapheme
    ↓
token
    ↓
word
    ↓
phrase
    ↓
sentence
```

This is a conceptual hierarchy, not a rule that every language or system must follow in exactly this way.

## 2. The smallest visible unit is not always the useful unit

A code point is a Unicode value. A grapheme cluster is closer to what a reader may perceive as one character. A token is a unit selected for a particular processing task. These are not interchangeable concepts.

A system that treats every code point independently may split a user-perceived character. A system that treats only whole sentences as units may hide useful local structure. The appropriate unit depends on the question the next stage must answer.

## 3. Connection to the input-method buffer

The lesson used an open-buffer example:

```text
a    → WAIT
am   → WAIT
ami  → recognisable unit → PROCESS
```

This illustrates that a system can delay commitment while more input arrives. It is not a universal rule that `ami` is always a complete token or that every IME behaves this way.

## 4. Why tokenisation changes what can be measured

```text
key events
    ↓
buffer
    ↓
tokeniser
    ↓
interpreter
    ↓
output
```

The tokeniser decides what is grouped together. If the wrong boundary is chosen, the next stage may receive too little context, combine unrelated material or lose the relationship between a unit and its source.

## 5. Technical refinement: JavaScript iteration

JavaScript strings are UTF-16 sequences. `Array.from(text)` iterates Unicode code points rather than UTF-16 code units, but it does not automatically produce grapheme clusters. Therefore, a description such as “character-by-character” needs to say whether it means code units, code points or grapheme clusters.

This refinement matters when handling combining marks, emoji sequences and other text where one perceived character can contain multiple code points.

## 6. Principle

> Before a system can reason about input, it must establish what counts as an input unit.

A stronger formulation for later lessons is: **choose units according to the evidence question, and preserve enough source context to verify what those units represent.**

## 7. Boundaries and open questions

This lesson did not establish one universally correct tokeniser, one minimum token length or a complete multilingual segmentation method. It established that unit selection shapes downstream observation and measurement.

**Next question:** Once a unit has been selected, what is measured from it, and what information is removed before measurement?
