# Jesus Carlos Martinez Gonzalez
# 04/07/2023
# 2D Array - DS (https://www.hackerrank.com/challenges/2d-array/problem)

"""
Given a 6x6 2D Array, arr:

An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:

There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6x6.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    sums = []

    for i in range(4):
        for j in range(1, 5):
            sums.append(
                arr[i][j - 1]
                + arr[i][j]
                + arr[i][j + 1]
                + arr[i + 1][j]
                + arr[i + 2][j - 1]
                + arr[i + 2][j]
                + arr[i + 2][j + 1]
            )
    return max(sums)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
