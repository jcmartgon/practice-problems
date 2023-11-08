# Jesus Carlos Martinez Gonzalez
# 08/09/2023
# Chef eren (https://www.codechef.com/problems/CHEFEREN)

"""
Chef is a very big fan of Eren Yeager.
In the last season of Attack on Titan, there were N episodes numbered from I to N.
Each even indexed episode was A minutes long and each odd indexed episode was B minutes long.
Calculate the total duration (in minutes) of the last season.
"""

from math import ceil

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    q, r = divmod(a, 2)
    print(q * b + (q + ceil(r)) * c)
