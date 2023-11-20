# Jesus Carlos Martinez Gonzalez
# 19/11/2023
# Rcb and playoffs (https://www.codechef.com/problems/RCBPLAY)

"""
Alice and Bob are playing a game. Each player rolls a regular six faced dice 3 times.
The score of a player is the sum of the values of the highest 2 rolls. The player with the highest score
wins, and the game ends in a Tie if both players have the same score.
Find the winner of the game or determine whether it is a tie.
"""


for _ in range(int(input())):
    scores = [int(x) for x in input().split()]

    a = sum(scores[:3]) - min(scores[:3])
    b = sum(scores[3:]) - min(scores[3:])

    print("Alice" if a > b else "Bob" if a < b else "Tie")
