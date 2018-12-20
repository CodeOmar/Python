# Omar Aguirre
# Basic Calculator
# 12-19-18

num1 = float(input("Enter First Number: "))
op = input("Enter operation: ")
num2 = float(input("Enter Second Number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Operation invalid")
