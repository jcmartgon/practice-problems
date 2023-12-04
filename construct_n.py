# Jesus Carlos Martinez Gonzalez
# 04/12/2023
# Construct n (https://www.codechef.com/problems/CONN)

"""
You are given an integer N. Find if it is possible to represent N as the sum of several(possibly zero) 2's
and several(possibly zero) 7's.
Formally. find if there exist two integers X, Y (X, Y 0) such that 2 • X + 7 • Y = N.
"""

for _ in range(int(input())):
    n = int(input())

    print("YES" if (n % 7) % 2 == 0 or n > 7 else "NO")
