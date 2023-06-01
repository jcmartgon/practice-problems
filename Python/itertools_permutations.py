# Jesus Carlos Martinez Gonzalez
# 01/06/2023
# itertools.permutations (https://www.hackerrank.com/challenges/itertools-permutations/problem)

"""
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
"""

from itertools import permutations

if __name__ == "__main__":
    text, k = input().split()
    print("\n".join(sorted(map("".join, permutations(text, int(k))))))
