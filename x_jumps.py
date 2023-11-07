# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# X jumps (https://www.codechef.com/problems/XJUMP)

"""
Chef is currently standing at stair O and he wants to reach stair numbered X.
Chef can climb either Y steps or 1 step in one move.
Find the minimum number of moves required by him to reach exactly the stair numbered X.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    x = a // b
    print(x + a - (b * x))
