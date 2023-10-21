# Jesus Carlos Martinez Gonzalez
# 20/10/2023
# Minimum pizzas (https://www.codechef.com/problems/MINPIZZA?tab=submissions)

"""
Each pizza consists of 4 slices. There are N friends and each friend needs exactly X slices.
Find the minimum number of pizzas they should order to satisfy their appetite.
Input Format
• The first line of input will contain a single integer T, denoting the number of test cases.
• Each test case consists of two integers N and X the number of friends and the number of slices
each friend wants respectively.
"""

from math import ceil

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(ceil((a * b) / 4))
