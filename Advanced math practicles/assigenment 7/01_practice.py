import numpy as np
n = int(input('Enter number of data points:-'))
x = np.zeros((n))
y = np.zeros((n,n))
print('Enter the x and y values:-')
for i in range(n):
    x[i] = float(input('x['+str(i)+']='))
    y[i][j] = float(input('y['+str(i)+']='))
for i in range(1,n):
    for j in range(n-1,i-2,-1):
        y[j][i] = y[j][i-1]-y[j-1][i-1]
print("BACKWARD DIFFERENCE TABLE\n")
for i in range(0,n):
    print('%0.2f'%(x[i]),end='')
    for i in range(0,i+1):
        print('\t%02f'%(y[i][j]))
    print()