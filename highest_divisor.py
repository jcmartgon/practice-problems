# Jesus Carlos Martinez Gonzalez
# 03/12/2023
# Highest divisor (https://www.codechef.com/problems/HDIVISR)

"""
You are given an integer N. Find the largest integer between 1 and 10 (inclusive) which divides N.
"""

n = int(input())

for i in range(10, 0, -1):
    if n % i == 0:
        print(i)
        break
