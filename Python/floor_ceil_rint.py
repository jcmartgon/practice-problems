# Jesus Carlos Martinez Gonzalez
# 01/07/2023
# Floor, Ceil, and Rint (https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem)

"""
You are given a 1-D array, A. Your task is to print the floor, ceil, and rint of all the elements of A.
"""

import numpy as np

np.set_printoptions(legacy="1.13")


if __name__ == "__main__":
    a = np.array([float(x) for x in input().split()])
    print(np.floor(a), np.ceil(a), np.rint(a), sep="\n")
