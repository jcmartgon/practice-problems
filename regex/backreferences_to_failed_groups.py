# Jesus Carlos Martinez Gonzalez
# 27/05/2023
# Backreferences to Failed Groups (https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem)

"""
You have a test string S.
Your task is to write a regex which will match S, with following condition(s):

S consists of 8 digits.
S may have "-" separator such that string  gets divided in  parts, with each part having exactly two digits. (Eg. 12-34-56-78)
"""

Regex_Pattern = r"^\d{2}(-?)(\d{2}\1){2}\d{2}$"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
