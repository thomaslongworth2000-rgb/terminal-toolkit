from datetime import datetime, timezone

expenses = []
number_of_expenses = int(input("How many expenses would you like to enter? "))

for expense_number in range(number_of_expenses):
    description = input(f"Expense {expense_number + 1} description: ")
    amount = float(input(f"Expense {expense_number + 1} amount: "))
    category = input(f"Expense {expense_number + 1} category: ")
    date = datetime.strptime(
        input(f"Expense {expense_number + 1} date (YYYY-MM-DD): "),
        "%Y-%m-%d",
    ).replace(tzinfo=timezone.utc)

    expenses.append(
        {
            "description": description,
            "amount": amount,
            "category": category,
            "date": date,
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
