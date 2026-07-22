# Write a Python program to display calendar.
import calendar

def calender_function():
    year = int(input("Enter year: "))
    month = int(input("Enter Month: "))
    day = int(input("Enter day: "))
    return calendar.month(year, month, day)

while True:
    try:
        result = calender_function()
        print(result)
    
    except ValueError:
        print("Enter only an Integal value")
        continue
    
    again = input("Do you want to continue? (y/n): ")
    
    if again.lower() != "y":
        print("Good bye!")
        break