#15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
def sort_words(items):
    words = [word for word in items.split('-')]
    words.sort()
    print('-'.join(words))
items = input("Sample Items :")
sort_words(items)


# Sample Items :green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
