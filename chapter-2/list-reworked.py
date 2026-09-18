from datetime import datetime

expenses = [
    {
        "description": "rent",
        "amount": 1200,
        "category": "housing",
        "date": datetime.strptime("2023-01-01", "%Y-%m-%d"),
    },
    {
        "description": "utilities",
        "amount": 300,
        "category": "housing",
        "date": datetime.strptime("2023-01-02", "%Y-%m-%d"),
    },
    {
        "description": "groceries",
        "amount": 400,
        "category": "food",
        "date": datetime.strptime("2023-01-03", "%Y-%m-%d"),
    },
    {
        "description": "transportation",
        "amount": 150,
        "category": "transportation",
        "date": datetime.strptime("2023-01-04", "%Y-%m-%d"),
    },
    {
        "description": "entertainment",
        "amount": 200,
        "category": "entertainment",
        "date": datetime.strptime("2023-01-05", "%Y-%m-%d"),
    },
]

expenses.append(
    {
        "description": "going out",
        "amount": 100,
        "category": "entertainment",
        "date": datetime.strptime("2023-01-06", "%Y-%m-%d"),
    }
)

print("Expenses List:")
print(f"{'Description':<20} {'Amount':>12} {'Category':<20} {'Date':<30}")
print("-" * 86)

for expense in expenses:
    print(
        f"{expense['description']:<20} "
        f"${expense['amount']:>11,.2f} "
        f"{expense['category']:<20} "
        f"{expense['date']!s:<30}"
    )

sum_expenses = sum(expense["amount"] for expense in expenses)

print("Total Expenses:", sum_expenses)
