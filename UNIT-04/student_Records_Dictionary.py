students = {}

number_of_students = int(input("How many students? "))

for _ in range(number_of_students):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    students[name] = {
        "marks": marks,
        "grade": grade
    }

print("\nStudent records:")
for name, record in students.items():
    print(f"{name}: Marks = {record['marks']}, Grade = {record['grade']}")