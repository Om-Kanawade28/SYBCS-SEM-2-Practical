def raphson(f,g,x0,e,N):
    x0 = float(x0)
    e = float(e)
    N = int(N)
    flag = 1
    step = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print("Divide zero error")
            break
        x1 = x0 - (f(x0)/g(x0))
        print(f"Iteration {step} , x1 = {x1:.6f}, f(x1) = {f(x1):.6f}")
        x0 = x1
        step += 1
        if step > N:
            flag = 0
            break
        condition = abs(f(x1)) > e
    if(flag == 1):
        print("\nRequired root =",x1)
    else:
        print("\nNot convergent")
        
def f(x):
    return x**2 - 50

def g(x):
    return 2*x

raphson(f,g,7.5,0.00001,10)


# Iteration 1 , x1 = 7.083333, f(x1) = 0.173611
# Iteration 2 , x1 = 7.071078, f(x1) = 0.000150
# Iteration 3 , x1 = 7.071068, f(x1) = 0.000000

# Required root = 7.07106781187345