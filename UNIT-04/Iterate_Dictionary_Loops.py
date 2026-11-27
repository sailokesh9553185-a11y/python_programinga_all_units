student = {
    "name": "Meera",
    "age": 19,
    "course": "Python"
}

print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-value pairs:")
for key, value in student.items():
    print(key, ":", value)