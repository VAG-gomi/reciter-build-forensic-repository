# Lesson 2 — Keyboard → IME → Input System

**Status:** Established conceptual architecture  
**Central question:** Where does interpretation occur between the keyboard interface and the receiving application?

## 1. Layered model

```text
Keyboard UI
    ↓
IME / Input Method
    ↓
Android input system
    ↓
Focused application
```

A more explicit conceptual path is:

```text
user gesture or key event
          ↓
keyboard interface
          ↓
input-method logic and state
          ↓
Android input-method framework / connection
          ↓
focused text editor
```

This is a responsibility diagram. It does not claim that every box must be a separate process, package or independently deployed component.

## 2. What each layer contributes

### Keyboard interface
Presents the visible controls and captures the user's interactions.

### IME / input method
Interprets incoming events. It may maintain a composing buffer, use previous input as context, apply rules, offer candidates and decide when text is ready to be committed.

### Android input system
Provides the framework through which an input method interacts with the currently focused editor. The IME is not simply drawing characters directly onto the application's screen.

### Focused application
Receives the committed text or editing operation through its text-input interface.

## 3. Stateful interpretation

The lesson's central model was:

```text
previous input
      +
current input
      +
rules / state
      =
current interpretation
```

A current event may be ambiguous in isolation but interpretable when combined with earlier events. That is why the input method's buffer and context can matter.

## 4. Rules do not require AI

**ESTABLISHED:** A deterministic rule system can transform an input sequence. A system can keep state, wait for more input, apply a mapping and then commit a result without an AI service.

**NOT ESTABLISHED:** That every keyboard uses only deterministic rules, or that every input method uses the same buffering and candidate-selection design.

## 5. Connection to tokenisation

Incoming events can be grouped into units before interpretation. The input method must have some operational idea of whether it should keep waiting for more input or process what it has received.

```text
incoming events
      ↓
buffer / context
      ↓
unit formation
      ↓
interpretation
      ↓
committed output
```

This led to a broader question: what counts as a meaningful unit of input?

## 6. Principle

> Input does not have to equal output.

The input method can preserve earlier events, use rules and interpret the current sequence as a whole.

## 7. Boundaries and open questions

The diagram is a conceptual explanation of responsibilities, not a complete Android implementation specification. The exact APIs, lifecycle and composition behaviour of a particular IME require platform-specific technical documentation and tests.

**Next question:** How does a system determine what the text represents, and why is identifying its writing system not the same as identifying its language?
