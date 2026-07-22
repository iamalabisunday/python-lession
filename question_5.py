# Write a Python program to generate a random number.
import random

while True:
    print(f"Random number: {random.randint(1, 100)}")
    
    again = input("Do you want to try again? (y/n): ")
    if again.lower() != "y":
        print("Good bye!")
        break