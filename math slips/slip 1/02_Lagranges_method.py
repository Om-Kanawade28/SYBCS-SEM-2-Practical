import numpy as np
n = int(input('Enter the number of data points:-'))
x = np.zeros((n))
y = np.zeros((n))
print("Enter the values of x and y:-\n")
for i in range(n):
    x[i] = float(input('X['+str(i)+']='))
    y[i] = float(input('Y['+str(i)+']='))

xp = float(input('Enter the point interpolation :-'))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i!=j:
            p *= (xp -x[j])/(x[i]-x[j])
    yp = yp + p*y[i]
print('Interploted value at %.3f is %.3f'%(xp,yp))

# Enter the number of data points:-4
# Enter the values of x and y:-

# X[0]=0
# Y[0]=5
# X[1]=1
# Y[1]=13
# X[2]=2
# Y[2]=22
# X[3]=5
# Y[3]=129 
# Enter the point interpolation :-3
# Interploted value at 3.000 is 39.400