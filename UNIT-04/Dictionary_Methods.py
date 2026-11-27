student = {
    "name": "Ravi",
    "age": 20,
    "course": "Python"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name using get():", student.get("name"))

student.update({"age": 21})
print("After update():", student)

removed_course = student.pop("course")
print("Removed value:", removed_course)
print("After pop():", student)