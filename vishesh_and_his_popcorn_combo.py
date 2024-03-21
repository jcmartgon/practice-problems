# Jesus Carlos Martinez Gonzalez
# 20/03/2024
# Game between friends (https://www.codechef.com/problems/FRGAME)

"""
Vishesh has gone to watch the new Spider-Man movie. but he is having troubles choosing which
Popcorn-and-Coke combo to buy.
There are three combos A, B, and C available at the counter. You are given the time (in minute) for
which each Popcorn bucket and Coke cup lasts. Given that Vishesh's satisfaction from a combo is
defined as the total lasting time (in minute) of the Popcorn bucket and the Coke cup, find the maximum
satisfaction he can get by buying a single combo.
"""

for _ in range(int(input())):
    best = 0

    for _ in range(3):
        combo = sum([int(x) for x in input().split()])
        if combo > best:
            best = combo

    print(best)
