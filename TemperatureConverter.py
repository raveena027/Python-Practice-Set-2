'''Question 9: Temperature Converter 
Write a Python program that converts temperatures between Celsius and Fahrenheit based on user input  '''


def fahrenheit_to_celsius():
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) / 1.8
        print(f"The temperature in Celsius is {celsius:.2f}°C")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def celsius_to_fahrenheit():
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"The temperature in Fahrenheit is {fahrenheit:.2f}°F")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print('''
        1. Convert to Celsius
        2. Convert to Fahrenheit''')

choice = input("Enter the choice: ")

if choice == '1':
    fahrenheit_to_celsius()
elif choice == '2':
    celsius_to_fahrenheit()
else:
    print("Invalid choice")
