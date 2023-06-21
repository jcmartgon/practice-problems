# Jesus Carlos Martinez Gonzalez
# 20/06/2023
# Check Subset(https://www.hackerrank.com/challenges/py-check-subset/problem)

"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
"""

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = set(input().split())
        m = int(input())
        b = set(input().split())

        print(a.issubset(b))
