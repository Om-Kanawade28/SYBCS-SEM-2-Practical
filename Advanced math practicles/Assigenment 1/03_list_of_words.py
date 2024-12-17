#write a python function that takes a list of words and returns the length of the longest one
list1 = []
choice = 1
while choice:
    word = input("Enter the word:-")
    list1.append(word)
    choice =int(input("Do you want to continue(0,1)?"))
def largest_word(list1):
    max_len = len(list1[0])
    count = -1
    for w in list1:
        if len(w) > max_len:
            max_len = len(w)
        count+=1
        
    return count,max_len
count,max_len = largest_word(list1)
print(list1)
print(f"the largest word is {list1[count]} and its count is {max_len} ")
# Enter the word:-om 
# Do you want to continue(0,1)?1
# Enter the word:-sai
# Do you want to continue(0,1)?1
# Enter the word:-kanawade
# Do you want to continue(0,1)?0
# ['om ', 'sai', 'kanawade']
# the largest word is kanawade and its count is 8