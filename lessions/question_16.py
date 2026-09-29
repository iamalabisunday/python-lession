# Write a Python Program to Find the Factorial of a Number.
def factorial_number():
    num = int(input("Enter a number: "))
    factorial = 1
    
    for i in range(num, 0, -1):
        factorial *= i
        
    return f"The factorial of {num} is {factorial}"

try:
    result = factorial_number()
    print(result)
except ValueError:
    print("Enter a vaild number")
    
