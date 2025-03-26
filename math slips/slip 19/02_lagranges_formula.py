import numpy as np
n = int(input('Enter the data  points:-'))
x = np.zeros((n))
y = np.zeros((n))
print("Enter the data of x and y:-")
for i in range(n):
    x[i] = float(input('x['+str(i)+']='))
    y[i] = float(input('y['+str(i)+']='))
xp = float(input('Enter the interpolated point:-'))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i!=j:
            p *= (xp -x[j])/(x[i] - x[j])
    yp = yp + p*y[i]
    
print('Interpolation at point %0.6f is %0.6f'%(xp,yp))



# Enter the data  points:-4
# Enter the data of x and y:-
# x[0]=1
# y[0]=1
# x[1]=2
# y[1]=8
# x[2]=3
# y[2]=27
# x[3]=4
# y[3]=64
# Enter the interpolated point:-2.5
# Interpolation at point 2.500000 is 15.625000