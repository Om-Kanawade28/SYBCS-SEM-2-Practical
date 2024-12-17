#write  a python program to sum all the items in list
list1 = []
choice = 1
while choice:
    element = input("Enter the element:-")
    list1.append(int(element))
    choice =int(input("Do you want to continue(0,1)?"))

def sum_list(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum
print("Sum of list using user define function:-",sum_list(list1))
#usijng predefine sum function
print("Sum of list using sum():-",sum(list1))
#using lambda function
sum_list = lambda list1: sum(list1)
print("Sum of list using lambda function:-",sum_list(list1))


# Enter the element:-1
# Do you want to continue(0,1)?1
# Enter the element:-5
# Do you want to continue(0,1)?1
# Enter the element:-93
# Do you want to continue(0,1)?0
# Sum of list using user define function:- 99
# Sum of list using sum():- 99
# Sum of list using lambda function:- 99