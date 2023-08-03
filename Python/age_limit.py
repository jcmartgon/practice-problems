# Jesus Carlos Martinez Gonzalez
# 02/08/2023
# Age limit (https://www.codechef.com/problems/AGELIMIT)

"""
Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

Minimum age limit is X (i.e. Age should be greater than or equal to X). Age should be strictly less than Y. Chef's current Age is A. Find whether he is currently eligible to take the exam or not.
"""

n = int(input())
for _ in range(n):
    x, y, a = map(int, input().split())
    print("YES" if x <= a < y else "NO")
