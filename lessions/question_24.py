# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.
def convert_decimal():
    try:
        dec_num = int(input("Enter the decimal number: "))
        
    except ValueError:
        return("Invalid input: Please enter a valid integer.")
    
    if dec_num <= 0:
        return "Enter a positive number greater than one"
        
    convert = input("Enter the Decimal to (bin | oct | hex): ").lower()

    if convert == "bin":
        return f"The decimal value of {dec_num} is {bin(dec_num)} in binary"
    elif convert == "oct":
        return f"The decimal value of {dec_num} is {oct(dec_num)} in binary"
    elif convert == "hex":
        return f"The decimal value of {dec_num} is {hex(dec_num)} in binary"
    else:
        return "Invalid conversion method. Choose 'bin', 'oct', or 'hex'."
    
    
# ------------------------------------
result = convert_decimal()
print(result)
# ------------------------------------

    