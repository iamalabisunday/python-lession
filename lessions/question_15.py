# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.

def prime_number():
    num = []
    for i in range(1, 11):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                num.append(i)
    return num

try:
    result = prime_number()
    print(f"Answer: {result}")
    
except ValueError:
    print("Error - Check code")