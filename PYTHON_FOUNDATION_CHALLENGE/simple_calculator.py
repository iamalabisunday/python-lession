def calculator(number, operator, inputed_number):
    if operator == "+":
        return number + inputed_number
    elif operator == "-":
        return number - inputed_number
    elif operator == "*":
        return number * inputed_number
    elif operator == "/":
        if inputed_number == 0:
            return("Error: Cannot be divided by zero")
        return number / inputed_number
    else:
        return "Invalid opertor"

sum_result = 0
prev_result = []

while True:
    user_input = input("Input: ").strip()

# ****** The undo section ******
    if user_input.lower() == "undo":
        
        if len(prev_result) < 2:
            print("There is nothing to undo")
            continue

        prev_result.pop()
        result = prev_result[-1]
        print("Result:", result)

# ****** Calculator section ******
    operator, number = user_input.split(" ")

    result = calculator(sum_result, operator, float(number))
    sum_result = result
    prev_result.append(result)

    print(sum_result)