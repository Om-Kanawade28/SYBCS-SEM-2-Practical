# 8. Write a Python program to extract year, month, date and time using Lambda.
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178
import datetime
now = datetime.datetime.now()
print (now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(time(now))

# Output:-
# 2024-12-24 14:49:06.950704
# 2024
# 12
# 24
# 14:49:06.950704
