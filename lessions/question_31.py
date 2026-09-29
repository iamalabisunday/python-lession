# Write a Python Program for cube sum of first n natural numbers?
def cube_sum(num):
    if num <= 0:
        return "Enter a vaild postive number"
    
    count = []
    for i in range(1, num+1):
        count.append(i ** num)
        
    return sum(count)


while True: 
    
    try:
        num = int(input("Enter a vaild positive number: "))
        result = cube_sum(num)
        print(f"The cube sum of the first {num} natural numbers is: {result}")
        
    except ValueError:
        print("Error")
        
    again = input("Do you want to try again - y/n: ").lower()
    if again != "y":
        break