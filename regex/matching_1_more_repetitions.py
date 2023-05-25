# Jesus Carlos Martinez Gonzalez
# 25/05/23
# Matching 1 or more repetitions (https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem?isFullScreen=true)

"""
You have a test string S.
Your task is to write a regex that will match  using the following conditions:

* S should begin with 1 or more digits.
* After that,  should have 1 or more uppercase letters.
* S should end with 1 or more lowercase letters.
"""

Regex_Pattern = r"^\d+[A-Z]+[a-z]+$"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
