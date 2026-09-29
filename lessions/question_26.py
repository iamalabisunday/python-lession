# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.

def calc():
    try:
        num_first = float(input("Enter a vaild first number: "))
        num_second = float(input("Enter a vaild second number: "))
    except ValueError:
        return "Error: enter a vaild number"
    
    try:
        operation = str(input("Enter the operation (add | subtract | multiply | divide): ")).lower()
    except ValueError:
        return "Enter a vaild operation"

    if operation == "add" or operation == "+":
        result = num_first + num_second
        return f"The result of {num_first} + {num_second} = {result}"
    elif operation == "subtract" or operation == "-":
        result = num_first - num_second
        return f"The result of {num_first} - {num_second} = {result}"
    elif operation == "multiply" or operation == "*":
        result = num_first * num_second
        return f"The result of {num_first} * {num_second} = {result}"
    elif operation == "divide" or operation == "/":
        result = num_first / num_second
        return f"The result of {num_first} / {num_second} = {result}"
    else:
        return "Error: Invaild input"

while True:
    result = calc()
    print(result)
    print("------------------------------------------------")
    again = (input("Do you want to try again: enter y/n: ")).lower()
    if again != "y":
        break