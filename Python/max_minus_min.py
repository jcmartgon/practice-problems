# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Max minus min (https://www.codechef.com/problems/MAXDIFFMIN)

"""
Chef is given 3 integers A, B, and C such that A < B < C.
Chef needs to find the value of maa(A, B, C) — min(A, B, C).
Here mac(A, B, C) denotes the maximum value among A, B, Cwhile min(A, B, C) denotes the
minimum value among A, B, C.
"""

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    print(max(lst) - min(lst))
