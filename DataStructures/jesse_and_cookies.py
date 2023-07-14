# Jesus Carlos Martinez Gonzalez
# 13/07/2023
# Jesse  and Cookies (https://www.hackerrank.com/challenges/jesse-and-cookies/problem)

"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than value k.
To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

sweetness = (lx Least sweet cookie + 2x 2nd least sweet cookie).

This occurs until all the cookies have a sweetness 2 k.

Given the sweetness of a number of cookies, determine the minimum number of operations required. 
If it is not possible, return —1.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

import heapq


def cookies(k, A):
    heapq.heapify(A)
    steps = 0

    while A[0] < k and len(A) > 1:
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        heapq.heappush(A, a + 2 * b)
        steps += 1

    if A[0] >= k:
        return steps
    else:
        return -1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + "\n")

    fptr.close()
