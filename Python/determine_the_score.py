# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# Determine the score (https://www.codechef.com/problems/DETSCORE)

"""
Chef appeared for a placement test.
There is a problem worth X points. Chef finds out that the problem has exactly 10 test cases. It is
known that each test case is worth the same number of points.
Chef passes N test cases among them. Determine the score Chef will get.
NOTE: See sample explanation for more clarity.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y * (x // 10))
