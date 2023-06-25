# Jesus Carlos Martinez Gonzalez
# 24/06/2023
# Detect Floating Point Number (https://www.hackerrank.com/challenges/introduction-to-regex/problem)

"""
You are given a string N.
Your task is to verify that N is a floating point number.
"""

import re

fp_pattern = r"[+-]{0,1}\d*\.\d+"

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        f = input()
        if re.fullmatch(fp_pattern, f):
            print(True)
        else:
            print(False)
