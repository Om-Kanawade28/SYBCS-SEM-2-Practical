def falsi(f,x0,x1,e):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)
    if f(x0)*f(x1) > 0.0:
        print("take the different values")
        return
    step = 1
    condition = True
    while condition:
        x2 = x0 -(x1 -x0)*f(x0)/(f(x1) -f(x0))
        print(f"Iteration {step},x2 = {x2:.6f},f(x2) = {f(x2):.6f}")
        if f(x0)*f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step += 1
        condition = abs(f(x2)) > e
    print("\nrequired root is =",x2)
    
def f(x):
    return x**3 - 2*x -5
falsi(f,2,3,0.00001)
        
        
# Iteration 1,x2 = 2.058824,f(x2) = -0.390800
# Iteration 2,x2 = 2.081264,f(x2) = -0.147204
# Iteration 3,x2 = 2.089639,f(x2) = -0.054677
# Iteration 4,x2 = 2.092740,f(x2) = -0.020203
# Iteration 5,x2 = 2.093884,f(x2) = -0.007451
# Iteration 6,x2 = 2.094305,f(x2) = -0.002746
# Iteration 7,x2 = 2.094461,f(x2) = -0.001012
# Iteration 8,x2 = 2.094518,f(x2) = -0.000373
# Iteration 9,x2 = 2.094539,f(x2) = -0.000137
# Iteration 10,x2 = 2.094547,f(x2) = -0.000051
# Iteration 11,x2 = 2.094550,f(x2) = -0.000019
# Iteration 12,x2 = 2.094551,f(x2) = -0.000007

# required root is = 2.0945508667513875
    
    