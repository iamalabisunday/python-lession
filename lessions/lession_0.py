# 1. Create a class Student:

# Requirements:

# Attributes: name, score
# Method: get_grade()
# 70+ → "A"
# 50–69 → "B"
# below 50 → "C"

# class Student:
#     def __init__(self, name, score):
        
#         if not (0 <= score <= 100):
#             raise ValueError("Score must be between 0 and 100")
        
#         self.name = name
#         self.score = score
        
#     def get_grade(self):
#         if self.score >= 70:
#             return "A"
#         elif self.score >= 50:
#             return "B"
#         else:
#             return "C"
    
#     def __str__(self):
#         return f"{self.name} scored {self.score} and got grade {self.get_grade()}"
        
# s1 = Student("Sunday", 75)
# print(s1)
# s2 = Student("John", 55)
# print(s2)
# s3 = Student("Jane", 40)
# print(s3)

# ------------------------------------------------------------------------

# 2. Create a class Rectangle:

# Requirements:

# width, height
# Method area()
# Method perimeter()

# class Rectangle:
#     def __init__(self, width, height):
#         if width < 0 or height < 0:
#             raise ValueError("Error: Kindly input a vaild postive number")
        
#         self.width = width
#         self.height = height
        
#     def area(self):
#         return self.width * self.height
        
#     def perimeter(self):
#         return 2 * (self.width + self.height)
    
#     def __str__(self):
#         return f"Area: {self.area()}, Perimeter: {self.perimeter()}"

# try:
#     result = Rectangle(2, 4)
#     print(result)
    
#     result1 = Rectangle(-1, 5) 
#     print(result1)
    
# except ValueError as e:
#     print(e)

# ------------------------------------------------------------------------

# Exercise 3: Counter (Understanding State)

# Create a class Counter:

# Requirements:

# Starts at 0
# Method increment()
# Method reset()

# 👉 This teaches state change inside objects

# class Counter:
#     def __init__(self, start = 0):
#         if start < 0:
#             raise ValueError("Error: Enter a vaild number")
        
#         self.count = start
        
#     def increment(self):
#         self.count += 1
#         return self.count
    
#     def reset(self):
#         self.count += 0
#         return self.count
    
#     def __str__(self):
#         return f"Current count: {self.count}"
    

# try: 
#     counter = Counter(2)

#     print(counter)   # 2
    
#     counter.increment()
#     counter.increment()
    
#     print(counter)   # 4
    
#     counter.reset()
#     print(counter)   # 0

# except ValueError as e:
#     print(e)