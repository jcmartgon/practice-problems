# Jesus Carlos Martinez Gonzalez
# 06/06/2023
# Symmetric Difference (https://www.hackerrank.com/challenges/symmetric-difference/problem)

"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""

if __name__ == "__main__":
    m = int(input())
    a = set(map(int, input().split()))

    n = int(input())
    b = set(map(int, input().split()))

    na = a.difference(b)
    nb = b.difference(a)
    for i in sorted(na.union(nb)):
        print(i)
