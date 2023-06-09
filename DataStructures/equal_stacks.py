# Jesus Carlos Martinez Gonzalez
# 10/07/2023
# Equal Stacks (https://www.hackerrank.com/challenges/equal-stacks/problem)

"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. 
You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#


def equalStacks(h1, h2, h3):
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)

    while True:
        min_height = min(s1, s2, s3)

        if min_height == 0:
            return 0

        if s1 > min_height:
            s1 -= h1.pop(0)

        if s2 > min_height:
            s2 -= h2.pop(0)

        if s3 > min_height:
            s3 -= h3.pop(0)

        if s1 == s2 == s3:
            return s1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + "\n")

    fptr.close()
