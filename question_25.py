# Write a Python Program To Find ASCII value of a character.
def find_ASCII_value():
    chr = str(input("Enter a single character: ")).strip()
    
    if len(chr) != 1:
        return "Error: Kindly enter exactly one character "
    
    result = ord(chr)
    return f"The ASCII value of {chr} is {result}"

# -------------------------------
result = find_ASCII_value()
print(result)
# -------------------------------