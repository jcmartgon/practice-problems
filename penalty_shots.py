# Jesus Carlos Martinez Gonzalez
# 01/03/2024
# Penalty shots (https://www.codechef.com/problems/PENALTY)

"""
It's the soccer match finals in Chefland and as always it has reached the penalty shotouts. Each team is
given 5 shots to make and the team scoring a goal on the maximum number of shots wins the game. If
both the teams' scores are equal, then the game is considered a draw and we would have 2
champions.
Given ten integers A1, .42, ... , AIO. where the odd indexed integers(A1, .43, A5, AT, A9) represent
the outcome of the shots made by team 1 and even indexed integers(A2, 244, A6, .48, AIO) represent
the outcome of the shots made by team 2 (here Ai = 1 indicates that it's a goal and Ai = 0 indicates a
miss), determine the winner or find if the game ends in a draw.
"""

for _ in range(int(input())):
    shots = list(map(int, input().split()))

    a = sum([s for i, s in enumerate(shots) if (i + 1) % 2 != 0])
    b = sum(shots) - a

    print(1 if a > b else 2 if a < b else 0)
