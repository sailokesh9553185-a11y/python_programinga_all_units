# Function using **kwargs to display student's name and subject marks

def display_student_details(name, **marks):
    print(f"Student Name: {name}")
    print("Subject Marks:")
    for subject, score in marks.items():
        print(f"  {subject}: {score}")


display_student_details("Ananya", Math=92, Physics=88, Chemistry=85)