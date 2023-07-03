# Jesus Carlos Martinez Gonzalez
# 02/07/2023
# The Minion Game (https://www.hackerrank.com/challenges/the-minion-game/problem)

"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
"""


def minion_game(string):
    vowels = "AEIOU"
    stuart_score = kevin_score = 0

    for i, char in enumerate(string):
        points = len(string) - i
        if char in vowels:
            kevin_score += points
        else:
            stuart_score += points

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
