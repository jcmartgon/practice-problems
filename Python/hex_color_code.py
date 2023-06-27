# Jesus Carlos Martinez Gonzalez
# 27/06/2023
# Hex color code (https://www.hackerrank.com/challenges/hex-color-code/problem)

"""
You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
"""

import re

color_pattern = r"#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?=[;),])"

if __name__ == "__main__":
    n = int(input())
    txt = ""
    for _ in range(n):
        txt += input()
    matches = re.findall(color_pattern, txt)

    for match in matches:
        print(match)
