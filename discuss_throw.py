# Jesus Carlos Martinez Gonzalez
# 02/09/2023
# Discus (https://www.codechef.com/problems/DISCUS)

"""
In discus throw, a player is given 3 throws and the throw with the longest distance is regarded as their
final score.
You are given the distances for all 3 throws of a player. Determine the final score of the player.
"""

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    print(max(lst))
