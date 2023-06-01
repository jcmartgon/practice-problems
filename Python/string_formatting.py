# Jesus Carlos Martinez Gonzalez
# 31/05/2023
# String Formatting (https://www.hackerrank.com/challenges/python-string-formatting/problem)

"""
Given an integer, , print the following values for each integer  from  to :

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

The four values must be printed on a single line in the order specified above for each i from 1 to number. 
Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.
"""


def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1, n + 1):
        print("{n:>{w}d} {n:>{w}o} {n:>{w}X} {n:>{w}b}".format(n=i, w=w))


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
