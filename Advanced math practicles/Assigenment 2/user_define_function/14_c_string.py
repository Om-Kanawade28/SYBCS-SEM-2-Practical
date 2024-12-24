# 14. Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
def pangram(str1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str1.lower():
            return False
    return True
str1 = "The quick brown fox jumps over the lazy dog"
if(pangram(str1)):
    print(f"{str1} is pangram")
else:
    print(f"{str1} is not pangram")
#output:-
# The quick brown fox jumps over the lazy dog is pangram

        

