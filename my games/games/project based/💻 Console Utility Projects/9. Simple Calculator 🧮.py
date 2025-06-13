"""
Perform addition, subtraction, multiplication, division.

Loop to allow multiple calculations.
"""
class Calculator:
    def add(x):
        return x + int(input("Enter second number: "))
    
    def sub(x):
        return x - int(input("Enter second number: "))
    
    def mul(x):
        return x * int(input("Enter second number: "))
    
    def division(x):
        return x / int(input("Enter second number: "))

# Infinite loop
while True:
    print("\nSelect operation: +  -  *  /  or q to quit")
    op = input("Enter operation: ")
    
    if op == "q":
        break
    
    x = int(input("Enter the first number : "))

    if op == "+" :
        print(Calculator.add(x))
    elif op == "-" :
        print(Calculator.sub(x))
    elif op == "*" :
        print(Calculator.mul(x))
    elif op == "/" :
        print(Calculator.division(x))
    else :
        print("Invalid opration.")