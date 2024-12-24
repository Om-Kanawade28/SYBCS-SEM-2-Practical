# 13. Write a Python function that prints out the first n rows of Pascal's triangle.
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
def pascal_triangle(n):
    if n < 1:
        print('Invalid number of rows')
    else:
        for i in range(1, n + 1):
            num = 1
            for j in range(1, i + 1):
                print(num, end=" ")
                num = num * (i - j) // j
            print()
pascal_triangle(5)
# output
# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
