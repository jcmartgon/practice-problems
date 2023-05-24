# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# Matching Specific String (https://www.hackerrank.com/challenges/matching-specific-string/problem?isFullScreen=true)

"""
You have a test string S. Your task is to match the string hackerrank. This is case sensitive.
"""

Regex_Pattern = r"hackerrank"  # Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
