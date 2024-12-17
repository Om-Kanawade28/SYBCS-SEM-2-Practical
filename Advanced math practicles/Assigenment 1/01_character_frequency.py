#write a python program to count the number of charters(character frequency) in a string
def char_freq(name):
    freq = {}
    for n in name:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return freq

name = input("Enter the String:-")
print(char_freq(name))


    