# Jesus Carlos Martinez Gonzalez
# 11/06/2023
# Mod Divmod (https://www.hackerrank.com/challenges/py-set-intersection-operation/problem)

"""
Read in two integers, a and b, and print three lines.
The first line is the integer division a//b.
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b.
"""

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(a // b)
    print(a % b)
    print(divmod(a, b))
