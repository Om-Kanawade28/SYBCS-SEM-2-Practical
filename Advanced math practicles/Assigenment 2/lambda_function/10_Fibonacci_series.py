# 10. Write a Python program to create Fibonacci series up to n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
from functools import reduce
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1]) if n > 1 else [0] if n ==1 else []
print(f"Fibonacci series upto 2:\n{fib_series(2)}")
print(f"Fibonacci series upto 5:\n{fib_series(5)}")
print(f"Fibonacci series upto 6:\n{fib_series(6)}")
print(f"Fibonacci series upto 9:\n{fib_series(9)}")

# output:-
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]