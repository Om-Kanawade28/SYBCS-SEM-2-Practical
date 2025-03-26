def newton_raphson(f,g,x0,e,N):
    x0 = float(x0)
    e = float(e)
    N = int(N)
    flag = 1
    condition = True
    step = 1
    while condition:
        if g(x0) == 0.0:
            print("zero divide error")
            break
        x1 = x0 - (f(x0)/g(x0))
        print(f"Iteration {step},x1 = {x1:.6f},f(x1) = {f(x1):.6f}")
        x0 = x1
        step += 1
        if step  > N:
            flag = 0
            break
        condition = abs(f(x1)) > e
    if flag == 1:
        print("\nreuired root =",x1)
    else:
        print("\nRoot did not converge in given iterations")
        
def f(x):
    return x**5 - 3*x + 1

def g(x):
    return 5*x**4 -3

newton_raphson(f,g,-0.5,0.00001,10)




# Iteration 1,x1 = 0.418605,f(x1) = -0.242960
# Iteration 2,x1 = 0.333250,f(x1) = 0.004361
# Iteration 3,x1 = 0.334734,f(x1) = 0.000001

# reuired root = 0.33473386316280773