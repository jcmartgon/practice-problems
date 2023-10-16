# Jesus Carlos Martinez Gonzalez
# 15/10/2023
# Chef in his office (https://www.codechef.com/problems/OFFICE)

"""
Recently Chef joined a new company. In this company, the employees have to work for X hours each
day from Monday to Thursday. Also, in this company, Friday is called Chill Day — employees only have
to work for Y hours (Y < X) on Friday. Saturdays and Sundays are holidays.
Determine the total number of working hours in one week.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a * 4 + b)
