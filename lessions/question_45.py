# Write a Python program to check if the given number is Happy Number.
def is_happy_number(number, seen=None):
    if seen is None:
        seen = set()
        
    print(seen)
    
    if number == 1:
        return True
    
    if number in seen:
        return False
    
    seen.add(number)
    
    num_str = str(number)
    sum_total = 0
    
    for chr in num_str:
        chr_int = int(chr)
        sum_total += chr_int ** 2
   
    return is_happy_number(sum_total, seen)


while True:
    try:
        number = int(input("Enter a number: "))
        result = is_happy_number(number)
            
        print("-Ans:-----------------------------")
        if result is True:
            print(f"{number} is a Happy Number")
        else:
            print(f"{number} is not a Happy Number")
        print("-----------------------------------")
        
    except ValueError:
        print("Error")

    again = input("Do you want to try again - y/n: ").lower().strip()
    if again != "y":
        break