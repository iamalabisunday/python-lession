# Write a Python program to find the area of a triangle.
def area_of_triangle(value_B, value_H):
    result = 0.5 * value_B * value_H
    return f"The Area of the Triangle is {result}"

while True:
    try:
        value_B = float(input("What is the base of the triangle: "))
        value_H = float(input("what is the height of the triangle: "))
    
    except ValueError:
        print("Kindly Enter the Correct value for the base and height of the area of the triangle")
        continue
        
    area = area_of_triangle(value_B, value_H)
    print(area)
    
    again = input("Do you want to continue? (y/n): ")
    if again.lower() != "y":
        print("Thanks for your time!")
        break