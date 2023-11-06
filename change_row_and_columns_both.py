# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Change row and column both (https://www.codechef.com/problems/CHANGEPOS)

"""
There is a IO x 10 grid with rows numbered 1 to 10 from top to bottom. and columns 1 to 10 from left
to right. Each cell is identified by a pair (r, c) which means that the cell is located at row rand column
c.
If Chef's current location is (a, b), then in one move Chef can go to (c, d) if both of the following are
satisfied:
Determine the minimum number of moves required to go from (Sa, Sy) to (Q, ey).
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(1 if a != c and b != d else 2)
