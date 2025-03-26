def s13(a,b,n,f):
    h = float(b - a)/n
    I = f(a) + f(b)
    for i in range(1,n):
        k = a + i*h
        if i%2==0:
            I = I + 2*f(k)
        else:
            I = I + 4*f(k)
    I = (h/3)*I
    return I


def f(x):
    return 1/(1+x**2)
print(s13(0,1,4,f))

# "
# 0.7853921568627451