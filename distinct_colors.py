# Jesus Carlos Martinez Gonzalez
# 14/11/2023
# Distinct colors (https://www.codechef.com/problems/DISTINCTCOL)

"""
There are N different types of colours numbered from 1 to N. Chef has Ai balls having colour i (1
Chef will arrange some boxes and put each ball in exactly one of those boxes.
Find the minimum number of boxes Chef needs so that no box contains two balls of same colour.
"""


for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    print(max(lst))
