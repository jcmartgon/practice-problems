# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# Fill candies (https://www.codechef.com/problems/FILLCANDIES)

"""
Chef received N candies on his birthday. He wants to put these candies in some bags. A bag has K
pockets and each pocket can hold at most M candies. Find the minimum number of bags Chef needs
so that he can put every candy into a bag.
"""

from math import ceil

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(ceil(a / (b * c)))
