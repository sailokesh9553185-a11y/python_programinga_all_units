# Function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)
print(f"{c}°C = {f}°F")