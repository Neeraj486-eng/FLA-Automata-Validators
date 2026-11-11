"""FLA Automata Validators: password, simplified email, and ATM PIN checks."""

SPECIAL_CHARS = set("!@#$%^&*()-_=+[]{};:,.?/")


def password_dfa(password: str) -> bool:
    """Accept 8-16 ASCII characters with upper, lower, digit and special char."""
    if not 8 <= len(password) <= 16:
        return False

    # Each bit records whether a required character class has appeared.
    UPPER, LOWER, DIGIT, SPECIAL = 1, 2, 4, 8
    seen = 0
    for char in password:
        if "A" <= char <= "Z":
            seen |= UPPER
        elif "a" <= char <= "z":
            seen |= LOWER
        elif "0" <= char <= "9":
            seen |= DIGIT
        elif char in SPECIAL_CHARS:
            seen |= SPECIAL
        else:
            return False  # Spaces and unsupported characters are rejected.

    return seen == (UPPER | LOWER | DIGIT | SPECIAL)


def email_dfa(email: str) -> bool:
    """Accept a deliberately simplified email grammar (not full RFC syntax)."""
    if not email or email.count("@") != 1:
        return False

    local, domain = email.split("@")
    if not local or not domain or "." not in domain:
        return False

    # Local part: alphanumeric groups separated by one '.', '_' or '-'.
    if not local[0].isalnum() or not local[-1].isalnum():
        return False
    previous_separator = False
    for char in local:
        if char.isascii() and char.isalnum():
            previous_separator = False
        elif char in "._-" and not previous_separator:
            previous_separator = True
        else:
            return False

    # Domain: one alphanumeric label, a dot, and a 2+ letter suffix.
    if domain.count(".") != 1:
        return False
    host, suffix = domain.split(".")
    if not host or not suffix or len(suffix) < 2:
        return False
    if not all(c.isascii() and c.isalnum() for c in host):
        return False
    if not all(c.isascii() and c.isalpha() for c in suffix):
        return False
    return True


def pin_dfa(pin: str) -> bool:
    """Accept exactly four ASCII digits; leading zeroes are allowed."""
    return len(pin) == 4 and all("0" <= char <= "9" for char in pin)


def main() -> None:
    validators = {
        "1": ("Password", password_dfa),
        "2": ("Email", email_dfa),
        "3": ("ATM PIN", pin_dfa),
    }

    while True:
        print("\n=== FLA Automata Validators ===")
        print("1. Password structure verification")
        print("2. Simplified email syntax validation")
        print("3. Four-digit ATM PIN validation")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "4":
            print("Exiting program.")
            break
        if choice not in validators:
            print("Invalid option. Choose 1, 2, 3, or 4.")
            continue

        name, validator = validators[choice]
        value = input(f"Enter {name}: ")
        print("ACCEPTED" if validator(value) else "REJECTED")


if __name__ == "__main__":
    main()
