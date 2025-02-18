def falsepostion(f,x0,x1,e):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)
    if f(x0)*f(x1) > 0.0:
        print("Try th dffeerent value")
        return
    print("interation start:-")
    step = 1
    condition = True
    while condition:
        x2 = x0 - (x1 - x0)*f(x0)