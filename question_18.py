# Write a Python Program to Print the Fibonacci sequence.

# Fibonacci sequence:

# The Fibonacci sequence is a series of numbers where each number is the sum of the two
# preceding ones, typicaly starting with 0 and 1. So, the sequence begins with 0 and 1, and
# the next number is obtained by adding the previous two numbers. This pattern continues
# indefinitely, generating a sequence that looks like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.

# Mathematicaly, the Fibonacci sequence can be defined using the folowing recurrence relation:

# 𝐹(0) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛 − 1) + 𝐹(𝑛 − 2)𝑓𝑜𝑟𝑛 > 1

def fibonacci_sequence(n):
    if n <= 0:
        print("Enter a positive number")
        return
    
    x, y = 0, 1
    for _ in range(n):
        print(x, end=" ")
        x, y = y, x + y  


try:
    val = int(input("Enter the number of time, the sequence should run: "))
    fibonacci_sequence(val)
    
except ValueError:
    print("Error: check your code")
    
    
    
    