# Write a Python Program to Find the Sum of Natural Numbers.

# Natural numbers are a set of positive integers that are used to count and order objects.
# They are the numbers that typicaly start from 1 and continue indefinitely, including al the
# whole numbers greater than 0. In mathematical notation, the set of natural numbers is often
# denoted as "N" and can be expressed as:
# 𝑁 = 1, 2, 3, 4, 5, 6, 7, 8, . . .

def sum_of_natural_numbers():
    num = int(input("Enter a number: "))
    
    if num <= 0:
        return("Enter a positive number from 1")
    
    total = 0
    for digit in range(1, num+1):
        total += digit
    
    return total

try:
    result = sum_of_natural_numbers()
    print(result)
    
except ValueError:
    print("Enter a vaild number")