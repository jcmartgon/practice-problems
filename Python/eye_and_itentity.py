# Jesus Carlos Martinez Gonzalez
# 30/06/2023
# Eye and Identity (https://www.hackerrank.com/challenges/np-eye-and-identity/problem)

"""
Your task is to print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.
"""

import numpy as np

np.set_printoptions(legacy="1.13")


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    print(np.eye(n, m, k=0))
