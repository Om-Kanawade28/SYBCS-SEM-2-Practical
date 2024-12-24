# Write a Python program to reverse a string.

# Sample String: "1234abcd"
# Expected Output: "dcba4321"

str1 = "1234abcd"
def reverse_string(str1):
    str2 = ""
    index = len(str1)
    while index > 0:
        str2 = str2 + str1[index - 1]
        index = index - 1
    return str2
print(f"reverse string = {reverse_string(str1)}")
# output

# reverse string = dcba4321