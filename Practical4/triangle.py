# This script calculates and displays the first ten triangular numbers.

# Function to calculate the nth triangular number
def triangular_number(n):
    return n * (n + 1) // 2  # Using the formula: T_n = n * (n + 1) / 2

# Display the first ten triangular numbers
print("First 10 Triangular Numbers:")
for i in range(1, 11):
    print(f"T_{i} = {triangular_number(i)}")
