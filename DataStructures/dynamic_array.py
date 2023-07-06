# Jesus Carlos Martinez Gonzalez
# 05/07/2023
# Dynamic Array (https://www.hackerrank.com/challenges/dynamic-array/problem)

"""
- Declare a 2-dimensional array, arr. of n empty arrays. All arrays are zero indexed.
- Declare an integer, last Answer, and initialize it to O.
- There are 2 types of queries, given as an array of strings for you to parse:
    1. Query: 1 x y
        1. Let idx = ( (r ^ lastAnswer) % n ).
        2. Append the integer y to arr[idxl.
2. Query: 2 x y
    1. Let idx = (x ^ lastAnswer) % n ).
    2. Assign the value arr[idx][y % size(arr[idx])] to lastAnswer.
    3. Store the new value of last Answer to an answers array.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    answers = []

    for query in queries:
        t, x, y = query

        idx = (x ^ last_answer) % n
        if t == 1:
            arr[idx].append(y)
        else:
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)

    return answers


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
