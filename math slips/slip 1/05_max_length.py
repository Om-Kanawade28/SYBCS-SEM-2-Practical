# ) Write a Python function that takes a list of words and returns the length of the longest
#  one.
def longest_word(words):
    if not words:
        return 0
    else:
        return max(len(word) for word in words)
    
words = ['om','kanawade','sybcs']
print(longest_word(words))