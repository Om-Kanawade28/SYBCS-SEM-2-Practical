tuple1 = ()
choice = 1
while choice:
    element = input("Enter the element:-")
    tuple1 +=(element,)
    choice =int(input("Do you want to continue(0,1)?"))

#reverse tuphle function
def reverse_tuple(tuple1):
    tuple1 = tuple1[::-1]
    return tuple1
print("Your Tuple:-",tuple1)
print("Reverse Tuple user define:-",reverse_tuple(tuple1))
# their is predeifine function to reverse the tuple
print("Reverse Tuple using reversed():-",tuple(reversed(tuple1)))
# Enter the element:-q
# Do you want to continue(0,1)?1
# Enter the element:-w
# Do you want to continue(0,1)?1
# Enter the element:-e
# Do you want to continue(0,1)?0
# Your Tuple:- ('q', 'w', 'e')
# Reverse Tuple user define:- ('e', 'w', 'q')
# Reverse Tuple using reversed():- ('e', 'w', 'q')        
