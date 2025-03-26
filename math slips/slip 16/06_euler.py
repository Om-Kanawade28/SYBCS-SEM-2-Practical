def euler(f,x0,y0,h,x_end):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    while x < x_end:
        y = y + h*f(x,y)
        x = x + h
        x_values.append(x)
        y_values.append(y)
        
    return x_values,y_values


def f(x,y):
    return y**2 + 1

x_values,y_values = euler(f,0,0,0.05,0.05)
print("x values=",x_values)
print("y values=",y_values)


# x values= [0, 0.05]
# y values= [0, 0.05]