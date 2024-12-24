#Write a Python function to find the maximum of three numbers.
def max_of_three1(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
def max_of_two(y,z):
    if y > z:
        return y
    else:
        return z
def max_of_three2(x,y,z):
    return max_of_two(x,max_of_two(y,z))
print(max_of_three1(1,2,3))
print(max_of_three2(4,5,6))

# output
# 3
# 6