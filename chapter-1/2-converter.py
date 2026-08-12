convert = input("Convert to Fahrenheit, Celsius, Miles, or Kilometers? ")

print(type(convert))

if convert == "Fahrenheit":
    ori_celsius = float(input("What is the temperature in Celsius? "))
    new_fahrenheit = (ori_celsius * 1.8) + 32
    print(round(new_fahrenheit, 1), "F")
elif convert == "Celsius":
    ori_fahrenheit = float(input("What is the temperature in Fahrenheit? "))
    new_celsius = (ori_fahrenheit - 32) / 1.8
    print(int(new_celsius), "C")
elif convert == "Miles":
    ori_miles = float(input("How many miles? "))
    new_kilometers = ori_miles * 1.609
    print(round(new_kilometers, 1), "Kilometers")
elif convert == "Kilometers":
    ori_kilometers = float(input("How many kilometers? "))
    new_miles = ori_kilometers / 1.609
    print(round(new_miles, 1), "Miles")
else:
    print("Invalid conversion type. Please choose from Fahrenheit, Celsius, Miles, or Kilometers.")

