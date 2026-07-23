# Write a Python Program to Sort Words in Alphabetic Order.
def sort_word(word_list):

    n = len(word_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare words in lowercase to ignore capital letters
            if word_list[j].lower() > word_list[j + 1].lower():
                # Swap the elements
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]
                
    return word_list



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