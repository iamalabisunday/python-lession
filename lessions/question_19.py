# Write a Python Program to Check Armstrong Number?
# Armstrong Number:
# It is a number that is equal to the sum of its own digits, each raised to a power equal to the
# number of digits in the number.
# For example, let's consider the number 153:
# It has three digits (1, 5, and 3).
# If we calculate + , we get , which is equal to .
# 13 +
# 53 33 1 + 125 + 27 153
# So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
# of the number of digits in the number.
# Another example is 9474:
# It has four digits (9, 4, 7, and 4).

def armstrong_number():
    num = int(input("Enter a number: "))
    num_str = str(num) #convert num to str
    len_of_num = len(num_str) # To get the lenght of the numbers
    
    total = 0
    for digit in num_str:
        total += int(digit) ** len_of_num
    
    if total == num:
        return(f"{num} is a Armstrong Number")
    else:
        return(f"{num} is not a Armstrong Number")
    
    
try:
    result = armstrong_number()
    print(result)
    
except ValueError:
    print("Error: Check your code")
    

# Lession Rules 
# 1. To loop through a numbers, it has to be frist converted to a str; 
# 2. To get the len of a numbers like (123), it has to be converted to a str; len(str(num))