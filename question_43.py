# Write a Python program to check if the given number is a Disarium Number.
def disarium_number(number):
    number_str = str(number)
    sum_total = 0

    for index, char in enumerate(number_str, start = 1):
        digit = int(char)
        sum_total += digit ** index
        
    if sum_total == int(number_str):
        return f"{sum_total} is a Disarium number."
    else:
        return f"{sum_total} is not a Disarium number."


while True:
    try:
        number = int(input("Enter a number: "))
        result = disarium_number(number)
        
        print("--Ans--------------------------")
        print(result)
        print("-------------------------------")
        
    except ValueError:
        print("Error: you are only allow to enter number")
    
    again = input("Do you want to try again - y/n:" ).lower()
    if again != "y":
        break