#Write a Python program to multiplies all the items in a list.
list1 = []
choice = 1
while choice:
    element = input("Enter the element:-")
    list1.append(int(element))
    choice =int(input("Do you want to continue(0,1)?"))
#mautipliction by using user define function
def multiply_list(list1):
    multiply = 1
    for i in list1:
        multiply *= i
    return multiply
print("Multiply of list using user define function:-",multiply_list(list1))
#using predefine function
import math
print("Multiply of list using math.prod():-",math.prod(list1))

# Enter the element:-3
# Do you want to continue(0,1)?1
# Enter the element:-4
# Do you want to continue(0,1)?1
# Enter the element:-4
# Do you want to continue(0,1)?0
# Multiply of list using user define function:- 48
# Multiply of list using math.prod():- 48