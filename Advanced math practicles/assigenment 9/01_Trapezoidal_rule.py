from math import *
def Tr(a,b,n,f):
    h = float(b-a)/n
    I = f(a) + f(b)
    for i in range(1,n):
        I = I + 2*f(a + i*h)
    I = (h/2)*I
    return I


def f(x):
    return sin(x)
print(Tr(0,pi,4,f))