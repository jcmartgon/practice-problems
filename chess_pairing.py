# Jesus Carlos Martinez Gonzalez
# 24/12/2023
# Olympics ranking (https://www.codechef.com/problems/OLYRANK)

"""
You are hosting a chess tournament with 2N people. Exactly X of them are rated players. and the
remaining 2N — X are unrated players.
Your job is to distribute the players into N pairs, where every player plays against the person paired up
with them.
Since you want the rated players to have an advantage, you want to pair them with unrated players.
Thus, you want to minimize the number of rated players whose opponent is also rated.
Print the minimum number of rated players whose opponents are also rated, among all possible
pairings.
"""

for _ in range(int(input())):
    people, rated = map(int, input().split())
    unrated = people * 2 - rated

    print(rated - unrated if rated > unrated else 0)
