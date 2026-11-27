# Function divide(a, b) called with keyword and positional arguments

def divide(a, b):
    return a / b


res_keyword = divide(b=10, a=20)
res_positional = divide(10, 20)

print("divide(b=10, a=20) result:", res_keyword)
print("divide(10, 20) result:", res_positional)