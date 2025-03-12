import numpy as np

n = int(input("Enter number of data points: "))

x = np.zeros(n)
y = np.zeros((n, n))

print("\nEnter data points (x, y):")
for i in range(n):
    x[i] = float(input(f"x[{i}]: "))
    y[i][0] = float(input(f"y[{i}]: "))

# Compute backward difference table
for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

print("\nBackward Difference Table:")
for i in range(n):
    print(f"{x[i]:.2f}", end="  ")
    for j in range(i + 1):
        print(f"{y[i][j]:.2f}", end="  ")
    print()

# Function to calculate u term for interpolation
def u_calculate(u, n):
    result = u
    for i in range(1, n):
        result *= (u + i)
    return result

# Factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

# Input value to interpolate
value = float(input("\nEnter the value to interpolate: "))

# Applying Newton's Backward Interpolation Formula
u = (value - x[n - 1]) / (x[1] - x[0])
interpolated_value = y[n - 1][0]

for i in range(1, n):
    interpolated_value += (u_calculate(u, i) * y[n - 1][i]) / factorial(i)

# Display interpolated result
print(f"\nValue at x = {value} is {round(interpolated_value, 6)}")
