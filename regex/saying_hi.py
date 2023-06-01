# Jesus Carlos Martinez Gonzalez
# 01/06/2023
# Saying Hi (https://www.hackerrank.com/challenges/saying-hi/problem)

"""
Given a sentence, S, write a RegEx to match the following criteria:

The first character must be the letter H or h.
The second character must be the letter I or i.
The third character must be a single space (i.e.: \s).
The fourth character must not be the letter D or d.
Given  lines of sentences as input, print each sentence matching your RegEx on a new line.
"""

import re

hi_pattern = r"^[Hh][Ii]\s(?![Dd]).+"

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        text = input()
        if match := re.match(hi_pattern, text):
            print(text)
