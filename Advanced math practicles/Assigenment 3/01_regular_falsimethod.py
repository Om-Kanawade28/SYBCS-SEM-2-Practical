def falseposition(f,x0,x1,e):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)
    if f(x0)*f(x1) > 0.0:
        print("This given values do not backet a root . try with difernt values")
        return
    print("False position method starts\n")
    step = 1
    condition = True 
    while condition:
        x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
        print(f"iteration {step},x2 = {x2:.6f},f(x2) = {f(x2):.6f}")
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step += 1
        condition = abs(f(x2)) > e
    print(f"\nrequired root is:{x2:.8f}")
def f(x):
    return x**3 - 3*x + 1


falseposition(f,0,1,0.000001)
    