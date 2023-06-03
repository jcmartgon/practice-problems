# Jesus Carlos Martinez Gonzalez
# 02/06/2023
# Polar Coordinates (https://www.hackerrank.com/challenges/polar-coordinates/problem)

"""
You are given a complex z. Your task is to convert it to polar coordinates.
"""

from cmath import polar

if __name__ == "__main__":
    comp_num = complex(input())
    r, t = polar(comp_num)

    print(r)
    print(t)
