# Jesus Carlos Martinez Gonzalez
# 01/07/2023
# Sum and Prod (https://www.hackerrank.com/challenges/np-sum-and-prod/problem)

"""
You are given a 2-D array with dimensions NxM.
Your task is to perform the  tool over axis sum and then find the prod of that result.
"""

import numpy as np

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    arr = np.zeros((n, m), dtype=int)

    for i in range(n):
        arr[i] = input().split()

    print(np.prod(np.sum(arr, axis=0)))
