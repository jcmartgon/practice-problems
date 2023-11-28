# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Chess format (https://www.codechef.com/problems/CHSFORMT)

"""
Given the time control of a chess match as a + b, determine which format of chess out of the given 4 it
belongs to.
I) Bullet if a+ b < 3
2) Blitz if 3 a+ b f IO
3) Rapid if 11 a+ b S 60
4) Classical if 60 < a+ b
"""


for _ in range(int(input())):
    a, b = map(int, input().split())

    c = a + b

    print(1 if c < 3 else 2 if 3 <= c <= 10 else 3 if 11 <= c <= 60 else 4)
