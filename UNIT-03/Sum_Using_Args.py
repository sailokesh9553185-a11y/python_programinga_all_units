# Function using *args to find the sum of any number of values

def total_sum(*args):
    return sum(args)


print("Sum of 2 numbers:", total_sum(10, 20))
print("Sum of 4 numbers:", total_sum(5, 10, 15, 20))
print("Sum of 6 numbers:", total_sum(1, 2, 3, 4, 5, 6))