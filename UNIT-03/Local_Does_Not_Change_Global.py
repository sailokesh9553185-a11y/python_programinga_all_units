# Show that a local variable does not change a global variable with the same name

message = "Global Message"


def show_local():
    message = "Local Message"
    print("Inside function (local):", message)


print("Before function call (global):", message)
show_local()
print("After function call (global):", message)