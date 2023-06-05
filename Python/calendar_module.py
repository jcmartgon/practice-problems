# Jesus Carlos Martinez Gonzalez
# 04/06/2023
# Calendar Module (https://www.hackerrank.com/challenges/calendar-module/problem)

"""
You are given a date. Your task is to find what the day is on that date.
"""

import calendar


if __name__ == "__main__":
    month, day, year = map(int, input().split())
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())
