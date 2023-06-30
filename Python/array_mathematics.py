# Jesus Carlos Martinez Gonzalez
# 30/06/2023
# Array Mathematics (https://www.hackerrank.com/challenges/np-array-mathematics/problem)

"""
You are given two integer arrays, A and B of dimensions NxM.
Your task is to perform the following operations:

Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)
"""

import numpy as np

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    a = np.zeros((n, m), int)
    b = np.zeros((n, m), int)

    for i in range(n):
        a[i] = [float(x) for x in input().split()]
    for i in range(n):
        b[i] = [float(x) for x in input().split()]

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a**b)
