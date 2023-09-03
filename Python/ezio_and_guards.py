# Jesus Carlos Martinez Gonzalez
# 02/09/2023
# Ezio and guards (https://www.codechef.com/problems/MANIPULATE)

"""
Ezio can manipulate at most X number of guards with the apple of eden.
Given that there are Y number of guards, predict if he can safely manipulate all of them.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if a >= b else "NO")
