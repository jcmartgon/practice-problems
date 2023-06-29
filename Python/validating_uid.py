# Jesus Carlos Martinez Gonzalez
# 28/06/2023
# Validating UID (https://www.hackerrank.com/challenges/validating-uid/problem)

"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z, A - Z, & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
"""

import string
from collections import Counter


def main():
    for _ in range(int(input())):
        uid = input()
        print("Valid" if validate_uid(uid) else "Invalid")


def validate_uid(uid):
    if len(uid) != 10:
        return False

    valid_chars = string.digits + string.ascii_letters
    count_dict = Counter(uid)
    uppers = 0
    digits = 0

    for char, count in count_dict.items():
        if count > 1 or char not in valid_chars:
            return False
        if char in string.digits:
            digits += 1
        if char in string.ascii_uppercase:
            uppers += 1

    if digits >= 3 and uppers >= 2:
        return True
    return False


if __name__ == "__main__":
    main()
