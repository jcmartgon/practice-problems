# Jesus Carlos Martinez Gonzalez
# 29/05/2023
# String Validators (https://www.hackerrank.com/challenges/string-validators/problem)

"""
You are given a string S.

Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""


if __name__ == "__main__":
    s = input()
    print(any(ss.isalnum() for ss in s))
    print(any(ss.isalpha() for ss in s))
    print(any(ss.isdigit() for ss in s))
    print(any(ss.islower() for ss in s))
    print(any(ss.isupper() for ss in s))
