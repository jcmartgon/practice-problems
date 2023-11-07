# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# Chessboard distance (https://www.codechef.com/problems/CHESSDIST)

"""
The Chessboard Distance for any two points (Xl, YI) and (X2, Y2) on a Cartesian plane is defined as
mac(IX1 -X21,lY1 - Y21).
You are given two points (Xl, YI) and (X2, Y2). Output their Chessboard Distance.
Note that, IPl denotes the absolute value of integer P. For example, I — 41 = 4 and 171 = 7.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(max(abs(a - c), abs(b - d)))
