# 1. Write a list of 5 favorite foods to a file called foods.txt, one per line.

with open("foods.txt", "w") as f:
    f.write("Rice\n")
    f.write("Beans\n")
    f.write("Eggs\n")
    f.write("Fufu\n")
    f.write("Eba\n")

# 2. Read foods.txt back and print each line without the trailing newline character.

# Reading line by line
# with open("foods.txt", "r") as f:
#     for line in f:
#         print(line.strip()) # .strip() removes the trailing newline

# 3. Append one more food to foods.txt (don't overwrite the existing ones), then read and print the full updated file.

# Read list before adding to it
with open("foods.txt", "r") as f:
    content = f.read()
    print(content)
    
# Add to the list using append - "a"
with open("foods.txt", "a") as f:
    f.write("Vegetable\n")
    f.write("Banana\n")
    
# Read list after adding to it
with open("foods.txt", "r") as f:
    content = f.read()
    print(content)

# 4. Try to open a file that doesn't exist (ghost.txt) inside a try/except, and print a friendly message instead of crashing.

try:
    with open("ghost.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: 404 not found")
    
    
# 5. Create a dict representing a small "user profile" (name, email, age), write it to profile.json using json.dump(), then read it back using json.load() and print the loaded dict.

import json

data = {"name": "Sunday","email": "iamalabisunday@gmail.com", "age": 30}

# Write JSON to a file
with open("profile.json", "w") as f:
    json.dump(data, f)

# Read JSON from a file
with open("profile.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)