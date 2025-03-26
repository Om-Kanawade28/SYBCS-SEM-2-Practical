def pascal_triangle(n):
    for i in range(n):
        row = [1]
        for j in range(i):
           row.append(row[j]*(i-j)//(j+1))
        print(" ".join(map(str,row)).center(n*3))
        
        
n = int(input("Enter the number of rows:-"))
pascal_triangle(n)