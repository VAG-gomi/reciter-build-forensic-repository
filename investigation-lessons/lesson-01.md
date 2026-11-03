# Lesson 1 — Input → Interpretation → Output

**Status:** Established conceptual foundation  
**Central question:** How does an input action become the text or result that an application receives?

## 1. Core model

```text
INPUT
  ↓
INTERPRETATION
  ↓
OUTPUT
```

The visible keyboard is not the complete input system. What a person touches or types is an input event. A processing layer interprets that event, and the resulting text is delivered to the focused application.

## 2. What was established

- A touch or key action is an input event.
- The visible keyboard interface is only one part of the process.
- An input method can interpret an event before text reaches the application.
- The resulting text does not have to be identical to the physical or virtual key action.
- An input method can maintain internal state and perform transformations without using AI.

## 3. Why input and output can differ

An input system may buffer, compose, transform or select among possible outputs. A user action can therefore be an instruction to the input method rather than the final character itself.

Illustrative model:

```text
user action
   ↓
input event
   ↓
interpretation using current context and rules
   ↓
committed text
```

The exact interpretation depends on the input method's rules and state. This lesson did not establish the internal implementation of any one keyboard product.

## 4. Important distinction

**OBSERVED / conceptual:** The user performs an action and the system produces an output.

**INFERRED:** There must be some mechanism between the raw action and the committed text whenever the output is transformed or depends on prior input.

**NOT ESTABLISHED:** That this mechanism must be an AI model. Rule-based and stateful systems can also transform input.

## 5. Principle

> The visible keyboard is not the whole keyboard.

This means that the visible keys do not reveal the entire input-processing architecture. The interpretation mechanism and its state matter too.

## 6. Boundaries and open questions

This introductory model does not specify Android's exact API calls, the details of a particular IME, or the ideal tokenisation method. Those require separate investigation.

**Next question:** Which software layer performs the interpretation, and how does it communicate with the focused application?
