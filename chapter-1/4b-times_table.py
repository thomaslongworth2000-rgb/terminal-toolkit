def times_table():
    number = int(input("Enter a number: "))

    for n in range(1, 13):
        product = number * n
        print(f"{number} x {n} = {product}")
times_table()