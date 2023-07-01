# Jesus Carlos Martinez Gonzalez
# 01/07/2023
# Min and Max (https://www.hackerrank.com/challenges/np-min-and-max/problem)

"""
You are given a 2-D array with dimensions NxM.
Your task is to perform the min function over axis 1 and then find the max of that.
"""

import numpy as np

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    arr = np.zeros((n, m), dtype="i")

    for i in range(n):
        arr[i] = [int(x) for x in input().split()]

    print(np.max(np.min(arr, axis=1)))
