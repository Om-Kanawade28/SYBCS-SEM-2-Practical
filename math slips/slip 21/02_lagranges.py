import numpy as np
n = int(input('Enter the data points:-'))
x = np.zeros((n))
y = np.zeros((n))
for i in range(n):
    x[i] = float(input('x['+str(i)+']='))
    y[i] = float(input('y['+str(i)+']='))
xp = float(input('Enter the interploated point:-'))
yp = 0
for i in range(n):
    p=1
    for j in range(n):
        if i != j:
            p *= (xp - x[j])/(x[i] - x[j])
    yp = yp + p*y[i]
print('Interpolation value at %0.6f at %0.6f'%(xp,yp))




# Enter the data points:-3
# x[0]=2
# y[0]=0.593
# x[1]=2.5
# y[1]=0.816
# x[2]=3
# y[2]=1.078
# Enter the interploated point:-2.2
# Interpolation value 
# at 2.200000 at 0.677520
    