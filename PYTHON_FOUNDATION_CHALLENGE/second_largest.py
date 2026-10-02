user_input = input("input: ").strip().split(",")

user_input = []
for number in user_input:
    cleaned_string = number.strip()
    number = int(cleaned_string)
    user_input.append(number)

first_largest = user_input[0]
second_largest = 0

for index in range(0, len(user_input)):
    if user_input[index] > first_largest:
        first_largest = user_input[index]
    elif user_input[index] > second_largest and user_input[index] != first_largest:
        second_largest = user_input[index]

print("First Largest:", first_largest)
print("Second Largest:", second_largest)
