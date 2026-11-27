# Function taking marks of three subjects and returning total and average

def calculate_total_average(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average


s1 = float(input("Enter marks for Subject 1: "))
s2 = float(input("Enter marks for Subject 2: "))
s3 = float(input("Enter marks for Subject 3: "))

total, average = calculate_total_average(s1, s2, s3)
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")