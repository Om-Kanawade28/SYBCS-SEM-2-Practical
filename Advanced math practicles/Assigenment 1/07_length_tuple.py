# write a python program to find the length of tuple
tuple1 = ()
choice = 1
while choice:
    element = input("Enter the element:-")
    tuple1 +=(element,)
    choice =int(input("Do you want to continue(0,1)?"))
    

# length of tuple using function
def length_tuple(tuple1):
    length = len(tuple1)
    return length
print("Length of tuple using function:-",length_tuple(tuple1))
# Enter the element:-q
# Do you want to continue(0,1)?1
# Enter the element:-w
# Do you want to continue(0,1)?1
# Enter the element:-e
# Do you want to continue(0,1)?0
# Length of tuple using function:- 3