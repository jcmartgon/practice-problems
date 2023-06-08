# Jesus Carlos Martinez Gonzalez
# 07/06/2023
# Combinations with replacements (https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem)

"""
You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
"""

from itertools import combinations_with_replacement

if __name__ == "__main__":
    text, k = input().split()
    combs = list((combinations_with_replacement("".join(sorted(text)), int(k))))
    for comb in combs:
        print("".join(comb))
