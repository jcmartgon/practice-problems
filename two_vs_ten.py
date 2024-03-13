# Jesus Carlos Martinez Gonzalez
# 12/03/2024
# Two vs ten (https://www.codechef.com/problems/TWOVSTEN?tab=statement)

"""
Chef Two and Chef Ten are playing a game with a number X. In one turn. they can multiply X by 2. The
goal of the game is to make X divisible by 10.
Help the Chefs find the smallest number of turns necessary to win the game (it may be possible to win
in zero turns) or determine that it is impossible.
"""

for _ in range(int(input())):
    x = int(input())

    if x % 10 == 0:
        print(0)
    elif x % 5 == 0:
        print(1)
    else:
        print(-1)
