# Jesus Carlos Martinez Gonzalez
# 27/06/2023
# Validating and Parsing Email Addresses (https://www.hackerrank.com/challenges/validating-named-email-addresses/problem)

"""
Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
"""

import email.utils
import re

email_pattern = r"[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]*\.[a-zA-Z]{1,3}"

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        name, addr = email.utils.parseaddr(input())
        if match := re.fullmatch(email_pattern, addr):
            print(f"{name} <{addr}>")
