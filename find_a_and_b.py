# Jesus Carlos Martinez Gonzalez
# 23/11/2023
# Find a and b (https://www.codechef.com/problems/FINDK3)

"""
You are given three distinct positive integers X, Y, and Z. Your task is to find integers A and B such
that:
B is equal to one of the three given numbers:
A is equal to the product of remaining two numbers;
• A is divisible by B.
Print A and B which satisfy the given conditions. If no such pair of A and B exists, print —I instead.
"""


for _ in range(int(input())):
    x, y, z = map(int, input().split())

    if (x * y) % z == 0:
        print(x * y, z)
    elif (x * z) % y == 0:
        print(x * z, y)
    elif (y * z) % x == 0:
        print(y * z, x)
    else:
        print(-1)
