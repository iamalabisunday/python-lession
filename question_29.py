# Write a Python Program to calculate your Body Mass Index.

def cal_body_mass(weight, height ):
    result = weight / (height**2)
    return result

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

print("----------------------------")

bmi = cal_body_mass(weight, height)
print(f"Your BMI is {bmi}")

print("----------------------------")

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")
