from math import *
def trepo(a,b,n,f):
    h = float(b-a)/n
    I = f(a) + f(b)
    for i in range(1,n):
        I = I + 2*f(a+i*h)
    I = (h/2)*I
    return I

def f(x):
    return cos(x)

print(trepo(0,1,5,f))

# 0.8386642098070081