# Jesus Carlos Martinez Gonzalez
# 06/03/2024
# First and last (https://www.codechef.com/problems/FIRSTANDLAST)

"""
You are given an array A = [A1, .42, ... , AN] of length N.
you can right rotate it any number of times (possibly, zero). What is the maximum value of A1 + AN
you can get?
Note: Right rotating the array [A1, .42, ... , AN] once gives the array [AN, A1, 442, ... , AN-I]. For
example, right rotating [1, 2, 3] once gives [3, 1, 2], and right rotating it again gives [2, 3, 11.
"""

for _ in range(int(input())):
    n = int(input())
    lst = [int(x) for x in input().split()]

    max_sum = lst[0] + lst[-1]

    for i in range(n - 1):
        curr_sum = lst[i] + lst[i + 1]
        if curr_sum > max_sum:
            max_sum = curr_sum

    print(max_sum)
