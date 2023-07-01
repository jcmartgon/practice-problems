# Jesus Carlos Martinez Gonzalez
# 01/07/2023
# Dot and Cross (https://www.hackerrank.com/challenges/np-dot-and-cross/problem)

"""
You are given two arrays: A and B.
Your task is to compute their inner and outer product.
"""

import numpy as np

if __name__ == "__main__":
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(np.inner(a, b))
    print(np.outer(a, b))
