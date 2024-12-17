#write a python program that change a given string to a new string where the first and last chars have been exchanged
string = input("Enter the String:-")
def exchange(string):
    new_string = string[-1] + string[1:-1] + string[0]
    print("New String:-",new_string)
exchange(string)
# Enter the String:-kanawade
# New String:- eanawadk