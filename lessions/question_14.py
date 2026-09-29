# Write a Python Program to Check Prime Number.
# Prime Numbers:
# A prime number is a whole number that cannot be evenly divided by any other number
# except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
# cannot be divided by any other positive integer except for 1 and their own value.
def prime_number():
    num = int(input("Enter a number: "))
    if num > 1:
        
        for i in range(2, num):
            if num % i == 0:
                return f"{num} is a not Prime Number"
        else:
            return f"{num} is a Prime Number"
        
    return f"{num} is not a Prime Number"
                
try:
    result = prime_number()
    print(result)

except ValueError:
    print("Enter a vaild number")