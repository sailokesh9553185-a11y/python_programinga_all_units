# Find the GCD of two numbers using recursion (Euclidean algorithm)

def gcd(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"GCD of {x} and {y} is {gcd(x, y)}")