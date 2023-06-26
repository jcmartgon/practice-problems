# Jesus Carlos Martinez Gonzalez
# 25/06/2023
# Group(), Groups(), & Groupdcit() (https://www.hackerrank.com/challenges/re-group-groups/problem)

"""
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.
"""

import re

alphanum_pattern = r"([0-9a-zA-Z])\1"

if __name__ == "__main__":
    s = input()
    if match := re.search(alphanum_pattern, s):
        print(match.group()[0])
    else:
        print(-1)
