# Employee Attendance Processor 🐍

A simple Python program that calculates employee attendance percentages, classifies attendance status, and generates an attendance report.

## Features

- Calculate employee attendance percentages.
- Classify attendance as Excellent, Good, or Low Attendance.
- Count employees with low attendance.
- Display individual employee details and a final summary.

## Technologies Used

- Python 3
- Functions
- Loops and conditional statements
- Lists and dictionaries

## Attendance Classification

| Attendance | Status |
|---|---|
| 90% and above | Excellent |
| 75% – below 90% | Good |
| Below 75% | Low Attendance |

## Project Structure

```text
employee-attendance-processor/
├── employee_attendance.py
└── README.md
```

## How to Run

1. Make sure Python 3 is installed.
2. Run the following command:

```bash
python employee_attendance.py
```

## Sample Output

```text
========== EMPLOYEE ATTENDANCE REPORT ==========

ID: 101
Name: Arun
Attendance: 88.00%
Status: Good
------------------------------
ID: 102
Name: Bala
Attendance: 72.00%
Status: Low Attendance
------------------------------
ID: 103
Name: Charan
Attendance: 100.00%
Status: Excellent
------------------------------
ID: 104
Name: Divya
Attendance: 80.00%
Status: Good
------------------------------
ID: 105
Name: Esha
Attendance: 60.00%
Status: Low Attendance
------------------------------

Total Employees: 5
Low Attendance Employees: 2
```

## How It Works

1. Employee details are stored in a list of dictionaries.
2. A function calculates each employee's attendance percentage.
3. Conditional statements determine attendance status.
4. A loop processes all employees.
5. The program displays the attendance report and summary.

**Formula:**

Attendance Percentage = (Present Days / Total Days) × 100

## What I Learned

- Working with lists and dictionaries.
- Creating and calling functions.
- Using loops and conditions.
- Formatting percentages.
- Counting records based on conditions.
- Fixing logical and indentation errors.

## Project Status

**Completed — Task 001**

*Built as part of my Python software development practice.*