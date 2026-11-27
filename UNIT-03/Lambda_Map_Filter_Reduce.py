# Demonstrate lambda functions with map(), filter(), and reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
print("Original list:", numbers)

# map() - square each number
squares = list(map(lambda x: x ** 2, numbers))
print("Squares using map():", squares)

# filter() - keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", evens)

# reduce() - compute sum of all elements
total = reduce(lambda acc, x: acc + x, numbers)
print("Sum using reduce():", total)