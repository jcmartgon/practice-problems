# Jesus Carlos Martinez Gonzalez
# 11/07/2023
# Maximum Element (https://www.hackerrank.com/challenges/maximum-element/problem)

"""
You have an empty sequence, and you will be given N queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

Complete the getMax function in the editor below.

getMax has the following parameters:
- string operations[n]: operations as strings   

Returns
- int[]: the answers to each type 3 query
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#


def getMax(operations):
    stack = []

    for operation in operations:
        match operation[0]:
            case "1":
                stack.insert(0, operation.split()[1])
            case "2":
                stack.pop(0)
            case "3":
                print(max(stack))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write("\n".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
