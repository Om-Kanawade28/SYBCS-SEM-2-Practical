#write a python program to add 'ing' at the end of given string
def add_ing(string):
    if len(string) > 3 and string[-3:] =='ing':
        string += 'ly'
    else:
        string += 'ing'
    return string
string = input("Enter the string:-")
print(f"your word={string}\nAfter add ing:-{add_ing(string)}")
# your word=play
# After add ing:-playing