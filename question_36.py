# Write a Python Program to check if given array is Monotonic.
def check_if_array_monotonic(num):
    if num < 1:
        return "Error: enter a vaild positive number"
    
    arrays = []
    for _ in range(num):
        array = int(input("Enter number: ")) 
        arrays.append(array)
        
    increasing = decreasing = True
    
    for i in range(1, len(arrays)):
        if arrays[i] > arrays[i-1]:
            decreasing = False
        elif  arrays[i] < arrays[i-1]:
            increasing = False
        
    return arrays, (increasing or decreasing)

while True:
    try: 
        num = int(input("Enter number of element in an array: "))
        arrays, result = check_if_array_monotonic(num)
        print("---------------Ans:------------------------")
        print(f"{arrays} is monotonic: {result}")
        print("-------------------------------------------")

    except ValueError:
        print("-------------------------------------------")
        print("Error")
        print("-------------------------------------------")
        
    again = input("Do you want to try again - y/n: ").lower()
    if again != "y":
        break