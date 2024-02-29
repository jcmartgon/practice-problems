# Jesus Carlos Martinez Gonzalez
# 27/02/2024
# Problem (https://www.codechef.com/problems/TWORANGES)

"""
Chef has two ranges [A, B] and [C, D]. Chef needs to find the number of integers that belong to at
least one of the ranges.
Note: A range [P, Q] contains all the integers {P, P + 1, P + 2,... ,
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    lst = list(range(a, b + 1))
    lst.append(list(range(c, d + 1)))
    st = set(lst)

    print(len(st))
