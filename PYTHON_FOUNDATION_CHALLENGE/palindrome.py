while True:
    user_input = input("Input: ").lower()

    clean_input_list = []
    for char in user_input:
        if char.isalnum():
        # if "a" <= char <= "z":
            clean_input_list.append(char)

    clean_input = "".join(clean_input_list)

    print(clean_input)

    left = 0
    right = len(clean_input)

    again = input("Do you want to try again - (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break