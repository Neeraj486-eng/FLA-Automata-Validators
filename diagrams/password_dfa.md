# Password DFA (conceptual state model)

The validator tracks the input length and four flags: uppercase (U), lowercase (L), digit (D), and special character (S). The accepting condition is reached only when the length is 8–16 and all four flags are set. Any unsupported character or length beyond 16 leads to rejection.

```mermaid
flowchart TD
    A([Start]) --> B[Read characters and update U/L/D/S flags]
    B --> C{Unsupported character or length > 16?}
    C -- Yes --> X([Reject])
    C -- No --> D{End of input?}
    D -- No --> B
    D -- Yes --> E{Length 8–16 and U, L, D, S all set?}
    E -- Yes --> F([Accept])
    E -- No --> X
```

This is a compact conceptual representation of a product DFA; each distinct combination of length and flags corresponds to a state.
