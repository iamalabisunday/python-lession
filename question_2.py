# Write a Python program to do arithmetical operations addition and division.
def addition_division(num1, num2, operation):    
    if operation == "+":
        result = num1 + num2
        return f"{num1} {operation} {num2} = {result}"
    elif operation == "/":
        result = num1 / num2
        return f"{num1} {operation} {num2} = {result}"
    else:
        return "Invalid operation"
    
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print('You can only enter numbers')
        continue

    operation = input("Enter the operation (+ or /): ")
    
    key = addition_division(num1, num2, operation)
    print(key)
    
    again = input("Do you want to continue? (y/n): ")
    if again.lower() != "y":
        print("Good bye!")
        break