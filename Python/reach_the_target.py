# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Reach the target (https://www.codechef.com/problems/REACHTARGET)

"""
There is a cricket match going on between two teams A and B.
Team B is batting second and got a target of X runs. Currently. team B has scored Y runs. Determine
how many more runs Team B should score to win the match.
Note: The target score in cricket matches is one more than the number of runs scored by the team that
batted first.
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(x - y)
