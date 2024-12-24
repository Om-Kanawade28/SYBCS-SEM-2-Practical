# Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def upper_lower(str1):
    lower = 0
    upper = 0
    for i in str1:
        if i.isupper():
            upper += 1
        elif i.lower():
            lower += 1
    print(f"# No. of Upper case characters : {upper}")
    print(f"# No. of Lower case Characters : {lower}")

str1 = 'The quick Brow Fox'
upper_lower(str1)

# output
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
