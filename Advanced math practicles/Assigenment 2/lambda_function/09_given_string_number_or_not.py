# 9. Write a Python program to check whether a given string is a number or not using Lambda.
# Sample Output:
# True
# True
# False
# True
# False
# True
# Print checking numbers:
# True
# True
is_number = lambda x: x.replace('.','',1).isdigit()
print(is_number("123"))
print(is_number("123.45"))
print(is_number("abc"))
print(is_number("123.456"))
print(is_number("123a"))
print(is_number("-123"))
print("Print checking numbers:")
print(is_number("123"))
print(is_number("123.45"))

# Output:-
# True
# True
# False
# True
# False
# False
# Print checking numbers:
# True
# True