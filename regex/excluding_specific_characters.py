# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# Excluding Specific Characters(https://www.hackerrank.com/challenges/excluding-specific-characters/problem)

"""
You have a test string S.
Your task is to write a regex that will match S with the following conditions:

S must be of length 6.
First character should not be a digit.
Second character should not be a lowercase vowel.
Third character should not be b, c, D or F.
Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
Fifth character should not be a uppercase vowel.
Sixth character should not be a . or , symbol.
"""

Regex_Pattern = r"^\D[^aeiou][^bcDF]\S[^AEIOU][^\.,]$"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
