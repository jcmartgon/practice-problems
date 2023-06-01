# Jesus Carlos Martinez Gonzalez
# 01/06/2023
# Splitting Phone Numbers (https://www.hackerrank.com/challenges/split-number/problem)

"""
There is a list of phone numbers which needs the attention of a text processing expert. As an expert in regular expressions, you are being roped in for the task. A phone number directory can reveal a lot such as country codes and local area codes. The only constraint is that one should know how to process it correctly.

A Phone number is of the following format

[Country code]-[Local Area Code]-[Number]  

There might either be a '-' ( ascii value 45), or a ' ' ( space, ascii value 32) between the segments
Where the country and local area codes can have 1-3 numerals each and the number section can have 4-10 numerals each.

And so, if we tried to apply the a regular expression with groups on this phone number: 1-425-9854706

We'd get:
Group 1 = 1
Group 2 = 425
Group 3 = 9854706

You will be provided a list of N phone numbers which conform to the pattern described above. Your task is to split it into the country code, local area code and the number.
"""

import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        phone = input()
        if match := re.fullmatch(r"(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})", phone):
            print(
                f"CountryCode={match.group(1)},LocalAreaCode={match.group(2)},Number={match.group(3)}"
            )
