# Super Simple Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sign = input("Enter +, -, *, or /: ")

if sign == "+":
    print(num1 + num2)
if sign == "-":
    print(num1 - num2)
if sign == "*":
    print(num1 * num2)
if sign == "/":
    print(num1 / num2)
