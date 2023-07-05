# Jesus Carlos Martinez Gonzalez
# 04/07/2023
# Arrays DS (https://www.hackerrank.com/challenges/arrays-ds/problem)

"""
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. 
In an array, A, of size N, each memory location has some unique index, i (where 0 <= i <= N), that can be referenced as A[i] or Ai.

Reverse an array of integers
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def reverseArray(a):
    return a[::-1]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(" ".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
