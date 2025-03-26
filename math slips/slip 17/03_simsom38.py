def simp38(a,b,n,f):
    h = float(b - a)/n
    I = f(a) + f(b)
    for i in range(1,n):
        k= a + i*h
        if i%3==0:
            I = I + 2*f(k)
        else:
            I= I + 3*f(k)
    I = (3*h/8)*I
    return I

def f(x):
    return 2**2 + 5*x

print(simp38(1,10,9,f))

# 283.5