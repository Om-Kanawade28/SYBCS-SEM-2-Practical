# 16. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
def square_of_number():
    list1 = []
    for i in range(1,31):
        list1.append(i*i)
    print(list1)
square_of_number()
# output
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
