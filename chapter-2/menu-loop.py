from datetime import datetime, timezone

expenses = []

def add_expense():
    description = input("Description: ")
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = datetime.strptime(
        input("Date (YYYY-MM-DD): "),
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

def list_expenses():
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

def delete_expense():
    list_expenses()
    index = int(input("Enter the index of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        del expenses[index]
        print("Expense deleted.")
    else:
        print("Invalid index.")

def update_expense():
    list_expenses()
    index = int(input("Enter the index of the expense to update: ")) - 1
    if 0 <= index < len(expenses):
        description = input("New Description: ")
        amount = float(input("New Amount: "))
        category = input("New Category: ")
        date = datetime.strptime(
            input("New Date (YYYY-MM-DD): "),
            "%Y-%m-%d",
        ).replace(tzinfo=timezone.utc)

        expenses[index] = {
            "description": description,
            "amount": amount,
            "category": category,
            "date": date,
        }
        print("Expense updated.")
    else:
        print("Invalid index.")

def calculate_total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print("Total Expenses:", total)

while True:
    print("1: add   2: list   3: delete   4: update   5: total   6: quit")
    choice = input("> ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        update_expense()
    elif choice == "5":
        calculate_total_expenses()
    elif choice == "6":
        break
    else:
        print("Didn't understand that.")