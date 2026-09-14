import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional

DATA_FILE = Path(__file__).with_name("expenses.json")
CATEGORIES = ("Food", "Travel", "Education", "Bills", "Shopping", "Other")

@dataclass
class Expense:
    expense_id: int
    amount: float
    category: str
    description: str
    date: str

class ExpenseManager:
    """Handles expense persistence and business operations."""
    def __init__(self, data_file: Path = DATA_FILE):
        self.data_file = data_file
        self.expenses: List[Expense] = []
        self.load()

    def load(self) -> None:
        if not self.data_file.exists() or self.data_file.stat().st_size == 0:
            self.expenses = []
            return
        try:
            raw = json.loads(self.data_file.read_text(encoding="utf-8"))
            self.expenses = [Expense(**item) for item in raw]
        except (json.JSONDecodeError, TypeError, ValueError):
            self.expenses = []

    def save(self) -> None:
        self.data_file.write_text(json.dumps([asdict(e) for e in self.expenses], indent=2), encoding="utf-8")

    def add_expense(self, amount: float, category: str, description: str, date: Optional[str] = None) -> Expense:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if category not in CATEGORIES:
            raise ValueError("Invalid category.")
        if not description.strip():
            raise ValueError("Description cannot be empty.")
        date = date or datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError("Date must be in YYYY-MM-DD format.") from exc
        expense = Expense(max((e.expense_id for e in self.expenses), default=0) + 1, round(amount, 2), category, description.strip(), date)
        self.expenses.append(expense)
        self.save()
        return expense

    def delete_expense(self, expense_id: int) -> bool:
        for index, expense in enumerate(self.expenses):
            if expense.expense_id == expense_id:
                del self.expenses[index]
                self.save()
                return True
        return False

    def get_expense(self, expense_id: int) -> Optional[Expense]:
        return next((e for e in self.expenses if e.expense_id == expense_id), None)

    def recent(self, limit: int = 10) -> List[Expense]:
        return sorted(self.expenses, key=lambda e: (e.date, e.expense_id), reverse=True)[:limit]

    def total(self) -> float:
        return round(sum(e.amount for e in self.expenses), 2)

    def total_by_category(self) -> dict:
        totals = {category: 0.0 for category in CATEGORIES}
        for expense in self.expenses:
            totals[expense.category] += expense.amount
        return {key: round(value, 2) for key, value in totals.items()}

    def monthly_total(self, year: int, month: int) -> float:
        total = 0.0
        for expense in self.expenses:
            d = datetime.strptime(expense.date, "%Y-%m-%d")
            if d.year == year and d.month == month:
                total += expense.amount
        return round(total, 2)
