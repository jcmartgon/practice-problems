# Jesus Carlos Martinez Gonzalez
# 09/10/2023
# Cricket match (https://www.codechef.com/problems/CRICMATCH)

"""
There is a cricket match in Chefland. Chef's team requires N runs to win in M overs.
Given that 1 over consists of 6 balls and a player can score a maximum of 6 runs in a ball, find whether
Chef's team can win.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if b * 36 >= a else "NO")
