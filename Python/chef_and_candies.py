# Jesus Carlos Martinez Gonzalez
# 27/10/2023
# Chef and candies (https://www.codechef.com/problems/CHEFCAND)

"""
There are N children and Chef wants to give them I candy each. Chef already has X candies with him.
To buy the rest, he visits a candy shop. In the shop, packets containing exactly 4 candies are available.
Determine the minimum number of candy packets Chef must buy so that he is able to give 1 candy to
each of the N children.
"""

from math import ceil

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(ceil((a - b) / 4) if a - b > 0 else 0)
