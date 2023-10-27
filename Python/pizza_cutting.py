# Jesus Carlos Martinez Gonzalez
# 26/10/2023
# Pizza cutting (https://www.codechef.com/problems/PIZZAC)

"""
Chef has a circular pizza and a knife to cut that into pieces. He can only cut the pizza in a way such that
the knife starts from the boundary of the pizza, passes the centre, and ends at the boundary.
Find whether Chef an divide the pizza into N pieces using any (possibly zero) number of cuts.
"""

for _ in range(int(input())):
    x = int(input())
    print("YES" if x == 1 or x % 2 == 0 else "NO")
