# Your exercise — write lesson4.py:

# 1. Write a function is_even(n) that returns True/False depending on whether n is even.

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# result = is_even(53)
# print(result)

# 2. Write a function calculate_area(length, width=1) that returns the area of a rectangle, defaulting to a square-friendly width if not provided.

# def calculate_area(length, width=1):
#     area_of_rect = length * width
#     return area_of_rect

# result = calculate_area(3, 4)
# print(result)
# result2 = calculate_area(5)
# print(result2)

# 3. Write a function describe_person(name, **kwargs) that accepts any number of extra keyword details (e.g. age=30, city="Lagos") and returns a formatted string listing all of them.

# def describe_person(name, **kwargs):
#     details = ""
#     for key, value in kwargs.items():
#         details += f"{key}: {value}, "
#     return f"{name} - {details}"

# result = describe_person(name = "Sunday", age = 30, city = "Lagos")
# print(result)

# 4. Reproduce the mutable default argument bug yourself: write a broken version with cart=[], call it twice, and show me the surprising output. Then fix it using the None pattern and show the corrected output.

# def mut_def(items, cart = []):
#     cart.append(items)
#     return cart

# result = mut_def("fufu")
# result2 = mut_def("Egg")

# print(result)
# print(result2)


def mut2_def(items, cart = None):
    if cart is None:
        cart = []
    cart.append(items)
    return cart

result = mut2_def("Vegetable", "Meat")
result2 = mut2_def("Eba")
print(result)
print(result2)

# 5. Conceptual: what's the difference between a parameter having a default value vs being passed via **kwargs? When would you use one over the other?
