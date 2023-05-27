# Jesus Carlos Martinez Gonzalez
# 27/05/2023
# Swap Case (https://www.hackerrank.com/challenges/swap-case/problem)

"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""


def swap_case(s):
    swapped = ""
    for c in s:
        sc = c.lower() if c.isupper() else c.upper()
        swapped += sc
    return swapped


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
