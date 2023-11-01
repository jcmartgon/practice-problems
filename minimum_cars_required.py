# Jesus Carlos Martinez Gonzalez
# 01/09/2023
# Minimum cars required (https://www.codechef.com/problems/MINCARS)

"""
A single car can accommodate at most 4 people.
N friends want to go to a restaurant for a party. Find the minimum number of cars required to
accommodate all the friends.
"""

from math import ceil

for _ in range(int(input())):
    print(ceil(int(input()) / 4))
