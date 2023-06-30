# Jesus Carlos Martinez Gonzalez
# 30/06/2023
# Concatenate (https://www.hackerrank.com/challenges/np-concatenate/problem)

"""
You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis .
"""

import numpy as np

if __name__ == "__main__":
    n, m, p = [int(x) for x in input().split()]
    arr1 = np.zeros((n, p), dtype=int)
    arr2 = np.zeros((m, p), dtype=int)
    for i in range(n):
        arr1[i] = [int(x) for x in input().split()]
    for i in range(m):
        arr2[i] = [int(x) for x in input().split()]
    print(np.concatenate((arr1, arr2), axis=0))
