import numpy as np
n = int(input('Enter the no of data points:-'))
x = np.zeros((n))
y = np.zeros((n))
for i in range(n):
    x[i] = float(input('x['+str(i)+']='))
    y[i] = float(input('y['+str(i)+']='))
    
xp = float(input("Enter the interpolated point:-"))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i!=j:
            p *= (xp-x[j])/(x[i] - x[j])
    yp = yp + p*y[i]

print('Interpolation value at %0.6f is %0.6f'%(xp,yp))
    
    
# Enter the no of data pointu "f:\math slips\slip 16\02_lagranges.py"   s:-4                      s:-
# x[0]=0
# y[0]=2
# x[1]=1
# y[1]=3
# x[2]=2
# y[2]=12
# x[3]=5
# y[3]=147
# Enter the interpolated point:-3.5
# Interpolation value at 3.500000 is 53.625000  