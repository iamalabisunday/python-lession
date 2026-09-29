# Write a Python Program to Display the multiplication Table.
def multiplication_table():
    num = int(input("Display the multiplicastion of table of: "))
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
        
try:
    multiplication_table()
    
except ValueError:
    print("Check your code")