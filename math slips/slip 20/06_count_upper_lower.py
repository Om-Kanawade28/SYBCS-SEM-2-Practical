string = input('Enter the string:-')
def count_upp_low(s):
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.lower())
    return upper,lower
upper,lower = count_upp_low(string)
print("upper case count=",upper)
print("lowet case count =",lower)