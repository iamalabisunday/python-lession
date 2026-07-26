# Write a Python Program to Remove Punctuation From a String.
def remove_punctuation(text):
    words = ""
    for char in text:
        if ("a" <= char <= "z")  or ("A" <= char <= "Z") or char == " ":
            words += char
    return words

while True:
    try:
       text = input("Enter a statment: ")
       result = remove_punctuation(text) 
       
       print("---Ans-------------")
       print(result) 
       print("-------------------")
       
    except ValueError:
        print("Error")
        
    again = input("Do you want to try again - y/n:" ).lower().strip()
    if again != "y":
        break
    
# Enter a string: Hello!!!, he said ---and went
# Hello he said and went