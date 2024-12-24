# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
list1 = [8,2,3,-1,7]
def multiply_element_list(list1):
    total = 1
    for x in list1:
        total *= x
    return total
print(f"Mulitply the element of list {list1} is {multiply_element_list(list1)}")

# output
# Mulitply the element of list [8, 2, 3, -1, 7] is -336