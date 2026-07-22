# Write a Python program to convert Celsius to Fahrenheit.
def  celsius_to_Fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

while True:
    try:
        value = float(input("Enter value in celsius: "))
        result = celsius_to_Fahrenheit(value)
        print(f"{value} degrees Celsius is equal to {result} degrees Fahrenheit")
    
    except ValueError:
        print("You can only enter a number")
        continue
    
    again = input("Do you wwant to continue? (y/n): ")
    if again.lower() != "y":
        print("Good bye!")
        break