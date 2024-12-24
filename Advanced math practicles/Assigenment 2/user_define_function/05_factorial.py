# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("enter the number:-"))
print(f"factorial of {n} is {factorial(n)}")
# enter the number:-5
# factorial of 5 is 120