def miles_to_kilometers(miles):
    return miles * 1.609

def kilometers_to_miles(kilometers):
    return kilometers / 1.609

def convert_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

print ("Welcome to the Unit Converter! ")
convert_choice = input("Convert to Fahrenheit, Celsius, Miles, Kilometers, Pounds, or Kilograms? ").strip().lower()
number = float(input("Enter the number to convert: "))

actions = {
    "fahrenheit": convert_to_fahrenheit,
    "celsius": convert_to_celsius,
    "miles": miles_to_kilometers,
    "kilometers": kilometers_to_miles,
    "pounds": pounds_to_kilograms,
    "kilograms": kilograms_to_pounds,
}           

result = actions[convert_choice](number)
print(f"The converted value is: {result}")  