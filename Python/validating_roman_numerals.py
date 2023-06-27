# Jesus Carlos Martinez Gonzalez
# 27/06/2023
# Validating Roman Numerals (https://www.hackerrank.com/challenges/validate-a-roman-number/problem)

"""
You are given a string, and you have to validate whether it's a valid Roman numeral. 
If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.
"""

regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re

print(str(bool(re.match(regex_pattern, input()))))
