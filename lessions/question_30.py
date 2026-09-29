# Write a Python Program to calculate the natural logarithm of any number.
import math

def natural_log(num):
    if num <= 0:
        return "Please enter a positive number."
    else:
        result = math.log(num)
        return f"The natural logarithm of {num} is: {result}"
   
    
num = float(input("Enter a number: "))
result =  natural_log(num)
print(result)