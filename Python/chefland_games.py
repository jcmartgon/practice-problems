# Jesus Carlos Martinez Gonzalez
# 21/10/2023
# Chefland games (https://www.codechef.com/problems/CHEFGAMES)

"""
In Chefland, a tennis game involves 4 referees.
Each referee has to point out whether he considers the ball to be inside limits or outside limits. The ball
is considered to be IN if and only if all the referees agree that it was inside limits.
Given the decision of the 4 referees, help Chef determine whether the ball is considered inside limits or
not.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("IN" if a + b + c + d == 0 else "OUT")
