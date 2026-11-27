# Use a global counter and increment it inside a function using 'global'

counter = 0


def increment_counter():
    global counter
    counter += 1
    print("Counter inside function:", counter)


print("Initial counter:", counter)
increment_counter()
increment_counter()
increment_counter()
print("Final counter after 3 calls:", counter)