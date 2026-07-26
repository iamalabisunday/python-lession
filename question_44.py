# Write a Python program to print all disarium numbers between 1 to 100.
def disarim_number(num):
    num_str = str(num)
    total_sum = 0
    for index, char in enumerate(num_str, start=1):
        char_int = int(char)
        total_sum += char_int ** index
            
    if total_sum == num:
       return total_sum


while True:
    try:
        print('Enter disarim number between')
        number_start = int(input("from: "))
        number_end = int(input("end: "))
        
        print("\n--------------------------------------")
        for index in range(number_start, number_end):
            result = disarim_number(index)
            if result != None:
               print(result, end=" | ") 
        print("\n--------------------------------------")
        
    except ValueError:
        print("Error:")
        
    again = input("Do you want to try again - y/n: ").lower()
    if again != "y":
        break