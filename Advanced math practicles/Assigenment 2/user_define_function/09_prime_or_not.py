# 9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def prime_number(n):
    if n > 1:
        for i in range(2,int(n**0.5) + 1):
            if n%i == 0:
                print(f"{n} is not prime number")
                break
            else:
                print(f"{n} is prime number")
                break
    else:
        print(f"{n} is not prime number")
        
prime_number(11)
prime_number(99)
prime_number(14)
# output:-
# 11 is prime number
# 99 is prime number
# 14 is not prime number