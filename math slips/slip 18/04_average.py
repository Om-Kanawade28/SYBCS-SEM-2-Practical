def average_50to100():
    sum = 0
    for i in range(50,101):
        sum = sum + i
    avg = sum/51
    print("averge 50 to 100 :_",avg)
    
def average_50to100f():
    first = 50
    last = 100
    n = 51
    s = (n/2)*(first+last)
    avg = s/n
    print("averge 50 to 100 :_",avg)
    
average_50to100()
average_50to100f()