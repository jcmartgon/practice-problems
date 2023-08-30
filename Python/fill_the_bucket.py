# Jesus Carlos Martinez Gonzalez
# 29/08/2023
# Fill the bucket (https://www.codechef.com/problems/FBC)

"""
Chef has a bucket having a capacity of K liters. It is already filled with X liters of water.
Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a - b)
