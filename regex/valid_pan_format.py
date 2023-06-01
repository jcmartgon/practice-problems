# Jesus Carlos Martinez Gonzalez
# 31/05/2023
# Valid PAN Format (https://www.hackerrank.com/challenges/valid-pan-format/problem)

"""
The equivalent of SSN in India is a PAN number, which is unique to each of its citizens. In any of the country's official documents, the PAN number is listed as follows

<char><char><char><char><char><digit><digit><digit><digit><char>

Your task is to figure out if the PAN number is valid or not. A valid PAN number will have all its letters in uppercase and digits in the same order as listed above.
"""

import re

pan_pattern = r"[A-Z]{5}\d{4}[A-Z]"

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        pan_text = input()
        if re.fullmatch(pan_pattern, pan_text):
            print("YES")
        else:
            print("NO")
