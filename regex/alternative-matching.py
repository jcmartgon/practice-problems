# Jesus Carlos Martinez Gonzalez
# 26/05/2023
# Alternative Matching (https://www.hackerrank.com/challenges/alternative-matching/problem)

"""
Given a test string, S, write a RegEx that matches S under the following conditions:

S must start with Mr., Mrs., Ms., Dr. or Er..
The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).
"""

Regex_Pattern = r"^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
