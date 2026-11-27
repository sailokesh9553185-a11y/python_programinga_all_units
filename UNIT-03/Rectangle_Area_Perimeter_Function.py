# Function to calculate area and perimeter of a rectangle

def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter


l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

area, perimeter = rectangle_area_perimeter(l, b)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")