# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# Mater chef finals (https://www.codechef.com/problems/TOP10)

"""
Chef has been working hard to compete in MasterChef.
He is ranked X out of all contestants. However, only 10 contestants would be selected for the finals. Check whether Chef made it to the top 10 or not?
"""

t = int(input())
for _ in range(t):
    print("YES" if int(input()) <= 10 else "NO")
