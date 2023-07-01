# Jesus Carlos Martinez Gonzalez
# 01/07/2023
# Dot and Cross (https://www.hackerrank.com/challenges/np-dot-and-cross/problem)

"""
You are given two arrays A and B. Both have dimensions of NxM.
Your task is to compute their matrix product.
"""

import numpy as np

if __name__ == "__main__":
    n = int(input())
    a = np.zeros((n, n), dtype="i")
    b = np.zeros((n, n), dtype="i")

    for i in range(n):
        a[i] = [int(x) for x in input().split()]

    for i in range(n):
        b[i] = [int(x) for x in input().split()]

    print(np.dot(a, b))
