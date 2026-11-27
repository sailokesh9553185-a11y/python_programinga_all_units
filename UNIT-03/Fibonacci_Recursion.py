# Generate Fibonacci series using recursion

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter number of terms: "))
series = [fibonacci(i) for i in range(terms)]
print("Fibonacci series:", series)
