# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]    
list_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list_tuples.sort(key = lambda x: x[1])



print(f"Sorting the List of Tuples:\n{list_tuples}")
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)] 

