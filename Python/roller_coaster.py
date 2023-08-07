# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Roller coaster (https://www.codechef.com/problems/MINHEIGHT)

"""
Chefs son wants to go on a roller coaster ride. The height of Chefs son is X inches while the minimum
height required to go on the ride is H inches. Determine whether he can go on the ride or not.
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print("YES" if x >= y else "NO")
