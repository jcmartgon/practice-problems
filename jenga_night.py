# Jesus Carlos Martinez Gonzalez
# 02/09/2023
# Jenga night (https://www.codechef.com/problems/JENGA)

"""
Chef hosts a party for his birthday. There are N people at the party. All these N people decide to play
Jenga.
There are X Jenga tiles available. In one round, all the players pick 1 tile each and place it in the tower.
The game is validif:
• All the players have a tile in each round;
• All the tiles are used at the end.
Given N and X, find whether the game is valid.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if b % a == 0 else "NO")
