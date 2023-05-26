# Jesus Carlos Martinez Gonzalez
# 26/05/2023
# Capturing and non-capturing groups (https://www.hackerrank.com/challenges/capturing-non-capturing-groups/problem)

"""
You have a test String S.
Your task is to write a regex which will match S with the following condition:

S should have  or more consecutive repetitions of ok.
"""

Regex_Pattern = r"(?:ok){3,}"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
