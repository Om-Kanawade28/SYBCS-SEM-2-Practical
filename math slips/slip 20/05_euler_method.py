import numpy as np
def euler_method(fun,x0,y0,h,x_end):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    while x < x_end:
        y = y + h*fun(x,y)
        x = x + h
        x_values.append(x)
        y_values.append(y)
    return x_values,y_values

def mu_fun(x,y):
    return x + y**2
x0 = 1
y0 = 1
h = 0.1
x_end = 1.6

x_values  , y_values = euler_method(mu_fun,x0,y0,h,x_end)

print("x values =",x_values)
print("y values =",y_values)
       
       
       
       
# x values = [1, 1.1, 1.2000000000000002, 1.3000000000000003, 1.4000000000000004, 1.5000000000000004, 1.6000000000000005]
# y values = [1, 1.2, 1.454, 1.7854116, 2.234181058141456, 2.8733375581972638, 3.848944430531965]