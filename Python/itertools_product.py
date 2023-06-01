# Jesus Carlos Martinez Gonzalez
# 01/06/2023
# itertools.product (https://www.hackerrank.com/challenges/itertools-product/problem)

"""
itertools.product()

This tool computes the cartesian product of input iterables.

You are given a two lists A and B. Your task is to compute their cartesian product AxB.
"""

from itertools import product

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for tpl in product(a, b):
        print(tpl, end=" ")
    print()
