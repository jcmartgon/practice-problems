# Jesus Carlos Martinez Gonzalez
# 01/09/2023
# Qualify the round (https://www.codechef.com/problems/QUALIFY)

"""
In a coding contest, there are two types of problems:
• Easy problems. which are worth 1 point each
• Hard problems, which are worth 2 points each
To qualify for the next round, a contestant must score at least X points. Chef solved A Easy problems
and B Hard problems. Will Chef qualify or not?
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("Qualify" if b + 2 * c >= a else "NotQualify")
