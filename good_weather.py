# Jesus Carlos Martinez Gonzalez
# 26/11/2023
# Good weather (https://www.codechef.com/problems/GOODWEAT)

"""
The weather report of Chefland is Good if the number of sunny days in a week is strictly greater than
the number of rainy days.
Given 7 integers A1, .42, .43, .44, .45, .46, .47 where Ai = I denotes that the i day of week in
Chefland is a sunny day, Ai = O denotes that thet day in Chefland is a rainy day. Determine if the
weather report of Chefland is Good or not.
"""


for _ in range(int(input())):
    week = [int(x) for x in input().split()]

    print("YES" if sum(week) > 3 else "NO")
