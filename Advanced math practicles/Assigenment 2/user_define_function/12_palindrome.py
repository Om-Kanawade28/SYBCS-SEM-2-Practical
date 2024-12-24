# 2. Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(str1):
    str2 = ""
    index = len(str1)
    while index > 0:
        str2 = str2 + str1[index - 1]
        index = index - 1
    if str1 == str2:
        print(f"{str1} is palindrome")
    else:
        print(f"{str1} is not palindrome")
palindrome("madam")
palindrome("121")
palindrome("hello")
# output:-
# madam is palindrome
# 121 is palindrome
# hello is not palindrome
