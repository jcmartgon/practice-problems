# Jesus Carlos Martinez Gonzalez
# 16/12/2023
# Find the direction (https://www.codechef.com/problems/FACEDIR)

"""
Chef is currently facing the north direction. Each second he rotates exactly 90 degrees in clockwise
direction. Find the direction in which Chef is facing after exactly X seconds.
Note : There are only 4 directions: North, East South, West (in clockwise order).
"""

for _ in range(int(input())):
    directions = ["North", "East", "South", "West"]

    print(directions[int(input()) % 4])
