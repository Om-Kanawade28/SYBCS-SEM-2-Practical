#write a python program to get  a string made of the first 2 and the last 2 chars from a give string
def first_two_last(string):
    new_string = string[:2] + string[-2:]
    print("New string:-",new_string)
string = input("Enter the String:-")
first_two_last(string)
# Enter the String:-omkanawade
# New string:- omde