# Function shopping_cart(**products) to display item prices in ₹ and total

def shopping_cart(**products):
    total = 0
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total += price
    print(f"Total: ₹{total}")


shopping_cart(apple=15, orange=12, mango=10)