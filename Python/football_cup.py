# Jesus Carlos Martinez Gonzalez
# 27/08/2023
# Football cup (https://www.codechef.com/problems/FOOTCUP)

"""
It is the final day of La Liga. Chef has a certain criteria for assessing football matches.
In particular, he only likes a match if:
• The match ends in a draw, and,
• At least one goal has been scored by either team.
Given the goals scored by both the teams as X and Y respectively, determine whether Chef will like
the match or not.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if a == b and a > 0 else "NO")
