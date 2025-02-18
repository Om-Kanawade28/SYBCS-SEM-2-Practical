import numpy as np
n = int(input('Enter the number data points:-'))
x = np.zeros((n))
y = np.zeros((n))
print("Enter the value of x and y:-")
for i in range(n):
    x = float(input('x['+str(i)+']='))
    y = float(input('y['+str(i)+']='))
xp = float(input('Enter the interpolotion point:-'))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i!=j:
            p = p*(xp - x[j])/(x[j] -x[j])
            yp = yp + p*y[i]
            
print("interploated value at %.3f is %.3f"%(xp,yp))
