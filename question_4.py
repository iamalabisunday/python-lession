# Write a Python program to swap two variables.
while True:
    try:
        a = str(input("Enter the first value for a: "))
        b = str(input("Enter the second value for b: "))
        print(f"First value is {a} while Second value is {b}")

    # To swap value
        c = a
        a = b
        b = c
        print(f"First value is {a} while Second value is {b}")

    except ValueError:
        print("Enter string vaule only")
        continue
    
    again = input("Do you want to try again? (y/n): ")
    
    if again.lower() != "y":
        print("Thanks for your time!")
        break