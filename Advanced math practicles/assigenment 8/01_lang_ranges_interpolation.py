import numpy as np
n = int(input('Enter number of data point:'))
x = np.zeros((n))
y = np.zeros((n))
print('Enter data for x any:-')
for i in range(n):
    x[i] = float(input('x['+str(i)+']='))
    y[i]  = float(input('y['+str(i)+']='))
xp = float(input('Enter interpolation point:-'))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i!=j:
            p = p*(xp-x[j])/(x[i]-x[j])
            yp = yp + p*y[i]
print('Interpolated value at %.3f is %.3f'%(xp,yp))

# Enter number of data point:4 
# Enter data for x any:-
# x[0]=0
# y[0]=5
# x[1]=1
# y[1]=13
# x[2]=2
# y[2]=22
# x[3]=5
# y[3]=29
# Enter interpolation point:-2.5
# Interpolated value at 2.500 is 
# 125.375