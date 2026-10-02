students = [{"name": "Sam", "scores": [80, 90]}, {"name": "David", "scores": [55, 60]}]

highest_student = None
highest_avg = None

lowest_student = None
lowest_avg = None

for student in students:
    name = student["name"]
    scores = student["scores"]

    total = 0
    for score in scores:
        total += score

    total_number_scores = len(scores)
    average = total / total_number_scores

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"

    print(f"{name} - Average: {average} - Grade: {grade}")

    # Tracking highest performing student
    if highest_avg is None or average > highest_avg:
        highest_avg = average
        highest_student = name

    # Tracking lowest performing student
    if lowest_avg is None or average < lowest_avg:
        lowest_avg = average
        lowest_student = name

print("=" * 50)
print("--- Overall Summary ---")
print(f"Highest Performed Student: {highest_student} - with an average of {highest_avg}")
print(f"Lowest Performed Student: {lowest_student} - with an average of {lowest_avg}")