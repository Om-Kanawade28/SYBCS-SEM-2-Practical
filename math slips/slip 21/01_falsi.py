def fassi(f,x0,x1,e):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)
    if f(x0)*f(x1) > 0.0:
        print("take the different values")
        return
    condition = True
    step = 1
    while condition:
        x2 = x0 - (x1 - x0)*f(x0)/(f(x1) - f(x0))
        print(f"Iteration {step},x1 = {x1:.6f},f(x2)={f(x1):.6f}")
        if f(x0)*f(x2):
            x1 = x2
        else:
            x0 = x2
        step += 1
        condition = abs(f(x2)) > e
    print("\nrequired root =",x2)
def f(x):
    return x**3 - 4*x -9

fassi(f,2,3,0.00001)