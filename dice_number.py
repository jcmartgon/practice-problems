# Jesus Carlos Martinez Gonzalez
# 16/03/2024
# Dice number (https://www.codechef.com/problems/DICENUM)

"""
Alice and Bob are playing a game. Each player rolls a regular six faced dice 3 times.
The score of a player is the maximum number that can be formed using the rolls.
The player with the highest score wins, and the game ends in a tie if both players have the same score.
Find the winner of the game or determine whether it is a tie.
"""

for _ in range(int(input())):
    scores = [int(x) for x in input().split()]

    alice = int("".join(map(str, sorted(scores[:3], reverse=True))))
    bob = int("".join(map(str, sorted(scores[3:], reverse=True))))

    print("Alice" if alice > bob else "Bob" if alice < bob else "Tie")
