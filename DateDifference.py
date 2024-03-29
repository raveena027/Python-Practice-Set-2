'''Question 5: Date Difference
 Write a Python function that calculates the difference in days between two given dates  '''

from datetime import date

def get_difference(date1, date2):
    delta = date2 - date1
    return delta.days

d1 = date(2020, 10, 20)
d2 = date(2022, 2, 20)
days = get_difference(d1, d2)
print(f'Difference is {days} days')
