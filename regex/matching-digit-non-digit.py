# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# Matching Digit & Non-Digit Characters (https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem?isFullScreen=true)

"""
You have a test string S. Your task is to match the pattern xxXxxXxxxx
Here x denotes a digit character, and X denotes a non-digit character.
"""

Regex_Pattern = r"(?:\d\d\D){2}\d{4}"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
