# Jesus Carlos Martinez Gonzalez
# 27/06/2023
# re.start() & re.end() (https://www.hackerrank.com/challenges/re-start-re-end/problem)

"""
You are given a string S.
Your task is to find the indices of the start and end of string K in S.
"""

import re

if __name__ == "__main__":
    s = input()
    k = input()
    l = len(k) - 1
    pattern = re.compile(f"(?=({(k)}))")

    matches = pattern.finditer(s)

    try:
        nxt = next(matches)
        start = nxt.start()
        end = start + l
        print((start, end))
    except StopIteration:
        print((-1, -1))

    for match in matches:
        start = match.start()
        end = start + l
        print((start, end))
