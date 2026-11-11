# Finite Automata for Real-Time Validation

## Project Details

- **Course:** Formal Languages and Automata (FLA)
- **Project Title:** Designing Automata for Real-Time Applications
- **Student Name:** K Neeraj
- **Register Number:** RA2411026050023

---

## 1. Introduction

Finite Automata are mathematical models used to recognize patterns and validate strings based on predefined rules. This project demonstrates the practical application of Deterministic Finite Automata (DFA) through three real-time validation examples.

## 2. Applications

### 2.1 Password Validation

The password validator checks whether a password satisfies the following conditions:

- Length must be between 8 and 16 characters.
- At least one uppercase letter.
- At least one lowercase letter.
- At least one digit.
- At least one permitted special character.
- Spaces and unsupported characters are rejected.

**Example:**
- Accepted: `Abcdef1!`
- Rejected: `abcdef1!`

### 2.2 Email Validation

The email validator checks a simplified email syntax using finite automata.

**Rules:**
- Must contain a valid alphanumeric username.
- Optional dots, underscores, or hyphens may separate username parts.
- Must contain `@`.
- Must have a domain name.
- Must end with at least two alphabetic characters.

**Example:**
- Accepted: `alex@example.com`
- Rejected: `alexexample.com`

### 2.3 ATM PIN Validation

The PIN validator checks whether the entered PIN contains exactly four digits.

**Rules:**
- PIN must contain exactly four digits.
- Only numeric characters are accepted.
- Leading zeros are allowed.

**Example:**
- Accepted: `1234`
- Rejected: `12345`

---

## 3. Technologies Used

- Python
- Finite Automata
- Deterministic Finite Automata (DFA)
- Regular Languages

## 4. How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone https://github.com/Neeraj486-eng/FLA-Automata-Validators.git
```

**Step 2:** Open the project folder.

```bash
cd FLA-Automata-Validators
```

**Step 3:** Run the Python program.

```bash
python main.py
```

No third-party libraries are required.

## 5. Project Structure

```text
FLA-Automata-Validators/
│
├── main.py
├── README.md
├── requirements.txt
│
├── diagrams/
│   ├── password_dfa.md
│   ├── email_dfa.md
│   └── pin_dfa.md
│
└── test_cases/
    └── test_cases.md
```

## 6. Testing

The project includes test cases for all three validators.

- Password validation: accepted and rejected password examples.
- Email validation: accepted and rejected email examples.
- PIN validation: accepted and rejected PIN examples.

Refer to the `test_cases` folder for the complete test cases.

## 7. Limitations

- Password validation checks only the specified format, not actual authentication.
- Email validation uses a simplified syntax and does not verify whether an email address exists.
- PIN validation checks only the four-digit format and does not perform ATM authentication.

## 8. Conclusion

This project demonstrates how finite automata can be applied to practical string-validation problems. By designing separate automata for password, email, and ATM PIN validation, the project connects theoretical concepts from Formal Languages and Automata with real-world applications.

---

**Developed by:** K Neeraj  
**Register Number:** RA2411026050023
