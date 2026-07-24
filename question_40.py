# Write a Python Program to Sort Words in Alphabetic Order.
def sort_word(word_list):
    result = word_list
    return result

while True:
    try:
        statment = input("Enter a statment: ").split()
        result = sort_word(statment)

        print("--------------------------------------")
        print(f"Here are the result: {result}")
        print("--------------------------------------")

    except ValueError:
        print("Error")

    again = input("Do you want to try again - y/n: ")
    if again != "y":
        break