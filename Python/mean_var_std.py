# Jesus Carlos Martinez Gonzalez
# 01/07/2023
# Mean, Var, and Std (https://www.hackerrank.com/challenges/np-mean-var-and-std/problem)

"""
You are given a 2-D array of size NxM.
Your task is to find:

1. The mean along axis 1
2. The var along axis 0
3. The std along axis None
"""

import numpy as np

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    arr = np.zeros((n, m), dtype="i")

    for i in range(n):
        arr[i] = [int(x) for x in input().split()]

    print(np.mean(arr, axis=1), np.var(arr, axis=0), round(np.std(arr), 11), sep="\n")
