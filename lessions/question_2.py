# Write a Python program to do arithmetical operations addition and division.

# First method
# def addition_division(num1, num2, operation):    
#     if operation == "+":
#         result = num1 + num2
#         return f"{num1} {operation} {num2} = {result}"
#     elif operation == "/":
#         result = num1 / num2
#         return f"{num1} {operation} {num2} = {result}"
#     else:
#         return "Invalid operation"
    
# while True:
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#     except ValueError:
#         print('You can only enter numbers')
#         continue

#     operation = input("Enter the operation (+ or /): ")
    
#     key = addition_division(num1, num2, operation)
#     print(key)
    
#     again = input("Do you want to continue? (y/n): ")
#     if again.lower() != "y":
#         print("Good bye!")
#         break

# Second Method
class ArithmeticalOperations:
    def __init__(self, num1: float, num2: float, operation: str):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def add(self):
        return self.num1 + self.num2

    def division(self):
        if self.num2 == 0:
            return "Error: Divition by zero"
        return self.num1 / self.num2

    def __str__(self):
        if self.operation == "+":
            return f"Result: {self.add()}"
        elif self.operation == "-":
            return f"Result: {self.division()}"
        else:
            return "Error: invalid operation"
        
def promptNumber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def stop_continue():
    while True:
        again = input("Do you want to try again (yes or no): ").strip().lower()
        if again in ("y", "yes"):
            return True
        else:
            return False
        
def main():
    num1 = promptNumber("Enter the first number: ")
    num2 = promptNumber("Enter the second number: ")
    operation = input("Enter the operation (additon or division): ")

    result = ArithmeticalOperations(num1, num2, operation)

    print("-----------------------------------")
    print(result)
    print("-----------------------------------")

if __name__ == "__main__":
    while True:
        main()
        if not stop_continue():
            print("Goodbye!")
            break