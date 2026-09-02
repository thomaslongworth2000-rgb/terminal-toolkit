convert_choice = (
    input("Convert to Fahrenheit, Celsius, Miles, Kilometers, Pounds, or Kilograms? ")
    .strip()
    .lower()
)

number = float(input("Enter the number to convert: "))

from converter import (
    convert_to_celsius,
    convert_to_fahrenheit,
    kilograms_to_pounds,
    kilometers_to_miles,
    miles_to_kilometers,
    pounds_to_kilograms,
)

actions = {
    "fahrenheit": convert_to_fahrenheit,
    "celsius": convert_to_celsius,
    "miles": miles_to_kilometers,
    "kilometers": kilometers_to_miles,
    "pounds": pounds_to_kilograms,
    "kilograms": kilograms_to_pounds,
}

action = actions.get(convert_choice)
if action:
    print(action(number))
else:
    print(
        "Invalid conversion type. Please choose from Fahrenheit, Celsius, Miles, Kilometers, Pounds, or Kilograms."
    )
