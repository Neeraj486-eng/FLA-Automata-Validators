# Simplified Email DFA

The diagram represents the simplified grammar used by `email_dfa`. `qA` is the accepting state; invalid transitions lead to the dead state `qD`.

```mermaid
flowchart TD
    S([Start]) --> Q0[q0: read local alphanumeric]
    Q0 --> Q1[q1: local alphanumeric]
    Q1 --> Q1
    Q1 --> Q2[q2: local separator . _ -]
    Q2 --> Q1
    Q1 --> Q3[q3: @]
    Q3 --> Q4[q4: domain alphanumeric]
    Q4 --> Q4
    Q4 --> Q5[q5: .]
    Q5 --> Q6[q6: suffix letter 1]
    Q6 --> Q7[q7: suffix letter 2+]
    Q7 --> Q7
    Q7 --> A([Accept])
    Q0 -. invalid .-> D([Dead / Reject])
```

The implementation also rejects repeated or trailing local-part separators and requires exactly one `@` and one domain dot.
