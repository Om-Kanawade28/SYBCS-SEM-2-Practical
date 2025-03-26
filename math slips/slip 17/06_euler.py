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
    return x**2 + y**2

x_values,y_values = euler(f,0,1,0.1,0.5)
print("x values =",x_values)
print("y values = ",y_values)



# x values = [0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5]
# y values =  [1, 1.1, 1.2220000000000002, 1.3753284000000003, 1.5734812207846565, 1.8370655360008539]