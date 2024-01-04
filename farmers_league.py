# Jesus Carlos Martinez Gonzalez
# 03/01/2024
# Farmers league (https://www.codechef.com/problems/LEAGUE)

"""
A football league of N teams is taking place, where each team plays other teams once in single round
robin fashion. A team gets 3 points for winning a game and 0 for losing (assume that no games end in a
draw/tie). What is the maximum possible difference of points between the winning team and the
second-placed team?
"""

for _ in range(int(input())):
    n = int(input())
    matches = n - 1

    print(matches * 3 - matches // 2 * 3)
