import numpy as np
def euler_method(func,x0,y0,h,e_end):
    x_values = [x0]
    y_values = [y0]
    x= x0
    y = y0
    while x < x_end:
        y = y + h*func(x,y)
        x = x + h
        x_values.append(x)
        y_values.append(y)
    return x_values,y_values
def my_func(x,y):
    return 1 + y**2

x0 = 0
y0 = 0
h = 0.1
x_end = 0.5

x_values,y_values = euler_method(my_func,x0,y0,h,x_end)
print("x values:-",x_values)
print("y values:-",y_values)



# PS F:\math slips> python -u "f:\math slips\slip 21\05_euler.py"       
# x values:- [0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5]
# y values:- [0, 0.1, 0.201, 0.30504010000000004, 0.41434504626080104, 0.5315132279968876]