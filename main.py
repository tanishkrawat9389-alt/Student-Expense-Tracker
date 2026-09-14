from datetime import datetime
from expense_manager import CATEGORIES, ExpenseManager


def read_amount():
    while True:
        try:
            amount = float(input("Amount (₹): "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Please enter a valid amount greater than 0.")


def choose_category():
    print("\nCategories:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")
    while True:
        try:
            choice = int(input("Choose category: "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
        except ValueError:
            pass
        print("Invalid category. Try again.")


def add_expense(manager):
    print("\n--- ADD EXPENSE ---")
    amount = read_amount()
    category = choose_category()
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return
    date = input("Date (YYYY-MM-DD, blank for today): ").strip() or datetime.now().strftime("%Y-%m-%d")
    try:
        expense = manager.add_expense(amount, category, description, date)
        print(f"Expense added successfully. ID: {expense.expense_id}")
    except ValueError as exc:
        print(f"Error: {exc}")


def view_expenses(manager):
    print("\n--- ALL EXPENSES ---")
    if not manager.expenses:
        print("No expenses recorded yet.")
        return
    print(f"{'ID':<5}{'DATE':<13}{'CATEGORY':<13}{'AMOUNT':>12}  DESCRIPTION")
    print("-" * 70)
    for e in sorted(manager.expenses, key=lambda x: (x.date, x.expense_id), reverse=True):
        print(f"{e.expense_id:<5}{e.date:<13}{e.category:<13}₹{e.amount:>10.2f}  {e.description}")
    print(f"\nTOTAL SPENDING: ₹{manager.total():.2f}")


def summary(manager):
    print("\n--- SPENDING SUMMARY ---")
    print(f"Total spending: ₹{manager.total():.2f}")
    for category, amount in manager.total_by_category().items():
        if amount:
            print(f"{category:<12}: ₹{amount:.2f}")


def delete_expense(manager):
    print("\n--- DELETE EXPENSE ---")
    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    if manager.delete_expense(expense_id):
        print("Expense deleted successfully.")
    else:
        print("Expense ID not found.")


def monthly_report(manager):
    print("\n--- MONTHLY REPORT ---")
    try:
        year = int(input("Year (YYYY): "))
        month = int(input("Month (1-12): "))
        if not 1 <= month <= 12:
            raise ValueError
        print(f"Total for {year}-{month:02d}: ₹{manager.monthly_total(year, month):.2f}")
    except ValueError:
        print("Please enter a valid year and month.")


def main():
    manager = ExpenseManager()
    print("=" * 48)
    print("        STUDENT EXPENSE TRACKER")
    print("=" * 48)
    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Spending summary")
        print("4. Monthly report")
        print("5. Delete expense")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1": add_expense(manager)
        elif choice == "2": view_expenses(manager)
        elif choice == "3": summary(manager)
        elif choice == "4": monthly_report(manager)
        elif choice == "5": delete_expense(manager)
        elif choice == "0":
            print("Thank you for using Student Expense Tracker!")
            break
        else: print("Invalid choice. Please select 0-5.")


if __name__ == "__main__":
    main()
