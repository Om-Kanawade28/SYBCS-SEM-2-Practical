# 11. Write a Python function to check whether a number is "Perfect" or not.
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    if sum == n:
        print(f"{n} is perfect number")
    else:
        print(f"{n} is not perfect number")
perfect_number(6)
perfect_number(28)
perfect_number(99)
# output:-
# 6 is perfect number
# 28 is perfect number
# 99 is not perfect number

