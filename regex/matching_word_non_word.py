# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# Matching Word & Non-Word Character (https://www.hackerrank.com/challenges/matching-word-non-word/problem)

"""
You have a test string . Your task is to match the pattern xxxXxxxxxxxxxxXxxx
Here x denotes any word character and X denotes any non-word character.
"""

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
