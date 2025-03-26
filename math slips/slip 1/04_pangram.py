import string

def is_pangram(s):
    alphabets = set(string.ascii_lowercase)  # Set of all lowercase letters a-z
    return set(s.lower()) >= alphabets  # Check if all letters exist in the input string

# Example Usage
sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))  # Output: True
