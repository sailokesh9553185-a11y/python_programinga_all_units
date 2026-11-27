# Function to calculate simple interest with default rate = 5

def simple_interest(principal, time, rate=5):
    return (principal * time * rate) / 100


si_default = simple_interest(1000, 2)
print("Simple Interest (default rate 5%):", si_default)

si_custom = simple_interest(1000, 2, 7.5)
print("Simple Interest (custom rate 7.5%):", si_custom)