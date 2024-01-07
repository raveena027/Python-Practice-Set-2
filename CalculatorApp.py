'''Question 1: Calculator App 
Create a Python program that acts as a simple calculator. 
It should take two numbers and an operator as input and perform the corresponding operation.'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y

    else:
        return "Undefined"

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
operation = input("Enter the operation you want to perform (+, -, *, /): ")

if operation == '+':
    result = add(a, b)
elif operator == '-':
    result = subtract(a, b)
elif operator == '*':
    result = multiply(a, b)
elif operator == '/':
    result = divide(a, b)
else:
    result = "Invalid Input"

print(f"Result: {result}")
