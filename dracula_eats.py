# Jesus Carlos Martinez Gonzalez
# 15/11/2023
# Dracula eats (https://www.codechef.com/problems/CHEAT)

"""
Eat, drink, and be scary
There are N spooky days left until Halloween.
Dracula dines at a mysterious restaurant that changes its spooky menu daily. He particularly enjoys
what they serve on Tuesday.
Today is Monday, so he wishes to calculate how many times he can indulge in his favourite menu in the
next N days (including today) before Halloween.
Note that Dracula follows the standard 7-day calendar, with Tuesday immediately following Monday.
"""


for _ in range(int(input())):
    q, r = divmod(int(input()), 7)
    print(q + 1 if int(r) >= 2 else q)
