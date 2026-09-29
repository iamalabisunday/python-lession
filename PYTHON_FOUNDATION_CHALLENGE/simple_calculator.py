def operator():
    return input("Enter an operator: ").strip()


def num(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Invalid: Kindly enter a valid number only")
        return num("Try again: ")


start_addition = 0
start_mult = 5
start_div = 1
num_lists = []

current_operator = operator()

if current_operator == "+":
    first_num = num("Enter a number: ")
    
    result = start_addition + first_num
    num_lists.append(result)
    print(result)

elif current_operator == "-":
    first_num = num("Enter a number: ")
    
    result = first_num - start_addition
    num_lists.append(result)
    print(result)

elif current_operator == "*":
    first_num = num("Enter a number: ")

    result = start_mult * first_num
    num_lists.append(result)
    print(result)

elif current_operator == "/":
    first_num = num("Enter a number: ")

    result = first_num / start_div
    num_lists.append(result)
    print(result)


else:
    print("Invalid operator.")
    exit()


while True:
    continue_calculation = input("Do you want to continue - (y/n): ").strip().lower()

    if continue_calculation == "y":
        current_operator = operator()
        num_another = num("Enter another number: ")

        previous_result = num_lists.pop()

        if current_operator == "+":
            result = previous_result + num_another

        elif current_operator == "-":
            result = previous_result - num_another

        elif current_operator == "*":
            result = previous_result * num_another

        elif current_operator == "/":
            if previous_result == 0 or num_another == 0:
                print("Invaild: Divide by zero")
                break
            elif previous_result > num_another:
                result = previous_result / num_another
            elif num_another > previous_result:
                result = f"-{num_another / previous_result}"

        else:
            print("Invalid operator.")
            num_lists.append(previous_result)
            continue

        num_lists.append(result)
        print(result)

    elif continue_calculation == "n":
        print(f"Final Answer: {num_lists.pop()}")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter y or n.")
