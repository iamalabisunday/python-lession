# Write a Python Program to find sum of array.
def sum_array(num):
    array = []
    for _ in range(1, num+1):
        num = float(input("Enter number: "))
        array.append(num)   
    return sum(array)    

while True:
    try:
        num = int(input("Enter number of elements: "))
        
        if num < 1:
            print("Kinldy enter a positive number")
        else:
            result = sum_array(num)
            print(f"Sum of the array is {result}")
        
    except ValueError:
        print("Error: enter a vaild positive number")
        
    again = input("Do you want to try again - y/n: ").lower()
    if again != "y":
        break