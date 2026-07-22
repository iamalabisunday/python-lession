# Write a Python Program to Check if a Number is Positive, Negative or Zero.
def check_if_a_number_is_positive_negative_zero():
    num = float(input("Enter a number: "))
    
    if num > 0:
        print(f"{num} is a Positive Number")
    elif num == 0:
        print(f"{num} is a Zero")
    else:
        print(f"{num} is a Negative Number")
        
    return num

try:
    check_if_a_number_is_positive_negative_zero()

except ValueError:
    print("Enter a number only")