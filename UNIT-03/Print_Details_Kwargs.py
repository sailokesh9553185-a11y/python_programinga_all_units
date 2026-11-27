# Function print_details(**kwargs) to print each key and value

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Krishna", age=26, city="Guntur")