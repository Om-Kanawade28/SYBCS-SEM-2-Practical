#write a python program to cheak wether an element exists within a tuple
tuple1 = ()
choice = 1
while choice:
    element = input("Enter the element:-")
    tuple1 +=(element,)
    choice =int(input("Do you want to continue(0,1)?"))

print(tuple1)
element = input("Enter the element to search:-")
def search_element(tuple1,element):
    if element in tuple1:
        print(f"your element {element} on {tuple1.index(element)+ 1} position")
    else:
        print(f"element {element} not found")
search_element(tuple1,element)
# Enter the element:-1
# Do you want to continue(0,1)?1
# Enter the element:-s
# Do you want to continue(0,1)?1
# Enter the element:-jjd
# Do you want to continue(0,1)?0
# ('1', 's', 'jjd')
# Enter the element to search:-jjd
# your element jjd on 3 position
