"""Conversion helpers for temperatures, distances and weights.

Functions accept a numeric value and return a formatted string. When called
directly, they will prompt the user for input.
"""


def convert_to_fahrenheit(celsius=None):
    if celsius is None:
        celsius = float(input("What is the temperature in Celsius? "))
    new_fahrenheit = (celsius * 1.8) + 32
    return f"{round(new_fahrenheit, 1)} F"


def convert_to_celsius(fahrenheit=None):
    if fahrenheit is None:
        fahrenheit = float(input("What is the temperature in Fahrenheit? "))
    new_celsius = (fahrenheit - 32) / 1.8
    return f"{round(new_celsius, 1)} C"


def miles_to_kilometers(miles=None):
    if miles is None:
        miles = float(input("How many miles? "))
    new_kilometers = miles * 1.609
    return f"{round(new_kilometers, 1)} Kilometers"


def kilometers_to_miles(kilometers=None):
    if kilometers is None:
        kilometers = float(input("How many kilometers? "))
    new_miles = kilometers / 1.609
    return f"{round(new_miles, 1)} Miles"


def pounds_to_kilograms(pounds=None):
    if pounds is None:
        pounds = float(input("How many pounds? "))
    new_kilograms = pounds * 0.453592
    return f"{round(new_kilograms, 1)} Kilograms"


def kilograms_to_pounds(kilograms=None):
    if kilograms is None:
        kilograms = float(input("How many kilograms? "))
    new_pounds = kilograms / 0.453592
    return f"{round(new_pounds, 1)} Pounds"


actions = {
    "fahrenheit": convert_to_fahrenheit,
    "celsius": convert_to_celsius,
    "miles": miles_to_kilometers,
    "kilometers": kilometers_to_miles,
    "pounds": pounds_to_kilograms,
    "kilograms": kilograms_to_pounds,
}


if __name__ == "__main__":
    choice = (
        input(
            "Convert to Fahrenheit, Celsius, Miles, Kilometers, Pounds, or Kilograms? "
        )
        .strip()
        .lower()
    )
    value = float(input("Enter the number to convert: "))
    action = actions.get(choice)
    if action:
        print(action(value))
    else:
        print(
            "Invalid conversion type. Please choose from Fahrenheit, Celsius, Miles, Kilometers, Pounds, or Kilograms."
        )
