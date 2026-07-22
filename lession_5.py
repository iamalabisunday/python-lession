# 1. Write a function safe_divide(a, b) that returns a / b, but catches ZeroDivisionError and returns None with a printed message instead of crashing.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: let's your 'b' be greater than 0")
        return None

print(safe_divide(10, 2))   # should print 5.0
print(safe_divide(10, 0))   # should print the message, then None
    
# 2. Write a function parse_age(value) that tries to convert value to an int. Catch ValueError and print a friendly error message if it fails. Test it with "25" (should work) and "abc" (should fail gracefully).

def parse_age(value):
    try:
        result = int(value)
        print(result)
    except ValueError:
        print("Error: kindly try again")
        
parse_age("25")
parse_age("abc")

# 3. Create a custom exception class NegativeAmountError(Exception). Write a function deposit(amount) that raises this exception if amount < 0, otherwise returns the amount. Test both a valid and invalid call, using try/except around the invalid one so the program doesn't crash.

class NegativeAmountError(Exception):
    pass

def deposit(amount):
    if amount < 0:
        raise NegativeAmountError("Cannot deposit a negative amount")
    return amount

# Valid case
result = deposit(34)
print(result)

# Invalid case - caught, doesn't crash
try:
    deposit(-10)
except NegativeAmountError as e:
    print(f"Error: {e}")

# 4. Conceptual: why is except Exception: pass considered bad practice in real backend code? Think about what happens when something actually goes wrong in production.          # always runs, no matter what

# Ans
# because when something fails, you get: No error message, No stack trace  and No logs