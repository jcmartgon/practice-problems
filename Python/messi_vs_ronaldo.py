# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Messi vs Ronaldo (https://www.codechef.com/problems/MVR)

"""
In Chefland. a football player gets 2 points for each goal and 1 point for each assist.
Messi has A goals and B assists this season, whereas Ronaldo has X goals and Y assists.
Find out the player with more points this season.
"""

a, b, x, y = map(int, input().split())
if a * 2 + b > x * 2 + y:
    print("MESSI")
elif a * 2 + b < x * 2 + y:
    print("RONALDO")
else:
    print("EQUAL")
