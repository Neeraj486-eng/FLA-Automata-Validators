# FLA Automata Validators

A Python project demonstrating finite automata concepts through three simple real-time-style format validators:

1. Password structure verification
2. Simplified email syntax validation
3. Four-digit ATM PIN format validation

## Objectives

- Apply finite-state-machine ideas to practical input-validation examples.
- Identify states, transitions, alphabets, and accepting conditions.
- Distinguish format validation from full authentication or real-world verification.

## Requirements

- Python 3.8 or later
- No third-party packages are required.

## Run the project

```bash
python main.py
```

Select an option from the menu, enter a value, and observe whether it is accepted or rejected.

## Automata specifications

### 1. Password validator

- Input length: 8 to 16 characters.
- Must contain at least one uppercase letter, one lowercase letter, one digit, and one permitted special character.
- Permitted special characters: `!@#$%^&*()-_=+[]{};:,.?/`
- Spaces and all other characters are rejected.
- The implementation tracks the four required character classes using a four-bit state mask, along with the input length.

### 2. Simplified email validator

The accepted pattern is:

```text
alphanumeric+ ( [._-] alphanumeric+ )* @ alphanumeric+ . letter{2,}
```

This is an educational simplification. It permits one dot in the domain and does not support every valid email form or subdomains.

### 3. ATM PIN validator

- Exactly four ASCII digits.
- Leading zeroes are allowed.
- Any non-digit or any other length is rejected.

## Example inputs

| Validator | Accepted examples | Rejected examples |
|---|---|---|
| Password | `Abcdef1!`, `Hello123@`, `A1!bcdef`, `Password1#`, `Zebra9@tree` | `abcdef1!`, `ABCDEF1!`, `Abcdefgh!`, `Abcdef12`, `Ab1!` |
| Email | `alex@example.com`, `a1@test.org`, `john.doe@mail.net`, `user_name@host.in`, `first-last@site.edu` | `@example.com`, `alexexample.com`, `alex@.com`, `alex@example.c`, `alex..doe@example.com` |
| PIN | `1234`, `0000`, `2580`, `9876`, `0042` | `123`, `12345`, `12a4`, `12 4`, `+123` |

## Important limitations

- Password validation checks structure only. It does not authenticate a user, securely store passwords, or assess password strength beyond the listed rules.
- PIN validation checks only the four-digit format. It is not an ATM login system and does not verify a PIN against an account.
- Email validation checks a simplified syntax only. It does not confirm that a domain or mailbox exists.

## Project structure

```text
FLA-Automata-Validators/
├── main.py
├── README.md
├── requirements.txt
├── diagrams/
│   ├── password_dfa.md
│   ├── email_dfa.md
│   └── pin_dfa.md
└── test_cases/
    └── test_cases.md
```

## Conclusion

This project demonstrates how finite automata can model input patterns by reading symbols, updating states, and deciding acceptance. The three examples show how the same core idea can be applied to different validation tasks.
