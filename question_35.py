# Write a Python Program to Split the array and add the first part to the end?
def split_array(num, split):
    if num < 1:
        return "Error: Kinldy enter a vaild number"
    if split >= num:
        return "Error: The split numbe rshuld be less than the len of array"
    
    array = []
    for _ in range(num):
        elements = input("Enter number: ")
        array.append(elements)
        
    # To split the array
    split = split % len(array)
    
    rearrange = array[split:] + array[:split]
    
    return array, rearrange

        
while True:
    try: 
        num = int(input("Enter the numbers of element in an arrow: "))
        split = int(input("Enter split position: "))
        array, rearrange = split_array(num)
        
        print("---------------Ans:------------------------")
        print(array)
        print(rearrange)
        print("-------------------------------------------")
        
    except ValueError:
        print("-------------------------------------------")
        print("Error:")
        print("-------------------------------------------")
        
    again = input("Do you want to try again - y/n: ").lower().strip()
    if again != 'y':
        break