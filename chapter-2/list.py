rent = 1200
utilities = 300
groceries = 400
transportation = 150
entertainment = 200 

expenses = {
	"rent": rent,
	"utilities": utilities,
	"groceries": groceries,
	"transportation": transportation,
	"entertainment": entertainment,
}

going_out = 100
expenses["going out"] = going_out

print("Expenses List:", list(expenses.keys()))

sum_expenses = sum(expenses.values())

print("Total Expenses:", sum_expenses)

