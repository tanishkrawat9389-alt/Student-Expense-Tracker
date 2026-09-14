# Student Expense Tracker

A simple, beginner-friendly **Python command-line Student Expense Tracker** that stores expenses in a local JSON file.

## Features

- Add an expense with amount, category, description and date
- View all saved expenses
- Calculate total spending
- View spending by category
- Generate a monthly spending report
- Delete an expense by ID
- Persistent storage using `expenses.json`
- Input validation for amounts, categories, dates and menu choices

## Categories

Food, Travel, Education, Bills, Shopping and Other.

## Requirements

- Python 3.9+
- No external packages are required

## How to Run

```bash
python main.py
```

## Example

```text
================================================
        STUDENT EXPENSE TRACKER
================================================

1. Add expense
2. View expenses
3. Spending summary
4. Monthly report
5. Delete expense
0. Exit
Choose an option: 1

--- ADD EXPENSE ---
Amount (₹): 250

Categories:
1. Food
2. Travel
3. Education
4. Bills
5. Shopping
6. Other
Choose category: 1
Description: College canteen
Date (YYYY-MM-DD, blank for today):
Expense added successfully. ID: 1
```

## Project Structure

```text
Student-Expense-Tracker/
├── main.py              # CLI and user interaction
├── expense_manager.py   # Expense model, validation, persistence and calculations
├── expenses.json        # Local expense data
└── README.md
```

## Data Format

Each saved expense contains an ID, amount, category, description and date. Data is stored locally as JSON so it remains available the next time the application starts.
