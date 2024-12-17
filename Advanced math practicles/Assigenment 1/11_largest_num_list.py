#Write a Python program to get the largest number from a list.
list1 = []
choice = 1
while choice:
    element = input("Enter the element:-")
    list1.append(int(element))
    choice =int(input("Do you want to continue(0,1)?"))
#using max() function
print("Largest number in list using max():-",max(list1))
#using loop
def largest_num(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max
print("Largest number in list using loop:-",largest_num(list1))
#using sort() method
list1.sort()
print("Largest number in list using sort():-",list1[-1])

# Enter the element:-1
# Do you want to continue(0,1)?1
# Enter the element:-5
# Do you want to continue(0,1)?1
# Enter the element:-93
# Do you want to continue(0,1)?0
# Largest number in list using max():- 93
# Largest number in list using loop:- 93
# Largest number in list using sort():- 93
