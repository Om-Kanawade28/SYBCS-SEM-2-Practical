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
    return (-(x*(y**2)))

x_values,y_values =euler(f,0,1,0.1,0.6)

print("x_values = ",x_values)
print("y_values = ",y_values)
        
        
# x_values =  [0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6]
# y_values =  [1, 1.0, 0.99, 0.970398, 0.94214783164788, 0.9066421301807279, 0.8655421325697955]