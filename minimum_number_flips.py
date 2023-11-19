# Jesus Carlos Martinez Gonzalez
# 17/11/2023
# Minimum number of flips (https://www.codechef.com/problems/MINFLIPS)

"""
Chef has an array A of length N consisting of I and —I only.
In one operation, Chef can choose any index i (1 i N) and multiply the element Ai by —1.
Find the minimum number of operations required to make the sum of the array equal to 0. Output -1
if the sum of the array cannot be made O.
"""


for _ in range(int(input())):
    n = int(input())
    values = list(map(int, input().split()))

    if n % 2 != 0:
        print(-1)
    else:
        print(abs(sum(values)) // 2)
