students = [
    {"name": "Ravi", "marks": 78},
    {"name": "Anu", "marks": 92},
    {"name": "Meera", "marks": 85}
]

sorted_students = sorted(students, key=lambda student: student["marks"])

print("Students sorted by marks:")
for student in sorted_students:
    print(student)