def newton_raphson(f,g,x0,e,N):
    x0 = float(x0)
    e = float(e)
    N = int(N)
    step = 1
    flag = 1
    condition = True 
    
    while condition:
        if g(x0) == 0.0:
            print("Zero divided error ")