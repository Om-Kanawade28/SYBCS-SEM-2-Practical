def falsi(f,x0,x1,e):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)
    if f(x0)*f(x1) > 0.0:
        print("take different values")
        return
    condition = True
    step = 1
    while condition:
        x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
        print(f"Interation {step},x2 = {x2:.6f},f(x2) = {f(x2):.6f}")
        if f(x0)*f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step += 1
        condition = abs(f(x2)) > e
    print("\nreuired root",x2)
def f(x):
    return x**5 + 3*x + 1

falsi(f,-2,0,0.0001)