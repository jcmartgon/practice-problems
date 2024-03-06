# Jesus Carlos Martinez Gonzalez
# 04/03/2024
# Akash and missing class (https://www.codechef.com/problems/CHFCLASS)

"""
Akash loves going to school, but not on weekends.
A week consists of 7 days (Monday to Sunday). Akash takes a leave every Saturday.
If a month consists of N days and the first-day of the month is Monday. find the number of days
Akash would take a leave in the whole month.
"""

for _ in range(int(input())):
    days = int(input())

    weeks = days // 7

    print(weeks + 1 if days - weeks * 7 == 6 else weeks)
