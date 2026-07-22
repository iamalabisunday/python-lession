# Write a Python Program to Find Factorial of Number Using Recursion.

def recur_factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Sorry, factorial does not exist for negative numbers"
    else:
        return n * recur_factorial(n-1)
    
while True:        
    num = int(input("Enter a number: ").strip())
    result = recur_factorial(num)
    print(f"The factorial of {num} is {result}")
    
    again = input("Do you want to try again - y/n: ").lower().strip()
    if again != 'y':
        break