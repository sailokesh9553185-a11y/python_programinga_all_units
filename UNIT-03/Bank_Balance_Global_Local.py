# Simple bank balance demonstrating global vs. local scope

balance = 1000


def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}. Updated account balance: ₹{balance}")


def try_local_deposit(amount):
    balance = 500  # Local variable shadowing global balance
    balance += amount
    print(f"Inside local-only function: local balance = ₹{balance}")


print("Starting account balance:", f"₹{balance}")
deposit(500)
try_local_deposit(300)
print("Actual account balance after local-only function:", f"₹{balance}")