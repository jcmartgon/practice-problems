# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# Donation drive (https://www.codechef.com/problems/DONDRIVE)

"""
A blood drive aims to collect N number of blood donations.
The drive has collected X donations so far. Find the remaining number of donations needed to reach
the target.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x - y)
