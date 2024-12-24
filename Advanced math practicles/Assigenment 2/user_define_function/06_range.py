# Write a Python function to check whether a number falls within a given range.
def c_range(n):
    if n in range(1,10):
        print(f"{n} is between the 1 to 10 range ")
    else:
        print(f"{n} is not between the 1 to 10 range")
c_range(4)
c_range(100)
# output
# 4 is between the 1 to 10 range 
# 100 is not between the 1 to 10 range