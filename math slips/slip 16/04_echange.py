def swap_first_last(s):
    if len(s) < 2:
        return s  # If string has 0 or 1 character, return it as is
    return s[-1] + s[1:-1] + s[0]

# Example usage
string = input("Enter a string: ")
new_string = swap_first_last(string)
print("Modified string:", new_string)
