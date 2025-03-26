import numpy as np
n = int(input('Enter number of data point:-'))
x = np.zeros((n))
y = np.zeros((n))
print('Enter data for x and y:-')
for i in range(n):
    x[i] = float(input('x['+str(i)+']='))
    y[i] = float(input('y['+str(i)+']='))
xp = float(input('Ente the interpolation point:-'))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
            if i != j:
                p *= (xp - x[j])/(x[i] - x[j])
    yp = yp + p*y[i]
print('Interpolted value at %.3f is %.3f'%(xp,yp))
        


# Enter data for x and y:-
# x[0]=150
# y[0]=12.247
# x[1]=152
# y[1]=12.329
# x[2]=154
# y[2]=12.410
# x[3]=155
# y[3]=12.490
# Ente the interpolation point:-153
# Interpolted value at 153.000 is 12.362 
        
        
        
        
        
        
        
        
        
        
        
        
        