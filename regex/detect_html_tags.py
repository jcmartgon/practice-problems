# Jesus Carlos Martinez Gonzalez
# 28/05/2023
# Detecting HTML Tags (https://www.hackerrank.com/challenges/detect-html-tags)

"""
Given N lines of HTML, find the tag names (ignore any attributes) and print them as a single line of lexicographically ordered semicolon-separated values (e.g.:tag1;tag2;tag3).
"""

regex_pattern = r"<\/?([a-z0-9]+) ?"

import re

if __name__ == "__main__":
    N = int(input())

    matches = []
    for i in range(N):
        line = input()
        matches.append(re.findall(regex_pattern, line))

matches = [item for sublist in matches for item in sublist]
matches = sorted(set(matches))
print(";".join(match for match in matches))
