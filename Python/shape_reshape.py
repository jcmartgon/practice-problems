# Jesus Carlos Martinez Gonzalez
# 29/06/2023
# Shape and Reshape (https://www.hackerrank.com/challenges/np-shape-reshape/problem)

"""
You are given a space separated list of nine integers. Your task is to convert this list into a 3x3 NumPy array.
"""

import numpy


if __name__ == "__main__":
    arr = numpy.array(input().split(), int)
    print(numpy.reshape(arr, (3, 3)))
