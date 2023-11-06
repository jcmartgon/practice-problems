# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Chess ratings (https://www.codechef.com/problems/C_RATING)

"""
Alice has recently started playing Chess. Her current rating is X. She noticed that when she wins a
game, her rating increases by 8 points.
Can you help Alice in finding out the minimum number of games she needs to win in order to make
her rating greater than or equal to Y?
"""

from math import ceil

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(ceil((b - a) / 8))
