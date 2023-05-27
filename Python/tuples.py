# Jesus Carlos Martinez Gonzalez
# 27/05/2023
# Tuples (https://www.hackerrank.com/challenges/python-tuples/problem)

"""
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those  integers. Then compute and print the result of hash(t).
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))
