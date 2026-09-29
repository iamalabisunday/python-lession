# Write a Python Program to Find HCF.

def hcf():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    
    if first_num <= 0 or second_num <= 0:
        return "Enter a vaild positive number"

    first_factor = []
    for i in range(1, first_num + 1):
        if first_num % i == 0:
            first_factor.append(i)
    
    second_factor = []
    for i in range(1, second_num + 1):
        if second_num % i == 0:
            second_factor.append(i)
            
    commond_factor = []
    for factor_first in first_factor:
        if factor_first in second_factor:
            commond_factor.append(factor_first)
    
    if commond_factor:
        return f"The HCF is {max(commond_factor)}"
    else:
        return "No commond factor found"
    
try:
    result = hcf()
    print(result)
    
except ValueError:
    print("Error: Check your code")