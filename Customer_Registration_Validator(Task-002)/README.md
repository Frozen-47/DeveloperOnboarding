# Customer Registration Validator 🐍

A simple Python program that validates customer registration details and displays a registration success or failure message.

Built as **Task 002** of my Python software development practice.

## Features

- Validate customer names (cannot be empty or contain only spaces).
- Validate age (must be between 18 and 100).
- Validate email (must contain `@` and `.`).
- Validate phone numbers (must contain exactly 10 digits).
- Handle invalid age input using exception handling.
- Display validation errors and a formatted registration result.

## Technologies Used

- Python 3
- Functions
- Conditional statements
- String methods
- Exception handling (`try-except`)

## Project Structure

```text
Customer_Registration_Validator(Task-002)/
├── registration_validator.py
└── README.md
```

## How to Run

Make sure Python 3 is installed, then run:

```bash
python registration_validator.py
```

## Sample Input

```text
Enter Your Name: Arun
Enter Your Age (18 - 100): 22
Enter Your email: arun@gmail.com
Enter Your phone: 9876543210
```

## Sample Output

```text
========================================
        REGISTRATION SUCCESSFUL
----------------------------------------
Customer Name : Arun
Age           : 22
Email         : arun@gmail.com
Phone         : 9876543210
========================================
```

## How It Works

1. Collects customer details using `input()`.
2. Validates name, age, email, and phone using separate functions.
3. Uses `try-except` to handle invalid age values.
4. Displays error messages for invalid fields.
5. Shows registration success only when all details are valid.

## What I Learned

- Creating reusable validation functions.
- Validating user input with conditional statements.
- Using string methods such as `strip()` and `isdigit()`.
- Handling errors using `try-except`.
- Combining Boolean results to determine registration status.
- Formatting console output.

## Project Status

**Completed — Task 002**

*Built as part of my Python software development practice.*