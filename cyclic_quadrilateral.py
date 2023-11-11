# Jesus Carlos Martinez Gonzalez
# 10/11/2023
# Cyclic quadrilateral (https://www.codechef.com/problems/CYCLICQD)

"""
You are given the sizes of angles of a simple quadrilateral (in degrees) A, B, C and D, in some order
along its perimeter. Determine whether the quadrilateral is cyclic.
Note: A quadrilateral is cyclic if and only if the sum of opposite angles is 1800.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("YES" if a + c == b + d == 180 else "NO")
