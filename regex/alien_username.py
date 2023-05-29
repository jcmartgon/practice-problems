# Jesus Carlos Martinez Gonzalez
# 29/05/2023
# Alien Username (https://www.hackerrank.com/challenges/alien-username/problem)

"""
In a galaxy far, far away, on a planet different from ours, each computer username uses the following format:

1. It must begin with either an underscore, _ (ASCII value 95), or a period, . (ASCII value 46).
2. The first character must be immediately followed by one or more digits in the range 0 through 9.
3. After some number of digits, there must be 0 or more English letters (uppercase and/or lowercase).
4. It may be terminated with an optional _ (ASCII value 95). Note that if it's not terminated with an underscore, then there should be no characters after the sequence of 0 or more English letters.
Given  strings, determine which ones are valid alien usernames. If a string is a valid alien username, print VALID on a new line; otherwise, print INVALID.
"""

import re

username_pattern = r"(?:_|\.)\d+[a-zA-Z]*_?"

if __name__ == "__main__":
    n = int(input())
    usernames = []
    for _ in range(n):
        username = input()
        if match := re.fullmatch(username_pattern, username):
            usernames.append("VALID")
        else:
            usernames.append("INVALID")
    for username in usernames:
        print(username)
