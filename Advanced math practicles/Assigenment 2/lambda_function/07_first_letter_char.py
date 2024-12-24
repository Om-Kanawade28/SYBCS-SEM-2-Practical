# 7. Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output:
# True
# False
starts_with = lambda x, y: x.startswith(y)
string1 = "Hello World"
string2 = "Python"
char1 = "H"
char2 = "P"
print(starts_with(string1, char1))
print(starts_with(string2, char1))


#output:-
# True
# False