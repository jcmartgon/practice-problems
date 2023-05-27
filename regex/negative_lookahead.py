# Jesus Carlos Martinez Gonzalez
# 27/05/2023
# Negative Lookahead (https://www.hackerrank.com/challenges/negative-lookahead/problem)

"""
You have a test String S.
Write a regex which can match all characters which are not immediately followed by that same character.
"""

Regex_Pattern = r"(.)(?!\1)"  # Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
