# Write a Python Program to Find LCM.

def lcm():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    
    if first_num <= 0 or second_num <= 0:
        return "Enter a vaild positive number"
    
    i, j = 1, 1
    
    while True:
        first_mul = first_num * i
        second_mul = second_num * j
        
        if first_mul == second_mul:
            return f"The LCM is {first_mul}"
        
        elif first_mul < second_mul:
            i += 1
        else:
            j += 1
            
            
try:
    result = lcm()
    print(result)
    
except ValueError:
    print("Error: Kindly check your code")