# Jesus Carlos Martinez Gonzalez
# 27/05/2023
# Positivie Loockbehind (https://www.hackerrank.com/challenges/positive-lookbehind/problem)

"""
You have a test String S.
Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.
"""

Regex_Pattern = r"(?<=[13579])\d"  # Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
