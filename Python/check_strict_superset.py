# Jesus Carlos Martinez Gonzalez
# 20/06/2023
# Check Strict Superset (https://www.hackerrank.com/challenges/py-check-strict-superset/problem)

"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the n sets.

Print True, if  is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
"""

if __name__ == "__main__":
    a = set(input().split())
    n = int(input())
    strict = True
    for _ in range(n):
        b = set(input().split())
        if not b.issubset(a) or len(a) <= len(a.intersection(b)):
            strict = False
            break
    print(strict)
