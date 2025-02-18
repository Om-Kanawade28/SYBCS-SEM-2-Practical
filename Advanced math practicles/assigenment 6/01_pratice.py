import numpy as  np
n = int(input("Enter the number of Points:-"))#enter the no of rows
x = np.zeros((n))#x column o declaration 1-D
y = np.zeros((n,n))# n x n dimention array of zeros
for i in range(n):#taking input from use r o to n value
    x[i]= float(input('x['+str(i)+']='))#value of x column
    y[i][0] =float(input('y['+str(i)+']='))#valuen of y column and other remaning column will bw zero of n
for i in range(1,n):#column of the array 
    for j in range(1,n-1):#row of the array
        y[j][i] = y[j+1][i-1] - y[j][i-1]#3rd colum form due to 2d colun of 2nd el - 1st ele
        #y[row_el][colum_no]
print("FORWARD DIFFERENCE TABLE\n")
for i in range(0,n):
    print('%0.2f'%(x[i]),end='')
    for j in range(0,n-i):
        print('\t\t%0.2f'%(y[i][j]),end='')
    print()
    