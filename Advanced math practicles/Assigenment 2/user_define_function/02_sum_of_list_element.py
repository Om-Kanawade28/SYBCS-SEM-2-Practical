#2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
list1 = [8,2,3,0,7]
def sum_of_element_of_list(list1):
    sum_list = 0
    for i in list1:
        sum_list = i + sum_list
    print(f"sum of list {list1} is {sum_list}")
    
sum_of_element_of_list(list1)
     
# output
# sum of list [8, 2, 3, 0, 7] is 20