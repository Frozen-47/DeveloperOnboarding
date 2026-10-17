# Customer Records Manager 🐍

A simple menu-driven Customer Records Management System developed using Python.

This project allows users to add, view, search, update, and delete customer records through a command-line interface.

**Task 003 — Python Software Development Practice**

## Features

- Add customers with unique IDs
- View all customer records
- Search customers by ID
- Update existing customer information
- Delete customer records
- Validate customer name, email, and phone number
- Prevent duplicate customer IDs
- Handle invalid numeric inputs using exception handling
- Preserve existing records when an update fails
- Display the total number of customers

## Technologies Used

- Python 3.10+
- Lists and dictionaries
- Functions
- Loops and conditional statements
- Match-case statements
- Exception handling
- String methods

## Project Structure

```text
Customer_Records_Manager/
├── record_manager.py
└── README.md
```

## How to Run

1. Make sure Python 3.10 or later is installed.
2. Open a terminal in the project directory.
3. Run the program:

```bash
python record_manager.py
```

## Main Menu

```text
========== CUSTOMER RECORD MANAGER ==========

1. Add Customer
2. View All Customers
3. Search Customer
4. Update Customer
5. Delete Customer
6. Exit

Enter your choice:
```

## Sample Output

### Add Customer

```text
Enter Customer ID: 101
Enter Name: Arun
Enter Email: arun@gmail.com
Enter Phone: 9876543210

Customer added successfully!
```

### View Customers

```text
========== CUSTOMER LIST ==========

Customer ID: 101
Name       : Arun
Email      : arun@gmail.com
Phone      : 9876543210
----------------------------------
Total Customer: 1
```

### Search Customer

```text
Enter Customer ID: 101

Customer Found!

Customer ID: 101
Name       : Arun
Email      : arun@gmail.com
Phone      : 9876543210
```

### Update Customer

```text
Enter Customer ID: 101
Enter New Name: Arun Kumar
Enter New Email: arunkumar@gmail.com
Enter New Phone: 9876543210

Customer updated successfully!
```

### Delete Customer

```text
Enter Customer ID: 101

Customer deleted successfully!
```

## Validation Rules

| Field | Validation |
|---|---|
| Customer ID | Positive integer and unique |
| Name | Cannot be empty or contain only spaces |
| Email | Must contain `@` and `.` |
| Phone | Must contain exactly 10 numeric digits |

## How It Works

1. The program starts with an empty customer list.
2. The user selects an operation from the menu.
3. Customer IDs and input fields are validated.
4. The selected operation is performed.
5. The program returns to the menu until the user selects Exit.

Customer records are stored in memory using a list of dictionaries. Records are not saved after the program exits.

## What I Learned

- Implementing CRUD operations
- Managing records with lists and dictionaries
- Writing reusable functions
- Validating user input
- Handling errors using `try-except`
- Searching records using a unique identifier
- Preventing unintended data changes
- Building menu-driven command-line applications

## Project Status

**Completed — Task 003**

Built as part of my Python software development practice.