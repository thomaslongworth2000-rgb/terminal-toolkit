import csv
import json
from datetime import datetime, timezone

FILENAME = "expenses.json"


def load_expenses():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    loaded = []
    for item in data:
        if "date" in item and isinstance(item["date"], str):
            item = dict(item)
            item["date"] = datetime.fromisoformat(item["date"]).replace(
                tzinfo=timezone.utc
            )
        loaded.append(item)
    return loaded


def save_expenses():
    serializable = []
    for item in expenses:
        record = dict(item)
        record["date"] = record["date"].isoformat()
        serializable.append(record)

    with open(FILENAME, "w") as f:
        json.dump(serializable, f, indent=2)


expenses = load_expenses()


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
    save_expenses()


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
        save_expenses()
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
        save_expenses()
        print("Expense updated.")
    else:
        print("Invalid index.")


def calculate_total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print("Total Expenses:", total)


def total_expenses_by_category():
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    print("Total Expenses by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:,.2f}")


def filter_expenses_by_category():
    category = input("Enter category to filter by: ")
    filtered_expenses = [
        expense for expense in expenses if expense["category"] == category
    ]

    if filtered_expenses:
        print(f"Expenses in category '{category}':")
        print(f"{'Description':<20} {'Amount':>12} {'Category':<20} {'Date':<30}")
        print("-" * 86)
        for expense in filtered_expenses:
            print(
                f"{expense['description']:<20} "
                f"${expense['amount']:>11,.2f} "
                f"{expense['category']:<20} "
                f"{expense['date']!s:<30}"
            )
    else:
        print(f"No expenses found in category '{category}'.")


def filter_by_date_range():
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").replace(
            tzinfo=timezone.utc
        )
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").replace(
            tzinfo=timezone.utc
        )
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    filtered_expenses = [
        expense for expense in expenses if start_date <= expense["date"] <= end_date
    ]

    if filtered_expenses:
        print(f"Expenses from {start_date_str} to {end_date_str}:")
        print(f"{'Description':<20} {'Amount':>12} {'Category':<20} {'Date':<30}")
        print("-" * 86)
        for expense in filtered_expenses:
            print(
                f"{expense['description']:<20} "
                f"${expense['amount']:>11,.2f} "
                f"{expense['category']:<20} "
                f"{expense['date']!s:<30}"
            )
    else:
        print(f"No expenses found between {start_date_str} and {end_date_str}.")


def sort_expenses_by_date_or_amount():
    sort_choice = input("Sort by date (d) or amount (a)? ")
    if sort_choice == "d":
        expenses.sort(key=lambda x: x["date"])
    elif sort_choice == "a":
        expenses.sort(key=lambda x: x["amount"], reverse=True)
    print("Expenses sorted.")
    list_expenses()


def save_expenses_to_csv():
    rows = []
    for expense in expenses:
        row = dict(expense)
        row["date"] = row["date"].isoformat()
        rows.append(row)

    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["description", "amount", "category", "date"]
        )
        writer.writeheader()
        writer.writerows(rows)


while True:
    print(
        "1: add   2: list   3: delete   4: update   5: total   6: total by category   7: filter by category   8: filter by date range   9: sort   10: save to csv   11: quit"
    )
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
        total_expenses_by_category()
    elif choice == "7":
        filter_expenses_by_category()
    elif choice == "8":
        filter_by_date_range()
    elif choice == "9":
        sort_expenses_by_date_or_amount()
    elif choice == "10":
        save_expenses_to_csv()
    elif choice == "11":
        break
    else:
        print("Didn't understand that.")
