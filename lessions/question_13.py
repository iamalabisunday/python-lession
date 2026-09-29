# Write a Python Program to Check Leap Year.
def check_leap_year():
    year = int(input("Enter a year to check if it a Leap Year: "))
    if (year % 100) != 0 or (year % 4 == 0 and year % 400 == 0):
        return (f"{year} is a Leap Year")
    else:
        return (f"{year} is not a Leap Year")
    
try:
    result = check_leap_year()
    print(result)
    
except ValueError:
    print("Enter a vaild year")