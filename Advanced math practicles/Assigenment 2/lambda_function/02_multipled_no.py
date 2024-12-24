# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
def fun_lambada(n):
     return lambda x:x*n
double = fun_lambada(2)
triple = fun_lambada(3)
quadruple = fun_lambada(4)
quadtuple = fun_lambada(5)
print(f"Double the number of 15 = {double(15)}")
print(f"Triple the number of 15 ={triple(15)}")
print(f"Quadruple the number of 15 = {quadruple(15)}")
print(f"Quintuple the number 15 = {quadtuple(15)}")
 
# Output:-
# Double the number of 15 = 30
# Triple the number of 15 =45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75