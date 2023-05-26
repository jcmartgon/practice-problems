# Jesus Carlos Martinez Gonzalez
# 26/05/2023
# Matching Ending Items (https://www.hackerrank.com/challenges/matching-ending-items/problem)

"""
Write a RegEx to match a test string, S, under the following conditions:

S should consist of only lowercase and uppercase letters (no numbers or symbols).
S should end in s.
This is a RegEx-only challenge, so you are not required to write any code.
Simply replace the blank (_________) with your RegEx pattern.
"""

Regex_Pattern = r"^[a-zA-Z]*s"
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
