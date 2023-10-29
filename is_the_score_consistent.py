# Jesus Carlos Martinez Gonzalez
# 28/10/2023
# Is the score consistent (https://www.codechef.com/problems/TRUESCORE)

"""
Chef is watching a football match. The current score is A : B, that is, team I has scored A goals and
team 2 has scored B goals. Chefwonders if it is possible for the score to become C : D ata later point
in the game (i.e. team 1 has scored C goals and team 2 has scored D goals). Can you help Chef by
answering his question?
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print("POSSIBLE" if c >= a and d >= b else "IMPOSSIBLE")
