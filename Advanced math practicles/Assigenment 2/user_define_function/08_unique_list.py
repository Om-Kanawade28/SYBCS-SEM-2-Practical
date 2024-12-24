# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(Sample_List):
    unique_list1 = []
    for el in Sample_List:
        if el not in unique_list1:
            unique_list1.append(el)
    print(f"Sample List : {Sample_List}")
    print(f"Unique List : {unique_list1}")
Sample_List = [1,2,3,3,3,3,4,5]
unique_list(Sample_List)
#output
# Sample List : [1, 2, 3, 3, 3, 3, 4, 5]
# Unique List : [1, 2, 3, 4, 5]