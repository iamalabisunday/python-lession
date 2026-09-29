import math

def quadratic_equation():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    d = (b ** 2) - (4 * a * c)

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")

    elif d == 0:
        root = -b / (2 * a)
        print(f"Root: {root}")

    else:
        root = -b / (2 * a)
        imaginary_part = math.sqrt(abs(d)) / (2 * a)
        print(f"Root 1: {root} + {imaginary_part}i")
        print(f"Root 2: {root} - {imaginary_part}i")


while True:
    try:
        quadratic_equation()
    except ValueError:
        print("Please enter valid numbers only.")
        continue
    
    again = input("Do you want to continue? (y/n): ")
    
    if again.lower() != "y":
        print("Good bye")
        break