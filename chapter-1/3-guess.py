import random

difficulty = input("Choose a difficulty level: Easy or Hard? ").strip().lower()

if difficulty == "easy":
    secret_number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        
        if guess < 1 or guess > 10:
            print("Please enter a valid number between 1 and 10.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("You guessed it! The secret number is", secret_number)
            break

elif difficulty == "hard":
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < 1 or guess > 100:
            print("Please enter a valid number between 1 and 100.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("You guessed it! The secret number is", secret_number)
            break

else:
    print("Invalid difficulty selected.")

print("You have completed the game! Thank you for playing.")
