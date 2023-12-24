# Jesus Carlos Martinez Gonzalez
# 23/12/2023
# Olympics ranking (https://www.codechef.com/problems/OLYRANK)

"""
In Olympics, the countries are ranked by the total number of medals won. You are given six integers
GI, Sl, Bl, and G2, .52, B2, the number of gold, silver and bronze medals won by two different
countries respectively. Determine which country is ranked better on the leaderboard. It is guaranteed
that there will not be a tie between the two countries.
"""

for _ in range(int(input())):
    gold1, silver1, bronze1, gold2, silver2, bronze2 = map(int, input().split())

    one = gold1 + silver1 + bronze1
    two = gold2 + silver2 + bronze2

    print(1 if one > two else 2)
