def tip_calculator():
    bill_amount = float(input("How much was the bill? "))
    people_splitting = int(input("How many people are splitting the bill? "))
    tip_percentage = float(input("What is the percentage you would like to tip? "))
    total_to_pay = bill_amount * (1 + tip_percentage / 100)
    amount_per_person = total_to_pay / people_splitting
    print(f"Each person should pay: £{amount_per_person:.2f}")
tip_calculator()