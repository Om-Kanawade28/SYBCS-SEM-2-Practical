def tripo(a,b,n,f):
    h = float(b-a)/n
    I = f(a) + f(b)
    for i in range(1,n):
        I = I + 2*f(a+i*h)
    I = (h/2)*I
    return I

def f(x):
    return 2*x**2 - 4*x -1

print(tripo(2,4,5,f))
# 11.440000000000001