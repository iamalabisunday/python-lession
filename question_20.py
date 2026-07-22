# Write a Python Program to Find Armstrong Number in an Interval.
def find_armstrong_number():
    start_number = int(input("Enter the starting number: "))
    end_number = int(input("Enter the ending number: "))
    
    if end_number < start_number:
        print("Start from a lower number to a greater number e.g 100 - 999")
      
    for each_number in range(start_number, end_number + 1 ):
        conv_to_str = str(each_number)
        len_of_each_number = len(conv_to_str)
        
        total = 0
        for digit in conv_to_str:
            total += int(digit) ** len_of_each_number
            
        if total == each_number:
            print(f"{each_number} is a Armstrong Number")
            
try:
    find_armstrong_number()
    
except ValueError:
    print("Error: Kindly check your code")