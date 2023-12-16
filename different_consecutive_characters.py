# Jesus Carlos Martinez Gonzalez
# 15/12/2023
# Different consecutive characters (https://www.codechef.com/problems/DIFFCONSEC)

"""
Chef has a binary string S of length N. Chef can perform the following operation on S:
• Insert any character (O or 1) at any position in S.
Find the minimum number of operations Chef needs to perform so that no two consecutive characters
are same in S.
"""

for _ in range(int(input())):
    n = int(input())

    repeats = 0
    prev = ""
    for curr in input():
        if curr == prev:
            repeats += 1
        prev = curr

    print(repeats)
