# Test Cases

Run the application with each sample value and compare the result with the expected output.

## Password validator

| Input | Expected |
|---|---|
| `Abcdef1!` | ACCEPTED |
| `Hello123@` | ACCEPTED |
| `A1!bcdef` | ACCEPTED |
| `Password1#` | ACCEPTED |
| `Zebra9@tree` | ACCEPTED |
| `abcdef1!` | REJECTED (no uppercase) |
| `ABCDEF1!` | REJECTED (no lowercase) |
| `Abcdefgh!` | REJECTED (no digit) |
| `Abcdef12` | REJECTED (no special character) |
| `Ab1!` | REJECTED (too short) |
| `Abcdefghijklmno1!X` | REJECTED (too long) |

## Simplified email validator

| Input | Expected |
|---|---|
| `alex@example.com` | ACCEPTED |
| `a1@test.org` | ACCEPTED |
| `john.doe@mail.net` | ACCEPTED |
| `user_name@host.in` | ACCEPTED |
| `first-last@site.edu` | ACCEPTED |
| `@example.com` | REJECTED (empty local part) |
| `alexexample.com` | REJECTED (missing @) |
| `alex@.com` | REJECTED (empty domain host) |
| `alex@example.c` | REJECTED (suffix too short) |
| `alex..doe@example.com` | REJECTED (repeated separator) |
| `alex@example.12` | REJECTED (suffix must contain letters) |

## PIN validator

| Input | Expected |
|---|---|
| `1234` | ACCEPTED |
| `0000` | ACCEPTED |
| `2580` | ACCEPTED |
| `9876` | ACCEPTED |
| `0042` | ACCEPTED |
| `123` | REJECTED (too short) |
| `12345` | REJECTED (too long) |
| `12a4` | REJECTED (contains a letter) |
| `12 4` | REJECTED (contains a space) |
| `+123` | REJECTED (contains a symbol) |
