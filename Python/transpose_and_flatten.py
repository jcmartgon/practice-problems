# Jesus Carlos Martinez Gonzalez
# 30/06/2023
# Transpose and Flatten (https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem)

"""
You are given a NxM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.
"""

import numpy as np

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    arr = np.zeros((n, m), dtype=int)
    for i in range(n):
        arr[i] = [int(x) for x in input().split()]
    print(np.transpose(arr))
    print(arr.flatten())
