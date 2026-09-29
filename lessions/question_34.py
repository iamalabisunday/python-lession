# Write a Python Program for array rotation.

def largest_array(num, rot):
    original_array = []
    
    for _ in range(num):
        numbers = float(input("Enter a number: "))
        original_array.append(numbers)
    
    rot = rot % len(original_array)
    
    rotated = original_array[rot:] + original_array[:rot]
        
    return original_array, rotated

while True:
    try:
        num = int(input("Enter number of elements: "))
        rot = int(input("Number of positions to rotate: "))
        
        if num < 1 or rot < 1:
            print("-------------------------------------------")
            print("Error: Kinldy enter a vaild positive number")
            print("-------------------------------------------")
        else:
            original_array, rotated = largest_array(num, rot)
            print(f"Original Array: {original_array}")
            print(f"Rotated Array: {rotated}")
            
    except ValueError:
        print("-------------------------------------------")
        print("Error: Kinldy enter a vaild number")
        print("-------------------------------------------")
        
    again = input("Do you want to try agai - y/n: ").lower().strip()
    if again != "y":
        break