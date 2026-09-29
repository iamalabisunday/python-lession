# Write a Python Program to find largest element in an array.
def largest_array(num):
    array = []
    
    for _ in range(1, num+1):
        numbers = float(input("Enter a number: "))
        array.append(numbers)
        
    return max(array)

while True:
    try:
        num = int(input("Enter number of elements: ").strip())
            
        result = largest_array(num)
        print(f"The largest element in the array is: {result}")
            
    except ValueError:
        print("Error: Kinldy enter a vaild number")
        
    again = input("Do you want to try agai - y/n: ").lower().strip()
    if again != "y":
        break