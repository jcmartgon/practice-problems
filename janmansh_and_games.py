# Jesus Carlos Martinez Gonzalez
# 15/11/2023
# Janmansh and games (https://www.codechef.com/problems/JGAMES)

"""
Janmansh and Jay are playing a game. They start with a number X and they play a total of Y moves.
Janmansh plays the first move of the game, after which both the players make moves alternatingly.
In one move, a player can increment or decrement X by 1.
Ifthe final number after performing Y moves is even, then Janmansh wins otherwise, Jay wins.
Determine the winner of the game if both the players play optimally.
"""


for _ in range(int(input())):
    x, y = map(int, input().split())
    print("Janmansh" if (x + y) % 2 == 0 else "Jay")
