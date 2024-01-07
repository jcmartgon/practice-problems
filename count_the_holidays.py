# Jesus Carlos Martinez Gonzalez
# 06/01/2024
# Count the holidays (https://www.codechef.com/problems/SUNDAY)

"""
A particular month has 30 days. numbered from 1 to 30.
Day 1 is a Monday, and the usual 7-day week is followed (so day 2 is Tuesday, day 3 is Wednesday, and
so on).
Every Saturday and Sunday is a holiday. There are N festival days. which are also holidays. Note that it
is possible for a festival day to occur on a Saturday or Sunday.
You are given the dates of the festivals. Determine the total number of holidays in this month.
"""

for _ in range(int(input())):
    festivals = int(input())
    fest_dates = [int(x) for x in input().split()]

    holidays = 8

    for date in fest_dates:
        if date % 7 not in [0, 6]:
            holidays += 1

    print(holidays)
