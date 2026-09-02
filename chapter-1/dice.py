def roll_dice():

    import random 

    dice_sides = int(input("Enter the number of sides for the dice: "))
    dice_amount = int(input("Enter the number of dice to roll: "))

    total = 0

    for i in range(dice_amount):
        roll = random.randint(1, dice_sides)
        print("Roll", i + 1, ":", roll) 
        total += roll
    print("Total:", total)

roll_dice()
