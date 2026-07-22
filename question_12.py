# Write a Python Program to Check if a Number is Odd or Even.
def check_for_odd_even_number():
    num = int(input("Enter a number: "))
    if num % 2 == 0: 
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")
    return num

try:
    check_for_odd_even_number()
except ValueError:
    print("Enter a vaild number")