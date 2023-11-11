# Jesus Carlos Martinez Gonzalez
# 10/11/2023
# A or b (https://www.codechef.com/problems/AORB)

"""
There are two problems in a contest.
• Problem A is worth 500 points at the start of the contest.
• Problem B is worth 1000 points at the start of the contest.
Once the contest starts, after each minute:
• Maximum points of Problem A reduce by 2 points .
• Maximum points of Problem B reduce by 4 points.
It is known that Chef requires X minutes to solve Problem A correctly and Y minutes to solve Problem
B correctly.
Find the maximum number of points Chef can score if he optimally decides the order of attempting
both the problems.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(
        max(
            ((500 - 2 * x) + (1000 - 4 * (x + y))),
            ((1000 - 4 * y) + (500 - 2 * (x + y))),
        )
    )
