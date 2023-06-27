# Jesus Carlos Martinez Gonzalez
# 27/06/2023
# Validating Phone Numbers (https://www.hackerrank.com/challenges/validating-the-phone-number/problem)

"""
Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7, 8 or 9.
"""

mn_patern = r"^[789]\d{9}$"

import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        mn = input()
        print("YES" if re.match(mn_patern, mn) else "NO")
