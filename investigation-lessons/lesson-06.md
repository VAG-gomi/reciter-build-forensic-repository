# Lesson 6 — Measurement → Ranking → Decision

**Status:** Established conceptual distinction and cross-checked against the recorded Reciter behaviour  
**Central question:** Does the candidate with the highest score automatically become an accepted classification?

## 1. Three separate stages

```text
MEASUREMENT
    ↓
RANKING
    ↓
DECISION
```

A measurement produces values. Ranking orders the candidates by those values. A decision applies an acceptance rule and determines what the system will report.

These stages should not be collapsed into one.

## 2. Illustrative example

The following values are a teaching example, not a recorded Reciter test result:

| Candidate | Score |
|---|---:|
| English | 0.42 |
| Spanish | 0.51 |
| French | 0.48 |
| German | 0.31 |

Spanish is the highest-ranked candidate. But if the acceptance boundary is `0.60`:

```text
0.51 < 0.60
```

Spanish wins the ranking but does not pass the acceptance rule.

## 3. The Reciter distinction

The original Reciter can calculate a highest-scoring n-gram profile and still return a fixed English fallback when the n-gram confidence is below its acceptance threshold.

The source logic uses a `60` threshold for the n-gram path. If the threshold is not met, the result is set to:

```text
languageCode: en-US
languageName: English
confidence: 35
method: fallback
```

The value `35` is the fallback value. It is not evidence that the input is 35% English.

For empty input, the implementation has a separate `method: none` result with confidence `0`.

## 4. Core distinctions

```text
winner ≠ accepted classification
score  ≠ probability
fallback ≠ language finding
similarity ≠ truth
```

A winner answers: “Which candidate scored highest among those measured?”

An acceptance rule answers: “Does the available evidence meet the system's criterion for returning a classification?”

A fallback answers: “What predetermined output does the implementation return when its conditions are not met?” It does not necessarily answer which language is actually present.

## 5. Cross-project architectural comparison

The session compared the Reciter's stages with patterns from three frozen project references. These were used as conceptual comparisons, not as proof that Reciter should copy their implementation.

### MAF pattern

```text
computed metric
      ↓
pre-registered rule
      ↓
verdict
```

A metric and a verdict are separate. An insufficient result can remain inconclusive.

### LHE pattern

```text
candidate measurement
      ↓
ranking
      ↓
selection
```

The highest score is a selection among represented candidates, not automatically a calibrated probability.

### CFHM pattern

```text
raw evidence
      ↓
ranking
      ↓
evidence-quality / stability gate
      ↓
decision-grade status
      ↓
classification
```

The comparison highlights the role of evidence quality between ranking and final decision.

## 6. Consolidated model

```text
observation
    ↓
measurement
    ↓
ranking
    ↓
evidence quality
    ↓
decision
```

The evidence-quality stage may include sample adequacy, feature coverage, discrimination between candidates, stability and uncertainty. The exact measures still need to be defined for a particular task.

## 7. What was established and what was not

**ESTABLISHED:** A ranking winner can fail an acceptance threshold. A fallback value must not be interpreted as a measured language proportion. Measurement, ranking and decision are distinct operations.

**NOT ESTABLISHED:** That a threshold of `60` is optimal; that the current profile scores are calibrated probabilities; or that the comparative architectures prove a particular future Reciter design.

**UNKNOWN:** How to calibrate thresholds across languages, sample lengths and mixed-language input.

## 8. Principle

> A candidate can win the ranking without earning an accepted decision.

**Next question:** Even when a score is high, how do we know whether the underlying evidence is strong enough for the question we are asking?
