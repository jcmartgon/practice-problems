# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Alice and marks (https://www.codechef.com/problems/MARKSTW)

"""
Alice has scored X marks in her test and Bob has scored Y marks in the same test. Alice is happy if
she scored at least twice the marks of Bob's score. Determine whether she is happy or not.
"""

x, y = map(int, input().split())
print("YES" if x >= y * 2 else "NO")
