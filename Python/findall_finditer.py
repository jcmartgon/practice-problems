# Jesus Carlos Martinez Gonzalez
# 25/06/2023
# Re.findall() & Re.finditer() (https://www.hackerrank.com/challenges/re-findall-re-finditer/problem)

"""
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.
"""

import re

pattern = r"(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])(([aeiouAEIOU]){2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])"

if __name__ == "__main__":
    s = input()
    if matches := re.findall(pattern, s):
        for match in matches:
            print(match[0])
    else:
        print(-1)
