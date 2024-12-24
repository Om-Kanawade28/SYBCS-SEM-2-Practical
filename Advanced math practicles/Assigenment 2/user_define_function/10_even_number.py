# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_number(list1):
    exp_list = []
    for i in list1:
        if i%2==0:
           exp_list.append(i)
    print(f"Sample List : {list1}")
    print(f"Expected Result : {exp_list}")
        
even_number(list1)
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
