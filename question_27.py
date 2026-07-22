# Write a Python Program to Display Fibonacci Sequence Using Recursion.
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
 
while True:   
    try:
        nterms = int(input("Enter the number of terms (greater than 0): "))
        
        # check if the number of terms is valid
        if nterms <= 0:
            print("Plese enter a positive integer")
    
        for i in range(nterms):
            print(recur_fibo(i))
        
    except ValueError:
        print("Error: Kindly enter a postive value number")
        
    again = input("Do you want to try again - y/n: ").lower()
    if again != "y":
        break
