# Jesus Carlos Martinez Gonzalez
# 06/06/2023
# itertools.combinations (https://www.hackerrank.com/challenges/itertools-combinations/problem)

"""
You are given a string S.
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.
"""

from itertools import combinations

if __name__ == "__main__":
    text, size = input().split()
    text = "".join(sorted(text))
    combs = []
    for i in range(1, int(size) + 1):
        combs.extend(list(combinations(text, i)))

    combs = sorted(("".join(tup) for tup in combs), key=lambda x: (len(x), x))

    for comb in combs:
        print(comb)
