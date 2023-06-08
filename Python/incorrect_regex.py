# Jesus Carlos Martinez Gonzalez
# 07/06/2023
# Incorrect Regex (https://www.hackerrank.com/challenges/incorrect-regex/problem)

"""
You are given a string S.
Your task is to find out whether S is a valid regex or not.
"""

import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        regex = input()
        try:
            re.compile(regex)
            print("True")
        except re.error:
            print("False")
