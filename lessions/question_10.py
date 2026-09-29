# Write a Python program to swap two variables without temp variable.
def swap_two_variable():
    a = input("Enter the first variables: ")
    b = input("Enter the second variables: ")
    a, b = b, a
    x = print(f"The First variable product the Second variable: {a}")
    y = print(f"The Second variable product the First variable: {b}")
    return x, y

while True:
    try:
        swap_two_variable()

    except ValueError:
        print("Enter a reasonable variables")
        continue
    
    again = input("Do you want to continue? (y/n): ")
    
    if again.lower() != "y":
        print("Thanks for your time!")
        break