# Jesus Carlos Martinez Gonzalez
# 02/03/2024
# Largest and second largest (https://www.codechef.com/problems/LARGESECOND)

"""
You are given an array A of N integers.
Find the maximum sum of two distinct integers in the array.
Note: It is guaranteed that there exist at least two distinct integers in the array.
"""

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1

    x = y = 0

    for i in a:
        if i > x:
            x = i

    for i in a:
        if i > y and i != x:
            y = i

    print(x + y)
